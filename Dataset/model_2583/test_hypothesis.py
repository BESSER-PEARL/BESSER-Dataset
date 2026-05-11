import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    triplet,
    afpText::CGCSGID,
    afpText::SetBiLevelImageColor,
    afpText::GSPCOL,
    afpText::GBIMG,
    afpText::BandImage,
    afpText::ObjectByteOffset,
    afpText::GSMC,
    afpText::AttributeQualifier,
    afpText::ObjectStructuredFieldOffset,
    afpText::ObjectCount,
    afpText::GSMX,
    afpText::EndImage,
    afpText::FontResolution,
    afpText::EndTile,
    afpText::GSGCH,
    afpText::ColorFidelity,
    afpText::IDESize,
    afpText::EncodingSchemeID,
    afpText::GSAP,
    afpText::GCCBEZ,
    afpText::GSECOL,
    afpText::GSCS,
    afpText::MediaEjectControl,
    afpText::BeginTransparencyMask,
    afpText::GSMS,
    afpText::GEPROL,
    afpText::ObjectFunctionSetSpecification,
    afpText::FontCodedGraphicCharacterSetGlobalIdentifier,
    afpText::GCHST,
    afpText::PagePositionInformation,
    afpText::ColorSpecification,
    afpText::TBM,
    afpText::GIMD,
    afpText::GSMP,
    afpText::GCBEZ,
    afpText::MetricAdjustment,
    afpText::ObjectContainerPresentationSpaceSize,
    afpText::ResourceLocalIdentifier,
    afpText::PresentationControl,
    afpText::ExtendedResourceLocalIdentifier,
    afpText::ColorManagementResourceDescriptor,
    afpText::GCCHST,
    afpText::LineDataObjectPositionMigration,
    afpText::GSCP,
    afpText::GCOMT,
    afpText::GBAR,
    afpText::FNNRG2,
    afpText::BLN,
    afpText::GSFLW,
    afpText::GSLT,
    afpText::ObjectByteExtent,
    afpText::GSBMX,
    afpText::USC,
    afpText::FinishingFidelity,
    afpText::ObjectClassification,
    afpText::IOCAFunctionSetIdentification,
    afpText::BandImageData,
    afpText::FontFidelity,
    afpText::BSU,
    afpText::TileSize,
    afpText::DrawingOrderSubset,
    afpText::WindowSpecification,
    afpText::TilePosition,
    afpText::GCLINE,
    afpText::GSPT,
    afpText::FontDescriptorSpecification,
    afpText::BeginSegmentCommand,
    afpText::DeviceAppearance,
    afpText::IncludeTile,
    afpText::TextFidelity,
    afpText::CRCResourceManagement,
    afpText::PageOverlayConditionalProcessing,
    afpText::GPARC,
    afpText::ImageSubsampling,
    afpText::TileSetColor,
    afpText::GSMT,
    afpText::FontHorizontalScaleFactor,
    afpText::GCRLINE,
    afpText::CMRFidelity,
    afpText::GCMRK,
    afpText::ExtensionFont,
    afpText::EndTransparencyMask,
    afpText::MediumOrientation,
    afpText::GMRK,
    afpText::ImageResolution,
    afpText::EndSegment,
    afpText::MediumMapPageNumber,
    afpText::GCFLT,
    afpText::SamplingRatios,
    afpText::GSCR,
    afpText::GSCC,
    afpText::MappingOption,
    afpText::LocalDateAndTimeStamp,
    afpText::GSCA,
    afpText::ObjectOffset,
    afpText::FullyQualifiedName,
    afpText::ImageData,
    afpText::ObjectOriginIdentifier,
    afpText::GSLJ,
    afpText::GFLT,
    afpText::GSLE,
    afpText::GFARC,
    afpText::ImageLUTID,
    afpText::GEIMG,
    afpText::MediaFidelity,
    afpText::MODCAInterchangeSet,
    afpText::GRLINE,
    afpText::EndSegmentCommand,
    afpText::GCBOX,
    afpText::ObjectStructuredFieldExtent,
    afpText::BeginTile,
    afpText::GCPARC,
    afpText::GNOP1,
    afpText::LocaleSelector,
    afpText::RenderingIntent,
    afpText::PresentationSpaceResetMixing,
    afpText::UP3iFinishingOperation,
    afpText::GEAR,
    afpText::ResourceUsageAttribute,
    afpText::GCFARC,
    afpText::ImageSize,
    afpText::PresentationSpaceMixingRules,
    afpText::ResourceObjectInclude,
    afpText::IDEStructure,
    afpText::TextOrientation,
    afpText::GLINE,
    afpText::GSLW,
    afpText::GSCD,
    afpText::ObjectAreaSize,
    afpText::GSCOL,
    afpText::GBOX,
    afpText::DataObjectFontDescriptor,
    afpText::GCBIMG,
    afpText::TonerSaver,
    afpText::TileTOC,
    afpText::Comment,
    afpText::BeginSegment,
    afpText::GSPS,
    afpText::ResourceSectionNumber,
    afpText::ExternalAlgorithm,
    afpText::BeginImage,
    afpText::AMI,
    afpText::GSCH,
    afpText::TRN,
    afpText::FinishingOperation,
    afpText::ImageEncoding,
    afpText::MeasurementUnits,
    afpText::AttributeValue,
    afpText::UniversalDateAndTimeStamp,
    afpText::CharacterRotation,
    afpText::DescriptorPosition,
    afpText::ResourceObjectType,
    afpText::AMB,
    afpText::SVI,
    afpText::STO,
    afpText::STC,
    afpText::SIM,
    afpText::SIA,
    afpText::SEC,
    afpText::SCFL,
    afpText::SBI,
    afpText::RPS,
    afpText::RMI,
    afpText::RMB,
    afpText::OVS,
    afpText::NOPCS,
    afpText::ESU,
    afpText::DIR,
    afpText::DBR,
    afpText::GCRLINERG,
    afpText::GRLINERG,
    afpText::GCMRKRG,
    afpText::GMRKRG,
    afpText::GCLINERG,
    afpText::triplet,
    structuredField,
    afpText::BCF,
    afpText::BDX,
    afpText::BFN,
    afpText::BGR,
    afpText::BOC,
    afpText::BFG,
    afpText::BII,
    afpText::BFM,
    afpText::BMM,
    afpText::BAG,
    afpText::BCP,
    afpText::BIM,
    afpText::BMO,
    afpText::BDD,
    afpText::BDA,
    afpText::BBC,
    afpText::BDI,
    afpText::BDM,
    afpText::BDG,
    afpText::BCA,
    afpText::BOG,
    afpText::BDT,
    afpText::BNG,
    afpText::BPF,
    afpText::LineData,
    afpText::structuredField,
    afpText::Model,
    afpText::GLINERG,
    afpText::GCFLTRG,
    afpText::GFLTRG,
    afpText::GCCBEZRG,
    afpText::GCBEZRG,
    afpText::FNNRG,
    afpText::ExternalAlgorithmRG,
    afpText::SamplingRatiosRG,
    afpText::TileTOCRG,
    afpText::BandImageRG,
    afpText::TLE,
    afpText::PTX,
    afpText::FGD,
    afpText::PGP,
    afpText::PTD1,
    afpText::PTD,
    afpText::PPORG,
    afpText::PPO,
    afpText::PMC,
    afpText::PGP1,
    afpText::PGPRG,
    afpText::NOP,
    afpText::MSURG,
    afpText::MSU,
    afpText::PGD,
    afpText::PFC,
    afpText::PEC,
    afpText::OCD,
    afpText::OBP,
    afpText::OBD,
    afpText::MGO,
    afpText::MPSRG,
    afpText::MPS,
    afpText::MPORG,
    afpText::MPO,
    afpText::MPGRG,
    afpText::MPG,
    afpText::MMTRG,
    afpText::MMT,
    afpText::MMORG,
    afpText::MMO,
    afpText::MMDRG,
    afpText::MMD,
    afpText::MMCRG,
    afpText::MMC,
    afpText::MIORG,
    afpText::MIO,
    afpText::MGORG,
    afpText::MCC,
    afpText::MCARG,
    afpText::MCA,
    afpText::MFC,
    afpText::MDRRG,
    afpText::MDR,
    afpText::MDD,
    afpText::MCF1RG,
    afpText::MCF1,
    afpText::MCFRG,
    afpText::MCF,
    afpText::MCDRG,
    afpText::MCD,
    afpText::MCCRG,
    afpText::LLE,
    afpText::MBCRG,
    afpText::MBC,
    afpText::LND,
    afpText::LNC,
    afpText::LLERG,
    afpText::IPO,
    afpText::IRD,
    afpText::IPS,
    afpText::IPG,
    afpText::IPD,
    afpText::ICP,
    afpText::IOC,
    afpText::IOB,
    afpText::IMM,
    afpText::IID,
    afpText::IEL,
    afpText::IDD,
    afpText::GDD,
    afpText::GAD,
    afpText::FNPRG,
    afpText::FNP,
    afpText::FNORG,
    afpText::FNO,
    afpText::FNMRG,
    afpText::FNM,
    afpText::FNN,
    afpText::FNIRG,
    afpText::FNI,
    afpText::FNG,
    afpText::EPT,
    afpText::FND,
    afpText::FNC,
    afpText::ESG,
    afpText::ERS,
    afpText::ERG,
    afpText::EIM,
    afpText::EPS,
    afpText::EPM,
    afpText::EPG,
    afpText::EPF,
    afpText::EOG,
    afpText::EOC,
    afpText::ENG,
    afpText::EMO,
    afpText::EMM,
    afpText::EII,
    afpText::EGR,
    afpText::EFN,
    afpText::EFM,
    afpText::EFG,
    afpText::EDX,
    afpText::EDT,
    afpText::EDM,
    afpText::EDI,
    afpText::EDG,
    afpText::ECP,
    afpText::ECF,
    afpText::ECA,
    afpText::EBC,
    afpText::EAG,
    afpText::DXD,
    afpText::BRG,
    afpText::CTC,
    afpText::CPIRG,
    afpText::CPI,
    afpText::CPD,
    afpText::CPC,
    afpText::CFIRG,
    afpText::CFI,
    afpText::CFC,
    afpText::CDD,
    afpText::CAT,
    afpText::BSG,
    afpText::BRS,
    afpText::BPT,
    afpText::BPS,
    afpText::BPM,
    afpText::BPG,
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



def test_afptext::cgcsgid_is_not_abstract():
    assert not inspect.isabstract(afpText::CGCSGID)


def test_afptext::cgcsgid_constructor_exists():
    assert callable(afpText::CGCSGID.__init__)


def test_afptext::cgcsgid_constructor_args():
    sig = inspect.signature(afpText::CGCSGID.__init__)
    params = list(sig.parameters.keys())
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"
    assert "CPGID" in params, "Missing parameter 'CPGID'"

def test_afptext::cgcsgid_has_GCSGID():
    assert hasattr(afpText::CGCSGID, "GCSGID")
    descriptor = None
    for klass in afpText::CGCSGID.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cgcsgid_has_CPGID():
    assert hasattr(afpText::CGCSGID, "CPGID")
    descriptor = None
    for klass in afpText::CGCSGID.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::setbilevelimagecolor_is_not_abstract():
    assert not inspect.isabstract(afpText::SetBiLevelImageColor)


def test_afptext::setbilevelimagecolor_constructor_exists():
    assert callable(afpText::SetBiLevelImageColor.__init__)


def test_afptext::setbilevelimagecolor_constructor_args():
    sig = inspect.signature(afpText::SetBiLevelImageColor.__init__)
    params = list(sig.parameters.keys())
    assert "NAMECOLR" in params, "Missing parameter 'NAMECOLR'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "AREA" in params, "Missing parameter 'AREA'"

def test_afptext::setbilevelimagecolor_has_NAMECOLR():
    assert hasattr(afpText::SetBiLevelImageColor, "NAMECOLR")
    descriptor = None
    for klass in afpText::SetBiLevelImageColor.__mro__:
        if "NAMECOLR" in klass.__dict__:
            descriptor = klass.__dict__["NAMECOLR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::setbilevelimagecolor_has_Reserved():
    assert hasattr(afpText::SetBiLevelImageColor, "Reserved")
    descriptor = None
    for klass in afpText::SetBiLevelImageColor.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::setbilevelimagecolor_has_AREA():
    assert hasattr(afpText::SetBiLevelImageColor, "AREA")
    descriptor = None
    for klass in afpText::SetBiLevelImageColor.__mro__:
        if "AREA" in klass.__dict__:
            descriptor = klass.__dict__["AREA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gspcol_is_not_abstract():
    assert not inspect.isabstract(afpText::GSPCOL)


def test_afptext::gspcol_constructor_exists():
    assert callable(afpText::GSPCOL.__init__)


def test_afptext::gspcol_constructor_args():
    sig = inspect.signature(afpText::GSPCOL.__init__)
    params = list(sig.parameters.keys())
    assert "RES2" in params, "Missing parameter 'RES2'"
    assert "RES1" in params, "Missing parameter 'RES1'"
    assert "COLSPCE" in params, "Missing parameter 'COLSPCE'"
    assert "COLSIZE3" in params, "Missing parameter 'COLSIZE3'"
    assert "COLSIZE4" in params, "Missing parameter 'COLSIZE4'"
    assert "COLSIZE2" in params, "Missing parameter 'COLSIZE2'"
    assert "COLVALUE" in params, "Missing parameter 'COLVALUE'"
    assert "COLSIZE1" in params, "Missing parameter 'COLSIZE1'"

def test_afptext::gspcol_has_RES2():
    assert hasattr(afpText::GSPCOL, "RES2")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "RES2" in klass.__dict__:
            descriptor = klass.__dict__["RES2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_RES1():
    assert hasattr(afpText::GSPCOL, "RES1")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "RES1" in klass.__dict__:
            descriptor = klass.__dict__["RES1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLSPCE():
    assert hasattr(afpText::GSPCOL, "COLSPCE")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLSPCE" in klass.__dict__:
            descriptor = klass.__dict__["COLSPCE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLSIZE3():
    assert hasattr(afpText::GSPCOL, "COLSIZE3")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLSIZE3" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLSIZE4():
    assert hasattr(afpText::GSPCOL, "COLSIZE4")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLSIZE4" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLSIZE2():
    assert hasattr(afpText::GSPCOL, "COLSIZE2")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLSIZE2" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLVALUE():
    assert hasattr(afpText::GSPCOL, "COLVALUE")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLVALUE" in klass.__dict__:
            descriptor = klass.__dict__["COLVALUE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gspcol_has_COLSIZE1():
    assert hasattr(afpText::GSPCOL, "COLSIZE1")
    descriptor = None
    for klass in afpText::GSPCOL.__mro__:
        if "COLSIZE1" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE1"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gbimg_is_not_abstract():
    assert not inspect.isabstract(afpText::GBIMG)


def test_afptext::gbimg_constructor_exists():
    assert callable(afpText::GBIMG.__init__)


def test_afptext::gbimg_constructor_args():
    sig = inspect.signature(afpText::GBIMG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"
    assert "HEIGHT" in params, "Missing parameter 'HEIGHT'"
    assert "RES" in params, "Missing parameter 'RES'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "WIDTH" in params, "Missing parameter 'WIDTH'"

def test_afptext::gbimg_has_YPOS():
    assert hasattr(afpText::GBIMG, "YPOS")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbimg_has_FORMAT():
    assert hasattr(afpText::GBIMG, "FORMAT")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbimg_has_HEIGHT():
    assert hasattr(afpText::GBIMG, "HEIGHT")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbimg_has_RES():
    assert hasattr(afpText::GBIMG, "RES")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbimg_has_XPOS():
    assert hasattr(afpText::GBIMG, "XPOS")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbimg_has_WIDTH():
    assert hasattr(afpText::GBIMG, "WIDTH")
    descriptor = None
    for klass in afpText::GBIMG.__mro__:
        if "WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["WIDTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bandimage_is_not_abstract():
    assert not inspect.isabstract(afpText::BandImage)


def test_afptext::bandimage_constructor_exists():
    assert callable(afpText::BandImage.__init__)


def test_afptext::bandimage_constructor_args():
    sig = inspect.signature(afpText::BandImage.__init__)
    params = list(sig.parameters.keys())
    assert "BCOUNT" in params, "Missing parameter 'BCOUNT'"

def test_afptext::bandimage_has_BCOUNT():
    assert hasattr(afpText::BandImage, "BCOUNT")
    descriptor = None
    for klass in afpText::BandImage.__mro__:
        if "BCOUNT" in klass.__dict__:
            descriptor = klass.__dict__["BCOUNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectbyteoffset_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectByteOffset)


def test_afptext::objectbyteoffset_constructor_exists():
    assert callable(afpText::ObjectByteOffset.__init__)


def test_afptext::objectbyteoffset_constructor_args():
    sig = inspect.signature(afpText::ObjectByteOffset.__init__)
    params = list(sig.parameters.keys())
    assert "DirByHi" in params, "Missing parameter 'DirByHi'"
    assert "DirByOff" in params, "Missing parameter 'DirByOff'"

def test_afptext::objectbyteoffset_has_DirByHi():
    assert hasattr(afpText::ObjectByteOffset, "DirByHi")
    descriptor = None
    for klass in afpText::ObjectByteOffset.__mro__:
        if "DirByHi" in klass.__dict__:
            descriptor = klass.__dict__["DirByHi"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectbyteoffset_has_DirByOff():
    assert hasattr(afpText::ObjectByteOffset, "DirByOff")
    descriptor = None
    for klass in afpText::ObjectByteOffset.__mro__:
        if "DirByOff" in klass.__dict__:
            descriptor = klass.__dict__["DirByOff"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsmc_is_not_abstract():
    assert not inspect.isabstract(afpText::GSMC)


def test_afptext::gsmc_constructor_exists():
    assert callable(afpText::GSMC.__init__)


def test_afptext::gsmc_constructor_args():
    sig = inspect.signature(afpText::GSMC.__init__)
    params = list(sig.parameters.keys())
    assert "CELLWI" in params, "Missing parameter 'CELLWI'"
    assert "CELLHI" in params, "Missing parameter 'CELLHI'"

def test_afptext::gsmc_has_CELLWI():
    assert hasattr(afpText::GSMC, "CELLWI")
    descriptor = None
    for klass in afpText::GSMC.__mro__:
        if "CELLWI" in klass.__dict__:
            descriptor = klass.__dict__["CELLWI"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsmc_has_CELLHI():
    assert hasattr(afpText::GSMC, "CELLHI")
    descriptor = None
    for klass in afpText::GSMC.__mro__:
        if "CELLHI" in klass.__dict__:
            descriptor = klass.__dict__["CELLHI"]
            break
    assert isinstance(descriptor, property)



def test_afptext::attributequalifier_is_not_abstract():
    assert not inspect.isabstract(afpText::AttributeQualifier)


def test_afptext::attributequalifier_constructor_exists():
    assert callable(afpText::AttributeQualifier.__init__)


def test_afptext::attributequalifier_constructor_args():
    sig = inspect.signature(afpText::AttributeQualifier.__init__)
    params = list(sig.parameters.keys())
    assert "SeqNum" in params, "Missing parameter 'SeqNum'"
    assert "LevNum" in params, "Missing parameter 'LevNum'"

def test_afptext::attributequalifier_has_SeqNum():
    assert hasattr(afpText::AttributeQualifier, "SeqNum")
    descriptor = None
    for klass in afpText::AttributeQualifier.__mro__:
        if "SeqNum" in klass.__dict__:
            descriptor = klass.__dict__["SeqNum"]
            break
    assert isinstance(descriptor, property)

def test_afptext::attributequalifier_has_LevNum():
    assert hasattr(afpText::AttributeQualifier, "LevNum")
    descriptor = None
    for klass in afpText::AttributeQualifier.__mro__:
        if "LevNum" in klass.__dict__:
            descriptor = klass.__dict__["LevNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectstructuredfieldoffset_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectStructuredFieldOffset)


def test_afptext::objectstructuredfieldoffset_constructor_exists():
    assert callable(afpText::ObjectStructuredFieldOffset.__init__)


def test_afptext::objectstructuredfieldoffset_constructor_args():
    sig = inspect.signature(afpText::ObjectStructuredFieldOffset.__init__)
    params = list(sig.parameters.keys())
    assert "SFOffHi" in params, "Missing parameter 'SFOffHi'"
    assert "SFOff" in params, "Missing parameter 'SFOff'"

def test_afptext::objectstructuredfieldoffset_has_SFOffHi():
    assert hasattr(afpText::ObjectStructuredFieldOffset, "SFOffHi")
    descriptor = None
    for klass in afpText::ObjectStructuredFieldOffset.__mro__:
        if "SFOffHi" in klass.__dict__:
            descriptor = klass.__dict__["SFOffHi"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectstructuredfieldoffset_has_SFOff():
    assert hasattr(afpText::ObjectStructuredFieldOffset, "SFOff")
    descriptor = None
    for klass in afpText::ObjectStructuredFieldOffset.__mro__:
        if "SFOff" in klass.__dict__:
            descriptor = klass.__dict__["SFOff"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectcount_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectCount)


def test_afptext::objectcount_constructor_exists():
    assert callable(afpText::ObjectCount.__init__)


def test_afptext::objectcount_constructor_args():
    sig = inspect.signature(afpText::ObjectCount.__init__)
    params = list(sig.parameters.keys())
    assert "SubObj" in params, "Missing parameter 'SubObj'"
    assert "SObjNum" in params, "Missing parameter 'SObjNum'"
    assert "SobjNmHi" in params, "Missing parameter 'SobjNmHi'"

def test_afptext::objectcount_has_SubObj():
    assert hasattr(afpText::ObjectCount, "SubObj")
    descriptor = None
    for klass in afpText::ObjectCount.__mro__:
        if "SubObj" in klass.__dict__:
            descriptor = klass.__dict__["SubObj"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectcount_has_SObjNum():
    assert hasattr(afpText::ObjectCount, "SObjNum")
    descriptor = None
    for klass in afpText::ObjectCount.__mro__:
        if "SObjNum" in klass.__dict__:
            descriptor = klass.__dict__["SObjNum"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectcount_has_SobjNmHi():
    assert hasattr(afpText::ObjectCount, "SobjNmHi")
    descriptor = None
    for klass in afpText::ObjectCount.__mro__:
        if "SobjNmHi" in klass.__dict__:
            descriptor = klass.__dict__["SobjNmHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsmx_is_not_abstract():
    assert not inspect.isabstract(afpText::GSMX)


def test_afptext::gsmx_constructor_exists():
    assert callable(afpText::GSMX.__init__)


def test_afptext::gsmx_constructor_args():
    sig = inspect.signature(afpText::GSMX.__init__)
    params = list(sig.parameters.keys())
    assert "MODE" in params, "Missing parameter 'MODE'"

def test_afptext::gsmx_has_MODE():
    assert hasattr(afpText::GSMX, "MODE")
    descriptor = None
    for klass in afpText::GSMX.__mro__:
        if "MODE" in klass.__dict__:
            descriptor = klass.__dict__["MODE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::endimage_is_not_abstract():
    assert not inspect.isabstract(afpText::EndImage)


def test_afptext::endimage_constructor_exists():
    assert callable(afpText::EndImage.__init__)


def test_afptext::endimage_constructor_args():
    sig = inspect.signature(afpText::EndImage.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fontresolution_is_not_abstract():
    assert not inspect.isabstract(afpText::FontResolution)


def test_afptext::fontresolution_constructor_exists():
    assert callable(afpText::FontResolution.__init__)


def test_afptext::fontresolution_constructor_args():
    sig = inspect.signature(afpText::FontResolution.__init__)
    params = list(sig.parameters.keys())
    assert "RPuBase" in params, "Missing parameter 'RPuBase'"
    assert "MetTech" in params, "Missing parameter 'MetTech'"
    assert "RPUnits" in params, "Missing parameter 'RPUnits'"

def test_afptext::fontresolution_has_RPuBase():
    assert hasattr(afpText::FontResolution, "RPuBase")
    descriptor = None
    for klass in afpText::FontResolution.__mro__:
        if "RPuBase" in klass.__dict__:
            descriptor = klass.__dict__["RPuBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontresolution_has_MetTech():
    assert hasattr(afpText::FontResolution, "MetTech")
    descriptor = None
    for klass in afpText::FontResolution.__mro__:
        if "MetTech" in klass.__dict__:
            descriptor = klass.__dict__["MetTech"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontresolution_has_RPUnits():
    assert hasattr(afpText::FontResolution, "RPUnits")
    descriptor = None
    for klass in afpText::FontResolution.__mro__:
        if "RPUnits" in klass.__dict__:
            descriptor = klass.__dict__["RPUnits"]
            break
    assert isinstance(descriptor, property)



def test_afptext::endtile_is_not_abstract():
    assert not inspect.isabstract(afpText::EndTile)


def test_afptext::endtile_constructor_exists():
    assert callable(afpText::EndTile.__init__)


def test_afptext::endtile_constructor_args():
    sig = inspect.signature(afpText::EndTile.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gsgch_is_not_abstract():
    assert not inspect.isabstract(afpText::GSGCH)


def test_afptext::gsgch_constructor_exists():
    assert callable(afpText::GSGCH.__init__)


def test_afptext::gsgch_constructor_args():
    sig = inspect.signature(afpText::GSGCH.__init__)
    params = list(sig.parameters.keys())



def test_afptext::colorfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::ColorFidelity)


def test_afptext::colorfidelity_constructor_exists():
    assert callable(afpText::ColorFidelity.__init__)


def test_afptext::colorfidelity_constructor_args():
    sig = inspect.signature(afpText::ColorFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpCoEx" in params, "Missing parameter 'StpCoEx'"
    assert "ColSub" in params, "Missing parameter 'ColSub'"
    assert "RepCoEx" in params, "Missing parameter 'RepCoEx'"

def test_afptext::colorfidelity_has_StpCoEx():
    assert hasattr(afpText::ColorFidelity, "StpCoEx")
    descriptor = None
    for klass in afpText::ColorFidelity.__mro__:
        if "StpCoEx" in klass.__dict__:
            descriptor = klass.__dict__["StpCoEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorfidelity_has_ColSub():
    assert hasattr(afpText::ColorFidelity, "ColSub")
    descriptor = None
    for klass in afpText::ColorFidelity.__mro__:
        if "ColSub" in klass.__dict__:
            descriptor = klass.__dict__["ColSub"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorfidelity_has_RepCoEx():
    assert hasattr(afpText::ColorFidelity, "RepCoEx")
    descriptor = None
    for klass in afpText::ColorFidelity.__mro__:
        if "RepCoEx" in klass.__dict__:
            descriptor = klass.__dict__["RepCoEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::idesize_is_not_abstract():
    assert not inspect.isabstract(afpText::IDESize)


def test_afptext::idesize_constructor_exists():
    assert callable(afpText::IDESize.__init__)


def test_afptext::idesize_constructor_args():
    sig = inspect.signature(afpText::IDESize.__init__)
    params = list(sig.parameters.keys())
    assert "IDESZ" in params, "Missing parameter 'IDESZ'"

def test_afptext::idesize_has_IDESZ():
    assert hasattr(afpText::IDESize, "IDESZ")
    descriptor = None
    for klass in afpText::IDESize.__mro__:
        if "IDESZ" in klass.__dict__:
            descriptor = klass.__dict__["IDESZ"]
            break
    assert isinstance(descriptor, property)



def test_afptext::encodingschemeid_is_not_abstract():
    assert not inspect.isabstract(afpText::EncodingSchemeID)


def test_afptext::encodingschemeid_constructor_exists():
    assert callable(afpText::EncodingSchemeID.__init__)


def test_afptext::encodingschemeid_constructor_args():
    sig = inspect.signature(afpText::EncodingSchemeID.__init__)
    params = list(sig.parameters.keys())
    assert "ESidCP" in params, "Missing parameter 'ESidCP'"
    assert "ESidUD" in params, "Missing parameter 'ESidUD'"

def test_afptext::encodingschemeid_has_ESidCP():
    assert hasattr(afpText::EncodingSchemeID, "ESidCP")
    descriptor = None
    for klass in afpText::EncodingSchemeID.__mro__:
        if "ESidCP" in klass.__dict__:
            descriptor = klass.__dict__["ESidCP"]
            break
    assert isinstance(descriptor, property)

def test_afptext::encodingschemeid_has_ESidUD():
    assert hasattr(afpText::EncodingSchemeID, "ESidUD")
    descriptor = None
    for klass in afpText::EncodingSchemeID.__mro__:
        if "ESidUD" in klass.__dict__:
            descriptor = klass.__dict__["ESidUD"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsap_is_not_abstract():
    assert not inspect.isabstract(afpText::GSAP)


def test_afptext::gsap_constructor_exists():
    assert callable(afpText::GSAP.__init__)


def test_afptext::gsap_constructor_args():
    sig = inspect.signature(afpText::GSAP.__init__)
    params = list(sig.parameters.keys())
    assert "Q" in params, "Missing parameter 'Q'"
    assert "S" in params, "Missing parameter 'S'"
    assert "R" in params, "Missing parameter 'R'"
    assert "P" in params, "Missing parameter 'P'"

def test_afptext::gsap_has_Q():
    assert hasattr(afpText::GSAP, "Q")
    descriptor = None
    for klass in afpText::GSAP.__mro__:
        if "Q" in klass.__dict__:
            descriptor = klass.__dict__["Q"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsap_has_S():
    assert hasattr(afpText::GSAP, "S")
    descriptor = None
    for klass in afpText::GSAP.__mro__:
        if "S" in klass.__dict__:
            descriptor = klass.__dict__["S"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsap_has_R():
    assert hasattr(afpText::GSAP, "R")
    descriptor = None
    for klass in afpText::GSAP.__mro__:
        if "R" in klass.__dict__:
            descriptor = klass.__dict__["R"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsap_has_P():
    assert hasattr(afpText::GSAP, "P")
    descriptor = None
    for klass in afpText::GSAP.__mro__:
        if "P" in klass.__dict__:
            descriptor = klass.__dict__["P"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gccbez_is_not_abstract():
    assert not inspect.isabstract(afpText::GCCBEZ)


def test_afptext::gccbez_constructor_exists():
    assert callable(afpText::GCCBEZ.__init__)


def test_afptext::gccbez_constructor_args():
    sig = inspect.signature(afpText::GCCBEZ.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gsecol_is_not_abstract():
    assert not inspect.isabstract(afpText::GSECOL)


def test_afptext::gsecol_constructor_exists():
    assert callable(afpText::GSECOL.__init__)


def test_afptext::gsecol_constructor_args():
    sig = inspect.signature(afpText::GSECOL.__init__)
    params = list(sig.parameters.keys())
    assert "COLOR" in params, "Missing parameter 'COLOR'"

def test_afptext::gsecol_has_COLOR():
    assert hasattr(afpText::GSECOL, "COLOR")
    descriptor = None
    for klass in afpText::GSECOL.__mro__:
        if "COLOR" in klass.__dict__:
            descriptor = klass.__dict__["COLOR"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gscs_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCS)


def test_afptext::gscs_constructor_exists():
    assert callable(afpText::GSCS.__init__)


def test_afptext::gscs_constructor_args():
    sig = inspect.signature(afpText::GSCS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext::gscs_has_LCID():
    assert hasattr(afpText::GSCS, "LCID")
    descriptor = None
    for klass in afpText::GSCS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mediaejectcontrol_is_not_abstract():
    assert not inspect.isabstract(afpText::MediaEjectControl)


def test_afptext::mediaejectcontrol_constructor_exists():
    assert callable(afpText::MediaEjectControl.__init__)


def test_afptext::mediaejectcontrol_constructor_args():
    sig = inspect.signature(afpText::MediaEjectControl.__init__)
    params = list(sig.parameters.keys())
    assert "EjCtrl" in params, "Missing parameter 'EjCtrl'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::mediaejectcontrol_has_EjCtrl():
    assert hasattr(afpText::MediaEjectControl, "EjCtrl")
    descriptor = None
    for klass in afpText::MediaEjectControl.__mro__:
        if "EjCtrl" in klass.__dict__:
            descriptor = klass.__dict__["EjCtrl"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mediaejectcontrol_has_Reserved():
    assert hasattr(afpText::MediaEjectControl, "Reserved")
    descriptor = None
    for klass in afpText::MediaEjectControl.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::begintransparencymask_is_not_abstract():
    assert not inspect.isabstract(afpText::BeginTransparencyMask)


def test_afptext::begintransparencymask_constructor_exists():
    assert callable(afpText::BeginTransparencyMask.__init__)


def test_afptext::begintransparencymask_constructor_args():
    sig = inspect.signature(afpText::BeginTransparencyMask.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gsms_is_not_abstract():
    assert not inspect.isabstract(afpText::GSMS)


def test_afptext::gsms_constructor_exists():
    assert callable(afpText::GSMS.__init__)


def test_afptext::gsms_constructor_args():
    sig = inspect.signature(afpText::GSMS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext::gsms_has_LCID():
    assert hasattr(afpText::GSMS, "LCID")
    descriptor = None
    for klass in afpText::GSMS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::geprol_is_not_abstract():
    assert not inspect.isabstract(afpText::GEPROL)


def test_afptext::geprol_constructor_exists():
    assert callable(afpText::GEPROL.__init__)


def test_afptext::geprol_constructor_args():
    sig = inspect.signature(afpText::GEPROL.__init__)
    params = list(sig.parameters.keys())
    assert "RES" in params, "Missing parameter 'RES'"

def test_afptext::geprol_has_RES():
    assert hasattr(afpText::GEPROL, "RES")
    descriptor = None
    for klass in afpText::GEPROL.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectfunctionsetspecification_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectFunctionSetSpecification)


def test_afptext::objectfunctionsetspecification_constructor_exists():
    assert callable(afpText::ObjectFunctionSetSpecification.__init__)


def test_afptext::objectfunctionsetspecification_constructor_args():
    sig = inspect.signature(afpText::ObjectFunctionSetSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "OCAFnSet" in params, "Missing parameter 'OCAFnSet'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "DCAFnSet" in params, "Missing parameter 'DCAFnSet'"
    assert "ArchVrsn" in params, "Missing parameter 'ArchVrsn'"

def test_afptext::objectfunctionsetspecification_has_OCAFnSet():
    assert hasattr(afpText::ObjectFunctionSetSpecification, "OCAFnSet")
    descriptor = None
    for klass in afpText::ObjectFunctionSetSpecification.__mro__:
        if "OCAFnSet" in klass.__dict__:
            descriptor = klass.__dict__["OCAFnSet"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectfunctionsetspecification_has_ObjType():
    assert hasattr(afpText::ObjectFunctionSetSpecification, "ObjType")
    descriptor = None
    for klass in afpText::ObjectFunctionSetSpecification.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectfunctionsetspecification_has_DCAFnSet():
    assert hasattr(afpText::ObjectFunctionSetSpecification, "DCAFnSet")
    descriptor = None
    for klass in afpText::ObjectFunctionSetSpecification.__mro__:
        if "DCAFnSet" in klass.__dict__:
            descriptor = klass.__dict__["DCAFnSet"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectfunctionsetspecification_has_ArchVrsn():
    assert hasattr(afpText::ObjectFunctionSetSpecification, "ArchVrsn")
    descriptor = None
    for klass in afpText::ObjectFunctionSetSpecification.__mro__:
        if "ArchVrsn" in klass.__dict__:
            descriptor = klass.__dict__["ArchVrsn"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fontcodedgraphiccharactersetglobalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText::FontCodedGraphicCharacterSetGlobalIdentifier)


def test_afptext::fontcodedgraphiccharactersetglobalidentifier_constructor_exists():
    assert callable(afpText::FontCodedGraphicCharacterSetGlobalIdentifier.__init__)


def test_afptext::fontcodedgraphiccharactersetglobalidentifier_constructor_args():
    sig = inspect.signature(afpText::FontCodedGraphicCharacterSetGlobalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"
    assert "CPGID" in params, "Missing parameter 'CPGID'"

def test_afptext::fontcodedgraphiccharactersetglobalidentifier_has_GCSGID():
    assert hasattr(afpText::FontCodedGraphicCharacterSetGlobalIdentifier, "GCSGID")
    descriptor = None
    for klass in afpText::FontCodedGraphicCharacterSetGlobalIdentifier.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontcodedgraphiccharactersetglobalidentifier_has_CPGID():
    assert hasattr(afpText::FontCodedGraphicCharacterSetGlobalIdentifier, "CPGID")
    descriptor = None
    for klass in afpText::FontCodedGraphicCharacterSetGlobalIdentifier.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gchst_is_not_abstract():
    assert not inspect.isabstract(afpText::GCHST)


def test_afptext::gchst_constructor_exists():
    assert callable(afpText::GCHST.__init__)


def test_afptext::gchst_constructor_args():
    sig = inspect.signature(afpText::GCHST.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "CP" in params, "Missing parameter 'CP'"

def test_afptext::gchst_has_YPOS():
    assert hasattr(afpText::GCHST, "YPOS")
    descriptor = None
    for klass in afpText::GCHST.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gchst_has_XPOS():
    assert hasattr(afpText::GCHST, "XPOS")
    descriptor = None
    for klass in afpText::GCHST.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gchst_has_CP():
    assert hasattr(afpText::GCHST, "CP")
    descriptor = None
    for klass in afpText::GCHST.__mro__:
        if "CP" in klass.__dict__:
            descriptor = klass.__dict__["CP"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pagepositioninformation_is_not_abstract():
    assert not inspect.isabstract(afpText::PagePositionInformation)


def test_afptext::pagepositioninformation_constructor_exists():
    assert callable(afpText::PagePositionInformation.__init__)


def test_afptext::pagepositioninformation_constructor_args():
    sig = inspect.signature(afpText::PagePositionInformation.__init__)
    params = list(sig.parameters.keys())
    assert "PGPRG" in params, "Missing parameter 'PGPRG'"

def test_afptext::pagepositioninformation_has_PGPRG():
    assert hasattr(afpText::PagePositionInformation, "PGPRG")
    descriptor = None
    for klass in afpText::PagePositionInformation.__mro__:
        if "PGPRG" in klass.__dict__:
            descriptor = klass.__dict__["PGPRG"]
            break
    assert isinstance(descriptor, property)



def test_afptext::colorspecification_is_not_abstract():
    assert not inspect.isabstract(afpText::ColorSpecification)


def test_afptext::colorspecification_constructor_exists():
    assert callable(afpText::ColorSpecification.__init__)


def test_afptext::colorspecification_constructor_args():
    sig = inspect.signature(afpText::ColorSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "ColSize1" in params, "Missing parameter 'ColSize1'"
    assert "ColSize2" in params, "Missing parameter 'ColSize2'"
    assert "Color" in params, "Missing parameter 'Color'"
    assert "ColSize4" in params, "Missing parameter 'ColSize4'"
    assert "ColSpce" in params, "Missing parameter 'ColSpce'"
    assert "ColSize3" in params, "Missing parameter 'ColSize3'"

def test_afptext::colorspecification_has_ColSize1():
    assert hasattr(afpText::ColorSpecification, "ColSize1")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "ColSize1" in klass.__dict__:
            descriptor = klass.__dict__["ColSize1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorspecification_has_ColSize2():
    assert hasattr(afpText::ColorSpecification, "ColSize2")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "ColSize2" in klass.__dict__:
            descriptor = klass.__dict__["ColSize2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorspecification_has_Color():
    assert hasattr(afpText::ColorSpecification, "Color")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorspecification_has_ColSize4():
    assert hasattr(afpText::ColorSpecification, "ColSize4")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "ColSize4" in klass.__dict__:
            descriptor = klass.__dict__["ColSize4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorspecification_has_ColSpce():
    assert hasattr(afpText::ColorSpecification, "ColSpce")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "ColSpce" in klass.__dict__:
            descriptor = klass.__dict__["ColSpce"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colorspecification_has_ColSize3():
    assert hasattr(afpText::ColorSpecification, "ColSize3")
    descriptor = None
    for klass in afpText::ColorSpecification.__mro__:
        if "ColSize3" in klass.__dict__:
            descriptor = klass.__dict__["ColSize3"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tbm_is_not_abstract():
    assert not inspect.isabstract(afpText::TBM)


def test_afptext::tbm_constructor_exists():
    assert callable(afpText::TBM.__init__)


def test_afptext::tbm_constructor_args():
    sig = inspect.signature(afpText::TBM.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"
    assert "PRECSION" in params, "Missing parameter 'PRECSION'"
    assert "DIRCTION" in params, "Missing parameter 'DIRCTION'"

def test_afptext::tbm_has_INCRMENT():
    assert hasattr(afpText::TBM, "INCRMENT")
    descriptor = None
    for klass in afpText::TBM.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tbm_has_PRECSION():
    assert hasattr(afpText::TBM, "PRECSION")
    descriptor = None
    for klass in afpText::TBM.__mro__:
        if "PRECSION" in klass.__dict__:
            descriptor = klass.__dict__["PRECSION"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tbm_has_DIRCTION():
    assert hasattr(afpText::TBM, "DIRCTION")
    descriptor = None
    for klass in afpText::TBM.__mro__:
        if "DIRCTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gimd_is_not_abstract():
    assert not inspect.isabstract(afpText::GIMD)


def test_afptext::gimd_constructor_exists():
    assert callable(afpText::GIMD.__init__)


def test_afptext::gimd_constructor_args():
    sig = inspect.signature(afpText::GIMD.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::gimd_has_DATA():
    assert hasattr(afpText::GIMD, "DATA")
    descriptor = None
    for klass in afpText::GIMD.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsmp_is_not_abstract():
    assert not inspect.isabstract(afpText::GSMP)


def test_afptext::gsmp_constructor_exists():
    assert callable(afpText::GSMP.__init__)


def test_afptext::gsmp_constructor_args():
    sig = inspect.signature(afpText::GSMP.__init__)
    params = list(sig.parameters.keys())
    assert "PREC" in params, "Missing parameter 'PREC'"

def test_afptext::gsmp_has_PREC():
    assert hasattr(afpText::GSMP, "PREC")
    descriptor = None
    for klass in afpText::GSMP.__mro__:
        if "PREC" in klass.__dict__:
            descriptor = klass.__dict__["PREC"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcbez_is_not_abstract():
    assert not inspect.isabstract(afpText::GCBEZ)


def test_afptext::gcbez_constructor_exists():
    assert callable(afpText::GCBEZ.__init__)


def test_afptext::gcbez_constructor_args():
    sig = inspect.signature(afpText::GCBEZ.__init__)
    params = list(sig.parameters.keys())



def test_afptext::metricadjustment_is_not_abstract():
    assert not inspect.isabstract(afpText::MetricAdjustment)


def test_afptext::metricadjustment_constructor_exists():
    assert callable(afpText::MetricAdjustment.__init__)


def test_afptext::metricadjustment_constructor_args():
    sig = inspect.signature(afpText::MetricAdjustment.__init__)
    params = list(sig.parameters.keys())
    assert "VUniformIncrement" in params, "Missing parameter 'VUniformIncrement'"
    assert "VBaselineIncrement" in params, "Missing parameter 'VBaselineIncrement'"
    assert "HUniformIncrement" in params, "Missing parameter 'HUniformIncrement'"
    assert "HBaselineIncrement" in params, "Missing parameter 'HBaselineIncrement'"
    assert "XUPUB" in params, "Missing parameter 'XUPUB'"
    assert "UnitBase" in params, "Missing parameter 'UnitBase'"
    assert "YUPUB" in params, "Missing parameter 'YUPUB'"

def test_afptext::metricadjustment_has_VUniformIncrement():
    assert hasattr(afpText::MetricAdjustment, "VUniformIncrement")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "VUniformIncrement" in klass.__dict__:
            descriptor = klass.__dict__["VUniformIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_VBaselineIncrement():
    assert hasattr(afpText::MetricAdjustment, "VBaselineIncrement")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "VBaselineIncrement" in klass.__dict__:
            descriptor = klass.__dict__["VBaselineIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_HUniformIncrement():
    assert hasattr(afpText::MetricAdjustment, "HUniformIncrement")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "HUniformIncrement" in klass.__dict__:
            descriptor = klass.__dict__["HUniformIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_HBaselineIncrement():
    assert hasattr(afpText::MetricAdjustment, "HBaselineIncrement")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "HBaselineIncrement" in klass.__dict__:
            descriptor = klass.__dict__["HBaselineIncrement"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_XUPUB():
    assert hasattr(afpText::MetricAdjustment, "XUPUB")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "XUPUB" in klass.__dict__:
            descriptor = klass.__dict__["XUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_UnitBase():
    assert hasattr(afpText::MetricAdjustment, "UnitBase")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "UnitBase" in klass.__dict__:
            descriptor = klass.__dict__["UnitBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::metricadjustment_has_YUPUB():
    assert hasattr(afpText::MetricAdjustment, "YUPUB")
    descriptor = None
    for klass in afpText::MetricAdjustment.__mro__:
        if "YUPUB" in klass.__dict__:
            descriptor = klass.__dict__["YUPUB"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectcontainerpresentationspacesize_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectContainerPresentationSpaceSize)


def test_afptext::objectcontainerpresentationspacesize_constructor_exists():
    assert callable(afpText::ObjectContainerPresentationSpaceSize.__init__)


def test_afptext::objectcontainerpresentationspacesize_constructor_args():
    sig = inspect.signature(afpText::ObjectContainerPresentationSpaceSize.__init__)
    params = list(sig.parameters.keys())
    assert "PDFSize" in params, "Missing parameter 'PDFSize'"

def test_afptext::objectcontainerpresentationspacesize_has_PDFSize():
    assert hasattr(afpText::ObjectContainerPresentationSpaceSize, "PDFSize")
    descriptor = None
    for klass in afpText::ObjectContainerPresentationSpaceSize.__mro__:
        if "PDFSize" in klass.__dict__:
            descriptor = klass.__dict__["PDFSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext::resourcelocalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText::ResourceLocalIdentifier)


def test_afptext::resourcelocalidentifier_constructor_exists():
    assert callable(afpText::ResourceLocalIdentifier.__init__)


def test_afptext::resourcelocalidentifier_constructor_args():
    sig = inspect.signature(afpText::ResourceLocalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "ResLID" in params, "Missing parameter 'ResLID'"
    assert "ResType" in params, "Missing parameter 'ResType'"

def test_afptext::resourcelocalidentifier_has_ResLID():
    assert hasattr(afpText::ResourceLocalIdentifier, "ResLID")
    descriptor = None
    for klass in afpText::ResourceLocalIdentifier.__mro__:
        if "ResLID" in klass.__dict__:
            descriptor = klass.__dict__["ResLID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourcelocalidentifier_has_ResType():
    assert hasattr(afpText::ResourceLocalIdentifier, "ResType")
    descriptor = None
    for klass in afpText::ResourceLocalIdentifier.__mro__:
        if "ResType" in klass.__dict__:
            descriptor = klass.__dict__["ResType"]
            break
    assert isinstance(descriptor, property)



def test_afptext::presentationcontrol_is_not_abstract():
    assert not inspect.isabstract(afpText::PresentationControl)


def test_afptext::presentationcontrol_constructor_exists():
    assert callable(afpText::PresentationControl.__init__)


def test_afptext::presentationcontrol_constructor_args():
    sig = inspect.signature(afpText::PresentationControl.__init__)
    params = list(sig.parameters.keys())
    assert "PRSFlg" in params, "Missing parameter 'PRSFlg'"

def test_afptext::presentationcontrol_has_PRSFlg():
    assert hasattr(afpText::PresentationControl, "PRSFlg")
    descriptor = None
    for klass in afpText::PresentationControl.__mro__:
        if "PRSFlg" in klass.__dict__:
            descriptor = klass.__dict__["PRSFlg"]
            break
    assert isinstance(descriptor, property)



def test_afptext::extendedresourcelocalidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText::ExtendedResourceLocalIdentifier)


def test_afptext::extendedresourcelocalidentifier_constructor_exists():
    assert callable(afpText::ExtendedResourceLocalIdentifier.__init__)


def test_afptext::extendedresourcelocalidentifier_constructor_args():
    sig = inspect.signature(afpText::ExtendedResourceLocalIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "ResLID" in params, "Missing parameter 'ResLID'"
    assert "ResType" in params, "Missing parameter 'ResType'"

def test_afptext::extendedresourcelocalidentifier_has_ResLID():
    assert hasattr(afpText::ExtendedResourceLocalIdentifier, "ResLID")
    descriptor = None
    for klass in afpText::ExtendedResourceLocalIdentifier.__mro__:
        if "ResLID" in klass.__dict__:
            descriptor = klass.__dict__["ResLID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::extendedresourcelocalidentifier_has_ResType():
    assert hasattr(afpText::ExtendedResourceLocalIdentifier, "ResType")
    descriptor = None
    for klass in afpText::ExtendedResourceLocalIdentifier.__mro__:
        if "ResType" in klass.__dict__:
            descriptor = klass.__dict__["ResType"]
            break
    assert isinstance(descriptor, property)



def test_afptext::colormanagementresourcedescriptor_is_not_abstract():
    assert not inspect.isabstract(afpText::ColorManagementResourceDescriptor)


def test_afptext::colormanagementresourcedescriptor_constructor_exists():
    assert callable(afpText::ColorManagementResourceDescriptor.__init__)


def test_afptext::colormanagementresourcedescriptor_constructor_args():
    sig = inspect.signature(afpText::ColorManagementResourceDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "ProcMode" in params, "Missing parameter 'ProcMode'"
    assert "CMRScpe" in params, "Missing parameter 'CMRScpe'"

def test_afptext::colormanagementresourcedescriptor_has_ProcMode():
    assert hasattr(afpText::ColorManagementResourceDescriptor, "ProcMode")
    descriptor = None
    for klass in afpText::ColorManagementResourceDescriptor.__mro__:
        if "ProcMode" in klass.__dict__:
            descriptor = klass.__dict__["ProcMode"]
            break
    assert isinstance(descriptor, property)

def test_afptext::colormanagementresourcedescriptor_has_CMRScpe():
    assert hasattr(afpText::ColorManagementResourceDescriptor, "CMRScpe")
    descriptor = None
    for klass in afpText::ColorManagementResourceDescriptor.__mro__:
        if "CMRScpe" in klass.__dict__:
            descriptor = klass.__dict__["CMRScpe"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcchst_is_not_abstract():
    assert not inspect.isabstract(afpText::GCCHST)


def test_afptext::gcchst_constructor_exists():
    assert callable(afpText::GCCHST.__init__)


def test_afptext::gcchst_constructor_args():
    sig = inspect.signature(afpText::GCCHST.__init__)
    params = list(sig.parameters.keys())
    assert "CP" in params, "Missing parameter 'CP'"

def test_afptext::gcchst_has_CP():
    assert hasattr(afpText::GCCHST, "CP")
    descriptor = None
    for klass in afpText::GCCHST.__mro__:
        if "CP" in klass.__dict__:
            descriptor = klass.__dict__["CP"]
            break
    assert isinstance(descriptor, property)



def test_afptext::linedataobjectpositionmigration_is_not_abstract():
    assert not inspect.isabstract(afpText::LineDataObjectPositionMigration)


def test_afptext::linedataobjectpositionmigration_constructor_exists():
    assert callable(afpText::LineDataObjectPositionMigration.__init__)


def test_afptext::linedataobjectpositionmigration_constructor_args():
    sig = inspect.signature(afpText::LineDataObjectPositionMigration.__init__)
    params = list(sig.parameters.keys())
    assert "TempOrient" in params, "Missing parameter 'TempOrient'"

def test_afptext::linedataobjectpositionmigration_has_TempOrient():
    assert hasattr(afpText::LineDataObjectPositionMigration, "TempOrient")
    descriptor = None
    for klass in afpText::LineDataObjectPositionMigration.__mro__:
        if "TempOrient" in klass.__dict__:
            descriptor = klass.__dict__["TempOrient"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gscp_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCP)


def test_afptext::gscp_constructor_exists():
    assert callable(afpText::GSCP.__init__)


def test_afptext::gscp_constructor_args():
    sig = inspect.signature(afpText::GSCP.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext::gscp_has_XPOS():
    assert hasattr(afpText::GSCP, "XPOS")
    descriptor = None
    for klass in afpText::GSCP.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gscp_has_YPOS():
    assert hasattr(afpText::GSCP, "YPOS")
    descriptor = None
    for klass in afpText::GSCP.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcomt_is_not_abstract():
    assert not inspect.isabstract(afpText::GCOMT)


def test_afptext::gcomt_constructor_exists():
    assert callable(afpText::GCOMT.__init__)


def test_afptext::gcomt_constructor_args():
    sig = inspect.signature(afpText::GCOMT.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::gcomt_has_DATA():
    assert hasattr(afpText::GCOMT, "DATA")
    descriptor = None
    for klass in afpText::GCOMT.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gbar_is_not_abstract():
    assert not inspect.isabstract(afpText::GBAR)


def test_afptext::gbar_constructor_exists():
    assert callable(afpText::GBAR.__init__)


def test_afptext::gbar_constructor_args():
    sig = inspect.signature(afpText::GBAR.__init__)
    params = list(sig.parameters.keys())
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"

def test_afptext::gbar_has_FLAGS():
    assert hasattr(afpText::GBAR, "FLAGS")
    descriptor = None
    for klass in afpText::GBAR.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnnrg2_is_not_abstract():
    assert not inspect.isabstract(afpText::FNNRG2)


def test_afptext::fnnrg2_constructor_exists():
    assert callable(afpText::FNNRG2.__init__)


def test_afptext::fnnrg2_constructor_args():
    sig = inspect.signature(afpText::FNNRG2.__init__)
    params = list(sig.parameters.keys())
    assert "TSID" in params, "Missing parameter 'TSID'"
    assert "TSIDLen" in params, "Missing parameter 'TSIDLen'"

def test_afptext::fnnrg2_has_TSID():
    assert hasattr(afpText::FNNRG2, "TSID")
    descriptor = None
    for klass in afpText::FNNRG2.__mro__:
        if "TSID" in klass.__dict__:
            descriptor = klass.__dict__["TSID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnnrg2_has_TSIDLen():
    assert hasattr(afpText::FNNRG2, "TSIDLen")
    descriptor = None
    for klass in afpText::FNNRG2.__mro__:
        if "TSIDLen" in klass.__dict__:
            descriptor = klass.__dict__["TSIDLen"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bln_is_not_abstract():
    assert not inspect.isabstract(afpText::BLN)


def test_afptext::bln_constructor_exists():
    assert callable(afpText::BLN.__init__)


def test_afptext::bln_constructor_args():
    sig = inspect.signature(afpText::BLN.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gsflw_is_not_abstract():
    assert not inspect.isabstract(afpText::GSFLW)


def test_afptext::gsflw_constructor_exists():
    assert callable(afpText::GSFLW.__init__)


def test_afptext::gsflw_constructor_args():
    sig = inspect.signature(afpText::GSFLW.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"
    assert "MFR" in params, "Missing parameter 'MFR'"

def test_afptext::gsflw_has_MH():
    assert hasattr(afpText::GSFLW, "MH")
    descriptor = None
    for klass in afpText::GSFLW.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsflw_has_MFR():
    assert hasattr(afpText::GSFLW, "MFR")
    descriptor = None
    for klass in afpText::GSFLW.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gslt_is_not_abstract():
    assert not inspect.isabstract(afpText::GSLT)


def test_afptext::gslt_constructor_exists():
    assert callable(afpText::GSLT.__init__)


def test_afptext::gslt_constructor_args():
    sig = inspect.signature(afpText::GSLT.__init__)
    params = list(sig.parameters.keys())
    assert "LINETYPE" in params, "Missing parameter 'LINETYPE'"

def test_afptext::gslt_has_LINETYPE():
    assert hasattr(afpText::GSLT, "LINETYPE")
    descriptor = None
    for klass in afpText::GSLT.__mro__:
        if "LINETYPE" in klass.__dict__:
            descriptor = klass.__dict__["LINETYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectbyteextent_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectByteExtent)


def test_afptext::objectbyteextent_constructor_exists():
    assert callable(afpText::ObjectByteExtent.__init__)


def test_afptext::objectbyteextent_constructor_args():
    sig = inspect.signature(afpText::ObjectByteExtent.__init__)
    params = list(sig.parameters.keys())
    assert "ByteExt" in params, "Missing parameter 'ByteExt'"
    assert "ByteExtHi" in params, "Missing parameter 'ByteExtHi'"

def test_afptext::objectbyteextent_has_ByteExt():
    assert hasattr(afpText::ObjectByteExtent, "ByteExt")
    descriptor = None
    for klass in afpText::ObjectByteExtent.__mro__:
        if "ByteExt" in klass.__dict__:
            descriptor = klass.__dict__["ByteExt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectbyteextent_has_ByteExtHi():
    assert hasattr(afpText::ObjectByteExtent, "ByteExtHi")
    descriptor = None
    for klass in afpText::ObjectByteExtent.__mro__:
        if "ByteExtHi" in klass.__dict__:
            descriptor = klass.__dict__["ByteExtHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsbmx_is_not_abstract():
    assert not inspect.isabstract(afpText::GSBMX)


def test_afptext::gsbmx_constructor_exists():
    assert callable(afpText::GSBMX.__init__)


def test_afptext::gsbmx_constructor_args():
    sig = inspect.signature(afpText::GSBMX.__init__)
    params = list(sig.parameters.keys())
    assert "MODE" in params, "Missing parameter 'MODE'"

def test_afptext::gsbmx_has_MODE():
    assert hasattr(afpText::GSBMX, "MODE")
    descriptor = None
    for klass in afpText::GSBMX.__mro__:
        if "MODE" in klass.__dict__:
            descriptor = klass.__dict__["MODE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::usc_is_not_abstract():
    assert not inspect.isabstract(afpText::USC)


def test_afptext::usc_constructor_exists():
    assert callable(afpText::USC.__init__)


def test_afptext::usc_constructor_args():
    sig = inspect.signature(afpText::USC.__init__)
    params = list(sig.parameters.keys())
    assert "BYPSIDEN" in params, "Missing parameter 'BYPSIDEN'"

def test_afptext::usc_has_BYPSIDEN():
    assert hasattr(afpText::USC, "BYPSIDEN")
    descriptor = None
    for klass in afpText::USC.__mro__:
        if "BYPSIDEN" in klass.__dict__:
            descriptor = klass.__dict__["BYPSIDEN"]
            break
    assert isinstance(descriptor, property)



def test_afptext::finishingfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::FinishingFidelity)


def test_afptext::finishingfidelity_constructor_exists():
    assert callable(afpText::FinishingFidelity.__init__)


def test_afptext::finishingfidelity_constructor_args():
    sig = inspect.signature(afpText::FinishingFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "RepFinEx" in params, "Missing parameter 'RepFinEx'"
    assert "StpFinEx" in params, "Missing parameter 'StpFinEx'"

def test_afptext::finishingfidelity_has_RepFinEx():
    assert hasattr(afpText::FinishingFidelity, "RepFinEx")
    descriptor = None
    for klass in afpText::FinishingFidelity.__mro__:
        if "RepFinEx" in klass.__dict__:
            descriptor = klass.__dict__["RepFinEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext::finishingfidelity_has_StpFinEx():
    assert hasattr(afpText::FinishingFidelity, "StpFinEx")
    descriptor = None
    for klass in afpText::FinishingFidelity.__mro__:
        if "StpFinEx" in klass.__dict__:
            descriptor = klass.__dict__["StpFinEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectclassification_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectClassification)


def test_afptext::objectclassification_constructor_exists():
    assert callable(afpText::ObjectClassification.__init__)


def test_afptext::objectclassification_constructor_args():
    sig = inspect.signature(afpText::ObjectClassification.__init__)
    params = list(sig.parameters.keys())
    assert "CompName" in params, "Missing parameter 'CompName'"
    assert "StrucFlgs" in params, "Missing parameter 'StrucFlgs'"
    assert "ObjTpName" in params, "Missing parameter 'ObjTpName'"
    assert "ObjClass" in params, "Missing parameter 'ObjClass'"
    assert "RegObjId" in params, "Missing parameter 'RegObjId'"
    assert "ObjLev" in params, "Missing parameter 'ObjLev'"

def test_afptext::objectclassification_has_CompName():
    assert hasattr(afpText::ObjectClassification, "CompName")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "CompName" in klass.__dict__:
            descriptor = klass.__dict__["CompName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectclassification_has_StrucFlgs():
    assert hasattr(afpText::ObjectClassification, "StrucFlgs")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "StrucFlgs" in klass.__dict__:
            descriptor = klass.__dict__["StrucFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectclassification_has_ObjTpName():
    assert hasattr(afpText::ObjectClassification, "ObjTpName")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "ObjTpName" in klass.__dict__:
            descriptor = klass.__dict__["ObjTpName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectclassification_has_ObjClass():
    assert hasattr(afpText::ObjectClassification, "ObjClass")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "ObjClass" in klass.__dict__:
            descriptor = klass.__dict__["ObjClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectclassification_has_RegObjId():
    assert hasattr(afpText::ObjectClassification, "RegObjId")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "RegObjId" in klass.__dict__:
            descriptor = klass.__dict__["RegObjId"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectclassification_has_ObjLev():
    assert hasattr(afpText::ObjectClassification, "ObjLev")
    descriptor = None
    for klass in afpText::ObjectClassification.__mro__:
        if "ObjLev" in klass.__dict__:
            descriptor = klass.__dict__["ObjLev"]
            break
    assert isinstance(descriptor, property)



def test_afptext::iocafunctionsetidentification_is_not_abstract():
    assert not inspect.isabstract(afpText::IOCAFunctionSetIdentification)


def test_afptext::iocafunctionsetidentification_constructor_exists():
    assert callable(afpText::IOCAFunctionSetIdentification.__init__)


def test_afptext::iocafunctionsetidentification_constructor_args():
    sig = inspect.signature(afpText::IOCAFunctionSetIdentification.__init__)
    params = list(sig.parameters.keys())
    assert "CATEGORY" in params, "Missing parameter 'CATEGORY'"
    assert "FCNSET" in params, "Missing parameter 'FCNSET'"

def test_afptext::iocafunctionsetidentification_has_CATEGORY():
    assert hasattr(afpText::IOCAFunctionSetIdentification, "CATEGORY")
    descriptor = None
    for klass in afpText::IOCAFunctionSetIdentification.__mro__:
        if "CATEGORY" in klass.__dict__:
            descriptor = klass.__dict__["CATEGORY"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iocafunctionsetidentification_has_FCNSET():
    assert hasattr(afpText::IOCAFunctionSetIdentification, "FCNSET")
    descriptor = None
    for klass in afpText::IOCAFunctionSetIdentification.__mro__:
        if "FCNSET" in klass.__dict__:
            descriptor = klass.__dict__["FCNSET"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bandimagedata_is_not_abstract():
    assert not inspect.isabstract(afpText::BandImageData)


def test_afptext::bandimagedata_constructor_exists():
    assert callable(afpText::BandImageData.__init__)


def test_afptext::bandimagedata_constructor_args():
    sig = inspect.signature(afpText::BandImageData.__init__)
    params = list(sig.parameters.keys())
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "BANDNUM" in params, "Missing parameter 'BANDNUM'"
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::bandimagedata_has_RESERVED():
    assert hasattr(afpText::BandImageData, "RESERVED")
    descriptor = None
    for klass in afpText::BandImageData.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bandimagedata_has_BANDNUM():
    assert hasattr(afpText::BandImageData, "BANDNUM")
    descriptor = None
    for klass in afpText::BandImageData.__mro__:
        if "BANDNUM" in klass.__dict__:
            descriptor = klass.__dict__["BANDNUM"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bandimagedata_has_DATA():
    assert hasattr(afpText::BandImageData, "DATA")
    descriptor = None
    for klass in afpText::BandImageData.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fontfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::FontFidelity)


def test_afptext::fontfidelity_constructor_exists():
    assert callable(afpText::FontFidelity.__init__)


def test_afptext::fontfidelity_constructor_args():
    sig = inspect.signature(afpText::FontFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpFntEx" in params, "Missing parameter 'StpFntEx'"

def test_afptext::fontfidelity_has_StpFntEx():
    assert hasattr(afpText::FontFidelity, "StpFntEx")
    descriptor = None
    for klass in afpText::FontFidelity.__mro__:
        if "StpFntEx" in klass.__dict__:
            descriptor = klass.__dict__["StpFntEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bsu_is_not_abstract():
    assert not inspect.isabstract(afpText::BSU)


def test_afptext::bsu_constructor_exists():
    assert callable(afpText::BSU.__init__)


def test_afptext::bsu_constructor_args():
    sig = inspect.signature(afpText::BSU.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext::bsu_has_LID():
    assert hasattr(afpText::BSU, "LID")
    descriptor = None
    for klass in afpText::BSU.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tilesize_is_not_abstract():
    assert not inspect.isabstract(afpText::TileSize)


def test_afptext::tilesize_constructor_exists():
    assert callable(afpText::TileSize.__init__)


def test_afptext::tilesize_constructor_args():
    sig = inspect.signature(afpText::TileSize.__init__)
    params = list(sig.parameters.keys())
    assert "TVSIZE" in params, "Missing parameter 'TVSIZE'"
    assert "THSIZE" in params, "Missing parameter 'THSIZE'"
    assert "RELRES" in params, "Missing parameter 'RELRES'"

def test_afptext::tilesize_has_TVSIZE():
    assert hasattr(afpText::TileSize, "TVSIZE")
    descriptor = None
    for klass in afpText::TileSize.__mro__:
        if "TVSIZE" in klass.__dict__:
            descriptor = klass.__dict__["TVSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesize_has_THSIZE():
    assert hasattr(afpText::TileSize, "THSIZE")
    descriptor = None
    for klass in afpText::TileSize.__mro__:
        if "THSIZE" in klass.__dict__:
            descriptor = klass.__dict__["THSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesize_has_RELRES():
    assert hasattr(afpText::TileSize, "RELRES")
    descriptor = None
    for klass in afpText::TileSize.__mro__:
        if "RELRES" in klass.__dict__:
            descriptor = klass.__dict__["RELRES"]
            break
    assert isinstance(descriptor, property)



def test_afptext::drawingordersubset_is_not_abstract():
    assert not inspect.isabstract(afpText::DrawingOrderSubset)


def test_afptext::drawingordersubset_constructor_exists():
    assert callable(afpText::DrawingOrderSubset.__init__)


def test_afptext::drawingordersubset_constructor_args():
    sig = inspect.signature(afpText::DrawingOrderSubset.__init__)
    params = list(sig.parameters.keys())



def test_afptext::windowspecification_is_not_abstract():
    assert not inspect.isabstract(afpText::WindowSpecification)


def test_afptext::windowspecification_constructor_exists():
    assert callable(afpText::WindowSpecification.__init__)


def test_afptext::windowspecification_constructor_args():
    sig = inspect.signature(afpText::WindowSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "YTWIND" in params, "Missing parameter 'YTWIND'"
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"
    assert "RES3" in params, "Missing parameter 'RES3'"
    assert "XRESOL" in params, "Missing parameter 'XRESOL'"
    assert "IMGXYRES" in params, "Missing parameter 'IMGXYRES'"
    assert "XLWIND" in params, "Missing parameter 'XLWIND'"
    assert "UBASE" in params, "Missing parameter 'UBASE'"
    assert "YBWIND" in params, "Missing parameter 'YBWIND'"
    assert "XRWIND" in params, "Missing parameter 'XRWIND'"
    assert "CFORMAT" in params, "Missing parameter 'CFORMAT'"
    assert "YRESOL" in params, "Missing parameter 'YRESOL'"

def test_afptext::windowspecification_has_YTWIND():
    assert hasattr(afpText::WindowSpecification, "YTWIND")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "YTWIND" in klass.__dict__:
            descriptor = klass.__dict__["YTWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_FLAGS():
    assert hasattr(afpText::WindowSpecification, "FLAGS")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_RES3():
    assert hasattr(afpText::WindowSpecification, "RES3")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "RES3" in klass.__dict__:
            descriptor = klass.__dict__["RES3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_XRESOL():
    assert hasattr(afpText::WindowSpecification, "XRESOL")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "XRESOL" in klass.__dict__:
            descriptor = klass.__dict__["XRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_IMGXYRES():
    assert hasattr(afpText::WindowSpecification, "IMGXYRES")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "IMGXYRES" in klass.__dict__:
            descriptor = klass.__dict__["IMGXYRES"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_XLWIND():
    assert hasattr(afpText::WindowSpecification, "XLWIND")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "XLWIND" in klass.__dict__:
            descriptor = klass.__dict__["XLWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_UBASE():
    assert hasattr(afpText::WindowSpecification, "UBASE")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "UBASE" in klass.__dict__:
            descriptor = klass.__dict__["UBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_YBWIND():
    assert hasattr(afpText::WindowSpecification, "YBWIND")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "YBWIND" in klass.__dict__:
            descriptor = klass.__dict__["YBWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_XRWIND():
    assert hasattr(afpText::WindowSpecification, "XRWIND")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "XRWIND" in klass.__dict__:
            descriptor = klass.__dict__["XRWIND"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_CFORMAT():
    assert hasattr(afpText::WindowSpecification, "CFORMAT")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "CFORMAT" in klass.__dict__:
            descriptor = klass.__dict__["CFORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::windowspecification_has_YRESOL():
    assert hasattr(afpText::WindowSpecification, "YRESOL")
    descriptor = None
    for klass in afpText::WindowSpecification.__mro__:
        if "YRESOL" in klass.__dict__:
            descriptor = klass.__dict__["YRESOL"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tileposition_is_not_abstract():
    assert not inspect.isabstract(afpText::TilePosition)


def test_afptext::tileposition_constructor_exists():
    assert callable(afpText::TilePosition.__init__)


def test_afptext::tileposition_constructor_args():
    sig = inspect.signature(afpText::TilePosition.__init__)
    params = list(sig.parameters.keys())
    assert "XOFFSET" in params, "Missing parameter 'XOFFSET'"
    assert "YOFFSET" in params, "Missing parameter 'YOFFSET'"

def test_afptext::tileposition_has_XOFFSET():
    assert hasattr(afpText::TilePosition, "XOFFSET")
    descriptor = None
    for klass in afpText::TilePosition.__mro__:
        if "XOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["XOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tileposition_has_YOFFSET():
    assert hasattr(afpText::TilePosition, "YOFFSET")
    descriptor = None
    for klass in afpText::TilePosition.__mro__:
        if "YOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["YOFFSET"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcline_is_not_abstract():
    assert not inspect.isabstract(afpText::GCLINE)


def test_afptext::gcline_constructor_exists():
    assert callable(afpText::GCLINE.__init__)


def test_afptext::gcline_constructor_args():
    sig = inspect.signature(afpText::GCLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gspt_is_not_abstract():
    assert not inspect.isabstract(afpText::GSPT)


def test_afptext::gspt_constructor_exists():
    assert callable(afpText::GSPT.__init__)


def test_afptext::gspt_constructor_args():
    sig = inspect.signature(afpText::GSPT.__init__)
    params = list(sig.parameters.keys())
    assert "PATT" in params, "Missing parameter 'PATT'"

def test_afptext::gspt_has_PATT():
    assert hasattr(afpText::GSPT, "PATT")
    descriptor = None
    for klass in afpText::GSPT.__mro__:
        if "PATT" in klass.__dict__:
            descriptor = klass.__dict__["PATT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fontdescriptorspecification_is_not_abstract():
    assert not inspect.isabstract(afpText::FontDescriptorSpecification)


def test_afptext::fontdescriptorspecification_constructor_exists():
    assert callable(afpText::FontDescriptorSpecification.__init__)


def test_afptext::fontdescriptorspecification_constructor_args():
    sig = inspect.signature(afpText::FontDescriptorSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "FtWidth" in params, "Missing parameter 'FtWidth'"
    assert "FtHeight" in params, "Missing parameter 'FtHeight'"
    assert "FtUsFlags" in params, "Missing parameter 'FtUsFlags'"
    assert "FtDsFlags" in params, "Missing parameter 'FtDsFlags'"
    assert "FtWdClass" in params, "Missing parameter 'FtWdClass'"
    assert "FtWtClass" in params, "Missing parameter 'FtWtClass'"

def test_afptext::fontdescriptorspecification_has_FtWidth():
    assert hasattr(afpText::FontDescriptorSpecification, "FtWidth")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtWidth" in klass.__dict__:
            descriptor = klass.__dict__["FtWidth"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontdescriptorspecification_has_FtHeight():
    assert hasattr(afpText::FontDescriptorSpecification, "FtHeight")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtHeight" in klass.__dict__:
            descriptor = klass.__dict__["FtHeight"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontdescriptorspecification_has_FtUsFlags():
    assert hasattr(afpText::FontDescriptorSpecification, "FtUsFlags")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtUsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtUsFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontdescriptorspecification_has_FtDsFlags():
    assert hasattr(afpText::FontDescriptorSpecification, "FtDsFlags")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtDsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtDsFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontdescriptorspecification_has_FtWdClass():
    assert hasattr(afpText::FontDescriptorSpecification, "FtWdClass")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtWdClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWdClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fontdescriptorspecification_has_FtWtClass():
    assert hasattr(afpText::FontDescriptorSpecification, "FtWtClass")
    descriptor = None
    for klass in afpText::FontDescriptorSpecification.__mro__:
        if "FtWtClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWtClass"]
            break
    assert isinstance(descriptor, property)



def test_afptext::beginsegmentcommand_is_not_abstract():
    assert not inspect.isabstract(afpText::BeginSegmentCommand)


def test_afptext::beginsegmentcommand_constructor_exists():
    assert callable(afpText::BeginSegmentCommand.__init__)


def test_afptext::beginsegmentcommand_constructor_args():
    sig = inspect.signature(afpText::BeginSegmentCommand.__init__)
    params = list(sig.parameters.keys())
    assert "FLAG2" in params, "Missing parameter 'FLAG2'"
    assert "PSNAME" in params, "Missing parameter 'PSNAME'"
    assert "FLAG1" in params, "Missing parameter 'FLAG1'"
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "LENGTH" in params, "Missing parameter 'LENGTH'"
    assert "SEGL" in params, "Missing parameter 'SEGL'"

def test_afptext::beginsegmentcommand_has_FLAG2():
    assert hasattr(afpText::BeginSegmentCommand, "FLAG2")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "FLAG2" in klass.__dict__:
            descriptor = klass.__dict__["FLAG2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::beginsegmentcommand_has_PSNAME():
    assert hasattr(afpText::BeginSegmentCommand, "PSNAME")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "PSNAME" in klass.__dict__:
            descriptor = klass.__dict__["PSNAME"]
            break
    assert isinstance(descriptor, property)

def test_afptext::beginsegmentcommand_has_FLAG1():
    assert hasattr(afpText::BeginSegmentCommand, "FLAG1")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "FLAG1" in klass.__dict__:
            descriptor = klass.__dict__["FLAG1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::beginsegmentcommand_has_NAME():
    assert hasattr(afpText::BeginSegmentCommand, "NAME")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
            break
    assert isinstance(descriptor, property)

def test_afptext::beginsegmentcommand_has_LENGTH():
    assert hasattr(afpText::BeginSegmentCommand, "LENGTH")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "LENGTH" in klass.__dict__:
            descriptor = klass.__dict__["LENGTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::beginsegmentcommand_has_SEGL():
    assert hasattr(afpText::BeginSegmentCommand, "SEGL")
    descriptor = None
    for klass in afpText::BeginSegmentCommand.__mro__:
        if "SEGL" in klass.__dict__:
            descriptor = klass.__dict__["SEGL"]
            break
    assert isinstance(descriptor, property)



def test_afptext::deviceappearance_is_not_abstract():
    assert not inspect.isabstract(afpText::DeviceAppearance)


def test_afptext::deviceappearance_constructor_exists():
    assert callable(afpText::DeviceAppearance.__init__)


def test_afptext::deviceappearance_constructor_args():
    sig = inspect.signature(afpText::DeviceAppearance.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "DevApp" in params, "Missing parameter 'DevApp'"

def test_afptext::deviceappearance_has_Reserved():
    assert hasattr(afpText::DeviceAppearance, "Reserved")
    descriptor = None
    for klass in afpText::DeviceAppearance.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::deviceappearance_has_DevApp():
    assert hasattr(afpText::DeviceAppearance, "DevApp")
    descriptor = None
    for klass in afpText::DeviceAppearance.__mro__:
        if "DevApp" in klass.__dict__:
            descriptor = klass.__dict__["DevApp"]
            break
    assert isinstance(descriptor, property)



def test_afptext::includetile_is_not_abstract():
    assert not inspect.isabstract(afpText::IncludeTile)


def test_afptext::includetile_constructor_exists():
    assert callable(afpText::IncludeTile.__init__)


def test_afptext::includetile_constructor_args():
    sig = inspect.signature(afpText::IncludeTile.__init__)
    params = list(sig.parameters.keys())
    assert "TIRID" in params, "Missing parameter 'TIRID'"

def test_afptext::includetile_has_TIRID():
    assert hasattr(afpText::IncludeTile, "TIRID")
    descriptor = None
    for klass in afpText::IncludeTile.__mro__:
        if "TIRID" in klass.__dict__:
            descriptor = klass.__dict__["TIRID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::textfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::TextFidelity)


def test_afptext::textfidelity_constructor_exists():
    assert callable(afpText::TextFidelity.__init__)


def test_afptext::textfidelity_constructor_args():
    sig = inspect.signature(afpText::TextFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "StpTxtEx" in params, "Missing parameter 'StpTxtEx'"
    assert "RepTxtEx" in params, "Missing parameter 'RepTxtEx'"

def test_afptext::textfidelity_has_StpTxtEx():
    assert hasattr(afpText::TextFidelity, "StpTxtEx")
    descriptor = None
    for klass in afpText::TextFidelity.__mro__:
        if "StpTxtEx" in klass.__dict__:
            descriptor = klass.__dict__["StpTxtEx"]
            break
    assert isinstance(descriptor, property)

def test_afptext::textfidelity_has_RepTxtEx():
    assert hasattr(afpText::TextFidelity, "RepTxtEx")
    descriptor = None
    for klass in afpText::TextFidelity.__mro__:
        if "RepTxtEx" in klass.__dict__:
            descriptor = klass.__dict__["RepTxtEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::crcresourcemanagement_is_not_abstract():
    assert not inspect.isabstract(afpText::CRCResourceManagement)


def test_afptext::crcresourcemanagement_constructor_exists():
    assert callable(afpText::CRCResourceManagement.__init__)


def test_afptext::crcresourcemanagement_constructor_args():
    sig = inspect.signature(afpText::CRCResourceManagement.__init__)
    params = list(sig.parameters.keys())
    assert "ResClassFlg" in params, "Missing parameter 'ResClassFlg'"
    assert "FmtQual" in params, "Missing parameter 'FmtQual'"
    assert "RMValue" in params, "Missing parameter 'RMValue'"

def test_afptext::crcresourcemanagement_has_ResClassFlg():
    assert hasattr(afpText::CRCResourceManagement, "ResClassFlg")
    descriptor = None
    for klass in afpText::CRCResourceManagement.__mro__:
        if "ResClassFlg" in klass.__dict__:
            descriptor = klass.__dict__["ResClassFlg"]
            break
    assert isinstance(descriptor, property)

def test_afptext::crcresourcemanagement_has_FmtQual():
    assert hasattr(afpText::CRCResourceManagement, "FmtQual")
    descriptor = None
    for klass in afpText::CRCResourceManagement.__mro__:
        if "FmtQual" in klass.__dict__:
            descriptor = klass.__dict__["FmtQual"]
            break
    assert isinstance(descriptor, property)

def test_afptext::crcresourcemanagement_has_RMValue():
    assert hasattr(afpText::CRCResourceManagement, "RMValue")
    descriptor = None
    for klass in afpText::CRCResourceManagement.__mro__:
        if "RMValue" in klass.__dict__:
            descriptor = klass.__dict__["RMValue"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pageoverlayconditionalprocessing_is_not_abstract():
    assert not inspect.isabstract(afpText::PageOverlayConditionalProcessing)


def test_afptext::pageoverlayconditionalprocessing_constructor_exists():
    assert callable(afpText::PageOverlayConditionalProcessing.__init__)


def test_afptext::pageoverlayconditionalprocessing_constructor_args():
    sig = inspect.signature(afpText::PageOverlayConditionalProcessing.__init__)
    params = list(sig.parameters.keys())
    assert "PgOvType" in params, "Missing parameter 'PgOvType'"
    assert "Level" in params, "Missing parameter 'Level'"

def test_afptext::pageoverlayconditionalprocessing_has_PgOvType():
    assert hasattr(afpText::PageOverlayConditionalProcessing, "PgOvType")
    descriptor = None
    for klass in afpText::PageOverlayConditionalProcessing.__mro__:
        if "PgOvType" in klass.__dict__:
            descriptor = klass.__dict__["PgOvType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pageoverlayconditionalprocessing_has_Level():
    assert hasattr(afpText::PageOverlayConditionalProcessing, "Level")
    descriptor = None
    for klass in afpText::PageOverlayConditionalProcessing.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gparc_is_not_abstract():
    assert not inspect.isabstract(afpText::GPARC)


def test_afptext::gparc_constructor_exists():
    assert callable(afpText::GPARC.__init__)


def test_afptext::gparc_constructor_args():
    sig = inspect.signature(afpText::GPARC.__init__)
    params = list(sig.parameters.keys())
    assert "SWEEP" in params, "Missing parameter 'SWEEP'"
    assert "START" in params, "Missing parameter 'START'"
    assert "XCENT" in params, "Missing parameter 'XCENT'"
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "YCENT" in params, "Missing parameter 'YCENT'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext::gparc_has_SWEEP():
    assert hasattr(afpText::GPARC, "SWEEP")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "SWEEP" in klass.__dict__:
            descriptor = klass.__dict__["SWEEP"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_START():
    assert hasattr(afpText::GPARC, "START")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "START" in klass.__dict__:
            descriptor = klass.__dict__["START"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_XCENT():
    assert hasattr(afpText::GPARC, "XCENT")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "XCENT" in klass.__dict__:
            descriptor = klass.__dict__["XCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_MFR():
    assert hasattr(afpText::GPARC, "MFR")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_YCENT():
    assert hasattr(afpText::GPARC, "YCENT")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "YCENT" in klass.__dict__:
            descriptor = klass.__dict__["YCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_YPOS():
    assert hasattr(afpText::GPARC, "YPOS")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_XPOS():
    assert hasattr(afpText::GPARC, "XPOS")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gparc_has_MH():
    assert hasattr(afpText::GPARC, "MH")
    descriptor = None
    for klass in afpText::GPARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imagesubsampling_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageSubsampling)


def test_afptext::imagesubsampling_constructor_exists():
    assert callable(afpText::ImageSubsampling.__init__)


def test_afptext::imagesubsampling_constructor_args():
    sig = inspect.signature(afpText::ImageSubsampling.__init__)
    params = list(sig.parameters.keys())



def test_afptext::tilesetcolor_is_not_abstract():
    assert not inspect.isabstract(afpText::TileSetColor)


def test_afptext::tilesetcolor_constructor_exists():
    assert callable(afpText::TileSetColor.__init__)


def test_afptext::tilesetcolor_constructor_args():
    sig = inspect.signature(afpText::TileSetColor.__init__)
    params = list(sig.parameters.keys())
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "SIZE3" in params, "Missing parameter 'SIZE3'"
    assert "CVAL2" in params, "Missing parameter 'CVAL2'"
    assert "SIZE4" in params, "Missing parameter 'SIZE4'"
    assert "CVAL3" in params, "Missing parameter 'CVAL3'"
    assert "SIZE1" in params, "Missing parameter 'SIZE1'"
    assert "CVAL4" in params, "Missing parameter 'CVAL4'"
    assert "CSPACE" in params, "Missing parameter 'CSPACE'"
    assert "CVAL1" in params, "Missing parameter 'CVAL1'"
    assert "SIZE2" in params, "Missing parameter 'SIZE2'"

def test_afptext::tilesetcolor_has_RESERVED():
    assert hasattr(afpText::TileSetColor, "RESERVED")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_SIZE3():
    assert hasattr(afpText::TileSetColor, "SIZE3")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "SIZE3" in klass.__dict__:
            descriptor = klass.__dict__["SIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_CVAL2():
    assert hasattr(afpText::TileSetColor, "CVAL2")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "CVAL2" in klass.__dict__:
            descriptor = klass.__dict__["CVAL2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_SIZE4():
    assert hasattr(afpText::TileSetColor, "SIZE4")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "SIZE4" in klass.__dict__:
            descriptor = klass.__dict__["SIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_CVAL3():
    assert hasattr(afpText::TileSetColor, "CVAL3")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "CVAL3" in klass.__dict__:
            descriptor = klass.__dict__["CVAL3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_SIZE1():
    assert hasattr(afpText::TileSetColor, "SIZE1")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "SIZE1" in klass.__dict__:
            descriptor = klass.__dict__["SIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_CVAL4():
    assert hasattr(afpText::TileSetColor, "CVAL4")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "CVAL4" in klass.__dict__:
            descriptor = klass.__dict__["CVAL4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_CSPACE():
    assert hasattr(afpText::TileSetColor, "CSPACE")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "CSPACE" in klass.__dict__:
            descriptor = klass.__dict__["CSPACE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_CVAL1():
    assert hasattr(afpText::TileSetColor, "CVAL1")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "CVAL1" in klass.__dict__:
            descriptor = klass.__dict__["CVAL1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tilesetcolor_has_SIZE2():
    assert hasattr(afpText::TileSetColor, "SIZE2")
    descriptor = None
    for klass in afpText::TileSetColor.__mro__:
        if "SIZE2" in klass.__dict__:
            descriptor = klass.__dict__["SIZE2"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsmt_is_not_abstract():
    assert not inspect.isabstract(afpText::GSMT)


def test_afptext::gsmt_constructor_exists():
    assert callable(afpText::GSMT.__init__)


def test_afptext::gsmt_constructor_args():
    sig = inspect.signature(afpText::GSMT.__init__)
    params = list(sig.parameters.keys())
    assert "MCPT" in params, "Missing parameter 'MCPT'"

def test_afptext::gsmt_has_MCPT():
    assert hasattr(afpText::GSMT, "MCPT")
    descriptor = None
    for klass in afpText::GSMT.__mro__:
        if "MCPT" in klass.__dict__:
            descriptor = klass.__dict__["MCPT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fonthorizontalscalefactor_is_not_abstract():
    assert not inspect.isabstract(afpText::FontHorizontalScaleFactor)


def test_afptext::fonthorizontalscalefactor_constructor_exists():
    assert callable(afpText::FontHorizontalScaleFactor.__init__)


def test_afptext::fonthorizontalscalefactor_constructor_args():
    sig = inspect.signature(afpText::FontHorizontalScaleFactor.__init__)
    params = list(sig.parameters.keys())
    assert "Hscale" in params, "Missing parameter 'Hscale'"

def test_afptext::fonthorizontalscalefactor_has_Hscale():
    assert hasattr(afpText::FontHorizontalScaleFactor, "Hscale")
    descriptor = None
    for klass in afpText::FontHorizontalScaleFactor.__mro__:
        if "Hscale" in klass.__dict__:
            descriptor = klass.__dict__["Hscale"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcrline_is_not_abstract():
    assert not inspect.isabstract(afpText::GCRLINE)


def test_afptext::gcrline_constructor_exists():
    assert callable(afpText::GCRLINE.__init__)


def test_afptext::gcrline_constructor_args():
    sig = inspect.signature(afpText::GCRLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext::cmrfidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::CMRFidelity)


def test_afptext::cmrfidelity_constructor_exists():
    assert callable(afpText::CMRFidelity.__init__)


def test_afptext::cmrfidelity_constructor_args():
    sig = inspect.signature(afpText::CMRFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "RepCMREx" in params, "Missing parameter 'RepCMREx'"
    assert "StpCMREx" in params, "Missing parameter 'StpCMREx'"

def test_afptext::cmrfidelity_has_RepCMREx():
    assert hasattr(afpText::CMRFidelity, "RepCMREx")
    descriptor = None
    for klass in afpText::CMRFidelity.__mro__:
        if "RepCMREx" in klass.__dict__:
            descriptor = klass.__dict__["RepCMREx"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cmrfidelity_has_StpCMREx():
    assert hasattr(afpText::CMRFidelity, "StpCMREx")
    descriptor = None
    for klass in afpText::CMRFidelity.__mro__:
        if "StpCMREx" in klass.__dict__:
            descriptor = klass.__dict__["StpCMREx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcmrk_is_not_abstract():
    assert not inspect.isabstract(afpText::GCMRK)


def test_afptext::gcmrk_constructor_exists():
    assert callable(afpText::GCMRK.__init__)


def test_afptext::gcmrk_constructor_args():
    sig = inspect.signature(afpText::GCMRK.__init__)
    params = list(sig.parameters.keys())



def test_afptext::extensionfont_is_not_abstract():
    assert not inspect.isabstract(afpText::ExtensionFont)


def test_afptext::extensionfont_constructor_exists():
    assert callable(afpText::ExtensionFont.__init__)


def test_afptext::extensionfont_constructor_args():
    sig = inspect.signature(afpText::ExtensionFont.__init__)
    params = list(sig.parameters.keys())
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"

def test_afptext::extensionfont_has_GCSGID():
    assert hasattr(afpText::ExtensionFont, "GCSGID")
    descriptor = None
    for klass in afpText::ExtensionFont.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::endtransparencymask_is_not_abstract():
    assert not inspect.isabstract(afpText::EndTransparencyMask)


def test_afptext::endtransparencymask_constructor_exists():
    assert callable(afpText::EndTransparencyMask.__init__)


def test_afptext::endtransparencymask_constructor_args():
    sig = inspect.signature(afpText::EndTransparencyMask.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mediumorientation_is_not_abstract():
    assert not inspect.isabstract(afpText::MediumOrientation)


def test_afptext::mediumorientation_constructor_exists():
    assert callable(afpText::MediumOrientation.__init__)


def test_afptext::mediumorientation_constructor_args():
    sig = inspect.signature(afpText::MediumOrientation.__init__)
    params = list(sig.parameters.keys())
    assert "MedOrient" in params, "Missing parameter 'MedOrient'"

def test_afptext::mediumorientation_has_MedOrient():
    assert hasattr(afpText::MediumOrientation, "MedOrient")
    descriptor = None
    for klass in afpText::MediumOrientation.__mro__:
        if "MedOrient" in klass.__dict__:
            descriptor = klass.__dict__["MedOrient"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gmrk_is_not_abstract():
    assert not inspect.isabstract(afpText::GMRK)


def test_afptext::gmrk_constructor_exists():
    assert callable(afpText::GMRK.__init__)


def test_afptext::gmrk_constructor_args():
    sig = inspect.signature(afpText::GMRK.__init__)
    params = list(sig.parameters.keys())



def test_afptext::imageresolution_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageResolution)


def test_afptext::imageresolution_constructor_exists():
    assert callable(afpText::ImageResolution.__init__)


def test_afptext::imageresolution_constructor_args():
    sig = inspect.signature(afpText::ImageResolution.__init__)
    params = list(sig.parameters.keys())
    assert "XBase" in params, "Missing parameter 'XBase'"
    assert "YBase" in params, "Missing parameter 'YBase'"
    assert "XResol" in params, "Missing parameter 'XResol'"
    assert "YResol" in params, "Missing parameter 'YResol'"

def test_afptext::imageresolution_has_XBase():
    assert hasattr(afpText::ImageResolution, "XBase")
    descriptor = None
    for klass in afpText::ImageResolution.__mro__:
        if "XBase" in klass.__dict__:
            descriptor = klass.__dict__["XBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imageresolution_has_YBase():
    assert hasattr(afpText::ImageResolution, "YBase")
    descriptor = None
    for klass in afpText::ImageResolution.__mro__:
        if "YBase" in klass.__dict__:
            descriptor = klass.__dict__["YBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imageresolution_has_XResol():
    assert hasattr(afpText::ImageResolution, "XResol")
    descriptor = None
    for klass in afpText::ImageResolution.__mro__:
        if "XResol" in klass.__dict__:
            descriptor = klass.__dict__["XResol"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imageresolution_has_YResol():
    assert hasattr(afpText::ImageResolution, "YResol")
    descriptor = None
    for klass in afpText::ImageResolution.__mro__:
        if "YResol" in klass.__dict__:
            descriptor = klass.__dict__["YResol"]
            break
    assert isinstance(descriptor, property)



def test_afptext::endsegment_is_not_abstract():
    assert not inspect.isabstract(afpText::EndSegment)


def test_afptext::endsegment_constructor_exists():
    assert callable(afpText::EndSegment.__init__)


def test_afptext::endsegment_constructor_args():
    sig = inspect.signature(afpText::EndSegment.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mediummappagenumber_is_not_abstract():
    assert not inspect.isabstract(afpText::MediumMapPageNumber)


def test_afptext::mediummappagenumber_constructor_exists():
    assert callable(afpText::MediumMapPageNumber.__init__)


def test_afptext::mediummappagenumber_constructor_args():
    sig = inspect.signature(afpText::MediumMapPageNumber.__init__)
    params = list(sig.parameters.keys())
    assert "PageNum" in params, "Missing parameter 'PageNum'"

def test_afptext::mediummappagenumber_has_PageNum():
    assert hasattr(afpText::MediumMapPageNumber, "PageNum")
    descriptor = None
    for klass in afpText::MediumMapPageNumber.__mro__:
        if "PageNum" in klass.__dict__:
            descriptor = klass.__dict__["PageNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcflt_is_not_abstract():
    assert not inspect.isabstract(afpText::GCFLT)


def test_afptext::gcflt_constructor_exists():
    assert callable(afpText::GCFLT.__init__)


def test_afptext::gcflt_constructor_args():
    sig = inspect.signature(afpText::GCFLT.__init__)
    params = list(sig.parameters.keys())



def test_afptext::samplingratios_is_not_abstract():
    assert not inspect.isabstract(afpText::SamplingRatios)


def test_afptext::samplingratios_constructor_exists():
    assert callable(afpText::SamplingRatios.__init__)


def test_afptext::samplingratios_constructor_args():
    sig = inspect.signature(afpText::SamplingRatios.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gscr_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCR)


def test_afptext::gscr_constructor_exists():
    assert callable(afpText::GSCR.__init__)


def test_afptext::gscr_constructor_args():
    sig = inspect.signature(afpText::GSCR.__init__)
    params = list(sig.parameters.keys())
    assert "PREC" in params, "Missing parameter 'PREC'"

def test_afptext::gscr_has_PREC():
    assert hasattr(afpText::GSCR, "PREC")
    descriptor = None
    for klass in afpText::GSCR.__mro__:
        if "PREC" in klass.__dict__:
            descriptor = klass.__dict__["PREC"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gscc_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCC)


def test_afptext::gscc_constructor_exists():
    assert callable(afpText::GSCC.__init__)


def test_afptext::gscc_constructor_args():
    sig = inspect.signature(afpText::GSCC.__init__)
    params = list(sig.parameters.keys())
    assert "CELLHFR" in params, "Missing parameter 'CELLHFR'"
    assert "CELLWI" in params, "Missing parameter 'CELLWI'"
    assert "CELLWFR" in params, "Missing parameter 'CELLWFR'"
    assert "CELLHI" in params, "Missing parameter 'CELLHI'"

def test_afptext::gscc_has_CELLHFR():
    assert hasattr(afpText::GSCC, "CELLHFR")
    descriptor = None
    for klass in afpText::GSCC.__mro__:
        if "CELLHFR" in klass.__dict__:
            descriptor = klass.__dict__["CELLHFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gscc_has_CELLWI():
    assert hasattr(afpText::GSCC, "CELLWI")
    descriptor = None
    for klass in afpText::GSCC.__mro__:
        if "CELLWI" in klass.__dict__:
            descriptor = klass.__dict__["CELLWI"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gscc_has_CELLWFR():
    assert hasattr(afpText::GSCC, "CELLWFR")
    descriptor = None
    for klass in afpText::GSCC.__mro__:
        if "CELLWFR" in klass.__dict__:
            descriptor = klass.__dict__["CELLWFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gscc_has_CELLHI():
    assert hasattr(afpText::GSCC, "CELLHI")
    descriptor = None
    for klass in afpText::GSCC.__mro__:
        if "CELLHI" in klass.__dict__:
            descriptor = klass.__dict__["CELLHI"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mappingoption_is_not_abstract():
    assert not inspect.isabstract(afpText::MappingOption)


def test_afptext::mappingoption_constructor_exists():
    assert callable(afpText::MappingOption.__init__)


def test_afptext::mappingoption_constructor_args():
    sig = inspect.signature(afpText::MappingOption.__init__)
    params = list(sig.parameters.keys())
    assert "MapValue" in params, "Missing parameter 'MapValue'"

def test_afptext::mappingoption_has_MapValue():
    assert hasattr(afpText::MappingOption, "MapValue")
    descriptor = None
    for klass in afpText::MappingOption.__mro__:
        if "MapValue" in klass.__dict__:
            descriptor = klass.__dict__["MapValue"]
            break
    assert isinstance(descriptor, property)



def test_afptext::localdateandtimestamp_is_not_abstract():
    assert not inspect.isabstract(afpText::LocalDateAndTimeStamp)


def test_afptext::localdateandtimestamp_constructor_exists():
    assert callable(afpText::LocalDateAndTimeStamp.__init__)


def test_afptext::localdateandtimestamp_constructor_args():
    sig = inspect.signature(afpText::LocalDateAndTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "Hour" in params, "Missing parameter 'Hour'"
    assert "Minute" in params, "Missing parameter 'Minute'"
    assert "HundSec" in params, "Missing parameter 'HundSec'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "THunYear" in params, "Missing parameter 'THunYear'"
    assert "StampType" in params, "Missing parameter 'StampType'"
    assert "TenYear" in params, "Missing parameter 'TenYear'"
    assert "Second" in params, "Missing parameter 'Second'"

def test_afptext::localdateandtimestamp_has_Hour():
    assert hasattr(afpText::LocalDateAndTimeStamp, "Hour")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "Hour" in klass.__dict__:
            descriptor = klass.__dict__["Hour"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_Minute():
    assert hasattr(afpText::LocalDateAndTimeStamp, "Minute")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "Minute" in klass.__dict__:
            descriptor = klass.__dict__["Minute"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_HundSec():
    assert hasattr(afpText::LocalDateAndTimeStamp, "HundSec")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "HundSec" in klass.__dict__:
            descriptor = klass.__dict__["HundSec"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_Day():
    assert hasattr(afpText::LocalDateAndTimeStamp, "Day")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "Day" in klass.__dict__:
            descriptor = klass.__dict__["Day"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_THunYear():
    assert hasattr(afpText::LocalDateAndTimeStamp, "THunYear")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "THunYear" in klass.__dict__:
            descriptor = klass.__dict__["THunYear"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_StampType():
    assert hasattr(afpText::LocalDateAndTimeStamp, "StampType")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "StampType" in klass.__dict__:
            descriptor = klass.__dict__["StampType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_TenYear():
    assert hasattr(afpText::LocalDateAndTimeStamp, "TenYear")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "TenYear" in klass.__dict__:
            descriptor = klass.__dict__["TenYear"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localdateandtimestamp_has_Second():
    assert hasattr(afpText::LocalDateAndTimeStamp, "Second")
    descriptor = None
    for klass in afpText::LocalDateAndTimeStamp.__mro__:
        if "Second" in klass.__dict__:
            descriptor = klass.__dict__["Second"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsca_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCA)


def test_afptext::gsca_constructor_exists():
    assert callable(afpText::GSCA.__init__)


def test_afptext::gsca_constructor_args():
    sig = inspect.signature(afpText::GSCA.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext::gsca_has_XPOS():
    assert hasattr(afpText::GSCA, "XPOS")
    descriptor = None
    for klass in afpText::GSCA.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsca_has_YPOS():
    assert hasattr(afpText::GSCA, "YPOS")
    descriptor = None
    for klass in afpText::GSCA.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectoffset_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectOffset)


def test_afptext::objectoffset_constructor_exists():
    assert callable(afpText::ObjectOffset.__init__)


def test_afptext::objectoffset_constructor_args():
    sig = inspect.signature(afpText::ObjectOffset.__init__)
    params = list(sig.parameters.keys())
    assert "ObjOset" in params, "Missing parameter 'ObjOset'"
    assert "ObjTpe" in params, "Missing parameter 'ObjTpe'"
    assert "ObjOstHi" in params, "Missing parameter 'ObjOstHi'"

def test_afptext::objectoffset_has_ObjOset():
    assert hasattr(afpText::ObjectOffset, "ObjOset")
    descriptor = None
    for klass in afpText::ObjectOffset.__mro__:
        if "ObjOset" in klass.__dict__:
            descriptor = klass.__dict__["ObjOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectoffset_has_ObjTpe():
    assert hasattr(afpText::ObjectOffset, "ObjTpe")
    descriptor = None
    for klass in afpText::ObjectOffset.__mro__:
        if "ObjTpe" in klass.__dict__:
            descriptor = klass.__dict__["ObjTpe"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectoffset_has_ObjOstHi():
    assert hasattr(afpText::ObjectOffset, "ObjOstHi")
    descriptor = None
    for klass in afpText::ObjectOffset.__mro__:
        if "ObjOstHi" in klass.__dict__:
            descriptor = klass.__dict__["ObjOstHi"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fullyqualifiedname_is_not_abstract():
    assert not inspect.isabstract(afpText::FullyQualifiedName)


def test_afptext::fullyqualifiedname_constructor_exists():
    assert callable(afpText::FullyQualifiedName.__init__)


def test_afptext::fullyqualifiedname_constructor_args():
    sig = inspect.signature(afpText::FullyQualifiedName.__init__)
    params = list(sig.parameters.keys())
    assert "FQNFormat" in params, "Missing parameter 'FQNFormat'"
    assert "FQNType" in params, "Missing parameter 'FQNType'"
    assert "FQName" in params, "Missing parameter 'FQName'"

def test_afptext::fullyqualifiedname_has_FQNFormat():
    assert hasattr(afpText::FullyQualifiedName, "FQNFormat")
    descriptor = None
    for klass in afpText::FullyQualifiedName.__mro__:
        if "FQNFormat" in klass.__dict__:
            descriptor = klass.__dict__["FQNFormat"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fullyqualifiedname_has_FQNType():
    assert hasattr(afpText::FullyQualifiedName, "FQNType")
    descriptor = None
    for klass in afpText::FullyQualifiedName.__mro__:
        if "FQNType" in klass.__dict__:
            descriptor = klass.__dict__["FQNType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fullyqualifiedname_has_FQName():
    assert hasattr(afpText::FullyQualifiedName, "FQName")
    descriptor = None
    for klass in afpText::FullyQualifiedName.__mro__:
        if "FQName" in klass.__dict__:
            descriptor = klass.__dict__["FQName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imagedata_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageData)


def test_afptext::imagedata_constructor_exists():
    assert callable(afpText::ImageData.__init__)


def test_afptext::imagedata_constructor_args():
    sig = inspect.signature(afpText::ImageData.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::imagedata_has_DATA():
    assert hasattr(afpText::ImageData, "DATA")
    descriptor = None
    for klass in afpText::ImageData.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectoriginidentifier_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectOriginIdentifier)


def test_afptext::objectoriginidentifier_constructor_exists():
    assert callable(afpText::ObjectOriginIdentifier.__init__)


def test_afptext::objectoriginidentifier_constructor_args():
    sig = inspect.signature(afpText::ObjectOriginIdentifier.__init__)
    params = list(sig.parameters.keys())
    assert "MedID" in params, "Missing parameter 'MedID'"
    assert "System" in params, "Missing parameter 'System'"
    assert "DSID" in params, "Missing parameter 'DSID'"
    assert "SysID" in params, "Missing parameter 'SysID'"

def test_afptext::objectoriginidentifier_has_MedID():
    assert hasattr(afpText::ObjectOriginIdentifier, "MedID")
    descriptor = None
    for klass in afpText::ObjectOriginIdentifier.__mro__:
        if "MedID" in klass.__dict__:
            descriptor = klass.__dict__["MedID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectoriginidentifier_has_System():
    assert hasattr(afpText::ObjectOriginIdentifier, "System")
    descriptor = None
    for klass in afpText::ObjectOriginIdentifier.__mro__:
        if "System" in klass.__dict__:
            descriptor = klass.__dict__["System"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectoriginidentifier_has_DSID():
    assert hasattr(afpText::ObjectOriginIdentifier, "DSID")
    descriptor = None
    for klass in afpText::ObjectOriginIdentifier.__mro__:
        if "DSID" in klass.__dict__:
            descriptor = klass.__dict__["DSID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectoriginidentifier_has_SysID():
    assert hasattr(afpText::ObjectOriginIdentifier, "SysID")
    descriptor = None
    for klass in afpText::ObjectOriginIdentifier.__mro__:
        if "SysID" in klass.__dict__:
            descriptor = klass.__dict__["SysID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gslj_is_not_abstract():
    assert not inspect.isabstract(afpText::GSLJ)


def test_afptext::gslj_constructor_exists():
    assert callable(afpText::GSLJ.__init__)


def test_afptext::gslj_constructor_args():
    sig = inspect.signature(afpText::GSLJ.__init__)
    params = list(sig.parameters.keys())
    assert "LINEJOIN" in params, "Missing parameter 'LINEJOIN'"

def test_afptext::gslj_has_LINEJOIN():
    assert hasattr(afpText::GSLJ, "LINEJOIN")
    descriptor = None
    for klass in afpText::GSLJ.__mro__:
        if "LINEJOIN" in klass.__dict__:
            descriptor = klass.__dict__["LINEJOIN"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gflt_is_not_abstract():
    assert not inspect.isabstract(afpText::GFLT)


def test_afptext::gflt_constructor_exists():
    assert callable(afpText::GFLT.__init__)


def test_afptext::gflt_constructor_args():
    sig = inspect.signature(afpText::GFLT.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gsle_is_not_abstract():
    assert not inspect.isabstract(afpText::GSLE)


def test_afptext::gsle_constructor_exists():
    assert callable(afpText::GSLE.__init__)


def test_afptext::gsle_constructor_args():
    sig = inspect.signature(afpText::GSLE.__init__)
    params = list(sig.parameters.keys())
    assert "LINEEND" in params, "Missing parameter 'LINEEND'"

def test_afptext::gsle_has_LINEEND():
    assert hasattr(afpText::GSLE, "LINEEND")
    descriptor = None
    for klass in afpText::GSLE.__mro__:
        if "LINEEND" in klass.__dict__:
            descriptor = klass.__dict__["LINEEND"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gfarc_is_not_abstract():
    assert not inspect.isabstract(afpText::GFARC)


def test_afptext::gfarc_constructor_exists():
    assert callable(afpText::GFARC.__init__)


def test_afptext::gfarc_constructor_args():
    sig = inspect.signature(afpText::GFARC.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "MFR" in params, "Missing parameter 'MFR'"

def test_afptext::gfarc_has_MH():
    assert hasattr(afpText::GFARC, "MH")
    descriptor = None
    for klass in afpText::GFARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gfarc_has_YPOS():
    assert hasattr(afpText::GFARC, "YPOS")
    descriptor = None
    for klass in afpText::GFARC.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gfarc_has_XPOS():
    assert hasattr(afpText::GFARC, "XPOS")
    descriptor = None
    for klass in afpText::GFARC.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gfarc_has_MFR():
    assert hasattr(afpText::GFARC, "MFR")
    descriptor = None
    for klass in afpText::GFARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imagelutid_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageLUTID)


def test_afptext::imagelutid_constructor_exists():
    assert callable(afpText::ImageLUTID.__init__)


def test_afptext::imagelutid_constructor_args():
    sig = inspect.signature(afpText::ImageLUTID.__init__)
    params = list(sig.parameters.keys())
    assert "LUTID" in params, "Missing parameter 'LUTID'"

def test_afptext::imagelutid_has_LUTID():
    assert hasattr(afpText::ImageLUTID, "LUTID")
    descriptor = None
    for klass in afpText::ImageLUTID.__mro__:
        if "LUTID" in klass.__dict__:
            descriptor = klass.__dict__["LUTID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::geimg_is_not_abstract():
    assert not inspect.isabstract(afpText::GEIMG)


def test_afptext::geimg_constructor_exists():
    assert callable(afpText::GEIMG.__init__)


def test_afptext::geimg_constructor_args():
    sig = inspect.signature(afpText::GEIMG.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::geimg_has_DATA():
    assert hasattr(afpText::GEIMG, "DATA")
    descriptor = None
    for klass in afpText::GEIMG.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mediafidelity_is_not_abstract():
    assert not inspect.isabstract(afpText::MediaFidelity)


def test_afptext::mediafidelity_constructor_exists():
    assert callable(afpText::MediaFidelity.__init__)


def test_afptext::mediafidelity_constructor_args():
    sig = inspect.signature(afpText::MediaFidelity.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "StpMedEx" in params, "Missing parameter 'StpMedEx'"

def test_afptext::mediafidelity_has_Reserved():
    assert hasattr(afpText::MediaFidelity, "Reserved")
    descriptor = None
    for klass in afpText::MediaFidelity.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mediafidelity_has_StpMedEx():
    assert hasattr(afpText::MediaFidelity, "StpMedEx")
    descriptor = None
    for klass in afpText::MediaFidelity.__mro__:
        if "StpMedEx" in klass.__dict__:
            descriptor = klass.__dict__["StpMedEx"]
            break
    assert isinstance(descriptor, property)



def test_afptext::modcainterchangeset_is_not_abstract():
    assert not inspect.isabstract(afpText::MODCAInterchangeSet)


def test_afptext::modcainterchangeset_constructor_exists():
    assert callable(afpText::MODCAInterchangeSet.__init__)


def test_afptext::modcainterchangeset_constructor_args():
    sig = inspect.signature(afpText::MODCAInterchangeSet.__init__)
    params = list(sig.parameters.keys())
    assert "ISid" in params, "Missing parameter 'ISid'"
    assert "IStype" in params, "Missing parameter 'IStype'"

def test_afptext::modcainterchangeset_has_ISid():
    assert hasattr(afpText::MODCAInterchangeSet, "ISid")
    descriptor = None
    for klass in afpText::MODCAInterchangeSet.__mro__:
        if "ISid" in klass.__dict__:
            descriptor = klass.__dict__["ISid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::modcainterchangeset_has_IStype():
    assert hasattr(afpText::MODCAInterchangeSet, "IStype")
    descriptor = None
    for klass in afpText::MODCAInterchangeSet.__mro__:
        if "IStype" in klass.__dict__:
            descriptor = klass.__dict__["IStype"]
            break
    assert isinstance(descriptor, property)



def test_afptext::grline_is_not_abstract():
    assert not inspect.isabstract(afpText::GRLINE)


def test_afptext::grline_constructor_exists():
    assert callable(afpText::GRLINE.__init__)


def test_afptext::grline_constructor_args():
    sig = inspect.signature(afpText::GRLINE.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::grline_has_YPOS():
    assert hasattr(afpText::GRLINE, "YPOS")
    descriptor = None
    for klass in afpText::GRLINE.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::grline_has_XPOS():
    assert hasattr(afpText::GRLINE, "XPOS")
    descriptor = None
    for klass in afpText::GRLINE.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::endsegmentcommand_is_not_abstract():
    assert not inspect.isabstract(afpText::EndSegmentCommand)


def test_afptext::endsegmentcommand_constructor_exists():
    assert callable(afpText::EndSegmentCommand.__init__)


def test_afptext::endsegmentcommand_constructor_args():
    sig = inspect.signature(afpText::EndSegmentCommand.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gcbox_is_not_abstract():
    assert not inspect.isabstract(afpText::GCBOX)


def test_afptext::gcbox_constructor_exists():
    assert callable(afpText::GCBOX.__init__)


def test_afptext::gcbox_constructor_args():
    sig = inspect.signature(afpText::GCBOX.__init__)
    params = list(sig.parameters.keys())
    assert "HAXIS" in params, "Missing parameter 'HAXIS'"
    assert "XPOS1" in params, "Missing parameter 'XPOS1'"
    assert "VAXIS" in params, "Missing parameter 'VAXIS'"
    assert "RES" in params, "Missing parameter 'RES'"
    assert "YPOS1" in params, "Missing parameter 'YPOS1'"

def test_afptext::gcbox_has_HAXIS():
    assert hasattr(afpText::GCBOX, "HAXIS")
    descriptor = None
    for klass in afpText::GCBOX.__mro__:
        if "HAXIS" in klass.__dict__:
            descriptor = klass.__dict__["HAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbox_has_XPOS1():
    assert hasattr(afpText::GCBOX, "XPOS1")
    descriptor = None
    for klass in afpText::GCBOX.__mro__:
        if "XPOS1" in klass.__dict__:
            descriptor = klass.__dict__["XPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbox_has_VAXIS():
    assert hasattr(afpText::GCBOX, "VAXIS")
    descriptor = None
    for klass in afpText::GCBOX.__mro__:
        if "VAXIS" in klass.__dict__:
            descriptor = klass.__dict__["VAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbox_has_RES():
    assert hasattr(afpText::GCBOX, "RES")
    descriptor = None
    for klass in afpText::GCBOX.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbox_has_YPOS1():
    assert hasattr(afpText::GCBOX, "YPOS1")
    descriptor = None
    for klass in afpText::GCBOX.__mro__:
        if "YPOS1" in klass.__dict__:
            descriptor = klass.__dict__["YPOS1"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectstructuredfieldextent_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectStructuredFieldExtent)


def test_afptext::objectstructuredfieldextent_constructor_exists():
    assert callable(afpText::ObjectStructuredFieldExtent.__init__)


def test_afptext::objectstructuredfieldextent_constructor_args():
    sig = inspect.signature(afpText::ObjectStructuredFieldExtent.__init__)
    params = list(sig.parameters.keys())
    assert "SFExtHi" in params, "Missing parameter 'SFExtHi'"
    assert "SFExt" in params, "Missing parameter 'SFExt'"

def test_afptext::objectstructuredfieldextent_has_SFExtHi():
    assert hasattr(afpText::ObjectStructuredFieldExtent, "SFExtHi")
    descriptor = None
    for klass in afpText::ObjectStructuredFieldExtent.__mro__:
        if "SFExtHi" in klass.__dict__:
            descriptor = klass.__dict__["SFExtHi"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectstructuredfieldextent_has_SFExt():
    assert hasattr(afpText::ObjectStructuredFieldExtent, "SFExt")
    descriptor = None
    for klass in afpText::ObjectStructuredFieldExtent.__mro__:
        if "SFExt" in klass.__dict__:
            descriptor = klass.__dict__["SFExt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::begintile_is_not_abstract():
    assert not inspect.isabstract(afpText::BeginTile)


def test_afptext::begintile_constructor_exists():
    assert callable(afpText::BeginTile.__init__)


def test_afptext::begintile_constructor_args():
    sig = inspect.signature(afpText::BeginTile.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gcparc_is_not_abstract():
    assert not inspect.isabstract(afpText::GCPARC)


def test_afptext::gcparc_constructor_exists():
    assert callable(afpText::GCPARC.__init__)


def test_afptext::gcparc_constructor_args():
    sig = inspect.signature(afpText::GCPARC.__init__)
    params = list(sig.parameters.keys())
    assert "XCENT" in params, "Missing parameter 'XCENT'"
    assert "SWEEP" in params, "Missing parameter 'SWEEP'"
    assert "YCENT" in params, "Missing parameter 'YCENT'"
    assert "START" in params, "Missing parameter 'START'"
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext::gcparc_has_XCENT():
    assert hasattr(afpText::GCPARC, "XCENT")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "XCENT" in klass.__dict__:
            descriptor = klass.__dict__["XCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcparc_has_SWEEP():
    assert hasattr(afpText::GCPARC, "SWEEP")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "SWEEP" in klass.__dict__:
            descriptor = klass.__dict__["SWEEP"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcparc_has_YCENT():
    assert hasattr(afpText::GCPARC, "YCENT")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "YCENT" in klass.__dict__:
            descriptor = klass.__dict__["YCENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcparc_has_START():
    assert hasattr(afpText::GCPARC, "START")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "START" in klass.__dict__:
            descriptor = klass.__dict__["START"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcparc_has_MFR():
    assert hasattr(afpText::GCPARC, "MFR")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcparc_has_MH():
    assert hasattr(afpText::GCPARC, "MH")
    descriptor = None
    for klass in afpText::GCPARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gnop1_is_not_abstract():
    assert not inspect.isabstract(afpText::GNOP1)


def test_afptext::gnop1_constructor_exists():
    assert callable(afpText::GNOP1.__init__)


def test_afptext::gnop1_constructor_args():
    sig = inspect.signature(afpText::GNOP1.__init__)
    params = list(sig.parameters.keys())



def test_afptext::localeselector_is_not_abstract():
    assert not inspect.isabstract(afpText::LocaleSelector)


def test_afptext::localeselector_constructor_exists():
    assert callable(afpText::LocaleSelector.__init__)


def test_afptext::localeselector_constructor_args():
    sig = inspect.signature(afpText::LocaleSelector.__init__)
    params = list(sig.parameters.keys())
    assert "LangCode" in params, "Missing parameter 'LangCode'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "RegCde" in params, "Missing parameter 'RegCde'"
    assert "ScrptCde" in params, "Missing parameter 'ScrptCde'"
    assert "LocFlgs" in params, "Missing parameter 'LocFlgs'"
    assert "VarCde" in params, "Missing parameter 'VarCde'"

def test_afptext::localeselector_has_LangCode():
    assert hasattr(afpText::LocaleSelector, "LangCode")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "LangCode" in klass.__dict__:
            descriptor = klass.__dict__["LangCode"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localeselector_has_Reserved():
    assert hasattr(afpText::LocaleSelector, "Reserved")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localeselector_has_RegCde():
    assert hasattr(afpText::LocaleSelector, "RegCde")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "RegCde" in klass.__dict__:
            descriptor = klass.__dict__["RegCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localeselector_has_ScrptCde():
    assert hasattr(afpText::LocaleSelector, "ScrptCde")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "ScrptCde" in klass.__dict__:
            descriptor = klass.__dict__["ScrptCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localeselector_has_LocFlgs():
    assert hasattr(afpText::LocaleSelector, "LocFlgs")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "LocFlgs" in klass.__dict__:
            descriptor = klass.__dict__["LocFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::localeselector_has_VarCde():
    assert hasattr(afpText::LocaleSelector, "VarCde")
    descriptor = None
    for klass in afpText::LocaleSelector.__mro__:
        if "VarCde" in klass.__dict__:
            descriptor = klass.__dict__["VarCde"]
            break
    assert isinstance(descriptor, property)



def test_afptext::renderingintent_is_not_abstract():
    assert not inspect.isabstract(afpText::RenderingIntent)


def test_afptext::renderingintent_constructor_exists():
    assert callable(afpText::RenderingIntent.__init__)


def test_afptext::renderingintent_constructor_args():
    sig = inspect.signature(afpText::RenderingIntent.__init__)
    params = list(sig.parameters.keys())
    assert "IOCARI" in params, "Missing parameter 'IOCARI'"
    assert "OCRI" in params, "Missing parameter 'OCRI'"
    assert "PTOCRI" in params, "Missing parameter 'PTOCRI'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "GOCARI" in params, "Missing parameter 'GOCARI'"

def test_afptext::renderingintent_has_IOCARI():
    assert hasattr(afpText::RenderingIntent, "IOCARI")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "IOCARI" in klass.__dict__:
            descriptor = klass.__dict__["IOCARI"]
            break
    assert isinstance(descriptor, property)

def test_afptext::renderingintent_has_OCRI():
    assert hasattr(afpText::RenderingIntent, "OCRI")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "OCRI" in klass.__dict__:
            descriptor = klass.__dict__["OCRI"]
            break
    assert isinstance(descriptor, property)

def test_afptext::renderingintent_has_PTOCRI():
    assert hasattr(afpText::RenderingIntent, "PTOCRI")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "PTOCRI" in klass.__dict__:
            descriptor = klass.__dict__["PTOCRI"]
            break
    assert isinstance(descriptor, property)

def test_afptext::renderingintent_has_Reserved():
    assert hasattr(afpText::RenderingIntent, "Reserved")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::renderingintent_has_Reserved2():
    assert hasattr(afpText::RenderingIntent, "Reserved2")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::renderingintent_has_GOCARI():
    assert hasattr(afpText::RenderingIntent, "GOCARI")
    descriptor = None
    for klass in afpText::RenderingIntent.__mro__:
        if "GOCARI" in klass.__dict__:
            descriptor = klass.__dict__["GOCARI"]
            break
    assert isinstance(descriptor, property)



def test_afptext::presentationspaceresetmixing_is_not_abstract():
    assert not inspect.isabstract(afpText::PresentationSpaceResetMixing)


def test_afptext::presentationspaceresetmixing_constructor_exists():
    assert callable(afpText::PresentationSpaceResetMixing.__init__)


def test_afptext::presentationspaceresetmixing_constructor_args():
    sig = inspect.signature(afpText::PresentationSpaceResetMixing.__init__)
    params = list(sig.parameters.keys())
    assert "BgMxFlag" in params, "Missing parameter 'BgMxFlag'"

def test_afptext::presentationspaceresetmixing_has_BgMxFlag():
    assert hasattr(afpText::PresentationSpaceResetMixing, "BgMxFlag")
    descriptor = None
    for klass in afpText::PresentationSpaceResetMixing.__mro__:
        if "BgMxFlag" in klass.__dict__:
            descriptor = klass.__dict__["BgMxFlag"]
            break
    assert isinstance(descriptor, property)



def test_afptext::up3ifinishingoperation_is_not_abstract():
    assert not inspect.isabstract(afpText::UP3iFinishingOperation)


def test_afptext::up3ifinishingoperation_constructor_exists():
    assert callable(afpText::UP3iFinishingOperation.__init__)


def test_afptext::up3ifinishingoperation_constructor_args():
    sig = inspect.signature(afpText::UP3iFinishingOperation.__init__)
    params = list(sig.parameters.keys())
    assert "Seqnum" in params, "Missing parameter 'Seqnum'"
    assert "UP3iDat" in params, "Missing parameter 'UP3iDat'"

def test_afptext::up3ifinishingoperation_has_Seqnum():
    assert hasattr(afpText::UP3iFinishingOperation, "Seqnum")
    descriptor = None
    for klass in afpText::UP3iFinishingOperation.__mro__:
        if "Seqnum" in klass.__dict__:
            descriptor = klass.__dict__["Seqnum"]
            break
    assert isinstance(descriptor, property)

def test_afptext::up3ifinishingoperation_has_UP3iDat():
    assert hasattr(afpText::UP3iFinishingOperation, "UP3iDat")
    descriptor = None
    for klass in afpText::UP3iFinishingOperation.__mro__:
        if "UP3iDat" in klass.__dict__:
            descriptor = klass.__dict__["UP3iDat"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gear_is_not_abstract():
    assert not inspect.isabstract(afpText::GEAR)


def test_afptext::gear_constructor_exists():
    assert callable(afpText::GEAR.__init__)


def test_afptext::gear_constructor_args():
    sig = inspect.signature(afpText::GEAR.__init__)
    params = list(sig.parameters.keys())
    assert "DATA" in params, "Missing parameter 'DATA'"

def test_afptext::gear_has_DATA():
    assert hasattr(afpText::GEAR, "DATA")
    descriptor = None
    for klass in afpText::GEAR.__mro__:
        if "DATA" in klass.__dict__:
            descriptor = klass.__dict__["DATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::resourceusageattribute_is_not_abstract():
    assert not inspect.isabstract(afpText::ResourceUsageAttribute)


def test_afptext::resourceusageattribute_constructor_exists():
    assert callable(afpText::ResourceUsageAttribute.__init__)


def test_afptext::resourceusageattribute_constructor_args():
    sig = inspect.signature(afpText::ResourceUsageAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "Frequency" in params, "Missing parameter 'Frequency'"

def test_afptext::resourceusageattribute_has_Frequency():
    assert hasattr(afpText::ResourceUsageAttribute, "Frequency")
    descriptor = None
    for klass in afpText::ResourceUsageAttribute.__mro__:
        if "Frequency" in klass.__dict__:
            descriptor = klass.__dict__["Frequency"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcfarc_is_not_abstract():
    assert not inspect.isabstract(afpText::GCFARC)


def test_afptext::gcfarc_constructor_exists():
    assert callable(afpText::GCFARC.__init__)


def test_afptext::gcfarc_constructor_args():
    sig = inspect.signature(afpText::GCFARC.__init__)
    params = list(sig.parameters.keys())
    assert "MFR" in params, "Missing parameter 'MFR'"
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext::gcfarc_has_MFR():
    assert hasattr(afpText::GCFARC, "MFR")
    descriptor = None
    for klass in afpText::GCFARC.__mro__:
        if "MFR" in klass.__dict__:
            descriptor = klass.__dict__["MFR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcfarc_has_MH():
    assert hasattr(afpText::GCFARC, "MH")
    descriptor = None
    for klass in afpText::GCFARC.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imagesize_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageSize)


def test_afptext::imagesize_constructor_exists():
    assert callable(afpText::ImageSize.__init__)


def test_afptext::imagesize_constructor_args():
    sig = inspect.signature(afpText::ImageSize.__init__)
    params = list(sig.parameters.keys())
    assert "UNITBASE" in params, "Missing parameter 'UNITBASE'"
    assert "HSIZE" in params, "Missing parameter 'HSIZE'"
    assert "VRESOL" in params, "Missing parameter 'VRESOL'"
    assert "VSIZE" in params, "Missing parameter 'VSIZE'"
    assert "HRESOL" in params, "Missing parameter 'HRESOL'"

def test_afptext::imagesize_has_UNITBASE():
    assert hasattr(afpText::ImageSize, "UNITBASE")
    descriptor = None
    for klass in afpText::ImageSize.__mro__:
        if "UNITBASE" in klass.__dict__:
            descriptor = klass.__dict__["UNITBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imagesize_has_HSIZE():
    assert hasattr(afpText::ImageSize, "HSIZE")
    descriptor = None
    for klass in afpText::ImageSize.__mro__:
        if "HSIZE" in klass.__dict__:
            descriptor = klass.__dict__["HSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imagesize_has_VRESOL():
    assert hasattr(afpText::ImageSize, "VRESOL")
    descriptor = None
    for klass in afpText::ImageSize.__mro__:
        if "VRESOL" in klass.__dict__:
            descriptor = klass.__dict__["VRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imagesize_has_VSIZE():
    assert hasattr(afpText::ImageSize, "VSIZE")
    descriptor = None
    for klass in afpText::ImageSize.__mro__:
        if "VSIZE" in klass.__dict__:
            descriptor = klass.__dict__["VSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imagesize_has_HRESOL():
    assert hasattr(afpText::ImageSize, "HRESOL")
    descriptor = None
    for klass in afpText::ImageSize.__mro__:
        if "HRESOL" in klass.__dict__:
            descriptor = klass.__dict__["HRESOL"]
            break
    assert isinstance(descriptor, property)



def test_afptext::presentationspacemixingrules_is_not_abstract():
    assert not inspect.isabstract(afpText::PresentationSpaceMixingRules)


def test_afptext::presentationspacemixingrules_constructor_exists():
    assert callable(afpText::PresentationSpaceMixingRules.__init__)


def test_afptext::presentationspacemixingrules_constructor_args():
    sig = inspect.signature(afpText::PresentationSpaceMixingRules.__init__)
    params = list(sig.parameters.keys())



def test_afptext::resourceobjectinclude_is_not_abstract():
    assert not inspect.isabstract(afpText::ResourceObjectInclude)


def test_afptext::resourceobjectinclude_constructor_exists():
    assert callable(afpText::ResourceObjectInclude.__init__)


def test_afptext::resourceobjectinclude_constructor_args():
    sig = inspect.signature(afpText::ResourceObjectInclude.__init__)
    params = list(sig.parameters.keys())
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "YobjOset" in params, "Missing parameter 'YobjOset'"
    assert "ObOrent" in params, "Missing parameter 'ObOrent'"
    assert "ObjName" in params, "Missing parameter 'ObjName'"
    assert "XobjOset" in params, "Missing parameter 'XobjOset'"

def test_afptext::resourceobjectinclude_has_ObjType():
    assert hasattr(afpText::ResourceObjectInclude, "ObjType")
    descriptor = None
    for klass in afpText::ResourceObjectInclude.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourceobjectinclude_has_YobjOset():
    assert hasattr(afpText::ResourceObjectInclude, "YobjOset")
    descriptor = None
    for klass in afpText::ResourceObjectInclude.__mro__:
        if "YobjOset" in klass.__dict__:
            descriptor = klass.__dict__["YobjOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourceobjectinclude_has_ObOrent():
    assert hasattr(afpText::ResourceObjectInclude, "ObOrent")
    descriptor = None
    for klass in afpText::ResourceObjectInclude.__mro__:
        if "ObOrent" in klass.__dict__:
            descriptor = klass.__dict__["ObOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourceobjectinclude_has_ObjName():
    assert hasattr(afpText::ResourceObjectInclude, "ObjName")
    descriptor = None
    for klass in afpText::ResourceObjectInclude.__mro__:
        if "ObjName" in klass.__dict__:
            descriptor = klass.__dict__["ObjName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourceobjectinclude_has_XobjOset():
    assert hasattr(afpText::ResourceObjectInclude, "XobjOset")
    descriptor = None
    for klass in afpText::ResourceObjectInclude.__mro__:
        if "XobjOset" in klass.__dict__:
            descriptor = klass.__dict__["XobjOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext::idestructure_is_not_abstract():
    assert not inspect.isabstract(afpText::IDEStructure)


def test_afptext::idestructure_constructor_exists():
    assert callable(afpText::IDEStructure.__init__)


def test_afptext::idestructure_constructor_args():
    sig = inspect.signature(afpText::IDEStructure.__init__)
    params = list(sig.parameters.keys())
    assert "SIZE2" in params, "Missing parameter 'SIZE2'"
    assert "FLAGS" in params, "Missing parameter 'FLAGS'"
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"
    assert "SIZE1" in params, "Missing parameter 'SIZE1'"
    assert "SIZE4" in params, "Missing parameter 'SIZE4'"
    assert "SIZE3" in params, "Missing parameter 'SIZE3'"

def test_afptext::idestructure_has_SIZE2():
    assert hasattr(afpText::IDEStructure, "SIZE2")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "SIZE2" in klass.__dict__:
            descriptor = klass.__dict__["SIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idestructure_has_FLAGS():
    assert hasattr(afpText::IDEStructure, "FLAGS")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "FLAGS" in klass.__dict__:
            descriptor = klass.__dict__["FLAGS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idestructure_has_FORMAT():
    assert hasattr(afpText::IDEStructure, "FORMAT")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idestructure_has_SIZE1():
    assert hasattr(afpText::IDEStructure, "SIZE1")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "SIZE1" in klass.__dict__:
            descriptor = klass.__dict__["SIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idestructure_has_SIZE4():
    assert hasattr(afpText::IDEStructure, "SIZE4")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "SIZE4" in klass.__dict__:
            descriptor = klass.__dict__["SIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idestructure_has_SIZE3():
    assert hasattr(afpText::IDEStructure, "SIZE3")
    descriptor = None
    for klass in afpText::IDEStructure.__mro__:
        if "SIZE3" in klass.__dict__:
            descriptor = klass.__dict__["SIZE3"]
            break
    assert isinstance(descriptor, property)



def test_afptext::textorientation_is_not_abstract():
    assert not inspect.isabstract(afpText::TextOrientation)


def test_afptext::textorientation_constructor_exists():
    assert callable(afpText::TextOrientation.__init__)


def test_afptext::textorientation_constructor_args():
    sig = inspect.signature(afpText::TextOrientation.__init__)
    params = list(sig.parameters.keys())
    assert "IAxis" in params, "Missing parameter 'IAxis'"
    assert "BAxis" in params, "Missing parameter 'BAxis'"

def test_afptext::textorientation_has_IAxis():
    assert hasattr(afpText::TextOrientation, "IAxis")
    descriptor = None
    for klass in afpText::TextOrientation.__mro__:
        if "IAxis" in klass.__dict__:
            descriptor = klass.__dict__["IAxis"]
            break
    assert isinstance(descriptor, property)

def test_afptext::textorientation_has_BAxis():
    assert hasattr(afpText::TextOrientation, "BAxis")
    descriptor = None
    for klass in afpText::TextOrientation.__mro__:
        if "BAxis" in klass.__dict__:
            descriptor = klass.__dict__["BAxis"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gline_is_not_abstract():
    assert not inspect.isabstract(afpText::GLINE)


def test_afptext::gline_constructor_exists():
    assert callable(afpText::GLINE.__init__)


def test_afptext::gline_constructor_args():
    sig = inspect.signature(afpText::GLINE.__init__)
    params = list(sig.parameters.keys())



def test_afptext::gslw_is_not_abstract():
    assert not inspect.isabstract(afpText::GSLW)


def test_afptext::gslw_constructor_exists():
    assert callable(afpText::GSLW.__init__)


def test_afptext::gslw_constructor_args():
    sig = inspect.signature(afpText::GSLW.__init__)
    params = list(sig.parameters.keys())
    assert "MH" in params, "Missing parameter 'MH'"

def test_afptext::gslw_has_MH():
    assert hasattr(afpText::GSLW, "MH")
    descriptor = None
    for klass in afpText::GSLW.__mro__:
        if "MH" in klass.__dict__:
            descriptor = klass.__dict__["MH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gscd_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCD)


def test_afptext::gscd_constructor_exists():
    assert callable(afpText::GSCD.__init__)


def test_afptext::gscd_constructor_args():
    sig = inspect.signature(afpText::GSCD.__init__)
    params = list(sig.parameters.keys())
    assert "DIRECTION" in params, "Missing parameter 'DIRECTION'"

def test_afptext::gscd_has_DIRECTION():
    assert hasattr(afpText::GSCD, "DIRECTION")
    descriptor = None
    for klass in afpText::GSCD.__mro__:
        if "DIRECTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRECTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext::objectareasize_is_not_abstract():
    assert not inspect.isabstract(afpText::ObjectAreaSize)


def test_afptext::objectareasize_constructor_exists():
    assert callable(afpText::ObjectAreaSize.__init__)


def test_afptext::objectareasize_constructor_args():
    sig = inspect.signature(afpText::ObjectAreaSize.__init__)
    params = list(sig.parameters.keys())
    assert "XoaSize" in params, "Missing parameter 'XoaSize'"
    assert "YoaSize" in params, "Missing parameter 'YoaSize'"
    assert "SizeType" in params, "Missing parameter 'SizeType'"

def test_afptext::objectareasize_has_XoaSize():
    assert hasattr(afpText::ObjectAreaSize, "XoaSize")
    descriptor = None
    for klass in afpText::ObjectAreaSize.__mro__:
        if "XoaSize" in klass.__dict__:
            descriptor = klass.__dict__["XoaSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectareasize_has_YoaSize():
    assert hasattr(afpText::ObjectAreaSize, "YoaSize")
    descriptor = None
    for klass in afpText::ObjectAreaSize.__mro__:
        if "YoaSize" in klass.__dict__:
            descriptor = klass.__dict__["YoaSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::objectareasize_has_SizeType():
    assert hasattr(afpText::ObjectAreaSize, "SizeType")
    descriptor = None
    for klass in afpText::ObjectAreaSize.__mro__:
        if "SizeType" in klass.__dict__:
            descriptor = klass.__dict__["SizeType"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gscol_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCOL)


def test_afptext::gscol_constructor_exists():
    assert callable(afpText::GSCOL.__init__)


def test_afptext::gscol_constructor_args():
    sig = inspect.signature(afpText::GSCOL.__init__)
    params = list(sig.parameters.keys())
    assert "COL" in params, "Missing parameter 'COL'"

def test_afptext::gscol_has_COL():
    assert hasattr(afpText::GSCOL, "COL")
    descriptor = None
    for klass in afpText::GSCOL.__mro__:
        if "COL" in klass.__dict__:
            descriptor = klass.__dict__["COL"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gbox_is_not_abstract():
    assert not inspect.isabstract(afpText::GBOX)


def test_afptext::gbox_constructor_exists():
    assert callable(afpText::GBOX.__init__)


def test_afptext::gbox_constructor_args():
    sig = inspect.signature(afpText::GBOX.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS0" in params, "Missing parameter 'XPOS0'"
    assert "VAXIS" in params, "Missing parameter 'VAXIS'"
    assert "YPOS1" in params, "Missing parameter 'YPOS1'"
    assert "HAXIS" in params, "Missing parameter 'HAXIS'"
    assert "XPOS1" in params, "Missing parameter 'XPOS1'"
    assert "YPOS0" in params, "Missing parameter 'YPOS0'"
    assert "RES" in params, "Missing parameter 'RES'"

def test_afptext::gbox_has_XPOS0():
    assert hasattr(afpText::GBOX, "XPOS0")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "XPOS0" in klass.__dict__:
            descriptor = klass.__dict__["XPOS0"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_VAXIS():
    assert hasattr(afpText::GBOX, "VAXIS")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "VAXIS" in klass.__dict__:
            descriptor = klass.__dict__["VAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_YPOS1():
    assert hasattr(afpText::GBOX, "YPOS1")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "YPOS1" in klass.__dict__:
            descriptor = klass.__dict__["YPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_HAXIS():
    assert hasattr(afpText::GBOX, "HAXIS")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "HAXIS" in klass.__dict__:
            descriptor = klass.__dict__["HAXIS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_XPOS1():
    assert hasattr(afpText::GBOX, "XPOS1")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "XPOS1" in klass.__dict__:
            descriptor = klass.__dict__["XPOS1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_YPOS0():
    assert hasattr(afpText::GBOX, "YPOS0")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "YPOS0" in klass.__dict__:
            descriptor = klass.__dict__["YPOS0"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gbox_has_RES():
    assert hasattr(afpText::GBOX, "RES")
    descriptor = None
    for klass in afpText::GBOX.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)



def test_afptext::dataobjectfontdescriptor_is_not_abstract():
    assert not inspect.isabstract(afpText::DataObjectFontDescriptor)


def test_afptext::dataobjectfontdescriptor_constructor_exists():
    assert callable(afpText::DataObjectFontDescriptor.__init__)


def test_afptext::dataobjectfontdescriptor_constructor_args():
    sig = inspect.signature(afpText::DataObjectFontDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "FontTech" in params, "Missing parameter 'FontTech'"
    assert "DOFtFlgs" in params, "Missing parameter 'DOFtFlgs'"
    assert "HFS" in params, "Missing parameter 'HFS'"
    assert "EncID" in params, "Missing parameter 'EncID'"
    assert "EncEnv" in params, "Missing parameter 'EncEnv'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "VFS" in params, "Missing parameter 'VFS'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"

def test_afptext::dataobjectfontdescriptor_has_FontTech():
    assert hasattr(afpText::DataObjectFontDescriptor, "FontTech")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "FontTech" in klass.__dict__:
            descriptor = klass.__dict__["FontTech"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_DOFtFlgs():
    assert hasattr(afpText::DataObjectFontDescriptor, "DOFtFlgs")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "DOFtFlgs" in klass.__dict__:
            descriptor = klass.__dict__["DOFtFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_HFS():
    assert hasattr(afpText::DataObjectFontDescriptor, "HFS")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "HFS" in klass.__dict__:
            descriptor = klass.__dict__["HFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_EncID():
    assert hasattr(afpText::DataObjectFontDescriptor, "EncID")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "EncID" in klass.__dict__:
            descriptor = klass.__dict__["EncID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_EncEnv():
    assert hasattr(afpText::DataObjectFontDescriptor, "EncEnv")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "EncEnv" in klass.__dict__:
            descriptor = klass.__dict__["EncEnv"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_Reserved():
    assert hasattr(afpText::DataObjectFontDescriptor, "Reserved")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_VFS():
    assert hasattr(afpText::DataObjectFontDescriptor, "VFS")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "VFS" in klass.__dict__:
            descriptor = klass.__dict__["VFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dataobjectfontdescriptor_has_CharRot():
    assert hasattr(afpText::DataObjectFontDescriptor, "CharRot")
    descriptor = None
    for klass in afpText::DataObjectFontDescriptor.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcbimg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCBIMG)


def test_afptext::gcbimg_constructor_exists():
    assert callable(afpText::GCBIMG.__init__)


def test_afptext::gcbimg_constructor_args():
    sig = inspect.signature(afpText::GCBIMG.__init__)
    params = list(sig.parameters.keys())
    assert "RES" in params, "Missing parameter 'RES'"
    assert "HEIGHT" in params, "Missing parameter 'HEIGHT'"
    assert "WIDTH" in params, "Missing parameter 'WIDTH'"
    assert "FORMAT" in params, "Missing parameter 'FORMAT'"

def test_afptext::gcbimg_has_RES():
    assert hasattr(afpText::GCBIMG, "RES")
    descriptor = None
    for klass in afpText::GCBIMG.__mro__:
        if "RES" in klass.__dict__:
            descriptor = klass.__dict__["RES"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbimg_has_HEIGHT():
    assert hasattr(afpText::GCBIMG, "HEIGHT")
    descriptor = None
    for klass in afpText::GCBIMG.__mro__:
        if "HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbimg_has_WIDTH():
    assert hasattr(afpText::GCBIMG, "WIDTH")
    descriptor = None
    for klass in afpText::GCBIMG.__mro__:
        if "WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["WIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbimg_has_FORMAT():
    assert hasattr(afpText::GCBIMG, "FORMAT")
    descriptor = None
    for klass in afpText::GCBIMG.__mro__:
        if "FORMAT" in klass.__dict__:
            descriptor = klass.__dict__["FORMAT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tonersaver_is_not_abstract():
    assert not inspect.isabstract(afpText::TonerSaver)


def test_afptext::tonersaver_constructor_exists():
    assert callable(afpText::TonerSaver.__init__)


def test_afptext::tonersaver_constructor_args():
    sig = inspect.signature(afpText::TonerSaver.__init__)
    params = list(sig.parameters.keys())
    assert "TSvCtrl" in params, "Missing parameter 'TSvCtrl'"

def test_afptext::tonersaver_has_TSvCtrl():
    assert hasattr(afpText::TonerSaver, "TSvCtrl")
    descriptor = None
    for klass in afpText::TonerSaver.__mro__:
        if "TSvCtrl" in klass.__dict__:
            descriptor = klass.__dict__["TSvCtrl"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tiletoc_is_not_abstract():
    assert not inspect.isabstract(afpText::TileTOC)


def test_afptext::tiletoc_constructor_exists():
    assert callable(afpText::TileTOC.__init__)


def test_afptext::tiletoc_constructor_args():
    sig = inspect.signature(afpText::TileTOC.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::tiletoc_has_Reserved():
    assert hasattr(afpText::TileTOC, "Reserved")
    descriptor = None
    for klass in afpText::TileTOC.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::comment_is_not_abstract():
    assert not inspect.isabstract(afpText::Comment)


def test_afptext::comment_constructor_exists():
    assert callable(afpText::Comment.__init__)


def test_afptext::comment_constructor_args():
    sig = inspect.signature(afpText::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "Comment" in params, "Missing parameter 'Comment'"

def test_afptext::comment_has_Comment():
    assert hasattr(afpText::Comment, "Comment")
    descriptor = None
    for klass in afpText::Comment.__mro__:
        if "Comment" in klass.__dict__:
            descriptor = klass.__dict__["Comment"]
            break
    assert isinstance(descriptor, property)



def test_afptext::beginsegment_is_not_abstract():
    assert not inspect.isabstract(afpText::BeginSegment)


def test_afptext::beginsegment_constructor_exists():
    assert callable(afpText::BeginSegment.__init__)


def test_afptext::beginsegment_constructor_args():
    sig = inspect.signature(afpText::BeginSegment.__init__)
    params = list(sig.parameters.keys())
    assert "SEGNAME" in params, "Missing parameter 'SEGNAME'"

def test_afptext::beginsegment_has_SEGNAME():
    assert hasattr(afpText::BeginSegment, "SEGNAME")
    descriptor = None
    for klass in afpText::BeginSegment.__mro__:
        if "SEGNAME" in klass.__dict__:
            descriptor = klass.__dict__["SEGNAME"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsps_is_not_abstract():
    assert not inspect.isabstract(afpText::GSPS)


def test_afptext::gsps_constructor_exists():
    assert callable(afpText::GSPS.__init__)


def test_afptext::gsps_constructor_args():
    sig = inspect.signature(afpText::GSPS.__init__)
    params = list(sig.parameters.keys())
    assert "LCID" in params, "Missing parameter 'LCID'"

def test_afptext::gsps_has_LCID():
    assert hasattr(afpText::GSPS, "LCID")
    descriptor = None
    for klass in afpText::GSPS.__mro__:
        if "LCID" in klass.__dict__:
            descriptor = klass.__dict__["LCID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::resourcesectionnumber_is_not_abstract():
    assert not inspect.isabstract(afpText::ResourceSectionNumber)


def test_afptext::resourcesectionnumber_constructor_exists():
    assert callable(afpText::ResourceSectionNumber.__init__)


def test_afptext::resourcesectionnumber_constructor_args():
    sig = inspect.signature(afpText::ResourceSectionNumber.__init__)
    params = list(sig.parameters.keys())
    assert "ResSNum" in params, "Missing parameter 'ResSNum'"

def test_afptext::resourcesectionnumber_has_ResSNum():
    assert hasattr(afpText::ResourceSectionNumber, "ResSNum")
    descriptor = None
    for klass in afpText::ResourceSectionNumber.__mro__:
        if "ResSNum" in klass.__dict__:
            descriptor = klass.__dict__["ResSNum"]
            break
    assert isinstance(descriptor, property)



def test_afptext::externalalgorithm_is_not_abstract():
    assert not inspect.isabstract(afpText::ExternalAlgorithm)


def test_afptext::externalalgorithm_constructor_exists():
    assert callable(afpText::ExternalAlgorithm.__init__)


def test_afptext::externalalgorithm_constructor_args():
    sig = inspect.signature(afpText::ExternalAlgorithm.__init__)
    params = list(sig.parameters.keys())
    assert "ALGTYPE" in params, "Missing parameter 'ALGTYPE'"

def test_afptext::externalalgorithm_has_ALGTYPE():
    assert hasattr(afpText::ExternalAlgorithm, "ALGTYPE")
    descriptor = None
    for klass in afpText::ExternalAlgorithm.__mro__:
        if "ALGTYPE" in klass.__dict__:
            descriptor = klass.__dict__["ALGTYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::beginimage_is_not_abstract():
    assert not inspect.isabstract(afpText::BeginImage)


def test_afptext::beginimage_constructor_exists():
    assert callable(afpText::BeginImage.__init__)


def test_afptext::beginimage_constructor_args():
    sig = inspect.signature(afpText::BeginImage.__init__)
    params = list(sig.parameters.keys())
    assert "OBJTYPE" in params, "Missing parameter 'OBJTYPE'"

def test_afptext::beginimage_has_OBJTYPE():
    assert hasattr(afpText::BeginImage, "OBJTYPE")
    descriptor = None
    for klass in afpText::BeginImage.__mro__:
        if "OBJTYPE" in klass.__dict__:
            descriptor = klass.__dict__["OBJTYPE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ami_is_not_abstract():
    assert not inspect.isabstract(afpText::AMI)


def test_afptext::ami_constructor_exists():
    assert callable(afpText::AMI.__init__)


def test_afptext::ami_constructor_args():
    sig = inspect.signature(afpText::AMI.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext::ami_has_DSPLCMNT():
    assert hasattr(afpText::AMI, "DSPLCMNT")
    descriptor = None
    for klass in afpText::AMI.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gsch_is_not_abstract():
    assert not inspect.isabstract(afpText::GSCH)


def test_afptext::gsch_constructor_exists():
    assert callable(afpText::GSCH.__init__)


def test_afptext::gsch_constructor_args():
    sig = inspect.signature(afpText::GSCH.__init__)
    params = list(sig.parameters.keys())
    assert "HX" in params, "Missing parameter 'HX'"
    assert "HY" in params, "Missing parameter 'HY'"

def test_afptext::gsch_has_HX():
    assert hasattr(afpText::GSCH, "HX")
    descriptor = None
    for klass in afpText::GSCH.__mro__:
        if "HX" in klass.__dict__:
            descriptor = klass.__dict__["HX"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gsch_has_HY():
    assert hasattr(afpText::GSCH, "HY")
    descriptor = None
    for klass in afpText::GSCH.__mro__:
        if "HY" in klass.__dict__:
            descriptor = klass.__dict__["HY"]
            break
    assert isinstance(descriptor, property)



def test_afptext::trn_is_not_abstract():
    assert not inspect.isabstract(afpText::TRN)


def test_afptext::trn_constructor_exists():
    assert callable(afpText::TRN.__init__)


def test_afptext::trn_constructor_args():
    sig = inspect.signature(afpText::TRN.__init__)
    params = list(sig.parameters.keys())
    assert "TRNDATA" in params, "Missing parameter 'TRNDATA'"

def test_afptext::trn_has_TRNDATA():
    assert hasattr(afpText::TRN, "TRNDATA")
    descriptor = None
    for klass in afpText::TRN.__mro__:
        if "TRNDATA" in klass.__dict__:
            descriptor = klass.__dict__["TRNDATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::finishingoperation_is_not_abstract():
    assert not inspect.isabstract(afpText::FinishingOperation)


def test_afptext::finishingoperation_constructor_exists():
    assert callable(afpText::FinishingOperation.__init__)


def test_afptext::finishingoperation_constructor_args():
    sig = inspect.signature(afpText::FinishingOperation.__init__)
    params = list(sig.parameters.keys())
    assert "AxOffst" in params, "Missing parameter 'AxOffst'"
    assert "FOpType" in params, "Missing parameter 'FOpType'"
    assert "RefEdge" in params, "Missing parameter 'RefEdge'"
    assert "FOpCnt" in params, "Missing parameter 'FOpCnt'"
    assert "OpPos" in params, "Missing parameter 'OpPos'"

def test_afptext::finishingoperation_has_AxOffst():
    assert hasattr(afpText::FinishingOperation, "AxOffst")
    descriptor = None
    for klass in afpText::FinishingOperation.__mro__:
        if "AxOffst" in klass.__dict__:
            descriptor = klass.__dict__["AxOffst"]
            break
    assert isinstance(descriptor, property)

def test_afptext::finishingoperation_has_FOpType():
    assert hasattr(afpText::FinishingOperation, "FOpType")
    descriptor = None
    for klass in afpText::FinishingOperation.__mro__:
        if "FOpType" in klass.__dict__:
            descriptor = klass.__dict__["FOpType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::finishingoperation_has_RefEdge():
    assert hasattr(afpText::FinishingOperation, "RefEdge")
    descriptor = None
    for klass in afpText::FinishingOperation.__mro__:
        if "RefEdge" in klass.__dict__:
            descriptor = klass.__dict__["RefEdge"]
            break
    assert isinstance(descriptor, property)

def test_afptext::finishingoperation_has_FOpCnt():
    assert hasattr(afpText::FinishingOperation, "FOpCnt")
    descriptor = None
    for klass in afpText::FinishingOperation.__mro__:
        if "FOpCnt" in klass.__dict__:
            descriptor = klass.__dict__["FOpCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::finishingoperation_has_OpPos():
    assert hasattr(afpText::FinishingOperation, "OpPos")
    descriptor = None
    for klass in afpText::FinishingOperation.__mro__:
        if "OpPos" in klass.__dict__:
            descriptor = klass.__dict__["OpPos"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imageencoding_is_not_abstract():
    assert not inspect.isabstract(afpText::ImageEncoding)


def test_afptext::imageencoding_constructor_exists():
    assert callable(afpText::ImageEncoding.__init__)


def test_afptext::imageencoding_constructor_args():
    sig = inspect.signature(afpText::ImageEncoding.__init__)
    params = list(sig.parameters.keys())
    assert "RECID" in params, "Missing parameter 'RECID'"
    assert "BITORDR" in params, "Missing parameter 'BITORDR'"
    assert "COMPRID" in params, "Missing parameter 'COMPRID'"

def test_afptext::imageencoding_has_RECID():
    assert hasattr(afpText::ImageEncoding, "RECID")
    descriptor = None
    for klass in afpText::ImageEncoding.__mro__:
        if "RECID" in klass.__dict__:
            descriptor = klass.__dict__["RECID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imageencoding_has_BITORDR():
    assert hasattr(afpText::ImageEncoding, "BITORDR")
    descriptor = None
    for klass in afpText::ImageEncoding.__mro__:
        if "BITORDR" in klass.__dict__:
            descriptor = klass.__dict__["BITORDR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::imageencoding_has_COMPRID():
    assert hasattr(afpText::ImageEncoding, "COMPRID")
    descriptor = None
    for klass in afpText::ImageEncoding.__mro__:
        if "COMPRID" in klass.__dict__:
            descriptor = klass.__dict__["COMPRID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::measurementunits_is_not_abstract():
    assert not inspect.isabstract(afpText::MeasurementUnits)


def test_afptext::measurementunits_constructor_exists():
    assert callable(afpText::MeasurementUnits.__init__)


def test_afptext::measurementunits_constructor_args():
    sig = inspect.signature(afpText::MeasurementUnits.__init__)
    params = list(sig.parameters.keys())
    assert "XoaUnits" in params, "Missing parameter 'XoaUnits'"
    assert "YoaUnits" in params, "Missing parameter 'YoaUnits'"
    assert "YoaBase" in params, "Missing parameter 'YoaBase'"
    assert "XoaBase" in params, "Missing parameter 'XoaBase'"

def test_afptext::measurementunits_has_XoaUnits():
    assert hasattr(afpText::MeasurementUnits, "XoaUnits")
    descriptor = None
    for klass in afpText::MeasurementUnits.__mro__:
        if "XoaUnits" in klass.__dict__:
            descriptor = klass.__dict__["XoaUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::measurementunits_has_YoaUnits():
    assert hasattr(afpText::MeasurementUnits, "YoaUnits")
    descriptor = None
    for klass in afpText::MeasurementUnits.__mro__:
        if "YoaUnits" in klass.__dict__:
            descriptor = klass.__dict__["YoaUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::measurementunits_has_YoaBase():
    assert hasattr(afpText::MeasurementUnits, "YoaBase")
    descriptor = None
    for klass in afpText::MeasurementUnits.__mro__:
        if "YoaBase" in klass.__dict__:
            descriptor = klass.__dict__["YoaBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::measurementunits_has_XoaBase():
    assert hasattr(afpText::MeasurementUnits, "XoaBase")
    descriptor = None
    for klass in afpText::MeasurementUnits.__mro__:
        if "XoaBase" in klass.__dict__:
            descriptor = klass.__dict__["XoaBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext::attributevalue_is_not_abstract():
    assert not inspect.isabstract(afpText::AttributeValue)


def test_afptext::attributevalue_constructor_exists():
    assert callable(afpText::AttributeValue.__init__)


def test_afptext::attributevalue_constructor_args():
    sig = inspect.signature(afpText::AttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved0" in params, "Missing parameter 'Reserved0'"
    assert "AttVal" in params, "Missing parameter 'AttVal'"

def test_afptext::attributevalue_has_Reserved0():
    assert hasattr(afpText::AttributeValue, "Reserved0")
    descriptor = None
    for klass in afpText::AttributeValue.__mro__:
        if "Reserved0" in klass.__dict__:
            descriptor = klass.__dict__["Reserved0"]
            break
    assert isinstance(descriptor, property)

def test_afptext::attributevalue_has_AttVal():
    assert hasattr(afpText::AttributeValue, "AttVal")
    descriptor = None
    for klass in afpText::AttributeValue.__mro__:
        if "AttVal" in klass.__dict__:
            descriptor = klass.__dict__["AttVal"]
            break
    assert isinstance(descriptor, property)



def test_afptext::universaldateandtimestamp_is_not_abstract():
    assert not inspect.isabstract(afpText::UniversalDateAndTimeStamp)


def test_afptext::universaldateandtimestamp_constructor_exists():
    assert callable(afpText::UniversalDateAndTimeStamp.__init__)


def test_afptext::universaldateandtimestamp_constructor_args():
    sig = inspect.signature(afpText::UniversalDateAndTimeStamp.__init__)
    params = list(sig.parameters.keys())
    assert "Hour" in params, "Missing parameter 'Hour'"
    assert "Second" in params, "Missing parameter 'Second'"
    assert "Day" in params, "Missing parameter 'Day'"
    assert "UTCDiffM" in params, "Missing parameter 'UTCDiffM'"
    assert "Month" in params, "Missing parameter 'Month'"
    assert "YearAD" in params, "Missing parameter 'YearAD'"
    assert "TimeZone" in params, "Missing parameter 'TimeZone'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "UTCDiffH" in params, "Missing parameter 'UTCDiffH'"
    assert "Minute" in params, "Missing parameter 'Minute'"

def test_afptext::universaldateandtimestamp_has_Hour():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Hour")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Hour" in klass.__dict__:
            descriptor = klass.__dict__["Hour"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_Second():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Second")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Second" in klass.__dict__:
            descriptor = klass.__dict__["Second"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_Day():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Day")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Day" in klass.__dict__:
            descriptor = klass.__dict__["Day"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_UTCDiffM():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "UTCDiffM")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "UTCDiffM" in klass.__dict__:
            descriptor = klass.__dict__["UTCDiffM"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_Month():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Month")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Month" in klass.__dict__:
            descriptor = klass.__dict__["Month"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_YearAD():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "YearAD")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "YearAD" in klass.__dict__:
            descriptor = klass.__dict__["YearAD"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_TimeZone():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "TimeZone")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "TimeZone" in klass.__dict__:
            descriptor = klass.__dict__["TimeZone"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_Reserved():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Reserved")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_UTCDiffH():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "UTCDiffH")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "UTCDiffH" in klass.__dict__:
            descriptor = klass.__dict__["UTCDiffH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::universaldateandtimestamp_has_Minute():
    assert hasattr(afpText::UniversalDateAndTimeStamp, "Minute")
    descriptor = None
    for klass in afpText::UniversalDateAndTimeStamp.__mro__:
        if "Minute" in klass.__dict__:
            descriptor = klass.__dict__["Minute"]
            break
    assert isinstance(descriptor, property)



def test_afptext::characterrotation_is_not_abstract():
    assert not inspect.isabstract(afpText::CharacterRotation)


def test_afptext::characterrotation_constructor_exists():
    assert callable(afpText::CharacterRotation.__init__)


def test_afptext::characterrotation_constructor_args():
    sig = inspect.signature(afpText::CharacterRotation.__init__)
    params = list(sig.parameters.keys())
    assert "CharRot" in params, "Missing parameter 'CharRot'"

def test_afptext::characterrotation_has_CharRot():
    assert hasattr(afpText::CharacterRotation, "CharRot")
    descriptor = None
    for klass in afpText::CharacterRotation.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)



def test_afptext::descriptorposition_is_not_abstract():
    assert not inspect.isabstract(afpText::DescriptorPosition)


def test_afptext::descriptorposition_constructor_exists():
    assert callable(afpText::DescriptorPosition.__init__)


def test_afptext::descriptorposition_constructor_args():
    sig = inspect.signature(afpText::DescriptorPosition.__init__)
    params = list(sig.parameters.keys())
    assert "DesPosID" in params, "Missing parameter 'DesPosID'"

def test_afptext::descriptorposition_has_DesPosID():
    assert hasattr(afpText::DescriptorPosition, "DesPosID")
    descriptor = None
    for klass in afpText::DescriptorPosition.__mro__:
        if "DesPosID" in klass.__dict__:
            descriptor = klass.__dict__["DesPosID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::resourceobjecttype_is_not_abstract():
    assert not inspect.isabstract(afpText::ResourceObjectType)


def test_afptext::resourceobjecttype_constructor_exists():
    assert callable(afpText::ResourceObjectType.__init__)


def test_afptext::resourceobjecttype_constructor_args():
    sig = inspect.signature(afpText::ResourceObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"

def test_afptext::resourceobjecttype_has_ConData():
    assert hasattr(afpText::ResourceObjectType, "ConData")
    descriptor = None
    for klass in afpText::ResourceObjectType.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)

def test_afptext::resourceobjecttype_has_ObjType():
    assert hasattr(afpText::ResourceObjectType, "ObjType")
    descriptor = None
    for klass in afpText::ResourceObjectType.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)



def test_afptext::amb_is_not_abstract():
    assert not inspect.isabstract(afpText::AMB)


def test_afptext::amb_constructor_exists():
    assert callable(afpText::AMB.__init__)


def test_afptext::amb_constructor_args():
    sig = inspect.signature(afpText::AMB.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext::amb_has_DSPLCMNT():
    assert hasattr(afpText::AMB, "DSPLCMNT")
    descriptor = None
    for klass in afpText::AMB.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::svi_is_not_abstract():
    assert not inspect.isabstract(afpText::SVI)


def test_afptext::svi_constructor_exists():
    assert callable(afpText::SVI.__init__)


def test_afptext::svi_constructor_args():
    sig = inspect.signature(afpText::SVI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext::svi_has_INCRMENT():
    assert hasattr(afpText::SVI, "INCRMENT")
    descriptor = None
    for klass in afpText::SVI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::sto_is_not_abstract():
    assert not inspect.isabstract(afpText::STO)


def test_afptext::sto_constructor_exists():
    assert callable(afpText::STO.__init__)


def test_afptext::sto_constructor_args():
    sig = inspect.signature(afpText::STO.__init__)
    params = list(sig.parameters.keys())
    assert "BORNTION" in params, "Missing parameter 'BORNTION'"
    assert "IORNTION" in params, "Missing parameter 'IORNTION'"

def test_afptext::sto_has_BORNTION():
    assert hasattr(afpText::STO, "BORNTION")
    descriptor = None
    for klass in afpText::STO.__mro__:
        if "BORNTION" in klass.__dict__:
            descriptor = klass.__dict__["BORNTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sto_has_IORNTION():
    assert hasattr(afpText::STO, "IORNTION")
    descriptor = None
    for klass in afpText::STO.__mro__:
        if "IORNTION" in klass.__dict__:
            descriptor = klass.__dict__["IORNTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext::stc_is_not_abstract():
    assert not inspect.isabstract(afpText::STC)


def test_afptext::stc_constructor_exists():
    assert callable(afpText::STC.__init__)


def test_afptext::stc_constructor_args():
    sig = inspect.signature(afpText::STC.__init__)
    params = list(sig.parameters.keys())
    assert "FRGCOLOR" in params, "Missing parameter 'FRGCOLOR'"
    assert "PRECSION" in params, "Missing parameter 'PRECSION'"

def test_afptext::stc_has_FRGCOLOR():
    assert hasattr(afpText::STC, "FRGCOLOR")
    descriptor = None
    for klass in afpText::STC.__mro__:
        if "FRGCOLOR" in klass.__dict__:
            descriptor = klass.__dict__["FRGCOLOR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::stc_has_PRECSION():
    assert hasattr(afpText::STC, "PRECSION")
    descriptor = None
    for klass in afpText::STC.__mro__:
        if "PRECSION" in klass.__dict__:
            descriptor = klass.__dict__["PRECSION"]
            break
    assert isinstance(descriptor, property)



def test_afptext::sim_is_not_abstract():
    assert not inspect.isabstract(afpText::SIM)


def test_afptext::sim_constructor_exists():
    assert callable(afpText::SIM.__init__)


def test_afptext::sim_constructor_args():
    sig = inspect.signature(afpText::SIM.__init__)
    params = list(sig.parameters.keys())
    assert "DSPLCMNT" in params, "Missing parameter 'DSPLCMNT'"

def test_afptext::sim_has_DSPLCMNT():
    assert hasattr(afpText::SIM, "DSPLCMNT")
    descriptor = None
    for klass in afpText::SIM.__mro__:
        if "DSPLCMNT" in klass.__dict__:
            descriptor = klass.__dict__["DSPLCMNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::sia_is_not_abstract():
    assert not inspect.isabstract(afpText::SIA)


def test_afptext::sia_constructor_exists():
    assert callable(afpText::SIA.__init__)


def test_afptext::sia_constructor_args():
    sig = inspect.signature(afpText::SIA.__init__)
    params = list(sig.parameters.keys())
    assert "ADJSTMNT" in params, "Missing parameter 'ADJSTMNT'"
    assert "DIRCTION" in params, "Missing parameter 'DIRCTION'"

def test_afptext::sia_has_ADJSTMNT():
    assert hasattr(afpText::SIA, "ADJSTMNT")
    descriptor = None
    for klass in afpText::SIA.__mro__:
        if "ADJSTMNT" in klass.__dict__:
            descriptor = klass.__dict__["ADJSTMNT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sia_has_DIRCTION():
    assert hasattr(afpText::SIA, "DIRCTION")
    descriptor = None
    for klass in afpText::SIA.__mro__:
        if "DIRCTION" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTION"]
            break
    assert isinstance(descriptor, property)



def test_afptext::sec_is_not_abstract():
    assert not inspect.isabstract(afpText::SEC)


def test_afptext::sec_constructor_exists():
    assert callable(afpText::SEC.__init__)


def test_afptext::sec_constructor_args():
    sig = inspect.signature(afpText::SEC.__init__)
    params = list(sig.parameters.keys())
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "COLSIZE4" in params, "Missing parameter 'COLSIZE4'"
    assert "COLSIZE3" in params, "Missing parameter 'COLSIZE3'"
    assert "COLSIZE2" in params, "Missing parameter 'COLSIZE2'"
    assert "COLSIZE1" in params, "Missing parameter 'COLSIZE1'"
    assert "COLVALUE" in params, "Missing parameter 'COLVALUE'"
    assert "COLSPCE" in params, "Missing parameter 'COLSPCE'"

def test_afptext::sec_has_RESERVED():
    assert hasattr(afpText::SEC, "RESERVED")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLSIZE4():
    assert hasattr(afpText::SEC, "COLSIZE4")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLSIZE4" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE4"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLSIZE3():
    assert hasattr(afpText::SEC, "COLSIZE3")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLSIZE3" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLSIZE2():
    assert hasattr(afpText::SEC, "COLSIZE2")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLSIZE2" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLSIZE1():
    assert hasattr(afpText::SEC, "COLSIZE1")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLSIZE1" in klass.__dict__:
            descriptor = klass.__dict__["COLSIZE1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLVALUE():
    assert hasattr(afpText::SEC, "COLVALUE")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLVALUE" in klass.__dict__:
            descriptor = klass.__dict__["COLVALUE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::sec_has_COLSPCE():
    assert hasattr(afpText::SEC, "COLSPCE")
    descriptor = None
    for klass in afpText::SEC.__mro__:
        if "COLSPCE" in klass.__dict__:
            descriptor = klass.__dict__["COLSPCE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::scfl_is_not_abstract():
    assert not inspect.isabstract(afpText::SCFL)


def test_afptext::scfl_constructor_exists():
    assert callable(afpText::SCFL.__init__)


def test_afptext::scfl_constructor_args():
    sig = inspect.signature(afpText::SCFL.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext::scfl_has_LID():
    assert hasattr(afpText::SCFL, "LID")
    descriptor = None
    for klass in afpText::SCFL.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::sbi_is_not_abstract():
    assert not inspect.isabstract(afpText::SBI)


def test_afptext::sbi_constructor_exists():
    assert callable(afpText::SBI.__init__)


def test_afptext::sbi_constructor_args():
    sig = inspect.signature(afpText::SBI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext::sbi_has_INCRMENT():
    assert hasattr(afpText::SBI, "INCRMENT")
    descriptor = None
    for klass in afpText::SBI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::rps_is_not_abstract():
    assert not inspect.isabstract(afpText::RPS)


def test_afptext::rps_constructor_exists():
    assert callable(afpText::RPS.__init__)


def test_afptext::rps_constructor_args():
    sig = inspect.signature(afpText::RPS.__init__)
    params = list(sig.parameters.keys())
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"
    assert "RPTDATA" in params, "Missing parameter 'RPTDATA'"

def test_afptext::rps_has_RLENGTH():
    assert hasattr(afpText::RPS, "RLENGTH")
    descriptor = None
    for klass in afpText::RPS.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::rps_has_RPTDATA():
    assert hasattr(afpText::RPS, "RPTDATA")
    descriptor = None
    for klass in afpText::RPS.__mro__:
        if "RPTDATA" in klass.__dict__:
            descriptor = klass.__dict__["RPTDATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::rmi_is_not_abstract():
    assert not inspect.isabstract(afpText::RMI)


def test_afptext::rmi_constructor_exists():
    assert callable(afpText::RMI.__init__)


def test_afptext::rmi_constructor_args():
    sig = inspect.signature(afpText::RMI.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext::rmi_has_INCRMENT():
    assert hasattr(afpText::RMI, "INCRMENT")
    descriptor = None
    for klass in afpText::RMI.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::rmb_is_not_abstract():
    assert not inspect.isabstract(afpText::RMB)


def test_afptext::rmb_constructor_exists():
    assert callable(afpText::RMB.__init__)


def test_afptext::rmb_constructor_args():
    sig = inspect.signature(afpText::RMB.__init__)
    params = list(sig.parameters.keys())
    assert "INCRMENT" in params, "Missing parameter 'INCRMENT'"

def test_afptext::rmb_has_INCRMENT():
    assert hasattr(afpText::RMB, "INCRMENT")
    descriptor = None
    for klass in afpText::RMB.__mro__:
        if "INCRMENT" in klass.__dict__:
            descriptor = klass.__dict__["INCRMENT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ovs_is_not_abstract():
    assert not inspect.isabstract(afpText::OVS)


def test_afptext::ovs_constructor_exists():
    assert callable(afpText::OVS.__init__)


def test_afptext::ovs_constructor_args():
    sig = inspect.signature(afpText::OVS.__init__)
    params = list(sig.parameters.keys())
    assert "BYPSIDEN" in params, "Missing parameter 'BYPSIDEN'"
    assert "OVERCHAR" in params, "Missing parameter 'OVERCHAR'"

def test_afptext::ovs_has_BYPSIDEN():
    assert hasattr(afpText::OVS, "BYPSIDEN")
    descriptor = None
    for klass in afpText::OVS.__mro__:
        if "BYPSIDEN" in klass.__dict__:
            descriptor = klass.__dict__["BYPSIDEN"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ovs_has_OVERCHAR():
    assert hasattr(afpText::OVS, "OVERCHAR")
    descriptor = None
    for klass in afpText::OVS.__mro__:
        if "OVERCHAR" in klass.__dict__:
            descriptor = klass.__dict__["OVERCHAR"]
            break
    assert isinstance(descriptor, property)



def test_afptext::nopcs_is_not_abstract():
    assert not inspect.isabstract(afpText::NOPCS)


def test_afptext::nopcs_constructor_exists():
    assert callable(afpText::NOPCS.__init__)


def test_afptext::nopcs_constructor_args():
    sig = inspect.signature(afpText::NOPCS.__init__)
    params = list(sig.parameters.keys())
    assert "IGNDATA" in params, "Missing parameter 'IGNDATA'"

def test_afptext::nopcs_has_IGNDATA():
    assert hasattr(afpText::NOPCS, "IGNDATA")
    descriptor = None
    for klass in afpText::NOPCS.__mro__:
        if "IGNDATA" in klass.__dict__:
            descriptor = klass.__dict__["IGNDATA"]
            break
    assert isinstance(descriptor, property)



def test_afptext::esu_is_not_abstract():
    assert not inspect.isabstract(afpText::ESU)


def test_afptext::esu_constructor_exists():
    assert callable(afpText::ESU.__init__)


def test_afptext::esu_constructor_args():
    sig = inspect.signature(afpText::ESU.__init__)
    params = list(sig.parameters.keys())
    assert "LID" in params, "Missing parameter 'LID'"

def test_afptext::esu_has_LID():
    assert hasattr(afpText::ESU, "LID")
    descriptor = None
    for klass in afpText::ESU.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::dir_is_not_abstract():
    assert not inspect.isabstract(afpText::DIR)


def test_afptext::dir_constructor_exists():
    assert callable(afpText::DIR.__init__)


def test_afptext::dir_constructor_args():
    sig = inspect.signature(afpText::DIR.__init__)
    params = list(sig.parameters.keys())
    assert "RWIDTHFRACTION" in params, "Missing parameter 'RWIDTHFRACTION'"
    assert "RWIDTH" in params, "Missing parameter 'RWIDTH'"
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"

def test_afptext::dir_has_RWIDTHFRACTION():
    assert hasattr(afpText::DIR, "RWIDTHFRACTION")
    descriptor = None
    for klass in afpText::DIR.__mro__:
        if "RWIDTHFRACTION" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTHFRACTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dir_has_RWIDTH():
    assert hasattr(afpText::DIR, "RWIDTH")
    descriptor = None
    for klass in afpText::DIR.__mro__:
        if "RWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dir_has_RLENGTH():
    assert hasattr(afpText::DIR, "RLENGTH")
    descriptor = None
    for klass in afpText::DIR.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::dbr_is_not_abstract():
    assert not inspect.isabstract(afpText::DBR)


def test_afptext::dbr_constructor_exists():
    assert callable(afpText::DBR.__init__)


def test_afptext::dbr_constructor_args():
    sig = inspect.signature(afpText::DBR.__init__)
    params = list(sig.parameters.keys())
    assert "RLENGTH" in params, "Missing parameter 'RLENGTH'"
    assert "RWIDTHFRACTION" in params, "Missing parameter 'RWIDTHFRACTION'"
    assert "RWIDTH" in params, "Missing parameter 'RWIDTH'"

def test_afptext::dbr_has_RLENGTH():
    assert hasattr(afpText::DBR, "RLENGTH")
    descriptor = None
    for klass in afpText::DBR.__mro__:
        if "RLENGTH" in klass.__dict__:
            descriptor = klass.__dict__["RLENGTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dbr_has_RWIDTHFRACTION():
    assert hasattr(afpText::DBR, "RWIDTHFRACTION")
    descriptor = None
    for klass in afpText::DBR.__mro__:
        if "RWIDTHFRACTION" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTHFRACTION"]
            break
    assert isinstance(descriptor, property)

def test_afptext::dbr_has_RWIDTH():
    assert hasattr(afpText::DBR, "RWIDTH")
    descriptor = None
    for klass in afpText::DBR.__mro__:
        if "RWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["RWIDTH"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcrlinerg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCRLINERG)


def test_afptext::gcrlinerg_constructor_exists():
    assert callable(afpText::GCRLINERG.__init__)


def test_afptext::gcrlinerg_constructor_args():
    sig = inspect.signature(afpText::GCRLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YOFFS" in params, "Missing parameter 'YOFFS'"
    assert "XOSSF" in params, "Missing parameter 'XOSSF'"

def test_afptext::gcrlinerg_has_YOFFS():
    assert hasattr(afpText::GCRLINERG, "YOFFS")
    descriptor = None
    for klass in afpText::GCRLINERG.__mro__:
        if "YOFFS" in klass.__dict__:
            descriptor = klass.__dict__["YOFFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcrlinerg_has_XOSSF():
    assert hasattr(afpText::GCRLINERG, "XOSSF")
    descriptor = None
    for klass in afpText::GCRLINERG.__mro__:
        if "XOSSF" in klass.__dict__:
            descriptor = klass.__dict__["XOSSF"]
            break
    assert isinstance(descriptor, property)



def test_afptext::grlinerg_is_not_abstract():
    assert not inspect.isabstract(afpText::GRLINERG)


def test_afptext::grlinerg_constructor_exists():
    assert callable(afpText::GRLINERG.__init__)


def test_afptext::grlinerg_constructor_args():
    sig = inspect.signature(afpText::GRLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YOFFS" in params, "Missing parameter 'YOFFS'"
    assert "XOSSF" in params, "Missing parameter 'XOSSF'"

def test_afptext::grlinerg_has_YOFFS():
    assert hasattr(afpText::GRLINERG, "YOFFS")
    descriptor = None
    for klass in afpText::GRLINERG.__mro__:
        if "YOFFS" in klass.__dict__:
            descriptor = klass.__dict__["YOFFS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::grlinerg_has_XOSSF():
    assert hasattr(afpText::GRLINERG, "XOSSF")
    descriptor = None
    for klass in afpText::GRLINERG.__mro__:
        if "XOSSF" in klass.__dict__:
            descriptor = klass.__dict__["XOSSF"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcmrkrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCMRKRG)


def test_afptext::gcmrkrg_constructor_exists():
    assert callable(afpText::GCMRKRG.__init__)


def test_afptext::gcmrkrg_constructor_args():
    sig = inspect.signature(afpText::GCMRKRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::gcmrkrg_has_YPOS():
    assert hasattr(afpText::GCMRKRG, "YPOS")
    descriptor = None
    for klass in afpText::GCMRKRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcmrkrg_has_XPOS():
    assert hasattr(afpText::GCMRKRG, "XPOS")
    descriptor = None
    for klass in afpText::GCMRKRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gmrkrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GMRKRG)


def test_afptext::gmrkrg_constructor_exists():
    assert callable(afpText::GMRKRG.__init__)


def test_afptext::gmrkrg_constructor_args():
    sig = inspect.signature(afpText::GMRKRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::gmrkrg_has_YPOS():
    assert hasattr(afpText::GMRKRG, "YPOS")
    descriptor = None
    for klass in afpText::GMRKRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gmrkrg_has_XPOS():
    assert hasattr(afpText::GMRKRG, "XPOS")
    descriptor = None
    for klass in afpText::GMRKRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gclinerg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCLINERG)


def test_afptext::gclinerg_constructor_exists():
    assert callable(afpText::GCLINERG.__init__)


def test_afptext::gclinerg_constructor_args():
    sig = inspect.signature(afpText::GCLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::gclinerg_has_YPOS():
    assert hasattr(afpText::GCLINERG, "YPOS")
    descriptor = None
    for klass in afpText::GCLINERG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gclinerg_has_XPOS():
    assert hasattr(afpText::GCLINERG, "XPOS")
    descriptor = None
    for klass in afpText::GCLINERG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::triplet_is_not_abstract():
    assert not inspect.isabstract(afpText::triplet)


def test_afptext::triplet_constructor_exists():
    assert callable(afpText::triplet.__init__)


def test_afptext::triplet_constructor_args():
    sig = inspect.signature(afpText::triplet.__init__)
    params = list(sig.parameters.keys())



def test_structuredfield_is_not_abstract():
    assert not inspect.isabstract(structuredField)


def test_structuredfield_constructor_exists():
    assert callable(structuredField.__init__)


def test_structuredfield_constructor_args():
    sig = inspect.signature(structuredField.__init__)
    params = list(sig.parameters.keys())



def test_afptext::bcf_is_not_abstract():
    assert not inspect.isabstract(afpText::BCF)


def test_afptext::bcf_constructor_exists():
    assert callable(afpText::BCF.__init__)


def test_afptext::bcf_constructor_args():
    sig = inspect.signature(afpText::BCF.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::bcf_has_RSName():
    assert hasattr(afpText::BCF, "RSName")
    descriptor = None
    for klass in afpText::BCF.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdx_is_not_abstract():
    assert not inspect.isabstract(afpText::BDX)


def test_afptext::bdx_constructor_exists():
    assert callable(afpText::BDX.__init__)


def test_afptext::bdx_constructor_args():
    sig = inspect.signature(afpText::BDX.__init__)
    params = list(sig.parameters.keys())
    assert "DMXName" in params, "Missing parameter 'DMXName'"

def test_afptext::bdx_has_DMXName():
    assert hasattr(afpText::BDX, "DMXName")
    descriptor = None
    for klass in afpText::BDX.__mro__:
        if "DMXName" in klass.__dict__:
            descriptor = klass.__dict__["DMXName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bfn_is_not_abstract():
    assert not inspect.isabstract(afpText::BFN)


def test_afptext::bfn_constructor_exists():
    assert callable(afpText::BFN.__init__)


def test_afptext::bfn_constructor_args():
    sig = inspect.signature(afpText::BFN.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::bfn_has_RSName():
    assert hasattr(afpText::BFN, "RSName")
    descriptor = None
    for klass in afpText::BFN.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bgr_is_not_abstract():
    assert not inspect.isabstract(afpText::BGR)


def test_afptext::bgr_constructor_exists():
    assert callable(afpText::BGR.__init__)


def test_afptext::bgr_constructor_args():
    sig = inspect.signature(afpText::BGR.__init__)
    params = list(sig.parameters.keys())
    assert "GdoName" in params, "Missing parameter 'GdoName'"

def test_afptext::bgr_has_GdoName():
    assert hasattr(afpText::BGR, "GdoName")
    descriptor = None
    for klass in afpText::BGR.__mro__:
        if "GdoName" in klass.__dict__:
            descriptor = klass.__dict__["GdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::boc_is_not_abstract():
    assert not inspect.isabstract(afpText::BOC)


def test_afptext::boc_constructor_exists():
    assert callable(afpText::BOC.__init__)


def test_afptext::boc_constructor_args():
    sig = inspect.signature(afpText::BOC.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCName" in params, "Missing parameter 'ObjCName'"

def test_afptext::boc_has_ObjCName():
    assert hasattr(afpText::BOC, "ObjCName")
    descriptor = None
    for klass in afpText::BOC.__mro__:
        if "ObjCName" in klass.__dict__:
            descriptor = klass.__dict__["ObjCName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bfg_is_not_abstract():
    assert not inspect.isabstract(afpText::BFG)


def test_afptext::bfg_constructor_exists():
    assert callable(afpText::BFG.__init__)


def test_afptext::bfg_constructor_args():
    sig = inspect.signature(afpText::BFG.__init__)
    params = list(sig.parameters.keys())
    assert "FEGName" in params, "Missing parameter 'FEGName'"

def test_afptext::bfg_has_FEGName():
    assert hasattr(afpText::BFG, "FEGName")
    descriptor = None
    for klass in afpText::BFG.__mro__:
        if "FEGName" in klass.__dict__:
            descriptor = klass.__dict__["FEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bii_is_not_abstract():
    assert not inspect.isabstract(afpText::BII)


def test_afptext::bii_constructor_exists():
    assert callable(afpText::BII.__init__)


def test_afptext::bii_constructor_args():
    sig = inspect.signature(afpText::BII.__init__)
    params = list(sig.parameters.keys())
    assert "ImoName" in params, "Missing parameter 'ImoName'"

def test_afptext::bii_has_ImoName():
    assert hasattr(afpText::BII, "ImoName")
    descriptor = None
    for klass in afpText::BII.__mro__:
        if "ImoName" in klass.__dict__:
            descriptor = klass.__dict__["ImoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bfm_is_not_abstract():
    assert not inspect.isabstract(afpText::BFM)


def test_afptext::bfm_constructor_exists():
    assert callable(afpText::BFM.__init__)


def test_afptext::bfm_constructor_args():
    sig = inspect.signature(afpText::BFM.__init__)
    params = list(sig.parameters.keys())
    assert "FMName" in params, "Missing parameter 'FMName'"

def test_afptext::bfm_has_FMName():
    assert hasattr(afpText::BFM, "FMName")
    descriptor = None
    for klass in afpText::BFM.__mro__:
        if "FMName" in klass.__dict__:
            descriptor = klass.__dict__["FMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bmm_is_not_abstract():
    assert not inspect.isabstract(afpText::BMM)


def test_afptext::bmm_constructor_exists():
    assert callable(afpText::BMM.__init__)


def test_afptext::bmm_constructor_args():
    sig = inspect.signature(afpText::BMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMName" in params, "Missing parameter 'MMName'"

def test_afptext::bmm_has_MMName():
    assert hasattr(afpText::BMM, "MMName")
    descriptor = None
    for klass in afpText::BMM.__mro__:
        if "MMName" in klass.__dict__:
            descriptor = klass.__dict__["MMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bag_is_not_abstract():
    assert not inspect.isabstract(afpText::BAG)


def test_afptext::bag_constructor_exists():
    assert callable(afpText::BAG.__init__)


def test_afptext::bag_constructor_args():
    sig = inspect.signature(afpText::BAG.__init__)
    params = list(sig.parameters.keys())
    assert "AEGName" in params, "Missing parameter 'AEGName'"

def test_afptext::bag_has_AEGName():
    assert hasattr(afpText::BAG, "AEGName")
    descriptor = None
    for klass in afpText::BAG.__mro__:
        if "AEGName" in klass.__dict__:
            descriptor = klass.__dict__["AEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bcp_is_not_abstract():
    assert not inspect.isabstract(afpText::BCP)


def test_afptext::bcp_constructor_exists():
    assert callable(afpText::BCP.__init__)


def test_afptext::bcp_constructor_args():
    sig = inspect.signature(afpText::BCP.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::bcp_has_RSName():
    assert hasattr(afpText::BCP, "RSName")
    descriptor = None
    for klass in afpText::BCP.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bim_is_not_abstract():
    assert not inspect.isabstract(afpText::BIM)


def test_afptext::bim_constructor_exists():
    assert callable(afpText::BIM.__init__)


def test_afptext::bim_constructor_args():
    sig = inspect.signature(afpText::BIM.__init__)
    params = list(sig.parameters.keys())
    assert "IdoName" in params, "Missing parameter 'IdoName'"

def test_afptext::bim_has_IdoName():
    assert hasattr(afpText::BIM, "IdoName")
    descriptor = None
    for klass in afpText::BIM.__mro__:
        if "IdoName" in klass.__dict__:
            descriptor = klass.__dict__["IdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bmo_is_not_abstract():
    assert not inspect.isabstract(afpText::BMO)


def test_afptext::bmo_constructor_exists():
    assert callable(afpText::BMO.__init__)


def test_afptext::bmo_constructor_args():
    sig = inspect.signature(afpText::BMO.__init__)
    params = list(sig.parameters.keys())
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"

def test_afptext::bmo_has_OvlyName():
    assert hasattr(afpText::BMO, "OvlyName")
    descriptor = None
    for klass in afpText::BMO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdd_is_not_abstract():
    assert not inspect.isabstract(afpText::BDD)


def test_afptext::bdd_constructor_exists():
    assert callable(afpText::BDD.__init__)


def test_afptext::bdd_constructor_args():
    sig = inspect.signature(afpText::BDD.__init__)
    params = list(sig.parameters.keys())
    assert "YEXTENT" in params, "Missing parameter 'YEXTENT'"
    assert "UBASE" in params, "Missing parameter 'UBASE'"
    assert "COLOR" in params, "Missing parameter 'COLOR'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "XUPUB" in params, "Missing parameter 'XUPUB'"
    assert "MOD" in params, "Missing parameter 'MOD'"
    assert "WENE" in params, "Missing parameter 'WENE'"
    assert "MULT" in params, "Missing parameter 'MULT'"
    assert "ELEMENTHEIGHT" in params, "Missing parameter 'ELEMENTHEIGHT'"
    assert "YUPUB" in params, "Missing parameter 'YUPUB'"
    assert "MODULEWIDTH" in params, "Missing parameter 'MODULEWIDTH'"
    assert "TYPE" in params, "Missing parameter 'TYPE'"
    assert "XEXTENT" in params, "Missing parameter 'XEXTENT'"
    assert "LID" in params, "Missing parameter 'LID'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::bdd_has_YEXTENT():
    assert hasattr(afpText::BDD, "YEXTENT")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "YEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_UBASE():
    assert hasattr(afpText::BDD, "UBASE")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "UBASE" in klass.__dict__:
            descriptor = klass.__dict__["UBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_COLOR():
    assert hasattr(afpText::BDD, "COLOR")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "COLOR" in klass.__dict__:
            descriptor = klass.__dict__["COLOR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_Reserved2():
    assert hasattr(afpText::BDD, "Reserved2")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_XUPUB():
    assert hasattr(afpText::BDD, "XUPUB")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "XUPUB" in klass.__dict__:
            descriptor = klass.__dict__["XUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_MOD():
    assert hasattr(afpText::BDD, "MOD")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "MOD" in klass.__dict__:
            descriptor = klass.__dict__["MOD"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_WENE():
    assert hasattr(afpText::BDD, "WENE")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "WENE" in klass.__dict__:
            descriptor = klass.__dict__["WENE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_MULT():
    assert hasattr(afpText::BDD, "MULT")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "MULT" in klass.__dict__:
            descriptor = klass.__dict__["MULT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_ELEMENTHEIGHT():
    assert hasattr(afpText::BDD, "ELEMENTHEIGHT")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "ELEMENTHEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["ELEMENTHEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_YUPUB():
    assert hasattr(afpText::BDD, "YUPUB")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "YUPUB" in klass.__dict__:
            descriptor = klass.__dict__["YUPUB"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_MODULEWIDTH():
    assert hasattr(afpText::BDD, "MODULEWIDTH")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "MODULEWIDTH" in klass.__dict__:
            descriptor = klass.__dict__["MODULEWIDTH"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_TYPE():
    assert hasattr(afpText::BDD, "TYPE")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "TYPE" in klass.__dict__:
            descriptor = klass.__dict__["TYPE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_XEXTENT():
    assert hasattr(afpText::BDD, "XEXTENT")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "XEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_LID():
    assert hasattr(afpText::BDD, "LID")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "LID" in klass.__dict__:
            descriptor = klass.__dict__["LID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdd_has_Reserved():
    assert hasattr(afpText::BDD, "Reserved")
    descriptor = None
    for klass in afpText::BDD.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bda_is_not_abstract():
    assert not inspect.isabstract(afpText::BDA)


def test_afptext::bda_constructor_exists():
    assert callable(afpText::BDA.__init__)


def test_afptext::bda_constructor_args():
    sig = inspect.signature(afpText::BDA.__init__)
    params = list(sig.parameters.keys())
    assert "Xoffset" in params, "Missing parameter 'Xoffset'"
    assert "Yoffset" in params, "Missing parameter 'Yoffset'"
    assert "Data" in params, "Missing parameter 'Data'"
    assert "Flags" in params, "Missing parameter 'Flags'"

def test_afptext::bda_has_Xoffset():
    assert hasattr(afpText::BDA, "Xoffset")
    descriptor = None
    for klass in afpText::BDA.__mro__:
        if "Xoffset" in klass.__dict__:
            descriptor = klass.__dict__["Xoffset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bda_has_Yoffset():
    assert hasattr(afpText::BDA, "Yoffset")
    descriptor = None
    for klass in afpText::BDA.__mro__:
        if "Yoffset" in klass.__dict__:
            descriptor = klass.__dict__["Yoffset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bda_has_Data():
    assert hasattr(afpText::BDA, "Data")
    descriptor = None
    for klass in afpText::BDA.__mro__:
        if "Data" in klass.__dict__:
            descriptor = klass.__dict__["Data"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bda_has_Flags():
    assert hasattr(afpText::BDA, "Flags")
    descriptor = None
    for klass in afpText::BDA.__mro__:
        if "Flags" in klass.__dict__:
            descriptor = klass.__dict__["Flags"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bbc_is_not_abstract():
    assert not inspect.isabstract(afpText::BBC)


def test_afptext::bbc_constructor_exists():
    assert callable(afpText::BBC.__init__)


def test_afptext::bbc_constructor_args():
    sig = inspect.signature(afpText::BBC.__init__)
    params = list(sig.parameters.keys())
    assert "BCdoName" in params, "Missing parameter 'BCdoName'"

def test_afptext::bbc_has_BCdoName():
    assert hasattr(afpText::BBC, "BCdoName")
    descriptor = None
    for klass in afpText::BBC.__mro__:
        if "BCdoName" in klass.__dict__:
            descriptor = klass.__dict__["BCdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdi_is_not_abstract():
    assert not inspect.isabstract(afpText::BDI)


def test_afptext::bdi_constructor_exists():
    assert callable(afpText::BDI.__init__)


def test_afptext::bdi_constructor_args():
    sig = inspect.signature(afpText::BDI.__init__)
    params = list(sig.parameters.keys())
    assert "IndxName" in params, "Missing parameter 'IndxName'"

def test_afptext::bdi_has_IndxName():
    assert hasattr(afpText::BDI, "IndxName")
    descriptor = None
    for klass in afpText::BDI.__mro__:
        if "IndxName" in klass.__dict__:
            descriptor = klass.__dict__["IndxName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdm_is_not_abstract():
    assert not inspect.isabstract(afpText::BDM)


def test_afptext::bdm_constructor_exists():
    assert callable(afpText::BDM.__init__)


def test_afptext::bdm_constructor_args():
    sig = inspect.signature(afpText::BDM.__init__)
    params = list(sig.parameters.keys())
    assert "DMName" in params, "Missing parameter 'DMName'"
    assert "DatFmt" in params, "Missing parameter 'DatFmt'"

def test_afptext::bdm_has_DMName():
    assert hasattr(afpText::BDM, "DMName")
    descriptor = None
    for klass in afpText::BDM.__mro__:
        if "DMName" in klass.__dict__:
            descriptor = klass.__dict__["DMName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdm_has_DatFmt():
    assert hasattr(afpText::BDM, "DatFmt")
    descriptor = None
    for klass in afpText::BDM.__mro__:
        if "DatFmt" in klass.__dict__:
            descriptor = klass.__dict__["DatFmt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdg_is_not_abstract():
    assert not inspect.isabstract(afpText::BDG)


def test_afptext::bdg_constructor_exists():
    assert callable(afpText::BDG.__init__)


def test_afptext::bdg_constructor_args():
    sig = inspect.signature(afpText::BDG.__init__)
    params = list(sig.parameters.keys())
    assert "DEGName" in params, "Missing parameter 'DEGName'"

def test_afptext::bdg_has_DEGName():
    assert hasattr(afpText::BDG, "DEGName")
    descriptor = None
    for klass in afpText::BDG.__mro__:
        if "DEGName" in klass.__dict__:
            descriptor = klass.__dict__["DEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bca_is_not_abstract():
    assert not inspect.isabstract(afpText::BCA)


def test_afptext::bca_constructor_exists():
    assert callable(afpText::BCA.__init__)


def test_afptext::bca_constructor_args():
    sig = inspect.signature(afpText::BCA.__init__)
    params = list(sig.parameters.keys())
    assert "CATName" in params, "Missing parameter 'CATName'"

def test_afptext::bca_has_CATName():
    assert hasattr(afpText::BCA, "CATName")
    descriptor = None
    for klass in afpText::BCA.__mro__:
        if "CATName" in klass.__dict__:
            descriptor = klass.__dict__["CATName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bog_is_not_abstract():
    assert not inspect.isabstract(afpText::BOG)


def test_afptext::bog_constructor_exists():
    assert callable(afpText::BOG.__init__)


def test_afptext::bog_constructor_args():
    sig = inspect.signature(afpText::BOG.__init__)
    params = list(sig.parameters.keys())
    assert "OEGName" in params, "Missing parameter 'OEGName'"

def test_afptext::bog_has_OEGName():
    assert hasattr(afpText::BOG, "OEGName")
    descriptor = None
    for klass in afpText::BOG.__mro__:
        if "OEGName" in klass.__dict__:
            descriptor = klass.__dict__["OEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bdt_is_not_abstract():
    assert not inspect.isabstract(afpText::BDT)


def test_afptext::bdt_constructor_exists():
    assert callable(afpText::BDT.__init__)


def test_afptext::bdt_constructor_args():
    sig = inspect.signature(afpText::BDT.__init__)
    params = list(sig.parameters.keys())
    assert "DocName" in params, "Missing parameter 'DocName'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::bdt_has_DocName():
    assert hasattr(afpText::BDT, "DocName")
    descriptor = None
    for klass in afpText::BDT.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::bdt_has_Reserved():
    assert hasattr(afpText::BDT, "Reserved")
    descriptor = None
    for klass in afpText::BDT.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bng_is_not_abstract():
    assert not inspect.isabstract(afpText::BNG)


def test_afptext::bng_constructor_exists():
    assert callable(afpText::BNG.__init__)


def test_afptext::bng_constructor_args():
    sig = inspect.signature(afpText::BNG.__init__)
    params = list(sig.parameters.keys())
    assert "PGrpName" in params, "Missing parameter 'PGrpName'"

def test_afptext::bng_has_PGrpName():
    assert hasattr(afpText::BNG, "PGrpName")
    descriptor = None
    for klass in afpText::BNG.__mro__:
        if "PGrpName" in klass.__dict__:
            descriptor = klass.__dict__["PGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bpf_is_not_abstract():
    assert not inspect.isabstract(afpText::BPF)


def test_afptext::bpf_constructor_exists():
    assert callable(afpText::BPF.__init__)


def test_afptext::bpf_constructor_args():
    sig = inspect.signature(afpText::BPF.__init__)
    params = list(sig.parameters.keys())
    assert "PFName" in params, "Missing parameter 'PFName'"

def test_afptext::bpf_has_PFName():
    assert hasattr(afpText::BPF, "PFName")
    descriptor = None
    for klass in afpText::BPF.__mro__:
        if "PFName" in klass.__dict__:
            descriptor = klass.__dict__["PFName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::linedata_is_not_abstract():
    assert not inspect.isabstract(afpText::LineData)


def test_afptext::linedata_constructor_exists():
    assert callable(afpText::LineData.__init__)


def test_afptext::linedata_constructor_args():
    sig = inspect.signature(afpText::LineData.__init__)
    params = list(sig.parameters.keys())
    assert "linedata" in params, "Missing parameter 'linedata'"

def test_afptext::linedata_has_linedata():
    assert hasattr(afpText::LineData, "linedata")
    descriptor = None
    for klass in afpText::LineData.__mro__:
        if "linedata" in klass.__dict__:
            descriptor = klass.__dict__["linedata"]
            break
    assert isinstance(descriptor, property)



def test_afptext::structuredfield_is_not_abstract():
    assert not inspect.isabstract(afpText::structuredField)


def test_afptext::structuredfield_constructor_exists():
    assert callable(afpText::structuredField.__init__)


def test_afptext::structuredfield_constructor_args():
    sig = inspect.signature(afpText::structuredField.__init__)
    params = list(sig.parameters.keys())



def test_afptext::model_is_not_abstract():
    assert not inspect.isabstract(afpText::Model)


def test_afptext::model_constructor_exists():
    assert callable(afpText::Model.__init__)


def test_afptext::model_constructor_args():
    sig = inspect.signature(afpText::Model.__init__)
    params = list(sig.parameters.keys())



def test_afptext::glinerg_is_not_abstract():
    assert not inspect.isabstract(afpText::GLINERG)


def test_afptext::glinerg_constructor_exists():
    assert callable(afpText::GLINERG.__init__)


def test_afptext::glinerg_constructor_args():
    sig = inspect.signature(afpText::GLINERG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext::glinerg_has_XPOS():
    assert hasattr(afpText::GLINERG, "XPOS")
    descriptor = None
    for klass in afpText::GLINERG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::glinerg_has_YPOS():
    assert hasattr(afpText::GLINERG, "YPOS")
    descriptor = None
    for klass in afpText::GLINERG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcfltrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCFLTRG)


def test_afptext::gcfltrg_constructor_exists():
    assert callable(afpText::GCFLTRG.__init__)


def test_afptext::gcfltrg_constructor_args():
    sig = inspect.signature(afpText::GCFLTRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext::gcfltrg_has_XPOS():
    assert hasattr(afpText::GCFLTRG, "XPOS")
    descriptor = None
    for klass in afpText::GCFLTRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcfltrg_has_YPOS():
    assert hasattr(afpText::GCFLTRG, "YPOS")
    descriptor = None
    for klass in afpText::GCFLTRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gfltrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GFLTRG)


def test_afptext::gfltrg_constructor_exists():
    assert callable(afpText::GFLTRG.__init__)


def test_afptext::gfltrg_constructor_args():
    sig = inspect.signature(afpText::GFLTRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::gfltrg_has_YPOS():
    assert hasattr(afpText::GFLTRG, "YPOS")
    descriptor = None
    for klass in afpText::GFLTRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gfltrg_has_XPOS():
    assert hasattr(afpText::GFLTRG, "XPOS")
    descriptor = None
    for klass in afpText::GFLTRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gccbezrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCCBEZRG)


def test_afptext::gccbezrg_constructor_exists():
    assert callable(afpText::GCCBEZRG.__init__)


def test_afptext::gccbezrg_constructor_args():
    sig = inspect.signature(afpText::GCCBEZRG.__init__)
    params = list(sig.parameters.keys())
    assert "YPOS" in params, "Missing parameter 'YPOS'"
    assert "XPOS" in params, "Missing parameter 'XPOS'"

def test_afptext::gccbezrg_has_YPOS():
    assert hasattr(afpText::GCCBEZRG, "YPOS")
    descriptor = None
    for klass in afpText::GCCBEZRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gccbezrg_has_XPOS():
    assert hasattr(afpText::GCCBEZRG, "XPOS")
    descriptor = None
    for klass in afpText::GCCBEZRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gcbezrg_is_not_abstract():
    assert not inspect.isabstract(afpText::GCBEZRG)


def test_afptext::gcbezrg_constructor_exists():
    assert callable(afpText::GCBEZRG.__init__)


def test_afptext::gcbezrg_constructor_args():
    sig = inspect.signature(afpText::GCBEZRG.__init__)
    params = list(sig.parameters.keys())
    assert "XPOS" in params, "Missing parameter 'XPOS'"
    assert "YPOS" in params, "Missing parameter 'YPOS'"

def test_afptext::gcbezrg_has_XPOS():
    assert hasattr(afpText::GCBEZRG, "XPOS")
    descriptor = None
    for klass in afpText::GCBEZRG.__mro__:
        if "XPOS" in klass.__dict__:
            descriptor = klass.__dict__["XPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::gcbezrg_has_YPOS():
    assert hasattr(afpText::GCBEZRG, "YPOS")
    descriptor = None
    for klass in afpText::GCBEZRG.__mro__:
        if "YPOS" in klass.__dict__:
            descriptor = klass.__dict__["YPOS"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnnrg_is_not_abstract():
    assert not inspect.isabstract(afpText::FNNRG)


def test_afptext::fnnrg_constructor_exists():
    assert callable(afpText::FNNRG.__init__)


def test_afptext::fnnrg_constructor_args():
    sig = inspect.signature(afpText::FNNRG.__init__)
    params = list(sig.parameters.keys())
    assert "TSOffset" in params, "Missing parameter 'TSOffset'"
    assert "GCGID" in params, "Missing parameter 'GCGID'"

def test_afptext::fnnrg_has_TSOffset():
    assert hasattr(afpText::FNNRG, "TSOffset")
    descriptor = None
    for klass in afpText::FNNRG.__mro__:
        if "TSOffset" in klass.__dict__:
            descriptor = klass.__dict__["TSOffset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnnrg_has_GCGID():
    assert hasattr(afpText::FNNRG, "GCGID")
    descriptor = None
    for klass in afpText::FNNRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::externalalgorithmrg_is_not_abstract():
    assert not inspect.isabstract(afpText::ExternalAlgorithmRG)


def test_afptext::externalalgorithmrg_constructor_exists():
    assert callable(afpText::ExternalAlgorithmRG.__init__)


def test_afptext::externalalgorithmrg_constructor_args():
    sig = inspect.signature(afpText::ExternalAlgorithmRG.__init__)
    params = list(sig.parameters.keys())
    assert "PADALMT" in params, "Missing parameter 'PADALMT'"
    assert "DIRCTN" in params, "Missing parameter 'DIRCTN'"
    assert "PADBDRY" in params, "Missing parameter 'PADBDRY'"

def test_afptext::externalalgorithmrg_has_PADALMT():
    assert hasattr(afpText::ExternalAlgorithmRG, "PADALMT")
    descriptor = None
    for klass in afpText::ExternalAlgorithmRG.__mro__:
        if "PADALMT" in klass.__dict__:
            descriptor = klass.__dict__["PADALMT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::externalalgorithmrg_has_DIRCTN():
    assert hasattr(afpText::ExternalAlgorithmRG, "DIRCTN")
    descriptor = None
    for klass in afpText::ExternalAlgorithmRG.__mro__:
        if "DIRCTN" in klass.__dict__:
            descriptor = klass.__dict__["DIRCTN"]
            break
    assert isinstance(descriptor, property)

def test_afptext::externalalgorithmrg_has_PADBDRY():
    assert hasattr(afpText::ExternalAlgorithmRG, "PADBDRY")
    descriptor = None
    for klass in afpText::ExternalAlgorithmRG.__mro__:
        if "PADBDRY" in klass.__dict__:
            descriptor = klass.__dict__["PADBDRY"]
            break
    assert isinstance(descriptor, property)



def test_afptext::samplingratiosrg_is_not_abstract():
    assert not inspect.isabstract(afpText::SamplingRatiosRG)


def test_afptext::samplingratiosrg_constructor_exists():
    assert callable(afpText::SamplingRatiosRG.__init__)


def test_afptext::samplingratiosrg_constructor_args():
    sig = inspect.signature(afpText::SamplingRatiosRG.__init__)
    params = list(sig.parameters.keys())
    assert "VSAMPLE" in params, "Missing parameter 'VSAMPLE'"
    assert "HSAMPLE" in params, "Missing parameter 'HSAMPLE'"

def test_afptext::samplingratiosrg_has_VSAMPLE():
    assert hasattr(afpText::SamplingRatiosRG, "VSAMPLE")
    descriptor = None
    for klass in afpText::SamplingRatiosRG.__mro__:
        if "VSAMPLE" in klass.__dict__:
            descriptor = klass.__dict__["VSAMPLE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::samplingratiosrg_has_HSAMPLE():
    assert hasattr(afpText::SamplingRatiosRG, "HSAMPLE")
    descriptor = None
    for klass in afpText::SamplingRatiosRG.__mro__:
        if "HSAMPLE" in klass.__dict__:
            descriptor = klass.__dict__["HSAMPLE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tiletocrg_is_not_abstract():
    assert not inspect.isabstract(afpText::TileTOCRG)


def test_afptext::tiletocrg_constructor_exists():
    assert callable(afpText::TileTOCRG.__init__)


def test_afptext::tiletocrg_constructor_args():
    sig = inspect.signature(afpText::TileTOCRG.__init__)
    params = list(sig.parameters.keys())
    assert "YOFFSET" in params, "Missing parameter 'YOFFSET'"
    assert "DATAPOS" in params, "Missing parameter 'DATAPOS'"
    assert "RELRES" in params, "Missing parameter 'RELRES'"
    assert "THSIZE" in params, "Missing parameter 'THSIZE'"
    assert "COMPR" in params, "Missing parameter 'COMPR'"
    assert "XOFFSET" in params, "Missing parameter 'XOFFSET'"
    assert "TVSIZE" in params, "Missing parameter 'TVSIZE'"

def test_afptext::tiletocrg_has_YOFFSET():
    assert hasattr(afpText::TileTOCRG, "YOFFSET")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "YOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["YOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_DATAPOS():
    assert hasattr(afpText::TileTOCRG, "DATAPOS")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "DATAPOS" in klass.__dict__:
            descriptor = klass.__dict__["DATAPOS"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_RELRES():
    assert hasattr(afpText::TileTOCRG, "RELRES")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "RELRES" in klass.__dict__:
            descriptor = klass.__dict__["RELRES"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_THSIZE():
    assert hasattr(afpText::TileTOCRG, "THSIZE")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "THSIZE" in klass.__dict__:
            descriptor = klass.__dict__["THSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_COMPR():
    assert hasattr(afpText::TileTOCRG, "COMPR")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "COMPR" in klass.__dict__:
            descriptor = klass.__dict__["COMPR"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_XOFFSET():
    assert hasattr(afpText::TileTOCRG, "XOFFSET")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "XOFFSET" in klass.__dict__:
            descriptor = klass.__dict__["XOFFSET"]
            break
    assert isinstance(descriptor, property)

def test_afptext::tiletocrg_has_TVSIZE():
    assert hasattr(afpText::TileTOCRG, "TVSIZE")
    descriptor = None
    for klass in afpText::TileTOCRG.__mro__:
        if "TVSIZE" in klass.__dict__:
            descriptor = klass.__dict__["TVSIZE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bandimagerg_is_not_abstract():
    assert not inspect.isabstract(afpText::BandImageRG)


def test_afptext::bandimagerg_constructor_exists():
    assert callable(afpText::BandImageRG.__init__)


def test_afptext::bandimagerg_constructor_args():
    sig = inspect.signature(afpText::BandImageRG.__init__)
    params = list(sig.parameters.keys())
    assert "BITCNT" in params, "Missing parameter 'BITCNT'"

def test_afptext::bandimagerg_has_BITCNT():
    assert hasattr(afpText::BandImageRG, "BITCNT")
    descriptor = None
    for klass in afpText::BandImageRG.__mro__:
        if "BITCNT" in klass.__dict__:
            descriptor = klass.__dict__["BITCNT"]
            break
    assert isinstance(descriptor, property)



def test_afptext::tle_is_not_abstract():
    assert not inspect.isabstract(afpText::TLE)


def test_afptext::tle_constructor_exists():
    assert callable(afpText::TLE.__init__)


def test_afptext::tle_constructor_args():
    sig = inspect.signature(afpText::TLE.__init__)
    params = list(sig.parameters.keys())



def test_afptext::ptx_is_not_abstract():
    assert not inspect.isabstract(afpText::PTX)


def test_afptext::ptx_constructor_exists():
    assert callable(afpText::PTX.__init__)


def test_afptext::ptx_constructor_args():
    sig = inspect.signature(afpText::PTX.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fgd_is_not_abstract():
    assert not inspect.isabstract(afpText::FGD)


def test_afptext::fgd_constructor_exists():
    assert callable(afpText::FGD.__init__)


def test_afptext::fgd_constructor_args():
    sig = inspect.signature(afpText::FGD.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"

def test_afptext::fgd_has_ConData():
    assert hasattr(afpText::FGD, "ConData")
    descriptor = None
    for klass in afpText::FGD.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pgp_is_not_abstract():
    assert not inspect.isabstract(afpText::PGP)


def test_afptext::pgp_constructor_exists():
    assert callable(afpText::PGP.__init__)


def test_afptext::pgp_constructor_args():
    sig = inspect.signature(afpText::PGP.__init__)
    params = list(sig.parameters.keys())
    assert "Constant" in params, "Missing parameter 'Constant'"

def test_afptext::pgp_has_Constant():
    assert hasattr(afpText::PGP, "Constant")
    descriptor = None
    for klass in afpText::PGP.__mro__:
        if "Constant" in klass.__dict__:
            descriptor = klass.__dict__["Constant"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ptd1_is_not_abstract():
    assert not inspect.isabstract(afpText::PTD1)


def test_afptext::ptd1_constructor_exists():
    assert callable(afpText::PTD1.__init__)


def test_afptext::ptd1_constructor_args():
    sig = inspect.signature(afpText::PTD1.__init__)
    params = list(sig.parameters.keys())
    assert "YPEXTENT" in params, "Missing parameter 'YPEXTENT'"
    assert "YPUNITVL" in params, "Missing parameter 'YPUNITVL'"
    assert "XPEXTENT" in params, "Missing parameter 'XPEXTENT'"
    assert "XPBASE" in params, "Missing parameter 'XPBASE'"
    assert "YPBASE" in params, "Missing parameter 'YPBASE'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "XPUNITVL" in params, "Missing parameter 'XPUNITVL'"

def test_afptext::ptd1_has_YPEXTENT():
    assert hasattr(afpText::PTD1, "YPEXTENT")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "YPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_YPUNITVL():
    assert hasattr(afpText::PTD1, "YPUNITVL")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "YPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["YPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_XPEXTENT():
    assert hasattr(afpText::PTD1, "XPEXTENT")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "XPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_XPBASE():
    assert hasattr(afpText::PTD1, "XPBASE")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "XPBASE" in klass.__dict__:
            descriptor = klass.__dict__["XPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_YPBASE():
    assert hasattr(afpText::PTD1, "YPBASE")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "YPBASE" in klass.__dict__:
            descriptor = klass.__dict__["YPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_RESERVED():
    assert hasattr(afpText::PTD1, "RESERVED")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd1_has_XPUNITVL():
    assert hasattr(afpText::PTD1, "XPUNITVL")
    descriptor = None
    for klass in afpText::PTD1.__mro__:
        if "XPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["XPUNITVL"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ptd_is_not_abstract():
    assert not inspect.isabstract(afpText::PTD)


def test_afptext::ptd_constructor_exists():
    assert callable(afpText::PTD.__init__)


def test_afptext::ptd_constructor_args():
    sig = inspect.signature(afpText::PTD.__init__)
    params = list(sig.parameters.keys())
    assert "YPUNITVL" in params, "Missing parameter 'YPUNITVL'"
    assert "XPUNITVL" in params, "Missing parameter 'XPUNITVL'"
    assert "YPEXTENT" in params, "Missing parameter 'YPEXTENT'"
    assert "RESERVED" in params, "Missing parameter 'RESERVED'"
    assert "YPBASE" in params, "Missing parameter 'YPBASE'"
    assert "XPEXTENT" in params, "Missing parameter 'XPEXTENT'"
    assert "XPBASE" in params, "Missing parameter 'XPBASE'"

def test_afptext::ptd_has_YPUNITVL():
    assert hasattr(afpText::PTD, "YPUNITVL")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "YPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["YPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_XPUNITVL():
    assert hasattr(afpText::PTD, "XPUNITVL")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "XPUNITVL" in klass.__dict__:
            descriptor = klass.__dict__["XPUNITVL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_YPEXTENT():
    assert hasattr(afpText::PTD, "YPEXTENT")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "YPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["YPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_RESERVED():
    assert hasattr(afpText::PTD, "RESERVED")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "RESERVED" in klass.__dict__:
            descriptor = klass.__dict__["RESERVED"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_YPBASE():
    assert hasattr(afpText::PTD, "YPBASE")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "YPBASE" in klass.__dict__:
            descriptor = klass.__dict__["YPBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_XPEXTENT():
    assert hasattr(afpText::PTD, "XPEXTENT")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "XPEXTENT" in klass.__dict__:
            descriptor = klass.__dict__["XPEXTENT"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ptd_has_XPBASE():
    assert hasattr(afpText::PTD, "XPBASE")
    descriptor = None
    for klass in afpText::PTD.__mro__:
        if "XPBASE" in klass.__dict__:
            descriptor = klass.__dict__["XPBASE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pporg_is_not_abstract():
    assert not inspect.isabstract(afpText::PPORG)


def test_afptext::pporg_constructor_exists():
    assert callable(afpText::PPORG.__init__)


def test_afptext::pporg_constructor_args():
    sig = inspect.signature(afpText::PPORG.__init__)
    params = list(sig.parameters.keys())
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "ProcFlgs" in params, "Missing parameter 'ProcFlgs'"
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"

def test_afptext::pporg_has_YocaOset():
    assert hasattr(afpText::PPORG, "YocaOset")
    descriptor = None
    for klass in afpText::PPORG.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pporg_has_ObjType():
    assert hasattr(afpText::PPORG, "ObjType")
    descriptor = None
    for klass in afpText::PPORG.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pporg_has_RGLength():
    assert hasattr(afpText::PPORG, "RGLength")
    descriptor = None
    for klass in afpText::PPORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pporg_has_ProcFlgs():
    assert hasattr(afpText::PPORG, "ProcFlgs")
    descriptor = None
    for klass in afpText::PPORG.__mro__:
        if "ProcFlgs" in klass.__dict__:
            descriptor = klass.__dict__["ProcFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pporg_has_XocaOset():
    assert hasattr(afpText::PPORG, "XocaOset")
    descriptor = None
    for klass in afpText::PPORG.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ppo_is_not_abstract():
    assert not inspect.isabstract(afpText::PPO)


def test_afptext::ppo_constructor_exists():
    assert callable(afpText::PPO.__init__)


def test_afptext::ppo_constructor_args():
    sig = inspect.signature(afpText::PPO.__init__)
    params = list(sig.parameters.keys())



def test_afptext::pmc_is_not_abstract():
    assert not inspect.isabstract(afpText::PMC)


def test_afptext::pmc_constructor_exists():
    assert callable(afpText::PMC.__init__)


def test_afptext::pmc_constructor_args():
    sig = inspect.signature(afpText::PMC.__init__)
    params = list(sig.parameters.keys())
    assert "PMCid" in params, "Missing parameter 'PMCid'"

def test_afptext::pmc_has_PMCid():
    assert hasattr(afpText::PMC, "PMCid")
    descriptor = None
    for klass in afpText::PMC.__mro__:
        if "PMCid" in klass.__dict__:
            descriptor = klass.__dict__["PMCid"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pgp1_is_not_abstract():
    assert not inspect.isabstract(afpText::PGP1)


def test_afptext::pgp1_constructor_exists():
    assert callable(afpText::PGP1.__init__)


def test_afptext::pgp1_constructor_args():
    sig = inspect.signature(afpText::PGP1.__init__)
    params = list(sig.parameters.keys())
    assert "YOset" in params, "Missing parameter 'YOset'"
    assert "XOset" in params, "Missing parameter 'XOset'"

def test_afptext::pgp1_has_YOset():
    assert hasattr(afpText::PGP1, "YOset")
    descriptor = None
    for klass in afpText::PGP1.__mro__:
        if "YOset" in klass.__dict__:
            descriptor = klass.__dict__["YOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgp1_has_XOset():
    assert hasattr(afpText::PGP1, "XOset")
    descriptor = None
    for klass in afpText::PGP1.__mro__:
        if "XOset" in klass.__dict__:
            descriptor = klass.__dict__["XOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pgprg_is_not_abstract():
    assert not inspect.isabstract(afpText::PGPRG)


def test_afptext::pgprg_constructor_exists():
    assert callable(afpText::PGPRG.__init__)


def test_afptext::pgprg_constructor_args():
    sig = inspect.signature(afpText::PGPRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "YmOset" in params, "Missing parameter 'YmOset'"
    assert "XmOset" in params, "Missing parameter 'XmOset'"
    assert "PMCid" in params, "Missing parameter 'PMCid'"
    assert "PGorient" in params, "Missing parameter 'PGorient'"
    assert "PgFlgs" in params, "Missing parameter 'PgFlgs'"
    assert "SHside" in params, "Missing parameter 'SHside'"

def test_afptext::pgprg_has_RGLength():
    assert hasattr(afpText::PGPRG, "RGLength")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_YmOset():
    assert hasattr(afpText::PGPRG, "YmOset")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "YmOset" in klass.__dict__:
            descriptor = klass.__dict__["YmOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_XmOset():
    assert hasattr(afpText::PGPRG, "XmOset")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "XmOset" in klass.__dict__:
            descriptor = klass.__dict__["XmOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_PMCid():
    assert hasattr(afpText::PGPRG, "PMCid")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "PMCid" in klass.__dict__:
            descriptor = klass.__dict__["PMCid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_PGorient():
    assert hasattr(afpText::PGPRG, "PGorient")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "PGorient" in klass.__dict__:
            descriptor = klass.__dict__["PGorient"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_PgFlgs():
    assert hasattr(afpText::PGPRG, "PgFlgs")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "PgFlgs" in klass.__dict__:
            descriptor = klass.__dict__["PgFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgprg_has_SHside():
    assert hasattr(afpText::PGPRG, "SHside")
    descriptor = None
    for klass in afpText::PGPRG.__mro__:
        if "SHside" in klass.__dict__:
            descriptor = klass.__dict__["SHside"]
            break
    assert isinstance(descriptor, property)



def test_afptext::nop_is_not_abstract():
    assert not inspect.isabstract(afpText::NOP)


def test_afptext::nop_constructor_exists():
    assert callable(afpText::NOP.__init__)


def test_afptext::nop_constructor_args():
    sig = inspect.signature(afpText::NOP.__init__)
    params = list(sig.parameters.keys())
    assert "UndfData" in params, "Missing parameter 'UndfData'"

def test_afptext::nop_has_UndfData():
    assert hasattr(afpText::NOP, "UndfData")
    descriptor = None
    for klass in afpText::NOP.__mro__:
        if "UndfData" in klass.__dict__:
            descriptor = klass.__dict__["UndfData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::msurg_is_not_abstract():
    assert not inspect.isabstract(afpText::MSURG)


def test_afptext::msurg_constructor_exists():
    assert callable(afpText::MSURG.__init__)


def test_afptext::msurg_constructor_args():
    sig = inspect.signature(afpText::MSURG.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "SUPname" in params, "Missing parameter 'SUPname'"
    assert "SUPid" in params, "Missing parameter 'SUPid'"

def test_afptext::msurg_has_Reserved():
    assert hasattr(afpText::MSURG, "Reserved")
    descriptor = None
    for klass in afpText::MSURG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::msurg_has_SUPname():
    assert hasattr(afpText::MSURG, "SUPname")
    descriptor = None
    for klass in afpText::MSURG.__mro__:
        if "SUPname" in klass.__dict__:
            descriptor = klass.__dict__["SUPname"]
            break
    assert isinstance(descriptor, property)

def test_afptext::msurg_has_SUPid():
    assert hasattr(afpText::MSURG, "SUPid")
    descriptor = None
    for klass in afpText::MSURG.__mro__:
        if "SUPid" in klass.__dict__:
            descriptor = klass.__dict__["SUPid"]
            break
    assert isinstance(descriptor, property)



def test_afptext::msu_is_not_abstract():
    assert not inspect.isabstract(afpText::MSU)


def test_afptext::msu_constructor_exists():
    assert callable(afpText::MSU.__init__)


def test_afptext::msu_constructor_args():
    sig = inspect.signature(afpText::MSU.__init__)
    params = list(sig.parameters.keys())



def test_afptext::pgd_is_not_abstract():
    assert not inspect.isabstract(afpText::PGD)


def test_afptext::pgd_constructor_exists():
    assert callable(afpText::PGD.__init__)


def test_afptext::pgd_constructor_args():
    sig = inspect.signature(afpText::PGD.__init__)
    params = list(sig.parameters.keys())
    assert "XpgBase" in params, "Missing parameter 'XpgBase'"
    assert "YpgSize" in params, "Missing parameter 'YpgSize'"
    assert "XpgUnits" in params, "Missing parameter 'XpgUnits'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "YpgUnits" in params, "Missing parameter 'YpgUnits'"
    assert "YpgBase" in params, "Missing parameter 'YpgBase'"
    assert "XpgSize" in params, "Missing parameter 'XpgSize'"

def test_afptext::pgd_has_XpgBase():
    assert hasattr(afpText::PGD, "XpgBase")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "XpgBase" in klass.__dict__:
            descriptor = klass.__dict__["XpgBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_YpgSize():
    assert hasattr(afpText::PGD, "YpgSize")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "YpgSize" in klass.__dict__:
            descriptor = klass.__dict__["YpgSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_XpgUnits():
    assert hasattr(afpText::PGD, "XpgUnits")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "XpgUnits" in klass.__dict__:
            descriptor = klass.__dict__["XpgUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_Reserved():
    assert hasattr(afpText::PGD, "Reserved")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_YpgUnits():
    assert hasattr(afpText::PGD, "YpgUnits")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "YpgUnits" in klass.__dict__:
            descriptor = klass.__dict__["YpgUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_YpgBase():
    assert hasattr(afpText::PGD, "YpgBase")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "YpgBase" in klass.__dict__:
            descriptor = klass.__dict__["YpgBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::pgd_has_XpgSize():
    assert hasattr(afpText::PGD, "XpgSize")
    descriptor = None
    for klass in afpText::PGD.__mro__:
        if "XpgSize" in klass.__dict__:
            descriptor = klass.__dict__["XpgSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pfc_is_not_abstract():
    assert not inspect.isabstract(afpText::PFC)


def test_afptext::pfc_constructor_exists():
    assert callable(afpText::PFC.__init__)


def test_afptext::pfc_constructor_args():
    sig = inspect.signature(afpText::PFC.__init__)
    params = list(sig.parameters.keys())
    assert "PFCFlgs" in params, "Missing parameter 'PFCFlgs'"

def test_afptext::pfc_has_PFCFlgs():
    assert hasattr(afpText::PFC, "PFCFlgs")
    descriptor = None
    for klass in afpText::PFC.__mro__:
        if "PFCFlgs" in klass.__dict__:
            descriptor = klass.__dict__["PFCFlgs"]
            break
    assert isinstance(descriptor, property)



def test_afptext::pec_is_not_abstract():
    assert not inspect.isabstract(afpText::PEC)


def test_afptext::pec_constructor_exists():
    assert callable(afpText::PEC.__init__)


def test_afptext::pec_constructor_args():
    sig = inspect.signature(afpText::PEC.__init__)
    params = list(sig.parameters.keys())



def test_afptext::ocd_is_not_abstract():
    assert not inspect.isabstract(afpText::OCD)


def test_afptext::ocd_constructor_exists():
    assert callable(afpText::OCD.__init__)


def test_afptext::ocd_constructor_args():
    sig = inspect.signature(afpText::OCD.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCdat" in params, "Missing parameter 'ObjCdat'"

def test_afptext::ocd_has_ObjCdat():
    assert hasattr(afpText::OCD, "ObjCdat")
    descriptor = None
    for klass in afpText::OCD.__mro__:
        if "ObjCdat" in klass.__dict__:
            descriptor = klass.__dict__["ObjCdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext::obp_is_not_abstract():
    assert not inspect.isabstract(afpText::OBP)


def test_afptext::obp_constructor_exists():
    assert callable(afpText::OBP.__init__)


def test_afptext::obp_constructor_args():
    sig = inspect.signature(afpText::OBP.__init__)
    params = list(sig.parameters.keys())
    assert "YocaOrent" in params, "Missing parameter 'YocaOrent'"
    assert "XocaOrent" in params, "Missing parameter 'XocaOrent'"
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"
    assert "RefCSys" in params, "Missing parameter 'RefCSys'"
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "OAPosID" in params, "Missing parameter 'OAPosID'"

def test_afptext::obp_has_YocaOrent():
    assert hasattr(afpText::OBP, "YocaOrent")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "YocaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YocaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_XocaOrent():
    assert hasattr(afpText::OBP, "XocaOrent")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "XocaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XocaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_YocaOset():
    assert hasattr(afpText::OBP, "YocaOset")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_RGLength():
    assert hasattr(afpText::OBP, "RGLength")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_YoaOrent():
    assert hasattr(afpText::OBP, "YoaOrent")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_XocaOset():
    assert hasattr(afpText::OBP, "XocaOset")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_RefCSys():
    assert hasattr(afpText::OBP, "RefCSys")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "RefCSys" in klass.__dict__:
            descriptor = klass.__dict__["RefCSys"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_XoaOrent():
    assert hasattr(afpText::OBP, "XoaOrent")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_YoaOset():
    assert hasattr(afpText::OBP, "YoaOset")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_XoaOset():
    assert hasattr(afpText::OBP, "XoaOset")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::obp_has_OAPosID():
    assert hasattr(afpText::OBP, "OAPosID")
    descriptor = None
    for klass in afpText::OBP.__mro__:
        if "OAPosID" in klass.__dict__:
            descriptor = klass.__dict__["OAPosID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::obd_is_not_abstract():
    assert not inspect.isabstract(afpText::OBD)


def test_afptext::obd_constructor_exists():
    assert callable(afpText::OBD.__init__)


def test_afptext::obd_constructor_args():
    sig = inspect.signature(afpText::OBD.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mgo_is_not_abstract():
    assert not inspect.isabstract(afpText::MGO)


def test_afptext::mgo_constructor_exists():
    assert callable(afpText::MGO.__init__)


def test_afptext::mgo_constructor_args():
    sig = inspect.signature(afpText::MGO.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mpsrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MPSRG)


def test_afptext::mpsrg_constructor_exists():
    assert callable(afpText::MPSRG.__init__)


def test_afptext::mpsrg_constructor_args():
    sig = inspect.signature(afpText::MPSRG.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext::mpsrg_has_Reserved():
    assert hasattr(afpText::MPSRG, "Reserved")
    descriptor = None
    for klass in afpText::MPSRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mpsrg_has_PsegName():
    assert hasattr(afpText::MPSRG, "PsegName")
    descriptor = None
    for klass in afpText::MPSRG.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mps_is_not_abstract():
    assert not inspect.isabstract(afpText::MPS)


def test_afptext::mps_constructor_exists():
    assert callable(afpText::MPS.__init__)


def test_afptext::mps_constructor_args():
    sig = inspect.signature(afpText::MPS.__init__)
    params = list(sig.parameters.keys())
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mps_has_Reserved():
    assert hasattr(afpText::MPS, "Reserved")
    descriptor = None
    for klass in afpText::MPS.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mps_has_RGLength():
    assert hasattr(afpText::MPS, "RGLength")
    descriptor = None
    for klass in afpText::MPS.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mporg_is_not_abstract():
    assert not inspect.isabstract(afpText::MPORG)


def test_afptext::mporg_constructor_exists():
    assert callable(afpText::MPORG.__init__)


def test_afptext::mporg_constructor_args():
    sig = inspect.signature(afpText::MPORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mporg_has_RGLength():
    assert hasattr(afpText::MPORG, "RGLength")
    descriptor = None
    for klass in afpText::MPORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mpo_is_not_abstract():
    assert not inspect.isabstract(afpText::MPO)


def test_afptext::mpo_constructor_exists():
    assert callable(afpText::MPO.__init__)


def test_afptext::mpo_constructor_args():
    sig = inspect.signature(afpText::MPO.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mpgrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MPGRG)


def test_afptext::mpgrg_constructor_exists():
    assert callable(afpText::MPGRG.__init__)


def test_afptext::mpgrg_constructor_args():
    sig = inspect.signature(afpText::MPGRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mpgrg_has_RGLength():
    assert hasattr(afpText::MPGRG, "RGLength")
    descriptor = None
    for klass in afpText::MPGRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mpg_is_not_abstract():
    assert not inspect.isabstract(afpText::MPG)


def test_afptext::mpg_constructor_exists():
    assert callable(afpText::MPG.__init__)


def test_afptext::mpg_constructor_args():
    sig = inspect.signature(afpText::MPG.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mmtrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MMTRG)


def test_afptext::mmtrg_constructor_exists():
    assert callable(afpText::MMTRG.__init__)


def test_afptext::mmtrg_constructor_args():
    sig = inspect.signature(afpText::MMTRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mmtrg_has_RGLength():
    assert hasattr(afpText::MMTRG, "RGLength")
    descriptor = None
    for klass in afpText::MMTRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mmt_is_not_abstract():
    assert not inspect.isabstract(afpText::MMT)


def test_afptext::mmt_constructor_exists():
    assert callable(afpText::MMT.__init__)


def test_afptext::mmt_constructor_args():
    sig = inspect.signature(afpText::MMT.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mmorg_is_not_abstract():
    assert not inspect.isabstract(afpText::MMORG)


def test_afptext::mmorg_constructor_exists():
    assert callable(afpText::MMORG.__init__)


def test_afptext::mmorg_constructor_args():
    sig = inspect.signature(afpText::MMORG.__init__)
    params = list(sig.parameters.keys())
    assert "OVLname" in params, "Missing parameter 'OVLname'"
    assert "OVLid" in params, "Missing parameter 'OVLid'"
    assert "Flags" in params, "Missing parameter 'Flags'"

def test_afptext::mmorg_has_OVLname():
    assert hasattr(afpText::MMORG, "OVLname")
    descriptor = None
    for klass in afpText::MMORG.__mro__:
        if "OVLname" in klass.__dict__:
            descriptor = klass.__dict__["OVLname"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mmorg_has_OVLid():
    assert hasattr(afpText::MMORG, "OVLid")
    descriptor = None
    for klass in afpText::MMORG.__mro__:
        if "OVLid" in klass.__dict__:
            descriptor = klass.__dict__["OVLid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mmorg_has_Flags():
    assert hasattr(afpText::MMORG, "Flags")
    descriptor = None
    for klass in afpText::MMORG.__mro__:
        if "Flags" in klass.__dict__:
            descriptor = klass.__dict__["Flags"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mmo_is_not_abstract():
    assert not inspect.isabstract(afpText::MMO)


def test_afptext::mmo_constructor_exists():
    assert callable(afpText::MMO.__init__)


def test_afptext::mmo_constructor_args():
    sig = inspect.signature(afpText::MMO.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mmo_has_RGLength():
    assert hasattr(afpText::MMO, "RGLength")
    descriptor = None
    for klass in afpText::MMO.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mmdrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MMDRG)


def test_afptext::mmdrg_constructor_exists():
    assert callable(afpText::MMDRG.__init__)


def test_afptext::mmdrg_constructor_args():
    sig = inspect.signature(afpText::MMDRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mmdrg_has_RGLength():
    assert hasattr(afpText::MMDRG, "RGLength")
    descriptor = None
    for klass in afpText::MMDRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mmd_is_not_abstract():
    assert not inspect.isabstract(afpText::MMD)


def test_afptext::mmd_constructor_exists():
    assert callable(afpText::MMD.__init__)


def test_afptext::mmd_constructor_args():
    sig = inspect.signature(afpText::MMD.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mmcrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MMCRG)


def test_afptext::mmcrg_constructor_exists():
    assert callable(afpText::MMCRG.__init__)


def test_afptext::mmcrg_constructor_args():
    sig = inspect.signature(afpText::MMCRG.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_afptext::mmcrg_has_key():
    assert hasattr(afpText::MMCRG, "key")
    descriptor = None
    for klass in afpText::MMCRG.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mmcrg_has_value():
    assert hasattr(afpText::MMCRG, "value")
    descriptor = None
    for klass in afpText::MMCRG.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mmc_is_not_abstract():
    assert not inspect.isabstract(afpText::MMC)


def test_afptext::mmc_constructor_exists():
    assert callable(afpText::MMC.__init__)


def test_afptext::mmc_constructor_args():
    sig = inspect.signature(afpText::MMC.__init__)
    params = list(sig.parameters.keys())
    assert "MMCid" in params, "Missing parameter 'MMCid'"
    assert "PARAMETER1" in params, "Missing parameter 'PARAMETER1'"

def test_afptext::mmc_has_MMCid():
    assert hasattr(afpText::MMC, "MMCid")
    descriptor = None
    for klass in afpText::MMC.__mro__:
        if "MMCid" in klass.__dict__:
            descriptor = klass.__dict__["MMCid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mmc_has_PARAMETER1():
    assert hasattr(afpText::MMC, "PARAMETER1")
    descriptor = None
    for klass in afpText::MMC.__mro__:
        if "PARAMETER1" in klass.__dict__:
            descriptor = klass.__dict__["PARAMETER1"]
            break
    assert isinstance(descriptor, property)



def test_afptext::miorg_is_not_abstract():
    assert not inspect.isabstract(afpText::MIORG)


def test_afptext::miorg_constructor_exists():
    assert callable(afpText::MIORG.__init__)


def test_afptext::miorg_constructor_args():
    sig = inspect.signature(afpText::MIORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::miorg_has_RGLength():
    assert hasattr(afpText::MIORG, "RGLength")
    descriptor = None
    for klass in afpText::MIORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mio_is_not_abstract():
    assert not inspect.isabstract(afpText::MIO)


def test_afptext::mio_constructor_exists():
    assert callable(afpText::MIO.__init__)


def test_afptext::mio_constructor_args():
    sig = inspect.signature(afpText::MIO.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mgorg_is_not_abstract():
    assert not inspect.isabstract(afpText::MGORG)


def test_afptext::mgorg_constructor_exists():
    assert callable(afpText::MGORG.__init__)


def test_afptext::mgorg_constructor_args():
    sig = inspect.signature(afpText::MGORG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mgorg_has_RGLength():
    assert hasattr(afpText::MGORG, "RGLength")
    descriptor = None
    for klass in afpText::MGORG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcc_is_not_abstract():
    assert not inspect.isabstract(afpText::MCC)


def test_afptext::mcc_constructor_exists():
    assert callable(afpText::MCC.__init__)


def test_afptext::mcc_constructor_args():
    sig = inspect.signature(afpText::MCC.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mcarg_is_not_abstract():
    assert not inspect.isabstract(afpText::MCARG)


def test_afptext::mcarg_constructor_exists():
    assert callable(afpText::MCARG.__init__)


def test_afptext::mcarg_constructor_args():
    sig = inspect.signature(afpText::MCARG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mcarg_has_RGLength():
    assert hasattr(afpText::MCARG, "RGLength")
    descriptor = None
    for klass in afpText::MCARG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mca_is_not_abstract():
    assert not inspect.isabstract(afpText::MCA)


def test_afptext::mca_constructor_exists():
    assert callable(afpText::MCA.__init__)


def test_afptext::mca_constructor_args():
    sig = inspect.signature(afpText::MCA.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mfc_is_not_abstract():
    assert not inspect.isabstract(afpText::MFC)


def test_afptext::mfc_constructor_exists():
    assert callable(afpText::MFC.__init__)


def test_afptext::mfc_constructor_args():
    sig = inspect.signature(afpText::MFC.__init__)
    params = list(sig.parameters.keys())
    assert "MFCScpe" in params, "Missing parameter 'MFCScpe'"
    assert "MedColl" in params, "Missing parameter 'MedColl'"
    assert "MFCFlgs" in params, "Missing parameter 'MFCFlgs'"

def test_afptext::mfc_has_MFCScpe():
    assert hasattr(afpText::MFC, "MFCScpe")
    descriptor = None
    for klass in afpText::MFC.__mro__:
        if "MFCScpe" in klass.__dict__:
            descriptor = klass.__dict__["MFCScpe"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mfc_has_MedColl():
    assert hasattr(afpText::MFC, "MedColl")
    descriptor = None
    for klass in afpText::MFC.__mro__:
        if "MedColl" in klass.__dict__:
            descriptor = klass.__dict__["MedColl"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mfc_has_MFCFlgs():
    assert hasattr(afpText::MFC, "MFCFlgs")
    descriptor = None
    for klass in afpText::MFC.__mro__:
        if "MFCFlgs" in klass.__dict__:
            descriptor = klass.__dict__["MFCFlgs"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mdrrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MDRRG)


def test_afptext::mdrrg_constructor_exists():
    assert callable(afpText::MDRRG.__init__)


def test_afptext::mdrrg_constructor_args():
    sig = inspect.signature(afpText::MDRRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mdrrg_has_RGLength():
    assert hasattr(afpText::MDRRG, "RGLength")
    descriptor = None
    for klass in afpText::MDRRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mdr_is_not_abstract():
    assert not inspect.isabstract(afpText::MDR)


def test_afptext::mdr_constructor_exists():
    assert callable(afpText::MDR.__init__)


def test_afptext::mdr_constructor_args():
    sig = inspect.signature(afpText::MDR.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mdd_is_not_abstract():
    assert not inspect.isabstract(afpText::MDD)


def test_afptext::mdd_constructor_exists():
    assert callable(afpText::MDD.__init__)


def test_afptext::mdd_constructor_args():
    sig = inspect.signature(afpText::MDD.__init__)
    params = list(sig.parameters.keys())
    assert "XmSize" in params, "Missing parameter 'XmSize'"
    assert "MDDFlgs" in params, "Missing parameter 'MDDFlgs'"
    assert "YmBase" in params, "Missing parameter 'YmBase'"
    assert "YmUnits" in params, "Missing parameter 'YmUnits'"
    assert "YmSize" in params, "Missing parameter 'YmSize'"
    assert "XmUnits" in params, "Missing parameter 'XmUnits'"
    assert "XmBase" in params, "Missing parameter 'XmBase'"

def test_afptext::mdd_has_XmSize():
    assert hasattr(afpText::MDD, "XmSize")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "XmSize" in klass.__dict__:
            descriptor = klass.__dict__["XmSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_MDDFlgs():
    assert hasattr(afpText::MDD, "MDDFlgs")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "MDDFlgs" in klass.__dict__:
            descriptor = klass.__dict__["MDDFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_YmBase():
    assert hasattr(afpText::MDD, "YmBase")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "YmBase" in klass.__dict__:
            descriptor = klass.__dict__["YmBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_YmUnits():
    assert hasattr(afpText::MDD, "YmUnits")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "YmUnits" in klass.__dict__:
            descriptor = klass.__dict__["YmUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_YmSize():
    assert hasattr(afpText::MDD, "YmSize")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "YmSize" in klass.__dict__:
            descriptor = klass.__dict__["YmSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_XmUnits():
    assert hasattr(afpText::MDD, "XmUnits")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "XmUnits" in klass.__dict__:
            descriptor = klass.__dict__["XmUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mdd_has_XmBase():
    assert hasattr(afpText::MDD, "XmBase")
    descriptor = None
    for klass in afpText::MDD.__mro__:
        if "XmBase" in klass.__dict__:
            descriptor = klass.__dict__["XmBase"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcf1rg_is_not_abstract():
    assert not inspect.isabstract(afpText::MCF1RG)


def test_afptext::mcf1rg_constructor_exists():
    assert callable(afpText::MCF1RG.__init__)


def test_afptext::mcf1rg_constructor_args():
    sig = inspect.signature(afpText::MCF1RG.__init__)
    params = list(sig.parameters.keys())
    assert "CFLid" in params, "Missing parameter 'CFLid'"
    assert "CPName" in params, "Missing parameter 'CPName'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"
    assert "Sectid" in params, "Missing parameter 'Sectid'"
    assert "CFName" in params, "Missing parameter 'CFName'"
    assert "FCSName" in params, "Missing parameter 'FCSName'"

def test_afptext::mcf1rg_has_CFLid():
    assert hasattr(afpText::MCF1RG, "CFLid")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "CFLid" in klass.__dict__:
            descriptor = klass.__dict__["CFLid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mcf1rg_has_CPName():
    assert hasattr(afpText::MCF1RG, "CPName")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "CPName" in klass.__dict__:
            descriptor = klass.__dict__["CPName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mcf1rg_has_CharRot():
    assert hasattr(afpText::MCF1RG, "CharRot")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mcf1rg_has_Sectid():
    assert hasattr(afpText::MCF1RG, "Sectid")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "Sectid" in klass.__dict__:
            descriptor = klass.__dict__["Sectid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mcf1rg_has_CFName():
    assert hasattr(afpText::MCF1RG, "CFName")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "CFName" in klass.__dict__:
            descriptor = klass.__dict__["CFName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mcf1rg_has_FCSName():
    assert hasattr(afpText::MCF1RG, "FCSName")
    descriptor = None
    for klass in afpText::MCF1RG.__mro__:
        if "FCSName" in klass.__dict__:
            descriptor = klass.__dict__["FCSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcf1_is_not_abstract():
    assert not inspect.isabstract(afpText::MCF1)


def test_afptext::mcf1_constructor_exists():
    assert callable(afpText::MCF1.__init__)


def test_afptext::mcf1_constructor_args():
    sig = inspect.signature(afpText::MCF1.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mcf1_has_RGLength():
    assert hasattr(afpText::MCF1, "RGLength")
    descriptor = None
    for klass in afpText::MCF1.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcfrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MCFRG)


def test_afptext::mcfrg_constructor_exists():
    assert callable(afpText::MCFRG.__init__)


def test_afptext::mcfrg_constructor_args():
    sig = inspect.signature(afpText::MCFRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mcfrg_has_RGLength():
    assert hasattr(afpText::MCFRG, "RGLength")
    descriptor = None
    for klass in afpText::MCFRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcf_is_not_abstract():
    assert not inspect.isabstract(afpText::MCF)


def test_afptext::mcf_constructor_exists():
    assert callable(afpText::MCF.__init__)


def test_afptext::mcf_constructor_args():
    sig = inspect.signature(afpText::MCF.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mcdrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MCDRG)


def test_afptext::mcdrg_constructor_exists():
    assert callable(afpText::MCDRG.__init__)


def test_afptext::mcdrg_constructor_args():
    sig = inspect.signature(afpText::MCDRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mcdrg_has_RGLength():
    assert hasattr(afpText::MCDRG, "RGLength")
    descriptor = None
    for klass in afpText::MCDRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mcd_is_not_abstract():
    assert not inspect.isabstract(afpText::MCD)


def test_afptext::mcd_constructor_exists():
    assert callable(afpText::MCD.__init__)


def test_afptext::mcd_constructor_args():
    sig = inspect.signature(afpText::MCD.__init__)
    params = list(sig.parameters.keys())



def test_afptext::mccrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MCCRG)


def test_afptext::mccrg_constructor_exists():
    assert callable(afpText::MCCRG.__init__)


def test_afptext::mccrg_constructor_args():
    sig = inspect.signature(afpText::MCCRG.__init__)
    params = list(sig.parameters.keys())
    assert "Startnum" in params, "Missing parameter 'Startnum'"
    assert "Stopnum" in params, "Missing parameter 'Stopnum'"
    assert "MMCid" in params, "Missing parameter 'MMCid'"

def test_afptext::mccrg_has_Startnum():
    assert hasattr(afpText::MCCRG, "Startnum")
    descriptor = None
    for klass in afpText::MCCRG.__mro__:
        if "Startnum" in klass.__dict__:
            descriptor = klass.__dict__["Startnum"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mccrg_has_Stopnum():
    assert hasattr(afpText::MCCRG, "Stopnum")
    descriptor = None
    for klass in afpText::MCCRG.__mro__:
        if "Stopnum" in klass.__dict__:
            descriptor = klass.__dict__["Stopnum"]
            break
    assert isinstance(descriptor, property)

def test_afptext::mccrg_has_MMCid():
    assert hasattr(afpText::MCCRG, "MMCid")
    descriptor = None
    for klass in afpText::MCCRG.__mro__:
        if "MMCid" in klass.__dict__:
            descriptor = klass.__dict__["MMCid"]
            break
    assert isinstance(descriptor, property)



def test_afptext::lle_is_not_abstract():
    assert not inspect.isabstract(afpText::LLE)


def test_afptext::lle_constructor_exists():
    assert callable(afpText::LLE.__init__)


def test_afptext::lle_constructor_args():
    sig = inspect.signature(afpText::LLE.__init__)
    params = list(sig.parameters.keys())
    assert "LnkType" in params, "Missing parameter 'LnkType'"

def test_afptext::lle_has_LnkType():
    assert hasattr(afpText::LLE, "LnkType")
    descriptor = None
    for klass in afpText::LLE.__mro__:
        if "LnkType" in klass.__dict__:
            descriptor = klass.__dict__["LnkType"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mbcrg_is_not_abstract():
    assert not inspect.isabstract(afpText::MBCRG)


def test_afptext::mbcrg_constructor_exists():
    assert callable(afpText::MBCRG.__init__)


def test_afptext::mbcrg_constructor_args():
    sig = inspect.signature(afpText::MBCRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"

def test_afptext::mbcrg_has_RGLength():
    assert hasattr(afpText::MBCRG, "RGLength")
    descriptor = None
    for klass in afpText::MBCRG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)



def test_afptext::mbc_is_not_abstract():
    assert not inspect.isabstract(afpText::MBC)


def test_afptext::mbc_constructor_exists():
    assert callable(afpText::MBC.__init__)


def test_afptext::mbc_constructor_args():
    sig = inspect.signature(afpText::MBC.__init__)
    params = list(sig.parameters.keys())



def test_afptext::lnd_is_not_abstract():
    assert not inspect.isabstract(afpText::LND)


def test_afptext::lnd_constructor_exists():
    assert callable(afpText::LND.__init__)


def test_afptext::lnd_constructor_args():
    sig = inspect.signature(afpText::LND.__init__)
    params = list(sig.parameters.keys())
    assert "TxtOrent" in params, "Missing parameter 'TxtOrent'"
    assert "SubpgID" in params, "Missing parameter 'SubpgID'"
    assert "DataLgth" in params, "Missing parameter 'DataLgth'"
    assert "NLNDskp" in params, "Missing parameter 'NLNDskp'"
    assert "ChnlCde" in params, "Missing parameter 'ChnlCde'"
    assert "SupName" in params, "Missing parameter 'SupName'"
    assert "NLNDreu" in params, "Missing parameter 'NLNDreu'"
    assert "LNDFlgs" in params, "Missing parameter 'LNDFlgs'"
    assert "CCPID" in params, "Missing parameter 'CCPID'"
    assert "TxtColor" in params, "Missing parameter 'TxtColor'"
    assert "NLNDsp" in params, "Missing parameter 'NLNDsp'"
    assert "SOLid" in params, "Missing parameter 'SOLid'"
    assert "FntLID" in params, "Missing parameter 'FntLID'"
    assert "BPos" in params, "Missing parameter 'BPos'"
    assert "IPos" in params, "Missing parameter 'IPos'"
    assert "NLNDccp" in params, "Missing parameter 'NLNDccp'"
    assert "DataStrt" in params, "Missing parameter 'DataStrt'"

def test_afptext::lnd_has_TxtOrent():
    assert hasattr(afpText::LND, "TxtOrent")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "TxtOrent" in klass.__dict__:
            descriptor = klass.__dict__["TxtOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_SubpgID():
    assert hasattr(afpText::LND, "SubpgID")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "SubpgID" in klass.__dict__:
            descriptor = klass.__dict__["SubpgID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_DataLgth():
    assert hasattr(afpText::LND, "DataLgth")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "DataLgth" in klass.__dict__:
            descriptor = klass.__dict__["DataLgth"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_NLNDskp():
    assert hasattr(afpText::LND, "NLNDskp")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "NLNDskp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDskp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_ChnlCde():
    assert hasattr(afpText::LND, "ChnlCde")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "ChnlCde" in klass.__dict__:
            descriptor = klass.__dict__["ChnlCde"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_SupName():
    assert hasattr(afpText::LND, "SupName")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "SupName" in klass.__dict__:
            descriptor = klass.__dict__["SupName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_NLNDreu():
    assert hasattr(afpText::LND, "NLNDreu")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "NLNDreu" in klass.__dict__:
            descriptor = klass.__dict__["NLNDreu"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_LNDFlgs():
    assert hasattr(afpText::LND, "LNDFlgs")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "LNDFlgs" in klass.__dict__:
            descriptor = klass.__dict__["LNDFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_CCPID():
    assert hasattr(afpText::LND, "CCPID")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "CCPID" in klass.__dict__:
            descriptor = klass.__dict__["CCPID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_TxtColor():
    assert hasattr(afpText::LND, "TxtColor")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "TxtColor" in klass.__dict__:
            descriptor = klass.__dict__["TxtColor"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_NLNDsp():
    assert hasattr(afpText::LND, "NLNDsp")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "NLNDsp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDsp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_SOLid():
    assert hasattr(afpText::LND, "SOLid")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "SOLid" in klass.__dict__:
            descriptor = klass.__dict__["SOLid"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_FntLID():
    assert hasattr(afpText::LND, "FntLID")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "FntLID" in klass.__dict__:
            descriptor = klass.__dict__["FntLID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_BPos():
    assert hasattr(afpText::LND, "BPos")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "BPos" in klass.__dict__:
            descriptor = klass.__dict__["BPos"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_IPos():
    assert hasattr(afpText::LND, "IPos")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "IPos" in klass.__dict__:
            descriptor = klass.__dict__["IPos"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_NLNDccp():
    assert hasattr(afpText::LND, "NLNDccp")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "NLNDccp" in klass.__dict__:
            descriptor = klass.__dict__["NLNDccp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::lnd_has_DataStrt():
    assert hasattr(afpText::LND, "DataStrt")
    descriptor = None
    for klass in afpText::LND.__mro__:
        if "DataStrt" in klass.__dict__:
            descriptor = klass.__dict__["DataStrt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::lnc_is_not_abstract():
    assert not inspect.isabstract(afpText::LNC)


def test_afptext::lnc_constructor_exists():
    assert callable(afpText::LNC.__init__)


def test_afptext::lnc_constructor_args():
    sig = inspect.signature(afpText::LNC.__init__)
    params = list(sig.parameters.keys())
    assert "NumDSC" in params, "Missing parameter 'NumDSC'"

def test_afptext::lnc_has_NumDSC():
    assert hasattr(afpText::LNC, "NumDSC")
    descriptor = None
    for klass in afpText::LNC.__mro__:
        if "NumDSC" in klass.__dict__:
            descriptor = klass.__dict__["NumDSC"]
            break
    assert isinstance(descriptor, property)



def test_afptext::llerg_is_not_abstract():
    assert not inspect.isabstract(afpText::LLERG)


def test_afptext::llerg_constructor_exists():
    assert callable(afpText::LLERG.__init__)


def test_afptext::llerg_constructor_args():
    sig = inspect.signature(afpText::LLERG.__init__)
    params = list(sig.parameters.keys())
    assert "RGLength" in params, "Missing parameter 'RGLength'"
    assert "RGFunct" in params, "Missing parameter 'RGFunct'"

def test_afptext::llerg_has_RGLength():
    assert hasattr(afpText::LLERG, "RGLength")
    descriptor = None
    for klass in afpText::LLERG.__mro__:
        if "RGLength" in klass.__dict__:
            descriptor = klass.__dict__["RGLength"]
            break
    assert isinstance(descriptor, property)

def test_afptext::llerg_has_RGFunct():
    assert hasattr(afpText::LLERG, "RGFunct")
    descriptor = None
    for klass in afpText::LLERG.__mro__:
        if "RGFunct" in klass.__dict__:
            descriptor = klass.__dict__["RGFunct"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ipo_is_not_abstract():
    assert not inspect.isabstract(afpText::IPO)


def test_afptext::ipo_constructor_exists():
    assert callable(afpText::IPO.__init__)


def test_afptext::ipo_constructor_args():
    sig = inspect.signature(afpText::IPO.__init__)
    params = list(sig.parameters.keys())
    assert "XolOset" in params, "Missing parameter 'XolOset'"
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"
    assert "OvlyOrent" in params, "Missing parameter 'OvlyOrent'"
    assert "YolOset" in params, "Missing parameter 'YolOset'"

def test_afptext::ipo_has_XolOset():
    assert hasattr(afpText::IPO, "XolOset")
    descriptor = None
    for klass in afpText::IPO.__mro__:
        if "XolOset" in klass.__dict__:
            descriptor = klass.__dict__["XolOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ipo_has_OvlyName():
    assert hasattr(afpText::IPO, "OvlyName")
    descriptor = None
    for klass in afpText::IPO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ipo_has_OvlyOrent():
    assert hasattr(afpText::IPO, "OvlyOrent")
    descriptor = None
    for klass in afpText::IPO.__mro__:
        if "OvlyOrent" in klass.__dict__:
            descriptor = klass.__dict__["OvlyOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ipo_has_YolOset():
    assert hasattr(afpText::IPO, "YolOset")
    descriptor = None
    for klass in afpText::IPO.__mro__:
        if "YolOset" in klass.__dict__:
            descriptor = klass.__dict__["YolOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ird_is_not_abstract():
    assert not inspect.isabstract(afpText::IRD)


def test_afptext::ird_constructor_exists():
    assert callable(afpText::IRD.__init__)


def test_afptext::ird_constructor_args():
    sig = inspect.signature(afpText::IRD.__init__)
    params = list(sig.parameters.keys())
    assert "IMdata" in params, "Missing parameter 'IMdata'"

def test_afptext::ird_has_IMdata():
    assert hasattr(afpText::IRD, "IMdata")
    descriptor = None
    for klass in afpText::IRD.__mro__:
        if "IMdata" in klass.__dict__:
            descriptor = klass.__dict__["IMdata"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ips_is_not_abstract():
    assert not inspect.isabstract(afpText::IPS)


def test_afptext::ips_constructor_exists():
    assert callable(afpText::IPS.__init__)


def test_afptext::ips_constructor_args():
    sig = inspect.signature(afpText::IPS.__init__)
    params = list(sig.parameters.keys())
    assert "YpsOset" in params, "Missing parameter 'YpsOset'"
    assert "XpsOset" in params, "Missing parameter 'XpsOset'"
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext::ips_has_YpsOset():
    assert hasattr(afpText::IPS, "YpsOset")
    descriptor = None
    for klass in afpText::IPS.__mro__:
        if "YpsOset" in klass.__dict__:
            descriptor = klass.__dict__["YpsOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ips_has_XpsOset():
    assert hasattr(afpText::IPS, "XpsOset")
    descriptor = None
    for klass in afpText::IPS.__mro__:
        if "XpsOset" in klass.__dict__:
            descriptor = klass.__dict__["XpsOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ips_has_PsegName():
    assert hasattr(afpText::IPS, "PsegName")
    descriptor = None
    for klass in afpText::IPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ipg_is_not_abstract():
    assert not inspect.isabstract(afpText::IPG)


def test_afptext::ipg_constructor_exists():
    assert callable(afpText::IPG.__init__)


def test_afptext::ipg_constructor_args():
    sig = inspect.signature(afpText::IPG.__init__)
    params = list(sig.parameters.keys())
    assert "IPgFlgs" in params, "Missing parameter 'IPgFlgs'"
    assert "PgName" in params, "Missing parameter 'PgName'"

def test_afptext::ipg_has_IPgFlgs():
    assert hasattr(afpText::IPG, "IPgFlgs")
    descriptor = None
    for klass in afpText::IPG.__mro__:
        if "IPgFlgs" in klass.__dict__:
            descriptor = klass.__dict__["IPgFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ipg_has_PgName():
    assert hasattr(afpText::IPG, "PgName")
    descriptor = None
    for klass in afpText::IPG.__mro__:
        if "PgName" in klass.__dict__:
            descriptor = klass.__dict__["PgName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ipd_is_not_abstract():
    assert not inspect.isabstract(afpText::IPD)


def test_afptext::ipd_constructor_exists():
    assert callable(afpText::IPD.__init__)


def test_afptext::ipd_constructor_args():
    sig = inspect.signature(afpText::IPD.__init__)
    params = list(sig.parameters.keys())
    assert "imageData" in params, "Missing parameter 'imageData'"
    assert "IOCAdat" in params, "Missing parameter 'IOCAdat'"

def test_afptext::ipd_has_imageData():
    assert hasattr(afpText::IPD, "imageData")
    descriptor = None
    for klass in afpText::IPD.__mro__:
        if "imageData" in klass.__dict__:
            descriptor = klass.__dict__["imageData"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ipd_has_IOCAdat():
    assert hasattr(afpText::IPD, "IOCAdat")
    descriptor = None
    for klass in afpText::IPD.__mro__:
        if "IOCAdat" in klass.__dict__:
            descriptor = klass.__dict__["IOCAdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext::icp_is_not_abstract():
    assert not inspect.isabstract(afpText::ICP)


def test_afptext::icp_constructor_exists():
    assert callable(afpText::ICP.__init__)


def test_afptext::icp_constructor_args():
    sig = inspect.signature(afpText::ICP.__init__)
    params = list(sig.parameters.keys())
    assert "XFilSize" in params, "Missing parameter 'XFilSize'"
    assert "YFilSize" in params, "Missing parameter 'YFilSize'"
    assert "YCSize" in params, "Missing parameter 'YCSize'"
    assert "XCOset" in params, "Missing parameter 'XCOset'"
    assert "XCSize" in params, "Missing parameter 'XCSize'"
    assert "YCOset" in params, "Missing parameter 'YCOset'"

def test_afptext::icp_has_XFilSize():
    assert hasattr(afpText::ICP, "XFilSize")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "XFilSize" in klass.__dict__:
            descriptor = klass.__dict__["XFilSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::icp_has_YFilSize():
    assert hasattr(afpText::ICP, "YFilSize")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "YFilSize" in klass.__dict__:
            descriptor = klass.__dict__["YFilSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::icp_has_YCSize():
    assert hasattr(afpText::ICP, "YCSize")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "YCSize" in klass.__dict__:
            descriptor = klass.__dict__["YCSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::icp_has_XCOset():
    assert hasattr(afpText::ICP, "XCOset")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "XCOset" in klass.__dict__:
            descriptor = klass.__dict__["XCOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::icp_has_XCSize():
    assert hasattr(afpText::ICP, "XCSize")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "XCSize" in klass.__dict__:
            descriptor = klass.__dict__["XCSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::icp_has_YCOset():
    assert hasattr(afpText::ICP, "YCOset")
    descriptor = None
    for klass in afpText::ICP.__mro__:
        if "YCOset" in klass.__dict__:
            descriptor = klass.__dict__["YCOset"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ioc_is_not_abstract():
    assert not inspect.isabstract(afpText::IOC)


def test_afptext::ioc_constructor_exists():
    assert callable(afpText::IOC.__init__)


def test_afptext::ioc_constructor_args():
    sig = inspect.signature(afpText::IOC.__init__)
    params = list(sig.parameters.keys())
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "ConData1" in params, "Missing parameter 'ConData1'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"
    assert "XMap" in params, "Missing parameter 'XMap'"
    assert "YMap" in params, "Missing parameter 'YMap'"
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "ConData2" in params, "Missing parameter 'ConData2'"

def test_afptext::ioc_has_YoaOrent():
    assert hasattr(afpText::IOC, "YoaOrent")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_XoaOset():
    assert hasattr(afpText::IOC, "XoaOset")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_ConData1():
    assert hasattr(afpText::IOC, "ConData1")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "ConData1" in klass.__dict__:
            descriptor = klass.__dict__["ConData1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_YoaOset():
    assert hasattr(afpText::IOC, "YoaOset")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_XMap():
    assert hasattr(afpText::IOC, "XMap")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "XMap" in klass.__dict__:
            descriptor = klass.__dict__["XMap"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_YMap():
    assert hasattr(afpText::IOC, "YMap")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "YMap" in klass.__dict__:
            descriptor = klass.__dict__["YMap"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_XoaOrent():
    assert hasattr(afpText::IOC, "XoaOrent")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::ioc_has_ConData2():
    assert hasattr(afpText::IOC, "ConData2")
    descriptor = None
    for klass in afpText::IOC.__mro__:
        if "ConData2" in klass.__dict__:
            descriptor = klass.__dict__["ConData2"]
            break
    assert isinstance(descriptor, property)



def test_afptext::iob_is_not_abstract():
    assert not inspect.isabstract(afpText::IOB)


def test_afptext::iob_constructor_exists():
    assert callable(afpText::IOB.__init__)


def test_afptext::iob_constructor_args():
    sig = inspect.signature(afpText::IOB.__init__)
    params = list(sig.parameters.keys())
    assert "ObjName" in params, "Missing parameter 'ObjName'"
    assert "YoaOset" in params, "Missing parameter 'YoaOset'"
    assert "XoaOset" in params, "Missing parameter 'XoaOset'"
    assert "XocaOset" in params, "Missing parameter 'XocaOset'"
    assert "ObjType" in params, "Missing parameter 'ObjType'"
    assert "YocaOset" in params, "Missing parameter 'YocaOset'"
    assert "RefCSys" in params, "Missing parameter 'RefCSys'"
    assert "XoaOrent" in params, "Missing parameter 'XoaOrent'"
    assert "YoaOrent" in params, "Missing parameter 'YoaOrent'"

def test_afptext::iob_has_ObjName():
    assert hasattr(afpText::IOB, "ObjName")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "ObjName" in klass.__dict__:
            descriptor = klass.__dict__["ObjName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_YoaOset():
    assert hasattr(afpText::IOB, "YoaOset")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "YoaOset" in klass.__dict__:
            descriptor = klass.__dict__["YoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_XoaOset():
    assert hasattr(afpText::IOB, "XoaOset")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "XoaOset" in klass.__dict__:
            descriptor = klass.__dict__["XoaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_XocaOset():
    assert hasattr(afpText::IOB, "XocaOset")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "XocaOset" in klass.__dict__:
            descriptor = klass.__dict__["XocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_ObjType():
    assert hasattr(afpText::IOB, "ObjType")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "ObjType" in klass.__dict__:
            descriptor = klass.__dict__["ObjType"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_YocaOset():
    assert hasattr(afpText::IOB, "YocaOset")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "YocaOset" in klass.__dict__:
            descriptor = klass.__dict__["YocaOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_RefCSys():
    assert hasattr(afpText::IOB, "RefCSys")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "RefCSys" in klass.__dict__:
            descriptor = klass.__dict__["RefCSys"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_XoaOrent():
    assert hasattr(afpText::IOB, "XoaOrent")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "XoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["XoaOrent"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iob_has_YoaOrent():
    assert hasattr(afpText::IOB, "YoaOrent")
    descriptor = None
    for klass in afpText::IOB.__mro__:
        if "YoaOrent" in klass.__dict__:
            descriptor = klass.__dict__["YoaOrent"]
            break
    assert isinstance(descriptor, property)



def test_afptext::imm_is_not_abstract():
    assert not inspect.isabstract(afpText::IMM)


def test_afptext::imm_constructor_exists():
    assert callable(afpText::IMM.__init__)


def test_afptext::imm_constructor_args():
    sig = inspect.signature(afpText::IMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMPName" in params, "Missing parameter 'MMPName'"

def test_afptext::imm_has_MMPName():
    assert hasattr(afpText::IMM, "MMPName")
    descriptor = None
    for klass in afpText::IMM.__mro__:
        if "MMPName" in klass.__dict__:
            descriptor = klass.__dict__["MMPName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::iid_is_not_abstract():
    assert not inspect.isabstract(afpText::IID)


def test_afptext::iid_constructor_exists():
    assert callable(afpText::IID.__init__)


def test_afptext::iid_constructor_args():
    sig = inspect.signature(afpText::IID.__init__)
    params = list(sig.parameters.keys())
    assert "YCSizeD" in params, "Missing parameter 'YCSizeD'"
    assert "ConData2" in params, "Missing parameter 'ConData2'"
    assert "XSize" in params, "Missing parameter 'XSize'"
    assert "XCSizeD" in params, "Missing parameter 'XCSizeD'"
    assert "YBase" in params, "Missing parameter 'YBase'"
    assert "YSize" in params, "Missing parameter 'YSize'"
    assert "ConData1" in params, "Missing parameter 'ConData1'"
    assert "YUnits" in params, "Missing parameter 'YUnits'"
    assert "XBase" in params, "Missing parameter 'XBase'"
    assert "XUnits" in params, "Missing parameter 'XUnits'"
    assert "ConData3" in params, "Missing parameter 'ConData3'"
    assert "Color" in params, "Missing parameter 'Color'"

def test_afptext::iid_has_YCSizeD():
    assert hasattr(afpText::IID, "YCSizeD")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "YCSizeD" in klass.__dict__:
            descriptor = klass.__dict__["YCSizeD"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_ConData2():
    assert hasattr(afpText::IID, "ConData2")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "ConData2" in klass.__dict__:
            descriptor = klass.__dict__["ConData2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_XSize():
    assert hasattr(afpText::IID, "XSize")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "XSize" in klass.__dict__:
            descriptor = klass.__dict__["XSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_XCSizeD():
    assert hasattr(afpText::IID, "XCSizeD")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "XCSizeD" in klass.__dict__:
            descriptor = klass.__dict__["XCSizeD"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_YBase():
    assert hasattr(afpText::IID, "YBase")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "YBase" in klass.__dict__:
            descriptor = klass.__dict__["YBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_YSize():
    assert hasattr(afpText::IID, "YSize")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "YSize" in klass.__dict__:
            descriptor = klass.__dict__["YSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_ConData1():
    assert hasattr(afpText::IID, "ConData1")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "ConData1" in klass.__dict__:
            descriptor = klass.__dict__["ConData1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_YUnits():
    assert hasattr(afpText::IID, "YUnits")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "YUnits" in klass.__dict__:
            descriptor = klass.__dict__["YUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_XBase():
    assert hasattr(afpText::IID, "XBase")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "XBase" in klass.__dict__:
            descriptor = klass.__dict__["XBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_XUnits():
    assert hasattr(afpText::IID, "XUnits")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "XUnits" in klass.__dict__:
            descriptor = klass.__dict__["XUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_ConData3():
    assert hasattr(afpText::IID, "ConData3")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "ConData3" in klass.__dict__:
            descriptor = klass.__dict__["ConData3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::iid_has_Color():
    assert hasattr(afpText::IID, "Color")
    descriptor = None
    for klass in afpText::IID.__mro__:
        if "Color" in klass.__dict__:
            descriptor = klass.__dict__["Color"]
            break
    assert isinstance(descriptor, property)



def test_afptext::iel_is_not_abstract():
    assert not inspect.isabstract(afpText::IEL)


def test_afptext::iel_constructor_exists():
    assert callable(afpText::IEL.__init__)


def test_afptext::iel_constructor_args():
    sig = inspect.signature(afpText::IEL.__init__)
    params = list(sig.parameters.keys())



def test_afptext::idd_is_not_abstract():
    assert not inspect.isabstract(afpText::IDD)


def test_afptext::idd_constructor_exists():
    assert callable(afpText::IDD.__init__)


def test_afptext::idd_constructor_args():
    sig = inspect.signature(afpText::IDD.__init__)
    params = list(sig.parameters.keys())
    assert "UNITBASE" in params, "Missing parameter 'UNITBASE'"
    assert "XRESOL" in params, "Missing parameter 'XRESOL'"
    assert "YRESOL" in params, "Missing parameter 'YRESOL'"
    assert "XSIZE" in params, "Missing parameter 'XSIZE'"
    assert "YSIZE" in params, "Missing parameter 'YSIZE'"

def test_afptext::idd_has_UNITBASE():
    assert hasattr(afpText::IDD, "UNITBASE")
    descriptor = None
    for klass in afpText::IDD.__mro__:
        if "UNITBASE" in klass.__dict__:
            descriptor = klass.__dict__["UNITBASE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idd_has_XRESOL():
    assert hasattr(afpText::IDD, "XRESOL")
    descriptor = None
    for klass in afpText::IDD.__mro__:
        if "XRESOL" in klass.__dict__:
            descriptor = klass.__dict__["XRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idd_has_YRESOL():
    assert hasattr(afpText::IDD, "YRESOL")
    descriptor = None
    for klass in afpText::IDD.__mro__:
        if "YRESOL" in klass.__dict__:
            descriptor = klass.__dict__["YRESOL"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idd_has_XSIZE():
    assert hasattr(afpText::IDD, "XSIZE")
    descriptor = None
    for klass in afpText::IDD.__mro__:
        if "XSIZE" in klass.__dict__:
            descriptor = klass.__dict__["XSIZE"]
            break
    assert isinstance(descriptor, property)

def test_afptext::idd_has_YSIZE():
    assert hasattr(afpText::IDD, "YSIZE")
    descriptor = None
    for klass in afpText::IDD.__mro__:
        if "YSIZE" in klass.__dict__:
            descriptor = klass.__dict__["YSIZE"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gdd_is_not_abstract():
    assert not inspect.isabstract(afpText::GDD)


def test_afptext::gdd_constructor_exists():
    assert callable(afpText::GDD.__init__)


def test_afptext::gdd_constructor_args():
    sig = inspect.signature(afpText::GDD.__init__)
    params = list(sig.parameters.keys())
    assert "GOCAdes" in params, "Missing parameter 'GOCAdes'"

def test_afptext::gdd_has_GOCAdes():
    assert hasattr(afpText::GDD, "GOCAdes")
    descriptor = None
    for klass in afpText::GDD.__mro__:
        if "GOCAdes" in klass.__dict__:
            descriptor = klass.__dict__["GOCAdes"]
            break
    assert isinstance(descriptor, property)



def test_afptext::gad_is_not_abstract():
    assert not inspect.isabstract(afpText::GAD)


def test_afptext::gad_constructor_exists():
    assert callable(afpText::GAD.__init__)


def test_afptext::gad_constructor_args():
    sig = inspect.signature(afpText::GAD.__init__)
    params = list(sig.parameters.keys())
    assert "GOCAdat" in params, "Missing parameter 'GOCAdat'"

def test_afptext::gad_has_GOCAdat():
    assert hasattr(afpText::GAD, "GOCAdat")
    descriptor = None
    for klass in afpText::GAD.__mro__:
        if "GOCAdat" in klass.__dict__:
            descriptor = klass.__dict__["GOCAdat"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnprg_is_not_abstract():
    assert not inspect.isabstract(afpText::FNPRG)


def test_afptext::fnprg_constructor_exists():
    assert callable(afpText::FNPRG.__init__)


def test_afptext::fnprg_constructor_args():
    sig = inspect.signature(afpText::FNPRG.__init__)
    params = list(sig.parameters.keys())
    assert "MaxDesDp" in params, "Missing parameter 'MaxDesDp'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "UscoreWdf" in params, "Missing parameter 'UscoreWdf'"
    assert "MaxAscHt" in params, "Missing parameter 'MaxAscHt'"
    assert "LcHeight" in params, "Missing parameter 'LcHeight'"
    assert "CapMHt" in params, "Missing parameter 'CapMHt'"
    assert "UscorePos" in params, "Missing parameter 'UscorePos'"
    assert "UscoreWd" in params, "Missing parameter 'UscoreWd'"
    assert "Retired" in params, "Missing parameter 'Retired'"
    assert "Reserved3" in params, "Missing parameter 'Reserved3'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::fnprg_has_MaxDesDp():
    assert hasattr(afpText::FNPRG, "MaxDesDp")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "MaxDesDp" in klass.__dict__:
            descriptor = klass.__dict__["MaxDesDp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_Reserved2():
    assert hasattr(afpText::FNPRG, "Reserved2")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_UscoreWdf():
    assert hasattr(afpText::FNPRG, "UscoreWdf")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "UscoreWdf" in klass.__dict__:
            descriptor = klass.__dict__["UscoreWdf"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_MaxAscHt():
    assert hasattr(afpText::FNPRG, "MaxAscHt")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "MaxAscHt" in klass.__dict__:
            descriptor = klass.__dict__["MaxAscHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_LcHeight():
    assert hasattr(afpText::FNPRG, "LcHeight")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "LcHeight" in klass.__dict__:
            descriptor = klass.__dict__["LcHeight"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_CapMHt():
    assert hasattr(afpText::FNPRG, "CapMHt")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "CapMHt" in klass.__dict__:
            descriptor = klass.__dict__["CapMHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_UscorePos():
    assert hasattr(afpText::FNPRG, "UscorePos")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "UscorePos" in klass.__dict__:
            descriptor = klass.__dict__["UscorePos"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_UscoreWd():
    assert hasattr(afpText::FNPRG, "UscoreWd")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "UscoreWd" in klass.__dict__:
            descriptor = klass.__dict__["UscoreWd"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_Retired():
    assert hasattr(afpText::FNPRG, "Retired")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "Retired" in klass.__dict__:
            descriptor = klass.__dict__["Retired"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_Reserved3():
    assert hasattr(afpText::FNPRG, "Reserved3")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "Reserved3" in klass.__dict__:
            descriptor = klass.__dict__["Reserved3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnprg_has_Reserved():
    assert hasattr(afpText::FNPRG, "Reserved")
    descriptor = None
    for klass in afpText::FNPRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnp_is_not_abstract():
    assert not inspect.isabstract(afpText::FNP)


def test_afptext::fnp_constructor_exists():
    assert callable(afpText::FNP.__init__)


def test_afptext::fnp_constructor_args():
    sig = inspect.signature(afpText::FNP.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fnorg_is_not_abstract():
    assert not inspect.isabstract(afpText::FNORG)


def test_afptext::fnorg_constructor_exists():
    assert callable(afpText::FNORG.__init__)


def test_afptext::fnorg_constructor_args():
    sig = inspect.signature(afpText::FNORG.__init__)
    params = list(sig.parameters.keys())
    assert "OrntFlgs" in params, "Missing parameter 'OrntFlgs'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "NomCharInc" in params, "Missing parameter 'NomCharInc'"
    assert "MaxCharInc" in params, "Missing parameter 'MaxCharInc'"
    assert "MaxBOset" in params, "Missing parameter 'MaxBOset'"
    assert "MaxBExt" in params, "Missing parameter 'MaxBExt'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "MinASp" in params, "Missing parameter 'MinASp'"
    assert "EmSpInc" in params, "Missing parameter 'EmSpInc'"
    assert "FigSpInc" in params, "Missing parameter 'FigSpInc'"
    assert "SpCharInc" in params, "Missing parameter 'SpCharInc'"
    assert "Reserved3" in params, "Missing parameter 'Reserved3'"
    assert "CharRot" in params, "Missing parameter 'CharRot'"
    assert "DefBInc" in params, "Missing parameter 'DefBInc'"

def test_afptext::fnorg_has_OrntFlgs():
    assert hasattr(afpText::FNORG, "OrntFlgs")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "OrntFlgs" in klass.__dict__:
            descriptor = klass.__dict__["OrntFlgs"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_Reserved2():
    assert hasattr(afpText::FNORG, "Reserved2")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_NomCharInc():
    assert hasattr(afpText::FNORG, "NomCharInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "NomCharInc" in klass.__dict__:
            descriptor = klass.__dict__["NomCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_MaxCharInc():
    assert hasattr(afpText::FNORG, "MaxCharInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "MaxCharInc" in klass.__dict__:
            descriptor = klass.__dict__["MaxCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_MaxBOset():
    assert hasattr(afpText::FNORG, "MaxBOset")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "MaxBOset" in klass.__dict__:
            descriptor = klass.__dict__["MaxBOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_MaxBExt():
    assert hasattr(afpText::FNORG, "MaxBExt")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "MaxBExt" in klass.__dict__:
            descriptor = klass.__dict__["MaxBExt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_Reserved():
    assert hasattr(afpText::FNORG, "Reserved")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_MinASp():
    assert hasattr(afpText::FNORG, "MinASp")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "MinASp" in klass.__dict__:
            descriptor = klass.__dict__["MinASp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_EmSpInc():
    assert hasattr(afpText::FNORG, "EmSpInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "EmSpInc" in klass.__dict__:
            descriptor = klass.__dict__["EmSpInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_FigSpInc():
    assert hasattr(afpText::FNORG, "FigSpInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "FigSpInc" in klass.__dict__:
            descriptor = klass.__dict__["FigSpInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_SpCharInc():
    assert hasattr(afpText::FNORG, "SpCharInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "SpCharInc" in klass.__dict__:
            descriptor = klass.__dict__["SpCharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_Reserved3():
    assert hasattr(afpText::FNORG, "Reserved3")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "Reserved3" in klass.__dict__:
            descriptor = klass.__dict__["Reserved3"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_CharRot():
    assert hasattr(afpText::FNORG, "CharRot")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "CharRot" in klass.__dict__:
            descriptor = klass.__dict__["CharRot"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnorg_has_DefBInc():
    assert hasattr(afpText::FNORG, "DefBInc")
    descriptor = None
    for klass in afpText::FNORG.__mro__:
        if "DefBInc" in klass.__dict__:
            descriptor = klass.__dict__["DefBInc"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fno_is_not_abstract():
    assert not inspect.isabstract(afpText::FNO)


def test_afptext::fno_constructor_exists():
    assert callable(afpText::FNO.__init__)


def test_afptext::fno_constructor_args():
    sig = inspect.signature(afpText::FNO.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fnmrg_is_not_abstract():
    assert not inspect.isabstract(afpText::FNMRG)


def test_afptext::fnmrg_constructor_exists():
    assert callable(afpText::FNMRG.__init__)


def test_afptext::fnmrg_constructor_args():
    sig = inspect.signature(afpText::FNMRG.__init__)
    params = list(sig.parameters.keys())
    assert "CharBoxWd" in params, "Missing parameter 'CharBoxWd'"
    assert "PatDOset" in params, "Missing parameter 'PatDOset'"
    assert "CharBoxHt" in params, "Missing parameter 'CharBoxHt'"

def test_afptext::fnmrg_has_CharBoxWd():
    assert hasattr(afpText::FNMRG, "CharBoxWd")
    descriptor = None
    for klass in afpText::FNMRG.__mro__:
        if "CharBoxWd" in klass.__dict__:
            descriptor = klass.__dict__["CharBoxWd"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnmrg_has_PatDOset():
    assert hasattr(afpText::FNMRG, "PatDOset")
    descriptor = None
    for klass in afpText::FNMRG.__mro__:
        if "PatDOset" in klass.__dict__:
            descriptor = klass.__dict__["PatDOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnmrg_has_CharBoxHt():
    assert hasattr(afpText::FNMRG, "CharBoxHt")
    descriptor = None
    for klass in afpText::FNMRG.__mro__:
        if "CharBoxHt" in klass.__dict__:
            descriptor = klass.__dict__["CharBoxHt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnm_is_not_abstract():
    assert not inspect.isabstract(afpText::FNM)


def test_afptext::fnm_constructor_exists():
    assert callable(afpText::FNM.__init__)


def test_afptext::fnm_constructor_args():
    sig = inspect.signature(afpText::FNM.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fnn_is_not_abstract():
    assert not inspect.isabstract(afpText::FNN)


def test_afptext::fnn_constructor_exists():
    assert callable(afpText::FNN.__init__)


def test_afptext::fnn_constructor_args():
    sig = inspect.signature(afpText::FNN.__init__)
    params = list(sig.parameters.keys())
    assert "FNNData" in params, "Missing parameter 'FNNData'"

def test_afptext::fnn_has_FNNData():
    assert hasattr(afpText::FNN, "FNNData")
    descriptor = None
    for klass in afpText::FNN.__mro__:
        if "FNNData" in klass.__dict__:
            descriptor = klass.__dict__["FNNData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnirg_is_not_abstract():
    assert not inspect.isabstract(afpText::FNIRG)


def test_afptext::fnirg_constructor_exists():
    assert callable(afpText::FNIRG.__init__)


def test_afptext::fnirg_constructor_args():
    sig = inspect.signature(afpText::FNIRG.__init__)
    params = list(sig.parameters.keys())
    assert "BSpace" in params, "Missing parameter 'BSpace'"
    assert "DescendDp" in params, "Missing parameter 'DescendDp'"
    assert "GCGID" in params, "Missing parameter 'GCGID'"
    assert "ASpace" in params, "Missing parameter 'ASpace'"
    assert "FNMCnt" in params, "Missing parameter 'FNMCnt'"
    assert "CharInc" in params, "Missing parameter 'CharInc'"
    assert "BaseOset" in params, "Missing parameter 'BaseOset'"
    assert "CSpace" in params, "Missing parameter 'CSpace'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "AscendHt" in params, "Missing parameter 'AscendHt'"

def test_afptext::fnirg_has_BSpace():
    assert hasattr(afpText::FNIRG, "BSpace")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "BSpace" in klass.__dict__:
            descriptor = klass.__dict__["BSpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_DescendDp():
    assert hasattr(afpText::FNIRG, "DescendDp")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "DescendDp" in klass.__dict__:
            descriptor = klass.__dict__["DescendDp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_GCGID():
    assert hasattr(afpText::FNIRG, "GCGID")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_ASpace():
    assert hasattr(afpText::FNIRG, "ASpace")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "ASpace" in klass.__dict__:
            descriptor = klass.__dict__["ASpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_FNMCnt():
    assert hasattr(afpText::FNIRG, "FNMCnt")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "FNMCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNMCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_CharInc():
    assert hasattr(afpText::FNIRG, "CharInc")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "CharInc" in klass.__dict__:
            descriptor = klass.__dict__["CharInc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_BaseOset():
    assert hasattr(afpText::FNIRG, "BaseOset")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "BaseOset" in klass.__dict__:
            descriptor = klass.__dict__["BaseOset"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_CSpace():
    assert hasattr(afpText::FNIRG, "CSpace")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "CSpace" in klass.__dict__:
            descriptor = klass.__dict__["CSpace"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_Reserved():
    assert hasattr(afpText::FNIRG, "Reserved")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_Reserved2():
    assert hasattr(afpText::FNIRG, "Reserved2")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnirg_has_AscendHt():
    assert hasattr(afpText::FNIRG, "AscendHt")
    descriptor = None
    for klass in afpText::FNIRG.__mro__:
        if "AscendHt" in klass.__dict__:
            descriptor = klass.__dict__["AscendHt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fni_is_not_abstract():
    assert not inspect.isabstract(afpText::FNI)


def test_afptext::fni_constructor_exists():
    assert callable(afpText::FNI.__init__)


def test_afptext::fni_constructor_args():
    sig = inspect.signature(afpText::FNI.__init__)
    params = list(sig.parameters.keys())



def test_afptext::fng_is_not_abstract():
    assert not inspect.isabstract(afpText::FNG)


def test_afptext::fng_constructor_exists():
    assert callable(afpText::FNG.__init__)


def test_afptext::fng_constructor_args():
    sig = inspect.signature(afpText::FNG.__init__)
    params = list(sig.parameters.keys())
    assert "PatData" in params, "Missing parameter 'PatData'"

def test_afptext::fng_has_PatData():
    assert hasattr(afpText::FNG, "PatData")
    descriptor = None
    for klass in afpText::FNG.__mro__:
        if "PatData" in klass.__dict__:
            descriptor = klass.__dict__["PatData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ept_is_not_abstract():
    assert not inspect.isabstract(afpText::EPT)


def test_afptext::ept_constructor_exists():
    assert callable(afpText::EPT.__init__)


def test_afptext::ept_constructor_args():
    sig = inspect.signature(afpText::EPT.__init__)
    params = list(sig.parameters.keys())
    assert "PTdoName" in params, "Missing parameter 'PTdoName'"

def test_afptext::ept_has_PTdoName():
    assert hasattr(afpText::EPT, "PTdoName")
    descriptor = None
    for klass in afpText::EPT.__mro__:
        if "PTdoName" in klass.__dict__:
            descriptor = klass.__dict__["PTdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnd_is_not_abstract():
    assert not inspect.isabstract(afpText::FND)


def test_afptext::fnd_constructor_exists():
    assert callable(afpText::FND.__init__)


def test_afptext::fnd_constructor_args():
    sig = inspect.signature(afpText::FND.__init__)
    params = list(sig.parameters.keys())
    assert "FtDsFlags" in params, "Missing parameter 'FtDsFlags'"
    assert "MinHSize" in params, "Missing parameter 'MinHSize'"
    assert "DsnSpcGrp" in params, "Missing parameter 'DsnSpcGrp'"
    assert "FtWdClass" in params, "Missing parameter 'FtWdClass'"
    assert "Reserved1" in params, "Missing parameter 'Reserved1'"
    assert "MaxHSize" in params, "Missing parameter 'MaxHSize'"
    assert "TypeFcDesc" in params, "Missing parameter 'TypeFcDesc'"
    assert "MaxPtSize" in params, "Missing parameter 'MaxPtSize'"
    assert "DsnGenCls" in params, "Missing parameter 'DsnGenCls'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "NomHSize" in params, "Missing parameter 'NomHSize'"
    assert "FGID" in params, "Missing parameter 'FGID'"
    assert "NomPtSize" in params, "Missing parameter 'NomPtSize'"
    assert "MinPtSize" in params, "Missing parameter 'MinPtSize'"
    assert "DsnSubCls" in params, "Missing parameter 'DsnSubCls'"
    assert "GCSID" in params, "Missing parameter 'GCSID'"
    assert "FtWtClass" in params, "Missing parameter 'FtWtClass'"

def test_afptext::fnd_has_FtDsFlags():
    assert hasattr(afpText::FND, "FtDsFlags")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "FtDsFlags" in klass.__dict__:
            descriptor = klass.__dict__["FtDsFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_MinHSize():
    assert hasattr(afpText::FND, "MinHSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "MinHSize" in klass.__dict__:
            descriptor = klass.__dict__["MinHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_DsnSpcGrp():
    assert hasattr(afpText::FND, "DsnSpcGrp")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "DsnSpcGrp" in klass.__dict__:
            descriptor = klass.__dict__["DsnSpcGrp"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_FtWdClass():
    assert hasattr(afpText::FND, "FtWdClass")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "FtWdClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWdClass"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_Reserved1():
    assert hasattr(afpText::FND, "Reserved1")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "Reserved1" in klass.__dict__:
            descriptor = klass.__dict__["Reserved1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_MaxHSize():
    assert hasattr(afpText::FND, "MaxHSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "MaxHSize" in klass.__dict__:
            descriptor = klass.__dict__["MaxHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_TypeFcDesc():
    assert hasattr(afpText::FND, "TypeFcDesc")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "TypeFcDesc" in klass.__dict__:
            descriptor = klass.__dict__["TypeFcDesc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_MaxPtSize():
    assert hasattr(afpText::FND, "MaxPtSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "MaxPtSize" in klass.__dict__:
            descriptor = klass.__dict__["MaxPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_DsnGenCls():
    assert hasattr(afpText::FND, "DsnGenCls")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "DsnGenCls" in klass.__dict__:
            descriptor = klass.__dict__["DsnGenCls"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_Reserved2():
    assert hasattr(afpText::FND, "Reserved2")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_NomHSize():
    assert hasattr(afpText::FND, "NomHSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "NomHSize" in klass.__dict__:
            descriptor = klass.__dict__["NomHSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_FGID():
    assert hasattr(afpText::FND, "FGID")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "FGID" in klass.__dict__:
            descriptor = klass.__dict__["FGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_NomPtSize():
    assert hasattr(afpText::FND, "NomPtSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "NomPtSize" in klass.__dict__:
            descriptor = klass.__dict__["NomPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_MinPtSize():
    assert hasattr(afpText::FND, "MinPtSize")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "MinPtSize" in klass.__dict__:
            descriptor = klass.__dict__["MinPtSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_DsnSubCls():
    assert hasattr(afpText::FND, "DsnSubCls")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "DsnSubCls" in klass.__dict__:
            descriptor = klass.__dict__["DsnSubCls"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_GCSID():
    assert hasattr(afpText::FND, "GCSID")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "GCSID" in klass.__dict__:
            descriptor = klass.__dict__["GCSID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnd_has_FtWtClass():
    assert hasattr(afpText::FND, "FtWtClass")
    descriptor = None
    for klass in afpText::FND.__mro__:
        if "FtWtClass" in klass.__dict__:
            descriptor = klass.__dict__["FtWtClass"]
            break
    assert isinstance(descriptor, property)



def test_afptext::fnc_is_not_abstract():
    assert not inspect.isabstract(afpText::FNC)


def test_afptext::fnc_constructor_exists():
    assert callable(afpText::FNC.__init__)


def test_afptext::fnc_constructor_args():
    sig = inspect.signature(afpText::FNC.__init__)
    params = list(sig.parameters.keys())
    assert "MaxBoxHt" in params, "Missing parameter 'MaxBoxHt'"
    assert "ResYUBase" in params, "Missing parameter 'ResYUBase'"
    assert "Reserved1" in params, "Missing parameter 'Reserved1'"
    assert "PatTech" in params, "Missing parameter 'PatTech'"
    assert "Reserved2" in params, "Missing parameter 'Reserved2'"
    assert "PatAlign" in params, "Missing parameter 'PatAlign'"
    assert "YUnitBase" in params, "Missing parameter 'YUnitBase'"
    assert "XUnitBase" in params, "Missing parameter 'XUnitBase'"
    assert "XftUnits" in params, "Missing parameter 'XftUnits'"
    assert "YfrUnits" in params, "Missing parameter 'YfrUnits'"
    assert "FNORGLen" in params, "Missing parameter 'FNORGLen'"
    assert "FNIRGLen" in params, "Missing parameter 'FNIRGLen'"
    assert "XfrUnits" in params, "Missing parameter 'XfrUnits'"
    assert "RPatDCnt" in params, "Missing parameter 'RPatDCnt'"
    assert "FNMRGLen" in params, "Missing parameter 'FNMRGLen'"
    assert "OPatDCnt" in params, "Missing parameter 'OPatDCnt'"
    assert "ResXUBase" in params, "Missing parameter 'ResXUBase'"
    assert "FNNRGLen" in params, "Missing parameter 'FNNRGLen'"
    assert "FNPRGLen" in params, "Missing parameter 'FNPRGLen'"
    assert "MaxBoxWd" in params, "Missing parameter 'MaxBoxWd'"
    assert "FNNDCnt" in params, "Missing parameter 'FNNDCnt'"
    assert "FntFlags" in params, "Missing parameter 'FntFlags'"
    assert "YftUnits" in params, "Missing parameter 'YftUnits'"
    assert "Retired" in params, "Missing parameter 'Retired'"
    assert "FNNMapCnt" in params, "Missing parameter 'FNNMapCnt'"

def test_afptext::fnc_has_MaxBoxHt():
    assert hasattr(afpText::FNC, "MaxBoxHt")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "MaxBoxHt" in klass.__dict__:
            descriptor = klass.__dict__["MaxBoxHt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_ResYUBase():
    assert hasattr(afpText::FNC, "ResYUBase")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "ResYUBase" in klass.__dict__:
            descriptor = klass.__dict__["ResYUBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_Reserved1():
    assert hasattr(afpText::FNC, "Reserved1")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "Reserved1" in klass.__dict__:
            descriptor = klass.__dict__["Reserved1"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_PatTech():
    assert hasattr(afpText::FNC, "PatTech")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "PatTech" in klass.__dict__:
            descriptor = klass.__dict__["PatTech"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_Reserved2():
    assert hasattr(afpText::FNC, "Reserved2")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "Reserved2" in klass.__dict__:
            descriptor = klass.__dict__["Reserved2"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_PatAlign():
    assert hasattr(afpText::FNC, "PatAlign")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "PatAlign" in klass.__dict__:
            descriptor = klass.__dict__["PatAlign"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_YUnitBase():
    assert hasattr(afpText::FNC, "YUnitBase")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "YUnitBase" in klass.__dict__:
            descriptor = klass.__dict__["YUnitBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_XUnitBase():
    assert hasattr(afpText::FNC, "XUnitBase")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "XUnitBase" in klass.__dict__:
            descriptor = klass.__dict__["XUnitBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_XftUnits():
    assert hasattr(afpText::FNC, "XftUnits")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "XftUnits" in klass.__dict__:
            descriptor = klass.__dict__["XftUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_YfrUnits():
    assert hasattr(afpText::FNC, "YfrUnits")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "YfrUnits" in klass.__dict__:
            descriptor = klass.__dict__["YfrUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNORGLen():
    assert hasattr(afpText::FNC, "FNORGLen")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNORGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNORGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNIRGLen():
    assert hasattr(afpText::FNC, "FNIRGLen")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_XfrUnits():
    assert hasattr(afpText::FNC, "XfrUnits")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "XfrUnits" in klass.__dict__:
            descriptor = klass.__dict__["XfrUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_RPatDCnt():
    assert hasattr(afpText::FNC, "RPatDCnt")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "RPatDCnt" in klass.__dict__:
            descriptor = klass.__dict__["RPatDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNMRGLen():
    assert hasattr(afpText::FNC, "FNMRGLen")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNMRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNMRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_OPatDCnt():
    assert hasattr(afpText::FNC, "OPatDCnt")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "OPatDCnt" in klass.__dict__:
            descriptor = klass.__dict__["OPatDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_ResXUBase():
    assert hasattr(afpText::FNC, "ResXUBase")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "ResXUBase" in klass.__dict__:
            descriptor = klass.__dict__["ResXUBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNNRGLen():
    assert hasattr(afpText::FNC, "FNNRGLen")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNNRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNNRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNPRGLen():
    assert hasattr(afpText::FNC, "FNPRGLen")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNPRGLen" in klass.__dict__:
            descriptor = klass.__dict__["FNPRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_MaxBoxWd():
    assert hasattr(afpText::FNC, "MaxBoxWd")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "MaxBoxWd" in klass.__dict__:
            descriptor = klass.__dict__["MaxBoxWd"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNNDCnt():
    assert hasattr(afpText::FNC, "FNNDCnt")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNNDCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNNDCnt"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FntFlags():
    assert hasattr(afpText::FNC, "FntFlags")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FntFlags" in klass.__dict__:
            descriptor = klass.__dict__["FntFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_YftUnits():
    assert hasattr(afpText::FNC, "YftUnits")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "YftUnits" in klass.__dict__:
            descriptor = klass.__dict__["YftUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_Retired():
    assert hasattr(afpText::FNC, "Retired")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "Retired" in klass.__dict__:
            descriptor = klass.__dict__["Retired"]
            break
    assert isinstance(descriptor, property)

def test_afptext::fnc_has_FNNMapCnt():
    assert hasattr(afpText::FNC, "FNNMapCnt")
    descriptor = None
    for klass in afpText::FNC.__mro__:
        if "FNNMapCnt" in klass.__dict__:
            descriptor = klass.__dict__["FNNMapCnt"]
            break
    assert isinstance(descriptor, property)



def test_afptext::esg_is_not_abstract():
    assert not inspect.isabstract(afpText::ESG)


def test_afptext::esg_constructor_exists():
    assert callable(afpText::ESG.__init__)


def test_afptext::esg_constructor_args():
    sig = inspect.signature(afpText::ESG.__init__)
    params = list(sig.parameters.keys())
    assert "REGName" in params, "Missing parameter 'REGName'"

def test_afptext::esg_has_REGName():
    assert hasattr(afpText::ESG, "REGName")
    descriptor = None
    for klass in afpText::ESG.__mro__:
        if "REGName" in klass.__dict__:
            descriptor = klass.__dict__["REGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ers_is_not_abstract():
    assert not inspect.isabstract(afpText::ERS)


def test_afptext::ers_constructor_exists():
    assert callable(afpText::ERS.__init__)


def test_afptext::ers_constructor_args():
    sig = inspect.signature(afpText::ERS.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::ers_has_RSName():
    assert hasattr(afpText::ERS, "RSName")
    descriptor = None
    for klass in afpText::ERS.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::erg_is_not_abstract():
    assert not inspect.isabstract(afpText::ERG)


def test_afptext::erg_constructor_exists():
    assert callable(afpText::ERG.__init__)


def test_afptext::erg_constructor_args():
    sig = inspect.signature(afpText::ERG.__init__)
    params = list(sig.parameters.keys())
    assert "RGrpName" in params, "Missing parameter 'RGrpName'"

def test_afptext::erg_has_RGrpName():
    assert hasattr(afpText::ERG, "RGrpName")
    descriptor = None
    for klass in afpText::ERG.__mro__:
        if "RGrpName" in klass.__dict__:
            descriptor = klass.__dict__["RGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eim_is_not_abstract():
    assert not inspect.isabstract(afpText::EIM)


def test_afptext::eim_constructor_exists():
    assert callable(afpText::EIM.__init__)


def test_afptext::eim_constructor_args():
    sig = inspect.signature(afpText::EIM.__init__)
    params = list(sig.parameters.keys())
    assert "IdoName" in params, "Missing parameter 'IdoName'"

def test_afptext::eim_has_IdoName():
    assert hasattr(afpText::EIM, "IdoName")
    descriptor = None
    for klass in afpText::EIM.__mro__:
        if "IdoName" in klass.__dict__:
            descriptor = klass.__dict__["IdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eps_is_not_abstract():
    assert not inspect.isabstract(afpText::EPS)


def test_afptext::eps_constructor_exists():
    assert callable(afpText::EPS.__init__)


def test_afptext::eps_constructor_args():
    sig = inspect.signature(afpText::EPS.__init__)
    params = list(sig.parameters.keys())
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext::eps_has_PsegName():
    assert hasattr(afpText::EPS, "PsegName")
    descriptor = None
    for klass in afpText::EPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::epm_is_not_abstract():
    assert not inspect.isabstract(afpText::EPM)


def test_afptext::epm_constructor_exists():
    assert callable(afpText::EPM.__init__)


def test_afptext::epm_constructor_args():
    sig = inspect.signature(afpText::EPM.__init__)
    params = list(sig.parameters.keys())
    assert "PMName" in params, "Missing parameter 'PMName'"

def test_afptext::epm_has_PMName():
    assert hasattr(afpText::EPM, "PMName")
    descriptor = None
    for klass in afpText::EPM.__mro__:
        if "PMName" in klass.__dict__:
            descriptor = klass.__dict__["PMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::epg_is_not_abstract():
    assert not inspect.isabstract(afpText::EPG)


def test_afptext::epg_constructor_exists():
    assert callable(afpText::EPG.__init__)


def test_afptext::epg_constructor_args():
    sig = inspect.signature(afpText::EPG.__init__)
    params = list(sig.parameters.keys())
    assert "PageName" in params, "Missing parameter 'PageName'"

def test_afptext::epg_has_PageName():
    assert hasattr(afpText::EPG, "PageName")
    descriptor = None
    for klass in afpText::EPG.__mro__:
        if "PageName" in klass.__dict__:
            descriptor = klass.__dict__["PageName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::epf_is_not_abstract():
    assert not inspect.isabstract(afpText::EPF)


def test_afptext::epf_constructor_exists():
    assert callable(afpText::EPF.__init__)


def test_afptext::epf_constructor_args():
    sig = inspect.signature(afpText::EPF.__init__)
    params = list(sig.parameters.keys())
    assert "PFName" in params, "Missing parameter 'PFName'"

def test_afptext::epf_has_PFName():
    assert hasattr(afpText::EPF, "PFName")
    descriptor = None
    for klass in afpText::EPF.__mro__:
        if "PFName" in klass.__dict__:
            descriptor = klass.__dict__["PFName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eog_is_not_abstract():
    assert not inspect.isabstract(afpText::EOG)


def test_afptext::eog_constructor_exists():
    assert callable(afpText::EOG.__init__)


def test_afptext::eog_constructor_args():
    sig = inspect.signature(afpText::EOG.__init__)
    params = list(sig.parameters.keys())
    assert "OEGName" in params, "Missing parameter 'OEGName'"

def test_afptext::eog_has_OEGName():
    assert hasattr(afpText::EOG, "OEGName")
    descriptor = None
    for klass in afpText::EOG.__mro__:
        if "OEGName" in klass.__dict__:
            descriptor = klass.__dict__["OEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eoc_is_not_abstract():
    assert not inspect.isabstract(afpText::EOC)


def test_afptext::eoc_constructor_exists():
    assert callable(afpText::EOC.__init__)


def test_afptext::eoc_constructor_args():
    sig = inspect.signature(afpText::EOC.__init__)
    params = list(sig.parameters.keys())
    assert "ObjCName" in params, "Missing parameter 'ObjCName'"

def test_afptext::eoc_has_ObjCName():
    assert hasattr(afpText::EOC, "ObjCName")
    descriptor = None
    for klass in afpText::EOC.__mro__:
        if "ObjCName" in klass.__dict__:
            descriptor = klass.__dict__["ObjCName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eng_is_not_abstract():
    assert not inspect.isabstract(afpText::ENG)


def test_afptext::eng_constructor_exists():
    assert callable(afpText::ENG.__init__)


def test_afptext::eng_constructor_args():
    sig = inspect.signature(afpText::ENG.__init__)
    params = list(sig.parameters.keys())
    assert "PGrpName" in params, "Missing parameter 'PGrpName'"

def test_afptext::eng_has_PGrpName():
    assert hasattr(afpText::ENG, "PGrpName")
    descriptor = None
    for klass in afpText::ENG.__mro__:
        if "PGrpName" in klass.__dict__:
            descriptor = klass.__dict__["PGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::emo_is_not_abstract():
    assert not inspect.isabstract(afpText::EMO)


def test_afptext::emo_constructor_exists():
    assert callable(afpText::EMO.__init__)


def test_afptext::emo_constructor_args():
    sig = inspect.signature(afpText::EMO.__init__)
    params = list(sig.parameters.keys())
    assert "OvlyName" in params, "Missing parameter 'OvlyName'"

def test_afptext::emo_has_OvlyName():
    assert hasattr(afpText::EMO, "OvlyName")
    descriptor = None
    for klass in afpText::EMO.__mro__:
        if "OvlyName" in klass.__dict__:
            descriptor = klass.__dict__["OvlyName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::emm_is_not_abstract():
    assert not inspect.isabstract(afpText::EMM)


def test_afptext::emm_constructor_exists():
    assert callable(afpText::EMM.__init__)


def test_afptext::emm_constructor_args():
    sig = inspect.signature(afpText::EMM.__init__)
    params = list(sig.parameters.keys())
    assert "MMName" in params, "Missing parameter 'MMName'"

def test_afptext::emm_has_MMName():
    assert hasattr(afpText::EMM, "MMName")
    descriptor = None
    for klass in afpText::EMM.__mro__:
        if "MMName" in klass.__dict__:
            descriptor = klass.__dict__["MMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eii_is_not_abstract():
    assert not inspect.isabstract(afpText::EII)


def test_afptext::eii_constructor_exists():
    assert callable(afpText::EII.__init__)


def test_afptext::eii_constructor_args():
    sig = inspect.signature(afpText::EII.__init__)
    params = list(sig.parameters.keys())
    assert "ImoName" in params, "Missing parameter 'ImoName'"

def test_afptext::eii_has_ImoName():
    assert hasattr(afpText::EII, "ImoName")
    descriptor = None
    for klass in afpText::EII.__mro__:
        if "ImoName" in klass.__dict__:
            descriptor = klass.__dict__["ImoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::egr_is_not_abstract():
    assert not inspect.isabstract(afpText::EGR)


def test_afptext::egr_constructor_exists():
    assert callable(afpText::EGR.__init__)


def test_afptext::egr_constructor_args():
    sig = inspect.signature(afpText::EGR.__init__)
    params = list(sig.parameters.keys())
    assert "GdoName" in params, "Missing parameter 'GdoName'"

def test_afptext::egr_has_GdoName():
    assert hasattr(afpText::EGR, "GdoName")
    descriptor = None
    for klass in afpText::EGR.__mro__:
        if "GdoName" in klass.__dict__:
            descriptor = klass.__dict__["GdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::efn_is_not_abstract():
    assert not inspect.isabstract(afpText::EFN)


def test_afptext::efn_constructor_exists():
    assert callable(afpText::EFN.__init__)


def test_afptext::efn_constructor_args():
    sig = inspect.signature(afpText::EFN.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::efn_has_RSName():
    assert hasattr(afpText::EFN, "RSName")
    descriptor = None
    for klass in afpText::EFN.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::efm_is_not_abstract():
    assert not inspect.isabstract(afpText::EFM)


def test_afptext::efm_constructor_exists():
    assert callable(afpText::EFM.__init__)


def test_afptext::efm_constructor_args():
    sig = inspect.signature(afpText::EFM.__init__)
    params = list(sig.parameters.keys())
    assert "FMName" in params, "Missing parameter 'FMName'"

def test_afptext::efm_has_FMName():
    assert hasattr(afpText::EFM, "FMName")
    descriptor = None
    for klass in afpText::EFM.__mro__:
        if "FMName" in klass.__dict__:
            descriptor = klass.__dict__["FMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::efg_is_not_abstract():
    assert not inspect.isabstract(afpText::EFG)


def test_afptext::efg_constructor_exists():
    assert callable(afpText::EFG.__init__)


def test_afptext::efg_constructor_args():
    sig = inspect.signature(afpText::EFG.__init__)
    params = list(sig.parameters.keys())
    assert "FEGName" in params, "Missing parameter 'FEGName'"

def test_afptext::efg_has_FEGName():
    assert hasattr(afpText::EFG, "FEGName")
    descriptor = None
    for klass in afpText::EFG.__mro__:
        if "FEGName" in klass.__dict__:
            descriptor = klass.__dict__["FEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::edx_is_not_abstract():
    assert not inspect.isabstract(afpText::EDX)


def test_afptext::edx_constructor_exists():
    assert callable(afpText::EDX.__init__)


def test_afptext::edx_constructor_args():
    sig = inspect.signature(afpText::EDX.__init__)
    params = list(sig.parameters.keys())
    assert "DMXName" in params, "Missing parameter 'DMXName'"

def test_afptext::edx_has_DMXName():
    assert hasattr(afpText::EDX, "DMXName")
    descriptor = None
    for klass in afpText::EDX.__mro__:
        if "DMXName" in klass.__dict__:
            descriptor = klass.__dict__["DMXName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::edt_is_not_abstract():
    assert not inspect.isabstract(afpText::EDT)


def test_afptext::edt_constructor_exists():
    assert callable(afpText::EDT.__init__)


def test_afptext::edt_constructor_args():
    sig = inspect.signature(afpText::EDT.__init__)
    params = list(sig.parameters.keys())
    assert "DocName" in params, "Missing parameter 'DocName'"

def test_afptext::edt_has_DocName():
    assert hasattr(afpText::EDT, "DocName")
    descriptor = None
    for klass in afpText::EDT.__mro__:
        if "DocName" in klass.__dict__:
            descriptor = klass.__dict__["DocName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::edm_is_not_abstract():
    assert not inspect.isabstract(afpText::EDM)


def test_afptext::edm_constructor_exists():
    assert callable(afpText::EDM.__init__)


def test_afptext::edm_constructor_args():
    sig = inspect.signature(afpText::EDM.__init__)
    params = list(sig.parameters.keys())
    assert "DMName" in params, "Missing parameter 'DMName'"

def test_afptext::edm_has_DMName():
    assert hasattr(afpText::EDM, "DMName")
    descriptor = None
    for klass in afpText::EDM.__mro__:
        if "DMName" in klass.__dict__:
            descriptor = klass.__dict__["DMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::edi_is_not_abstract():
    assert not inspect.isabstract(afpText::EDI)


def test_afptext::edi_constructor_exists():
    assert callable(afpText::EDI.__init__)


def test_afptext::edi_constructor_args():
    sig = inspect.signature(afpText::EDI.__init__)
    params = list(sig.parameters.keys())
    assert "IndxName" in params, "Missing parameter 'IndxName'"

def test_afptext::edi_has_IndxName():
    assert hasattr(afpText::EDI, "IndxName")
    descriptor = None
    for klass in afpText::EDI.__mro__:
        if "IndxName" in klass.__dict__:
            descriptor = klass.__dict__["IndxName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::edg_is_not_abstract():
    assert not inspect.isabstract(afpText::EDG)


def test_afptext::edg_constructor_exists():
    assert callable(afpText::EDG.__init__)


def test_afptext::edg_constructor_args():
    sig = inspect.signature(afpText::EDG.__init__)
    params = list(sig.parameters.keys())
    assert "DEGName" in params, "Missing parameter 'DEGName'"

def test_afptext::edg_has_DEGName():
    assert hasattr(afpText::EDG, "DEGName")
    descriptor = None
    for klass in afpText::EDG.__mro__:
        if "DEGName" in klass.__dict__:
            descriptor = klass.__dict__["DEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ecp_is_not_abstract():
    assert not inspect.isabstract(afpText::ECP)


def test_afptext::ecp_constructor_exists():
    assert callable(afpText::ECP.__init__)


def test_afptext::ecp_constructor_args():
    sig = inspect.signature(afpText::ECP.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::ecp_has_RSName():
    assert hasattr(afpText::ECP, "RSName")
    descriptor = None
    for klass in afpText::ECP.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ecf_is_not_abstract():
    assert not inspect.isabstract(afpText::ECF)


def test_afptext::ecf_constructor_exists():
    assert callable(afpText::ECF.__init__)


def test_afptext::ecf_constructor_args():
    sig = inspect.signature(afpText::ECF.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::ecf_has_RSName():
    assert hasattr(afpText::ECF, "RSName")
    descriptor = None
    for klass in afpText::ECF.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eca_is_not_abstract():
    assert not inspect.isabstract(afpText::ECA)


def test_afptext::eca_constructor_exists():
    assert callable(afpText::ECA.__init__)


def test_afptext::eca_constructor_args():
    sig = inspect.signature(afpText::ECA.__init__)
    params = list(sig.parameters.keys())
    assert "CATName" in params, "Missing parameter 'CATName'"

def test_afptext::eca_has_CATName():
    assert hasattr(afpText::ECA, "CATName")
    descriptor = None
    for klass in afpText::ECA.__mro__:
        if "CATName" in klass.__dict__:
            descriptor = klass.__dict__["CATName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ebc_is_not_abstract():
    assert not inspect.isabstract(afpText::EBC)


def test_afptext::ebc_constructor_exists():
    assert callable(afpText::EBC.__init__)


def test_afptext::ebc_constructor_args():
    sig = inspect.signature(afpText::EBC.__init__)
    params = list(sig.parameters.keys())
    assert "BCdoName" in params, "Missing parameter 'BCdoName'"

def test_afptext::ebc_has_BCdoName():
    assert hasattr(afpText::EBC, "BCdoName")
    descriptor = None
    for klass in afpText::EBC.__mro__:
        if "BCdoName" in klass.__dict__:
            descriptor = klass.__dict__["BCdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::eag_is_not_abstract():
    assert not inspect.isabstract(afpText::EAG)


def test_afptext::eag_constructor_exists():
    assert callable(afpText::EAG.__init__)


def test_afptext::eag_constructor_args():
    sig = inspect.signature(afpText::EAG.__init__)
    params = list(sig.parameters.keys())
    assert "AEGName" in params, "Missing parameter 'AEGName'"

def test_afptext::eag_has_AEGName():
    assert hasattr(afpText::EAG, "AEGName")
    descriptor = None
    for klass in afpText::EAG.__mro__:
        if "AEGName" in klass.__dict__:
            descriptor = klass.__dict__["AEGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::dxd_is_not_abstract():
    assert not inspect.isabstract(afpText::DXD)


def test_afptext::dxd_constructor_exists():
    assert callable(afpText::DXD.__init__)


def test_afptext::dxd_constructor_args():
    sig = inspect.signature(afpText::DXD.__init__)
    params = list(sig.parameters.keys())



def test_afptext::brg_is_not_abstract():
    assert not inspect.isabstract(afpText::BRG)


def test_afptext::brg_constructor_exists():
    assert callable(afpText::BRG.__init__)


def test_afptext::brg_constructor_args():
    sig = inspect.signature(afpText::BRG.__init__)
    params = list(sig.parameters.keys())
    assert "RGrpName" in params, "Missing parameter 'RGrpName'"

def test_afptext::brg_has_RGrpName():
    assert hasattr(afpText::BRG, "RGrpName")
    descriptor = None
    for klass in afpText::BRG.__mro__:
        if "RGrpName" in klass.__dict__:
            descriptor = klass.__dict__["RGrpName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::ctc_is_not_abstract():
    assert not inspect.isabstract(afpText::CTC)


def test_afptext::ctc_constructor_exists():
    assert callable(afpText::CTC.__init__)


def test_afptext::ctc_constructor_args():
    sig = inspect.signature(afpText::CTC.__init__)
    params = list(sig.parameters.keys())
    assert "ConData" in params, "Missing parameter 'ConData'"

def test_afptext::ctc_has_ConData():
    assert hasattr(afpText::CTC, "ConData")
    descriptor = None
    for klass in afpText::CTC.__mro__:
        if "ConData" in klass.__dict__:
            descriptor = klass.__dict__["ConData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cpirg_is_not_abstract():
    assert not inspect.isabstract(afpText::CPIRG)


def test_afptext::cpirg_constructor_exists():
    assert callable(afpText::CPIRG.__init__)


def test_afptext::cpirg_constructor_args():
    sig = inspect.signature(afpText::CPIRG.__init__)
    params = list(sig.parameters.keys())
    assert "Count" in params, "Missing parameter 'Count'"
    assert "CodePoint" in params, "Missing parameter 'CodePoint'"
    assert "PrtFlags" in params, "Missing parameter 'PrtFlags'"
    assert "GCGID" in params, "Missing parameter 'GCGID'"

def test_afptext::cpirg_has_Count():
    assert hasattr(afpText::CPIRG, "Count")
    descriptor = None
    for klass in afpText::CPIRG.__mro__:
        if "Count" in klass.__dict__:
            descriptor = klass.__dict__["Count"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpirg_has_CodePoint():
    assert hasattr(afpText::CPIRG, "CodePoint")
    descriptor = None
    for klass in afpText::CPIRG.__mro__:
        if "CodePoint" in klass.__dict__:
            descriptor = klass.__dict__["CodePoint"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpirg_has_PrtFlags():
    assert hasattr(afpText::CPIRG, "PrtFlags")
    descriptor = None
    for klass in afpText::CPIRG.__mro__:
        if "PrtFlags" in klass.__dict__:
            descriptor = klass.__dict__["PrtFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpirg_has_GCGID():
    assert hasattr(afpText::CPIRG, "GCGID")
    descriptor = None
    for klass in afpText::CPIRG.__mro__:
        if "GCGID" in klass.__dict__:
            descriptor = klass.__dict__["GCGID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cpi_is_not_abstract():
    assert not inspect.isabstract(afpText::CPI)


def test_afptext::cpi_constructor_exists():
    assert callable(afpText::CPI.__init__)


def test_afptext::cpi_constructor_args():
    sig = inspect.signature(afpText::CPI.__init__)
    params = list(sig.parameters.keys())



def test_afptext::cpd_is_not_abstract():
    assert not inspect.isabstract(afpText::CPD)


def test_afptext::cpd_constructor_exists():
    assert callable(afpText::CPD.__init__)


def test_afptext::cpd_constructor_args():
    sig = inspect.signature(afpText::CPD.__init__)
    params = list(sig.parameters.keys())
    assert "GCGIDLen" in params, "Missing parameter 'GCGIDLen'"
    assert "CPDesc" in params, "Missing parameter 'CPDesc'"
    assert "CPGID" in params, "Missing parameter 'CPGID'"
    assert "GCSGID" in params, "Missing parameter 'GCSGID'"
    assert "NumCdPts" in params, "Missing parameter 'NumCdPts'"
    assert "EncScheme" in params, "Missing parameter 'EncScheme'"

def test_afptext::cpd_has_GCGIDLen():
    assert hasattr(afpText::CPD, "GCGIDLen")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "GCGIDLen" in klass.__dict__:
            descriptor = klass.__dict__["GCGIDLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpd_has_CPDesc():
    assert hasattr(afpText::CPD, "CPDesc")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "CPDesc" in klass.__dict__:
            descriptor = klass.__dict__["CPDesc"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpd_has_CPGID():
    assert hasattr(afpText::CPD, "CPGID")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "CPGID" in klass.__dict__:
            descriptor = klass.__dict__["CPGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpd_has_GCSGID():
    assert hasattr(afpText::CPD, "GCSGID")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "GCSGID" in klass.__dict__:
            descriptor = klass.__dict__["GCSGID"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpd_has_NumCdPts():
    assert hasattr(afpText::CPD, "NumCdPts")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "NumCdPts" in klass.__dict__:
            descriptor = klass.__dict__["NumCdPts"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpd_has_EncScheme():
    assert hasattr(afpText::CPD, "EncScheme")
    descriptor = None
    for klass in afpText::CPD.__mro__:
        if "EncScheme" in klass.__dict__:
            descriptor = klass.__dict__["EncScheme"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cpc_is_not_abstract():
    assert not inspect.isabstract(afpText::CPC)


def test_afptext::cpc_constructor_exists():
    assert callable(afpText::CPC.__init__)


def test_afptext::cpc_constructor_args():
    sig = inspect.signature(afpText::CPC.__init__)
    params = list(sig.parameters.keys())
    assert "VSFlags" in params, "Missing parameter 'VSFlags'"
    assert "VSChar" in params, "Missing parameter 'VSChar'"
    assert "CPIRGLen" in params, "Missing parameter 'CPIRGLen'"
    assert "PrtFlags" in params, "Missing parameter 'PrtFlags'"
    assert "VSCharSN" in params, "Missing parameter 'VSCharSN'"
    assert "DefCharID" in params, "Missing parameter 'DefCharID'"

def test_afptext::cpc_has_VSFlags():
    assert hasattr(afpText::CPC, "VSFlags")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "VSFlags" in klass.__dict__:
            descriptor = klass.__dict__["VSFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpc_has_VSChar():
    assert hasattr(afpText::CPC, "VSChar")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "VSChar" in klass.__dict__:
            descriptor = klass.__dict__["VSChar"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpc_has_CPIRGLen():
    assert hasattr(afpText::CPC, "CPIRGLen")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "CPIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["CPIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpc_has_PrtFlags():
    assert hasattr(afpText::CPC, "PrtFlags")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "PrtFlags" in klass.__dict__:
            descriptor = klass.__dict__["PrtFlags"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpc_has_VSCharSN():
    assert hasattr(afpText::CPC, "VSCharSN")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "VSCharSN" in klass.__dict__:
            descriptor = klass.__dict__["VSCharSN"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cpc_has_DefCharID():
    assert hasattr(afpText::CPC, "DefCharID")
    descriptor = None
    for klass in afpText::CPC.__mro__:
        if "DefCharID" in klass.__dict__:
            descriptor = klass.__dict__["DefCharID"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cfirg_is_not_abstract():
    assert not inspect.isabstract(afpText::CFIRG)


def test_afptext::cfirg_constructor_exists():
    assert callable(afpText::CFIRG.__init__)


def test_afptext::cfirg_constructor_args():
    sig = inspect.signature(afpText::CFIRG.__init__)
    params = list(sig.parameters.keys())
    assert "SHScale" in params, "Missing parameter 'SHScale'"
    assert "SVSize" in params, "Missing parameter 'SVSize'"
    assert "FCSName" in params, "Missing parameter 'FCSName'"
    assert "CPName" in params, "Missing parameter 'CPName'"
    assert "Section" in params, "Missing parameter 'Section'"
    assert "Reserved" in params, "Missing parameter 'Reserved'"

def test_afptext::cfirg_has_SHScale():
    assert hasattr(afpText::CFIRG, "SHScale")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "SHScale" in klass.__dict__:
            descriptor = klass.__dict__["SHScale"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfirg_has_SVSize():
    assert hasattr(afpText::CFIRG, "SVSize")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "SVSize" in klass.__dict__:
            descriptor = klass.__dict__["SVSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfirg_has_FCSName():
    assert hasattr(afpText::CFIRG, "FCSName")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "FCSName" in klass.__dict__:
            descriptor = klass.__dict__["FCSName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfirg_has_CPName():
    assert hasattr(afpText::CFIRG, "CPName")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "CPName" in klass.__dict__:
            descriptor = klass.__dict__["CPName"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfirg_has_Section():
    assert hasattr(afpText::CFIRG, "Section")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "Section" in klass.__dict__:
            descriptor = klass.__dict__["Section"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfirg_has_Reserved():
    assert hasattr(afpText::CFIRG, "Reserved")
    descriptor = None
    for klass in afpText::CFIRG.__mro__:
        if "Reserved" in klass.__dict__:
            descriptor = klass.__dict__["Reserved"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cfi_is_not_abstract():
    assert not inspect.isabstract(afpText::CFI)


def test_afptext::cfi_constructor_exists():
    assert callable(afpText::CFI.__init__)


def test_afptext::cfi_constructor_args():
    sig = inspect.signature(afpText::CFI.__init__)
    params = list(sig.parameters.keys())



def test_afptext::cfc_is_not_abstract():
    assert not inspect.isabstract(afpText::CFC)


def test_afptext::cfc_constructor_exists():
    assert callable(afpText::CFC.__init__)


def test_afptext::cfc_constructor_args():
    sig = inspect.signature(afpText::CFC.__init__)
    params = list(sig.parameters.keys())
    assert "CFIRGLen" in params, "Missing parameter 'CFIRGLen'"
    assert "Retired1" in params, "Missing parameter 'Retired1'"

def test_afptext::cfc_has_CFIRGLen():
    assert hasattr(afpText::CFC, "CFIRGLen")
    descriptor = None
    for klass in afpText::CFC.__mro__:
        if "CFIRGLen" in klass.__dict__:
            descriptor = klass.__dict__["CFIRGLen"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cfc_has_Retired1():
    assert hasattr(afpText::CFC, "Retired1")
    descriptor = None
    for klass in afpText::CFC.__mro__:
        if "Retired1" in klass.__dict__:
            descriptor = klass.__dict__["Retired1"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cdd_is_not_abstract():
    assert not inspect.isabstract(afpText::CDD)


def test_afptext::cdd_constructor_exists():
    assert callable(afpText::CDD.__init__)


def test_afptext::cdd_constructor_args():
    sig = inspect.signature(afpText::CDD.__init__)
    params = list(sig.parameters.keys())
    assert "XocSize" in params, "Missing parameter 'XocSize'"
    assert "YocUnits" in params, "Missing parameter 'YocUnits'"
    assert "XocUnits" in params, "Missing parameter 'XocUnits'"
    assert "YocBase" in params, "Missing parameter 'YocBase'"
    assert "XocBase" in params, "Missing parameter 'XocBase'"
    assert "YocSize" in params, "Missing parameter 'YocSize'"

def test_afptext::cdd_has_XocSize():
    assert hasattr(afpText::CDD, "XocSize")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "XocSize" in klass.__dict__:
            descriptor = klass.__dict__["XocSize"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cdd_has_YocUnits():
    assert hasattr(afpText::CDD, "YocUnits")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "YocUnits" in klass.__dict__:
            descriptor = klass.__dict__["YocUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cdd_has_XocUnits():
    assert hasattr(afpText::CDD, "XocUnits")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "XocUnits" in klass.__dict__:
            descriptor = klass.__dict__["XocUnits"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cdd_has_YocBase():
    assert hasattr(afpText::CDD, "YocBase")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "YocBase" in klass.__dict__:
            descriptor = klass.__dict__["YocBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cdd_has_XocBase():
    assert hasattr(afpText::CDD, "XocBase")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "XocBase" in klass.__dict__:
            descriptor = klass.__dict__["XocBase"]
            break
    assert isinstance(descriptor, property)

def test_afptext::cdd_has_YocSize():
    assert hasattr(afpText::CDD, "YocSize")
    descriptor = None
    for klass in afpText::CDD.__mro__:
        if "YocSize" in klass.__dict__:
            descriptor = klass.__dict__["YocSize"]
            break
    assert isinstance(descriptor, property)



def test_afptext::cat_is_not_abstract():
    assert not inspect.isabstract(afpText::CAT)


def test_afptext::cat_constructor_exists():
    assert callable(afpText::CAT.__init__)


def test_afptext::cat_constructor_args():
    sig = inspect.signature(afpText::CAT.__init__)
    params = list(sig.parameters.keys())
    assert "CATData" in params, "Missing parameter 'CATData'"

def test_afptext::cat_has_CATData():
    assert hasattr(afpText::CAT, "CATData")
    descriptor = None
    for klass in afpText::CAT.__mro__:
        if "CATData" in klass.__dict__:
            descriptor = klass.__dict__["CATData"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bsg_is_not_abstract():
    assert not inspect.isabstract(afpText::BSG)


def test_afptext::bsg_constructor_exists():
    assert callable(afpText::BSG.__init__)


def test_afptext::bsg_constructor_args():
    sig = inspect.signature(afpText::BSG.__init__)
    params = list(sig.parameters.keys())
    assert "REGName" in params, "Missing parameter 'REGName'"

def test_afptext::bsg_has_REGName():
    assert hasattr(afpText::BSG, "REGName")
    descriptor = None
    for klass in afpText::BSG.__mro__:
        if "REGName" in klass.__dict__:
            descriptor = klass.__dict__["REGName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::brs_is_not_abstract():
    assert not inspect.isabstract(afpText::BRS)


def test_afptext::brs_constructor_exists():
    assert callable(afpText::BRS.__init__)


def test_afptext::brs_constructor_args():
    sig = inspect.signature(afpText::BRS.__init__)
    params = list(sig.parameters.keys())
    assert "RSName" in params, "Missing parameter 'RSName'"

def test_afptext::brs_has_RSName():
    assert hasattr(afpText::BRS, "RSName")
    descriptor = None
    for klass in afpText::BRS.__mro__:
        if "RSName" in klass.__dict__:
            descriptor = klass.__dict__["RSName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bpt_is_not_abstract():
    assert not inspect.isabstract(afpText::BPT)


def test_afptext::bpt_constructor_exists():
    assert callable(afpText::BPT.__init__)


def test_afptext::bpt_constructor_args():
    sig = inspect.signature(afpText::BPT.__init__)
    params = list(sig.parameters.keys())
    assert "PTdoName" in params, "Missing parameter 'PTdoName'"

def test_afptext::bpt_has_PTdoName():
    assert hasattr(afpText::BPT, "PTdoName")
    descriptor = None
    for klass in afpText::BPT.__mro__:
        if "PTdoName" in klass.__dict__:
            descriptor = klass.__dict__["PTdoName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bps_is_not_abstract():
    assert not inspect.isabstract(afpText::BPS)


def test_afptext::bps_constructor_exists():
    assert callable(afpText::BPS.__init__)


def test_afptext::bps_constructor_args():
    sig = inspect.signature(afpText::BPS.__init__)
    params = list(sig.parameters.keys())
    assert "PsegName" in params, "Missing parameter 'PsegName'"

def test_afptext::bps_has_PsegName():
    assert hasattr(afpText::BPS, "PsegName")
    descriptor = None
    for klass in afpText::BPS.__mro__:
        if "PsegName" in klass.__dict__:
            descriptor = klass.__dict__["PsegName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bpm_is_not_abstract():
    assert not inspect.isabstract(afpText::BPM)


def test_afptext::bpm_constructor_exists():
    assert callable(afpText::BPM.__init__)


def test_afptext::bpm_constructor_args():
    sig = inspect.signature(afpText::BPM.__init__)
    params = list(sig.parameters.keys())
    assert "PMName" in params, "Missing parameter 'PMName'"

def test_afptext::bpm_has_PMName():
    assert hasattr(afpText::BPM, "PMName")
    descriptor = None
    for klass in afpText::BPM.__mro__:
        if "PMName" in klass.__dict__:
            descriptor = klass.__dict__["PMName"]
            break
    assert isinstance(descriptor, property)



def test_afptext::bpg_is_not_abstract():
    assert not inspect.isabstract(afpText::BPG)


def test_afptext::bpg_constructor_exists():
    assert callable(afpText::BPG.__init__)


def test_afptext::bpg_constructor_args():
    sig = inspect.signature(afpText::BPG.__init__)
    params = list(sig.parameters.keys())
    assert "PageName" in params, "Missing parameter 'PageName'"

def test_afptext::bpg_has_PageName():
    assert hasattr(afpText::BPG, "PageName")
    descriptor = None
    for klass in afpText::BPG.__mro__:
        if "PageName" in klass.__dict__:
            descriptor = klass.__dict__["PageName"]
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
afpText::CGCSGID_strategy = st.builds(
    afpText::CGCSGID,
    GCSGID=
        safe_text,
    CPGID=
        safe_text
)
afpText::SetBiLevelImageColor_strategy = st.builds(
    afpText::SetBiLevelImageColor,
    NAMECOLR=
        safe_text,
    Reserved=
        safe_text,
    AREA=
        safe_text
)
afpText::GSPCOL_strategy = st.builds(
    afpText::GSPCOL,
    RES2=
        safe_text,
    RES1=
        safe_text,
    COLSPCE=
        safe_text,
    COLSIZE3=
        safe_text,
    COLSIZE4=
        safe_text,
    COLSIZE2=
        safe_text,
    COLVALUE=
        safe_text,
    COLSIZE1=
        safe_text
)
afpText::GBIMG_strategy = st.builds(
    afpText::GBIMG,
    YPOS=
        safe_text,
    FORMAT=
        safe_text,
    HEIGHT=
        safe_text,
    RES=
        safe_text,
    XPOS=
        safe_text,
    WIDTH=
        safe_text
)
afpText::BandImage_strategy = st.builds(
    afpText::BandImage,
    BCOUNT=
        safe_text
)
afpText::ObjectByteOffset_strategy = st.builds(
    afpText::ObjectByteOffset,
    DirByHi=
        safe_text,
    DirByOff=
        safe_text
)
afpText::GSMC_strategy = st.builds(
    afpText::GSMC,
    CELLWI=
        safe_text,
    CELLHI=
        safe_text
)
afpText::AttributeQualifier_strategy = st.builds(
    afpText::AttributeQualifier,
    SeqNum=
        safe_text,
    LevNum=
        safe_text
)
afpText::ObjectStructuredFieldOffset_strategy = st.builds(
    afpText::ObjectStructuredFieldOffset,
    SFOffHi=
        safe_text,
    SFOff=
        safe_text
)
afpText::ObjectCount_strategy = st.builds(
    afpText::ObjectCount,
    SubObj=
        safe_text,
    SObjNum=
        safe_text,
    SobjNmHi=
        safe_text
)
afpText::GSMX_strategy = st.builds(
    afpText::GSMX,
    MODE=
        safe_text
)
afpText::EndImage_strategy = st.builds(
    afpText::EndImage,
)
afpText::FontResolution_strategy = st.builds(
    afpText::FontResolution,
    RPuBase=
        safe_text,
    MetTech=
        safe_text,
    RPUnits=
        safe_text
)
afpText::EndTile_strategy = st.builds(
    afpText::EndTile,
)
afpText::GSGCH_strategy = st.builds(
    afpText::GSGCH,
)
afpText::ColorFidelity_strategy = st.builds(
    afpText::ColorFidelity,
    StpCoEx=
        safe_text,
    ColSub=
        safe_text,
    RepCoEx=
        safe_text
)
afpText::IDESize_strategy = st.builds(
    afpText::IDESize,
    IDESZ=
        safe_text
)
afpText::EncodingSchemeID_strategy = st.builds(
    afpText::EncodingSchemeID,
    ESidCP=
        safe_text,
    ESidUD=
        safe_text
)
afpText::GSAP_strategy = st.builds(
    afpText::GSAP,
    Q=
        safe_text,
    S=
        safe_text,
    R=
        safe_text,
    P=
        safe_text
)
afpText::GCCBEZ_strategy = st.builds(
    afpText::GCCBEZ,
)
afpText::GSECOL_strategy = st.builds(
    afpText::GSECOL,
    COLOR=
        safe_text
)
afpText::GSCS_strategy = st.builds(
    afpText::GSCS,
    LCID=
        safe_text
)
afpText::MediaEjectControl_strategy = st.builds(
    afpText::MediaEjectControl,
    EjCtrl=
        safe_text,
    Reserved=
        safe_text
)
afpText::BeginTransparencyMask_strategy = st.builds(
    afpText::BeginTransparencyMask,
)
afpText::GSMS_strategy = st.builds(
    afpText::GSMS,
    LCID=
        safe_text
)
afpText::GEPROL_strategy = st.builds(
    afpText::GEPROL,
    RES=
        safe_text
)
afpText::ObjectFunctionSetSpecification_strategy = st.builds(
    afpText::ObjectFunctionSetSpecification,
    OCAFnSet=
        safe_text,
    ObjType=
        safe_text,
    DCAFnSet=
        safe_text,
    ArchVrsn=
        safe_text
)
afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy = st.builds(
    afpText::FontCodedGraphicCharacterSetGlobalIdentifier,
    GCSGID=
        safe_text,
    CPGID=
        safe_text
)
afpText::GCHST_strategy = st.builds(
    afpText::GCHST,
    YPOS=
        safe_text,
    XPOS=
        safe_text,
    CP=
        safe_text
)
afpText::PagePositionInformation_strategy = st.builds(
    afpText::PagePositionInformation,
    PGPRG=
        safe_text
)
afpText::ColorSpecification_strategy = st.builds(
    afpText::ColorSpecification,
    ColSize1=
        safe_text,
    ColSize2=
        safe_text,
    Color=
        safe_text,
    ColSize4=
        safe_text,
    ColSpce=
        safe_text,
    ColSize3=
        safe_text
)
afpText::TBM_strategy = st.builds(
    afpText::TBM,
    INCRMENT=
        safe_text,
    PRECSION=
        safe_text,
    DIRCTION=
        safe_text
)
afpText::GIMD_strategy = st.builds(
    afpText::GIMD,
    DATA=
        safe_text
)
afpText::GSMP_strategy = st.builds(
    afpText::GSMP,
    PREC=
        safe_text
)
afpText::GCBEZ_strategy = st.builds(
    afpText::GCBEZ,
)
afpText::MetricAdjustment_strategy = st.builds(
    afpText::MetricAdjustment,
    VUniformIncrement=
        safe_text,
    VBaselineIncrement=
        safe_text,
    HUniformIncrement=
        safe_text,
    HBaselineIncrement=
        safe_text,
    XUPUB=
        safe_text,
    UnitBase=
        safe_text,
    YUPUB=
        safe_text
)
afpText::ObjectContainerPresentationSpaceSize_strategy = st.builds(
    afpText::ObjectContainerPresentationSpaceSize,
    PDFSize=
        safe_text
)
afpText::ResourceLocalIdentifier_strategy = st.builds(
    afpText::ResourceLocalIdentifier,
    ResLID=
        safe_text,
    ResType=
        safe_text
)
afpText::PresentationControl_strategy = st.builds(
    afpText::PresentationControl,
    PRSFlg=
        safe_text
)
afpText::ExtendedResourceLocalIdentifier_strategy = st.builds(
    afpText::ExtendedResourceLocalIdentifier,
    ResLID=
        safe_text,
    ResType=
        safe_text
)
afpText::ColorManagementResourceDescriptor_strategy = st.builds(
    afpText::ColorManagementResourceDescriptor,
    ProcMode=
        safe_text,
    CMRScpe=
        safe_text
)
afpText::GCCHST_strategy = st.builds(
    afpText::GCCHST,
    CP=
        safe_text
)
afpText::LineDataObjectPositionMigration_strategy = st.builds(
    afpText::LineDataObjectPositionMigration,
    TempOrient=
        safe_text
)
afpText::GSCP_strategy = st.builds(
    afpText::GSCP,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText::GCOMT_strategy = st.builds(
    afpText::GCOMT,
    DATA=
        safe_text
)
afpText::GBAR_strategy = st.builds(
    afpText::GBAR,
    FLAGS=
        safe_text
)
afpText::FNNRG2_strategy = st.builds(
    afpText::FNNRG2,
    TSID=
        safe_text,
    TSIDLen=
        safe_text
)
afpText::BLN_strategy = st.builds(
    afpText::BLN,
)
afpText::GSFLW_strategy = st.builds(
    afpText::GSFLW,
    MH=
        safe_text,
    MFR=
        safe_text
)
afpText::GSLT_strategy = st.builds(
    afpText::GSLT,
    LINETYPE=
        safe_text
)
afpText::ObjectByteExtent_strategy = st.builds(
    afpText::ObjectByteExtent,
    ByteExt=
        safe_text,
    ByteExtHi=
        safe_text
)
afpText::GSBMX_strategy = st.builds(
    afpText::GSBMX,
    MODE=
        safe_text
)
afpText::USC_strategy = st.builds(
    afpText::USC,
    BYPSIDEN=
        safe_text
)
afpText::FinishingFidelity_strategy = st.builds(
    afpText::FinishingFidelity,
    RepFinEx=
        safe_text,
    StpFinEx=
        safe_text
)
afpText::ObjectClassification_strategy = st.builds(
    afpText::ObjectClassification,
    CompName=
        safe_text,
    StrucFlgs=
        safe_text,
    ObjTpName=
        safe_text,
    ObjClass=
        safe_text,
    RegObjId=
        safe_text,
    ObjLev=
        safe_text
)
afpText::IOCAFunctionSetIdentification_strategy = st.builds(
    afpText::IOCAFunctionSetIdentification,
    CATEGORY=
        safe_text,
    FCNSET=
        safe_text
)
afpText::BandImageData_strategy = st.builds(
    afpText::BandImageData,
    RESERVED=
        safe_text,
    BANDNUM=
        safe_text,
    DATA=
        safe_text
)
afpText::FontFidelity_strategy = st.builds(
    afpText::FontFidelity,
    StpFntEx=
        safe_text
)
afpText::BSU_strategy = st.builds(
    afpText::BSU,
    LID=
        safe_text
)
afpText::TileSize_strategy = st.builds(
    afpText::TileSize,
    TVSIZE=
        safe_text,
    THSIZE=
        safe_text,
    RELRES=
        safe_text
)
afpText::DrawingOrderSubset_strategy = st.builds(
    afpText::DrawingOrderSubset,
)
afpText::WindowSpecification_strategy = st.builds(
    afpText::WindowSpecification,
    YTWIND=
        safe_text,
    FLAGS=
        safe_text,
    RES3=
        safe_text,
    XRESOL=
        safe_text,
    IMGXYRES=
        safe_text,
    XLWIND=
        safe_text,
    UBASE=
        safe_text,
    YBWIND=
        safe_text,
    XRWIND=
        safe_text,
    CFORMAT=
        safe_text,
    YRESOL=
        safe_text
)
afpText::TilePosition_strategy = st.builds(
    afpText::TilePosition,
    XOFFSET=
        safe_text,
    YOFFSET=
        safe_text
)
afpText::GCLINE_strategy = st.builds(
    afpText::GCLINE,
)
afpText::GSPT_strategy = st.builds(
    afpText::GSPT,
    PATT=
        safe_text
)
afpText::FontDescriptorSpecification_strategy = st.builds(
    afpText::FontDescriptorSpecification,
    FtWidth=
        safe_text,
    FtHeight=
        safe_text,
    FtUsFlags=
        safe_text,
    FtDsFlags=
        safe_text,
    FtWdClass=
        safe_text,
    FtWtClass=
        safe_text
)
afpText::BeginSegmentCommand_strategy = st.builds(
    afpText::BeginSegmentCommand,
    FLAG2=
        safe_text,
    PSNAME=
        safe_text,
    FLAG1=
        safe_text,
    NAME=
        safe_text,
    LENGTH=
        safe_text,
    SEGL=
        safe_text
)
afpText::DeviceAppearance_strategy = st.builds(
    afpText::DeviceAppearance,
    Reserved=
        safe_text,
    DevApp=
        safe_text
)
afpText::IncludeTile_strategy = st.builds(
    afpText::IncludeTile,
    TIRID=
        safe_text
)
afpText::TextFidelity_strategy = st.builds(
    afpText::TextFidelity,
    StpTxtEx=
        safe_text,
    RepTxtEx=
        safe_text
)
afpText::CRCResourceManagement_strategy = st.builds(
    afpText::CRCResourceManagement,
    ResClassFlg=
        safe_text,
    FmtQual=
        safe_text,
    RMValue=
        safe_text
)
afpText::PageOverlayConditionalProcessing_strategy = st.builds(
    afpText::PageOverlayConditionalProcessing,
    PgOvType=
        safe_text,
    Level=
        safe_text
)
afpText::GPARC_strategy = st.builds(
    afpText::GPARC,
    SWEEP=
        safe_text,
    START=
        safe_text,
    XCENT=
        safe_text,
    MFR=
        safe_text,
    YCENT=
        safe_text,
    YPOS=
        safe_text,
    XPOS=
        safe_text,
    MH=
        safe_text
)
afpText::ImageSubsampling_strategy = st.builds(
    afpText::ImageSubsampling,
)
afpText::TileSetColor_strategy = st.builds(
    afpText::TileSetColor,
    RESERVED=
        safe_text,
    SIZE3=
        safe_text,
    CVAL2=
        safe_text,
    SIZE4=
        safe_text,
    CVAL3=
        safe_text,
    SIZE1=
        safe_text,
    CVAL4=
        safe_text,
    CSPACE=
        safe_text,
    CVAL1=
        safe_text,
    SIZE2=
        safe_text
)
afpText::GSMT_strategy = st.builds(
    afpText::GSMT,
    MCPT=
        safe_text
)
afpText::FontHorizontalScaleFactor_strategy = st.builds(
    afpText::FontHorizontalScaleFactor,
    Hscale=
        safe_text
)
afpText::GCRLINE_strategy = st.builds(
    afpText::GCRLINE,
)
afpText::CMRFidelity_strategy = st.builds(
    afpText::CMRFidelity,
    RepCMREx=
        safe_text,
    StpCMREx=
        safe_text
)
afpText::GCMRK_strategy = st.builds(
    afpText::GCMRK,
)
afpText::ExtensionFont_strategy = st.builds(
    afpText::ExtensionFont,
    GCSGID=
        safe_text
)
afpText::EndTransparencyMask_strategy = st.builds(
    afpText::EndTransparencyMask,
)
afpText::MediumOrientation_strategy = st.builds(
    afpText::MediumOrientation,
    MedOrient=
        safe_text
)
afpText::GMRK_strategy = st.builds(
    afpText::GMRK,
)
afpText::ImageResolution_strategy = st.builds(
    afpText::ImageResolution,
    XBase=
        safe_text,
    YBase=
        safe_text,
    XResol=
        safe_text,
    YResol=
        safe_text
)
afpText::EndSegment_strategy = st.builds(
    afpText::EndSegment,
)
afpText::MediumMapPageNumber_strategy = st.builds(
    afpText::MediumMapPageNumber,
    PageNum=
        safe_text
)
afpText::GCFLT_strategy = st.builds(
    afpText::GCFLT,
)
afpText::SamplingRatios_strategy = st.builds(
    afpText::SamplingRatios,
)
afpText::GSCR_strategy = st.builds(
    afpText::GSCR,
    PREC=
        safe_text
)
afpText::GSCC_strategy = st.builds(
    afpText::GSCC,
    CELLHFR=
        safe_text,
    CELLWI=
        safe_text,
    CELLWFR=
        safe_text,
    CELLHI=
        safe_text
)
afpText::MappingOption_strategy = st.builds(
    afpText::MappingOption,
    MapValue=
        safe_text
)
afpText::LocalDateAndTimeStamp_strategy = st.builds(
    afpText::LocalDateAndTimeStamp,
    Hour=
        safe_text,
    Minute=
        safe_text,
    HundSec=
        safe_text,
    Day=
        safe_text,
    THunYear=
        safe_text,
    StampType=
        safe_text,
    TenYear=
        safe_text,
    Second=
        safe_text
)
afpText::GSCA_strategy = st.builds(
    afpText::GSCA,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText::ObjectOffset_strategy = st.builds(
    afpText::ObjectOffset,
    ObjOset=
        safe_text,
    ObjTpe=
        safe_text,
    ObjOstHi=
        safe_text
)
afpText::FullyQualifiedName_strategy = st.builds(
    afpText::FullyQualifiedName,
    FQNFormat=
        safe_text,
    FQNType=
        safe_text,
    FQName=
        safe_text
)
afpText::ImageData_strategy = st.builds(
    afpText::ImageData,
    DATA=
        safe_text
)
afpText::ObjectOriginIdentifier_strategy = st.builds(
    afpText::ObjectOriginIdentifier,
    MedID=
        safe_text,
    System=
        safe_text,
    DSID=
        safe_text,
    SysID=
        safe_text
)
afpText::GSLJ_strategy = st.builds(
    afpText::GSLJ,
    LINEJOIN=
        safe_text
)
afpText::GFLT_strategy = st.builds(
    afpText::GFLT,
)
afpText::GSLE_strategy = st.builds(
    afpText::GSLE,
    LINEEND=
        safe_text
)
afpText::GFARC_strategy = st.builds(
    afpText::GFARC,
    MH=
        safe_text,
    YPOS=
        safe_text,
    XPOS=
        safe_text,
    MFR=
        safe_text
)
afpText::ImageLUTID_strategy = st.builds(
    afpText::ImageLUTID,
    LUTID=
        safe_text
)
afpText::GEIMG_strategy = st.builds(
    afpText::GEIMG,
    DATA=
        safe_text
)
afpText::MediaFidelity_strategy = st.builds(
    afpText::MediaFidelity,
    Reserved=
        safe_text,
    StpMedEx=
        safe_text
)
afpText::MODCAInterchangeSet_strategy = st.builds(
    afpText::MODCAInterchangeSet,
    ISid=
        safe_text,
    IStype=
        safe_text
)
afpText::GRLINE_strategy = st.builds(
    afpText::GRLINE,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::EndSegmentCommand_strategy = st.builds(
    afpText::EndSegmentCommand,
)
afpText::GCBOX_strategy = st.builds(
    afpText::GCBOX,
    HAXIS=
        safe_text,
    XPOS1=
        safe_text,
    VAXIS=
        safe_text,
    RES=
        safe_text,
    YPOS1=
        safe_text
)
afpText::ObjectStructuredFieldExtent_strategy = st.builds(
    afpText::ObjectStructuredFieldExtent,
    SFExtHi=
        safe_text,
    SFExt=
        safe_text
)
afpText::BeginTile_strategy = st.builds(
    afpText::BeginTile,
)
afpText::GCPARC_strategy = st.builds(
    afpText::GCPARC,
    XCENT=
        safe_text,
    SWEEP=
        safe_text,
    YCENT=
        safe_text,
    START=
        safe_text,
    MFR=
        safe_text,
    MH=
        safe_text
)
afpText::GNOP1_strategy = st.builds(
    afpText::GNOP1,
)
afpText::LocaleSelector_strategy = st.builds(
    afpText::LocaleSelector,
    LangCode=
        safe_text,
    Reserved=
        safe_text,
    RegCde=
        safe_text,
    ScrptCde=
        safe_text,
    LocFlgs=
        safe_text,
    VarCde=
        safe_text
)
afpText::RenderingIntent_strategy = st.builds(
    afpText::RenderingIntent,
    IOCARI=
        safe_text,
    OCRI=
        safe_text,
    PTOCRI=
        safe_text,
    Reserved=
        safe_text,
    Reserved2=
        safe_text,
    GOCARI=
        safe_text
)
afpText::PresentationSpaceResetMixing_strategy = st.builds(
    afpText::PresentationSpaceResetMixing,
    BgMxFlag=
        safe_text
)
afpText::UP3iFinishingOperation_strategy = st.builds(
    afpText::UP3iFinishingOperation,
    Seqnum=
        safe_text,
    UP3iDat=
        safe_text
)
afpText::GEAR_strategy = st.builds(
    afpText::GEAR,
    DATA=
        safe_text
)
afpText::ResourceUsageAttribute_strategy = st.builds(
    afpText::ResourceUsageAttribute,
    Frequency=
        safe_text
)
afpText::GCFARC_strategy = st.builds(
    afpText::GCFARC,
    MFR=
        safe_text,
    MH=
        safe_text
)
afpText::ImageSize_strategy = st.builds(
    afpText::ImageSize,
    UNITBASE=
        safe_text,
    HSIZE=
        safe_text,
    VRESOL=
        safe_text,
    VSIZE=
        safe_text,
    HRESOL=
        safe_text
)
afpText::PresentationSpaceMixingRules_strategy = st.builds(
    afpText::PresentationSpaceMixingRules,
)
afpText::ResourceObjectInclude_strategy = st.builds(
    afpText::ResourceObjectInclude,
    ObjType=
        safe_text,
    YobjOset=
        safe_text,
    ObOrent=
        safe_text,
    ObjName=
        safe_text,
    XobjOset=
        safe_text
)
afpText::IDEStructure_strategy = st.builds(
    afpText::IDEStructure,
    SIZE2=
        safe_text,
    FLAGS=
        safe_text,
    FORMAT=
        safe_text,
    SIZE1=
        safe_text,
    SIZE4=
        safe_text,
    SIZE3=
        safe_text
)
afpText::TextOrientation_strategy = st.builds(
    afpText::TextOrientation,
    IAxis=
        safe_text,
    BAxis=
        safe_text
)
afpText::GLINE_strategy = st.builds(
    afpText::GLINE,
)
afpText::GSLW_strategy = st.builds(
    afpText::GSLW,
    MH=
        safe_text
)
afpText::GSCD_strategy = st.builds(
    afpText::GSCD,
    DIRECTION=
        safe_text
)
afpText::ObjectAreaSize_strategy = st.builds(
    afpText::ObjectAreaSize,
    XoaSize=
        safe_text,
    YoaSize=
        safe_text,
    SizeType=
        safe_text
)
afpText::GSCOL_strategy = st.builds(
    afpText::GSCOL,
    COL=
        safe_text
)
afpText::GBOX_strategy = st.builds(
    afpText::GBOX,
    XPOS0=
        safe_text,
    VAXIS=
        safe_text,
    YPOS1=
        safe_text,
    HAXIS=
        safe_text,
    XPOS1=
        safe_text,
    YPOS0=
        safe_text,
    RES=
        safe_text
)
afpText::DataObjectFontDescriptor_strategy = st.builds(
    afpText::DataObjectFontDescriptor,
    FontTech=
        safe_text,
    DOFtFlgs=
        safe_text,
    HFS=
        safe_text,
    EncID=
        safe_text,
    EncEnv=
        safe_text,
    Reserved=
        safe_text,
    VFS=
        safe_text,
    CharRot=
        safe_text
)
afpText::GCBIMG_strategy = st.builds(
    afpText::GCBIMG,
    RES=
        safe_text,
    HEIGHT=
        safe_text,
    WIDTH=
        safe_text,
    FORMAT=
        safe_text
)
afpText::TonerSaver_strategy = st.builds(
    afpText::TonerSaver,
    TSvCtrl=
        safe_text
)
afpText::TileTOC_strategy = st.builds(
    afpText::TileTOC,
    Reserved=
        safe_text
)
afpText::Comment_strategy = st.builds(
    afpText::Comment,
    Comment=
        safe_text
)
afpText::BeginSegment_strategy = st.builds(
    afpText::BeginSegment,
    SEGNAME=
        safe_text
)
afpText::GSPS_strategy = st.builds(
    afpText::GSPS,
    LCID=
        safe_text
)
afpText::ResourceSectionNumber_strategy = st.builds(
    afpText::ResourceSectionNumber,
    ResSNum=
        safe_text
)
afpText::ExternalAlgorithm_strategy = st.builds(
    afpText::ExternalAlgorithm,
    ALGTYPE=
        safe_text
)
afpText::BeginImage_strategy = st.builds(
    afpText::BeginImage,
    OBJTYPE=
        safe_text
)
afpText::AMI_strategy = st.builds(
    afpText::AMI,
    DSPLCMNT=
        safe_text
)
afpText::GSCH_strategy = st.builds(
    afpText::GSCH,
    HX=
        safe_text,
    HY=
        safe_text
)
afpText::TRN_strategy = st.builds(
    afpText::TRN,
    TRNDATA=
        safe_text
)
afpText::FinishingOperation_strategy = st.builds(
    afpText::FinishingOperation,
    AxOffst=
        safe_text,
    FOpType=
        safe_text,
    RefEdge=
        safe_text,
    FOpCnt=
        safe_text,
    OpPos=
        safe_text
)
afpText::ImageEncoding_strategy = st.builds(
    afpText::ImageEncoding,
    RECID=
        safe_text,
    BITORDR=
        safe_text,
    COMPRID=
        safe_text
)
afpText::MeasurementUnits_strategy = st.builds(
    afpText::MeasurementUnits,
    XoaUnits=
        safe_text,
    YoaUnits=
        safe_text,
    YoaBase=
        safe_text,
    XoaBase=
        safe_text
)
afpText::AttributeValue_strategy = st.builds(
    afpText::AttributeValue,
    Reserved0=
        safe_text,
    AttVal=
        safe_text
)
afpText::UniversalDateAndTimeStamp_strategy = st.builds(
    afpText::UniversalDateAndTimeStamp,
    Hour=
        safe_text,
    Second=
        safe_text,
    Day=
        safe_text,
    UTCDiffM=
        safe_text,
    Month=
        safe_text,
    YearAD=
        safe_text,
    TimeZone=
        safe_text,
    Reserved=
        safe_text,
    UTCDiffH=
        safe_text,
    Minute=
        safe_text
)
afpText::CharacterRotation_strategy = st.builds(
    afpText::CharacterRotation,
    CharRot=
        safe_text
)
afpText::DescriptorPosition_strategy = st.builds(
    afpText::DescriptorPosition,
    DesPosID=
        safe_text
)
afpText::ResourceObjectType_strategy = st.builds(
    afpText::ResourceObjectType,
    ConData=
        safe_text,
    ObjType=
        safe_text
)
afpText::AMB_strategy = st.builds(
    afpText::AMB,
    DSPLCMNT=
        safe_text
)
afpText::SVI_strategy = st.builds(
    afpText::SVI,
    INCRMENT=
        safe_text
)
afpText::STO_strategy = st.builds(
    afpText::STO,
    BORNTION=
        safe_text,
    IORNTION=
        safe_text
)
afpText::STC_strategy = st.builds(
    afpText::STC,
    FRGCOLOR=
        safe_text,
    PRECSION=
        safe_text
)
afpText::SIM_strategy = st.builds(
    afpText::SIM,
    DSPLCMNT=
        safe_text
)
afpText::SIA_strategy = st.builds(
    afpText::SIA,
    ADJSTMNT=
        safe_text,
    DIRCTION=
        safe_text
)
afpText::SEC_strategy = st.builds(
    afpText::SEC,
    RESERVED=
        safe_text,
    COLSIZE4=
        safe_text,
    COLSIZE3=
        safe_text,
    COLSIZE2=
        safe_text,
    COLSIZE1=
        safe_text,
    COLVALUE=
        safe_text,
    COLSPCE=
        safe_text
)
afpText::SCFL_strategy = st.builds(
    afpText::SCFL,
    LID=
        safe_text
)
afpText::SBI_strategy = st.builds(
    afpText::SBI,
    INCRMENT=
        safe_text
)
afpText::RPS_strategy = st.builds(
    afpText::RPS,
    RLENGTH=
        safe_text,
    RPTDATA=
        safe_text
)
afpText::RMI_strategy = st.builds(
    afpText::RMI,
    INCRMENT=
        safe_text
)
afpText::RMB_strategy = st.builds(
    afpText::RMB,
    INCRMENT=
        safe_text
)
afpText::OVS_strategy = st.builds(
    afpText::OVS,
    BYPSIDEN=
        safe_text,
    OVERCHAR=
        safe_text
)
afpText::NOPCS_strategy = st.builds(
    afpText::NOPCS,
    IGNDATA=
        safe_text
)
afpText::ESU_strategy = st.builds(
    afpText::ESU,
    LID=
        safe_text
)
afpText::DIR_strategy = st.builds(
    afpText::DIR,
    RWIDTHFRACTION=
        safe_text,
    RWIDTH=
        safe_text,
    RLENGTH=
        safe_text
)
afpText::DBR_strategy = st.builds(
    afpText::DBR,
    RLENGTH=
        safe_text,
    RWIDTHFRACTION=
        safe_text,
    RWIDTH=
        safe_text
)
afpText::GCRLINERG_strategy = st.builds(
    afpText::GCRLINERG,
    YOFFS=
        safe_text,
    XOSSF=
        safe_text
)
afpText::GRLINERG_strategy = st.builds(
    afpText::GRLINERG,
    YOFFS=
        safe_text,
    XOSSF=
        safe_text
)
afpText::GCMRKRG_strategy = st.builds(
    afpText::GCMRKRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::GMRKRG_strategy = st.builds(
    afpText::GMRKRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::GCLINERG_strategy = st.builds(
    afpText::GCLINERG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::triplet_strategy = st.builds(
    afpText::triplet,
)
structuredField_strategy = st.builds(
    structuredField,
)
afpText::BCF_strategy = st.builds(
    afpText::BCF,
    RSName=
        safe_text
)
afpText::BDX_strategy = st.builds(
    afpText::BDX,
    DMXName=
        safe_text
)
afpText::BFN_strategy = st.builds(
    afpText::BFN,
    RSName=
        safe_text
)
afpText::BGR_strategy = st.builds(
    afpText::BGR,
    GdoName=
        safe_text
)
afpText::BOC_strategy = st.builds(
    afpText::BOC,
    ObjCName=
        safe_text
)
afpText::BFG_strategy = st.builds(
    afpText::BFG,
    FEGName=
        safe_text
)
afpText::BII_strategy = st.builds(
    afpText::BII,
    ImoName=
        safe_text
)
afpText::BFM_strategy = st.builds(
    afpText::BFM,
    FMName=
        safe_text
)
afpText::BMM_strategy = st.builds(
    afpText::BMM,
    MMName=
        safe_text
)
afpText::BAG_strategy = st.builds(
    afpText::BAG,
    AEGName=
        safe_text
)
afpText::BCP_strategy = st.builds(
    afpText::BCP,
    RSName=
        safe_text
)
afpText::BIM_strategy = st.builds(
    afpText::BIM,
    IdoName=
        safe_text
)
afpText::BMO_strategy = st.builds(
    afpText::BMO,
    OvlyName=
        safe_text
)
afpText::BDD_strategy = st.builds(
    afpText::BDD,
    YEXTENT=
        safe_text,
    UBASE=
        safe_text,
    COLOR=
        safe_text,
    Reserved2=
        safe_text,
    XUPUB=
        safe_text,
    MOD=
        safe_text,
    WENE=
        safe_text,
    MULT=
        safe_text,
    ELEMENTHEIGHT=
        safe_text,
    YUPUB=
        safe_text,
    MODULEWIDTH=
        safe_text,
    TYPE=
        safe_text,
    XEXTENT=
        safe_text,
    LID=
        safe_text,
    Reserved=
        safe_text
)
afpText::BDA_strategy = st.builds(
    afpText::BDA,
    Xoffset=
        safe_text,
    Yoffset=
        safe_text,
    Data=
        safe_text,
    Flags=
        safe_text
)
afpText::BBC_strategy = st.builds(
    afpText::BBC,
    BCdoName=
        safe_text
)
afpText::BDI_strategy = st.builds(
    afpText::BDI,
    IndxName=
        safe_text
)
afpText::BDM_strategy = st.builds(
    afpText::BDM,
    DMName=
        safe_text,
    DatFmt=
        safe_text
)
afpText::BDG_strategy = st.builds(
    afpText::BDG,
    DEGName=
        safe_text
)
afpText::BCA_strategy = st.builds(
    afpText::BCA,
    CATName=
        safe_text
)
afpText::BOG_strategy = st.builds(
    afpText::BOG,
    OEGName=
        safe_text
)
afpText::BDT_strategy = st.builds(
    afpText::BDT,
    DocName=
        safe_text,
    Reserved=
        safe_text
)
afpText::BNG_strategy = st.builds(
    afpText::BNG,
    PGrpName=
        safe_text
)
afpText::BPF_strategy = st.builds(
    afpText::BPF,
    PFName=
        safe_text
)
afpText::LineData_strategy = st.builds(
    afpText::LineData,
    linedata=
        safe_text
)
afpText::structuredField_strategy = st.builds(
    afpText::structuredField,
)
afpText::Model_strategy = st.builds(
    afpText::Model,
)
afpText::GLINERG_strategy = st.builds(
    afpText::GLINERG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText::GCFLTRG_strategy = st.builds(
    afpText::GCFLTRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText::GFLTRG_strategy = st.builds(
    afpText::GFLTRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::GCCBEZRG_strategy = st.builds(
    afpText::GCCBEZRG,
    YPOS=
        safe_text,
    XPOS=
        safe_text
)
afpText::GCBEZRG_strategy = st.builds(
    afpText::GCBEZRG,
    XPOS=
        safe_text,
    YPOS=
        safe_text
)
afpText::FNNRG_strategy = st.builds(
    afpText::FNNRG,
    TSOffset=
        safe_text,
    GCGID=
        safe_text
)
afpText::ExternalAlgorithmRG_strategy = st.builds(
    afpText::ExternalAlgorithmRG,
    PADALMT=
        safe_text,
    DIRCTN=
        safe_text,
    PADBDRY=
        safe_text
)
afpText::SamplingRatiosRG_strategy = st.builds(
    afpText::SamplingRatiosRG,
    VSAMPLE=
        safe_text,
    HSAMPLE=
        safe_text
)
afpText::TileTOCRG_strategy = st.builds(
    afpText::TileTOCRG,
    YOFFSET=
        safe_text,
    DATAPOS=
        safe_text,
    RELRES=
        safe_text,
    THSIZE=
        safe_text,
    COMPR=
        safe_text,
    XOFFSET=
        safe_text,
    TVSIZE=
        safe_text
)
afpText::BandImageRG_strategy = st.builds(
    afpText::BandImageRG,
    BITCNT=
        safe_text
)
afpText::TLE_strategy = st.builds(
    afpText::TLE,
)
afpText::PTX_strategy = st.builds(
    afpText::PTX,
)
afpText::FGD_strategy = st.builds(
    afpText::FGD,
    ConData=
        safe_text
)
afpText::PGP_strategy = st.builds(
    afpText::PGP,
    Constant=
        safe_text
)
afpText::PTD1_strategy = st.builds(
    afpText::PTD1,
    YPEXTENT=
        safe_text,
    YPUNITVL=
        safe_text,
    XPEXTENT=
        safe_text,
    XPBASE=
        safe_text,
    YPBASE=
        safe_text,
    RESERVED=
        safe_text,
    XPUNITVL=
        safe_text
)
afpText::PTD_strategy = st.builds(
    afpText::PTD,
    YPUNITVL=
        safe_text,
    XPUNITVL=
        safe_text,
    YPEXTENT=
        safe_text,
    RESERVED=
        safe_text,
    YPBASE=
        safe_text,
    XPEXTENT=
        safe_text,
    XPBASE=
        safe_text
)
afpText::PPORG_strategy = st.builds(
    afpText::PPORG,
    YocaOset=
        safe_text,
    ObjType=
        safe_text,
    RGLength=
        safe_text,
    ProcFlgs=
        safe_text,
    XocaOset=
        safe_text
)
afpText::PPO_strategy = st.builds(
    afpText::PPO,
)
afpText::PMC_strategy = st.builds(
    afpText::PMC,
    PMCid=
        safe_text
)
afpText::PGP1_strategy = st.builds(
    afpText::PGP1,
    YOset=
        safe_text,
    XOset=
        safe_text
)
afpText::PGPRG_strategy = st.builds(
    afpText::PGPRG,
    RGLength=
        safe_text,
    YmOset=
        safe_text,
    XmOset=
        safe_text,
    PMCid=
        safe_text,
    PGorient=
        safe_text,
    PgFlgs=
        safe_text,
    SHside=
        safe_text
)
afpText::NOP_strategy = st.builds(
    afpText::NOP,
    UndfData=
        safe_text
)
afpText::MSURG_strategy = st.builds(
    afpText::MSURG,
    Reserved=
        safe_text,
    SUPname=
        safe_text,
    SUPid=
        safe_text
)
afpText::MSU_strategy = st.builds(
    afpText::MSU,
)
afpText::PGD_strategy = st.builds(
    afpText::PGD,
    XpgBase=
        safe_text,
    YpgSize=
        safe_text,
    XpgUnits=
        safe_text,
    Reserved=
        safe_text,
    YpgUnits=
        safe_text,
    YpgBase=
        safe_text,
    XpgSize=
        safe_text
)
afpText::PFC_strategy = st.builds(
    afpText::PFC,
    PFCFlgs=
        safe_text
)
afpText::PEC_strategy = st.builds(
    afpText::PEC,
)
afpText::OCD_strategy = st.builds(
    afpText::OCD,
    ObjCdat=
        safe_text
)
afpText::OBP_strategy = st.builds(
    afpText::OBP,
    YocaOrent=
        safe_text,
    XocaOrent=
        safe_text,
    YocaOset=
        safe_text,
    RGLength=
        safe_text,
    YoaOrent=
        safe_text,
    XocaOset=
        safe_text,
    RefCSys=
        safe_text,
    XoaOrent=
        safe_text,
    YoaOset=
        safe_text,
    XoaOset=
        safe_text,
    OAPosID=
        safe_text
)
afpText::OBD_strategy = st.builds(
    afpText::OBD,
)
afpText::MGO_strategy = st.builds(
    afpText::MGO,
)
afpText::MPSRG_strategy = st.builds(
    afpText::MPSRG,
    Reserved=
        safe_text,
    PsegName=
        safe_text
)
afpText::MPS_strategy = st.builds(
    afpText::MPS,
    Reserved=
        safe_text,
    RGLength=
        safe_text
)
afpText::MPORG_strategy = st.builds(
    afpText::MPORG,
    RGLength=
        safe_text
)
afpText::MPO_strategy = st.builds(
    afpText::MPO,
)
afpText::MPGRG_strategy = st.builds(
    afpText::MPGRG,
    RGLength=
        safe_text
)
afpText::MPG_strategy = st.builds(
    afpText::MPG,
)
afpText::MMTRG_strategy = st.builds(
    afpText::MMTRG,
    RGLength=
        safe_text
)
afpText::MMT_strategy = st.builds(
    afpText::MMT,
)
afpText::MMORG_strategy = st.builds(
    afpText::MMORG,
    OVLname=
        safe_text,
    OVLid=
        safe_text,
    Flags=
        safe_text
)
afpText::MMO_strategy = st.builds(
    afpText::MMO,
    RGLength=
        safe_text
)
afpText::MMDRG_strategy = st.builds(
    afpText::MMDRG,
    RGLength=
        safe_text
)
afpText::MMD_strategy = st.builds(
    afpText::MMD,
)
afpText::MMCRG_strategy = st.builds(
    afpText::MMCRG,
    key=
        safe_text,
    value=
        safe_text
)
afpText::MMC_strategy = st.builds(
    afpText::MMC,
    MMCid=
        safe_text,
    PARAMETER1=
        safe_text
)
afpText::MIORG_strategy = st.builds(
    afpText::MIORG,
    RGLength=
        safe_text
)
afpText::MIO_strategy = st.builds(
    afpText::MIO,
)
afpText::MGORG_strategy = st.builds(
    afpText::MGORG,
    RGLength=
        safe_text
)
afpText::MCC_strategy = st.builds(
    afpText::MCC,
)
afpText::MCARG_strategy = st.builds(
    afpText::MCARG,
    RGLength=
        safe_text
)
afpText::MCA_strategy = st.builds(
    afpText::MCA,
)
afpText::MFC_strategy = st.builds(
    afpText::MFC,
    MFCScpe=
        safe_text,
    MedColl=
        safe_text,
    MFCFlgs=
        safe_text
)
afpText::MDRRG_strategy = st.builds(
    afpText::MDRRG,
    RGLength=
        safe_text
)
afpText::MDR_strategy = st.builds(
    afpText::MDR,
)
afpText::MDD_strategy = st.builds(
    afpText::MDD,
    XmSize=
        safe_text,
    MDDFlgs=
        safe_text,
    YmBase=
        safe_text,
    YmUnits=
        safe_text,
    YmSize=
        safe_text,
    XmUnits=
        safe_text,
    XmBase=
        safe_text
)
afpText::MCF1RG_strategy = st.builds(
    afpText::MCF1RG,
    CFLid=
        safe_text,
    CPName=
        safe_text,
    CharRot=
        safe_text,
    Sectid=
        safe_text,
    CFName=
        safe_text,
    FCSName=
        safe_text
)
afpText::MCF1_strategy = st.builds(
    afpText::MCF1,
    RGLength=
        safe_text
)
afpText::MCFRG_strategy = st.builds(
    afpText::MCFRG,
    RGLength=
        safe_text
)
afpText::MCF_strategy = st.builds(
    afpText::MCF,
)
afpText::MCDRG_strategy = st.builds(
    afpText::MCDRG,
    RGLength=
        safe_text
)
afpText::MCD_strategy = st.builds(
    afpText::MCD,
)
afpText::MCCRG_strategy = st.builds(
    afpText::MCCRG,
    Startnum=
        safe_text,
    Stopnum=
        safe_text,
    MMCid=
        safe_text
)
afpText::LLE_strategy = st.builds(
    afpText::LLE,
    LnkType=
        safe_text
)
afpText::MBCRG_strategy = st.builds(
    afpText::MBCRG,
    RGLength=
        safe_text
)
afpText::MBC_strategy = st.builds(
    afpText::MBC,
)
afpText::LND_strategy = st.builds(
    afpText::LND,
    TxtOrent=
        safe_text,
    SubpgID=
        safe_text,
    DataLgth=
        safe_text,
    NLNDskp=
        safe_text,
    ChnlCde=
        safe_text,
    SupName=
        safe_text,
    NLNDreu=
        safe_text,
    LNDFlgs=
        safe_text,
    CCPID=
        safe_text,
    TxtColor=
        safe_text,
    NLNDsp=
        safe_text,
    SOLid=
        safe_text,
    FntLID=
        safe_text,
    BPos=
        safe_text,
    IPos=
        safe_text,
    NLNDccp=
        safe_text,
    DataStrt=
        safe_text
)
afpText::LNC_strategy = st.builds(
    afpText::LNC,
    NumDSC=
        safe_text
)
afpText::LLERG_strategy = st.builds(
    afpText::LLERG,
    RGLength=
        safe_text,
    RGFunct=
        safe_text
)
afpText::IPO_strategy = st.builds(
    afpText::IPO,
    XolOset=
        safe_text,
    OvlyName=
        safe_text,
    OvlyOrent=
        safe_text,
    YolOset=
        safe_text
)
afpText::IRD_strategy = st.builds(
    afpText::IRD,
    IMdata=
        safe_text
)
afpText::IPS_strategy = st.builds(
    afpText::IPS,
    YpsOset=
        safe_text,
    XpsOset=
        safe_text,
    PsegName=
        safe_text
)
afpText::IPG_strategy = st.builds(
    afpText::IPG,
    IPgFlgs=
        safe_text,
    PgName=
        safe_text
)
afpText::IPD_strategy = st.builds(
    afpText::IPD,
    imageData=
        safe_text,
    IOCAdat=
        safe_text
)
afpText::ICP_strategy = st.builds(
    afpText::ICP,
    XFilSize=
        safe_text,
    YFilSize=
        safe_text,
    YCSize=
        safe_text,
    XCOset=
        safe_text,
    XCSize=
        safe_text,
    YCOset=
        safe_text
)
afpText::IOC_strategy = st.builds(
    afpText::IOC,
    YoaOrent=
        safe_text,
    XoaOset=
        safe_text,
    ConData1=
        safe_text,
    YoaOset=
        safe_text,
    XMap=
        safe_text,
    YMap=
        safe_text,
    XoaOrent=
        safe_text,
    ConData2=
        safe_text
)
afpText::IOB_strategy = st.builds(
    afpText::IOB,
    ObjName=
        safe_text,
    YoaOset=
        safe_text,
    XoaOset=
        safe_text,
    XocaOset=
        safe_text,
    ObjType=
        safe_text,
    YocaOset=
        safe_text,
    RefCSys=
        safe_text,
    XoaOrent=
        safe_text,
    YoaOrent=
        safe_text
)
afpText::IMM_strategy = st.builds(
    afpText::IMM,
    MMPName=
        safe_text
)
afpText::IID_strategy = st.builds(
    afpText::IID,
    YCSizeD=
        safe_text,
    ConData2=
        safe_text,
    XSize=
        safe_text,
    XCSizeD=
        safe_text,
    YBase=
        safe_text,
    YSize=
        safe_text,
    ConData1=
        safe_text,
    YUnits=
        safe_text,
    XBase=
        safe_text,
    XUnits=
        safe_text,
    ConData3=
        safe_text,
    Color=
        safe_text
)
afpText::IEL_strategy = st.builds(
    afpText::IEL,
)
afpText::IDD_strategy = st.builds(
    afpText::IDD,
    UNITBASE=
        safe_text,
    XRESOL=
        safe_text,
    YRESOL=
        safe_text,
    XSIZE=
        safe_text,
    YSIZE=
        safe_text
)
afpText::GDD_strategy = st.builds(
    afpText::GDD,
    GOCAdes=
        safe_text
)
afpText::GAD_strategy = st.builds(
    afpText::GAD,
    GOCAdat=
        safe_text
)
afpText::FNPRG_strategy = st.builds(
    afpText::FNPRG,
    MaxDesDp=
        safe_text,
    Reserved2=
        safe_text,
    UscoreWdf=
        safe_text,
    MaxAscHt=
        safe_text,
    LcHeight=
        safe_text,
    CapMHt=
        safe_text,
    UscorePos=
        safe_text,
    UscoreWd=
        safe_text,
    Retired=
        safe_text,
    Reserved3=
        safe_text,
    Reserved=
        safe_text
)
afpText::FNP_strategy = st.builds(
    afpText::FNP,
)
afpText::FNORG_strategy = st.builds(
    afpText::FNORG,
    OrntFlgs=
        safe_text,
    Reserved2=
        safe_text,
    NomCharInc=
        safe_text,
    MaxCharInc=
        safe_text,
    MaxBOset=
        safe_text,
    MaxBExt=
        safe_text,
    Reserved=
        safe_text,
    MinASp=
        safe_text,
    EmSpInc=
        safe_text,
    FigSpInc=
        safe_text,
    SpCharInc=
        safe_text,
    Reserved3=
        safe_text,
    CharRot=
        safe_text,
    DefBInc=
        safe_text
)
afpText::FNO_strategy = st.builds(
    afpText::FNO,
)
afpText::FNMRG_strategy = st.builds(
    afpText::FNMRG,
    CharBoxWd=
        safe_text,
    PatDOset=
        safe_text,
    CharBoxHt=
        safe_text
)
afpText::FNM_strategy = st.builds(
    afpText::FNM,
)
afpText::FNN_strategy = st.builds(
    afpText::FNN,
    FNNData=
        safe_text
)
afpText::FNIRG_strategy = st.builds(
    afpText::FNIRG,
    BSpace=
        safe_text,
    DescendDp=
        safe_text,
    GCGID=
        safe_text,
    ASpace=
        safe_text,
    FNMCnt=
        safe_text,
    CharInc=
        safe_text,
    BaseOset=
        safe_text,
    CSpace=
        safe_text,
    Reserved=
        safe_text,
    Reserved2=
        safe_text,
    AscendHt=
        safe_text
)
afpText::FNI_strategy = st.builds(
    afpText::FNI,
)
afpText::FNG_strategy = st.builds(
    afpText::FNG,
    PatData=
        safe_text
)
afpText::EPT_strategy = st.builds(
    afpText::EPT,
    PTdoName=
        safe_text
)
afpText::FND_strategy = st.builds(
    afpText::FND,
    FtDsFlags=
        safe_text,
    MinHSize=
        safe_text,
    DsnSpcGrp=
        safe_text,
    FtWdClass=
        safe_text,
    Reserved1=
        safe_text,
    MaxHSize=
        safe_text,
    TypeFcDesc=
        safe_text,
    MaxPtSize=
        safe_text,
    DsnGenCls=
        safe_text,
    Reserved2=
        safe_text,
    NomHSize=
        safe_text,
    FGID=
        safe_text,
    NomPtSize=
        safe_text,
    MinPtSize=
        safe_text,
    DsnSubCls=
        safe_text,
    GCSID=
        safe_text,
    FtWtClass=
        safe_text
)
afpText::FNC_strategy = st.builds(
    afpText::FNC,
    MaxBoxHt=
        safe_text,
    ResYUBase=
        safe_text,
    Reserved1=
        safe_text,
    PatTech=
        safe_text,
    Reserved2=
        safe_text,
    PatAlign=
        safe_text,
    YUnitBase=
        safe_text,
    XUnitBase=
        safe_text,
    XftUnits=
        safe_text,
    YfrUnits=
        safe_text,
    FNORGLen=
        safe_text,
    FNIRGLen=
        safe_text,
    XfrUnits=
        safe_text,
    RPatDCnt=
        safe_text,
    FNMRGLen=
        safe_text,
    OPatDCnt=
        safe_text,
    ResXUBase=
        safe_text,
    FNNRGLen=
        safe_text,
    FNPRGLen=
        safe_text,
    MaxBoxWd=
        safe_text,
    FNNDCnt=
        safe_text,
    FntFlags=
        safe_text,
    YftUnits=
        safe_text,
    Retired=
        safe_text,
    FNNMapCnt=
        safe_text
)
afpText::ESG_strategy = st.builds(
    afpText::ESG,
    REGName=
        safe_text
)
afpText::ERS_strategy = st.builds(
    afpText::ERS,
    RSName=
        safe_text
)
afpText::ERG_strategy = st.builds(
    afpText::ERG,
    RGrpName=
        safe_text
)
afpText::EIM_strategy = st.builds(
    afpText::EIM,
    IdoName=
        safe_text
)
afpText::EPS_strategy = st.builds(
    afpText::EPS,
    PsegName=
        safe_text
)
afpText::EPM_strategy = st.builds(
    afpText::EPM,
    PMName=
        safe_text
)
afpText::EPG_strategy = st.builds(
    afpText::EPG,
    PageName=
        safe_text
)
afpText::EPF_strategy = st.builds(
    afpText::EPF,
    PFName=
        safe_text
)
afpText::EOG_strategy = st.builds(
    afpText::EOG,
    OEGName=
        safe_text
)
afpText::EOC_strategy = st.builds(
    afpText::EOC,
    ObjCName=
        safe_text
)
afpText::ENG_strategy = st.builds(
    afpText::ENG,
    PGrpName=
        safe_text
)
afpText::EMO_strategy = st.builds(
    afpText::EMO,
    OvlyName=
        safe_text
)
afpText::EMM_strategy = st.builds(
    afpText::EMM,
    MMName=
        safe_text
)
afpText::EII_strategy = st.builds(
    afpText::EII,
    ImoName=
        safe_text
)
afpText::EGR_strategy = st.builds(
    afpText::EGR,
    GdoName=
        safe_text
)
afpText::EFN_strategy = st.builds(
    afpText::EFN,
    RSName=
        safe_text
)
afpText::EFM_strategy = st.builds(
    afpText::EFM,
    FMName=
        safe_text
)
afpText::EFG_strategy = st.builds(
    afpText::EFG,
    FEGName=
        safe_text
)
afpText::EDX_strategy = st.builds(
    afpText::EDX,
    DMXName=
        safe_text
)
afpText::EDT_strategy = st.builds(
    afpText::EDT,
    DocName=
        safe_text
)
afpText::EDM_strategy = st.builds(
    afpText::EDM,
    DMName=
        safe_text
)
afpText::EDI_strategy = st.builds(
    afpText::EDI,
    IndxName=
        safe_text
)
afpText::EDG_strategy = st.builds(
    afpText::EDG,
    DEGName=
        safe_text
)
afpText::ECP_strategy = st.builds(
    afpText::ECP,
    RSName=
        safe_text
)
afpText::ECF_strategy = st.builds(
    afpText::ECF,
    RSName=
        safe_text
)
afpText::ECA_strategy = st.builds(
    afpText::ECA,
    CATName=
        safe_text
)
afpText::EBC_strategy = st.builds(
    afpText::EBC,
    BCdoName=
        safe_text
)
afpText::EAG_strategy = st.builds(
    afpText::EAG,
    AEGName=
        safe_text
)
afpText::DXD_strategy = st.builds(
    afpText::DXD,
)
afpText::BRG_strategy = st.builds(
    afpText::BRG,
    RGrpName=
        safe_text
)
afpText::CTC_strategy = st.builds(
    afpText::CTC,
    ConData=
        safe_text
)
afpText::CPIRG_strategy = st.builds(
    afpText::CPIRG,
    Count=
        safe_text,
    CodePoint=
        safe_text,
    PrtFlags=
        safe_text,
    GCGID=
        safe_text
)
afpText::CPI_strategy = st.builds(
    afpText::CPI,
)
afpText::CPD_strategy = st.builds(
    afpText::CPD,
    GCGIDLen=
        safe_text,
    CPDesc=
        safe_text,
    CPGID=
        safe_text,
    GCSGID=
        safe_text,
    NumCdPts=
        safe_text,
    EncScheme=
        safe_text
)
afpText::CPC_strategy = st.builds(
    afpText::CPC,
    VSFlags=
        safe_text,
    VSChar=
        safe_text,
    CPIRGLen=
        safe_text,
    PrtFlags=
        safe_text,
    VSCharSN=
        safe_text,
    DefCharID=
        safe_text
)
afpText::CFIRG_strategy = st.builds(
    afpText::CFIRG,
    SHScale=
        safe_text,
    SVSize=
        safe_text,
    FCSName=
        safe_text,
    CPName=
        safe_text,
    Section=
        safe_text,
    Reserved=
        safe_text
)
afpText::CFI_strategy = st.builds(
    afpText::CFI,
)
afpText::CFC_strategy = st.builds(
    afpText::CFC,
    CFIRGLen=
        safe_text,
    Retired1=
        safe_text
)
afpText::CDD_strategy = st.builds(
    afpText::CDD,
    XocSize=
        safe_text,
    YocUnits=
        safe_text,
    XocUnits=
        safe_text,
    YocBase=
        safe_text,
    XocBase=
        safe_text,
    YocSize=
        safe_text
)
afpText::CAT_strategy = st.builds(
    afpText::CAT,
    CATData=
        safe_text
)
afpText::BSG_strategy = st.builds(
    afpText::BSG,
    REGName=
        safe_text
)
afpText::BRS_strategy = st.builds(
    afpText::BRS,
    RSName=
        safe_text
)
afpText::BPT_strategy = st.builds(
    afpText::BPT,
    PTdoName=
        safe_text
)
afpText::BPS_strategy = st.builds(
    afpText::BPS,
    PsegName=
        safe_text
)
afpText::BPM_strategy = st.builds(
    afpText::BPM,
    PMName=
        safe_text
)
afpText::BPG_strategy = st.builds(
    afpText::BPG,
    PageName=
        safe_text
)

@given(instance=triplet_strategy)
@settings(max_examples=50)
def test_triplet_instantiation(instance):
    assert isinstance(instance, triplet)

@given(instance=afpText::CGCSGID_strategy)
@settings(max_examples=50)
def test_afptext::cgcsgid_instantiation(instance):
    assert isinstance(instance, afpText::CGCSGID)

@given(instance=afpText::CGCSGID_strategy)
def test_afptext::cgcsgid_GCSGID_type(instance):
    assert isinstance(instance.GCSGID, str)


@given(instance=afpText::CGCSGID_strategy)
def test_afptext::cgcsgid_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText::CGCSGID_strategy)
def test_afptext::cgcsgid_CPGID_type(instance):
    assert isinstance(instance.CPGID, str)


@given(instance=afpText::CGCSGID_strategy)
def test_afptext::cgcsgid_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original

@given(instance=afpText::SetBiLevelImageColor_strategy)
@settings(max_examples=50)
def test_afptext::setbilevelimagecolor_instantiation(instance):
    assert isinstance(instance, afpText::SetBiLevelImageColor)

@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_NAMECOLR_type(instance):
    assert isinstance(instance.NAMECOLR, str)


@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_NAMECOLR_setter(instance):
    original = instance.NAMECOLR
    instance.NAMECOLR = original
    assert instance.NAMECOLR == original

@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_AREA_type(instance):
    assert isinstance(instance.AREA, str)


@given(instance=afpText::SetBiLevelImageColor_strategy)
def test_afptext::setbilevelimagecolor_AREA_setter(instance):
    original = instance.AREA
    instance.AREA = original
    assert instance.AREA == original

@given(instance=afpText::GSPCOL_strategy)
@settings(max_examples=50)
def test_afptext::gspcol_instantiation(instance):
    assert isinstance(instance, afpText::GSPCOL)

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_RES2_type(instance):
    assert isinstance(instance.RES2, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_RES2_setter(instance):
    original = instance.RES2
    instance.RES2 = original
    assert instance.RES2 == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_RES1_type(instance):
    assert isinstance(instance.RES1, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_RES1_setter(instance):
    original = instance.RES1
    instance.RES1 = original
    assert instance.RES1 == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSPCE_type(instance):
    assert isinstance(instance.COLSPCE, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSPCE_setter(instance):
    original = instance.COLSPCE
    instance.COLSPCE = original
    assert instance.COLSPCE == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE3_type(instance):
    assert isinstance(instance.COLSIZE3, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE3_setter(instance):
    original = instance.COLSIZE3
    instance.COLSIZE3 = original
    assert instance.COLSIZE3 == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE4_type(instance):
    assert isinstance(instance.COLSIZE4, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE4_setter(instance):
    original = instance.COLSIZE4
    instance.COLSIZE4 = original
    assert instance.COLSIZE4 == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE2_type(instance):
    assert isinstance(instance.COLSIZE2, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE2_setter(instance):
    original = instance.COLSIZE2
    instance.COLSIZE2 = original
    assert instance.COLSIZE2 == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLVALUE_type(instance):
    assert isinstance(instance.COLVALUE, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLVALUE_setter(instance):
    original = instance.COLVALUE
    instance.COLVALUE = original
    assert instance.COLVALUE == original

@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE1_type(instance):
    assert isinstance(instance.COLSIZE1, str)


@given(instance=afpText::GSPCOL_strategy)
def test_afptext::gspcol_COLSIZE1_setter(instance):
    original = instance.COLSIZE1
    instance.COLSIZE1 = original
    assert instance.COLSIZE1 == original

@given(instance=afpText::GBIMG_strategy)
@settings(max_examples=50)
def test_afptext::gbimg_instantiation(instance):
    assert isinstance(instance, afpText::GBIMG)

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_FORMAT_type(instance):
    assert isinstance(instance.FORMAT, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_HEIGHT_type(instance):
    assert isinstance(instance.HEIGHT, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_HEIGHT_setter(instance):
    original = instance.HEIGHT
    instance.HEIGHT = original
    assert instance.HEIGHT == original

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_RES_type(instance):
    assert isinstance(instance.RES, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_WIDTH_type(instance):
    assert isinstance(instance.WIDTH, str)


@given(instance=afpText::GBIMG_strategy)
def test_afptext::gbimg_WIDTH_setter(instance):
    original = instance.WIDTH
    instance.WIDTH = original
    assert instance.WIDTH == original

@given(instance=afpText::BandImage_strategy)
@settings(max_examples=50)
def test_afptext::bandimage_instantiation(instance):
    assert isinstance(instance, afpText::BandImage)

@given(instance=afpText::BandImage_strategy)
def test_afptext::bandimage_BCOUNT_type(instance):
    assert isinstance(instance.BCOUNT, str)


@given(instance=afpText::BandImage_strategy)
def test_afptext::bandimage_BCOUNT_setter(instance):
    original = instance.BCOUNT
    instance.BCOUNT = original
    assert instance.BCOUNT == original

@given(instance=afpText::ObjectByteOffset_strategy)
@settings(max_examples=50)
def test_afptext::objectbyteoffset_instantiation(instance):
    assert isinstance(instance, afpText::ObjectByteOffset)

@given(instance=afpText::ObjectByteOffset_strategy)
def test_afptext::objectbyteoffset_DirByHi_type(instance):
    assert isinstance(instance.DirByHi, str)


@given(instance=afpText::ObjectByteOffset_strategy)
def test_afptext::objectbyteoffset_DirByHi_setter(instance):
    original = instance.DirByHi
    instance.DirByHi = original
    assert instance.DirByHi == original

@given(instance=afpText::ObjectByteOffset_strategy)
def test_afptext::objectbyteoffset_DirByOff_type(instance):
    assert isinstance(instance.DirByOff, str)


@given(instance=afpText::ObjectByteOffset_strategy)
def test_afptext::objectbyteoffset_DirByOff_setter(instance):
    original = instance.DirByOff
    instance.DirByOff = original
    assert instance.DirByOff == original

@given(instance=afpText::GSMC_strategy)
@settings(max_examples=50)
def test_afptext::gsmc_instantiation(instance):
    assert isinstance(instance, afpText::GSMC)

@given(instance=afpText::GSMC_strategy)
def test_afptext::gsmc_CELLWI_type(instance):
    assert isinstance(instance.CELLWI, str)


@given(instance=afpText::GSMC_strategy)
def test_afptext::gsmc_CELLWI_setter(instance):
    original = instance.CELLWI
    instance.CELLWI = original
    assert instance.CELLWI == original

@given(instance=afpText::GSMC_strategy)
def test_afptext::gsmc_CELLHI_type(instance):
    assert isinstance(instance.CELLHI, str)


@given(instance=afpText::GSMC_strategy)
def test_afptext::gsmc_CELLHI_setter(instance):
    original = instance.CELLHI
    instance.CELLHI = original
    assert instance.CELLHI == original

@given(instance=afpText::AttributeQualifier_strategy)
@settings(max_examples=50)
def test_afptext::attributequalifier_instantiation(instance):
    assert isinstance(instance, afpText::AttributeQualifier)

@given(instance=afpText::AttributeQualifier_strategy)
def test_afptext::attributequalifier_SeqNum_type(instance):
    assert isinstance(instance.SeqNum, str)


@given(instance=afpText::AttributeQualifier_strategy)
def test_afptext::attributequalifier_SeqNum_setter(instance):
    original = instance.SeqNum
    instance.SeqNum = original
    assert instance.SeqNum == original

@given(instance=afpText::AttributeQualifier_strategy)
def test_afptext::attributequalifier_LevNum_type(instance):
    assert isinstance(instance.LevNum, str)


@given(instance=afpText::AttributeQualifier_strategy)
def test_afptext::attributequalifier_LevNum_setter(instance):
    original = instance.LevNum
    instance.LevNum = original
    assert instance.LevNum == original

@given(instance=afpText::ObjectStructuredFieldOffset_strategy)
@settings(max_examples=50)
def test_afptext::objectstructuredfieldoffset_instantiation(instance):
    assert isinstance(instance, afpText::ObjectStructuredFieldOffset)

@given(instance=afpText::ObjectStructuredFieldOffset_strategy)
def test_afptext::objectstructuredfieldoffset_SFOffHi_type(instance):
    assert isinstance(instance.SFOffHi, str)


@given(instance=afpText::ObjectStructuredFieldOffset_strategy)
def test_afptext::objectstructuredfieldoffset_SFOffHi_setter(instance):
    original = instance.SFOffHi
    instance.SFOffHi = original
    assert instance.SFOffHi == original

@given(instance=afpText::ObjectStructuredFieldOffset_strategy)
def test_afptext::objectstructuredfieldoffset_SFOff_type(instance):
    assert isinstance(instance.SFOff, str)


@given(instance=afpText::ObjectStructuredFieldOffset_strategy)
def test_afptext::objectstructuredfieldoffset_SFOff_setter(instance):
    original = instance.SFOff
    instance.SFOff = original
    assert instance.SFOff == original

@given(instance=afpText::ObjectCount_strategy)
@settings(max_examples=50)
def test_afptext::objectcount_instantiation(instance):
    assert isinstance(instance, afpText::ObjectCount)

@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SubObj_type(instance):
    assert isinstance(instance.SubObj, str)


@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SubObj_setter(instance):
    original = instance.SubObj
    instance.SubObj = original
    assert instance.SubObj == original

@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SObjNum_type(instance):
    assert isinstance(instance.SObjNum, str)


@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SObjNum_setter(instance):
    original = instance.SObjNum
    instance.SObjNum = original
    assert instance.SObjNum == original

@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SobjNmHi_type(instance):
    assert isinstance(instance.SobjNmHi, str)


@given(instance=afpText::ObjectCount_strategy)
def test_afptext::objectcount_SobjNmHi_setter(instance):
    original = instance.SobjNmHi
    instance.SobjNmHi = original
    assert instance.SobjNmHi == original

@given(instance=afpText::GSMX_strategy)
@settings(max_examples=50)
def test_afptext::gsmx_instantiation(instance):
    assert isinstance(instance, afpText::GSMX)

@given(instance=afpText::GSMX_strategy)
def test_afptext::gsmx_MODE_type(instance):
    assert isinstance(instance.MODE, str)


@given(instance=afpText::GSMX_strategy)
def test_afptext::gsmx_MODE_setter(instance):
    original = instance.MODE
    instance.MODE = original
    assert instance.MODE == original

@given(instance=afpText::EndImage_strategy)
@settings(max_examples=50)
def test_afptext::endimage_instantiation(instance):
    assert isinstance(instance, afpText::EndImage)

@given(instance=afpText::FontResolution_strategy)
@settings(max_examples=50)
def test_afptext::fontresolution_instantiation(instance):
    assert isinstance(instance, afpText::FontResolution)

@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_RPuBase_type(instance):
    assert isinstance(instance.RPuBase, str)


@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_RPuBase_setter(instance):
    original = instance.RPuBase
    instance.RPuBase = original
    assert instance.RPuBase == original

@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_MetTech_type(instance):
    assert isinstance(instance.MetTech, str)


@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_MetTech_setter(instance):
    original = instance.MetTech
    instance.MetTech = original
    assert instance.MetTech == original

@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_RPUnits_type(instance):
    assert isinstance(instance.RPUnits, str)


@given(instance=afpText::FontResolution_strategy)
def test_afptext::fontresolution_RPUnits_setter(instance):
    original = instance.RPUnits
    instance.RPUnits = original
    assert instance.RPUnits == original

@given(instance=afpText::EndTile_strategy)
@settings(max_examples=50)
def test_afptext::endtile_instantiation(instance):
    assert isinstance(instance, afpText::EndTile)

@given(instance=afpText::GSGCH_strategy)
@settings(max_examples=50)
def test_afptext::gsgch_instantiation(instance):
    assert isinstance(instance, afpText::GSGCH)

@given(instance=afpText::ColorFidelity_strategy)
@settings(max_examples=50)
def test_afptext::colorfidelity_instantiation(instance):
    assert isinstance(instance, afpText::ColorFidelity)

@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_StpCoEx_type(instance):
    assert isinstance(instance.StpCoEx, str)


@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_StpCoEx_setter(instance):
    original = instance.StpCoEx
    instance.StpCoEx = original
    assert instance.StpCoEx == original

@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_ColSub_type(instance):
    assert isinstance(instance.ColSub, str)


@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_ColSub_setter(instance):
    original = instance.ColSub
    instance.ColSub = original
    assert instance.ColSub == original

@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_RepCoEx_type(instance):
    assert isinstance(instance.RepCoEx, str)


@given(instance=afpText::ColorFidelity_strategy)
def test_afptext::colorfidelity_RepCoEx_setter(instance):
    original = instance.RepCoEx
    instance.RepCoEx = original
    assert instance.RepCoEx == original

@given(instance=afpText::IDESize_strategy)
@settings(max_examples=50)
def test_afptext::idesize_instantiation(instance):
    assert isinstance(instance, afpText::IDESize)

@given(instance=afpText::IDESize_strategy)
def test_afptext::idesize_IDESZ_type(instance):
    assert isinstance(instance.IDESZ, str)


@given(instance=afpText::IDESize_strategy)
def test_afptext::idesize_IDESZ_setter(instance):
    original = instance.IDESZ
    instance.IDESZ = original
    assert instance.IDESZ == original

@given(instance=afpText::EncodingSchemeID_strategy)
@settings(max_examples=50)
def test_afptext::encodingschemeid_instantiation(instance):
    assert isinstance(instance, afpText::EncodingSchemeID)

@given(instance=afpText::EncodingSchemeID_strategy)
def test_afptext::encodingschemeid_ESidCP_type(instance):
    assert isinstance(instance.ESidCP, str)


@given(instance=afpText::EncodingSchemeID_strategy)
def test_afptext::encodingschemeid_ESidCP_setter(instance):
    original = instance.ESidCP
    instance.ESidCP = original
    assert instance.ESidCP == original

@given(instance=afpText::EncodingSchemeID_strategy)
def test_afptext::encodingschemeid_ESidUD_type(instance):
    assert isinstance(instance.ESidUD, str)


@given(instance=afpText::EncodingSchemeID_strategy)
def test_afptext::encodingschemeid_ESidUD_setter(instance):
    original = instance.ESidUD
    instance.ESidUD = original
    assert instance.ESidUD == original

@given(instance=afpText::GSAP_strategy)
@settings(max_examples=50)
def test_afptext::gsap_instantiation(instance):
    assert isinstance(instance, afpText::GSAP)

@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_Q_type(instance):
    assert isinstance(instance.Q, str)


@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_Q_setter(instance):
    original = instance.Q
    instance.Q = original
    assert instance.Q == original

@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_S_type(instance):
    assert isinstance(instance.S, str)


@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_S_setter(instance):
    original = instance.S
    instance.S = original
    assert instance.S == original

@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_R_type(instance):
    assert isinstance(instance.R, str)


@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_R_setter(instance):
    original = instance.R
    instance.R = original
    assert instance.R == original

@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_P_type(instance):
    assert isinstance(instance.P, str)


@given(instance=afpText::GSAP_strategy)
def test_afptext::gsap_P_setter(instance):
    original = instance.P
    instance.P = original
    assert instance.P == original

@given(instance=afpText::GCCBEZ_strategy)
@settings(max_examples=50)
def test_afptext::gccbez_instantiation(instance):
    assert isinstance(instance, afpText::GCCBEZ)

@given(instance=afpText::GSECOL_strategy)
@settings(max_examples=50)
def test_afptext::gsecol_instantiation(instance):
    assert isinstance(instance, afpText::GSECOL)

@given(instance=afpText::GSECOL_strategy)
def test_afptext::gsecol_COLOR_type(instance):
    assert isinstance(instance.COLOR, str)


@given(instance=afpText::GSECOL_strategy)
def test_afptext::gsecol_COLOR_setter(instance):
    original = instance.COLOR
    instance.COLOR = original
    assert instance.COLOR == original

@given(instance=afpText::GSCS_strategy)
@settings(max_examples=50)
def test_afptext::gscs_instantiation(instance):
    assert isinstance(instance, afpText::GSCS)

@given(instance=afpText::GSCS_strategy)
def test_afptext::gscs_LCID_type(instance):
    assert isinstance(instance.LCID, str)


@given(instance=afpText::GSCS_strategy)
def test_afptext::gscs_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText::MediaEjectControl_strategy)
@settings(max_examples=50)
def test_afptext::mediaejectcontrol_instantiation(instance):
    assert isinstance(instance, afpText::MediaEjectControl)

@given(instance=afpText::MediaEjectControl_strategy)
def test_afptext::mediaejectcontrol_EjCtrl_type(instance):
    assert isinstance(instance.EjCtrl, str)


@given(instance=afpText::MediaEjectControl_strategy)
def test_afptext::mediaejectcontrol_EjCtrl_setter(instance):
    original = instance.EjCtrl
    instance.EjCtrl = original
    assert instance.EjCtrl == original

@given(instance=afpText::MediaEjectControl_strategy)
def test_afptext::mediaejectcontrol_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::MediaEjectControl_strategy)
def test_afptext::mediaejectcontrol_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::BeginTransparencyMask_strategy)
@settings(max_examples=50)
def test_afptext::begintransparencymask_instantiation(instance):
    assert isinstance(instance, afpText::BeginTransparencyMask)

@given(instance=afpText::GSMS_strategy)
@settings(max_examples=50)
def test_afptext::gsms_instantiation(instance):
    assert isinstance(instance, afpText::GSMS)

@given(instance=afpText::GSMS_strategy)
def test_afptext::gsms_LCID_type(instance):
    assert isinstance(instance.LCID, str)


@given(instance=afpText::GSMS_strategy)
def test_afptext::gsms_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText::GEPROL_strategy)
@settings(max_examples=50)
def test_afptext::geprol_instantiation(instance):
    assert isinstance(instance, afpText::GEPROL)

@given(instance=afpText::GEPROL_strategy)
def test_afptext::geprol_RES_type(instance):
    assert isinstance(instance.RES, str)


@given(instance=afpText::GEPROL_strategy)
def test_afptext::geprol_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
@settings(max_examples=50)
def test_afptext::objectfunctionsetspecification_instantiation(instance):
    assert isinstance(instance, afpText::ObjectFunctionSetSpecification)

@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_OCAFnSet_type(instance):
    assert isinstance(instance.OCAFnSet, str)


@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_OCAFnSet_setter(instance):
    original = instance.OCAFnSet
    instance.OCAFnSet = original
    assert instance.OCAFnSet == original

@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_ObjType_type(instance):
    assert isinstance(instance.ObjType, str)


@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_DCAFnSet_type(instance):
    assert isinstance(instance.DCAFnSet, str)


@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_DCAFnSet_setter(instance):
    original = instance.DCAFnSet
    instance.DCAFnSet = original
    assert instance.DCAFnSet == original

@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_ArchVrsn_type(instance):
    assert isinstance(instance.ArchVrsn, str)


@given(instance=afpText::ObjectFunctionSetSpecification_strategy)
def test_afptext::objectfunctionsetspecification_ArchVrsn_setter(instance):
    original = instance.ArchVrsn
    instance.ArchVrsn = original
    assert instance.ArchVrsn == original

@given(instance=afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext::fontcodedgraphiccharactersetglobalidentifier_instantiation(instance):
    assert isinstance(instance, afpText::FontCodedGraphicCharacterSetGlobalIdentifier)

@given(instance=afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext::fontcodedgraphiccharactersetglobalidentifier_GCSGID_type(instance):
    assert isinstance(instance.GCSGID, str)


@given(instance=afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext::fontcodedgraphiccharactersetglobalidentifier_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext::fontcodedgraphiccharactersetglobalidentifier_CPGID_type(instance):
    assert isinstance(instance.CPGID, str)


@given(instance=afpText::FontCodedGraphicCharacterSetGlobalIdentifier_strategy)
def test_afptext::fontcodedgraphiccharactersetglobalidentifier_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original

@given(instance=afpText::GCHST_strategy)
@settings(max_examples=50)
def test_afptext::gchst_instantiation(instance):
    assert isinstance(instance, afpText::GCHST)

@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_CP_type(instance):
    assert isinstance(instance.CP, str)


@given(instance=afpText::GCHST_strategy)
def test_afptext::gchst_CP_setter(instance):
    original = instance.CP
    instance.CP = original
    assert instance.CP == original

@given(instance=afpText::PagePositionInformation_strategy)
@settings(max_examples=50)
def test_afptext::pagepositioninformation_instantiation(instance):
    assert isinstance(instance, afpText::PagePositionInformation)

@given(instance=afpText::PagePositionInformation_strategy)
def test_afptext::pagepositioninformation_PGPRG_type(instance):
    assert isinstance(instance.PGPRG, str)


@given(instance=afpText::PagePositionInformation_strategy)
def test_afptext::pagepositioninformation_PGPRG_setter(instance):
    original = instance.PGPRG
    instance.PGPRG = original
    assert instance.PGPRG == original

@given(instance=afpText::ColorSpecification_strategy)
@settings(max_examples=50)
def test_afptext::colorspecification_instantiation(instance):
    assert isinstance(instance, afpText::ColorSpecification)

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize1_type(instance):
    assert isinstance(instance.ColSize1, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize1_setter(instance):
    original = instance.ColSize1
    instance.ColSize1 = original
    assert instance.ColSize1 == original

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize2_type(instance):
    assert isinstance(instance.ColSize2, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize2_setter(instance):
    original = instance.ColSize2
    instance.ColSize2 = original
    assert instance.ColSize2 == original

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize4_type(instance):
    assert isinstance(instance.ColSize4, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize4_setter(instance):
    original = instance.ColSize4
    instance.ColSize4 = original
    assert instance.ColSize4 == original

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSpce_type(instance):
    assert isinstance(instance.ColSpce, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSpce_setter(instance):
    original = instance.ColSpce
    instance.ColSpce = original
    assert instance.ColSpce == original

@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize3_type(instance):
    assert isinstance(instance.ColSize3, str)


@given(instance=afpText::ColorSpecification_strategy)
def test_afptext::colorspecification_ColSize3_setter(instance):
    original = instance.ColSize3
    instance.ColSize3 = original
    assert instance.ColSize3 == original

@given(instance=afpText::TBM_strategy)
@settings(max_examples=50)
def test_afptext::tbm_instantiation(instance):
    assert isinstance(instance, afpText::TBM)

@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_INCRMENT_type(instance):
    assert isinstance(instance.INCRMENT, str)


@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_PRECSION_type(instance):
    assert isinstance(instance.PRECSION, str)


@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_PRECSION_setter(instance):
    original = instance.PRECSION
    instance.PRECSION = original
    assert instance.PRECSION == original

@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_DIRCTION_type(instance):
    assert isinstance(instance.DIRCTION, str)


@given(instance=afpText::TBM_strategy)
def test_afptext::tbm_DIRCTION_setter(instance):
    original = instance.DIRCTION
    instance.DIRCTION = original
    assert instance.DIRCTION == original

@given(instance=afpText::GIMD_strategy)
@settings(max_examples=50)
def test_afptext::gimd_instantiation(instance):
    assert isinstance(instance, afpText::GIMD)

@given(instance=afpText::GIMD_strategy)
def test_afptext::gimd_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::GIMD_strategy)
def test_afptext::gimd_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::GSMP_strategy)
@settings(max_examples=50)
def test_afptext::gsmp_instantiation(instance):
    assert isinstance(instance, afpText::GSMP)

@given(instance=afpText::GSMP_strategy)
def test_afptext::gsmp_PREC_type(instance):
    assert isinstance(instance.PREC, str)


@given(instance=afpText::GSMP_strategy)
def test_afptext::gsmp_PREC_setter(instance):
    original = instance.PREC
    instance.PREC = original
    assert instance.PREC == original

@given(instance=afpText::GCBEZ_strategy)
@settings(max_examples=50)
def test_afptext::gcbez_instantiation(instance):
    assert isinstance(instance, afpText::GCBEZ)

@given(instance=afpText::MetricAdjustment_strategy)
@settings(max_examples=50)
def test_afptext::metricadjustment_instantiation(instance):
    assert isinstance(instance, afpText::MetricAdjustment)

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_VUniformIncrement_type(instance):
    assert isinstance(instance.VUniformIncrement, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_VUniformIncrement_setter(instance):
    original = instance.VUniformIncrement
    instance.VUniformIncrement = original
    assert instance.VUniformIncrement == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_VBaselineIncrement_type(instance):
    assert isinstance(instance.VBaselineIncrement, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_VBaselineIncrement_setter(instance):
    original = instance.VBaselineIncrement
    instance.VBaselineIncrement = original
    assert instance.VBaselineIncrement == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_HUniformIncrement_type(instance):
    assert isinstance(instance.HUniformIncrement, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_HUniformIncrement_setter(instance):
    original = instance.HUniformIncrement
    instance.HUniformIncrement = original
    assert instance.HUniformIncrement == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_HBaselineIncrement_type(instance):
    assert isinstance(instance.HBaselineIncrement, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_HBaselineIncrement_setter(instance):
    original = instance.HBaselineIncrement
    instance.HBaselineIncrement = original
    assert instance.HBaselineIncrement == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_XUPUB_type(instance):
    assert isinstance(instance.XUPUB, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_XUPUB_setter(instance):
    original = instance.XUPUB
    instance.XUPUB = original
    assert instance.XUPUB == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_UnitBase_type(instance):
    assert isinstance(instance.UnitBase, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_UnitBase_setter(instance):
    original = instance.UnitBase
    instance.UnitBase = original
    assert instance.UnitBase == original

@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_YUPUB_type(instance):
    assert isinstance(instance.YUPUB, str)


@given(instance=afpText::MetricAdjustment_strategy)
def test_afptext::metricadjustment_YUPUB_setter(instance):
    original = instance.YUPUB
    instance.YUPUB = original
    assert instance.YUPUB == original

@given(instance=afpText::ObjectContainerPresentationSpaceSize_strategy)
@settings(max_examples=50)
def test_afptext::objectcontainerpresentationspacesize_instantiation(instance):
    assert isinstance(instance, afpText::ObjectContainerPresentationSpaceSize)

@given(instance=afpText::ObjectContainerPresentationSpaceSize_strategy)
def test_afptext::objectcontainerpresentationspacesize_PDFSize_type(instance):
    assert isinstance(instance.PDFSize, str)


@given(instance=afpText::ObjectContainerPresentationSpaceSize_strategy)
def test_afptext::objectcontainerpresentationspacesize_PDFSize_setter(instance):
    original = instance.PDFSize
    instance.PDFSize = original
    assert instance.PDFSize == original

@given(instance=afpText::ResourceLocalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext::resourcelocalidentifier_instantiation(instance):
    assert isinstance(instance, afpText::ResourceLocalIdentifier)

@given(instance=afpText::ResourceLocalIdentifier_strategy)
def test_afptext::resourcelocalidentifier_ResLID_type(instance):
    assert isinstance(instance.ResLID, str)


@given(instance=afpText::ResourceLocalIdentifier_strategy)
def test_afptext::resourcelocalidentifier_ResLID_setter(instance):
    original = instance.ResLID
    instance.ResLID = original
    assert instance.ResLID == original

@given(instance=afpText::ResourceLocalIdentifier_strategy)
def test_afptext::resourcelocalidentifier_ResType_type(instance):
    assert isinstance(instance.ResType, str)


@given(instance=afpText::ResourceLocalIdentifier_strategy)
def test_afptext::resourcelocalidentifier_ResType_setter(instance):
    original = instance.ResType
    instance.ResType = original
    assert instance.ResType == original

@given(instance=afpText::PresentationControl_strategy)
@settings(max_examples=50)
def test_afptext::presentationcontrol_instantiation(instance):
    assert isinstance(instance, afpText::PresentationControl)

@given(instance=afpText::PresentationControl_strategy)
def test_afptext::presentationcontrol_PRSFlg_type(instance):
    assert isinstance(instance.PRSFlg, str)


@given(instance=afpText::PresentationControl_strategy)
def test_afptext::presentationcontrol_PRSFlg_setter(instance):
    original = instance.PRSFlg
    instance.PRSFlg = original
    assert instance.PRSFlg == original

@given(instance=afpText::ExtendedResourceLocalIdentifier_strategy)
@settings(max_examples=50)
def test_afptext::extendedresourcelocalidentifier_instantiation(instance):
    assert isinstance(instance, afpText::ExtendedResourceLocalIdentifier)

@given(instance=afpText::ExtendedResourceLocalIdentifier_strategy)
def test_afptext::extendedresourcelocalidentifier_ResLID_type(instance):
    assert isinstance(instance.ResLID, str)


@given(instance=afpText::ExtendedResourceLocalIdentifier_strategy)
def test_afptext::extendedresourcelocalidentifier_ResLID_setter(instance):
    original = instance.ResLID
    instance.ResLID = original
    assert instance.ResLID == original

@given(instance=afpText::ExtendedResourceLocalIdentifier_strategy)
def test_afptext::extendedresourcelocalidentifier_ResType_type(instance):
    assert isinstance(instance.ResType, str)


@given(instance=afpText::ExtendedResourceLocalIdentifier_strategy)
def test_afptext::extendedresourcelocalidentifier_ResType_setter(instance):
    original = instance.ResType
    instance.ResType = original
    assert instance.ResType == original

@given(instance=afpText::ColorManagementResourceDescriptor_strategy)
@settings(max_examples=50)
def test_afptext::colormanagementresourcedescriptor_instantiation(instance):
    assert isinstance(instance, afpText::ColorManagementResourceDescriptor)

@given(instance=afpText::ColorManagementResourceDescriptor_strategy)
def test_afptext::colormanagementresourcedescriptor_ProcMode_type(instance):
    assert isinstance(instance.ProcMode, str)


@given(instance=afpText::ColorManagementResourceDescriptor_strategy)
def test_afptext::colormanagementresourcedescriptor_ProcMode_setter(instance):
    original = instance.ProcMode
    instance.ProcMode = original
    assert instance.ProcMode == original

@given(instance=afpText::ColorManagementResourceDescriptor_strategy)
def test_afptext::colormanagementresourcedescriptor_CMRScpe_type(instance):
    assert isinstance(instance.CMRScpe, str)


@given(instance=afpText::ColorManagementResourceDescriptor_strategy)
def test_afptext::colormanagementresourcedescriptor_CMRScpe_setter(instance):
    original = instance.CMRScpe
    instance.CMRScpe = original
    assert instance.CMRScpe == original

@given(instance=afpText::GCCHST_strategy)
@settings(max_examples=50)
def test_afptext::gcchst_instantiation(instance):
    assert isinstance(instance, afpText::GCCHST)

@given(instance=afpText::GCCHST_strategy)
def test_afptext::gcchst_CP_type(instance):
    assert isinstance(instance.CP, str)


@given(instance=afpText::GCCHST_strategy)
def test_afptext::gcchst_CP_setter(instance):
    original = instance.CP
    instance.CP = original
    assert instance.CP == original

@given(instance=afpText::LineDataObjectPositionMigration_strategy)
@settings(max_examples=50)
def test_afptext::linedataobjectpositionmigration_instantiation(instance):
    assert isinstance(instance, afpText::LineDataObjectPositionMigration)

@given(instance=afpText::LineDataObjectPositionMigration_strategy)
def test_afptext::linedataobjectpositionmigration_TempOrient_type(instance):
    assert isinstance(instance.TempOrient, str)


@given(instance=afpText::LineDataObjectPositionMigration_strategy)
def test_afptext::linedataobjectpositionmigration_TempOrient_setter(instance):
    original = instance.TempOrient
    instance.TempOrient = original
    assert instance.TempOrient == original

@given(instance=afpText::GSCP_strategy)
@settings(max_examples=50)
def test_afptext::gscp_instantiation(instance):
    assert isinstance(instance, afpText::GSCP)

@given(instance=afpText::GSCP_strategy)
def test_afptext::gscp_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GSCP_strategy)
def test_afptext::gscp_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GSCP_strategy)
def test_afptext::gscp_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GSCP_strategy)
def test_afptext::gscp_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCOMT_strategy)
@settings(max_examples=50)
def test_afptext::gcomt_instantiation(instance):
    assert isinstance(instance, afpText::GCOMT)

@given(instance=afpText::GCOMT_strategy)
def test_afptext::gcomt_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::GCOMT_strategy)
def test_afptext::gcomt_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::GBAR_strategy)
@settings(max_examples=50)
def test_afptext::gbar_instantiation(instance):
    assert isinstance(instance, afpText::GBAR)

@given(instance=afpText::GBAR_strategy)
def test_afptext::gbar_FLAGS_type(instance):
    assert isinstance(instance.FLAGS, str)


@given(instance=afpText::GBAR_strategy)
def test_afptext::gbar_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original

@given(instance=afpText::FNNRG2_strategy)
@settings(max_examples=50)
def test_afptext::fnnrg2_instantiation(instance):
    assert isinstance(instance, afpText::FNNRG2)

@given(instance=afpText::FNNRG2_strategy)
def test_afptext::fnnrg2_TSID_type(instance):
    assert isinstance(instance.TSID, str)


@given(instance=afpText::FNNRG2_strategy)
def test_afptext::fnnrg2_TSID_setter(instance):
    original = instance.TSID
    instance.TSID = original
    assert instance.TSID == original

@given(instance=afpText::FNNRG2_strategy)
def test_afptext::fnnrg2_TSIDLen_type(instance):
    assert isinstance(instance.TSIDLen, str)


@given(instance=afpText::FNNRG2_strategy)
def test_afptext::fnnrg2_TSIDLen_setter(instance):
    original = instance.TSIDLen
    instance.TSIDLen = original
    assert instance.TSIDLen == original

@given(instance=afpText::BLN_strategy)
@settings(max_examples=50)
def test_afptext::bln_instantiation(instance):
    assert isinstance(instance, afpText::BLN)

@given(instance=afpText::GSFLW_strategy)
@settings(max_examples=50)
def test_afptext::gsflw_instantiation(instance):
    assert isinstance(instance, afpText::GSFLW)

@given(instance=afpText::GSFLW_strategy)
def test_afptext::gsflw_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GSFLW_strategy)
def test_afptext::gsflw_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::GSFLW_strategy)
def test_afptext::gsflw_MFR_type(instance):
    assert isinstance(instance.MFR, str)


@given(instance=afpText::GSFLW_strategy)
def test_afptext::gsflw_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText::GSLT_strategy)
@settings(max_examples=50)
def test_afptext::gslt_instantiation(instance):
    assert isinstance(instance, afpText::GSLT)

@given(instance=afpText::GSLT_strategy)
def test_afptext::gslt_LINETYPE_type(instance):
    assert isinstance(instance.LINETYPE, str)


@given(instance=afpText::GSLT_strategy)
def test_afptext::gslt_LINETYPE_setter(instance):
    original = instance.LINETYPE
    instance.LINETYPE = original
    assert instance.LINETYPE == original

@given(instance=afpText::ObjectByteExtent_strategy)
@settings(max_examples=50)
def test_afptext::objectbyteextent_instantiation(instance):
    assert isinstance(instance, afpText::ObjectByteExtent)

@given(instance=afpText::ObjectByteExtent_strategy)
def test_afptext::objectbyteextent_ByteExt_type(instance):
    assert isinstance(instance.ByteExt, str)


@given(instance=afpText::ObjectByteExtent_strategy)
def test_afptext::objectbyteextent_ByteExt_setter(instance):
    original = instance.ByteExt
    instance.ByteExt = original
    assert instance.ByteExt == original

@given(instance=afpText::ObjectByteExtent_strategy)
def test_afptext::objectbyteextent_ByteExtHi_type(instance):
    assert isinstance(instance.ByteExtHi, str)


@given(instance=afpText::ObjectByteExtent_strategy)
def test_afptext::objectbyteextent_ByteExtHi_setter(instance):
    original = instance.ByteExtHi
    instance.ByteExtHi = original
    assert instance.ByteExtHi == original

@given(instance=afpText::GSBMX_strategy)
@settings(max_examples=50)
def test_afptext::gsbmx_instantiation(instance):
    assert isinstance(instance, afpText::GSBMX)

@given(instance=afpText::GSBMX_strategy)
def test_afptext::gsbmx_MODE_type(instance):
    assert isinstance(instance.MODE, str)


@given(instance=afpText::GSBMX_strategy)
def test_afptext::gsbmx_MODE_setter(instance):
    original = instance.MODE
    instance.MODE = original
    assert instance.MODE == original

@given(instance=afpText::USC_strategy)
@settings(max_examples=50)
def test_afptext::usc_instantiation(instance):
    assert isinstance(instance, afpText::USC)

@given(instance=afpText::USC_strategy)
def test_afptext::usc_BYPSIDEN_type(instance):
    assert isinstance(instance.BYPSIDEN, str)


@given(instance=afpText::USC_strategy)
def test_afptext::usc_BYPSIDEN_setter(instance):
    original = instance.BYPSIDEN
    instance.BYPSIDEN = original
    assert instance.BYPSIDEN == original

@given(instance=afpText::FinishingFidelity_strategy)
@settings(max_examples=50)
def test_afptext::finishingfidelity_instantiation(instance):
    assert isinstance(instance, afpText::FinishingFidelity)

@given(instance=afpText::FinishingFidelity_strategy)
def test_afptext::finishingfidelity_RepFinEx_type(instance):
    assert isinstance(instance.RepFinEx, str)


@given(instance=afpText::FinishingFidelity_strategy)
def test_afptext::finishingfidelity_RepFinEx_setter(instance):
    original = instance.RepFinEx
    instance.RepFinEx = original
    assert instance.RepFinEx == original

@given(instance=afpText::FinishingFidelity_strategy)
def test_afptext::finishingfidelity_StpFinEx_type(instance):
    assert isinstance(instance.StpFinEx, str)


@given(instance=afpText::FinishingFidelity_strategy)
def test_afptext::finishingfidelity_StpFinEx_setter(instance):
    original = instance.StpFinEx
    instance.StpFinEx = original
    assert instance.StpFinEx == original

@given(instance=afpText::ObjectClassification_strategy)
@settings(max_examples=50)
def test_afptext::objectclassification_instantiation(instance):
    assert isinstance(instance, afpText::ObjectClassification)

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_CompName_type(instance):
    assert isinstance(instance.CompName, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_CompName_setter(instance):
    original = instance.CompName
    instance.CompName = original
    assert instance.CompName == original

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_StrucFlgs_type(instance):
    assert isinstance(instance.StrucFlgs, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_StrucFlgs_setter(instance):
    original = instance.StrucFlgs
    instance.StrucFlgs = original
    assert instance.StrucFlgs == original

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjTpName_type(instance):
    assert isinstance(instance.ObjTpName, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjTpName_setter(instance):
    original = instance.ObjTpName
    instance.ObjTpName = original
    assert instance.ObjTpName == original

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjClass_type(instance):
    assert isinstance(instance.ObjClass, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjClass_setter(instance):
    original = instance.ObjClass
    instance.ObjClass = original
    assert instance.ObjClass == original

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_RegObjId_type(instance):
    assert isinstance(instance.RegObjId, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_RegObjId_setter(instance):
    original = instance.RegObjId
    instance.RegObjId = original
    assert instance.RegObjId == original

@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjLev_type(instance):
    assert isinstance(instance.ObjLev, str)


@given(instance=afpText::ObjectClassification_strategy)
def test_afptext::objectclassification_ObjLev_setter(instance):
    original = instance.ObjLev
    instance.ObjLev = original
    assert instance.ObjLev == original

@given(instance=afpText::IOCAFunctionSetIdentification_strategy)
@settings(max_examples=50)
def test_afptext::iocafunctionsetidentification_instantiation(instance):
    assert isinstance(instance, afpText::IOCAFunctionSetIdentification)

@given(instance=afpText::IOCAFunctionSetIdentification_strategy)
def test_afptext::iocafunctionsetidentification_CATEGORY_type(instance):
    assert isinstance(instance.CATEGORY, str)


@given(instance=afpText::IOCAFunctionSetIdentification_strategy)
def test_afptext::iocafunctionsetidentification_CATEGORY_setter(instance):
    original = instance.CATEGORY
    instance.CATEGORY = original
    assert instance.CATEGORY == original

@given(instance=afpText::IOCAFunctionSetIdentification_strategy)
def test_afptext::iocafunctionsetidentification_FCNSET_type(instance):
    assert isinstance(instance.FCNSET, str)


@given(instance=afpText::IOCAFunctionSetIdentification_strategy)
def test_afptext::iocafunctionsetidentification_FCNSET_setter(instance):
    original = instance.FCNSET
    instance.FCNSET = original
    assert instance.FCNSET == original

@given(instance=afpText::BandImageData_strategy)
@settings(max_examples=50)
def test_afptext::bandimagedata_instantiation(instance):
    assert isinstance(instance, afpText::BandImageData)

@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_RESERVED_type(instance):
    assert isinstance(instance.RESERVED, str)


@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_BANDNUM_type(instance):
    assert isinstance(instance.BANDNUM, str)


@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_BANDNUM_setter(instance):
    original = instance.BANDNUM
    instance.BANDNUM = original
    assert instance.BANDNUM == original

@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::BandImageData_strategy)
def test_afptext::bandimagedata_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::FontFidelity_strategy)
@settings(max_examples=50)
def test_afptext::fontfidelity_instantiation(instance):
    assert isinstance(instance, afpText::FontFidelity)

@given(instance=afpText::FontFidelity_strategy)
def test_afptext::fontfidelity_StpFntEx_type(instance):
    assert isinstance(instance.StpFntEx, str)


@given(instance=afpText::FontFidelity_strategy)
def test_afptext::fontfidelity_StpFntEx_setter(instance):
    original = instance.StpFntEx
    instance.StpFntEx = original
    assert instance.StpFntEx == original

@given(instance=afpText::BSU_strategy)
@settings(max_examples=50)
def test_afptext::bsu_instantiation(instance):
    assert isinstance(instance, afpText::BSU)

@given(instance=afpText::BSU_strategy)
def test_afptext::bsu_LID_type(instance):
    assert isinstance(instance.LID, str)


@given(instance=afpText::BSU_strategy)
def test_afptext::bsu_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText::TileSize_strategy)
@settings(max_examples=50)
def test_afptext::tilesize_instantiation(instance):
    assert isinstance(instance, afpText::TileSize)

@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_TVSIZE_type(instance):
    assert isinstance(instance.TVSIZE, str)


@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_TVSIZE_setter(instance):
    original = instance.TVSIZE
    instance.TVSIZE = original
    assert instance.TVSIZE == original

@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_THSIZE_type(instance):
    assert isinstance(instance.THSIZE, str)


@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_THSIZE_setter(instance):
    original = instance.THSIZE
    instance.THSIZE = original
    assert instance.THSIZE == original

@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_RELRES_type(instance):
    assert isinstance(instance.RELRES, str)


@given(instance=afpText::TileSize_strategy)
def test_afptext::tilesize_RELRES_setter(instance):
    original = instance.RELRES
    instance.RELRES = original
    assert instance.RELRES == original

@given(instance=afpText::DrawingOrderSubset_strategy)
@settings(max_examples=50)
def test_afptext::drawingordersubset_instantiation(instance):
    assert isinstance(instance, afpText::DrawingOrderSubset)

@given(instance=afpText::WindowSpecification_strategy)
@settings(max_examples=50)
def test_afptext::windowspecification_instantiation(instance):
    assert isinstance(instance, afpText::WindowSpecification)

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YTWIND_type(instance):
    assert isinstance(instance.YTWIND, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YTWIND_setter(instance):
    original = instance.YTWIND
    instance.YTWIND = original
    assert instance.YTWIND == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_FLAGS_type(instance):
    assert isinstance(instance.FLAGS, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_RES3_type(instance):
    assert isinstance(instance.RES3, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_RES3_setter(instance):
    original = instance.RES3
    instance.RES3 = original
    assert instance.RES3 == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XRESOL_type(instance):
    assert isinstance(instance.XRESOL, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XRESOL_setter(instance):
    original = instance.XRESOL
    instance.XRESOL = original
    assert instance.XRESOL == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_IMGXYRES_type(instance):
    assert isinstance(instance.IMGXYRES, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_IMGXYRES_setter(instance):
    original = instance.IMGXYRES
    instance.IMGXYRES = original
    assert instance.IMGXYRES == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XLWIND_type(instance):
    assert isinstance(instance.XLWIND, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XLWIND_setter(instance):
    original = instance.XLWIND
    instance.XLWIND = original
    assert instance.XLWIND == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_UBASE_type(instance):
    assert isinstance(instance.UBASE, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_UBASE_setter(instance):
    original = instance.UBASE
    instance.UBASE = original
    assert instance.UBASE == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YBWIND_type(instance):
    assert isinstance(instance.YBWIND, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YBWIND_setter(instance):
    original = instance.YBWIND
    instance.YBWIND = original
    assert instance.YBWIND == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XRWIND_type(instance):
    assert isinstance(instance.XRWIND, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_XRWIND_setter(instance):
    original = instance.XRWIND
    instance.XRWIND = original
    assert instance.XRWIND == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_CFORMAT_type(instance):
    assert isinstance(instance.CFORMAT, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_CFORMAT_setter(instance):
    original = instance.CFORMAT
    instance.CFORMAT = original
    assert instance.CFORMAT == original

@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YRESOL_type(instance):
    assert isinstance(instance.YRESOL, str)


@given(instance=afpText::WindowSpecification_strategy)
def test_afptext::windowspecification_YRESOL_setter(instance):
    original = instance.YRESOL
    instance.YRESOL = original
    assert instance.YRESOL == original

@given(instance=afpText::TilePosition_strategy)
@settings(max_examples=50)
def test_afptext::tileposition_instantiation(instance):
    assert isinstance(instance, afpText::TilePosition)

@given(instance=afpText::TilePosition_strategy)
def test_afptext::tileposition_XOFFSET_type(instance):
    assert isinstance(instance.XOFFSET, str)


@given(instance=afpText::TilePosition_strategy)
def test_afptext::tileposition_XOFFSET_setter(instance):
    original = instance.XOFFSET
    instance.XOFFSET = original
    assert instance.XOFFSET == original

@given(instance=afpText::TilePosition_strategy)
def test_afptext::tileposition_YOFFSET_type(instance):
    assert isinstance(instance.YOFFSET, str)


@given(instance=afpText::TilePosition_strategy)
def test_afptext::tileposition_YOFFSET_setter(instance):
    original = instance.YOFFSET
    instance.YOFFSET = original
    assert instance.YOFFSET == original

@given(instance=afpText::GCLINE_strategy)
@settings(max_examples=50)
def test_afptext::gcline_instantiation(instance):
    assert isinstance(instance, afpText::GCLINE)

@given(instance=afpText::GSPT_strategy)
@settings(max_examples=50)
def test_afptext::gspt_instantiation(instance):
    assert isinstance(instance, afpText::GSPT)

@given(instance=afpText::GSPT_strategy)
def test_afptext::gspt_PATT_type(instance):
    assert isinstance(instance.PATT, str)


@given(instance=afpText::GSPT_strategy)
def test_afptext::gspt_PATT_setter(instance):
    original = instance.PATT
    instance.PATT = original
    assert instance.PATT == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
@settings(max_examples=50)
def test_afptext::fontdescriptorspecification_instantiation(instance):
    assert isinstance(instance, afpText::FontDescriptorSpecification)

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWidth_type(instance):
    assert isinstance(instance.FtWidth, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWidth_setter(instance):
    original = instance.FtWidth
    instance.FtWidth = original
    assert instance.FtWidth == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtHeight_type(instance):
    assert isinstance(instance.FtHeight, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtHeight_setter(instance):
    original = instance.FtHeight
    instance.FtHeight = original
    assert instance.FtHeight == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtUsFlags_type(instance):
    assert isinstance(instance.FtUsFlags, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtUsFlags_setter(instance):
    original = instance.FtUsFlags
    instance.FtUsFlags = original
    assert instance.FtUsFlags == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtDsFlags_type(instance):
    assert isinstance(instance.FtDsFlags, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtDsFlags_setter(instance):
    original = instance.FtDsFlags
    instance.FtDsFlags = original
    assert instance.FtDsFlags == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWdClass_type(instance):
    assert isinstance(instance.FtWdClass, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWdClass_setter(instance):
    original = instance.FtWdClass
    instance.FtWdClass = original
    assert instance.FtWdClass == original

@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWtClass_type(instance):
    assert isinstance(instance.FtWtClass, str)


@given(instance=afpText::FontDescriptorSpecification_strategy)
def test_afptext::fontdescriptorspecification_FtWtClass_setter(instance):
    original = instance.FtWtClass
    instance.FtWtClass = original
    assert instance.FtWtClass == original

@given(instance=afpText::BeginSegmentCommand_strategy)
@settings(max_examples=50)
def test_afptext::beginsegmentcommand_instantiation(instance):
    assert isinstance(instance, afpText::BeginSegmentCommand)

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_FLAG2_type(instance):
    assert isinstance(instance.FLAG2, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_FLAG2_setter(instance):
    original = instance.FLAG2
    instance.FLAG2 = original
    assert instance.FLAG2 == original

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_PSNAME_type(instance):
    assert isinstance(instance.PSNAME, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_PSNAME_setter(instance):
    original = instance.PSNAME
    instance.PSNAME = original
    assert instance.PSNAME == original

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_FLAG1_type(instance):
    assert isinstance(instance.FLAG1, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_FLAG1_setter(instance):
    original = instance.FLAG1
    instance.FLAG1 = original
    assert instance.FLAG1 == original

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_NAME_type(instance):
    assert isinstance(instance.NAME, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_LENGTH_type(instance):
    assert isinstance(instance.LENGTH, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_LENGTH_setter(instance):
    original = instance.LENGTH
    instance.LENGTH = original
    assert instance.LENGTH == original

@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_SEGL_type(instance):
    assert isinstance(instance.SEGL, str)


@given(instance=afpText::BeginSegmentCommand_strategy)
def test_afptext::beginsegmentcommand_SEGL_setter(instance):
    original = instance.SEGL
    instance.SEGL = original
    assert instance.SEGL == original

@given(instance=afpText::DeviceAppearance_strategy)
@settings(max_examples=50)
def test_afptext::deviceappearance_instantiation(instance):
    assert isinstance(instance, afpText::DeviceAppearance)

@given(instance=afpText::DeviceAppearance_strategy)
def test_afptext::deviceappearance_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::DeviceAppearance_strategy)
def test_afptext::deviceappearance_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::DeviceAppearance_strategy)
def test_afptext::deviceappearance_DevApp_type(instance):
    assert isinstance(instance.DevApp, str)


@given(instance=afpText::DeviceAppearance_strategy)
def test_afptext::deviceappearance_DevApp_setter(instance):
    original = instance.DevApp
    instance.DevApp = original
    assert instance.DevApp == original

@given(instance=afpText::IncludeTile_strategy)
@settings(max_examples=50)
def test_afptext::includetile_instantiation(instance):
    assert isinstance(instance, afpText::IncludeTile)

@given(instance=afpText::IncludeTile_strategy)
def test_afptext::includetile_TIRID_type(instance):
    assert isinstance(instance.TIRID, str)


@given(instance=afpText::IncludeTile_strategy)
def test_afptext::includetile_TIRID_setter(instance):
    original = instance.TIRID
    instance.TIRID = original
    assert instance.TIRID == original

@given(instance=afpText::TextFidelity_strategy)
@settings(max_examples=50)
def test_afptext::textfidelity_instantiation(instance):
    assert isinstance(instance, afpText::TextFidelity)

@given(instance=afpText::TextFidelity_strategy)
def test_afptext::textfidelity_StpTxtEx_type(instance):
    assert isinstance(instance.StpTxtEx, str)


@given(instance=afpText::TextFidelity_strategy)
def test_afptext::textfidelity_StpTxtEx_setter(instance):
    original = instance.StpTxtEx
    instance.StpTxtEx = original
    assert instance.StpTxtEx == original

@given(instance=afpText::TextFidelity_strategy)
def test_afptext::textfidelity_RepTxtEx_type(instance):
    assert isinstance(instance.RepTxtEx, str)


@given(instance=afpText::TextFidelity_strategy)
def test_afptext::textfidelity_RepTxtEx_setter(instance):
    original = instance.RepTxtEx
    instance.RepTxtEx = original
    assert instance.RepTxtEx == original

@given(instance=afpText::CRCResourceManagement_strategy)
@settings(max_examples=50)
def test_afptext::crcresourcemanagement_instantiation(instance):
    assert isinstance(instance, afpText::CRCResourceManagement)

@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_ResClassFlg_type(instance):
    assert isinstance(instance.ResClassFlg, str)


@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_ResClassFlg_setter(instance):
    original = instance.ResClassFlg
    instance.ResClassFlg = original
    assert instance.ResClassFlg == original

@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_FmtQual_type(instance):
    assert isinstance(instance.FmtQual, str)


@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_FmtQual_setter(instance):
    original = instance.FmtQual
    instance.FmtQual = original
    assert instance.FmtQual == original

@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_RMValue_type(instance):
    assert isinstance(instance.RMValue, str)


@given(instance=afpText::CRCResourceManagement_strategy)
def test_afptext::crcresourcemanagement_RMValue_setter(instance):
    original = instance.RMValue
    instance.RMValue = original
    assert instance.RMValue == original

@given(instance=afpText::PageOverlayConditionalProcessing_strategy)
@settings(max_examples=50)
def test_afptext::pageoverlayconditionalprocessing_instantiation(instance):
    assert isinstance(instance, afpText::PageOverlayConditionalProcessing)

@given(instance=afpText::PageOverlayConditionalProcessing_strategy)
def test_afptext::pageoverlayconditionalprocessing_PgOvType_type(instance):
    assert isinstance(instance.PgOvType, str)


@given(instance=afpText::PageOverlayConditionalProcessing_strategy)
def test_afptext::pageoverlayconditionalprocessing_PgOvType_setter(instance):
    original = instance.PgOvType
    instance.PgOvType = original
    assert instance.PgOvType == original

@given(instance=afpText::PageOverlayConditionalProcessing_strategy)
def test_afptext::pageoverlayconditionalprocessing_Level_type(instance):
    assert isinstance(instance.Level, str)


@given(instance=afpText::PageOverlayConditionalProcessing_strategy)
def test_afptext::pageoverlayconditionalprocessing_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=afpText::GPARC_strategy)
@settings(max_examples=50)
def test_afptext::gparc_instantiation(instance):
    assert isinstance(instance, afpText::GPARC)

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_SWEEP_type(instance):
    assert isinstance(instance.SWEEP, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_SWEEP_setter(instance):
    original = instance.SWEEP
    instance.SWEEP = original
    assert instance.SWEEP == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_START_type(instance):
    assert isinstance(instance.START, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_START_setter(instance):
    original = instance.START
    instance.START = original
    assert instance.START == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_XCENT_type(instance):
    assert isinstance(instance.XCENT, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_XCENT_setter(instance):
    original = instance.XCENT
    instance.XCENT = original
    assert instance.XCENT == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_MFR_type(instance):
    assert isinstance(instance.MFR, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_YCENT_type(instance):
    assert isinstance(instance.YCENT, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_YCENT_setter(instance):
    original = instance.YCENT
    instance.YCENT = original
    assert instance.YCENT == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GPARC_strategy)
def test_afptext::gparc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::ImageSubsampling_strategy)
@settings(max_examples=50)
def test_afptext::imagesubsampling_instantiation(instance):
    assert isinstance(instance, afpText::ImageSubsampling)

@given(instance=afpText::TileSetColor_strategy)
@settings(max_examples=50)
def test_afptext::tilesetcolor_instantiation(instance):
    assert isinstance(instance, afpText::TileSetColor)

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_RESERVED_type(instance):
    assert isinstance(instance.RESERVED, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE3_type(instance):
    assert isinstance(instance.SIZE3, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE3_setter(instance):
    original = instance.SIZE3
    instance.SIZE3 = original
    assert instance.SIZE3 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL2_type(instance):
    assert isinstance(instance.CVAL2, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL2_setter(instance):
    original = instance.CVAL2
    instance.CVAL2 = original
    assert instance.CVAL2 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE4_type(instance):
    assert isinstance(instance.SIZE4, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE4_setter(instance):
    original = instance.SIZE4
    instance.SIZE4 = original
    assert instance.SIZE4 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL3_type(instance):
    assert isinstance(instance.CVAL3, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL3_setter(instance):
    original = instance.CVAL3
    instance.CVAL3 = original
    assert instance.CVAL3 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE1_type(instance):
    assert isinstance(instance.SIZE1, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE1_setter(instance):
    original = instance.SIZE1
    instance.SIZE1 = original
    assert instance.SIZE1 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL4_type(instance):
    assert isinstance(instance.CVAL4, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL4_setter(instance):
    original = instance.CVAL4
    instance.CVAL4 = original
    assert instance.CVAL4 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CSPACE_type(instance):
    assert isinstance(instance.CSPACE, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CSPACE_setter(instance):
    original = instance.CSPACE
    instance.CSPACE = original
    assert instance.CSPACE == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL1_type(instance):
    assert isinstance(instance.CVAL1, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_CVAL1_setter(instance):
    original = instance.CVAL1
    instance.CVAL1 = original
    assert instance.CVAL1 == original

@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE2_type(instance):
    assert isinstance(instance.SIZE2, str)


@given(instance=afpText::TileSetColor_strategy)
def test_afptext::tilesetcolor_SIZE2_setter(instance):
    original = instance.SIZE2
    instance.SIZE2 = original
    assert instance.SIZE2 == original

@given(instance=afpText::GSMT_strategy)
@settings(max_examples=50)
def test_afptext::gsmt_instantiation(instance):
    assert isinstance(instance, afpText::GSMT)

@given(instance=afpText::GSMT_strategy)
def test_afptext::gsmt_MCPT_type(instance):
    assert isinstance(instance.MCPT, str)


@given(instance=afpText::GSMT_strategy)
def test_afptext::gsmt_MCPT_setter(instance):
    original = instance.MCPT
    instance.MCPT = original
    assert instance.MCPT == original

@given(instance=afpText::FontHorizontalScaleFactor_strategy)
@settings(max_examples=50)
def test_afptext::fonthorizontalscalefactor_instantiation(instance):
    assert isinstance(instance, afpText::FontHorizontalScaleFactor)

@given(instance=afpText::FontHorizontalScaleFactor_strategy)
def test_afptext::fonthorizontalscalefactor_Hscale_type(instance):
    assert isinstance(instance.Hscale, str)


@given(instance=afpText::FontHorizontalScaleFactor_strategy)
def test_afptext::fonthorizontalscalefactor_Hscale_setter(instance):
    original = instance.Hscale
    instance.Hscale = original
    assert instance.Hscale == original

@given(instance=afpText::GCRLINE_strategy)
@settings(max_examples=50)
def test_afptext::gcrline_instantiation(instance):
    assert isinstance(instance, afpText::GCRLINE)

@given(instance=afpText::CMRFidelity_strategy)
@settings(max_examples=50)
def test_afptext::cmrfidelity_instantiation(instance):
    assert isinstance(instance, afpText::CMRFidelity)

@given(instance=afpText::CMRFidelity_strategy)
def test_afptext::cmrfidelity_RepCMREx_type(instance):
    assert isinstance(instance.RepCMREx, str)


@given(instance=afpText::CMRFidelity_strategy)
def test_afptext::cmrfidelity_RepCMREx_setter(instance):
    original = instance.RepCMREx
    instance.RepCMREx = original
    assert instance.RepCMREx == original

@given(instance=afpText::CMRFidelity_strategy)
def test_afptext::cmrfidelity_StpCMREx_type(instance):
    assert isinstance(instance.StpCMREx, str)


@given(instance=afpText::CMRFidelity_strategy)
def test_afptext::cmrfidelity_StpCMREx_setter(instance):
    original = instance.StpCMREx
    instance.StpCMREx = original
    assert instance.StpCMREx == original

@given(instance=afpText::GCMRK_strategy)
@settings(max_examples=50)
def test_afptext::gcmrk_instantiation(instance):
    assert isinstance(instance, afpText::GCMRK)

@given(instance=afpText::ExtensionFont_strategy)
@settings(max_examples=50)
def test_afptext::extensionfont_instantiation(instance):
    assert isinstance(instance, afpText::ExtensionFont)

@given(instance=afpText::ExtensionFont_strategy)
def test_afptext::extensionfont_GCSGID_type(instance):
    assert isinstance(instance.GCSGID, str)


@given(instance=afpText::ExtensionFont_strategy)
def test_afptext::extensionfont_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText::EndTransparencyMask_strategy)
@settings(max_examples=50)
def test_afptext::endtransparencymask_instantiation(instance):
    assert isinstance(instance, afpText::EndTransparencyMask)

@given(instance=afpText::MediumOrientation_strategy)
@settings(max_examples=50)
def test_afptext::mediumorientation_instantiation(instance):
    assert isinstance(instance, afpText::MediumOrientation)

@given(instance=afpText::MediumOrientation_strategy)
def test_afptext::mediumorientation_MedOrient_type(instance):
    assert isinstance(instance.MedOrient, str)


@given(instance=afpText::MediumOrientation_strategy)
def test_afptext::mediumorientation_MedOrient_setter(instance):
    original = instance.MedOrient
    instance.MedOrient = original
    assert instance.MedOrient == original

@given(instance=afpText::GMRK_strategy)
@settings(max_examples=50)
def test_afptext::gmrk_instantiation(instance):
    assert isinstance(instance, afpText::GMRK)

@given(instance=afpText::ImageResolution_strategy)
@settings(max_examples=50)
def test_afptext::imageresolution_instantiation(instance):
    assert isinstance(instance, afpText::ImageResolution)

@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_XBase_type(instance):
    assert isinstance(instance.XBase, str)


@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_XBase_setter(instance):
    original = instance.XBase
    instance.XBase = original
    assert instance.XBase == original

@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_YBase_type(instance):
    assert isinstance(instance.YBase, str)


@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_YBase_setter(instance):
    original = instance.YBase
    instance.YBase = original
    assert instance.YBase == original

@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_XResol_type(instance):
    assert isinstance(instance.XResol, str)


@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_XResol_setter(instance):
    original = instance.XResol
    instance.XResol = original
    assert instance.XResol == original

@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_YResol_type(instance):
    assert isinstance(instance.YResol, str)


@given(instance=afpText::ImageResolution_strategy)
def test_afptext::imageresolution_YResol_setter(instance):
    original = instance.YResol
    instance.YResol = original
    assert instance.YResol == original

@given(instance=afpText::EndSegment_strategy)
@settings(max_examples=50)
def test_afptext::endsegment_instantiation(instance):
    assert isinstance(instance, afpText::EndSegment)

@given(instance=afpText::MediumMapPageNumber_strategy)
@settings(max_examples=50)
def test_afptext::mediummappagenumber_instantiation(instance):
    assert isinstance(instance, afpText::MediumMapPageNumber)

@given(instance=afpText::MediumMapPageNumber_strategy)
def test_afptext::mediummappagenumber_PageNum_type(instance):
    assert isinstance(instance.PageNum, str)


@given(instance=afpText::MediumMapPageNumber_strategy)
def test_afptext::mediummappagenumber_PageNum_setter(instance):
    original = instance.PageNum
    instance.PageNum = original
    assert instance.PageNum == original

@given(instance=afpText::GCFLT_strategy)
@settings(max_examples=50)
def test_afptext::gcflt_instantiation(instance):
    assert isinstance(instance, afpText::GCFLT)

@given(instance=afpText::SamplingRatios_strategy)
@settings(max_examples=50)
def test_afptext::samplingratios_instantiation(instance):
    assert isinstance(instance, afpText::SamplingRatios)

@given(instance=afpText::GSCR_strategy)
@settings(max_examples=50)
def test_afptext::gscr_instantiation(instance):
    assert isinstance(instance, afpText::GSCR)

@given(instance=afpText::GSCR_strategy)
def test_afptext::gscr_PREC_type(instance):
    assert isinstance(instance.PREC, str)


@given(instance=afpText::GSCR_strategy)
def test_afptext::gscr_PREC_setter(instance):
    original = instance.PREC
    instance.PREC = original
    assert instance.PREC == original

@given(instance=afpText::GSCC_strategy)
@settings(max_examples=50)
def test_afptext::gscc_instantiation(instance):
    assert isinstance(instance, afpText::GSCC)

@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLHFR_type(instance):
    assert isinstance(instance.CELLHFR, str)


@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLHFR_setter(instance):
    original = instance.CELLHFR
    instance.CELLHFR = original
    assert instance.CELLHFR == original

@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLWI_type(instance):
    assert isinstance(instance.CELLWI, str)


@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLWI_setter(instance):
    original = instance.CELLWI
    instance.CELLWI = original
    assert instance.CELLWI == original

@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLWFR_type(instance):
    assert isinstance(instance.CELLWFR, str)


@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLWFR_setter(instance):
    original = instance.CELLWFR
    instance.CELLWFR = original
    assert instance.CELLWFR == original

@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLHI_type(instance):
    assert isinstance(instance.CELLHI, str)


@given(instance=afpText::GSCC_strategy)
def test_afptext::gscc_CELLHI_setter(instance):
    original = instance.CELLHI
    instance.CELLHI = original
    assert instance.CELLHI == original

@given(instance=afpText::MappingOption_strategy)
@settings(max_examples=50)
def test_afptext::mappingoption_instantiation(instance):
    assert isinstance(instance, afpText::MappingOption)

@given(instance=afpText::MappingOption_strategy)
def test_afptext::mappingoption_MapValue_type(instance):
    assert isinstance(instance.MapValue, str)


@given(instance=afpText::MappingOption_strategy)
def test_afptext::mappingoption_MapValue_setter(instance):
    original = instance.MapValue
    instance.MapValue = original
    assert instance.MapValue == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
@settings(max_examples=50)
def test_afptext::localdateandtimestamp_instantiation(instance):
    assert isinstance(instance, afpText::LocalDateAndTimeStamp)

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Hour_type(instance):
    assert isinstance(instance.Hour, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Hour_setter(instance):
    original = instance.Hour
    instance.Hour = original
    assert instance.Hour == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Minute_type(instance):
    assert isinstance(instance.Minute, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Minute_setter(instance):
    original = instance.Minute
    instance.Minute = original
    assert instance.Minute == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_HundSec_type(instance):
    assert isinstance(instance.HundSec, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_HundSec_setter(instance):
    original = instance.HundSec
    instance.HundSec = original
    assert instance.HundSec == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Day_type(instance):
    assert isinstance(instance.Day, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_THunYear_type(instance):
    assert isinstance(instance.THunYear, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_THunYear_setter(instance):
    original = instance.THunYear
    instance.THunYear = original
    assert instance.THunYear == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_StampType_type(instance):
    assert isinstance(instance.StampType, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_StampType_setter(instance):
    original = instance.StampType
    instance.StampType = original
    assert instance.StampType == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_TenYear_type(instance):
    assert isinstance(instance.TenYear, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_TenYear_setter(instance):
    original = instance.TenYear
    instance.TenYear = original
    assert instance.TenYear == original

@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Second_type(instance):
    assert isinstance(instance.Second, str)


@given(instance=afpText::LocalDateAndTimeStamp_strategy)
def test_afptext::localdateandtimestamp_Second_setter(instance):
    original = instance.Second
    instance.Second = original
    assert instance.Second == original

@given(instance=afpText::GSCA_strategy)
@settings(max_examples=50)
def test_afptext::gsca_instantiation(instance):
    assert isinstance(instance, afpText::GSCA)

@given(instance=afpText::GSCA_strategy)
def test_afptext::gsca_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GSCA_strategy)
def test_afptext::gsca_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GSCA_strategy)
def test_afptext::gsca_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GSCA_strategy)
def test_afptext::gsca_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::ObjectOffset_strategy)
@settings(max_examples=50)
def test_afptext::objectoffset_instantiation(instance):
    assert isinstance(instance, afpText::ObjectOffset)

@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjOset_type(instance):
    assert isinstance(instance.ObjOset, str)


@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjOset_setter(instance):
    original = instance.ObjOset
    instance.ObjOset = original
    assert instance.ObjOset == original

@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjTpe_type(instance):
    assert isinstance(instance.ObjTpe, str)


@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjTpe_setter(instance):
    original = instance.ObjTpe
    instance.ObjTpe = original
    assert instance.ObjTpe == original

@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjOstHi_type(instance):
    assert isinstance(instance.ObjOstHi, str)


@given(instance=afpText::ObjectOffset_strategy)
def test_afptext::objectoffset_ObjOstHi_setter(instance):
    original = instance.ObjOstHi
    instance.ObjOstHi = original
    assert instance.ObjOstHi == original

@given(instance=afpText::FullyQualifiedName_strategy)
@settings(max_examples=50)
def test_afptext::fullyqualifiedname_instantiation(instance):
    assert isinstance(instance, afpText::FullyQualifiedName)

@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQNFormat_type(instance):
    assert isinstance(instance.FQNFormat, str)


@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQNFormat_setter(instance):
    original = instance.FQNFormat
    instance.FQNFormat = original
    assert instance.FQNFormat == original

@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQNType_type(instance):
    assert isinstance(instance.FQNType, str)


@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQNType_setter(instance):
    original = instance.FQNType
    instance.FQNType = original
    assert instance.FQNType == original

@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQName_type(instance):
    assert isinstance(instance.FQName, str)


@given(instance=afpText::FullyQualifiedName_strategy)
def test_afptext::fullyqualifiedname_FQName_setter(instance):
    original = instance.FQName
    instance.FQName = original
    assert instance.FQName == original

@given(instance=afpText::ImageData_strategy)
@settings(max_examples=50)
def test_afptext::imagedata_instantiation(instance):
    assert isinstance(instance, afpText::ImageData)

@given(instance=afpText::ImageData_strategy)
def test_afptext::imagedata_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::ImageData_strategy)
def test_afptext::imagedata_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::ObjectOriginIdentifier_strategy)
@settings(max_examples=50)
def test_afptext::objectoriginidentifier_instantiation(instance):
    assert isinstance(instance, afpText::ObjectOriginIdentifier)

@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_MedID_type(instance):
    assert isinstance(instance.MedID, str)


@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_MedID_setter(instance):
    original = instance.MedID
    instance.MedID = original
    assert instance.MedID == original

@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_System_type(instance):
    assert isinstance(instance.System, str)


@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_System_setter(instance):
    original = instance.System
    instance.System = original
    assert instance.System == original

@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_DSID_type(instance):
    assert isinstance(instance.DSID, str)


@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_DSID_setter(instance):
    original = instance.DSID
    instance.DSID = original
    assert instance.DSID == original

@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_SysID_type(instance):
    assert isinstance(instance.SysID, str)


@given(instance=afpText::ObjectOriginIdentifier_strategy)
def test_afptext::objectoriginidentifier_SysID_setter(instance):
    original = instance.SysID
    instance.SysID = original
    assert instance.SysID == original

@given(instance=afpText::GSLJ_strategy)
@settings(max_examples=50)
def test_afptext::gslj_instantiation(instance):
    assert isinstance(instance, afpText::GSLJ)

@given(instance=afpText::GSLJ_strategy)
def test_afptext::gslj_LINEJOIN_type(instance):
    assert isinstance(instance.LINEJOIN, str)


@given(instance=afpText::GSLJ_strategy)
def test_afptext::gslj_LINEJOIN_setter(instance):
    original = instance.LINEJOIN
    instance.LINEJOIN = original
    assert instance.LINEJOIN == original

@given(instance=afpText::GFLT_strategy)
@settings(max_examples=50)
def test_afptext::gflt_instantiation(instance):
    assert isinstance(instance, afpText::GFLT)

@given(instance=afpText::GSLE_strategy)
@settings(max_examples=50)
def test_afptext::gsle_instantiation(instance):
    assert isinstance(instance, afpText::GSLE)

@given(instance=afpText::GSLE_strategy)
def test_afptext::gsle_LINEEND_type(instance):
    assert isinstance(instance.LINEEND, str)


@given(instance=afpText::GSLE_strategy)
def test_afptext::gsle_LINEEND_setter(instance):
    original = instance.LINEEND
    instance.LINEEND = original
    assert instance.LINEEND == original

@given(instance=afpText::GFARC_strategy)
@settings(max_examples=50)
def test_afptext::gfarc_instantiation(instance):
    assert isinstance(instance, afpText::GFARC)

@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_MFR_type(instance):
    assert isinstance(instance.MFR, str)


@given(instance=afpText::GFARC_strategy)
def test_afptext::gfarc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText::ImageLUTID_strategy)
@settings(max_examples=50)
def test_afptext::imagelutid_instantiation(instance):
    assert isinstance(instance, afpText::ImageLUTID)

@given(instance=afpText::ImageLUTID_strategy)
def test_afptext::imagelutid_LUTID_type(instance):
    assert isinstance(instance.LUTID, str)


@given(instance=afpText::ImageLUTID_strategy)
def test_afptext::imagelutid_LUTID_setter(instance):
    original = instance.LUTID
    instance.LUTID = original
    assert instance.LUTID == original

@given(instance=afpText::GEIMG_strategy)
@settings(max_examples=50)
def test_afptext::geimg_instantiation(instance):
    assert isinstance(instance, afpText::GEIMG)

@given(instance=afpText::GEIMG_strategy)
def test_afptext::geimg_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::GEIMG_strategy)
def test_afptext::geimg_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::MediaFidelity_strategy)
@settings(max_examples=50)
def test_afptext::mediafidelity_instantiation(instance):
    assert isinstance(instance, afpText::MediaFidelity)

@given(instance=afpText::MediaFidelity_strategy)
def test_afptext::mediafidelity_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::MediaFidelity_strategy)
def test_afptext::mediafidelity_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::MediaFidelity_strategy)
def test_afptext::mediafidelity_StpMedEx_type(instance):
    assert isinstance(instance.StpMedEx, str)


@given(instance=afpText::MediaFidelity_strategy)
def test_afptext::mediafidelity_StpMedEx_setter(instance):
    original = instance.StpMedEx
    instance.StpMedEx = original
    assert instance.StpMedEx == original

@given(instance=afpText::MODCAInterchangeSet_strategy)
@settings(max_examples=50)
def test_afptext::modcainterchangeset_instantiation(instance):
    assert isinstance(instance, afpText::MODCAInterchangeSet)

@given(instance=afpText::MODCAInterchangeSet_strategy)
def test_afptext::modcainterchangeset_ISid_type(instance):
    assert isinstance(instance.ISid, str)


@given(instance=afpText::MODCAInterchangeSet_strategy)
def test_afptext::modcainterchangeset_ISid_setter(instance):
    original = instance.ISid
    instance.ISid = original
    assert instance.ISid == original

@given(instance=afpText::MODCAInterchangeSet_strategy)
def test_afptext::modcainterchangeset_IStype_type(instance):
    assert isinstance(instance.IStype, str)


@given(instance=afpText::MODCAInterchangeSet_strategy)
def test_afptext::modcainterchangeset_IStype_setter(instance):
    original = instance.IStype
    instance.IStype = original
    assert instance.IStype == original

@given(instance=afpText::GRLINE_strategy)
@settings(max_examples=50)
def test_afptext::grline_instantiation(instance):
    assert isinstance(instance, afpText::GRLINE)

@given(instance=afpText::GRLINE_strategy)
def test_afptext::grline_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GRLINE_strategy)
def test_afptext::grline_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GRLINE_strategy)
def test_afptext::grline_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GRLINE_strategy)
def test_afptext::grline_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::EndSegmentCommand_strategy)
@settings(max_examples=50)
def test_afptext::endsegmentcommand_instantiation(instance):
    assert isinstance(instance, afpText::EndSegmentCommand)

@given(instance=afpText::GCBOX_strategy)
@settings(max_examples=50)
def test_afptext::gcbox_instantiation(instance):
    assert isinstance(instance, afpText::GCBOX)

@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_HAXIS_type(instance):
    assert isinstance(instance.HAXIS, str)


@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_HAXIS_setter(instance):
    original = instance.HAXIS
    instance.HAXIS = original
    assert instance.HAXIS == original

@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_XPOS1_type(instance):
    assert isinstance(instance.XPOS1, str)


@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_XPOS1_setter(instance):
    original = instance.XPOS1
    instance.XPOS1 = original
    assert instance.XPOS1 == original

@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_VAXIS_type(instance):
    assert isinstance(instance.VAXIS, str)


@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_VAXIS_setter(instance):
    original = instance.VAXIS
    instance.VAXIS = original
    assert instance.VAXIS == original

@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_RES_type(instance):
    assert isinstance(instance.RES, str)


@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_YPOS1_type(instance):
    assert isinstance(instance.YPOS1, str)


@given(instance=afpText::GCBOX_strategy)
def test_afptext::gcbox_YPOS1_setter(instance):
    original = instance.YPOS1
    instance.YPOS1 = original
    assert instance.YPOS1 == original

@given(instance=afpText::ObjectStructuredFieldExtent_strategy)
@settings(max_examples=50)
def test_afptext::objectstructuredfieldextent_instantiation(instance):
    assert isinstance(instance, afpText::ObjectStructuredFieldExtent)

@given(instance=afpText::ObjectStructuredFieldExtent_strategy)
def test_afptext::objectstructuredfieldextent_SFExtHi_type(instance):
    assert isinstance(instance.SFExtHi, str)


@given(instance=afpText::ObjectStructuredFieldExtent_strategy)
def test_afptext::objectstructuredfieldextent_SFExtHi_setter(instance):
    original = instance.SFExtHi
    instance.SFExtHi = original
    assert instance.SFExtHi == original

@given(instance=afpText::ObjectStructuredFieldExtent_strategy)
def test_afptext::objectstructuredfieldextent_SFExt_type(instance):
    assert isinstance(instance.SFExt, str)


@given(instance=afpText::ObjectStructuredFieldExtent_strategy)
def test_afptext::objectstructuredfieldextent_SFExt_setter(instance):
    original = instance.SFExt
    instance.SFExt = original
    assert instance.SFExt == original

@given(instance=afpText::BeginTile_strategy)
@settings(max_examples=50)
def test_afptext::begintile_instantiation(instance):
    assert isinstance(instance, afpText::BeginTile)

@given(instance=afpText::GCPARC_strategy)
@settings(max_examples=50)
def test_afptext::gcparc_instantiation(instance):
    assert isinstance(instance, afpText::GCPARC)

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_XCENT_type(instance):
    assert isinstance(instance.XCENT, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_XCENT_setter(instance):
    original = instance.XCENT
    instance.XCENT = original
    assert instance.XCENT == original

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_SWEEP_type(instance):
    assert isinstance(instance.SWEEP, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_SWEEP_setter(instance):
    original = instance.SWEEP
    instance.SWEEP = original
    assert instance.SWEEP == original

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_YCENT_type(instance):
    assert isinstance(instance.YCENT, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_YCENT_setter(instance):
    original = instance.YCENT
    instance.YCENT = original
    assert instance.YCENT == original

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_START_type(instance):
    assert isinstance(instance.START, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_START_setter(instance):
    original = instance.START
    instance.START = original
    assert instance.START == original

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_MFR_type(instance):
    assert isinstance(instance.MFR, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GCPARC_strategy)
def test_afptext::gcparc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::GNOP1_strategy)
@settings(max_examples=50)
def test_afptext::gnop1_instantiation(instance):
    assert isinstance(instance, afpText::GNOP1)

@given(instance=afpText::LocaleSelector_strategy)
@settings(max_examples=50)
def test_afptext::localeselector_instantiation(instance):
    assert isinstance(instance, afpText::LocaleSelector)

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_LangCode_type(instance):
    assert isinstance(instance.LangCode, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_LangCode_setter(instance):
    original = instance.LangCode
    instance.LangCode = original
    assert instance.LangCode == original

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_RegCde_type(instance):
    assert isinstance(instance.RegCde, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_RegCde_setter(instance):
    original = instance.RegCde
    instance.RegCde = original
    assert instance.RegCde == original

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_ScrptCde_type(instance):
    assert isinstance(instance.ScrptCde, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_ScrptCde_setter(instance):
    original = instance.ScrptCde
    instance.ScrptCde = original
    assert instance.ScrptCde == original

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_LocFlgs_type(instance):
    assert isinstance(instance.LocFlgs, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_LocFlgs_setter(instance):
    original = instance.LocFlgs
    instance.LocFlgs = original
    assert instance.LocFlgs == original

@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_VarCde_type(instance):
    assert isinstance(instance.VarCde, str)


@given(instance=afpText::LocaleSelector_strategy)
def test_afptext::localeselector_VarCde_setter(instance):
    original = instance.VarCde
    instance.VarCde = original
    assert instance.VarCde == original

@given(instance=afpText::RenderingIntent_strategy)
@settings(max_examples=50)
def test_afptext::renderingintent_instantiation(instance):
    assert isinstance(instance, afpText::RenderingIntent)

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_IOCARI_type(instance):
    assert isinstance(instance.IOCARI, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_IOCARI_setter(instance):
    original = instance.IOCARI
    instance.IOCARI = original
    assert instance.IOCARI == original

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_OCRI_type(instance):
    assert isinstance(instance.OCRI, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_OCRI_setter(instance):
    original = instance.OCRI
    instance.OCRI = original
    assert instance.OCRI == original

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_PTOCRI_type(instance):
    assert isinstance(instance.PTOCRI, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_PTOCRI_setter(instance):
    original = instance.PTOCRI
    instance.PTOCRI = original
    assert instance.PTOCRI == original

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_GOCARI_type(instance):
    assert isinstance(instance.GOCARI, str)


@given(instance=afpText::RenderingIntent_strategy)
def test_afptext::renderingintent_GOCARI_setter(instance):
    original = instance.GOCARI
    instance.GOCARI = original
    assert instance.GOCARI == original

@given(instance=afpText::PresentationSpaceResetMixing_strategy)
@settings(max_examples=50)
def test_afptext::presentationspaceresetmixing_instantiation(instance):
    assert isinstance(instance, afpText::PresentationSpaceResetMixing)

@given(instance=afpText::PresentationSpaceResetMixing_strategy)
def test_afptext::presentationspaceresetmixing_BgMxFlag_type(instance):
    assert isinstance(instance.BgMxFlag, str)


@given(instance=afpText::PresentationSpaceResetMixing_strategy)
def test_afptext::presentationspaceresetmixing_BgMxFlag_setter(instance):
    original = instance.BgMxFlag
    instance.BgMxFlag = original
    assert instance.BgMxFlag == original

@given(instance=afpText::UP3iFinishingOperation_strategy)
@settings(max_examples=50)
def test_afptext::up3ifinishingoperation_instantiation(instance):
    assert isinstance(instance, afpText::UP3iFinishingOperation)

@given(instance=afpText::UP3iFinishingOperation_strategy)
def test_afptext::up3ifinishingoperation_Seqnum_type(instance):
    assert isinstance(instance.Seqnum, str)


@given(instance=afpText::UP3iFinishingOperation_strategy)
def test_afptext::up3ifinishingoperation_Seqnum_setter(instance):
    original = instance.Seqnum
    instance.Seqnum = original
    assert instance.Seqnum == original

@given(instance=afpText::UP3iFinishingOperation_strategy)
def test_afptext::up3ifinishingoperation_UP3iDat_type(instance):
    assert isinstance(instance.UP3iDat, str)


@given(instance=afpText::UP3iFinishingOperation_strategy)
def test_afptext::up3ifinishingoperation_UP3iDat_setter(instance):
    original = instance.UP3iDat
    instance.UP3iDat = original
    assert instance.UP3iDat == original

@given(instance=afpText::GEAR_strategy)
@settings(max_examples=50)
def test_afptext::gear_instantiation(instance):
    assert isinstance(instance, afpText::GEAR)

@given(instance=afpText::GEAR_strategy)
def test_afptext::gear_DATA_type(instance):
    assert isinstance(instance.DATA, str)


@given(instance=afpText::GEAR_strategy)
def test_afptext::gear_DATA_setter(instance):
    original = instance.DATA
    instance.DATA = original
    assert instance.DATA == original

@given(instance=afpText::ResourceUsageAttribute_strategy)
@settings(max_examples=50)
def test_afptext::resourceusageattribute_instantiation(instance):
    assert isinstance(instance, afpText::ResourceUsageAttribute)

@given(instance=afpText::ResourceUsageAttribute_strategy)
def test_afptext::resourceusageattribute_Frequency_type(instance):
    assert isinstance(instance.Frequency, str)


@given(instance=afpText::ResourceUsageAttribute_strategy)
def test_afptext::resourceusageattribute_Frequency_setter(instance):
    original = instance.Frequency
    instance.Frequency = original
    assert instance.Frequency == original

@given(instance=afpText::GCFARC_strategy)
@settings(max_examples=50)
def test_afptext::gcfarc_instantiation(instance):
    assert isinstance(instance, afpText::GCFARC)

@given(instance=afpText::GCFARC_strategy)
def test_afptext::gcfarc_MFR_type(instance):
    assert isinstance(instance.MFR, str)


@given(instance=afpText::GCFARC_strategy)
def test_afptext::gcfarc_MFR_setter(instance):
    original = instance.MFR
    instance.MFR = original
    assert instance.MFR == original

@given(instance=afpText::GCFARC_strategy)
def test_afptext::gcfarc_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GCFARC_strategy)
def test_afptext::gcfarc_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::ImageSize_strategy)
@settings(max_examples=50)
def test_afptext::imagesize_instantiation(instance):
    assert isinstance(instance, afpText::ImageSize)

@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_UNITBASE_type(instance):
    assert isinstance(instance.UNITBASE, str)


@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_UNITBASE_setter(instance):
    original = instance.UNITBASE
    instance.UNITBASE = original
    assert instance.UNITBASE == original

@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_HSIZE_type(instance):
    assert isinstance(instance.HSIZE, str)


@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_HSIZE_setter(instance):
    original = instance.HSIZE
    instance.HSIZE = original
    assert instance.HSIZE == original

@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_VRESOL_type(instance):
    assert isinstance(instance.VRESOL, str)


@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_VRESOL_setter(instance):
    original = instance.VRESOL
    instance.VRESOL = original
    assert instance.VRESOL == original

@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_VSIZE_type(instance):
    assert isinstance(instance.VSIZE, str)


@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_VSIZE_setter(instance):
    original = instance.VSIZE
    instance.VSIZE = original
    assert instance.VSIZE == original

@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_HRESOL_type(instance):
    assert isinstance(instance.HRESOL, str)


@given(instance=afpText::ImageSize_strategy)
def test_afptext::imagesize_HRESOL_setter(instance):
    original = instance.HRESOL
    instance.HRESOL = original
    assert instance.HRESOL == original

@given(instance=afpText::PresentationSpaceMixingRules_strategy)
@settings(max_examples=50)
def test_afptext::presentationspacemixingrules_instantiation(instance):
    assert isinstance(instance, afpText::PresentationSpaceMixingRules)

@given(instance=afpText::ResourceObjectInclude_strategy)
@settings(max_examples=50)
def test_afptext::resourceobjectinclude_instantiation(instance):
    assert isinstance(instance, afpText::ResourceObjectInclude)

@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObjType_type(instance):
    assert isinstance(instance.ObjType, str)


@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_YobjOset_type(instance):
    assert isinstance(instance.YobjOset, str)


@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_YobjOset_setter(instance):
    original = instance.YobjOset
    instance.YobjOset = original
    assert instance.YobjOset == original

@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObOrent_type(instance):
    assert isinstance(instance.ObOrent, str)


@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObOrent_setter(instance):
    original = instance.ObOrent
    instance.ObOrent = original
    assert instance.ObOrent == original

@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObjName_type(instance):
    assert isinstance(instance.ObjName, str)


@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_ObjName_setter(instance):
    original = instance.ObjName
    instance.ObjName = original
    assert instance.ObjName == original

@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_XobjOset_type(instance):
    assert isinstance(instance.XobjOset, str)


@given(instance=afpText::ResourceObjectInclude_strategy)
def test_afptext::resourceobjectinclude_XobjOset_setter(instance):
    original = instance.XobjOset
    instance.XobjOset = original
    assert instance.XobjOset == original

@given(instance=afpText::IDEStructure_strategy)
@settings(max_examples=50)
def test_afptext::idestructure_instantiation(instance):
    assert isinstance(instance, afpText::IDEStructure)

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE2_type(instance):
    assert isinstance(instance.SIZE2, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE2_setter(instance):
    original = instance.SIZE2
    instance.SIZE2 = original
    assert instance.SIZE2 == original

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_FLAGS_type(instance):
    assert isinstance(instance.FLAGS, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_FLAGS_setter(instance):
    original = instance.FLAGS
    instance.FLAGS = original
    assert instance.FLAGS == original

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_FORMAT_type(instance):
    assert isinstance(instance.FORMAT, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE1_type(instance):
    assert isinstance(instance.SIZE1, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE1_setter(instance):
    original = instance.SIZE1
    instance.SIZE1 = original
    assert instance.SIZE1 == original

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE4_type(instance):
    assert isinstance(instance.SIZE4, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE4_setter(instance):
    original = instance.SIZE4
    instance.SIZE4 = original
    assert instance.SIZE4 == original

@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE3_type(instance):
    assert isinstance(instance.SIZE3, str)


@given(instance=afpText::IDEStructure_strategy)
def test_afptext::idestructure_SIZE3_setter(instance):
    original = instance.SIZE3
    instance.SIZE3 = original
    assert instance.SIZE3 == original

@given(instance=afpText::TextOrientation_strategy)
@settings(max_examples=50)
def test_afptext::textorientation_instantiation(instance):
    assert isinstance(instance, afpText::TextOrientation)

@given(instance=afpText::TextOrientation_strategy)
def test_afptext::textorientation_IAxis_type(instance):
    assert isinstance(instance.IAxis, str)


@given(instance=afpText::TextOrientation_strategy)
def test_afptext::textorientation_IAxis_setter(instance):
    original = instance.IAxis
    instance.IAxis = original
    assert instance.IAxis == original

@given(instance=afpText::TextOrientation_strategy)
def test_afptext::textorientation_BAxis_type(instance):
    assert isinstance(instance.BAxis, str)


@given(instance=afpText::TextOrientation_strategy)
def test_afptext::textorientation_BAxis_setter(instance):
    original = instance.BAxis
    instance.BAxis = original
    assert instance.BAxis == original

@given(instance=afpText::GLINE_strategy)
@settings(max_examples=50)
def test_afptext::gline_instantiation(instance):
    assert isinstance(instance, afpText::GLINE)

@given(instance=afpText::GSLW_strategy)
@settings(max_examples=50)
def test_afptext::gslw_instantiation(instance):
    assert isinstance(instance, afpText::GSLW)

@given(instance=afpText::GSLW_strategy)
def test_afptext::gslw_MH_type(instance):
    assert isinstance(instance.MH, str)


@given(instance=afpText::GSLW_strategy)
def test_afptext::gslw_MH_setter(instance):
    original = instance.MH
    instance.MH = original
    assert instance.MH == original

@given(instance=afpText::GSCD_strategy)
@settings(max_examples=50)
def test_afptext::gscd_instantiation(instance):
    assert isinstance(instance, afpText::GSCD)

@given(instance=afpText::GSCD_strategy)
def test_afptext::gscd_DIRECTION_type(instance):
    assert isinstance(instance.DIRECTION, str)


@given(instance=afpText::GSCD_strategy)
def test_afptext::gscd_DIRECTION_setter(instance):
    original = instance.DIRECTION
    instance.DIRECTION = original
    assert instance.DIRECTION == original

@given(instance=afpText::ObjectAreaSize_strategy)
@settings(max_examples=50)
def test_afptext::objectareasize_instantiation(instance):
    assert isinstance(instance, afpText::ObjectAreaSize)

@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_XoaSize_type(instance):
    assert isinstance(instance.XoaSize, str)


@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_XoaSize_setter(instance):
    original = instance.XoaSize
    instance.XoaSize = original
    assert instance.XoaSize == original

@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_YoaSize_type(instance):
    assert isinstance(instance.YoaSize, str)


@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_YoaSize_setter(instance):
    original = instance.YoaSize
    instance.YoaSize = original
    assert instance.YoaSize == original

@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_SizeType_type(instance):
    assert isinstance(instance.SizeType, str)


@given(instance=afpText::ObjectAreaSize_strategy)
def test_afptext::objectareasize_SizeType_setter(instance):
    original = instance.SizeType
    instance.SizeType = original
    assert instance.SizeType == original

@given(instance=afpText::GSCOL_strategy)
@settings(max_examples=50)
def test_afptext::gscol_instantiation(instance):
    assert isinstance(instance, afpText::GSCOL)

@given(instance=afpText::GSCOL_strategy)
def test_afptext::gscol_COL_type(instance):
    assert isinstance(instance.COL, str)


@given(instance=afpText::GSCOL_strategy)
def test_afptext::gscol_COL_setter(instance):
    original = instance.COL
    instance.COL = original
    assert instance.COL == original

@given(instance=afpText::GBOX_strategy)
@settings(max_examples=50)
def test_afptext::gbox_instantiation(instance):
    assert isinstance(instance, afpText::GBOX)

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_XPOS0_type(instance):
    assert isinstance(instance.XPOS0, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_XPOS0_setter(instance):
    original = instance.XPOS0
    instance.XPOS0 = original
    assert instance.XPOS0 == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_VAXIS_type(instance):
    assert isinstance(instance.VAXIS, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_VAXIS_setter(instance):
    original = instance.VAXIS
    instance.VAXIS = original
    assert instance.VAXIS == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_YPOS1_type(instance):
    assert isinstance(instance.YPOS1, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_YPOS1_setter(instance):
    original = instance.YPOS1
    instance.YPOS1 = original
    assert instance.YPOS1 == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_HAXIS_type(instance):
    assert isinstance(instance.HAXIS, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_HAXIS_setter(instance):
    original = instance.HAXIS
    instance.HAXIS = original
    assert instance.HAXIS == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_XPOS1_type(instance):
    assert isinstance(instance.XPOS1, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_XPOS1_setter(instance):
    original = instance.XPOS1
    instance.XPOS1 = original
    assert instance.XPOS1 == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_YPOS0_type(instance):
    assert isinstance(instance.YPOS0, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_YPOS0_setter(instance):
    original = instance.YPOS0
    instance.YPOS0 = original
    assert instance.YPOS0 == original

@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_RES_type(instance):
    assert isinstance(instance.RES, str)


@given(instance=afpText::GBOX_strategy)
def test_afptext::gbox_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
@settings(max_examples=50)
def test_afptext::dataobjectfontdescriptor_instantiation(instance):
    assert isinstance(instance, afpText::DataObjectFontDescriptor)

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_FontTech_type(instance):
    assert isinstance(instance.FontTech, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_FontTech_setter(instance):
    original = instance.FontTech
    instance.FontTech = original
    assert instance.FontTech == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_DOFtFlgs_type(instance):
    assert isinstance(instance.DOFtFlgs, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_DOFtFlgs_setter(instance):
    original = instance.DOFtFlgs
    instance.DOFtFlgs = original
    assert instance.DOFtFlgs == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_HFS_type(instance):
    assert isinstance(instance.HFS, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_HFS_setter(instance):
    original = instance.HFS
    instance.HFS = original
    assert instance.HFS == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_EncID_type(instance):
    assert isinstance(instance.EncID, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_EncID_setter(instance):
    original = instance.EncID
    instance.EncID = original
    assert instance.EncID == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_EncEnv_type(instance):
    assert isinstance(instance.EncEnv, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_EncEnv_setter(instance):
    original = instance.EncEnv
    instance.EncEnv = original
    assert instance.EncEnv == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_VFS_type(instance):
    assert isinstance(instance.VFS, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_VFS_setter(instance):
    original = instance.VFS
    instance.VFS = original
    assert instance.VFS == original

@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_CharRot_type(instance):
    assert isinstance(instance.CharRot, str)


@given(instance=afpText::DataObjectFontDescriptor_strategy)
def test_afptext::dataobjectfontdescriptor_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original

@given(instance=afpText::GCBIMG_strategy)
@settings(max_examples=50)
def test_afptext::gcbimg_instantiation(instance):
    assert isinstance(instance, afpText::GCBIMG)

@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_RES_type(instance):
    assert isinstance(instance.RES, str)


@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_RES_setter(instance):
    original = instance.RES
    instance.RES = original
    assert instance.RES == original

@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_HEIGHT_type(instance):
    assert isinstance(instance.HEIGHT, str)


@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_HEIGHT_setter(instance):
    original = instance.HEIGHT
    instance.HEIGHT = original
    assert instance.HEIGHT == original

@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_WIDTH_type(instance):
    assert isinstance(instance.WIDTH, str)


@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_WIDTH_setter(instance):
    original = instance.WIDTH
    instance.WIDTH = original
    assert instance.WIDTH == original

@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_FORMAT_type(instance):
    assert isinstance(instance.FORMAT, str)


@given(instance=afpText::GCBIMG_strategy)
def test_afptext::gcbimg_FORMAT_setter(instance):
    original = instance.FORMAT
    instance.FORMAT = original
    assert instance.FORMAT == original

@given(instance=afpText::TonerSaver_strategy)
@settings(max_examples=50)
def test_afptext::tonersaver_instantiation(instance):
    assert isinstance(instance, afpText::TonerSaver)

@given(instance=afpText::TonerSaver_strategy)
def test_afptext::tonersaver_TSvCtrl_type(instance):
    assert isinstance(instance.TSvCtrl, str)


@given(instance=afpText::TonerSaver_strategy)
def test_afptext::tonersaver_TSvCtrl_setter(instance):
    original = instance.TSvCtrl
    instance.TSvCtrl = original
    assert instance.TSvCtrl == original

@given(instance=afpText::TileTOC_strategy)
@settings(max_examples=50)
def test_afptext::tiletoc_instantiation(instance):
    assert isinstance(instance, afpText::TileTOC)

@given(instance=afpText::TileTOC_strategy)
def test_afptext::tiletoc_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::TileTOC_strategy)
def test_afptext::tiletoc_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::Comment_strategy)
@settings(max_examples=50)
def test_afptext::comment_instantiation(instance):
    assert isinstance(instance, afpText::Comment)

@given(instance=afpText::Comment_strategy)
def test_afptext::comment_Comment_type(instance):
    assert isinstance(instance.Comment, str)


@given(instance=afpText::Comment_strategy)
def test_afptext::comment_Comment_setter(instance):
    original = instance.Comment
    instance.Comment = original
    assert instance.Comment == original

@given(instance=afpText::BeginSegment_strategy)
@settings(max_examples=50)
def test_afptext::beginsegment_instantiation(instance):
    assert isinstance(instance, afpText::BeginSegment)

@given(instance=afpText::BeginSegment_strategy)
def test_afptext::beginsegment_SEGNAME_type(instance):
    assert isinstance(instance.SEGNAME, str)


@given(instance=afpText::BeginSegment_strategy)
def test_afptext::beginsegment_SEGNAME_setter(instance):
    original = instance.SEGNAME
    instance.SEGNAME = original
    assert instance.SEGNAME == original

@given(instance=afpText::GSPS_strategy)
@settings(max_examples=50)
def test_afptext::gsps_instantiation(instance):
    assert isinstance(instance, afpText::GSPS)

@given(instance=afpText::GSPS_strategy)
def test_afptext::gsps_LCID_type(instance):
    assert isinstance(instance.LCID, str)


@given(instance=afpText::GSPS_strategy)
def test_afptext::gsps_LCID_setter(instance):
    original = instance.LCID
    instance.LCID = original
    assert instance.LCID == original

@given(instance=afpText::ResourceSectionNumber_strategy)
@settings(max_examples=50)
def test_afptext::resourcesectionnumber_instantiation(instance):
    assert isinstance(instance, afpText::ResourceSectionNumber)

@given(instance=afpText::ResourceSectionNumber_strategy)
def test_afptext::resourcesectionnumber_ResSNum_type(instance):
    assert isinstance(instance.ResSNum, str)


@given(instance=afpText::ResourceSectionNumber_strategy)
def test_afptext::resourcesectionnumber_ResSNum_setter(instance):
    original = instance.ResSNum
    instance.ResSNum = original
    assert instance.ResSNum == original

@given(instance=afpText::ExternalAlgorithm_strategy)
@settings(max_examples=50)
def test_afptext::externalalgorithm_instantiation(instance):
    assert isinstance(instance, afpText::ExternalAlgorithm)

@given(instance=afpText::ExternalAlgorithm_strategy)
def test_afptext::externalalgorithm_ALGTYPE_type(instance):
    assert isinstance(instance.ALGTYPE, str)


@given(instance=afpText::ExternalAlgorithm_strategy)
def test_afptext::externalalgorithm_ALGTYPE_setter(instance):
    original = instance.ALGTYPE
    instance.ALGTYPE = original
    assert instance.ALGTYPE == original

@given(instance=afpText::BeginImage_strategy)
@settings(max_examples=50)
def test_afptext::beginimage_instantiation(instance):
    assert isinstance(instance, afpText::BeginImage)

@given(instance=afpText::BeginImage_strategy)
def test_afptext::beginimage_OBJTYPE_type(instance):
    assert isinstance(instance.OBJTYPE, str)


@given(instance=afpText::BeginImage_strategy)
def test_afptext::beginimage_OBJTYPE_setter(instance):
    original = instance.OBJTYPE
    instance.OBJTYPE = original
    assert instance.OBJTYPE == original

@given(instance=afpText::AMI_strategy)
@settings(max_examples=50)
def test_afptext::ami_instantiation(instance):
    assert isinstance(instance, afpText::AMI)

@given(instance=afpText::AMI_strategy)
def test_afptext::ami_DSPLCMNT_type(instance):
    assert isinstance(instance.DSPLCMNT, str)


@given(instance=afpText::AMI_strategy)
def test_afptext::ami_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText::GSCH_strategy)
@settings(max_examples=50)
def test_afptext::gsch_instantiation(instance):
    assert isinstance(instance, afpText::GSCH)

@given(instance=afpText::GSCH_strategy)
def test_afptext::gsch_HX_type(instance):
    assert isinstance(instance.HX, str)


@given(instance=afpText::GSCH_strategy)
def test_afptext::gsch_HX_setter(instance):
    original = instance.HX
    instance.HX = original
    assert instance.HX == original

@given(instance=afpText::GSCH_strategy)
def test_afptext::gsch_HY_type(instance):
    assert isinstance(instance.HY, str)


@given(instance=afpText::GSCH_strategy)
def test_afptext::gsch_HY_setter(instance):
    original = instance.HY
    instance.HY = original
    assert instance.HY == original

@given(instance=afpText::TRN_strategy)
@settings(max_examples=50)
def test_afptext::trn_instantiation(instance):
    assert isinstance(instance, afpText::TRN)

@given(instance=afpText::TRN_strategy)
def test_afptext::trn_TRNDATA_type(instance):
    assert isinstance(instance.TRNDATA, str)


@given(instance=afpText::TRN_strategy)
def test_afptext::trn_TRNDATA_setter(instance):
    original = instance.TRNDATA
    instance.TRNDATA = original
    assert instance.TRNDATA == original

@given(instance=afpText::FinishingOperation_strategy)
@settings(max_examples=50)
def test_afptext::finishingoperation_instantiation(instance):
    assert isinstance(instance, afpText::FinishingOperation)

@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_AxOffst_type(instance):
    assert isinstance(instance.AxOffst, str)


@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_AxOffst_setter(instance):
    original = instance.AxOffst
    instance.AxOffst = original
    assert instance.AxOffst == original

@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_FOpType_type(instance):
    assert isinstance(instance.FOpType, str)


@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_FOpType_setter(instance):
    original = instance.FOpType
    instance.FOpType = original
    assert instance.FOpType == original

@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_RefEdge_type(instance):
    assert isinstance(instance.RefEdge, str)


@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_RefEdge_setter(instance):
    original = instance.RefEdge
    instance.RefEdge = original
    assert instance.RefEdge == original

@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_FOpCnt_type(instance):
    assert isinstance(instance.FOpCnt, str)


@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_FOpCnt_setter(instance):
    original = instance.FOpCnt
    instance.FOpCnt = original
    assert instance.FOpCnt == original

@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_OpPos_type(instance):
    assert isinstance(instance.OpPos, str)


@given(instance=afpText::FinishingOperation_strategy)
def test_afptext::finishingoperation_OpPos_setter(instance):
    original = instance.OpPos
    instance.OpPos = original
    assert instance.OpPos == original

@given(instance=afpText::ImageEncoding_strategy)
@settings(max_examples=50)
def test_afptext::imageencoding_instantiation(instance):
    assert isinstance(instance, afpText::ImageEncoding)

@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_RECID_type(instance):
    assert isinstance(instance.RECID, str)


@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_RECID_setter(instance):
    original = instance.RECID
    instance.RECID = original
    assert instance.RECID == original

@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_BITORDR_type(instance):
    assert isinstance(instance.BITORDR, str)


@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_BITORDR_setter(instance):
    original = instance.BITORDR
    instance.BITORDR = original
    assert instance.BITORDR == original

@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_COMPRID_type(instance):
    assert isinstance(instance.COMPRID, str)


@given(instance=afpText::ImageEncoding_strategy)
def test_afptext::imageencoding_COMPRID_setter(instance):
    original = instance.COMPRID
    instance.COMPRID = original
    assert instance.COMPRID == original

@given(instance=afpText::MeasurementUnits_strategy)
@settings(max_examples=50)
def test_afptext::measurementunits_instantiation(instance):
    assert isinstance(instance, afpText::MeasurementUnits)

@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_XoaUnits_type(instance):
    assert isinstance(instance.XoaUnits, str)


@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_XoaUnits_setter(instance):
    original = instance.XoaUnits
    instance.XoaUnits = original
    assert instance.XoaUnits == original

@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_YoaUnits_type(instance):
    assert isinstance(instance.YoaUnits, str)


@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_YoaUnits_setter(instance):
    original = instance.YoaUnits
    instance.YoaUnits = original
    assert instance.YoaUnits == original

@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_YoaBase_type(instance):
    assert isinstance(instance.YoaBase, str)


@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_YoaBase_setter(instance):
    original = instance.YoaBase
    instance.YoaBase = original
    assert instance.YoaBase == original

@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_XoaBase_type(instance):
    assert isinstance(instance.XoaBase, str)


@given(instance=afpText::MeasurementUnits_strategy)
def test_afptext::measurementunits_XoaBase_setter(instance):
    original = instance.XoaBase
    instance.XoaBase = original
    assert instance.XoaBase == original

@given(instance=afpText::AttributeValue_strategy)
@settings(max_examples=50)
def test_afptext::attributevalue_instantiation(instance):
    assert isinstance(instance, afpText::AttributeValue)

@given(instance=afpText::AttributeValue_strategy)
def test_afptext::attributevalue_Reserved0_type(instance):
    assert isinstance(instance.Reserved0, str)


@given(instance=afpText::AttributeValue_strategy)
def test_afptext::attributevalue_Reserved0_setter(instance):
    original = instance.Reserved0
    instance.Reserved0 = original
    assert instance.Reserved0 == original

@given(instance=afpText::AttributeValue_strategy)
def test_afptext::attributevalue_AttVal_type(instance):
    assert isinstance(instance.AttVal, str)


@given(instance=afpText::AttributeValue_strategy)
def test_afptext::attributevalue_AttVal_setter(instance):
    original = instance.AttVal
    instance.AttVal = original
    assert instance.AttVal == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
@settings(max_examples=50)
def test_afptext::universaldateandtimestamp_instantiation(instance):
    assert isinstance(instance, afpText::UniversalDateAndTimeStamp)

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Hour_type(instance):
    assert isinstance(instance.Hour, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Hour_setter(instance):
    original = instance.Hour
    instance.Hour = original
    assert instance.Hour == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Second_type(instance):
    assert isinstance(instance.Second, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Second_setter(instance):
    original = instance.Second
    instance.Second = original
    assert instance.Second == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Day_type(instance):
    assert isinstance(instance.Day, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Day_setter(instance):
    original = instance.Day
    instance.Day = original
    assert instance.Day == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_UTCDiffM_type(instance):
    assert isinstance(instance.UTCDiffM, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_UTCDiffM_setter(instance):
    original = instance.UTCDiffM
    instance.UTCDiffM = original
    assert instance.UTCDiffM == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Month_type(instance):
    assert isinstance(instance.Month, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Month_setter(instance):
    original = instance.Month
    instance.Month = original
    assert instance.Month == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_YearAD_type(instance):
    assert isinstance(instance.YearAD, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_YearAD_setter(instance):
    original = instance.YearAD
    instance.YearAD = original
    assert instance.YearAD == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_TimeZone_type(instance):
    assert isinstance(instance.TimeZone, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_TimeZone_setter(instance):
    original = instance.TimeZone
    instance.TimeZone = original
    assert instance.TimeZone == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_UTCDiffH_type(instance):
    assert isinstance(instance.UTCDiffH, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_UTCDiffH_setter(instance):
    original = instance.UTCDiffH
    instance.UTCDiffH = original
    assert instance.UTCDiffH == original

@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Minute_type(instance):
    assert isinstance(instance.Minute, str)


@given(instance=afpText::UniversalDateAndTimeStamp_strategy)
def test_afptext::universaldateandtimestamp_Minute_setter(instance):
    original = instance.Minute
    instance.Minute = original
    assert instance.Minute == original

@given(instance=afpText::CharacterRotation_strategy)
@settings(max_examples=50)
def test_afptext::characterrotation_instantiation(instance):
    assert isinstance(instance, afpText::CharacterRotation)

@given(instance=afpText::CharacterRotation_strategy)
def test_afptext::characterrotation_CharRot_type(instance):
    assert isinstance(instance.CharRot, str)


@given(instance=afpText::CharacterRotation_strategy)
def test_afptext::characterrotation_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original

@given(instance=afpText::DescriptorPosition_strategy)
@settings(max_examples=50)
def test_afptext::descriptorposition_instantiation(instance):
    assert isinstance(instance, afpText::DescriptorPosition)

@given(instance=afpText::DescriptorPosition_strategy)
def test_afptext::descriptorposition_DesPosID_type(instance):
    assert isinstance(instance.DesPosID, str)


@given(instance=afpText::DescriptorPosition_strategy)
def test_afptext::descriptorposition_DesPosID_setter(instance):
    original = instance.DesPosID
    instance.DesPosID = original
    assert instance.DesPosID == original

@given(instance=afpText::ResourceObjectType_strategy)
@settings(max_examples=50)
def test_afptext::resourceobjecttype_instantiation(instance):
    assert isinstance(instance, afpText::ResourceObjectType)

@given(instance=afpText::ResourceObjectType_strategy)
def test_afptext::resourceobjecttype_ConData_type(instance):
    assert isinstance(instance.ConData, str)


@given(instance=afpText::ResourceObjectType_strategy)
def test_afptext::resourceobjecttype_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original

@given(instance=afpText::ResourceObjectType_strategy)
def test_afptext::resourceobjecttype_ObjType_type(instance):
    assert isinstance(instance.ObjType, str)


@given(instance=afpText::ResourceObjectType_strategy)
def test_afptext::resourceobjecttype_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText::AMB_strategy)
@settings(max_examples=50)
def test_afptext::amb_instantiation(instance):
    assert isinstance(instance, afpText::AMB)

@given(instance=afpText::AMB_strategy)
def test_afptext::amb_DSPLCMNT_type(instance):
    assert isinstance(instance.DSPLCMNT, str)


@given(instance=afpText::AMB_strategy)
def test_afptext::amb_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText::SVI_strategy)
@settings(max_examples=50)
def test_afptext::svi_instantiation(instance):
    assert isinstance(instance, afpText::SVI)

@given(instance=afpText::SVI_strategy)
def test_afptext::svi_INCRMENT_type(instance):
    assert isinstance(instance.INCRMENT, str)


@given(instance=afpText::SVI_strategy)
def test_afptext::svi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText::STO_strategy)
@settings(max_examples=50)
def test_afptext::sto_instantiation(instance):
    assert isinstance(instance, afpText::STO)

@given(instance=afpText::STO_strategy)
def test_afptext::sto_BORNTION_type(instance):
    assert isinstance(instance.BORNTION, str)


@given(instance=afpText::STO_strategy)
def test_afptext::sto_BORNTION_setter(instance):
    original = instance.BORNTION
    instance.BORNTION = original
    assert instance.BORNTION == original

@given(instance=afpText::STO_strategy)
def test_afptext::sto_IORNTION_type(instance):
    assert isinstance(instance.IORNTION, str)


@given(instance=afpText::STO_strategy)
def test_afptext::sto_IORNTION_setter(instance):
    original = instance.IORNTION
    instance.IORNTION = original
    assert instance.IORNTION == original

@given(instance=afpText::STC_strategy)
@settings(max_examples=50)
def test_afptext::stc_instantiation(instance):
    assert isinstance(instance, afpText::STC)

@given(instance=afpText::STC_strategy)
def test_afptext::stc_FRGCOLOR_type(instance):
    assert isinstance(instance.FRGCOLOR, str)


@given(instance=afpText::STC_strategy)
def test_afptext::stc_FRGCOLOR_setter(instance):
    original = instance.FRGCOLOR
    instance.FRGCOLOR = original
    assert instance.FRGCOLOR == original

@given(instance=afpText::STC_strategy)
def test_afptext::stc_PRECSION_type(instance):
    assert isinstance(instance.PRECSION, str)


@given(instance=afpText::STC_strategy)
def test_afptext::stc_PRECSION_setter(instance):
    original = instance.PRECSION
    instance.PRECSION = original
    assert instance.PRECSION == original

@given(instance=afpText::SIM_strategy)
@settings(max_examples=50)
def test_afptext::sim_instantiation(instance):
    assert isinstance(instance, afpText::SIM)

@given(instance=afpText::SIM_strategy)
def test_afptext::sim_DSPLCMNT_type(instance):
    assert isinstance(instance.DSPLCMNT, str)


@given(instance=afpText::SIM_strategy)
def test_afptext::sim_DSPLCMNT_setter(instance):
    original = instance.DSPLCMNT
    instance.DSPLCMNT = original
    assert instance.DSPLCMNT == original

@given(instance=afpText::SIA_strategy)
@settings(max_examples=50)
def test_afptext::sia_instantiation(instance):
    assert isinstance(instance, afpText::SIA)

@given(instance=afpText::SIA_strategy)
def test_afptext::sia_ADJSTMNT_type(instance):
    assert isinstance(instance.ADJSTMNT, str)


@given(instance=afpText::SIA_strategy)
def test_afptext::sia_ADJSTMNT_setter(instance):
    original = instance.ADJSTMNT
    instance.ADJSTMNT = original
    assert instance.ADJSTMNT == original

@given(instance=afpText::SIA_strategy)
def test_afptext::sia_DIRCTION_type(instance):
    assert isinstance(instance.DIRCTION, str)


@given(instance=afpText::SIA_strategy)
def test_afptext::sia_DIRCTION_setter(instance):
    original = instance.DIRCTION
    instance.DIRCTION = original
    assert instance.DIRCTION == original

@given(instance=afpText::SEC_strategy)
@settings(max_examples=50)
def test_afptext::sec_instantiation(instance):
    assert isinstance(instance, afpText::SEC)

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_RESERVED_type(instance):
    assert isinstance(instance.RESERVED, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE4_type(instance):
    assert isinstance(instance.COLSIZE4, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE4_setter(instance):
    original = instance.COLSIZE4
    instance.COLSIZE4 = original
    assert instance.COLSIZE4 == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE3_type(instance):
    assert isinstance(instance.COLSIZE3, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE3_setter(instance):
    original = instance.COLSIZE3
    instance.COLSIZE3 = original
    assert instance.COLSIZE3 == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE2_type(instance):
    assert isinstance(instance.COLSIZE2, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE2_setter(instance):
    original = instance.COLSIZE2
    instance.COLSIZE2 = original
    assert instance.COLSIZE2 == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE1_type(instance):
    assert isinstance(instance.COLSIZE1, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSIZE1_setter(instance):
    original = instance.COLSIZE1
    instance.COLSIZE1 = original
    assert instance.COLSIZE1 == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLVALUE_type(instance):
    assert isinstance(instance.COLVALUE, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLVALUE_setter(instance):
    original = instance.COLVALUE
    instance.COLVALUE = original
    assert instance.COLVALUE == original

@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSPCE_type(instance):
    assert isinstance(instance.COLSPCE, str)


@given(instance=afpText::SEC_strategy)
def test_afptext::sec_COLSPCE_setter(instance):
    original = instance.COLSPCE
    instance.COLSPCE = original
    assert instance.COLSPCE == original

@given(instance=afpText::SCFL_strategy)
@settings(max_examples=50)
def test_afptext::scfl_instantiation(instance):
    assert isinstance(instance, afpText::SCFL)

@given(instance=afpText::SCFL_strategy)
def test_afptext::scfl_LID_type(instance):
    assert isinstance(instance.LID, str)


@given(instance=afpText::SCFL_strategy)
def test_afptext::scfl_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText::SBI_strategy)
@settings(max_examples=50)
def test_afptext::sbi_instantiation(instance):
    assert isinstance(instance, afpText::SBI)

@given(instance=afpText::SBI_strategy)
def test_afptext::sbi_INCRMENT_type(instance):
    assert isinstance(instance.INCRMENT, str)


@given(instance=afpText::SBI_strategy)
def test_afptext::sbi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText::RPS_strategy)
@settings(max_examples=50)
def test_afptext::rps_instantiation(instance):
    assert isinstance(instance, afpText::RPS)

@given(instance=afpText::RPS_strategy)
def test_afptext::rps_RLENGTH_type(instance):
    assert isinstance(instance.RLENGTH, str)


@given(instance=afpText::RPS_strategy)
def test_afptext::rps_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original

@given(instance=afpText::RPS_strategy)
def test_afptext::rps_RPTDATA_type(instance):
    assert isinstance(instance.RPTDATA, str)


@given(instance=afpText::RPS_strategy)
def test_afptext::rps_RPTDATA_setter(instance):
    original = instance.RPTDATA
    instance.RPTDATA = original
    assert instance.RPTDATA == original

@given(instance=afpText::RMI_strategy)
@settings(max_examples=50)
def test_afptext::rmi_instantiation(instance):
    assert isinstance(instance, afpText::RMI)

@given(instance=afpText::RMI_strategy)
def test_afptext::rmi_INCRMENT_type(instance):
    assert isinstance(instance.INCRMENT, str)


@given(instance=afpText::RMI_strategy)
def test_afptext::rmi_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText::RMB_strategy)
@settings(max_examples=50)
def test_afptext::rmb_instantiation(instance):
    assert isinstance(instance, afpText::RMB)

@given(instance=afpText::RMB_strategy)
def test_afptext::rmb_INCRMENT_type(instance):
    assert isinstance(instance.INCRMENT, str)


@given(instance=afpText::RMB_strategy)
def test_afptext::rmb_INCRMENT_setter(instance):
    original = instance.INCRMENT
    instance.INCRMENT = original
    assert instance.INCRMENT == original

@given(instance=afpText::OVS_strategy)
@settings(max_examples=50)
def test_afptext::ovs_instantiation(instance):
    assert isinstance(instance, afpText::OVS)

@given(instance=afpText::OVS_strategy)
def test_afptext::ovs_BYPSIDEN_type(instance):
    assert isinstance(instance.BYPSIDEN, str)


@given(instance=afpText::OVS_strategy)
def test_afptext::ovs_BYPSIDEN_setter(instance):
    original = instance.BYPSIDEN
    instance.BYPSIDEN = original
    assert instance.BYPSIDEN == original

@given(instance=afpText::OVS_strategy)
def test_afptext::ovs_OVERCHAR_type(instance):
    assert isinstance(instance.OVERCHAR, str)


@given(instance=afpText::OVS_strategy)
def test_afptext::ovs_OVERCHAR_setter(instance):
    original = instance.OVERCHAR
    instance.OVERCHAR = original
    assert instance.OVERCHAR == original

@given(instance=afpText::NOPCS_strategy)
@settings(max_examples=50)
def test_afptext::nopcs_instantiation(instance):
    assert isinstance(instance, afpText::NOPCS)

@given(instance=afpText::NOPCS_strategy)
def test_afptext::nopcs_IGNDATA_type(instance):
    assert isinstance(instance.IGNDATA, str)


@given(instance=afpText::NOPCS_strategy)
def test_afptext::nopcs_IGNDATA_setter(instance):
    original = instance.IGNDATA
    instance.IGNDATA = original
    assert instance.IGNDATA == original

@given(instance=afpText::ESU_strategy)
@settings(max_examples=50)
def test_afptext::esu_instantiation(instance):
    assert isinstance(instance, afpText::ESU)

@given(instance=afpText::ESU_strategy)
def test_afptext::esu_LID_type(instance):
    assert isinstance(instance.LID, str)


@given(instance=afpText::ESU_strategy)
def test_afptext::esu_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText::DIR_strategy)
@settings(max_examples=50)
def test_afptext::dir_instantiation(instance):
    assert isinstance(instance, afpText::DIR)

@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RWIDTHFRACTION_type(instance):
    assert isinstance(instance.RWIDTHFRACTION, str)


@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RWIDTHFRACTION_setter(instance):
    original = instance.RWIDTHFRACTION
    instance.RWIDTHFRACTION = original
    assert instance.RWIDTHFRACTION == original

@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RWIDTH_type(instance):
    assert isinstance(instance.RWIDTH, str)


@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RWIDTH_setter(instance):
    original = instance.RWIDTH
    instance.RWIDTH = original
    assert instance.RWIDTH == original

@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RLENGTH_type(instance):
    assert isinstance(instance.RLENGTH, str)


@given(instance=afpText::DIR_strategy)
def test_afptext::dir_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original

@given(instance=afpText::DBR_strategy)
@settings(max_examples=50)
def test_afptext::dbr_instantiation(instance):
    assert isinstance(instance, afpText::DBR)

@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RLENGTH_type(instance):
    assert isinstance(instance.RLENGTH, str)


@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RLENGTH_setter(instance):
    original = instance.RLENGTH
    instance.RLENGTH = original
    assert instance.RLENGTH == original

@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RWIDTHFRACTION_type(instance):
    assert isinstance(instance.RWIDTHFRACTION, str)


@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RWIDTHFRACTION_setter(instance):
    original = instance.RWIDTHFRACTION
    instance.RWIDTHFRACTION = original
    assert instance.RWIDTHFRACTION == original

@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RWIDTH_type(instance):
    assert isinstance(instance.RWIDTH, str)


@given(instance=afpText::DBR_strategy)
def test_afptext::dbr_RWIDTH_setter(instance):
    original = instance.RWIDTH
    instance.RWIDTH = original
    assert instance.RWIDTH == original

@given(instance=afpText::GCRLINERG_strategy)
@settings(max_examples=50)
def test_afptext::gcrlinerg_instantiation(instance):
    assert isinstance(instance, afpText::GCRLINERG)

@given(instance=afpText::GCRLINERG_strategy)
def test_afptext::gcrlinerg_YOFFS_type(instance):
    assert isinstance(instance.YOFFS, str)


@given(instance=afpText::GCRLINERG_strategy)
def test_afptext::gcrlinerg_YOFFS_setter(instance):
    original = instance.YOFFS
    instance.YOFFS = original
    assert instance.YOFFS == original

@given(instance=afpText::GCRLINERG_strategy)
def test_afptext::gcrlinerg_XOSSF_type(instance):
    assert isinstance(instance.XOSSF, str)


@given(instance=afpText::GCRLINERG_strategy)
def test_afptext::gcrlinerg_XOSSF_setter(instance):
    original = instance.XOSSF
    instance.XOSSF = original
    assert instance.XOSSF == original

@given(instance=afpText::GRLINERG_strategy)
@settings(max_examples=50)
def test_afptext::grlinerg_instantiation(instance):
    assert isinstance(instance, afpText::GRLINERG)

@given(instance=afpText::GRLINERG_strategy)
def test_afptext::grlinerg_YOFFS_type(instance):
    assert isinstance(instance.YOFFS, str)


@given(instance=afpText::GRLINERG_strategy)
def test_afptext::grlinerg_YOFFS_setter(instance):
    original = instance.YOFFS
    instance.YOFFS = original
    assert instance.YOFFS == original

@given(instance=afpText::GRLINERG_strategy)
def test_afptext::grlinerg_XOSSF_type(instance):
    assert isinstance(instance.XOSSF, str)


@given(instance=afpText::GRLINERG_strategy)
def test_afptext::grlinerg_XOSSF_setter(instance):
    original = instance.XOSSF
    instance.XOSSF = original
    assert instance.XOSSF == original

@given(instance=afpText::GCMRKRG_strategy)
@settings(max_examples=50)
def test_afptext::gcmrkrg_instantiation(instance):
    assert isinstance(instance, afpText::GCMRKRG)

@given(instance=afpText::GCMRKRG_strategy)
def test_afptext::gcmrkrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCMRKRG_strategy)
def test_afptext::gcmrkrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCMRKRG_strategy)
def test_afptext::gcmrkrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCMRKRG_strategy)
def test_afptext::gcmrkrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GMRKRG_strategy)
@settings(max_examples=50)
def test_afptext::gmrkrg_instantiation(instance):
    assert isinstance(instance, afpText::GMRKRG)

@given(instance=afpText::GMRKRG_strategy)
def test_afptext::gmrkrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GMRKRG_strategy)
def test_afptext::gmrkrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GMRKRG_strategy)
def test_afptext::gmrkrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GMRKRG_strategy)
def test_afptext::gmrkrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCLINERG_strategy)
@settings(max_examples=50)
def test_afptext::gclinerg_instantiation(instance):
    assert isinstance(instance, afpText::GCLINERG)

@given(instance=afpText::GCLINERG_strategy)
def test_afptext::gclinerg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCLINERG_strategy)
def test_afptext::gclinerg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCLINERG_strategy)
def test_afptext::gclinerg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCLINERG_strategy)
def test_afptext::gclinerg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::triplet_strategy)
@settings(max_examples=50)
def test_afptext::triplet_instantiation(instance):
    assert isinstance(instance, afpText::triplet)

@given(instance=structuredField_strategy)
@settings(max_examples=50)
def test_structuredfield_instantiation(instance):
    assert isinstance(instance, structuredField)

@given(instance=afpText::BCF_strategy)
@settings(max_examples=50)
def test_afptext::bcf_instantiation(instance):
    assert isinstance(instance, afpText::BCF)

@given(instance=afpText::BCF_strategy)
def test_afptext::bcf_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::BCF_strategy)
def test_afptext::bcf_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::BDX_strategy)
@settings(max_examples=50)
def test_afptext::bdx_instantiation(instance):
    assert isinstance(instance, afpText::BDX)

@given(instance=afpText::BDX_strategy)
def test_afptext::bdx_DMXName_type(instance):
    assert isinstance(instance.DMXName, str)


@given(instance=afpText::BDX_strategy)
def test_afptext::bdx_DMXName_setter(instance):
    original = instance.DMXName
    instance.DMXName = original
    assert instance.DMXName == original

@given(instance=afpText::BFN_strategy)
@settings(max_examples=50)
def test_afptext::bfn_instantiation(instance):
    assert isinstance(instance, afpText::BFN)

@given(instance=afpText::BFN_strategy)
def test_afptext::bfn_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::BFN_strategy)
def test_afptext::bfn_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::BGR_strategy)
@settings(max_examples=50)
def test_afptext::bgr_instantiation(instance):
    assert isinstance(instance, afpText::BGR)

@given(instance=afpText::BGR_strategy)
def test_afptext::bgr_GdoName_type(instance):
    assert isinstance(instance.GdoName, str)


@given(instance=afpText::BGR_strategy)
def test_afptext::bgr_GdoName_setter(instance):
    original = instance.GdoName
    instance.GdoName = original
    assert instance.GdoName == original

@given(instance=afpText::BOC_strategy)
@settings(max_examples=50)
def test_afptext::boc_instantiation(instance):
    assert isinstance(instance, afpText::BOC)

@given(instance=afpText::BOC_strategy)
def test_afptext::boc_ObjCName_type(instance):
    assert isinstance(instance.ObjCName, str)


@given(instance=afpText::BOC_strategy)
def test_afptext::boc_ObjCName_setter(instance):
    original = instance.ObjCName
    instance.ObjCName = original
    assert instance.ObjCName == original

@given(instance=afpText::BFG_strategy)
@settings(max_examples=50)
def test_afptext::bfg_instantiation(instance):
    assert isinstance(instance, afpText::BFG)

@given(instance=afpText::BFG_strategy)
def test_afptext::bfg_FEGName_type(instance):
    assert isinstance(instance.FEGName, str)


@given(instance=afpText::BFG_strategy)
def test_afptext::bfg_FEGName_setter(instance):
    original = instance.FEGName
    instance.FEGName = original
    assert instance.FEGName == original

@given(instance=afpText::BII_strategy)
@settings(max_examples=50)
def test_afptext::bii_instantiation(instance):
    assert isinstance(instance, afpText::BII)

@given(instance=afpText::BII_strategy)
def test_afptext::bii_ImoName_type(instance):
    assert isinstance(instance.ImoName, str)


@given(instance=afpText::BII_strategy)
def test_afptext::bii_ImoName_setter(instance):
    original = instance.ImoName
    instance.ImoName = original
    assert instance.ImoName == original

@given(instance=afpText::BFM_strategy)
@settings(max_examples=50)
def test_afptext::bfm_instantiation(instance):
    assert isinstance(instance, afpText::BFM)

@given(instance=afpText::BFM_strategy)
def test_afptext::bfm_FMName_type(instance):
    assert isinstance(instance.FMName, str)


@given(instance=afpText::BFM_strategy)
def test_afptext::bfm_FMName_setter(instance):
    original = instance.FMName
    instance.FMName = original
    assert instance.FMName == original

@given(instance=afpText::BMM_strategy)
@settings(max_examples=50)
def test_afptext::bmm_instantiation(instance):
    assert isinstance(instance, afpText::BMM)

@given(instance=afpText::BMM_strategy)
def test_afptext::bmm_MMName_type(instance):
    assert isinstance(instance.MMName, str)


@given(instance=afpText::BMM_strategy)
def test_afptext::bmm_MMName_setter(instance):
    original = instance.MMName
    instance.MMName = original
    assert instance.MMName == original

@given(instance=afpText::BAG_strategy)
@settings(max_examples=50)
def test_afptext::bag_instantiation(instance):
    assert isinstance(instance, afpText::BAG)

@given(instance=afpText::BAG_strategy)
def test_afptext::bag_AEGName_type(instance):
    assert isinstance(instance.AEGName, str)


@given(instance=afpText::BAG_strategy)
def test_afptext::bag_AEGName_setter(instance):
    original = instance.AEGName
    instance.AEGName = original
    assert instance.AEGName == original

@given(instance=afpText::BCP_strategy)
@settings(max_examples=50)
def test_afptext::bcp_instantiation(instance):
    assert isinstance(instance, afpText::BCP)

@given(instance=afpText::BCP_strategy)
def test_afptext::bcp_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::BCP_strategy)
def test_afptext::bcp_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::BIM_strategy)
@settings(max_examples=50)
def test_afptext::bim_instantiation(instance):
    assert isinstance(instance, afpText::BIM)

@given(instance=afpText::BIM_strategy)
def test_afptext::bim_IdoName_type(instance):
    assert isinstance(instance.IdoName, str)


@given(instance=afpText::BIM_strategy)
def test_afptext::bim_IdoName_setter(instance):
    original = instance.IdoName
    instance.IdoName = original
    assert instance.IdoName == original

@given(instance=afpText::BMO_strategy)
@settings(max_examples=50)
def test_afptext::bmo_instantiation(instance):
    assert isinstance(instance, afpText::BMO)

@given(instance=afpText::BMO_strategy)
def test_afptext::bmo_OvlyName_type(instance):
    assert isinstance(instance.OvlyName, str)


@given(instance=afpText::BMO_strategy)
def test_afptext::bmo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original

@given(instance=afpText::BDD_strategy)
@settings(max_examples=50)
def test_afptext::bdd_instantiation(instance):
    assert isinstance(instance, afpText::BDD)

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_YEXTENT_type(instance):
    assert isinstance(instance.YEXTENT, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_YEXTENT_setter(instance):
    original = instance.YEXTENT
    instance.YEXTENT = original
    assert instance.YEXTENT == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_UBASE_type(instance):
    assert isinstance(instance.UBASE, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_UBASE_setter(instance):
    original = instance.UBASE
    instance.UBASE = original
    assert instance.UBASE == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_COLOR_type(instance):
    assert isinstance(instance.COLOR, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_COLOR_setter(instance):
    original = instance.COLOR
    instance.COLOR = original
    assert instance.COLOR == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_XUPUB_type(instance):
    assert isinstance(instance.XUPUB, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_XUPUB_setter(instance):
    original = instance.XUPUB
    instance.XUPUB = original
    assert instance.XUPUB == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MOD_type(instance):
    assert isinstance(instance.MOD, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MOD_setter(instance):
    original = instance.MOD
    instance.MOD = original
    assert instance.MOD == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_WENE_type(instance):
    assert isinstance(instance.WENE, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_WENE_setter(instance):
    original = instance.WENE
    instance.WENE = original
    assert instance.WENE == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MULT_type(instance):
    assert isinstance(instance.MULT, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MULT_setter(instance):
    original = instance.MULT
    instance.MULT = original
    assert instance.MULT == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_ELEMENTHEIGHT_type(instance):
    assert isinstance(instance.ELEMENTHEIGHT, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_ELEMENTHEIGHT_setter(instance):
    original = instance.ELEMENTHEIGHT
    instance.ELEMENTHEIGHT = original
    assert instance.ELEMENTHEIGHT == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_YUPUB_type(instance):
    assert isinstance(instance.YUPUB, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_YUPUB_setter(instance):
    original = instance.YUPUB
    instance.YUPUB = original
    assert instance.YUPUB == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MODULEWIDTH_type(instance):
    assert isinstance(instance.MODULEWIDTH, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_MODULEWIDTH_setter(instance):
    original = instance.MODULEWIDTH
    instance.MODULEWIDTH = original
    assert instance.MODULEWIDTH == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_TYPE_type(instance):
    assert isinstance(instance.TYPE, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_TYPE_setter(instance):
    original = instance.TYPE
    instance.TYPE = original
    assert instance.TYPE == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_XEXTENT_type(instance):
    assert isinstance(instance.XEXTENT, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_XEXTENT_setter(instance):
    original = instance.XEXTENT
    instance.XEXTENT = original
    assert instance.XEXTENT == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_LID_type(instance):
    assert isinstance(instance.LID, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_LID_setter(instance):
    original = instance.LID
    instance.LID = original
    assert instance.LID == original

@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::BDD_strategy)
def test_afptext::bdd_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::BDA_strategy)
@settings(max_examples=50)
def test_afptext::bda_instantiation(instance):
    assert isinstance(instance, afpText::BDA)

@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Xoffset_type(instance):
    assert isinstance(instance.Xoffset, str)


@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Xoffset_setter(instance):
    original = instance.Xoffset
    instance.Xoffset = original
    assert instance.Xoffset == original

@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Yoffset_type(instance):
    assert isinstance(instance.Yoffset, str)


@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Yoffset_setter(instance):
    original = instance.Yoffset
    instance.Yoffset = original
    assert instance.Yoffset == original

@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Data_type(instance):
    assert isinstance(instance.Data, str)


@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Data_setter(instance):
    original = instance.Data
    instance.Data = original
    assert instance.Data == original

@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Flags_type(instance):
    assert isinstance(instance.Flags, str)


@given(instance=afpText::BDA_strategy)
def test_afptext::bda_Flags_setter(instance):
    original = instance.Flags
    instance.Flags = original
    assert instance.Flags == original

@given(instance=afpText::BBC_strategy)
@settings(max_examples=50)
def test_afptext::bbc_instantiation(instance):
    assert isinstance(instance, afpText::BBC)

@given(instance=afpText::BBC_strategy)
def test_afptext::bbc_BCdoName_type(instance):
    assert isinstance(instance.BCdoName, str)


@given(instance=afpText::BBC_strategy)
def test_afptext::bbc_BCdoName_setter(instance):
    original = instance.BCdoName
    instance.BCdoName = original
    assert instance.BCdoName == original

@given(instance=afpText::BDI_strategy)
@settings(max_examples=50)
def test_afptext::bdi_instantiation(instance):
    assert isinstance(instance, afpText::BDI)

@given(instance=afpText::BDI_strategy)
def test_afptext::bdi_IndxName_type(instance):
    assert isinstance(instance.IndxName, str)


@given(instance=afpText::BDI_strategy)
def test_afptext::bdi_IndxName_setter(instance):
    original = instance.IndxName
    instance.IndxName = original
    assert instance.IndxName == original

@given(instance=afpText::BDM_strategy)
@settings(max_examples=50)
def test_afptext::bdm_instantiation(instance):
    assert isinstance(instance, afpText::BDM)

@given(instance=afpText::BDM_strategy)
def test_afptext::bdm_DMName_type(instance):
    assert isinstance(instance.DMName, str)


@given(instance=afpText::BDM_strategy)
def test_afptext::bdm_DMName_setter(instance):
    original = instance.DMName
    instance.DMName = original
    assert instance.DMName == original

@given(instance=afpText::BDM_strategy)
def test_afptext::bdm_DatFmt_type(instance):
    assert isinstance(instance.DatFmt, str)


@given(instance=afpText::BDM_strategy)
def test_afptext::bdm_DatFmt_setter(instance):
    original = instance.DatFmt
    instance.DatFmt = original
    assert instance.DatFmt == original

@given(instance=afpText::BDG_strategy)
@settings(max_examples=50)
def test_afptext::bdg_instantiation(instance):
    assert isinstance(instance, afpText::BDG)

@given(instance=afpText::BDG_strategy)
def test_afptext::bdg_DEGName_type(instance):
    assert isinstance(instance.DEGName, str)


@given(instance=afpText::BDG_strategy)
def test_afptext::bdg_DEGName_setter(instance):
    original = instance.DEGName
    instance.DEGName = original
    assert instance.DEGName == original

@given(instance=afpText::BCA_strategy)
@settings(max_examples=50)
def test_afptext::bca_instantiation(instance):
    assert isinstance(instance, afpText::BCA)

@given(instance=afpText::BCA_strategy)
def test_afptext::bca_CATName_type(instance):
    assert isinstance(instance.CATName, str)


@given(instance=afpText::BCA_strategy)
def test_afptext::bca_CATName_setter(instance):
    original = instance.CATName
    instance.CATName = original
    assert instance.CATName == original

@given(instance=afpText::BOG_strategy)
@settings(max_examples=50)
def test_afptext::bog_instantiation(instance):
    assert isinstance(instance, afpText::BOG)

@given(instance=afpText::BOG_strategy)
def test_afptext::bog_OEGName_type(instance):
    assert isinstance(instance.OEGName, str)


@given(instance=afpText::BOG_strategy)
def test_afptext::bog_OEGName_setter(instance):
    original = instance.OEGName
    instance.OEGName = original
    assert instance.OEGName == original

@given(instance=afpText::BDT_strategy)
@settings(max_examples=50)
def test_afptext::bdt_instantiation(instance):
    assert isinstance(instance, afpText::BDT)

@given(instance=afpText::BDT_strategy)
def test_afptext::bdt_DocName_type(instance):
    assert isinstance(instance.DocName, str)


@given(instance=afpText::BDT_strategy)
def test_afptext::bdt_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original

@given(instance=afpText::BDT_strategy)
def test_afptext::bdt_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::BDT_strategy)
def test_afptext::bdt_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::BNG_strategy)
@settings(max_examples=50)
def test_afptext::bng_instantiation(instance):
    assert isinstance(instance, afpText::BNG)

@given(instance=afpText::BNG_strategy)
def test_afptext::bng_PGrpName_type(instance):
    assert isinstance(instance.PGrpName, str)


@given(instance=afpText::BNG_strategy)
def test_afptext::bng_PGrpName_setter(instance):
    original = instance.PGrpName
    instance.PGrpName = original
    assert instance.PGrpName == original

@given(instance=afpText::BPF_strategy)
@settings(max_examples=50)
def test_afptext::bpf_instantiation(instance):
    assert isinstance(instance, afpText::BPF)

@given(instance=afpText::BPF_strategy)
def test_afptext::bpf_PFName_type(instance):
    assert isinstance(instance.PFName, str)


@given(instance=afpText::BPF_strategy)
def test_afptext::bpf_PFName_setter(instance):
    original = instance.PFName
    instance.PFName = original
    assert instance.PFName == original

@given(instance=afpText::LineData_strategy)
@settings(max_examples=50)
def test_afptext::linedata_instantiation(instance):
    assert isinstance(instance, afpText::LineData)

@given(instance=afpText::LineData_strategy)
def test_afptext::linedata_linedata_type(instance):
    assert isinstance(instance.linedata, str)


@given(instance=afpText::LineData_strategy)
def test_afptext::linedata_linedata_setter(instance):
    original = instance.linedata
    instance.linedata = original
    assert instance.linedata == original

@given(instance=afpText::structuredField_strategy)
@settings(max_examples=50)
def test_afptext::structuredfield_instantiation(instance):
    assert isinstance(instance, afpText::structuredField)

@given(instance=afpText::Model_strategy)
@settings(max_examples=50)
def test_afptext::model_instantiation(instance):
    assert isinstance(instance, afpText::Model)

@given(instance=afpText::GLINERG_strategy)
@settings(max_examples=50)
def test_afptext::glinerg_instantiation(instance):
    assert isinstance(instance, afpText::GLINERG)

@given(instance=afpText::GLINERG_strategy)
def test_afptext::glinerg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GLINERG_strategy)
def test_afptext::glinerg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GLINERG_strategy)
def test_afptext::glinerg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GLINERG_strategy)
def test_afptext::glinerg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCFLTRG_strategy)
@settings(max_examples=50)
def test_afptext::gcfltrg_instantiation(instance):
    assert isinstance(instance, afpText::GCFLTRG)

@given(instance=afpText::GCFLTRG_strategy)
def test_afptext::gcfltrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCFLTRG_strategy)
def test_afptext::gcfltrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCFLTRG_strategy)
def test_afptext::gcfltrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCFLTRG_strategy)
def test_afptext::gcfltrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GFLTRG_strategy)
@settings(max_examples=50)
def test_afptext::gfltrg_instantiation(instance):
    assert isinstance(instance, afpText::GFLTRG)

@given(instance=afpText::GFLTRG_strategy)
def test_afptext::gfltrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GFLTRG_strategy)
def test_afptext::gfltrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GFLTRG_strategy)
def test_afptext::gfltrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GFLTRG_strategy)
def test_afptext::gfltrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCCBEZRG_strategy)
@settings(max_examples=50)
def test_afptext::gccbezrg_instantiation(instance):
    assert isinstance(instance, afpText::GCCBEZRG)

@given(instance=afpText::GCCBEZRG_strategy)
def test_afptext::gccbezrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCCBEZRG_strategy)
def test_afptext::gccbezrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::GCCBEZRG_strategy)
def test_afptext::gccbezrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCCBEZRG_strategy)
def test_afptext::gccbezrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCBEZRG_strategy)
@settings(max_examples=50)
def test_afptext::gcbezrg_instantiation(instance):
    assert isinstance(instance, afpText::GCBEZRG)

@given(instance=afpText::GCBEZRG_strategy)
def test_afptext::gcbezrg_XPOS_type(instance):
    assert isinstance(instance.XPOS, str)


@given(instance=afpText::GCBEZRG_strategy)
def test_afptext::gcbezrg_XPOS_setter(instance):
    original = instance.XPOS
    instance.XPOS = original
    assert instance.XPOS == original

@given(instance=afpText::GCBEZRG_strategy)
def test_afptext::gcbezrg_YPOS_type(instance):
    assert isinstance(instance.YPOS, str)


@given(instance=afpText::GCBEZRG_strategy)
def test_afptext::gcbezrg_YPOS_setter(instance):
    original = instance.YPOS
    instance.YPOS = original
    assert instance.YPOS == original

@given(instance=afpText::FNNRG_strategy)
@settings(max_examples=50)
def test_afptext::fnnrg_instantiation(instance):
    assert isinstance(instance, afpText::FNNRG)

@given(instance=afpText::FNNRG_strategy)
def test_afptext::fnnrg_TSOffset_type(instance):
    assert isinstance(instance.TSOffset, str)


@given(instance=afpText::FNNRG_strategy)
def test_afptext::fnnrg_TSOffset_setter(instance):
    original = instance.TSOffset
    instance.TSOffset = original
    assert instance.TSOffset == original

@given(instance=afpText::FNNRG_strategy)
def test_afptext::fnnrg_GCGID_type(instance):
    assert isinstance(instance.GCGID, str)


@given(instance=afpText::FNNRG_strategy)
def test_afptext::fnnrg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original

@given(instance=afpText::ExternalAlgorithmRG_strategy)
@settings(max_examples=50)
def test_afptext::externalalgorithmrg_instantiation(instance):
    assert isinstance(instance, afpText::ExternalAlgorithmRG)

@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_PADALMT_type(instance):
    assert isinstance(instance.PADALMT, str)


@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_PADALMT_setter(instance):
    original = instance.PADALMT
    instance.PADALMT = original
    assert instance.PADALMT == original

@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_DIRCTN_type(instance):
    assert isinstance(instance.DIRCTN, str)


@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_DIRCTN_setter(instance):
    original = instance.DIRCTN
    instance.DIRCTN = original
    assert instance.DIRCTN == original

@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_PADBDRY_type(instance):
    assert isinstance(instance.PADBDRY, str)


@given(instance=afpText::ExternalAlgorithmRG_strategy)
def test_afptext::externalalgorithmrg_PADBDRY_setter(instance):
    original = instance.PADBDRY
    instance.PADBDRY = original
    assert instance.PADBDRY == original

@given(instance=afpText::SamplingRatiosRG_strategy)
@settings(max_examples=50)
def test_afptext::samplingratiosrg_instantiation(instance):
    assert isinstance(instance, afpText::SamplingRatiosRG)

@given(instance=afpText::SamplingRatiosRG_strategy)
def test_afptext::samplingratiosrg_VSAMPLE_type(instance):
    assert isinstance(instance.VSAMPLE, str)


@given(instance=afpText::SamplingRatiosRG_strategy)
def test_afptext::samplingratiosrg_VSAMPLE_setter(instance):
    original = instance.VSAMPLE
    instance.VSAMPLE = original
    assert instance.VSAMPLE == original

@given(instance=afpText::SamplingRatiosRG_strategy)
def test_afptext::samplingratiosrg_HSAMPLE_type(instance):
    assert isinstance(instance.HSAMPLE, str)


@given(instance=afpText::SamplingRatiosRG_strategy)
def test_afptext::samplingratiosrg_HSAMPLE_setter(instance):
    original = instance.HSAMPLE
    instance.HSAMPLE = original
    assert instance.HSAMPLE == original

@given(instance=afpText::TileTOCRG_strategy)
@settings(max_examples=50)
def test_afptext::tiletocrg_instantiation(instance):
    assert isinstance(instance, afpText::TileTOCRG)

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_YOFFSET_type(instance):
    assert isinstance(instance.YOFFSET, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_YOFFSET_setter(instance):
    original = instance.YOFFSET
    instance.YOFFSET = original
    assert instance.YOFFSET == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_DATAPOS_type(instance):
    assert isinstance(instance.DATAPOS, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_DATAPOS_setter(instance):
    original = instance.DATAPOS
    instance.DATAPOS = original
    assert instance.DATAPOS == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_RELRES_type(instance):
    assert isinstance(instance.RELRES, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_RELRES_setter(instance):
    original = instance.RELRES
    instance.RELRES = original
    assert instance.RELRES == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_THSIZE_type(instance):
    assert isinstance(instance.THSIZE, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_THSIZE_setter(instance):
    original = instance.THSIZE
    instance.THSIZE = original
    assert instance.THSIZE == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_COMPR_type(instance):
    assert isinstance(instance.COMPR, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_COMPR_setter(instance):
    original = instance.COMPR
    instance.COMPR = original
    assert instance.COMPR == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_XOFFSET_type(instance):
    assert isinstance(instance.XOFFSET, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_XOFFSET_setter(instance):
    original = instance.XOFFSET
    instance.XOFFSET = original
    assert instance.XOFFSET == original

@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_TVSIZE_type(instance):
    assert isinstance(instance.TVSIZE, str)


@given(instance=afpText::TileTOCRG_strategy)
def test_afptext::tiletocrg_TVSIZE_setter(instance):
    original = instance.TVSIZE
    instance.TVSIZE = original
    assert instance.TVSIZE == original

@given(instance=afpText::BandImageRG_strategy)
@settings(max_examples=50)
def test_afptext::bandimagerg_instantiation(instance):
    assert isinstance(instance, afpText::BandImageRG)

@given(instance=afpText::BandImageRG_strategy)
def test_afptext::bandimagerg_BITCNT_type(instance):
    assert isinstance(instance.BITCNT, str)


@given(instance=afpText::BandImageRG_strategy)
def test_afptext::bandimagerg_BITCNT_setter(instance):
    original = instance.BITCNT
    instance.BITCNT = original
    assert instance.BITCNT == original

@given(instance=afpText::TLE_strategy)
@settings(max_examples=50)
def test_afptext::tle_instantiation(instance):
    assert isinstance(instance, afpText::TLE)

@given(instance=afpText::PTX_strategy)
@settings(max_examples=50)
def test_afptext::ptx_instantiation(instance):
    assert isinstance(instance, afpText::PTX)

@given(instance=afpText::FGD_strategy)
@settings(max_examples=50)
def test_afptext::fgd_instantiation(instance):
    assert isinstance(instance, afpText::FGD)

@given(instance=afpText::FGD_strategy)
def test_afptext::fgd_ConData_type(instance):
    assert isinstance(instance.ConData, str)


@given(instance=afpText::FGD_strategy)
def test_afptext::fgd_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original

@given(instance=afpText::PGP_strategy)
@settings(max_examples=50)
def test_afptext::pgp_instantiation(instance):
    assert isinstance(instance, afpText::PGP)

@given(instance=afpText::PGP_strategy)
def test_afptext::pgp_Constant_type(instance):
    assert isinstance(instance.Constant, str)


@given(instance=afpText::PGP_strategy)
def test_afptext::pgp_Constant_setter(instance):
    original = instance.Constant
    instance.Constant = original
    assert instance.Constant == original

@given(instance=afpText::PTD1_strategy)
@settings(max_examples=50)
def test_afptext::ptd1_instantiation(instance):
    assert isinstance(instance, afpText::PTD1)

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPEXTENT_type(instance):
    assert isinstance(instance.YPEXTENT, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPEXTENT_setter(instance):
    original = instance.YPEXTENT
    instance.YPEXTENT = original
    assert instance.YPEXTENT == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPUNITVL_type(instance):
    assert isinstance(instance.YPUNITVL, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPUNITVL_setter(instance):
    original = instance.YPUNITVL
    instance.YPUNITVL = original
    assert instance.YPUNITVL == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPEXTENT_type(instance):
    assert isinstance(instance.XPEXTENT, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPEXTENT_setter(instance):
    original = instance.XPEXTENT
    instance.XPEXTENT = original
    assert instance.XPEXTENT == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPBASE_type(instance):
    assert isinstance(instance.XPBASE, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPBASE_setter(instance):
    original = instance.XPBASE
    instance.XPBASE = original
    assert instance.XPBASE == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPBASE_type(instance):
    assert isinstance(instance.YPBASE, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_YPBASE_setter(instance):
    original = instance.YPBASE
    instance.YPBASE = original
    assert instance.YPBASE == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_RESERVED_type(instance):
    assert isinstance(instance.RESERVED, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPUNITVL_type(instance):
    assert isinstance(instance.XPUNITVL, str)


@given(instance=afpText::PTD1_strategy)
def test_afptext::ptd1_XPUNITVL_setter(instance):
    original = instance.XPUNITVL
    instance.XPUNITVL = original
    assert instance.XPUNITVL == original

@given(instance=afpText::PTD_strategy)
@settings(max_examples=50)
def test_afptext::ptd_instantiation(instance):
    assert isinstance(instance, afpText::PTD)

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPUNITVL_type(instance):
    assert isinstance(instance.YPUNITVL, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPUNITVL_setter(instance):
    original = instance.YPUNITVL
    instance.YPUNITVL = original
    assert instance.YPUNITVL == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPUNITVL_type(instance):
    assert isinstance(instance.XPUNITVL, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPUNITVL_setter(instance):
    original = instance.XPUNITVL
    instance.XPUNITVL = original
    assert instance.XPUNITVL == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPEXTENT_type(instance):
    assert isinstance(instance.YPEXTENT, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPEXTENT_setter(instance):
    original = instance.YPEXTENT
    instance.YPEXTENT = original
    assert instance.YPEXTENT == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_RESERVED_type(instance):
    assert isinstance(instance.RESERVED, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_RESERVED_setter(instance):
    original = instance.RESERVED
    instance.RESERVED = original
    assert instance.RESERVED == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPBASE_type(instance):
    assert isinstance(instance.YPBASE, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_YPBASE_setter(instance):
    original = instance.YPBASE
    instance.YPBASE = original
    assert instance.YPBASE == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPEXTENT_type(instance):
    assert isinstance(instance.XPEXTENT, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPEXTENT_setter(instance):
    original = instance.XPEXTENT
    instance.XPEXTENT = original
    assert instance.XPEXTENT == original

@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPBASE_type(instance):
    assert isinstance(instance.XPBASE, str)


@given(instance=afpText::PTD_strategy)
def test_afptext::ptd_XPBASE_setter(instance):
    original = instance.XPBASE
    instance.XPBASE = original
    assert instance.XPBASE == original

@given(instance=afpText::PPORG_strategy)
@settings(max_examples=50)
def test_afptext::pporg_instantiation(instance):
    assert isinstance(instance, afpText::PPORG)

@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_YocaOset_type(instance):
    assert isinstance(instance.YocaOset, str)


@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original

@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_ObjType_type(instance):
    assert isinstance(instance.ObjType, str)


@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_ProcFlgs_type(instance):
    assert isinstance(instance.ProcFlgs, str)


@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_ProcFlgs_setter(instance):
    original = instance.ProcFlgs
    instance.ProcFlgs = original
    assert instance.ProcFlgs == original

@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_XocaOset_type(instance):
    assert isinstance(instance.XocaOset, str)


@given(instance=afpText::PPORG_strategy)
def test_afptext::pporg_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original

@given(instance=afpText::PPO_strategy)
@settings(max_examples=50)
def test_afptext::ppo_instantiation(instance):
    assert isinstance(instance, afpText::PPO)

@given(instance=afpText::PMC_strategy)
@settings(max_examples=50)
def test_afptext::pmc_instantiation(instance):
    assert isinstance(instance, afpText::PMC)

@given(instance=afpText::PMC_strategy)
def test_afptext::pmc_PMCid_type(instance):
    assert isinstance(instance.PMCid, str)


@given(instance=afpText::PMC_strategy)
def test_afptext::pmc_PMCid_setter(instance):
    original = instance.PMCid
    instance.PMCid = original
    assert instance.PMCid == original

@given(instance=afpText::PGP1_strategy)
@settings(max_examples=50)
def test_afptext::pgp1_instantiation(instance):
    assert isinstance(instance, afpText::PGP1)

@given(instance=afpText::PGP1_strategy)
def test_afptext::pgp1_YOset_type(instance):
    assert isinstance(instance.YOset, str)


@given(instance=afpText::PGP1_strategy)
def test_afptext::pgp1_YOset_setter(instance):
    original = instance.YOset
    instance.YOset = original
    assert instance.YOset == original

@given(instance=afpText::PGP1_strategy)
def test_afptext::pgp1_XOset_type(instance):
    assert isinstance(instance.XOset, str)


@given(instance=afpText::PGP1_strategy)
def test_afptext::pgp1_XOset_setter(instance):
    original = instance.XOset
    instance.XOset = original
    assert instance.XOset == original

@given(instance=afpText::PGPRG_strategy)
@settings(max_examples=50)
def test_afptext::pgprg_instantiation(instance):
    assert isinstance(instance, afpText::PGPRG)

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_YmOset_type(instance):
    assert isinstance(instance.YmOset, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_YmOset_setter(instance):
    original = instance.YmOset
    instance.YmOset = original
    assert instance.YmOset == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_XmOset_type(instance):
    assert isinstance(instance.XmOset, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_XmOset_setter(instance):
    original = instance.XmOset
    instance.XmOset = original
    assert instance.XmOset == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PMCid_type(instance):
    assert isinstance(instance.PMCid, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PMCid_setter(instance):
    original = instance.PMCid
    instance.PMCid = original
    assert instance.PMCid == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PGorient_type(instance):
    assert isinstance(instance.PGorient, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PGorient_setter(instance):
    original = instance.PGorient
    instance.PGorient = original
    assert instance.PGorient == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PgFlgs_type(instance):
    assert isinstance(instance.PgFlgs, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_PgFlgs_setter(instance):
    original = instance.PgFlgs
    instance.PgFlgs = original
    assert instance.PgFlgs == original

@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_SHside_type(instance):
    assert isinstance(instance.SHside, str)


@given(instance=afpText::PGPRG_strategy)
def test_afptext::pgprg_SHside_setter(instance):
    original = instance.SHside
    instance.SHside = original
    assert instance.SHside == original

@given(instance=afpText::NOP_strategy)
@settings(max_examples=50)
def test_afptext::nop_instantiation(instance):
    assert isinstance(instance, afpText::NOP)

@given(instance=afpText::NOP_strategy)
def test_afptext::nop_UndfData_type(instance):
    assert isinstance(instance.UndfData, str)


@given(instance=afpText::NOP_strategy)
def test_afptext::nop_UndfData_setter(instance):
    original = instance.UndfData
    instance.UndfData = original
    assert instance.UndfData == original

@given(instance=afpText::MSURG_strategy)
@settings(max_examples=50)
def test_afptext::msurg_instantiation(instance):
    assert isinstance(instance, afpText::MSURG)

@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_SUPname_type(instance):
    assert isinstance(instance.SUPname, str)


@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_SUPname_setter(instance):
    original = instance.SUPname
    instance.SUPname = original
    assert instance.SUPname == original

@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_SUPid_type(instance):
    assert isinstance(instance.SUPid, str)


@given(instance=afpText::MSURG_strategy)
def test_afptext::msurg_SUPid_setter(instance):
    original = instance.SUPid
    instance.SUPid = original
    assert instance.SUPid == original

@given(instance=afpText::MSU_strategy)
@settings(max_examples=50)
def test_afptext::msu_instantiation(instance):
    assert isinstance(instance, afpText::MSU)

@given(instance=afpText::PGD_strategy)
@settings(max_examples=50)
def test_afptext::pgd_instantiation(instance):
    assert isinstance(instance, afpText::PGD)

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgBase_type(instance):
    assert isinstance(instance.XpgBase, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgBase_setter(instance):
    original = instance.XpgBase
    instance.XpgBase = original
    assert instance.XpgBase == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgSize_type(instance):
    assert isinstance(instance.YpgSize, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgSize_setter(instance):
    original = instance.YpgSize
    instance.YpgSize = original
    assert instance.YpgSize == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgUnits_type(instance):
    assert isinstance(instance.XpgUnits, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgUnits_setter(instance):
    original = instance.XpgUnits
    instance.XpgUnits = original
    assert instance.XpgUnits == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgUnits_type(instance):
    assert isinstance(instance.YpgUnits, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgUnits_setter(instance):
    original = instance.YpgUnits
    instance.YpgUnits = original
    assert instance.YpgUnits == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgBase_type(instance):
    assert isinstance(instance.YpgBase, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_YpgBase_setter(instance):
    original = instance.YpgBase
    instance.YpgBase = original
    assert instance.YpgBase == original

@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgSize_type(instance):
    assert isinstance(instance.XpgSize, str)


@given(instance=afpText::PGD_strategy)
def test_afptext::pgd_XpgSize_setter(instance):
    original = instance.XpgSize
    instance.XpgSize = original
    assert instance.XpgSize == original

@given(instance=afpText::PFC_strategy)
@settings(max_examples=50)
def test_afptext::pfc_instantiation(instance):
    assert isinstance(instance, afpText::PFC)

@given(instance=afpText::PFC_strategy)
def test_afptext::pfc_PFCFlgs_type(instance):
    assert isinstance(instance.PFCFlgs, str)


@given(instance=afpText::PFC_strategy)
def test_afptext::pfc_PFCFlgs_setter(instance):
    original = instance.PFCFlgs
    instance.PFCFlgs = original
    assert instance.PFCFlgs == original

@given(instance=afpText::PEC_strategy)
@settings(max_examples=50)
def test_afptext::pec_instantiation(instance):
    assert isinstance(instance, afpText::PEC)

@given(instance=afpText::OCD_strategy)
@settings(max_examples=50)
def test_afptext::ocd_instantiation(instance):
    assert isinstance(instance, afpText::OCD)

@given(instance=afpText::OCD_strategy)
def test_afptext::ocd_ObjCdat_type(instance):
    assert isinstance(instance.ObjCdat, str)


@given(instance=afpText::OCD_strategy)
def test_afptext::ocd_ObjCdat_setter(instance):
    original = instance.ObjCdat
    instance.ObjCdat = original
    assert instance.ObjCdat == original

@given(instance=afpText::OBP_strategy)
@settings(max_examples=50)
def test_afptext::obp_instantiation(instance):
    assert isinstance(instance, afpText::OBP)

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YocaOrent_type(instance):
    assert isinstance(instance.YocaOrent, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YocaOrent_setter(instance):
    original = instance.YocaOrent
    instance.YocaOrent = original
    assert instance.YocaOrent == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XocaOrent_type(instance):
    assert isinstance(instance.XocaOrent, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XocaOrent_setter(instance):
    original = instance.XocaOrent
    instance.XocaOrent = original
    assert instance.XocaOrent == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YocaOset_type(instance):
    assert isinstance(instance.YocaOset, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YoaOrent_type(instance):
    assert isinstance(instance.YoaOrent, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XocaOset_type(instance):
    assert isinstance(instance.XocaOset, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_RefCSys_type(instance):
    assert isinstance(instance.RefCSys, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_RefCSys_setter(instance):
    original = instance.RefCSys
    instance.RefCSys = original
    assert instance.RefCSys == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XoaOrent_type(instance):
    assert isinstance(instance.XoaOrent, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YoaOset_type(instance):
    assert isinstance(instance.YoaOset, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XoaOset_type(instance):
    assert isinstance(instance.XoaOset, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original

@given(instance=afpText::OBP_strategy)
def test_afptext::obp_OAPosID_type(instance):
    assert isinstance(instance.OAPosID, str)


@given(instance=afpText::OBP_strategy)
def test_afptext::obp_OAPosID_setter(instance):
    original = instance.OAPosID
    instance.OAPosID = original
    assert instance.OAPosID == original

@given(instance=afpText::OBD_strategy)
@settings(max_examples=50)
def test_afptext::obd_instantiation(instance):
    assert isinstance(instance, afpText::OBD)

@given(instance=afpText::MGO_strategy)
@settings(max_examples=50)
def test_afptext::mgo_instantiation(instance):
    assert isinstance(instance, afpText::MGO)

@given(instance=afpText::MPSRG_strategy)
@settings(max_examples=50)
def test_afptext::mpsrg_instantiation(instance):
    assert isinstance(instance, afpText::MPSRG)

@given(instance=afpText::MPSRG_strategy)
def test_afptext::mpsrg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::MPSRG_strategy)
def test_afptext::mpsrg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::MPSRG_strategy)
def test_afptext::mpsrg_PsegName_type(instance):
    assert isinstance(instance.PsegName, str)


@given(instance=afpText::MPSRG_strategy)
def test_afptext::mpsrg_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText::MPS_strategy)
@settings(max_examples=50)
def test_afptext::mps_instantiation(instance):
    assert isinstance(instance, afpText::MPS)

@given(instance=afpText::MPS_strategy)
def test_afptext::mps_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::MPS_strategy)
def test_afptext::mps_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::MPS_strategy)
def test_afptext::mps_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MPS_strategy)
def test_afptext::mps_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MPORG_strategy)
@settings(max_examples=50)
def test_afptext::mporg_instantiation(instance):
    assert isinstance(instance, afpText::MPORG)

@given(instance=afpText::MPORG_strategy)
def test_afptext::mporg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MPORG_strategy)
def test_afptext::mporg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MPO_strategy)
@settings(max_examples=50)
def test_afptext::mpo_instantiation(instance):
    assert isinstance(instance, afpText::MPO)

@given(instance=afpText::MPGRG_strategy)
@settings(max_examples=50)
def test_afptext::mpgrg_instantiation(instance):
    assert isinstance(instance, afpText::MPGRG)

@given(instance=afpText::MPGRG_strategy)
def test_afptext::mpgrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MPGRG_strategy)
def test_afptext::mpgrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MPG_strategy)
@settings(max_examples=50)
def test_afptext::mpg_instantiation(instance):
    assert isinstance(instance, afpText::MPG)

@given(instance=afpText::MMTRG_strategy)
@settings(max_examples=50)
def test_afptext::mmtrg_instantiation(instance):
    assert isinstance(instance, afpText::MMTRG)

@given(instance=afpText::MMTRG_strategy)
def test_afptext::mmtrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MMTRG_strategy)
def test_afptext::mmtrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MMT_strategy)
@settings(max_examples=50)
def test_afptext::mmt_instantiation(instance):
    assert isinstance(instance, afpText::MMT)

@given(instance=afpText::MMORG_strategy)
@settings(max_examples=50)
def test_afptext::mmorg_instantiation(instance):
    assert isinstance(instance, afpText::MMORG)

@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_OVLname_type(instance):
    assert isinstance(instance.OVLname, str)


@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_OVLname_setter(instance):
    original = instance.OVLname
    instance.OVLname = original
    assert instance.OVLname == original

@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_OVLid_type(instance):
    assert isinstance(instance.OVLid, str)


@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_OVLid_setter(instance):
    original = instance.OVLid
    instance.OVLid = original
    assert instance.OVLid == original

@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_Flags_type(instance):
    assert isinstance(instance.Flags, str)


@given(instance=afpText::MMORG_strategy)
def test_afptext::mmorg_Flags_setter(instance):
    original = instance.Flags
    instance.Flags = original
    assert instance.Flags == original

@given(instance=afpText::MMO_strategy)
@settings(max_examples=50)
def test_afptext::mmo_instantiation(instance):
    assert isinstance(instance, afpText::MMO)

@given(instance=afpText::MMO_strategy)
def test_afptext::mmo_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MMO_strategy)
def test_afptext::mmo_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MMDRG_strategy)
@settings(max_examples=50)
def test_afptext::mmdrg_instantiation(instance):
    assert isinstance(instance, afpText::MMDRG)

@given(instance=afpText::MMDRG_strategy)
def test_afptext::mmdrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MMDRG_strategy)
def test_afptext::mmdrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MMD_strategy)
@settings(max_examples=50)
def test_afptext::mmd_instantiation(instance):
    assert isinstance(instance, afpText::MMD)

@given(instance=afpText::MMCRG_strategy)
@settings(max_examples=50)
def test_afptext::mmcrg_instantiation(instance):
    assert isinstance(instance, afpText::MMCRG)

@given(instance=afpText::MMCRG_strategy)
def test_afptext::mmcrg_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=afpText::MMCRG_strategy)
def test_afptext::mmcrg_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=afpText::MMCRG_strategy)
def test_afptext::mmcrg_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=afpText::MMCRG_strategy)
def test_afptext::mmcrg_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=afpText::MMC_strategy)
@settings(max_examples=50)
def test_afptext::mmc_instantiation(instance):
    assert isinstance(instance, afpText::MMC)

@given(instance=afpText::MMC_strategy)
def test_afptext::mmc_MMCid_type(instance):
    assert isinstance(instance.MMCid, str)


@given(instance=afpText::MMC_strategy)
def test_afptext::mmc_MMCid_setter(instance):
    original = instance.MMCid
    instance.MMCid = original
    assert instance.MMCid == original

@given(instance=afpText::MMC_strategy)
def test_afptext::mmc_PARAMETER1_type(instance):
    assert isinstance(instance.PARAMETER1, str)


@given(instance=afpText::MMC_strategy)
def test_afptext::mmc_PARAMETER1_setter(instance):
    original = instance.PARAMETER1
    instance.PARAMETER1 = original
    assert instance.PARAMETER1 == original

@given(instance=afpText::MIORG_strategy)
@settings(max_examples=50)
def test_afptext::miorg_instantiation(instance):
    assert isinstance(instance, afpText::MIORG)

@given(instance=afpText::MIORG_strategy)
def test_afptext::miorg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MIORG_strategy)
def test_afptext::miorg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MIO_strategy)
@settings(max_examples=50)
def test_afptext::mio_instantiation(instance):
    assert isinstance(instance, afpText::MIO)

@given(instance=afpText::MGORG_strategy)
@settings(max_examples=50)
def test_afptext::mgorg_instantiation(instance):
    assert isinstance(instance, afpText::MGORG)

@given(instance=afpText::MGORG_strategy)
def test_afptext::mgorg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MGORG_strategy)
def test_afptext::mgorg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MCC_strategy)
@settings(max_examples=50)
def test_afptext::mcc_instantiation(instance):
    assert isinstance(instance, afpText::MCC)

@given(instance=afpText::MCARG_strategy)
@settings(max_examples=50)
def test_afptext::mcarg_instantiation(instance):
    assert isinstance(instance, afpText::MCARG)

@given(instance=afpText::MCARG_strategy)
def test_afptext::mcarg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MCARG_strategy)
def test_afptext::mcarg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MCA_strategy)
@settings(max_examples=50)
def test_afptext::mca_instantiation(instance):
    assert isinstance(instance, afpText::MCA)

@given(instance=afpText::MFC_strategy)
@settings(max_examples=50)
def test_afptext::mfc_instantiation(instance):
    assert isinstance(instance, afpText::MFC)

@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MFCScpe_type(instance):
    assert isinstance(instance.MFCScpe, str)


@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MFCScpe_setter(instance):
    original = instance.MFCScpe
    instance.MFCScpe = original
    assert instance.MFCScpe == original

@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MedColl_type(instance):
    assert isinstance(instance.MedColl, str)


@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MedColl_setter(instance):
    original = instance.MedColl
    instance.MedColl = original
    assert instance.MedColl == original

@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MFCFlgs_type(instance):
    assert isinstance(instance.MFCFlgs, str)


@given(instance=afpText::MFC_strategy)
def test_afptext::mfc_MFCFlgs_setter(instance):
    original = instance.MFCFlgs
    instance.MFCFlgs = original
    assert instance.MFCFlgs == original

@given(instance=afpText::MDRRG_strategy)
@settings(max_examples=50)
def test_afptext::mdrrg_instantiation(instance):
    assert isinstance(instance, afpText::MDRRG)

@given(instance=afpText::MDRRG_strategy)
def test_afptext::mdrrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MDRRG_strategy)
def test_afptext::mdrrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MDR_strategy)
@settings(max_examples=50)
def test_afptext::mdr_instantiation(instance):
    assert isinstance(instance, afpText::MDR)

@given(instance=afpText::MDD_strategy)
@settings(max_examples=50)
def test_afptext::mdd_instantiation(instance):
    assert isinstance(instance, afpText::MDD)

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmSize_type(instance):
    assert isinstance(instance.XmSize, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmSize_setter(instance):
    original = instance.XmSize
    instance.XmSize = original
    assert instance.XmSize == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_MDDFlgs_type(instance):
    assert isinstance(instance.MDDFlgs, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_MDDFlgs_setter(instance):
    original = instance.MDDFlgs
    instance.MDDFlgs = original
    assert instance.MDDFlgs == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmBase_type(instance):
    assert isinstance(instance.YmBase, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmBase_setter(instance):
    original = instance.YmBase
    instance.YmBase = original
    assert instance.YmBase == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmUnits_type(instance):
    assert isinstance(instance.YmUnits, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmUnits_setter(instance):
    original = instance.YmUnits
    instance.YmUnits = original
    assert instance.YmUnits == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmSize_type(instance):
    assert isinstance(instance.YmSize, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_YmSize_setter(instance):
    original = instance.YmSize
    instance.YmSize = original
    assert instance.YmSize == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmUnits_type(instance):
    assert isinstance(instance.XmUnits, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmUnits_setter(instance):
    original = instance.XmUnits
    instance.XmUnits = original
    assert instance.XmUnits == original

@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmBase_type(instance):
    assert isinstance(instance.XmBase, str)


@given(instance=afpText::MDD_strategy)
def test_afptext::mdd_XmBase_setter(instance):
    original = instance.XmBase
    instance.XmBase = original
    assert instance.XmBase == original

@given(instance=afpText::MCF1RG_strategy)
@settings(max_examples=50)
def test_afptext::mcf1rg_instantiation(instance):
    assert isinstance(instance, afpText::MCF1RG)

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CFLid_type(instance):
    assert isinstance(instance.CFLid, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CFLid_setter(instance):
    original = instance.CFLid
    instance.CFLid = original
    assert instance.CFLid == original

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CPName_type(instance):
    assert isinstance(instance.CPName, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CPName_setter(instance):
    original = instance.CPName
    instance.CPName = original
    assert instance.CPName == original

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CharRot_type(instance):
    assert isinstance(instance.CharRot, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_Sectid_type(instance):
    assert isinstance(instance.Sectid, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_Sectid_setter(instance):
    original = instance.Sectid
    instance.Sectid = original
    assert instance.Sectid == original

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CFName_type(instance):
    assert isinstance(instance.CFName, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_CFName_setter(instance):
    original = instance.CFName
    instance.CFName = original
    assert instance.CFName == original

@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_FCSName_type(instance):
    assert isinstance(instance.FCSName, str)


@given(instance=afpText::MCF1RG_strategy)
def test_afptext::mcf1rg_FCSName_setter(instance):
    original = instance.FCSName
    instance.FCSName = original
    assert instance.FCSName == original

@given(instance=afpText::MCF1_strategy)
@settings(max_examples=50)
def test_afptext::mcf1_instantiation(instance):
    assert isinstance(instance, afpText::MCF1)

@given(instance=afpText::MCF1_strategy)
def test_afptext::mcf1_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MCF1_strategy)
def test_afptext::mcf1_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MCFRG_strategy)
@settings(max_examples=50)
def test_afptext::mcfrg_instantiation(instance):
    assert isinstance(instance, afpText::MCFRG)

@given(instance=afpText::MCFRG_strategy)
def test_afptext::mcfrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MCFRG_strategy)
def test_afptext::mcfrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MCF_strategy)
@settings(max_examples=50)
def test_afptext::mcf_instantiation(instance):
    assert isinstance(instance, afpText::MCF)

@given(instance=afpText::MCDRG_strategy)
@settings(max_examples=50)
def test_afptext::mcdrg_instantiation(instance):
    assert isinstance(instance, afpText::MCDRG)

@given(instance=afpText::MCDRG_strategy)
def test_afptext::mcdrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MCDRG_strategy)
def test_afptext::mcdrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MCD_strategy)
@settings(max_examples=50)
def test_afptext::mcd_instantiation(instance):
    assert isinstance(instance, afpText::MCD)

@given(instance=afpText::MCCRG_strategy)
@settings(max_examples=50)
def test_afptext::mccrg_instantiation(instance):
    assert isinstance(instance, afpText::MCCRG)

@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_Startnum_type(instance):
    assert isinstance(instance.Startnum, str)


@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_Startnum_setter(instance):
    original = instance.Startnum
    instance.Startnum = original
    assert instance.Startnum == original

@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_Stopnum_type(instance):
    assert isinstance(instance.Stopnum, str)


@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_Stopnum_setter(instance):
    original = instance.Stopnum
    instance.Stopnum = original
    assert instance.Stopnum == original

@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_MMCid_type(instance):
    assert isinstance(instance.MMCid, str)


@given(instance=afpText::MCCRG_strategy)
def test_afptext::mccrg_MMCid_setter(instance):
    original = instance.MMCid
    instance.MMCid = original
    assert instance.MMCid == original

@given(instance=afpText::LLE_strategy)
@settings(max_examples=50)
def test_afptext::lle_instantiation(instance):
    assert isinstance(instance, afpText::LLE)

@given(instance=afpText::LLE_strategy)
def test_afptext::lle_LnkType_type(instance):
    assert isinstance(instance.LnkType, str)


@given(instance=afpText::LLE_strategy)
def test_afptext::lle_LnkType_setter(instance):
    original = instance.LnkType
    instance.LnkType = original
    assert instance.LnkType == original

@given(instance=afpText::MBCRG_strategy)
@settings(max_examples=50)
def test_afptext::mbcrg_instantiation(instance):
    assert isinstance(instance, afpText::MBCRG)

@given(instance=afpText::MBCRG_strategy)
def test_afptext::mbcrg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::MBCRG_strategy)
def test_afptext::mbcrg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::MBC_strategy)
@settings(max_examples=50)
def test_afptext::mbc_instantiation(instance):
    assert isinstance(instance, afpText::MBC)

@given(instance=afpText::LND_strategy)
@settings(max_examples=50)
def test_afptext::lnd_instantiation(instance):
    assert isinstance(instance, afpText::LND)

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_TxtOrent_type(instance):
    assert isinstance(instance.TxtOrent, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_TxtOrent_setter(instance):
    original = instance.TxtOrent
    instance.TxtOrent = original
    assert instance.TxtOrent == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SubpgID_type(instance):
    assert isinstance(instance.SubpgID, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SubpgID_setter(instance):
    original = instance.SubpgID
    instance.SubpgID = original
    assert instance.SubpgID == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_DataLgth_type(instance):
    assert isinstance(instance.DataLgth, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_DataLgth_setter(instance):
    original = instance.DataLgth
    instance.DataLgth = original
    assert instance.DataLgth == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDskp_type(instance):
    assert isinstance(instance.NLNDskp, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDskp_setter(instance):
    original = instance.NLNDskp
    instance.NLNDskp = original
    assert instance.NLNDskp == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_ChnlCde_type(instance):
    assert isinstance(instance.ChnlCde, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_ChnlCde_setter(instance):
    original = instance.ChnlCde
    instance.ChnlCde = original
    assert instance.ChnlCde == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SupName_type(instance):
    assert isinstance(instance.SupName, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SupName_setter(instance):
    original = instance.SupName
    instance.SupName = original
    assert instance.SupName == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDreu_type(instance):
    assert isinstance(instance.NLNDreu, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDreu_setter(instance):
    original = instance.NLNDreu
    instance.NLNDreu = original
    assert instance.NLNDreu == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_LNDFlgs_type(instance):
    assert isinstance(instance.LNDFlgs, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_LNDFlgs_setter(instance):
    original = instance.LNDFlgs
    instance.LNDFlgs = original
    assert instance.LNDFlgs == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_CCPID_type(instance):
    assert isinstance(instance.CCPID, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_CCPID_setter(instance):
    original = instance.CCPID
    instance.CCPID = original
    assert instance.CCPID == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_TxtColor_type(instance):
    assert isinstance(instance.TxtColor, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_TxtColor_setter(instance):
    original = instance.TxtColor
    instance.TxtColor = original
    assert instance.TxtColor == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDsp_type(instance):
    assert isinstance(instance.NLNDsp, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDsp_setter(instance):
    original = instance.NLNDsp
    instance.NLNDsp = original
    assert instance.NLNDsp == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SOLid_type(instance):
    assert isinstance(instance.SOLid, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_SOLid_setter(instance):
    original = instance.SOLid
    instance.SOLid = original
    assert instance.SOLid == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_FntLID_type(instance):
    assert isinstance(instance.FntLID, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_FntLID_setter(instance):
    original = instance.FntLID
    instance.FntLID = original
    assert instance.FntLID == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_BPos_type(instance):
    assert isinstance(instance.BPos, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_BPos_setter(instance):
    original = instance.BPos
    instance.BPos = original
    assert instance.BPos == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_IPos_type(instance):
    assert isinstance(instance.IPos, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_IPos_setter(instance):
    original = instance.IPos
    instance.IPos = original
    assert instance.IPos == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDccp_type(instance):
    assert isinstance(instance.NLNDccp, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_NLNDccp_setter(instance):
    original = instance.NLNDccp
    instance.NLNDccp = original
    assert instance.NLNDccp == original

@given(instance=afpText::LND_strategy)
def test_afptext::lnd_DataStrt_type(instance):
    assert isinstance(instance.DataStrt, str)


@given(instance=afpText::LND_strategy)
def test_afptext::lnd_DataStrt_setter(instance):
    original = instance.DataStrt
    instance.DataStrt = original
    assert instance.DataStrt == original

@given(instance=afpText::LNC_strategy)
@settings(max_examples=50)
def test_afptext::lnc_instantiation(instance):
    assert isinstance(instance, afpText::LNC)

@given(instance=afpText::LNC_strategy)
def test_afptext::lnc_NumDSC_type(instance):
    assert isinstance(instance.NumDSC, str)


@given(instance=afpText::LNC_strategy)
def test_afptext::lnc_NumDSC_setter(instance):
    original = instance.NumDSC
    instance.NumDSC = original
    assert instance.NumDSC == original

@given(instance=afpText::LLERG_strategy)
@settings(max_examples=50)
def test_afptext::llerg_instantiation(instance):
    assert isinstance(instance, afpText::LLERG)

@given(instance=afpText::LLERG_strategy)
def test_afptext::llerg_RGLength_type(instance):
    assert isinstance(instance.RGLength, str)


@given(instance=afpText::LLERG_strategy)
def test_afptext::llerg_RGLength_setter(instance):
    original = instance.RGLength
    instance.RGLength = original
    assert instance.RGLength == original

@given(instance=afpText::LLERG_strategy)
def test_afptext::llerg_RGFunct_type(instance):
    assert isinstance(instance.RGFunct, str)


@given(instance=afpText::LLERG_strategy)
def test_afptext::llerg_RGFunct_setter(instance):
    original = instance.RGFunct
    instance.RGFunct = original
    assert instance.RGFunct == original

@given(instance=afpText::IPO_strategy)
@settings(max_examples=50)
def test_afptext::ipo_instantiation(instance):
    assert isinstance(instance, afpText::IPO)

@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_XolOset_type(instance):
    assert isinstance(instance.XolOset, str)


@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_XolOset_setter(instance):
    original = instance.XolOset
    instance.XolOset = original
    assert instance.XolOset == original

@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_OvlyName_type(instance):
    assert isinstance(instance.OvlyName, str)


@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original

@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_OvlyOrent_type(instance):
    assert isinstance(instance.OvlyOrent, str)


@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_OvlyOrent_setter(instance):
    original = instance.OvlyOrent
    instance.OvlyOrent = original
    assert instance.OvlyOrent == original

@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_YolOset_type(instance):
    assert isinstance(instance.YolOset, str)


@given(instance=afpText::IPO_strategy)
def test_afptext::ipo_YolOset_setter(instance):
    original = instance.YolOset
    instance.YolOset = original
    assert instance.YolOset == original

@given(instance=afpText::IRD_strategy)
@settings(max_examples=50)
def test_afptext::ird_instantiation(instance):
    assert isinstance(instance, afpText::IRD)

@given(instance=afpText::IRD_strategy)
def test_afptext::ird_IMdata_type(instance):
    assert isinstance(instance.IMdata, str)


@given(instance=afpText::IRD_strategy)
def test_afptext::ird_IMdata_setter(instance):
    original = instance.IMdata
    instance.IMdata = original
    assert instance.IMdata == original

@given(instance=afpText::IPS_strategy)
@settings(max_examples=50)
def test_afptext::ips_instantiation(instance):
    assert isinstance(instance, afpText::IPS)

@given(instance=afpText::IPS_strategy)
def test_afptext::ips_YpsOset_type(instance):
    assert isinstance(instance.YpsOset, str)


@given(instance=afpText::IPS_strategy)
def test_afptext::ips_YpsOset_setter(instance):
    original = instance.YpsOset
    instance.YpsOset = original
    assert instance.YpsOset == original

@given(instance=afpText::IPS_strategy)
def test_afptext::ips_XpsOset_type(instance):
    assert isinstance(instance.XpsOset, str)


@given(instance=afpText::IPS_strategy)
def test_afptext::ips_XpsOset_setter(instance):
    original = instance.XpsOset
    instance.XpsOset = original
    assert instance.XpsOset == original

@given(instance=afpText::IPS_strategy)
def test_afptext::ips_PsegName_type(instance):
    assert isinstance(instance.PsegName, str)


@given(instance=afpText::IPS_strategy)
def test_afptext::ips_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText::IPG_strategy)
@settings(max_examples=50)
def test_afptext::ipg_instantiation(instance):
    assert isinstance(instance, afpText::IPG)

@given(instance=afpText::IPG_strategy)
def test_afptext::ipg_IPgFlgs_type(instance):
    assert isinstance(instance.IPgFlgs, str)


@given(instance=afpText::IPG_strategy)
def test_afptext::ipg_IPgFlgs_setter(instance):
    original = instance.IPgFlgs
    instance.IPgFlgs = original
    assert instance.IPgFlgs == original

@given(instance=afpText::IPG_strategy)
def test_afptext::ipg_PgName_type(instance):
    assert isinstance(instance.PgName, str)


@given(instance=afpText::IPG_strategy)
def test_afptext::ipg_PgName_setter(instance):
    original = instance.PgName
    instance.PgName = original
    assert instance.PgName == original

@given(instance=afpText::IPD_strategy)
@settings(max_examples=50)
def test_afptext::ipd_instantiation(instance):
    assert isinstance(instance, afpText::IPD)

@given(instance=afpText::IPD_strategy)
def test_afptext::ipd_imageData_type(instance):
    assert isinstance(instance.imageData, str)


@given(instance=afpText::IPD_strategy)
def test_afptext::ipd_imageData_setter(instance):
    original = instance.imageData
    instance.imageData = original
    assert instance.imageData == original

@given(instance=afpText::IPD_strategy)
def test_afptext::ipd_IOCAdat_type(instance):
    assert isinstance(instance.IOCAdat, str)


@given(instance=afpText::IPD_strategy)
def test_afptext::ipd_IOCAdat_setter(instance):
    original = instance.IOCAdat
    instance.IOCAdat = original
    assert instance.IOCAdat == original

@given(instance=afpText::ICP_strategy)
@settings(max_examples=50)
def test_afptext::icp_instantiation(instance):
    assert isinstance(instance, afpText::ICP)

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XFilSize_type(instance):
    assert isinstance(instance.XFilSize, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XFilSize_setter(instance):
    original = instance.XFilSize
    instance.XFilSize = original
    assert instance.XFilSize == original

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YFilSize_type(instance):
    assert isinstance(instance.YFilSize, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YFilSize_setter(instance):
    original = instance.YFilSize
    instance.YFilSize = original
    assert instance.YFilSize == original

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YCSize_type(instance):
    assert isinstance(instance.YCSize, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YCSize_setter(instance):
    original = instance.YCSize
    instance.YCSize = original
    assert instance.YCSize == original

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XCOset_type(instance):
    assert isinstance(instance.XCOset, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XCOset_setter(instance):
    original = instance.XCOset
    instance.XCOset = original
    assert instance.XCOset == original

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XCSize_type(instance):
    assert isinstance(instance.XCSize, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_XCSize_setter(instance):
    original = instance.XCSize
    instance.XCSize = original
    assert instance.XCSize == original

@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YCOset_type(instance):
    assert isinstance(instance.YCOset, str)


@given(instance=afpText::ICP_strategy)
def test_afptext::icp_YCOset_setter(instance):
    original = instance.YCOset
    instance.YCOset = original
    assert instance.YCOset == original

@given(instance=afpText::IOC_strategy)
@settings(max_examples=50)
def test_afptext::ioc_instantiation(instance):
    assert isinstance(instance, afpText::IOC)

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YoaOrent_type(instance):
    assert isinstance(instance.YoaOrent, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XoaOset_type(instance):
    assert isinstance(instance.XoaOset, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_ConData1_type(instance):
    assert isinstance(instance.ConData1, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_ConData1_setter(instance):
    original = instance.ConData1
    instance.ConData1 = original
    assert instance.ConData1 == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YoaOset_type(instance):
    assert isinstance(instance.YoaOset, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XMap_type(instance):
    assert isinstance(instance.XMap, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XMap_setter(instance):
    original = instance.XMap
    instance.XMap = original
    assert instance.XMap == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YMap_type(instance):
    assert isinstance(instance.YMap, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_YMap_setter(instance):
    original = instance.YMap
    instance.YMap = original
    assert instance.YMap == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XoaOrent_type(instance):
    assert isinstance(instance.XoaOrent, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original

@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_ConData2_type(instance):
    assert isinstance(instance.ConData2, str)


@given(instance=afpText::IOC_strategy)
def test_afptext::ioc_ConData2_setter(instance):
    original = instance.ConData2
    instance.ConData2 = original
    assert instance.ConData2 == original

@given(instance=afpText::IOB_strategy)
@settings(max_examples=50)
def test_afptext::iob_instantiation(instance):
    assert isinstance(instance, afpText::IOB)

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_ObjName_type(instance):
    assert isinstance(instance.ObjName, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_ObjName_setter(instance):
    original = instance.ObjName
    instance.ObjName = original
    assert instance.ObjName == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YoaOset_type(instance):
    assert isinstance(instance.YoaOset, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YoaOset_setter(instance):
    original = instance.YoaOset
    instance.YoaOset = original
    assert instance.YoaOset == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XoaOset_type(instance):
    assert isinstance(instance.XoaOset, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XoaOset_setter(instance):
    original = instance.XoaOset
    instance.XoaOset = original
    assert instance.XoaOset == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XocaOset_type(instance):
    assert isinstance(instance.XocaOset, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XocaOset_setter(instance):
    original = instance.XocaOset
    instance.XocaOset = original
    assert instance.XocaOset == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_ObjType_type(instance):
    assert isinstance(instance.ObjType, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_ObjType_setter(instance):
    original = instance.ObjType
    instance.ObjType = original
    assert instance.ObjType == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YocaOset_type(instance):
    assert isinstance(instance.YocaOset, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YocaOset_setter(instance):
    original = instance.YocaOset
    instance.YocaOset = original
    assert instance.YocaOset == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_RefCSys_type(instance):
    assert isinstance(instance.RefCSys, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_RefCSys_setter(instance):
    original = instance.RefCSys
    instance.RefCSys = original
    assert instance.RefCSys == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XoaOrent_type(instance):
    assert isinstance(instance.XoaOrent, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_XoaOrent_setter(instance):
    original = instance.XoaOrent
    instance.XoaOrent = original
    assert instance.XoaOrent == original

@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YoaOrent_type(instance):
    assert isinstance(instance.YoaOrent, str)


@given(instance=afpText::IOB_strategy)
def test_afptext::iob_YoaOrent_setter(instance):
    original = instance.YoaOrent
    instance.YoaOrent = original
    assert instance.YoaOrent == original

@given(instance=afpText::IMM_strategy)
@settings(max_examples=50)
def test_afptext::imm_instantiation(instance):
    assert isinstance(instance, afpText::IMM)

@given(instance=afpText::IMM_strategy)
def test_afptext::imm_MMPName_type(instance):
    assert isinstance(instance.MMPName, str)


@given(instance=afpText::IMM_strategy)
def test_afptext::imm_MMPName_setter(instance):
    original = instance.MMPName
    instance.MMPName = original
    assert instance.MMPName == original

@given(instance=afpText::IID_strategy)
@settings(max_examples=50)
def test_afptext::iid_instantiation(instance):
    assert isinstance(instance, afpText::IID)

@given(instance=afpText::IID_strategy)
def test_afptext::iid_YCSizeD_type(instance):
    assert isinstance(instance.YCSizeD, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_YCSizeD_setter(instance):
    original = instance.YCSizeD
    instance.YCSizeD = original
    assert instance.YCSizeD == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData2_type(instance):
    assert isinstance(instance.ConData2, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData2_setter(instance):
    original = instance.ConData2
    instance.ConData2 = original
    assert instance.ConData2 == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_XSize_type(instance):
    assert isinstance(instance.XSize, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_XSize_setter(instance):
    original = instance.XSize
    instance.XSize = original
    assert instance.XSize == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_XCSizeD_type(instance):
    assert isinstance(instance.XCSizeD, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_XCSizeD_setter(instance):
    original = instance.XCSizeD
    instance.XCSizeD = original
    assert instance.XCSizeD == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_YBase_type(instance):
    assert isinstance(instance.YBase, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_YBase_setter(instance):
    original = instance.YBase
    instance.YBase = original
    assert instance.YBase == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_YSize_type(instance):
    assert isinstance(instance.YSize, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_YSize_setter(instance):
    original = instance.YSize
    instance.YSize = original
    assert instance.YSize == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData1_type(instance):
    assert isinstance(instance.ConData1, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData1_setter(instance):
    original = instance.ConData1
    instance.ConData1 = original
    assert instance.ConData1 == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_YUnits_type(instance):
    assert isinstance(instance.YUnits, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_YUnits_setter(instance):
    original = instance.YUnits
    instance.YUnits = original
    assert instance.YUnits == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_XBase_type(instance):
    assert isinstance(instance.XBase, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_XBase_setter(instance):
    original = instance.XBase
    instance.XBase = original
    assert instance.XBase == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_XUnits_type(instance):
    assert isinstance(instance.XUnits, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_XUnits_setter(instance):
    original = instance.XUnits
    instance.XUnits = original
    assert instance.XUnits == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData3_type(instance):
    assert isinstance(instance.ConData3, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_ConData3_setter(instance):
    original = instance.ConData3
    instance.ConData3 = original
    assert instance.ConData3 == original

@given(instance=afpText::IID_strategy)
def test_afptext::iid_Color_type(instance):
    assert isinstance(instance.Color, str)


@given(instance=afpText::IID_strategy)
def test_afptext::iid_Color_setter(instance):
    original = instance.Color
    instance.Color = original
    assert instance.Color == original

@given(instance=afpText::IEL_strategy)
@settings(max_examples=50)
def test_afptext::iel_instantiation(instance):
    assert isinstance(instance, afpText::IEL)

@given(instance=afpText::IDD_strategy)
@settings(max_examples=50)
def test_afptext::idd_instantiation(instance):
    assert isinstance(instance, afpText::IDD)

@given(instance=afpText::IDD_strategy)
def test_afptext::idd_UNITBASE_type(instance):
    assert isinstance(instance.UNITBASE, str)


@given(instance=afpText::IDD_strategy)
def test_afptext::idd_UNITBASE_setter(instance):
    original = instance.UNITBASE
    instance.UNITBASE = original
    assert instance.UNITBASE == original

@given(instance=afpText::IDD_strategy)
def test_afptext::idd_XRESOL_type(instance):
    assert isinstance(instance.XRESOL, str)


@given(instance=afpText::IDD_strategy)
def test_afptext::idd_XRESOL_setter(instance):
    original = instance.XRESOL
    instance.XRESOL = original
    assert instance.XRESOL == original

@given(instance=afpText::IDD_strategy)
def test_afptext::idd_YRESOL_type(instance):
    assert isinstance(instance.YRESOL, str)


@given(instance=afpText::IDD_strategy)
def test_afptext::idd_YRESOL_setter(instance):
    original = instance.YRESOL
    instance.YRESOL = original
    assert instance.YRESOL == original

@given(instance=afpText::IDD_strategy)
def test_afptext::idd_XSIZE_type(instance):
    assert isinstance(instance.XSIZE, str)


@given(instance=afpText::IDD_strategy)
def test_afptext::idd_XSIZE_setter(instance):
    original = instance.XSIZE
    instance.XSIZE = original
    assert instance.XSIZE == original

@given(instance=afpText::IDD_strategy)
def test_afptext::idd_YSIZE_type(instance):
    assert isinstance(instance.YSIZE, str)


@given(instance=afpText::IDD_strategy)
def test_afptext::idd_YSIZE_setter(instance):
    original = instance.YSIZE
    instance.YSIZE = original
    assert instance.YSIZE == original

@given(instance=afpText::GDD_strategy)
@settings(max_examples=50)
def test_afptext::gdd_instantiation(instance):
    assert isinstance(instance, afpText::GDD)

@given(instance=afpText::GDD_strategy)
def test_afptext::gdd_GOCAdes_type(instance):
    assert isinstance(instance.GOCAdes, str)


@given(instance=afpText::GDD_strategy)
def test_afptext::gdd_GOCAdes_setter(instance):
    original = instance.GOCAdes
    instance.GOCAdes = original
    assert instance.GOCAdes == original

@given(instance=afpText::GAD_strategy)
@settings(max_examples=50)
def test_afptext::gad_instantiation(instance):
    assert isinstance(instance, afpText::GAD)

@given(instance=afpText::GAD_strategy)
def test_afptext::gad_GOCAdat_type(instance):
    assert isinstance(instance.GOCAdat, str)


@given(instance=afpText::GAD_strategy)
def test_afptext::gad_GOCAdat_setter(instance):
    original = instance.GOCAdat
    instance.GOCAdat = original
    assert instance.GOCAdat == original

@given(instance=afpText::FNPRG_strategy)
@settings(max_examples=50)
def test_afptext::fnprg_instantiation(instance):
    assert isinstance(instance, afpText::FNPRG)

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_MaxDesDp_type(instance):
    assert isinstance(instance.MaxDesDp, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_MaxDesDp_setter(instance):
    original = instance.MaxDesDp
    instance.MaxDesDp = original
    assert instance.MaxDesDp == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscoreWdf_type(instance):
    assert isinstance(instance.UscoreWdf, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscoreWdf_setter(instance):
    original = instance.UscoreWdf
    instance.UscoreWdf = original
    assert instance.UscoreWdf == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_MaxAscHt_type(instance):
    assert isinstance(instance.MaxAscHt, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_MaxAscHt_setter(instance):
    original = instance.MaxAscHt
    instance.MaxAscHt = original
    assert instance.MaxAscHt == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_LcHeight_type(instance):
    assert isinstance(instance.LcHeight, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_LcHeight_setter(instance):
    original = instance.LcHeight
    instance.LcHeight = original
    assert instance.LcHeight == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_CapMHt_type(instance):
    assert isinstance(instance.CapMHt, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_CapMHt_setter(instance):
    original = instance.CapMHt
    instance.CapMHt = original
    assert instance.CapMHt == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscorePos_type(instance):
    assert isinstance(instance.UscorePos, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscorePos_setter(instance):
    original = instance.UscorePos
    instance.UscorePos = original
    assert instance.UscorePos == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscoreWd_type(instance):
    assert isinstance(instance.UscoreWd, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_UscoreWd_setter(instance):
    original = instance.UscoreWd
    instance.UscoreWd = original
    assert instance.UscoreWd == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Retired_type(instance):
    assert isinstance(instance.Retired, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Retired_setter(instance):
    original = instance.Retired
    instance.Retired = original
    assert instance.Retired == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved3_type(instance):
    assert isinstance(instance.Reserved3, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved3_setter(instance):
    original = instance.Reserved3
    instance.Reserved3 = original
    assert instance.Reserved3 == original

@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::FNPRG_strategy)
def test_afptext::fnprg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::FNP_strategy)
@settings(max_examples=50)
def test_afptext::fnp_instantiation(instance):
    assert isinstance(instance, afpText::FNP)

@given(instance=afpText::FNORG_strategy)
@settings(max_examples=50)
def test_afptext::fnorg_instantiation(instance):
    assert isinstance(instance, afpText::FNORG)

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_OrntFlgs_type(instance):
    assert isinstance(instance.OrntFlgs, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_OrntFlgs_setter(instance):
    original = instance.OrntFlgs
    instance.OrntFlgs = original
    assert instance.OrntFlgs == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_NomCharInc_type(instance):
    assert isinstance(instance.NomCharInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_NomCharInc_setter(instance):
    original = instance.NomCharInc
    instance.NomCharInc = original
    assert instance.NomCharInc == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxCharInc_type(instance):
    assert isinstance(instance.MaxCharInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxCharInc_setter(instance):
    original = instance.MaxCharInc
    instance.MaxCharInc = original
    assert instance.MaxCharInc == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxBOset_type(instance):
    assert isinstance(instance.MaxBOset, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxBOset_setter(instance):
    original = instance.MaxBOset
    instance.MaxBOset = original
    assert instance.MaxBOset == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxBExt_type(instance):
    assert isinstance(instance.MaxBExt, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MaxBExt_setter(instance):
    original = instance.MaxBExt
    instance.MaxBExt = original
    assert instance.MaxBExt == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MinASp_type(instance):
    assert isinstance(instance.MinASp, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_MinASp_setter(instance):
    original = instance.MinASp
    instance.MinASp = original
    assert instance.MinASp == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_EmSpInc_type(instance):
    assert isinstance(instance.EmSpInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_EmSpInc_setter(instance):
    original = instance.EmSpInc
    instance.EmSpInc = original
    assert instance.EmSpInc == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_FigSpInc_type(instance):
    assert isinstance(instance.FigSpInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_FigSpInc_setter(instance):
    original = instance.FigSpInc
    instance.FigSpInc = original
    assert instance.FigSpInc == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_SpCharInc_type(instance):
    assert isinstance(instance.SpCharInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_SpCharInc_setter(instance):
    original = instance.SpCharInc
    instance.SpCharInc = original
    assert instance.SpCharInc == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved3_type(instance):
    assert isinstance(instance.Reserved3, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_Reserved3_setter(instance):
    original = instance.Reserved3
    instance.Reserved3 = original
    assert instance.Reserved3 == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_CharRot_type(instance):
    assert isinstance(instance.CharRot, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_CharRot_setter(instance):
    original = instance.CharRot
    instance.CharRot = original
    assert instance.CharRot == original

@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_DefBInc_type(instance):
    assert isinstance(instance.DefBInc, str)


@given(instance=afpText::FNORG_strategy)
def test_afptext::fnorg_DefBInc_setter(instance):
    original = instance.DefBInc
    instance.DefBInc = original
    assert instance.DefBInc == original

@given(instance=afpText::FNO_strategy)
@settings(max_examples=50)
def test_afptext::fno_instantiation(instance):
    assert isinstance(instance, afpText::FNO)

@given(instance=afpText::FNMRG_strategy)
@settings(max_examples=50)
def test_afptext::fnmrg_instantiation(instance):
    assert isinstance(instance, afpText::FNMRG)

@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_CharBoxWd_type(instance):
    assert isinstance(instance.CharBoxWd, str)


@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_CharBoxWd_setter(instance):
    original = instance.CharBoxWd
    instance.CharBoxWd = original
    assert instance.CharBoxWd == original

@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_PatDOset_type(instance):
    assert isinstance(instance.PatDOset, str)


@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_PatDOset_setter(instance):
    original = instance.PatDOset
    instance.PatDOset = original
    assert instance.PatDOset == original

@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_CharBoxHt_type(instance):
    assert isinstance(instance.CharBoxHt, str)


@given(instance=afpText::FNMRG_strategy)
def test_afptext::fnmrg_CharBoxHt_setter(instance):
    original = instance.CharBoxHt
    instance.CharBoxHt = original
    assert instance.CharBoxHt == original

@given(instance=afpText::FNM_strategy)
@settings(max_examples=50)
def test_afptext::fnm_instantiation(instance):
    assert isinstance(instance, afpText::FNM)

@given(instance=afpText::FNN_strategy)
@settings(max_examples=50)
def test_afptext::fnn_instantiation(instance):
    assert isinstance(instance, afpText::FNN)

@given(instance=afpText::FNN_strategy)
def test_afptext::fnn_FNNData_type(instance):
    assert isinstance(instance.FNNData, str)


@given(instance=afpText::FNN_strategy)
def test_afptext::fnn_FNNData_setter(instance):
    original = instance.FNNData
    instance.FNNData = original
    assert instance.FNNData == original

@given(instance=afpText::FNIRG_strategy)
@settings(max_examples=50)
def test_afptext::fnirg_instantiation(instance):
    assert isinstance(instance, afpText::FNIRG)

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_BSpace_type(instance):
    assert isinstance(instance.BSpace, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_BSpace_setter(instance):
    original = instance.BSpace
    instance.BSpace = original
    assert instance.BSpace == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_DescendDp_type(instance):
    assert isinstance(instance.DescendDp, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_DescendDp_setter(instance):
    original = instance.DescendDp
    instance.DescendDp = original
    assert instance.DescendDp == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_GCGID_type(instance):
    assert isinstance(instance.GCGID, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_ASpace_type(instance):
    assert isinstance(instance.ASpace, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_ASpace_setter(instance):
    original = instance.ASpace
    instance.ASpace = original
    assert instance.ASpace == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_FNMCnt_type(instance):
    assert isinstance(instance.FNMCnt, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_FNMCnt_setter(instance):
    original = instance.FNMCnt
    instance.FNMCnt = original
    assert instance.FNMCnt == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_CharInc_type(instance):
    assert isinstance(instance.CharInc, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_CharInc_setter(instance):
    original = instance.CharInc
    instance.CharInc = original
    assert instance.CharInc == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_BaseOset_type(instance):
    assert isinstance(instance.BaseOset, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_BaseOset_setter(instance):
    original = instance.BaseOset
    instance.BaseOset = original
    assert instance.BaseOset == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_CSpace_type(instance):
    assert isinstance(instance.CSpace, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_CSpace_setter(instance):
    original = instance.CSpace
    instance.CSpace = original
    assert instance.CSpace == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_AscendHt_type(instance):
    assert isinstance(instance.AscendHt, str)


@given(instance=afpText::FNIRG_strategy)
def test_afptext::fnirg_AscendHt_setter(instance):
    original = instance.AscendHt
    instance.AscendHt = original
    assert instance.AscendHt == original

@given(instance=afpText::FNI_strategy)
@settings(max_examples=50)
def test_afptext::fni_instantiation(instance):
    assert isinstance(instance, afpText::FNI)

@given(instance=afpText::FNG_strategy)
@settings(max_examples=50)
def test_afptext::fng_instantiation(instance):
    assert isinstance(instance, afpText::FNG)

@given(instance=afpText::FNG_strategy)
def test_afptext::fng_PatData_type(instance):
    assert isinstance(instance.PatData, str)


@given(instance=afpText::FNG_strategy)
def test_afptext::fng_PatData_setter(instance):
    original = instance.PatData
    instance.PatData = original
    assert instance.PatData == original

@given(instance=afpText::EPT_strategy)
@settings(max_examples=50)
def test_afptext::ept_instantiation(instance):
    assert isinstance(instance, afpText::EPT)

@given(instance=afpText::EPT_strategy)
def test_afptext::ept_PTdoName_type(instance):
    assert isinstance(instance.PTdoName, str)


@given(instance=afpText::EPT_strategy)
def test_afptext::ept_PTdoName_setter(instance):
    original = instance.PTdoName
    instance.PTdoName = original
    assert instance.PTdoName == original

@given(instance=afpText::FND_strategy)
@settings(max_examples=50)
def test_afptext::fnd_instantiation(instance):
    assert isinstance(instance, afpText::FND)

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtDsFlags_type(instance):
    assert isinstance(instance.FtDsFlags, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtDsFlags_setter(instance):
    original = instance.FtDsFlags
    instance.FtDsFlags = original
    assert instance.FtDsFlags == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MinHSize_type(instance):
    assert isinstance(instance.MinHSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MinHSize_setter(instance):
    original = instance.MinHSize
    instance.MinHSize = original
    assert instance.MinHSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnSpcGrp_type(instance):
    assert isinstance(instance.DsnSpcGrp, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnSpcGrp_setter(instance):
    original = instance.DsnSpcGrp
    instance.DsnSpcGrp = original
    assert instance.DsnSpcGrp == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtWdClass_type(instance):
    assert isinstance(instance.FtWdClass, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtWdClass_setter(instance):
    original = instance.FtWdClass
    instance.FtWdClass = original
    assert instance.FtWdClass == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_Reserved1_type(instance):
    assert isinstance(instance.Reserved1, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_Reserved1_setter(instance):
    original = instance.Reserved1
    instance.Reserved1 = original
    assert instance.Reserved1 == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MaxHSize_type(instance):
    assert isinstance(instance.MaxHSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MaxHSize_setter(instance):
    original = instance.MaxHSize
    instance.MaxHSize = original
    assert instance.MaxHSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_TypeFcDesc_type(instance):
    assert isinstance(instance.TypeFcDesc, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_TypeFcDesc_setter(instance):
    original = instance.TypeFcDesc
    instance.TypeFcDesc = original
    assert instance.TypeFcDesc == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MaxPtSize_type(instance):
    assert isinstance(instance.MaxPtSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MaxPtSize_setter(instance):
    original = instance.MaxPtSize
    instance.MaxPtSize = original
    assert instance.MaxPtSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnGenCls_type(instance):
    assert isinstance(instance.DsnGenCls, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnGenCls_setter(instance):
    original = instance.DsnGenCls
    instance.DsnGenCls = original
    assert instance.DsnGenCls == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_NomHSize_type(instance):
    assert isinstance(instance.NomHSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_NomHSize_setter(instance):
    original = instance.NomHSize
    instance.NomHSize = original
    assert instance.NomHSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FGID_type(instance):
    assert isinstance(instance.FGID, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FGID_setter(instance):
    original = instance.FGID
    instance.FGID = original
    assert instance.FGID == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_NomPtSize_type(instance):
    assert isinstance(instance.NomPtSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_NomPtSize_setter(instance):
    original = instance.NomPtSize
    instance.NomPtSize = original
    assert instance.NomPtSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MinPtSize_type(instance):
    assert isinstance(instance.MinPtSize, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_MinPtSize_setter(instance):
    original = instance.MinPtSize
    instance.MinPtSize = original
    assert instance.MinPtSize == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnSubCls_type(instance):
    assert isinstance(instance.DsnSubCls, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_DsnSubCls_setter(instance):
    original = instance.DsnSubCls
    instance.DsnSubCls = original
    assert instance.DsnSubCls == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_GCSID_type(instance):
    assert isinstance(instance.GCSID, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_GCSID_setter(instance):
    original = instance.GCSID
    instance.GCSID = original
    assert instance.GCSID == original

@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtWtClass_type(instance):
    assert isinstance(instance.FtWtClass, str)


@given(instance=afpText::FND_strategy)
def test_afptext::fnd_FtWtClass_setter(instance):
    original = instance.FtWtClass
    instance.FtWtClass = original
    assert instance.FtWtClass == original

@given(instance=afpText::FNC_strategy)
@settings(max_examples=50)
def test_afptext::fnc_instantiation(instance):
    assert isinstance(instance, afpText::FNC)

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_MaxBoxHt_type(instance):
    assert isinstance(instance.MaxBoxHt, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_MaxBoxHt_setter(instance):
    original = instance.MaxBoxHt
    instance.MaxBoxHt = original
    assert instance.MaxBoxHt == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_ResYUBase_type(instance):
    assert isinstance(instance.ResYUBase, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_ResYUBase_setter(instance):
    original = instance.ResYUBase
    instance.ResYUBase = original
    assert instance.ResYUBase == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Reserved1_type(instance):
    assert isinstance(instance.Reserved1, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Reserved1_setter(instance):
    original = instance.Reserved1
    instance.Reserved1 = original
    assert instance.Reserved1 == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_PatTech_type(instance):
    assert isinstance(instance.PatTech, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_PatTech_setter(instance):
    original = instance.PatTech
    instance.PatTech = original
    assert instance.PatTech == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Reserved2_type(instance):
    assert isinstance(instance.Reserved2, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Reserved2_setter(instance):
    original = instance.Reserved2
    instance.Reserved2 = original
    assert instance.Reserved2 == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_PatAlign_type(instance):
    assert isinstance(instance.PatAlign, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_PatAlign_setter(instance):
    original = instance.PatAlign
    instance.PatAlign = original
    assert instance.PatAlign == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YUnitBase_type(instance):
    assert isinstance(instance.YUnitBase, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YUnitBase_setter(instance):
    original = instance.YUnitBase
    instance.YUnitBase = original
    assert instance.YUnitBase == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XUnitBase_type(instance):
    assert isinstance(instance.XUnitBase, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XUnitBase_setter(instance):
    original = instance.XUnitBase
    instance.XUnitBase = original
    assert instance.XUnitBase == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XftUnits_type(instance):
    assert isinstance(instance.XftUnits, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XftUnits_setter(instance):
    original = instance.XftUnits
    instance.XftUnits = original
    assert instance.XftUnits == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YfrUnits_type(instance):
    assert isinstance(instance.YfrUnits, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YfrUnits_setter(instance):
    original = instance.YfrUnits
    instance.YfrUnits = original
    assert instance.YfrUnits == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNORGLen_type(instance):
    assert isinstance(instance.FNORGLen, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNORGLen_setter(instance):
    original = instance.FNORGLen
    instance.FNORGLen = original
    assert instance.FNORGLen == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNIRGLen_type(instance):
    assert isinstance(instance.FNIRGLen, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNIRGLen_setter(instance):
    original = instance.FNIRGLen
    instance.FNIRGLen = original
    assert instance.FNIRGLen == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XfrUnits_type(instance):
    assert isinstance(instance.XfrUnits, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_XfrUnits_setter(instance):
    original = instance.XfrUnits
    instance.XfrUnits = original
    assert instance.XfrUnits == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_RPatDCnt_type(instance):
    assert isinstance(instance.RPatDCnt, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_RPatDCnt_setter(instance):
    original = instance.RPatDCnt
    instance.RPatDCnt = original
    assert instance.RPatDCnt == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNMRGLen_type(instance):
    assert isinstance(instance.FNMRGLen, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNMRGLen_setter(instance):
    original = instance.FNMRGLen
    instance.FNMRGLen = original
    assert instance.FNMRGLen == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_OPatDCnt_type(instance):
    assert isinstance(instance.OPatDCnt, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_OPatDCnt_setter(instance):
    original = instance.OPatDCnt
    instance.OPatDCnt = original
    assert instance.OPatDCnt == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_ResXUBase_type(instance):
    assert isinstance(instance.ResXUBase, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_ResXUBase_setter(instance):
    original = instance.ResXUBase
    instance.ResXUBase = original
    assert instance.ResXUBase == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNRGLen_type(instance):
    assert isinstance(instance.FNNRGLen, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNRGLen_setter(instance):
    original = instance.FNNRGLen
    instance.FNNRGLen = original
    assert instance.FNNRGLen == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNPRGLen_type(instance):
    assert isinstance(instance.FNPRGLen, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNPRGLen_setter(instance):
    original = instance.FNPRGLen
    instance.FNPRGLen = original
    assert instance.FNPRGLen == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_MaxBoxWd_type(instance):
    assert isinstance(instance.MaxBoxWd, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_MaxBoxWd_setter(instance):
    original = instance.MaxBoxWd
    instance.MaxBoxWd = original
    assert instance.MaxBoxWd == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNDCnt_type(instance):
    assert isinstance(instance.FNNDCnt, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNDCnt_setter(instance):
    original = instance.FNNDCnt
    instance.FNNDCnt = original
    assert instance.FNNDCnt == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FntFlags_type(instance):
    assert isinstance(instance.FntFlags, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FntFlags_setter(instance):
    original = instance.FntFlags
    instance.FntFlags = original
    assert instance.FntFlags == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YftUnits_type(instance):
    assert isinstance(instance.YftUnits, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_YftUnits_setter(instance):
    original = instance.YftUnits
    instance.YftUnits = original
    assert instance.YftUnits == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Retired_type(instance):
    assert isinstance(instance.Retired, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_Retired_setter(instance):
    original = instance.Retired
    instance.Retired = original
    assert instance.Retired == original

@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNMapCnt_type(instance):
    assert isinstance(instance.FNNMapCnt, str)


@given(instance=afpText::FNC_strategy)
def test_afptext::fnc_FNNMapCnt_setter(instance):
    original = instance.FNNMapCnt
    instance.FNNMapCnt = original
    assert instance.FNNMapCnt == original

@given(instance=afpText::ESG_strategy)
@settings(max_examples=50)
def test_afptext::esg_instantiation(instance):
    assert isinstance(instance, afpText::ESG)

@given(instance=afpText::ESG_strategy)
def test_afptext::esg_REGName_type(instance):
    assert isinstance(instance.REGName, str)


@given(instance=afpText::ESG_strategy)
def test_afptext::esg_REGName_setter(instance):
    original = instance.REGName
    instance.REGName = original
    assert instance.REGName == original

@given(instance=afpText::ERS_strategy)
@settings(max_examples=50)
def test_afptext::ers_instantiation(instance):
    assert isinstance(instance, afpText::ERS)

@given(instance=afpText::ERS_strategy)
def test_afptext::ers_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::ERS_strategy)
def test_afptext::ers_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::ERG_strategy)
@settings(max_examples=50)
def test_afptext::erg_instantiation(instance):
    assert isinstance(instance, afpText::ERG)

@given(instance=afpText::ERG_strategy)
def test_afptext::erg_RGrpName_type(instance):
    assert isinstance(instance.RGrpName, str)


@given(instance=afpText::ERG_strategy)
def test_afptext::erg_RGrpName_setter(instance):
    original = instance.RGrpName
    instance.RGrpName = original
    assert instance.RGrpName == original

@given(instance=afpText::EIM_strategy)
@settings(max_examples=50)
def test_afptext::eim_instantiation(instance):
    assert isinstance(instance, afpText::EIM)

@given(instance=afpText::EIM_strategy)
def test_afptext::eim_IdoName_type(instance):
    assert isinstance(instance.IdoName, str)


@given(instance=afpText::EIM_strategy)
def test_afptext::eim_IdoName_setter(instance):
    original = instance.IdoName
    instance.IdoName = original
    assert instance.IdoName == original

@given(instance=afpText::EPS_strategy)
@settings(max_examples=50)
def test_afptext::eps_instantiation(instance):
    assert isinstance(instance, afpText::EPS)

@given(instance=afpText::EPS_strategy)
def test_afptext::eps_PsegName_type(instance):
    assert isinstance(instance.PsegName, str)


@given(instance=afpText::EPS_strategy)
def test_afptext::eps_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText::EPM_strategy)
@settings(max_examples=50)
def test_afptext::epm_instantiation(instance):
    assert isinstance(instance, afpText::EPM)

@given(instance=afpText::EPM_strategy)
def test_afptext::epm_PMName_type(instance):
    assert isinstance(instance.PMName, str)


@given(instance=afpText::EPM_strategy)
def test_afptext::epm_PMName_setter(instance):
    original = instance.PMName
    instance.PMName = original
    assert instance.PMName == original

@given(instance=afpText::EPG_strategy)
@settings(max_examples=50)
def test_afptext::epg_instantiation(instance):
    assert isinstance(instance, afpText::EPG)

@given(instance=afpText::EPG_strategy)
def test_afptext::epg_PageName_type(instance):
    assert isinstance(instance.PageName, str)


@given(instance=afpText::EPG_strategy)
def test_afptext::epg_PageName_setter(instance):
    original = instance.PageName
    instance.PageName = original
    assert instance.PageName == original

@given(instance=afpText::EPF_strategy)
@settings(max_examples=50)
def test_afptext::epf_instantiation(instance):
    assert isinstance(instance, afpText::EPF)

@given(instance=afpText::EPF_strategy)
def test_afptext::epf_PFName_type(instance):
    assert isinstance(instance.PFName, str)


@given(instance=afpText::EPF_strategy)
def test_afptext::epf_PFName_setter(instance):
    original = instance.PFName
    instance.PFName = original
    assert instance.PFName == original

@given(instance=afpText::EOG_strategy)
@settings(max_examples=50)
def test_afptext::eog_instantiation(instance):
    assert isinstance(instance, afpText::EOG)

@given(instance=afpText::EOG_strategy)
def test_afptext::eog_OEGName_type(instance):
    assert isinstance(instance.OEGName, str)


@given(instance=afpText::EOG_strategy)
def test_afptext::eog_OEGName_setter(instance):
    original = instance.OEGName
    instance.OEGName = original
    assert instance.OEGName == original

@given(instance=afpText::EOC_strategy)
@settings(max_examples=50)
def test_afptext::eoc_instantiation(instance):
    assert isinstance(instance, afpText::EOC)

@given(instance=afpText::EOC_strategy)
def test_afptext::eoc_ObjCName_type(instance):
    assert isinstance(instance.ObjCName, str)


@given(instance=afpText::EOC_strategy)
def test_afptext::eoc_ObjCName_setter(instance):
    original = instance.ObjCName
    instance.ObjCName = original
    assert instance.ObjCName == original

@given(instance=afpText::ENG_strategy)
@settings(max_examples=50)
def test_afptext::eng_instantiation(instance):
    assert isinstance(instance, afpText::ENG)

@given(instance=afpText::ENG_strategy)
def test_afptext::eng_PGrpName_type(instance):
    assert isinstance(instance.PGrpName, str)


@given(instance=afpText::ENG_strategy)
def test_afptext::eng_PGrpName_setter(instance):
    original = instance.PGrpName
    instance.PGrpName = original
    assert instance.PGrpName == original

@given(instance=afpText::EMO_strategy)
@settings(max_examples=50)
def test_afptext::emo_instantiation(instance):
    assert isinstance(instance, afpText::EMO)

@given(instance=afpText::EMO_strategy)
def test_afptext::emo_OvlyName_type(instance):
    assert isinstance(instance.OvlyName, str)


@given(instance=afpText::EMO_strategy)
def test_afptext::emo_OvlyName_setter(instance):
    original = instance.OvlyName
    instance.OvlyName = original
    assert instance.OvlyName == original

@given(instance=afpText::EMM_strategy)
@settings(max_examples=50)
def test_afptext::emm_instantiation(instance):
    assert isinstance(instance, afpText::EMM)

@given(instance=afpText::EMM_strategy)
def test_afptext::emm_MMName_type(instance):
    assert isinstance(instance.MMName, str)


@given(instance=afpText::EMM_strategy)
def test_afptext::emm_MMName_setter(instance):
    original = instance.MMName
    instance.MMName = original
    assert instance.MMName == original

@given(instance=afpText::EII_strategy)
@settings(max_examples=50)
def test_afptext::eii_instantiation(instance):
    assert isinstance(instance, afpText::EII)

@given(instance=afpText::EII_strategy)
def test_afptext::eii_ImoName_type(instance):
    assert isinstance(instance.ImoName, str)


@given(instance=afpText::EII_strategy)
def test_afptext::eii_ImoName_setter(instance):
    original = instance.ImoName
    instance.ImoName = original
    assert instance.ImoName == original

@given(instance=afpText::EGR_strategy)
@settings(max_examples=50)
def test_afptext::egr_instantiation(instance):
    assert isinstance(instance, afpText::EGR)

@given(instance=afpText::EGR_strategy)
def test_afptext::egr_GdoName_type(instance):
    assert isinstance(instance.GdoName, str)


@given(instance=afpText::EGR_strategy)
def test_afptext::egr_GdoName_setter(instance):
    original = instance.GdoName
    instance.GdoName = original
    assert instance.GdoName == original

@given(instance=afpText::EFN_strategy)
@settings(max_examples=50)
def test_afptext::efn_instantiation(instance):
    assert isinstance(instance, afpText::EFN)

@given(instance=afpText::EFN_strategy)
def test_afptext::efn_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::EFN_strategy)
def test_afptext::efn_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::EFM_strategy)
@settings(max_examples=50)
def test_afptext::efm_instantiation(instance):
    assert isinstance(instance, afpText::EFM)

@given(instance=afpText::EFM_strategy)
def test_afptext::efm_FMName_type(instance):
    assert isinstance(instance.FMName, str)


@given(instance=afpText::EFM_strategy)
def test_afptext::efm_FMName_setter(instance):
    original = instance.FMName
    instance.FMName = original
    assert instance.FMName == original

@given(instance=afpText::EFG_strategy)
@settings(max_examples=50)
def test_afptext::efg_instantiation(instance):
    assert isinstance(instance, afpText::EFG)

@given(instance=afpText::EFG_strategy)
def test_afptext::efg_FEGName_type(instance):
    assert isinstance(instance.FEGName, str)


@given(instance=afpText::EFG_strategy)
def test_afptext::efg_FEGName_setter(instance):
    original = instance.FEGName
    instance.FEGName = original
    assert instance.FEGName == original

@given(instance=afpText::EDX_strategy)
@settings(max_examples=50)
def test_afptext::edx_instantiation(instance):
    assert isinstance(instance, afpText::EDX)

@given(instance=afpText::EDX_strategy)
def test_afptext::edx_DMXName_type(instance):
    assert isinstance(instance.DMXName, str)


@given(instance=afpText::EDX_strategy)
def test_afptext::edx_DMXName_setter(instance):
    original = instance.DMXName
    instance.DMXName = original
    assert instance.DMXName == original

@given(instance=afpText::EDT_strategy)
@settings(max_examples=50)
def test_afptext::edt_instantiation(instance):
    assert isinstance(instance, afpText::EDT)

@given(instance=afpText::EDT_strategy)
def test_afptext::edt_DocName_type(instance):
    assert isinstance(instance.DocName, str)


@given(instance=afpText::EDT_strategy)
def test_afptext::edt_DocName_setter(instance):
    original = instance.DocName
    instance.DocName = original
    assert instance.DocName == original

@given(instance=afpText::EDM_strategy)
@settings(max_examples=50)
def test_afptext::edm_instantiation(instance):
    assert isinstance(instance, afpText::EDM)

@given(instance=afpText::EDM_strategy)
def test_afptext::edm_DMName_type(instance):
    assert isinstance(instance.DMName, str)


@given(instance=afpText::EDM_strategy)
def test_afptext::edm_DMName_setter(instance):
    original = instance.DMName
    instance.DMName = original
    assert instance.DMName == original

@given(instance=afpText::EDI_strategy)
@settings(max_examples=50)
def test_afptext::edi_instantiation(instance):
    assert isinstance(instance, afpText::EDI)

@given(instance=afpText::EDI_strategy)
def test_afptext::edi_IndxName_type(instance):
    assert isinstance(instance.IndxName, str)


@given(instance=afpText::EDI_strategy)
def test_afptext::edi_IndxName_setter(instance):
    original = instance.IndxName
    instance.IndxName = original
    assert instance.IndxName == original

@given(instance=afpText::EDG_strategy)
@settings(max_examples=50)
def test_afptext::edg_instantiation(instance):
    assert isinstance(instance, afpText::EDG)

@given(instance=afpText::EDG_strategy)
def test_afptext::edg_DEGName_type(instance):
    assert isinstance(instance.DEGName, str)


@given(instance=afpText::EDG_strategy)
def test_afptext::edg_DEGName_setter(instance):
    original = instance.DEGName
    instance.DEGName = original
    assert instance.DEGName == original

@given(instance=afpText::ECP_strategy)
@settings(max_examples=50)
def test_afptext::ecp_instantiation(instance):
    assert isinstance(instance, afpText::ECP)

@given(instance=afpText::ECP_strategy)
def test_afptext::ecp_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::ECP_strategy)
def test_afptext::ecp_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::ECF_strategy)
@settings(max_examples=50)
def test_afptext::ecf_instantiation(instance):
    assert isinstance(instance, afpText::ECF)

@given(instance=afpText::ECF_strategy)
def test_afptext::ecf_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::ECF_strategy)
def test_afptext::ecf_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::ECA_strategy)
@settings(max_examples=50)
def test_afptext::eca_instantiation(instance):
    assert isinstance(instance, afpText::ECA)

@given(instance=afpText::ECA_strategy)
def test_afptext::eca_CATName_type(instance):
    assert isinstance(instance.CATName, str)


@given(instance=afpText::ECA_strategy)
def test_afptext::eca_CATName_setter(instance):
    original = instance.CATName
    instance.CATName = original
    assert instance.CATName == original

@given(instance=afpText::EBC_strategy)
@settings(max_examples=50)
def test_afptext::ebc_instantiation(instance):
    assert isinstance(instance, afpText::EBC)

@given(instance=afpText::EBC_strategy)
def test_afptext::ebc_BCdoName_type(instance):
    assert isinstance(instance.BCdoName, str)


@given(instance=afpText::EBC_strategy)
def test_afptext::ebc_BCdoName_setter(instance):
    original = instance.BCdoName
    instance.BCdoName = original
    assert instance.BCdoName == original

@given(instance=afpText::EAG_strategy)
@settings(max_examples=50)
def test_afptext::eag_instantiation(instance):
    assert isinstance(instance, afpText::EAG)

@given(instance=afpText::EAG_strategy)
def test_afptext::eag_AEGName_type(instance):
    assert isinstance(instance.AEGName, str)


@given(instance=afpText::EAG_strategy)
def test_afptext::eag_AEGName_setter(instance):
    original = instance.AEGName
    instance.AEGName = original
    assert instance.AEGName == original

@given(instance=afpText::DXD_strategy)
@settings(max_examples=50)
def test_afptext::dxd_instantiation(instance):
    assert isinstance(instance, afpText::DXD)

@given(instance=afpText::BRG_strategy)
@settings(max_examples=50)
def test_afptext::brg_instantiation(instance):
    assert isinstance(instance, afpText::BRG)

@given(instance=afpText::BRG_strategy)
def test_afptext::brg_RGrpName_type(instance):
    assert isinstance(instance.RGrpName, str)


@given(instance=afpText::BRG_strategy)
def test_afptext::brg_RGrpName_setter(instance):
    original = instance.RGrpName
    instance.RGrpName = original
    assert instance.RGrpName == original

@given(instance=afpText::CTC_strategy)
@settings(max_examples=50)
def test_afptext::ctc_instantiation(instance):
    assert isinstance(instance, afpText::CTC)

@given(instance=afpText::CTC_strategy)
def test_afptext::ctc_ConData_type(instance):
    assert isinstance(instance.ConData, str)


@given(instance=afpText::CTC_strategy)
def test_afptext::ctc_ConData_setter(instance):
    original = instance.ConData
    instance.ConData = original
    assert instance.ConData == original

@given(instance=afpText::CPIRG_strategy)
@settings(max_examples=50)
def test_afptext::cpirg_instantiation(instance):
    assert isinstance(instance, afpText::CPIRG)

@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_Count_type(instance):
    assert isinstance(instance.Count, str)


@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_Count_setter(instance):
    original = instance.Count
    instance.Count = original
    assert instance.Count == original

@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_CodePoint_type(instance):
    assert isinstance(instance.CodePoint, str)


@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_CodePoint_setter(instance):
    original = instance.CodePoint
    instance.CodePoint = original
    assert instance.CodePoint == original

@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_PrtFlags_type(instance):
    assert isinstance(instance.PrtFlags, str)


@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_PrtFlags_setter(instance):
    original = instance.PrtFlags
    instance.PrtFlags = original
    assert instance.PrtFlags == original

@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_GCGID_type(instance):
    assert isinstance(instance.GCGID, str)


@given(instance=afpText::CPIRG_strategy)
def test_afptext::cpirg_GCGID_setter(instance):
    original = instance.GCGID
    instance.GCGID = original
    assert instance.GCGID == original

@given(instance=afpText::CPI_strategy)
@settings(max_examples=50)
def test_afptext::cpi_instantiation(instance):
    assert isinstance(instance, afpText::CPI)

@given(instance=afpText::CPD_strategy)
@settings(max_examples=50)
def test_afptext::cpd_instantiation(instance):
    assert isinstance(instance, afpText::CPD)

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_GCGIDLen_type(instance):
    assert isinstance(instance.GCGIDLen, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_GCGIDLen_setter(instance):
    original = instance.GCGIDLen
    instance.GCGIDLen = original
    assert instance.GCGIDLen == original

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_CPDesc_type(instance):
    assert isinstance(instance.CPDesc, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_CPDesc_setter(instance):
    original = instance.CPDesc
    instance.CPDesc = original
    assert instance.CPDesc == original

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_CPGID_type(instance):
    assert isinstance(instance.CPGID, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_CPGID_setter(instance):
    original = instance.CPGID
    instance.CPGID = original
    assert instance.CPGID == original

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_GCSGID_type(instance):
    assert isinstance(instance.GCSGID, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_GCSGID_setter(instance):
    original = instance.GCSGID
    instance.GCSGID = original
    assert instance.GCSGID == original

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_NumCdPts_type(instance):
    assert isinstance(instance.NumCdPts, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_NumCdPts_setter(instance):
    original = instance.NumCdPts
    instance.NumCdPts = original
    assert instance.NumCdPts == original

@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_EncScheme_type(instance):
    assert isinstance(instance.EncScheme, str)


@given(instance=afpText::CPD_strategy)
def test_afptext::cpd_EncScheme_setter(instance):
    original = instance.EncScheme
    instance.EncScheme = original
    assert instance.EncScheme == original

@given(instance=afpText::CPC_strategy)
@settings(max_examples=50)
def test_afptext::cpc_instantiation(instance):
    assert isinstance(instance, afpText::CPC)

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSFlags_type(instance):
    assert isinstance(instance.VSFlags, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSFlags_setter(instance):
    original = instance.VSFlags
    instance.VSFlags = original
    assert instance.VSFlags == original

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSChar_type(instance):
    assert isinstance(instance.VSChar, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSChar_setter(instance):
    original = instance.VSChar
    instance.VSChar = original
    assert instance.VSChar == original

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_CPIRGLen_type(instance):
    assert isinstance(instance.CPIRGLen, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_CPIRGLen_setter(instance):
    original = instance.CPIRGLen
    instance.CPIRGLen = original
    assert instance.CPIRGLen == original

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_PrtFlags_type(instance):
    assert isinstance(instance.PrtFlags, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_PrtFlags_setter(instance):
    original = instance.PrtFlags
    instance.PrtFlags = original
    assert instance.PrtFlags == original

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSCharSN_type(instance):
    assert isinstance(instance.VSCharSN, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_VSCharSN_setter(instance):
    original = instance.VSCharSN
    instance.VSCharSN = original
    assert instance.VSCharSN == original

@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_DefCharID_type(instance):
    assert isinstance(instance.DefCharID, str)


@given(instance=afpText::CPC_strategy)
def test_afptext::cpc_DefCharID_setter(instance):
    original = instance.DefCharID
    instance.DefCharID = original
    assert instance.DefCharID == original

@given(instance=afpText::CFIRG_strategy)
@settings(max_examples=50)
def test_afptext::cfirg_instantiation(instance):
    assert isinstance(instance, afpText::CFIRG)

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_SHScale_type(instance):
    assert isinstance(instance.SHScale, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_SHScale_setter(instance):
    original = instance.SHScale
    instance.SHScale = original
    assert instance.SHScale == original

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_SVSize_type(instance):
    assert isinstance(instance.SVSize, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_SVSize_setter(instance):
    original = instance.SVSize
    instance.SVSize = original
    assert instance.SVSize == original

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_FCSName_type(instance):
    assert isinstance(instance.FCSName, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_FCSName_setter(instance):
    original = instance.FCSName
    instance.FCSName = original
    assert instance.FCSName == original

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_CPName_type(instance):
    assert isinstance(instance.CPName, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_CPName_setter(instance):
    original = instance.CPName
    instance.CPName = original
    assert instance.CPName == original

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_Section_type(instance):
    assert isinstance(instance.Section, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_Section_setter(instance):
    original = instance.Section
    instance.Section = original
    assert instance.Section == original

@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_Reserved_type(instance):
    assert isinstance(instance.Reserved, str)


@given(instance=afpText::CFIRG_strategy)
def test_afptext::cfirg_Reserved_setter(instance):
    original = instance.Reserved
    instance.Reserved = original
    assert instance.Reserved == original

@given(instance=afpText::CFI_strategy)
@settings(max_examples=50)
def test_afptext::cfi_instantiation(instance):
    assert isinstance(instance, afpText::CFI)

@given(instance=afpText::CFC_strategy)
@settings(max_examples=50)
def test_afptext::cfc_instantiation(instance):
    assert isinstance(instance, afpText::CFC)

@given(instance=afpText::CFC_strategy)
def test_afptext::cfc_CFIRGLen_type(instance):
    assert isinstance(instance.CFIRGLen, str)


@given(instance=afpText::CFC_strategy)
def test_afptext::cfc_CFIRGLen_setter(instance):
    original = instance.CFIRGLen
    instance.CFIRGLen = original
    assert instance.CFIRGLen == original

@given(instance=afpText::CFC_strategy)
def test_afptext::cfc_Retired1_type(instance):
    assert isinstance(instance.Retired1, str)


@given(instance=afpText::CFC_strategy)
def test_afptext::cfc_Retired1_setter(instance):
    original = instance.Retired1
    instance.Retired1 = original
    assert instance.Retired1 == original

@given(instance=afpText::CDD_strategy)
@settings(max_examples=50)
def test_afptext::cdd_instantiation(instance):
    assert isinstance(instance, afpText::CDD)

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocSize_type(instance):
    assert isinstance(instance.XocSize, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocSize_setter(instance):
    original = instance.XocSize
    instance.XocSize = original
    assert instance.XocSize == original

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocUnits_type(instance):
    assert isinstance(instance.YocUnits, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocUnits_setter(instance):
    original = instance.YocUnits
    instance.YocUnits = original
    assert instance.YocUnits == original

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocUnits_type(instance):
    assert isinstance(instance.XocUnits, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocUnits_setter(instance):
    original = instance.XocUnits
    instance.XocUnits = original
    assert instance.XocUnits == original

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocBase_type(instance):
    assert isinstance(instance.YocBase, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocBase_setter(instance):
    original = instance.YocBase
    instance.YocBase = original
    assert instance.YocBase == original

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocBase_type(instance):
    assert isinstance(instance.XocBase, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_XocBase_setter(instance):
    original = instance.XocBase
    instance.XocBase = original
    assert instance.XocBase == original

@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocSize_type(instance):
    assert isinstance(instance.YocSize, str)


@given(instance=afpText::CDD_strategy)
def test_afptext::cdd_YocSize_setter(instance):
    original = instance.YocSize
    instance.YocSize = original
    assert instance.YocSize == original

@given(instance=afpText::CAT_strategy)
@settings(max_examples=50)
def test_afptext::cat_instantiation(instance):
    assert isinstance(instance, afpText::CAT)

@given(instance=afpText::CAT_strategy)
def test_afptext::cat_CATData_type(instance):
    assert isinstance(instance.CATData, str)


@given(instance=afpText::CAT_strategy)
def test_afptext::cat_CATData_setter(instance):
    original = instance.CATData
    instance.CATData = original
    assert instance.CATData == original

@given(instance=afpText::BSG_strategy)
@settings(max_examples=50)
def test_afptext::bsg_instantiation(instance):
    assert isinstance(instance, afpText::BSG)

@given(instance=afpText::BSG_strategy)
def test_afptext::bsg_REGName_type(instance):
    assert isinstance(instance.REGName, str)


@given(instance=afpText::BSG_strategy)
def test_afptext::bsg_REGName_setter(instance):
    original = instance.REGName
    instance.REGName = original
    assert instance.REGName == original

@given(instance=afpText::BRS_strategy)
@settings(max_examples=50)
def test_afptext::brs_instantiation(instance):
    assert isinstance(instance, afpText::BRS)

@given(instance=afpText::BRS_strategy)
def test_afptext::brs_RSName_type(instance):
    assert isinstance(instance.RSName, str)


@given(instance=afpText::BRS_strategy)
def test_afptext::brs_RSName_setter(instance):
    original = instance.RSName
    instance.RSName = original
    assert instance.RSName == original

@given(instance=afpText::BPT_strategy)
@settings(max_examples=50)
def test_afptext::bpt_instantiation(instance):
    assert isinstance(instance, afpText::BPT)

@given(instance=afpText::BPT_strategy)
def test_afptext::bpt_PTdoName_type(instance):
    assert isinstance(instance.PTdoName, str)


@given(instance=afpText::BPT_strategy)
def test_afptext::bpt_PTdoName_setter(instance):
    original = instance.PTdoName
    instance.PTdoName = original
    assert instance.PTdoName == original

@given(instance=afpText::BPS_strategy)
@settings(max_examples=50)
def test_afptext::bps_instantiation(instance):
    assert isinstance(instance, afpText::BPS)

@given(instance=afpText::BPS_strategy)
def test_afptext::bps_PsegName_type(instance):
    assert isinstance(instance.PsegName, str)


@given(instance=afpText::BPS_strategy)
def test_afptext::bps_PsegName_setter(instance):
    original = instance.PsegName
    instance.PsegName = original
    assert instance.PsegName == original

@given(instance=afpText::BPM_strategy)
@settings(max_examples=50)
def test_afptext::bpm_instantiation(instance):
    assert isinstance(instance, afpText::BPM)

@given(instance=afpText::BPM_strategy)
def test_afptext::bpm_PMName_type(instance):
    assert isinstance(instance.PMName, str)


@given(instance=afpText::BPM_strategy)
def test_afptext::bpm_PMName_setter(instance):
    original = instance.PMName
    instance.PMName = original
    assert instance.PMName == original

@given(instance=afpText::BPG_strategy)
@settings(max_examples=50)
def test_afptext::bpg_instantiation(instance):
    assert isinstance(instance, afpText::BPG)

@given(instance=afpText::BPG_strategy)
def test_afptext::bpg_PageName_type(instance):
    assert isinstance(instance.PageName, str)


@given(instance=afpText::BPG_strategy)
def test_afptext::bpg_PageName_setter(instance):
    original = instance.PageName
    instance.PageName = original
    assert instance.PageName == original
