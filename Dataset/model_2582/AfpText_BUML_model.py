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

# Classes
afpText_structuredField = Class(name="afpText::structuredField")
afpText_LineData = Class(name="afpText::LineData")
structuredField = Class(name="structuredField")
afpText_BAG = Class(name="afpText::BAG")
afpText_triplet = Class(name="afpText::triplet")
afpText_BBC = Class(name="afpText::BBC")
afpText_Model = Class(name="afpText::Model")
afpText_BDD = Class(name="afpText::BDD")
afpText_BCA = Class(name="afpText::BCA")
afpText_BCF = Class(name="afpText::BCF")
afpText_BCP = Class(name="afpText::BCP")
afpText_BDA = Class(name="afpText::BDA")
afpText_BDX = Class(name="afpText::BDX")
afpText_BFG = Class(name="afpText::BFG")
afpText_BFM = Class(name="afpText::BFM")
afpText_BFN = Class(name="afpText::BFN")
afpText_BGR = Class(name="afpText::BGR")
afpText_BDG = Class(name="afpText::BDG")
afpText_BDI = Class(name="afpText::BDI")
afpText_BDM = Class(name="afpText::BDM")
afpText_BDT = Class(name="afpText::BDT")
afpText_BOG = Class(name="afpText::BOG")
afpText_BPF = Class(name="afpText::BPF")
afpText_BPG = Class(name="afpText::BPG")
afpText_BII = Class(name="afpText::BII")
afpText_BIM = Class(name="afpText::BIM")
afpText_BMM = Class(name="afpText::BMM")
afpText_BMO = Class(name="afpText::BMO")
afpText_BNG = Class(name="afpText::BNG")
afpText_BOC = Class(name="afpText::BOC")
afpText_CAT = Class(name="afpText::CAT")
afpText_CDD = Class(name="afpText::CDD")
afpText_CFC = Class(name="afpText::CFC")
afpText_BPM = Class(name="afpText::BPM")
afpText_BPS = Class(name="afpText::BPS")
afpText_BPT = Class(name="afpText::BPT")
afpText_BRG = Class(name="afpText::BRG")
afpText_BRS = Class(name="afpText::BRS")
afpText_BSG = Class(name="afpText::BSG")
afpText_CTC = Class(name="afpText::CTC")
afpText_DXD = Class(name="afpText::DXD")
afpText_EAG = Class(name="afpText::EAG")
afpText_EBC = Class(name="afpText::EBC")
afpText_ECA = Class(name="afpText::ECA")
afpText_CFI = Class(name="afpText::CFI")
afpText_CFIRG = Class(name="afpText::CFIRG")
afpText_CPC = Class(name="afpText::CPC")
afpText_CPD = Class(name="afpText::CPD")
afpText_CPI = Class(name="afpText::CPI")
afpText_CPIRG = Class(name="afpText::CPIRG")
afpText_EFM = Class(name="afpText::EFM")
afpText_EFN = Class(name="afpText::EFN")
afpText_EGR = Class(name="afpText::EGR")
afpText_EII = Class(name="afpText::EII")
afpText_EIM = Class(name="afpText::EIM")
afpText_ECF = Class(name="afpText::ECF")
afpText_ECP = Class(name="afpText::ECP")
afpText_EDG = Class(name="afpText::EDG")
afpText_EDI = Class(name="afpText::EDI")
afpText_EDM = Class(name="afpText::EDM")
afpText_EDT = Class(name="afpText::EDT")
afpText_EDX = Class(name="afpText::EDX")
afpText_EFG = Class(name="afpText::EFG")
afpText_EPF = Class(name="afpText::EPF")
afpText_EPG = Class(name="afpText::EPG")
afpText_EPM = Class(name="afpText::EPM")
afpText_EMM = Class(name="afpText::EMM")
afpText_EMO = Class(name="afpText::EMO")
afpText_ENG = Class(name="afpText::ENG")
afpText_EOC = Class(name="afpText::EOC")
afpText_EOG = Class(name="afpText::EOG")
afpText_EPS = Class(name="afpText::EPS")
afpText_EPT = Class(name="afpText::EPT")
afpText_ERG = Class(name="afpText::ERG")
afpText_ERS = Class(name="afpText::ERS")
afpText_ESG = Class(name="afpText::ESG")
afpText_FNC = Class(name="afpText::FNC")
afpText_FNG = Class(name="afpText::FNG")
afpText_FNI = Class(name="afpText::FNI")
afpText_FNIRG = Class(name="afpText::FNIRG")
afpText_FNN = Class(name="afpText::FNN")
afpText_FNM = Class(name="afpText::FNM")
afpText_FNMRG = Class(name="afpText::FNMRG")
afpText_FND = Class(name="afpText::FND")
afpText_IEL = Class(name="afpText::IEL")
afpText_FNO = Class(name="afpText::FNO")
afpText_FNORG = Class(name="afpText::FNORG")
afpText_FNP = Class(name="afpText::FNP")
afpText_FNPRG = Class(name="afpText::FNPRG")
afpText_GAD = Class(name="afpText::GAD")
afpText_GDD = Class(name="afpText::GDD")
afpText_ICP = Class(name="afpText::ICP")
afpText_IDD = Class(name="afpText::IDD")
afpText_IOC = Class(name="afpText::IOC")
afpText_IID = Class(name="afpText::IID")
afpText_IMM = Class(name="afpText::IMM")
afpText_IOB = Class(name="afpText::IOB")
afpText_IRD = Class(name="afpText::IRD")
afpText_LLE = Class(name="afpText::LLE")
afpText_LLERG = Class(name="afpText::LLERG")
afpText_LNC = Class(name="afpText::LNC")
afpText_LND = Class(name="afpText::LND")
afpText_IPD = Class(name="afpText::IPD")
afpText_IPG = Class(name="afpText::IPG")
afpText_IPO = Class(name="afpText::IPO")
afpText_IPS = Class(name="afpText::IPS")
afpText_MCDRG = Class(name="afpText::MCDRG")
afpText_MCF = Class(name="afpText::MCF")
afpText_MCFRG = Class(name="afpText::MCFRG")
afpText_MCF1 = Class(name="afpText::MCF1")
afpText_MCF1RG = Class(name="afpText::MCF1RG")
afpText_MDD = Class(name="afpText::MDD")
afpText_MBC = Class(name="afpText::MBC")
afpText_MBCRG = Class(name="afpText::MBCRG")
afpText_MCA = Class(name="afpText::MCA")
afpText_MCARG = Class(name="afpText::MCARG")
afpText_MCC = Class(name="afpText::MCC")
afpText_MCCRG = Class(name="afpText::MCCRG")
afpText_MCD = Class(name="afpText::MCD")
afpText_MMC = Class(name="afpText::MMC")
afpText_MMCRG = Class(name="afpText::MMCRG")
afpText_MMD = Class(name="afpText::MMD")
afpText_MMDRG = Class(name="afpText::MMDRG")
afpText_MDR = Class(name="afpText::MDR")
afpText_MDRRG = Class(name="afpText::MDRRG")
afpText_MFC = Class(name="afpText::MFC")
afpText_MGO = Class(name="afpText::MGO")
afpText_MGORG = Class(name="afpText::MGORG")
afpText_MIO = Class(name="afpText::MIO")
afpText_MIORG = Class(name="afpText::MIORG")
afpText_MSURG = Class(name="afpText::MSURG")
afpText_NOP = Class(name="afpText::NOP")
afpText_OBD = Class(name="afpText::OBD")
afpText_OBP = Class(name="afpText::OBP")
afpText_MMO = Class(name="afpText::MMO")
afpText_MMORG = Class(name="afpText::MMORG")
afpText_MMT = Class(name="afpText::MMT")
afpText_MMTRG = Class(name="afpText::MMTRG")
afpText_MPG = Class(name="afpText::MPG")
afpText_MPGRG = Class(name="afpText::MPGRG")
afpText_MPO = Class(name="afpText::MPO")
afpText_MPORG = Class(name="afpText::MPORG")
afpText_MPS = Class(name="afpText::MPS")
afpText_MPSRG = Class(name="afpText::MPSRG")
afpText_MSU = Class(name="afpText::MSU")
afpText_PGP = Class(name="afpText::PGP")
afpText_PGPRG = Class(name="afpText::PGPRG")
afpText_PGP1 = Class(name="afpText::PGP1")
afpText_PMC = Class(name="afpText::PMC")
afpText_OCD = Class(name="afpText::OCD")
afpText_PEC = Class(name="afpText::PEC")
afpText_PFC = Class(name="afpText::PFC")
afpText_PGD = Class(name="afpText::PGD")
afpText_PTD = Class(name="afpText::PTD")
afpText_PPO = Class(name="afpText::PPO")
afpText_PPORG = Class(name="afpText::PPORG")
afpText_FGD = Class(name="afpText::FGD")
afpText_PTD1 = Class(name="afpText::PTD1")
afpText_PTX = Class(name="afpText::PTX")
afpText_TLE = Class(name="afpText::TLE")
afpText_BandImageRG = Class(name="afpText::BandImageRG")
afpText_TileTOCRG = Class(name="afpText::TileTOCRG")
afpText_SamplingRatiosRG = Class(name="afpText::SamplingRatiosRG")
afpText_GFLTRG = Class(name="afpText::GFLTRG")
afpText_GCFLTRG = Class(name="afpText::GCFLTRG")
afpText_GLINERG = Class(name="afpText::GLINERG")
afpText_GCLINERG = Class(name="afpText::GCLINERG")
afpText_ExternalAlgorithmRG = Class(name="afpText::ExternalAlgorithmRG")
afpText_FNNRG = Class(name="afpText::FNNRG")
afpText_GCBEZRG = Class(name="afpText::GCBEZRG")
afpText_GCCBEZRG = Class(name="afpText::GCCBEZRG")
afpText_AMB = Class(name="afpText::AMB")
triplet = Class(name="triplet")
afpText_AMI = Class(name="afpText::AMI")
afpText_BLN = Class(name="afpText::BLN")
afpText_BSU = Class(name="afpText::BSU")
afpText_DBR = Class(name="afpText::DBR")
afpText_GMRKRG = Class(name="afpText::GMRKRG")
afpText_GCMRKRG = Class(name="afpText::GCMRKRG")
afpText_GRLINERG = Class(name="afpText::GRLINERG")
afpText_GCRLINERG = Class(name="afpText::GCRLINERG")
afpText_OVS = Class(name="afpText::OVS")
afpText_RMB = Class(name="afpText::RMB")
afpText_DIR = Class(name="afpText::DIR")
afpText_ESU = Class(name="afpText::ESU")
afpText_NOPCS = Class(name="afpText::NOPCS")
afpText_RMI = Class(name="afpText::RMI")
afpText_RPS = Class(name="afpText::RPS")
afpText_SBI = Class(name="afpText::SBI")
afpText_SCFL = Class(name="afpText::SCFL")
afpText_SEC = Class(name="afpText::SEC")
afpText_SIM = Class(name="afpText::SIM")
afpText_STC = Class(name="afpText::STC")
afpText_STO = Class(name="afpText::STO")
afpText_SVI = Class(name="afpText::SVI")
afpText_AttributeValue = Class(name="afpText::AttributeValue")
afpText_SIA = Class(name="afpText::SIA")
afpText_CGCSGID = Class(name="afpText::CGCSGID")
afpText_CRCResourceManagement = Class(name="afpText::CRCResourceManagement")
afpText_CharacterRotation = Class(name="afpText::CharacterRotation")
afpText_TBM = Class(name="afpText::TBM")
afpText_TRN = Class(name="afpText::TRN")
afpText_USC = Class(name="afpText::USC")
afpText_AttributeQualifier = Class(name="afpText::AttributeQualifier")
afpText_DescriptorPosition = Class(name="afpText::DescriptorPosition")
afpText_EncodingSchemeID = Class(name="afpText::EncodingSchemeID")
afpText_FontResolution = Class(name="afpText::FontResolution")
afpText_ColorSpecification = Class(name="afpText::ColorSpecification")
afpText_Comment = Class(name="afpText::Comment")
afpText_DataObjectFontDescriptor = Class(name="afpText::DataObjectFontDescriptor")
afpText_UniversalDateAndTimeStamp = Class(name="afpText::UniversalDateAndTimeStamp")
afpText_FullyQualifiedName = Class(name="afpText::FullyQualifiedName")
afpText_LocalDateAndTimeStamp = Class(name="afpText::LocalDateAndTimeStamp")
afpText_MediumOrientation = Class(name="afpText::MediumOrientation")
afpText_MeasurementUnits = Class(name="afpText::MeasurementUnits")
afpText_MODCAInterchangeSet = Class(name="afpText::MODCAInterchangeSet")
afpText_ObjectAreaSize = Class(name="afpText::ObjectAreaSize")
afpText_MappingOption = Class(name="afpText::MappingOption")
afpText_MediaEjectControl = Class(name="afpText::MediaEjectControl")
afpText_MediumMapPageNumber = Class(name="afpText::MediumMapPageNumber")
afpText_ObjectOffset = Class(name="afpText::ObjectOffset")
afpText_ResourceObjectType = Class(name="afpText::ResourceObjectType")
afpText_PagePositionInformation = Class(name="afpText::PagePositionInformation")
afpText_PresentationControl = Class(name="afpText::PresentationControl")
afpText_ObjectClassification = Class(name="afpText::ObjectClassification")
afpText_ObjectFunctionSetSpecification = Class(name="afpText::ObjectFunctionSetSpecification")
afpText_TextOrientation = Class(name="afpText::TextOrientation")
afpText_FontHorizontalScaleFactor = Class(name="afpText::FontHorizontalScaleFactor")
afpText_FontDescriptorSpecification = Class(name="afpText::FontDescriptorSpecification")
afpText_PresentationSpaceResetMixing = Class(name="afpText::PresentationSpaceResetMixing")
afpText_PresentationSpaceMixingRules = Class(name="afpText::PresentationSpaceMixingRules")
afpText_ResourceLocalIdentifier = Class(name="afpText::ResourceLocalIdentifier")
afpText_BeginImage = Class(name="afpText::BeginImage")
afpText_ResourceSectionNumber = Class(name="afpText::ResourceSectionNumber")
afpText_EndImage = Class(name="afpText::EndImage")
afpText_ImageSize = Class(name="afpText::ImageSize")
afpText_ImageEncoding = Class(name="afpText::ImageEncoding")
afpText_BeginSegment = Class(name="afpText::BeginSegment")
afpText_EndSegment = Class(name="afpText::EndSegment")
afpText_BeginTile = Class(name="afpText::BeginTile")
afpText_EndTile = Class(name="afpText::EndTile")
afpText_BeginTransparencyMask = Class(name="afpText::BeginTransparencyMask")
afpText_EndTransparencyMask = Class(name="afpText::EndTransparencyMask")
afpText_IDEStructure = Class(name="afpText::IDEStructure")
afpText_ExternalAlgorithm = Class(name="afpText::ExternalAlgorithm")
afpText_TilePosition = Class(name="afpText::TilePosition")
afpText_IDESize = Class(name="afpText::IDESize")
afpText_ImageLUTID = Class(name="afpText::ImageLUTID")
afpText_BandImage = Class(name="afpText::BandImage")
afpText_SetBiLevelImageColor = Class(name="afpText::SetBiLevelImageColor")
afpText_IOCAFunctionSetIdentification = Class(name="afpText::IOCAFunctionSetIdentification")
afpText_TileSize = Class(name="afpText::TileSize")
afpText_TileSetColor = Class(name="afpText::TileSetColor")
afpText_ImageSubsampling = Class(name="afpText::ImageSubsampling")
afpText_SamplingRatios = Class(name="afpText::SamplingRatios")
afpText_TileTOC = Class(name="afpText::TileTOC")
afpText_ImageData = Class(name="afpText::ImageData")
afpText_BandImageData = Class(name="afpText::BandImageData")
afpText_IncludeTile = Class(name="afpText::IncludeTile")
afpText_GBAR = Class(name="afpText::GBAR")
afpText_GBIMG = Class(name="afpText::GBIMG")
afpText_GCBIMG = Class(name="afpText::GCBIMG")
afpText_FNNRG2 = Class(name="afpText::FNNRG2")
afpText_BeginSegmentCommand = Class(name="afpText::BeginSegmentCommand")
afpText_EndSegmentCommand = Class(name="afpText::EndSegmentCommand")
afpText_GCBOX = Class(name="afpText::GCBOX")
afpText_GCHST = Class(name="afpText::GCHST")
afpText_GCCHST = Class(name="afpText::GCCHST")
afpText_GCOMT = Class(name="afpText::GCOMT")
afpText_GBOX = Class(name="afpText::GBOX")
afpText_GCFLT = Class(name="afpText::GCFLT")
afpText_GFARC = Class(name="afpText::GFARC")
afpText_GCFARC = Class(name="afpText::GCFARC")
afpText_GEAR = Class(name="afpText::GEAR")
afpText_GEIMG = Class(name="afpText::GEIMG")
afpText_GEPROL = Class(name="afpText::GEPROL")
afpText_GFLT = Class(name="afpText::GFLT")
afpText_GCLINE = Class(name="afpText::GCLINE")
afpText_GMRK = Class(name="afpText::GMRK")
afpText_GCMRK = Class(name="afpText::GCMRK")
afpText_GNOP1 = Class(name="afpText::GNOP1")
afpText_GPARC = Class(name="afpText::GPARC")
afpText_GIMD = Class(name="afpText::GIMD")
afpText_GLINE = Class(name="afpText::GLINE")
afpText_GRLINE = Class(name="afpText::GRLINE")
afpText_GCRLINE = Class(name="afpText::GCRLINE")
afpText_GCPARC = Class(name="afpText::GCPARC")
afpText_GSBMX = Class(name="afpText::GSBMX")
afpText_GSCA = Class(name="afpText::GSCA")
afpText_GSCC = Class(name="afpText::GSCC")
afpText_GSCD = Class(name="afpText::GSCD")
afpText_GSGCH = Class(name="afpText::GSGCH")
afpText_GSAP = Class(name="afpText::GSAP")
afpText_GSCOL = Class(name="afpText::GSCOL")
afpText_GSCP = Class(name="afpText::GSCP")
afpText_GSECOL = Class(name="afpText::GSECOL")
afpText_GSFLW = Class(name="afpText::GSFLW")
afpText_GSLT = Class(name="afpText::GSLT")
afpText_GSCR = Class(name="afpText::GSCR")
afpText_GSCS = Class(name="afpText::GSCS")
afpText_GSCH = Class(name="afpText::GSCH")
afpText_GSMS = Class(name="afpText::GSMS")
afpText_GSMT = Class(name="afpText::GSMT")
afpText_GSMX = Class(name="afpText::GSMX")
afpText_GSPS = Class(name="afpText::GSPS")
afpText_GSPT = Class(name="afpText::GSPT")
afpText_GSLW = Class(name="afpText::GSLW")
afpText_GSMC = Class(name="afpText::GSMC")
afpText_GSMP = Class(name="afpText::GSMP")
afpText_GSLE = Class(name="afpText::GSLE")
afpText_GSLJ = Class(name="afpText::GSLJ")
afpText_GCBEZ = Class(name="afpText::GCBEZ")
afpText_GCCBEZ = Class(name="afpText::GCCBEZ")
afpText_GSPCOL = Class(name="afpText::GSPCOL")
afpText_DrawingOrderSubset = Class(name="afpText::DrawingOrderSubset")
afpText_TonerSaver = Class(name="afpText::TonerSaver")
afpText_ColorFidelity = Class(name="afpText::ColorFidelity")
afpText_FontFidelity = Class(name="afpText::FontFidelity")
afpText_WindowSpecification = Class(name="afpText::WindowSpecification")
afpText_FinishingFidelity = Class(name="afpText::FinishingFidelity")
afpText_CMRFidelity = Class(name="afpText::CMRFidelity")
afpText_ObjectByteExtent = Class(name="afpText::ObjectByteExtent")
afpText_ObjectByteOffset = Class(name="afpText::ObjectByteOffset")
afpText_ObjectStructuredFieldExtent = Class(name="afpText::ObjectStructuredFieldExtent")
afpText_TextFidelity = Class(name="afpText::TextFidelity")
afpText_MediaFidelity = Class(name="afpText::MediaFidelity")
afpText_ObjectOriginIdentifier = Class(name="afpText::ObjectOriginIdentifier")
afpText_LineDataObjectPositionMigration = Class(name="afpText::LineDataObjectPositionMigration")
afpText_ColorManagementResourceDescriptor = Class(name="afpText::ColorManagementResourceDescriptor")
afpText_ObjectStructuredFieldOffset = Class(name="afpText::ObjectStructuredFieldOffset")
afpText_ObjectCount = Class(name="afpText::ObjectCount")
afpText_ExtendedResourceLocalIdentifier = Class(name="afpText::ExtendedResourceLocalIdentifier")
afpText_MetricAdjustment = Class(name="afpText::MetricAdjustment")
afpText_ExtensionFont = Class(name="afpText::ExtensionFont")
afpText_ImageResolution = Class(name="afpText::ImageResolution")
afpText_ObjectContainerPresentationSpaceSize = Class(name="afpText::ObjectContainerPresentationSpaceSize")
afpText_LocaleSelector = Class(name="afpText::LocaleSelector")
afpText_FinishingOperation = Class(name="afpText::FinishingOperation")
afpText_RenderingIntent = Class(name="afpText::RenderingIntent")
afpText_FontCodedGraphicCharacterSetGlobalIdentifier = Class(name="afpText::FontCodedGraphicCharacterSetGlobalIdentifier")
afpText_PageOverlayConditionalProcessing = Class(name="afpText::PageOverlayConditionalProcessing")
afpText_ResourceUsageAttribute = Class(name="afpText::ResourceUsageAttribute")
afpText_UP3iFinishingOperation = Class(name="afpText::UP3iFinishingOperation")
afpText_DeviceAppearance = Class(name="afpText::DeviceAppearance")
afpText_ResourceObjectInclude = Class(name="afpText::ResourceObjectInclude")

# afpText_structuredField class attributes and methods

# afpText_LineData class attributes and methods
afpText_LineData_linedata: Property = Property(name="linedata", type=StringType)
afpText_LineData.attributes={afpText_LineData_linedata}

# structuredField class attributes and methods

# afpText_BAG class attributes and methods
afpText_BAG_AEGName: Property = Property(name="AEGName", type=StringType)
afpText_BAG.attributes={afpText_BAG_AEGName}

# afpText_triplet class attributes and methods

# afpText_BBC class attributes and methods
afpText_BBC_BCdoName: Property = Property(name="BCdoName", type=StringType)
afpText_BBC.attributes={afpText_BBC_BCdoName}

# afpText_Model class attributes and methods

# afpText_BDD class attributes and methods
afpText_BDD_UBASE: Property = Property(name="UBASE", type=StringType)
afpText_BDD_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_BDD_XUPUB: Property = Property(name="XUPUB", type=StringType)
afpText_BDD_YUPUB: Property = Property(name="YUPUB", type=StringType)
afpText_BDD_XEXTENT: Property = Property(name="XEXTENT", type=StringType)
afpText_BDD_YEXTENT: Property = Property(name="YEXTENT", type=StringType)
afpText_BDD_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_BDD_TYPE: Property = Property(name="TYPE", type=StringType)
afpText_BDD_MOD: Property = Property(name="MOD", type=StringType)
afpText_BDD_LID: Property = Property(name="LID", type=StringType)
afpText_BDD_COLOR: Property = Property(name="COLOR", type=StringType)
afpText_BDD_MODULEWIDTH: Property = Property(name="MODULEWIDTH", type=StringType)
afpText_BDD_ELEMENTHEIGHT: Property = Property(name="ELEMENTHEIGHT", type=StringType)
afpText_BDD_MULT: Property = Property(name="MULT", type=StringType)
afpText_BDD_WENE: Property = Property(name="WENE", type=StringType)
afpText_BDD.attributes={afpText_BDD_WENE, afpText_BDD_MULT, afpText_BDD_XEXTENT, afpText_BDD_YEXTENT, afpText_BDD_LID, afpText_BDD_Reserved2, afpText_BDD_MODULEWIDTH, afpText_BDD_TYPE, afpText_BDD_ELEMENTHEIGHT, afpText_BDD_XUPUB, afpText_BDD_Reserved, afpText_BDD_YUPUB, afpText_BDD_COLOR, afpText_BDD_UBASE, afpText_BDD_MOD}

# afpText_BCA class attributes and methods
afpText_BCA_CATName: Property = Property(name="CATName", type=StringType)
afpText_BCA.attributes={afpText_BCA_CATName}

# afpText_BCF class attributes and methods
afpText_BCF_RSName: Property = Property(name="RSName", type=StringType)
afpText_BCF.attributes={afpText_BCF_RSName}

# afpText_BCP class attributes and methods
afpText_BCP_RSName: Property = Property(name="RSName", type=StringType)
afpText_BCP.attributes={afpText_BCP_RSName}

# afpText_BDA class attributes and methods
afpText_BDA_Yoffset: Property = Property(name="Yoffset", type=StringType)
afpText_BDA_Data: Property = Property(name="Data", type=StringType)
afpText_BDA_Flags: Property = Property(name="Flags", type=StringType)
afpText_BDA_Xoffset: Property = Property(name="Xoffset", type=StringType)
afpText_BDA.attributes={afpText_BDA_Data, afpText_BDA_Yoffset, afpText_BDA_Flags, afpText_BDA_Xoffset}

# afpText_BDX class attributes and methods
afpText_BDX_DMXName: Property = Property(name="DMXName", type=StringType)
afpText_BDX.attributes={afpText_BDX_DMXName}

# afpText_BFG class attributes and methods
afpText_BFG_FEGName: Property = Property(name="FEGName", type=StringType)
afpText_BFG.attributes={afpText_BFG_FEGName}

# afpText_BFM class attributes and methods
afpText_BFM_FMName: Property = Property(name="FMName", type=StringType)
afpText_BFM.attributes={afpText_BFM_FMName}

# afpText_BFN class attributes and methods
afpText_BFN_RSName: Property = Property(name="RSName", type=StringType)
afpText_BFN.attributes={afpText_BFN_RSName}

# afpText_BGR class attributes and methods
afpText_BGR_GdoName: Property = Property(name="GdoName", type=StringType)
afpText_BGR.attributes={afpText_BGR_GdoName}

# afpText_BDG class attributes and methods
afpText_BDG_DEGName: Property = Property(name="DEGName", type=StringType)
afpText_BDG.attributes={afpText_BDG_DEGName}

# afpText_BDI class attributes and methods
afpText_BDI_IndxName: Property = Property(name="IndxName", type=StringType)
afpText_BDI.attributes={afpText_BDI_IndxName}

# afpText_BDM class attributes and methods
afpText_BDM_DMName: Property = Property(name="DMName", type=StringType)
afpText_BDM_DatFmt: Property = Property(name="DatFmt", type=StringType)
afpText_BDM.attributes={afpText_BDM_DMName, afpText_BDM_DatFmt}

# afpText_BDT class attributes and methods
afpText_BDT_DocName: Property = Property(name="DocName", type=StringType)
afpText_BDT_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_BDT.attributes={afpText_BDT_DocName, afpText_BDT_Reserved}

# afpText_BOG class attributes and methods
afpText_BOG_OEGName: Property = Property(name="OEGName", type=StringType)
afpText_BOG.attributes={afpText_BOG_OEGName}

# afpText_BPF class attributes and methods
afpText_BPF_PFName: Property = Property(name="PFName", type=StringType)
afpText_BPF.attributes={afpText_BPF_PFName}

# afpText_BPG class attributes and methods
afpText_BPG_PageName: Property = Property(name="PageName", type=StringType)
afpText_BPG.attributes={afpText_BPG_PageName}

# afpText_BII class attributes and methods
afpText_BII_ImoName: Property = Property(name="ImoName", type=StringType)
afpText_BII.attributes={afpText_BII_ImoName}

# afpText_BIM class attributes and methods
afpText_BIM_IdoName: Property = Property(name="IdoName", type=StringType)
afpText_BIM.attributes={afpText_BIM_IdoName}

# afpText_BMM class attributes and methods
afpText_BMM_MMName: Property = Property(name="MMName", type=StringType)
afpText_BMM.attributes={afpText_BMM_MMName}

# afpText_BMO class attributes and methods
afpText_BMO_OvlyName: Property = Property(name="OvlyName", type=StringType)
afpText_BMO.attributes={afpText_BMO_OvlyName}

# afpText_BNG class attributes and methods
afpText_BNG_PGrpName: Property = Property(name="PGrpName", type=StringType)
afpText_BNG.attributes={afpText_BNG_PGrpName}

# afpText_BOC class attributes and methods
afpText_BOC_ObjCName: Property = Property(name="ObjCName", type=StringType)
afpText_BOC.attributes={afpText_BOC_ObjCName}

# afpText_CAT class attributes and methods
afpText_CAT_CATData: Property = Property(name="CATData", type=StringType)
afpText_CAT.attributes={afpText_CAT_CATData}

# afpText_CDD class attributes and methods
afpText_CDD_XocBase: Property = Property(name="XocBase", type=StringType)
afpText_CDD_YocBase: Property = Property(name="YocBase", type=StringType)
afpText_CDD_XocUnits: Property = Property(name="XocUnits", type=StringType)
afpText_CDD_YocUnits: Property = Property(name="YocUnits", type=StringType)
afpText_CDD_XocSize: Property = Property(name="XocSize", type=StringType)
afpText_CDD_YocSize: Property = Property(name="YocSize", type=StringType)
afpText_CDD.attributes={afpText_CDD_XocSize, afpText_CDD_XocUnits, afpText_CDD_YocBase, afpText_CDD_YocUnits, afpText_CDD_YocSize, afpText_CDD_XocBase}

# afpText_CFC class attributes and methods
afpText_CFC_CFIRGLen: Property = Property(name="CFIRGLen", type=StringType)
afpText_CFC_Retired1: Property = Property(name="Retired1", type=StringType)
afpText_CFC.attributes={afpText_CFC_Retired1, afpText_CFC_CFIRGLen}

# afpText_BPM class attributes and methods
afpText_BPM_PMName: Property = Property(name="PMName", type=StringType)
afpText_BPM.attributes={afpText_BPM_PMName}

# afpText_BPS class attributes and methods
afpText_BPS_PsegName: Property = Property(name="PsegName", type=StringType)
afpText_BPS.attributes={afpText_BPS_PsegName}

# afpText_BPT class attributes and methods
afpText_BPT_PTdoName: Property = Property(name="PTdoName", type=StringType)
afpText_BPT.attributes={afpText_BPT_PTdoName}

# afpText_BRG class attributes and methods
afpText_BRG_RGrpName: Property = Property(name="RGrpName", type=StringType)
afpText_BRG.attributes={afpText_BRG_RGrpName}

# afpText_BRS class attributes and methods
afpText_BRS_RSName: Property = Property(name="RSName", type=StringType)
afpText_BRS.attributes={afpText_BRS_RSName}

# afpText_BSG class attributes and methods
afpText_BSG_REGName: Property = Property(name="REGName", type=StringType)
afpText_BSG.attributes={afpText_BSG_REGName}

# afpText_CTC class attributes and methods
afpText_CTC_ConData: Property = Property(name="ConData", type=StringType)
afpText_CTC.attributes={afpText_CTC_ConData}

# afpText_DXD class attributes and methods

# afpText_EAG class attributes and methods
afpText_EAG_AEGName: Property = Property(name="AEGName", type=StringType)
afpText_EAG.attributes={afpText_EAG_AEGName}

# afpText_EBC class attributes and methods
afpText_EBC_BCdoName: Property = Property(name="BCdoName", type=StringType)
afpText_EBC.attributes={afpText_EBC_BCdoName}

# afpText_ECA class attributes and methods
afpText_ECA_CATName: Property = Property(name="CATName", type=StringType)
afpText_ECA.attributes={afpText_ECA_CATName}

# afpText_CFI class attributes and methods

# afpText_CFIRG class attributes and methods
afpText_CFIRG_FCSName: Property = Property(name="FCSName", type=StringType)
afpText_CFIRG_CPName: Property = Property(name="CPName", type=StringType)
afpText_CFIRG_SVSize: Property = Property(name="SVSize", type=StringType)
afpText_CFIRG_SHScale: Property = Property(name="SHScale", type=StringType)
afpText_CFIRG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_CFIRG_Section: Property = Property(name="Section", type=StringType)
afpText_CFIRG.attributes={afpText_CFIRG_SHScale, afpText_CFIRG_CPName, afpText_CFIRG_SVSize, afpText_CFIRG_FCSName, afpText_CFIRG_Section, afpText_CFIRG_Reserved}

# afpText_CPC class attributes and methods
afpText_CPC_DefCharID: Property = Property(name="DefCharID", type=StringType)
afpText_CPC_PrtFlags: Property = Property(name="PrtFlags", type=StringType)
afpText_CPC_CPIRGLen: Property = Property(name="CPIRGLen", type=StringType)
afpText_CPC_VSCharSN: Property = Property(name="VSCharSN", type=StringType)
afpText_CPC_VSChar: Property = Property(name="VSChar", type=StringType)
afpText_CPC_VSFlags: Property = Property(name="VSFlags", type=StringType)
afpText_CPC.attributes={afpText_CPC_VSCharSN, afpText_CPC_DefCharID, afpText_CPC_CPIRGLen, afpText_CPC_PrtFlags, afpText_CPC_VSChar, afpText_CPC_VSFlags}

# afpText_CPD class attributes and methods
afpText_CPD_CPDesc: Property = Property(name="CPDesc", type=StringType)
afpText_CPD_GCGIDLen: Property = Property(name="GCGIDLen", type=StringType)
afpText_CPD_NumCdPts: Property = Property(name="NumCdPts", type=StringType)
afpText_CPD_GCSGID: Property = Property(name="GCSGID", type=StringType)
afpText_CPD_CPGID: Property = Property(name="CPGID", type=StringType)
afpText_CPD_EncScheme: Property = Property(name="EncScheme", type=StringType)
afpText_CPD.attributes={afpText_CPD_GCSGID, afpText_CPD_GCGIDLen, afpText_CPD_CPGID, afpText_CPD_EncScheme, afpText_CPD_CPDesc, afpText_CPD_NumCdPts}

# afpText_CPI class attributes and methods

# afpText_CPIRG class attributes and methods
afpText_CPIRG_GCGID: Property = Property(name="GCGID", type=StringType)
afpText_CPIRG_PrtFlags: Property = Property(name="PrtFlags", type=StringType)
afpText_CPIRG_CodePoint: Property = Property(name="CodePoint", type=StringType)
afpText_CPIRG_Count: Property = Property(name="Count", type=StringType)
afpText_CPIRG.attributes={afpText_CPIRG_CodePoint, afpText_CPIRG_PrtFlags, afpText_CPIRG_GCGID, afpText_CPIRG_Count}

# afpText_EFM class attributes and methods
afpText_EFM_FMName: Property = Property(name="FMName", type=StringType)
afpText_EFM.attributes={afpText_EFM_FMName}

# afpText_EFN class attributes and methods
afpText_EFN_RSName: Property = Property(name="RSName", type=StringType)
afpText_EFN.attributes={afpText_EFN_RSName}

# afpText_EGR class attributes and methods
afpText_EGR_GdoName: Property = Property(name="GdoName", type=StringType)
afpText_EGR.attributes={afpText_EGR_GdoName}

# afpText_EII class attributes and methods
afpText_EII_ImoName: Property = Property(name="ImoName", type=StringType)
afpText_EII.attributes={afpText_EII_ImoName}

# afpText_EIM class attributes and methods
afpText_EIM_IdoName: Property = Property(name="IdoName", type=StringType)
afpText_EIM.attributes={afpText_EIM_IdoName}

# afpText_ECF class attributes and methods
afpText_ECF_RSName: Property = Property(name="RSName", type=StringType)
afpText_ECF.attributes={afpText_ECF_RSName}

# afpText_ECP class attributes and methods
afpText_ECP_RSName: Property = Property(name="RSName", type=StringType)
afpText_ECP.attributes={afpText_ECP_RSName}

# afpText_EDG class attributes and methods
afpText_EDG_DEGName: Property = Property(name="DEGName", type=StringType)
afpText_EDG.attributes={afpText_EDG_DEGName}

# afpText_EDI class attributes and methods
afpText_EDI_IndxName: Property = Property(name="IndxName", type=StringType)
afpText_EDI.attributes={afpText_EDI_IndxName}

# afpText_EDM class attributes and methods
afpText_EDM_DMName: Property = Property(name="DMName", type=StringType)
afpText_EDM.attributes={afpText_EDM_DMName}

# afpText_EDT class attributes and methods
afpText_EDT_DocName: Property = Property(name="DocName", type=StringType)
afpText_EDT.attributes={afpText_EDT_DocName}

# afpText_EDX class attributes and methods
afpText_EDX_DMXName: Property = Property(name="DMXName", type=StringType)
afpText_EDX.attributes={afpText_EDX_DMXName}

# afpText_EFG class attributes and methods
afpText_EFG_FEGName: Property = Property(name="FEGName", type=StringType)
afpText_EFG.attributes={afpText_EFG_FEGName}

# afpText_EPF class attributes and methods
afpText_EPF_PFName: Property = Property(name="PFName", type=StringType)
afpText_EPF.attributes={afpText_EPF_PFName}

# afpText_EPG class attributes and methods
afpText_EPG_PageName: Property = Property(name="PageName", type=StringType)
afpText_EPG.attributes={afpText_EPG_PageName}

# afpText_EPM class attributes and methods
afpText_EPM_PMName: Property = Property(name="PMName", type=StringType)
afpText_EPM.attributes={afpText_EPM_PMName}

# afpText_EMM class attributes and methods
afpText_EMM_MMName: Property = Property(name="MMName", type=StringType)
afpText_EMM.attributes={afpText_EMM_MMName}

# afpText_EMO class attributes and methods
afpText_EMO_OvlyName: Property = Property(name="OvlyName", type=StringType)
afpText_EMO.attributes={afpText_EMO_OvlyName}

# afpText_ENG class attributes and methods
afpText_ENG_PGrpName: Property = Property(name="PGrpName", type=StringType)
afpText_ENG.attributes={afpText_ENG_PGrpName}

# afpText_EOC class attributes and methods
afpText_EOC_ObjCName: Property = Property(name="ObjCName", type=StringType)
afpText_EOC.attributes={afpText_EOC_ObjCName}

# afpText_EOG class attributes and methods
afpText_EOG_OEGName: Property = Property(name="OEGName", type=StringType)
afpText_EOG.attributes={afpText_EOG_OEGName}

# afpText_EPS class attributes and methods
afpText_EPS_PsegName: Property = Property(name="PsegName", type=StringType)
afpText_EPS.attributes={afpText_EPS_PsegName}

# afpText_EPT class attributes and methods
afpText_EPT_PTdoName: Property = Property(name="PTdoName", type=StringType)
afpText_EPT.attributes={afpText_EPT_PTdoName}

# afpText_ERG class attributes and methods
afpText_ERG_RGrpName: Property = Property(name="RGrpName", type=StringType)
afpText_ERG.attributes={afpText_ERG_RGrpName}

# afpText_ERS class attributes and methods
afpText_ERS_RSName: Property = Property(name="RSName", type=StringType)
afpText_ERS.attributes={afpText_ERS_RSName}

# afpText_ESG class attributes and methods
afpText_ESG_REGName: Property = Property(name="REGName", type=StringType)
afpText_ESG.attributes={afpText_ESG_REGName}

# afpText_FNC class attributes and methods
afpText_FNC_XUnitBase: Property = Property(name="XUnitBase", type=StringType)
afpText_FNC_YUnitBase: Property = Property(name="YUnitBase", type=StringType)
afpText_FNC_XftUnits: Property = Property(name="XftUnits", type=StringType)
afpText_FNC_YftUnits: Property = Property(name="YftUnits", type=StringType)
afpText_FNC_MaxBoxWd: Property = Property(name="MaxBoxWd", type=StringType)
afpText_FNC_MaxBoxHt: Property = Property(name="MaxBoxHt", type=StringType)
afpText_FNC_FNORGLen: Property = Property(name="FNORGLen", type=StringType)
afpText_FNC_FNIRGLen: Property = Property(name="FNIRGLen", type=StringType)
afpText_FNC_PatAlign: Property = Property(name="PatAlign", type=StringType)
afpText_FNC_RPatDCnt: Property = Property(name="RPatDCnt", type=StringType)
afpText_FNC_FNPRGLen: Property = Property(name="FNPRGLen", type=StringType)
afpText_FNC_FNMRGLen: Property = Property(name="FNMRGLen", type=StringType)
afpText_FNC_ResXUBase: Property = Property(name="ResXUBase", type=StringType)
afpText_FNC_ResYUBase: Property = Property(name="ResYUBase", type=StringType)
afpText_FNC_XfrUnits: Property = Property(name="XfrUnits", type=StringType)
afpText_FNC_YfrUnits: Property = Property(name="YfrUnits", type=StringType)
afpText_FNC_OPatDCnt: Property = Property(name="OPatDCnt", type=StringType)
afpText_FNC_Retired: Property = Property(name="Retired", type=StringType)
afpText_FNC_PatTech: Property = Property(name="PatTech", type=StringType)
afpText_FNC_Reserved1: Property = Property(name="Reserved1", type=StringType)
afpText_FNC_FntFlags: Property = Property(name="FntFlags", type=StringType)
afpText_FNC_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_FNC_FNNRGLen: Property = Property(name="FNNRGLen", type=StringType)
afpText_FNC_FNNDCnt: Property = Property(name="FNNDCnt", type=StringType)
afpText_FNC_FNNMapCnt: Property = Property(name="FNNMapCnt", type=StringType)
afpText_FNC.attributes={afpText_FNC_FNORGLen, afpText_FNC_YftUnits, afpText_FNC_FNNRGLen, afpText_FNC_RPatDCnt, afpText_FNC_FNMRGLen, afpText_FNC_MaxBoxHt, afpText_FNC_YfrUnits, afpText_FNC_PatAlign, afpText_FNC_FntFlags, afpText_FNC_MaxBoxWd, afpText_FNC_FNIRGLen, afpText_FNC_FNPRGLen, afpText_FNC_Reserved2, afpText_FNC_FNNMapCnt, afpText_FNC_XUnitBase, afpText_FNC_PatTech, afpText_FNC_ResXUBase, afpText_FNC_Retired, afpText_FNC_YUnitBase, afpText_FNC_OPatDCnt, afpText_FNC_XfrUnits, afpText_FNC_ResYUBase, afpText_FNC_Reserved1, afpText_FNC_XftUnits, afpText_FNC_FNNDCnt}

# afpText_FNG class attributes and methods
afpText_FNG_PatData: Property = Property(name="PatData", type=StringType)
afpText_FNG.attributes={afpText_FNG_PatData}

# afpText_FNI class attributes and methods

# afpText_FNIRG class attributes and methods
afpText_FNIRG_GCGID: Property = Property(name="GCGID", type=StringType)
afpText_FNIRG_CharInc: Property = Property(name="CharInc", type=StringType)
afpText_FNIRG_AscendHt: Property = Property(name="AscendHt", type=StringType)
afpText_FNIRG_DescendDp: Property = Property(name="DescendDp", type=StringType)
afpText_FNIRG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_FNIRG_FNMCnt: Property = Property(name="FNMCnt", type=StringType)
afpText_FNIRG_ASpace: Property = Property(name="ASpace", type=StringType)
afpText_FNIRG_BSpace: Property = Property(name="BSpace", type=StringType)
afpText_FNIRG_CSpace: Property = Property(name="CSpace", type=StringType)
afpText_FNIRG_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_FNIRG_BaseOset: Property = Property(name="BaseOset", type=StringType)
afpText_FNIRG.attributes={afpText_FNIRG_CSpace, afpText_FNIRG_BSpace, afpText_FNIRG_Reserved2, afpText_FNIRG_Reserved, afpText_FNIRG_FNMCnt, afpText_FNIRG_DescendDp, afpText_FNIRG_AscendHt, afpText_FNIRG_GCGID, afpText_FNIRG_BaseOset, afpText_FNIRG_ASpace, afpText_FNIRG_CharInc}

# afpText_FNN class attributes and methods
afpText_FNN_FNNData: Property = Property(name="FNNData", type=StringType)
afpText_FNN.attributes={afpText_FNN_FNNData}

# afpText_FNM class attributes and methods

# afpText_FNMRG class attributes and methods
afpText_FNMRG_CharBoxWd: Property = Property(name="CharBoxWd", type=StringType)
afpText_FNMRG_CharBoxHt: Property = Property(name="CharBoxHt", type=StringType)
afpText_FNMRG_PatDOset: Property = Property(name="PatDOset", type=StringType)
afpText_FNMRG.attributes={afpText_FNMRG_PatDOset, afpText_FNMRG_CharBoxHt, afpText_FNMRG_CharBoxWd}

# afpText_FND class attributes and methods
afpText_FND_TypeFcDesc: Property = Property(name="TypeFcDesc", type=StringType)
afpText_FND_FtWtClass: Property = Property(name="FtWtClass", type=StringType)
afpText_FND_FtWdClass: Property = Property(name="FtWdClass", type=StringType)
afpText_FND_MaxPtSize: Property = Property(name="MaxPtSize", type=StringType)
afpText_FND_NomPtSize: Property = Property(name="NomPtSize", type=StringType)
afpText_FND_MinPtSize: Property = Property(name="MinPtSize", type=StringType)
afpText_FND_MaxHSize: Property = Property(name="MaxHSize", type=StringType)
afpText_FND_NomHSize: Property = Property(name="NomHSize", type=StringType)
afpText_FND_MinHSize: Property = Property(name="MinHSize", type=StringType)
afpText_FND_DsnGenCls: Property = Property(name="DsnGenCls", type=StringType)
afpText_FND_DsnSubCls: Property = Property(name="DsnSubCls", type=StringType)
afpText_FND_DsnSpcGrp: Property = Property(name="DsnSpcGrp", type=StringType)
afpText_FND_Reserved1: Property = Property(name="Reserved1", type=StringType)
afpText_FND_FtDsFlags: Property = Property(name="FtDsFlags", type=StringType)
afpText_FND_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_FND_GCSID: Property = Property(name="GCSID", type=StringType)
afpText_FND_FGID: Property = Property(name="FGID", type=StringType)
afpText_FND.attributes={afpText_FND_Reserved2, afpText_FND_MaxHSize, afpText_FND_FtWtClass, afpText_FND_NomHSize, afpText_FND_NomPtSize, afpText_FND_FGID, afpText_FND_MaxPtSize, afpText_FND_DsnSubCls, afpText_FND_DsnSpcGrp, afpText_FND_MinPtSize, afpText_FND_Reserved1, afpText_FND_MinHSize, afpText_FND_TypeFcDesc, afpText_FND_FtDsFlags, afpText_FND_DsnGenCls, afpText_FND_FtWdClass, afpText_FND_GCSID}

# afpText_IEL class attributes and methods

# afpText_FNO class attributes and methods

# afpText_FNORG class attributes and methods
afpText_FNORG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_FNORG_CharRot: Property = Property(name="CharRot", type=StringType)
afpText_FNORG_MaxBOset: Property = Property(name="MaxBOset", type=StringType)
afpText_FNORG_MaxCharInc: Property = Property(name="MaxCharInc", type=StringType)
afpText_FNORG_SpCharInc: Property = Property(name="SpCharInc", type=StringType)
afpText_FNORG_MaxBExt: Property = Property(name="MaxBExt", type=StringType)
afpText_FNORG_OrntFlgs: Property = Property(name="OrntFlgs", type=StringType)
afpText_FNORG_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_FNORG_EmSpInc: Property = Property(name="EmSpInc", type=StringType)
afpText_FNORG_Reserved3: Property = Property(name="Reserved3", type=StringType)
afpText_FNORG_FigSpInc: Property = Property(name="FigSpInc", type=StringType)
afpText_FNORG_NomCharInc: Property = Property(name="NomCharInc", type=StringType)
afpText_FNORG_DefBInc: Property = Property(name="DefBInc", type=StringType)
afpText_FNORG_MinASp: Property = Property(name="MinASp", type=StringType)
afpText_FNORG.attributes={afpText_FNORG_MaxCharInc, afpText_FNORG_Reserved2, afpText_FNORG_Reserved3, afpText_FNORG_MinASp, afpText_FNORG_MaxBExt, afpText_FNORG_CharRot, afpText_FNORG_DefBInc, afpText_FNORG_Reserved, afpText_FNORG_FigSpInc, afpText_FNORG_NomCharInc, afpText_FNORG_OrntFlgs, afpText_FNORG_EmSpInc, afpText_FNORG_MaxBOset, afpText_FNORG_SpCharInc}

# afpText_FNP class attributes and methods

# afpText_FNPRG class attributes and methods
afpText_FNPRG_Retired: Property = Property(name="Retired", type=StringType)
afpText_FNPRG_Reserved3: Property = Property(name="Reserved3", type=StringType)
afpText_FNPRG_UscoreWd: Property = Property(name="UscoreWd", type=StringType)
afpText_FNPRG_UscoreWdf: Property = Property(name="UscoreWdf", type=StringType)
afpText_FNPRG_UscorePos: Property = Property(name="UscorePos", type=StringType)
afpText_FNPRG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_FNPRG_LcHeight: Property = Property(name="LcHeight", type=StringType)
afpText_FNPRG_CapMHt: Property = Property(name="CapMHt", type=StringType)
afpText_FNPRG_MaxAscHt: Property = Property(name="MaxAscHt", type=StringType)
afpText_FNPRG_MaxDesDp: Property = Property(name="MaxDesDp", type=StringType)
afpText_FNPRG_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_FNPRG.attributes={afpText_FNPRG_Reserved3, afpText_FNPRG_MaxAscHt, afpText_FNPRG_Reserved2, afpText_FNPRG_Reserved, afpText_FNPRG_MaxDesDp, afpText_FNPRG_UscoreWdf, afpText_FNPRG_CapMHt, afpText_FNPRG_UscoreWd, afpText_FNPRG_UscorePos, afpText_FNPRG_LcHeight, afpText_FNPRG_Retired}

# afpText_GAD class attributes and methods
afpText_GAD_GOCAdat: Property = Property(name="GOCAdat", type=StringType)
afpText_GAD.attributes={afpText_GAD_GOCAdat}

# afpText_GDD class attributes and methods
afpText_GDD_GOCAdes: Property = Property(name="GOCAdes", type=StringType)
afpText_GDD.attributes={afpText_GDD_GOCAdes}

# afpText_ICP class attributes and methods
afpText_ICP_XCOset: Property = Property(name="XCOset", type=StringType)
afpText_ICP_YCOset: Property = Property(name="YCOset", type=StringType)
afpText_ICP_XCSize: Property = Property(name="XCSize", type=StringType)
afpText_ICP_YCSize: Property = Property(name="YCSize", type=StringType)
afpText_ICP_XFilSize: Property = Property(name="XFilSize", type=StringType)
afpText_ICP_YFilSize: Property = Property(name="YFilSize", type=StringType)
afpText_ICP.attributes={afpText_ICP_YCOset, afpText_ICP_YCSize, afpText_ICP_XCOset, afpText_ICP_XCSize, afpText_ICP_YFilSize, afpText_ICP_XFilSize}

# afpText_IDD class attributes and methods
afpText_IDD_UNITBASE: Property = Property(name="UNITBASE", type=StringType)
afpText_IDD_XRESOL: Property = Property(name="XRESOL", type=StringType)
afpText_IDD_YRESOL: Property = Property(name="YRESOL", type=StringType)
afpText_IDD_XSIZE: Property = Property(name="XSIZE", type=StringType)
afpText_IDD_YSIZE: Property = Property(name="YSIZE", type=StringType)
afpText_IDD.attributes={afpText_IDD_UNITBASE, afpText_IDD_YRESOL, afpText_IDD_XSIZE, afpText_IDD_XRESOL, afpText_IDD_YSIZE}

# afpText_IOC class attributes and methods
afpText_IOC_XoaOset: Property = Property(name="XoaOset", type=StringType)
afpText_IOC_YoaOset: Property = Property(name="YoaOset", type=StringType)
afpText_IOC_XoaOrent: Property = Property(name="XoaOrent", type=StringType)
afpText_IOC_YoaOrent: Property = Property(name="YoaOrent", type=StringType)
afpText_IOC_ConData1: Property = Property(name="ConData1", type=StringType)
afpText_IOC_XMap: Property = Property(name="XMap", type=StringType)
afpText_IOC_YMap: Property = Property(name="YMap", type=StringType)
afpText_IOC_ConData2: Property = Property(name="ConData2", type=StringType)
afpText_IOC.attributes={afpText_IOC_ConData1, afpText_IOC_ConData2, afpText_IOC_YMap, afpText_IOC_XoaOset, afpText_IOC_YoaOset, afpText_IOC_XoaOrent, afpText_IOC_YoaOrent, afpText_IOC_XMap}

# afpText_IID class attributes and methods
afpText_IID_ConData1: Property = Property(name="ConData1", type=StringType)
afpText_IID_XBase: Property = Property(name="XBase", type=StringType)
afpText_IID_YBase: Property = Property(name="YBase", type=StringType)
afpText_IID_XUnits: Property = Property(name="XUnits", type=StringType)
afpText_IID_YUnits: Property = Property(name="YUnits", type=StringType)
afpText_IID_XSize: Property = Property(name="XSize", type=StringType)
afpText_IID_YSize: Property = Property(name="YSize", type=StringType)
afpText_IID_ConData2: Property = Property(name="ConData2", type=StringType)
afpText_IID_XCSizeD: Property = Property(name="XCSizeD", type=StringType)
afpText_IID_YCSizeD: Property = Property(name="YCSizeD", type=StringType)
afpText_IID_ConData3: Property = Property(name="ConData3", type=StringType)
afpText_IID_Color: Property = Property(name="Color", type=StringType)
afpText_IID.attributes={afpText_IID_XBase, afpText_IID_ConData1, afpText_IID_YCSizeD, afpText_IID_YBase, afpText_IID_XUnits, afpText_IID_YUnits, afpText_IID_XSize, afpText_IID_Color, afpText_IID_YSize, afpText_IID_XCSizeD, afpText_IID_ConData2, afpText_IID_ConData3}

# afpText_IMM class attributes and methods
afpText_IMM_MMPName: Property = Property(name="MMPName", type=StringType)
afpText_IMM.attributes={afpText_IMM_MMPName}

# afpText_IOB class attributes and methods
afpText_IOB_XocaOset: Property = Property(name="XocaOset", type=StringType)
afpText_IOB_YocaOset: Property = Property(name="YocaOset", type=StringType)
afpText_IOB_RefCSys: Property = Property(name="RefCSys", type=StringType)
afpText_IOB_ObjName: Property = Property(name="ObjName", type=StringType)
afpText_IOB_ObjType: Property = Property(name="ObjType", type=StringType)
afpText_IOB_XoaOset: Property = Property(name="XoaOset", type=StringType)
afpText_IOB_YoaOset: Property = Property(name="YoaOset", type=StringType)
afpText_IOB_XoaOrent: Property = Property(name="XoaOrent", type=StringType)
afpText_IOB_YoaOrent: Property = Property(name="YoaOrent", type=StringType)
afpText_IOB.attributes={afpText_IOB_YocaOset, afpText_IOB_YoaOset, afpText_IOB_ObjName, afpText_IOB_XoaOrent, afpText_IOB_XoaOset, afpText_IOB_YoaOrent, afpText_IOB_ObjType, afpText_IOB_RefCSys, afpText_IOB_XocaOset}

# afpText_IRD class attributes and methods
afpText_IRD_IMdata: Property = Property(name="IMdata", type=StringType)
afpText_IRD.attributes={afpText_IRD_IMdata}

# afpText_LLE class attributes and methods
afpText_LLE_LnkType: Property = Property(name="LnkType", type=StringType)
afpText_LLE.attributes={afpText_LLE_LnkType}

# afpText_LLERG class attributes and methods
afpText_LLERG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_LLERG_RGFunct: Property = Property(name="RGFunct", type=StringType)
afpText_LLERG.attributes={afpText_LLERG_RGFunct, afpText_LLERG_RGLength}

# afpText_LNC class attributes and methods
afpText_LNC_NumDSC: Property = Property(name="NumDSC", type=StringType)
afpText_LNC.attributes={afpText_LNC_NumDSC}

# afpText_LND class attributes and methods
afpText_LND_LNDFlgs: Property = Property(name="LNDFlgs", type=StringType)
afpText_LND_IPos: Property = Property(name="IPos", type=StringType)
afpText_LND_BPos: Property = Property(name="BPos", type=StringType)
afpText_LND_TxtOrent: Property = Property(name="TxtOrent", type=StringType)
afpText_LND_FntLID: Property = Property(name="FntLID", type=StringType)
afpText_LND_ChnlCde: Property = Property(name="ChnlCde", type=StringType)
afpText_LND_NLNDskp: Property = Property(name="NLNDskp", type=StringType)
afpText_LND_NLNDsp: Property = Property(name="NLNDsp", type=StringType)
afpText_LND_NLNDreu: Property = Property(name="NLNDreu", type=StringType)
afpText_LND_SupName: Property = Property(name="SupName", type=StringType)
afpText_LND_SOLid: Property = Property(name="SOLid", type=StringType)
afpText_LND_DataStrt: Property = Property(name="DataStrt", type=StringType)
afpText_LND_DataLgth: Property = Property(name="DataLgth", type=StringType)
afpText_LND_TxtColor: Property = Property(name="TxtColor", type=StringType)
afpText_LND_NLNDccp: Property = Property(name="NLNDccp", type=StringType)
afpText_LND_SubpgID: Property = Property(name="SubpgID", type=StringType)
afpText_LND_CCPID: Property = Property(name="CCPID", type=StringType)
afpText_LND.attributes={afpText_LND_SupName, afpText_LND_ChnlCde, afpText_LND_NLNDsp, afpText_LND_DataStrt, afpText_LND_DataLgth, afpText_LND_TxtColor, afpText_LND_LNDFlgs, afpText_LND_FntLID, afpText_LND_IPos, afpText_LND_BPos, afpText_LND_SOLid, afpText_LND_NLNDccp, afpText_LND_NLNDskp, afpText_LND_CCPID, afpText_LND_NLNDreu, afpText_LND_SubpgID, afpText_LND_TxtOrent}

# afpText_IPD class attributes and methods
afpText_IPD_IOCAdat: Property = Property(name="IOCAdat", type=StringType)
afpText_IPD_imageData: Property = Property(name="imageData", type=StringType)
afpText_IPD.attributes={afpText_IPD_IOCAdat, afpText_IPD_imageData}

# afpText_IPG class attributes and methods
afpText_IPG_PgName: Property = Property(name="PgName", type=StringType)
afpText_IPG_IPgFlgs: Property = Property(name="IPgFlgs", type=StringType)
afpText_IPG.attributes={afpText_IPG_IPgFlgs, afpText_IPG_PgName}

# afpText_IPO class attributes and methods
afpText_IPO_OvlyName: Property = Property(name="OvlyName", type=StringType)
afpText_IPO_XolOset: Property = Property(name="XolOset", type=StringType)
afpText_IPO_YolOset: Property = Property(name="YolOset", type=StringType)
afpText_IPO_OvlyOrent: Property = Property(name="OvlyOrent", type=StringType)
afpText_IPO.attributes={afpText_IPO_OvlyName, afpText_IPO_OvlyOrent, afpText_IPO_XolOset, afpText_IPO_YolOset}

# afpText_IPS class attributes and methods
afpText_IPS_PsegName: Property = Property(name="PsegName", type=StringType)
afpText_IPS_XpsOset: Property = Property(name="XpsOset", type=StringType)
afpText_IPS_YpsOset: Property = Property(name="YpsOset", type=StringType)
afpText_IPS.attributes={afpText_IPS_XpsOset, afpText_IPS_PsegName, afpText_IPS_YpsOset}

# afpText_MCDRG class attributes and methods
afpText_MCDRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MCDRG.attributes={afpText_MCDRG_RGLength}

# afpText_MCF class attributes and methods

# afpText_MCFRG class attributes and methods
afpText_MCFRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MCFRG.attributes={afpText_MCFRG_RGLength}

# afpText_MCF1 class attributes and methods
afpText_MCF1_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MCF1.attributes={afpText_MCF1_RGLength}

# afpText_MCF1RG class attributes and methods
afpText_MCF1RG_FCSName: Property = Property(name="FCSName", type=StringType)
afpText_MCF1RG_CharRot: Property = Property(name="CharRot", type=StringType)
afpText_MCF1RG_CFLid: Property = Property(name="CFLid", type=StringType)
afpText_MCF1RG_Sectid: Property = Property(name="Sectid", type=StringType)
afpText_MCF1RG_CFName: Property = Property(name="CFName", type=StringType)
afpText_MCF1RG_CPName: Property = Property(name="CPName", type=StringType)
afpText_MCF1RG.attributes={afpText_MCF1RG_CPName, afpText_MCF1RG_FCSName, afpText_MCF1RG_CharRot, afpText_MCF1RG_Sectid, afpText_MCF1RG_CFName, afpText_MCF1RG_CFLid}

# afpText_MDD class attributes and methods
afpText_MDD_XmBase: Property = Property(name="XmBase", type=StringType)
afpText_MDD_YmBase: Property = Property(name="YmBase", type=StringType)
afpText_MDD_XmUnits: Property = Property(name="XmUnits", type=StringType)
afpText_MDD_YmUnits: Property = Property(name="YmUnits", type=StringType)
afpText_MDD_XmSize: Property = Property(name="XmSize", type=StringType)
afpText_MDD_YmSize: Property = Property(name="YmSize", type=StringType)
afpText_MDD_MDDFlgs: Property = Property(name="MDDFlgs", type=StringType)
afpText_MDD.attributes={afpText_MDD_YmBase, afpText_MDD_YmUnits, afpText_MDD_XmBase, afpText_MDD_XmSize, afpText_MDD_XmUnits, afpText_MDD_YmSize, afpText_MDD_MDDFlgs}

# afpText_MBC class attributes and methods

# afpText_MBCRG class attributes and methods
afpText_MBCRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MBCRG.attributes={afpText_MBCRG_RGLength}

# afpText_MCA class attributes and methods

# afpText_MCARG class attributes and methods
afpText_MCARG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MCARG.attributes={afpText_MCARG_RGLength}

# afpText_MCC class attributes and methods

# afpText_MCCRG class attributes and methods
afpText_MCCRG_Startnum: Property = Property(name="Startnum", type=StringType)
afpText_MCCRG_Stopnum: Property = Property(name="Stopnum", type=StringType)
afpText_MCCRG_MMCid: Property = Property(name="MMCid", type=StringType)
afpText_MCCRG.attributes={afpText_MCCRG_Startnum, afpText_MCCRG_MMCid, afpText_MCCRG_Stopnum}

# afpText_MCD class attributes and methods

# afpText_MMC class attributes and methods
afpText_MMC_MMCid: Property = Property(name="MMCid", type=StringType)
afpText_MMC_PARAMETER1: Property = Property(name="PARAMETER1", type=StringType)
afpText_MMC.attributes={afpText_MMC_MMCid, afpText_MMC_PARAMETER1}

# afpText_MMCRG class attributes and methods
afpText_MMCRG_key: Property = Property(name="key", type=StringType)
afpText_MMCRG_value: Property = Property(name="value", type=StringType)
afpText_MMCRG.attributes={afpText_MMCRG_key, afpText_MMCRG_value}

# afpText_MMD class attributes and methods

# afpText_MMDRG class attributes and methods
afpText_MMDRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MMDRG.attributes={afpText_MMDRG_RGLength}

# afpText_MDR class attributes and methods

# afpText_MDRRG class attributes and methods
afpText_MDRRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MDRRG.attributes={afpText_MDRRG_RGLength}

# afpText_MFC class attributes and methods
afpText_MFC_MFCFlgs: Property = Property(name="MFCFlgs", type=StringType)
afpText_MFC_MedColl: Property = Property(name="MedColl", type=StringType)
afpText_MFC_MFCScpe: Property = Property(name="MFCScpe", type=StringType)
afpText_MFC.attributes={afpText_MFC_MFCFlgs, afpText_MFC_MFCScpe, afpText_MFC_MedColl}

# afpText_MGO class attributes and methods

# afpText_MGORG class attributes and methods
afpText_MGORG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MGORG.attributes={afpText_MGORG_RGLength}

# afpText_MIO class attributes and methods

# afpText_MIORG class attributes and methods
afpText_MIORG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MIORG.attributes={afpText_MIORG_RGLength}

# afpText_MSURG class attributes and methods
afpText_MSURG_SUPname: Property = Property(name="SUPname", type=StringType)
afpText_MSURG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_MSURG_SUPid: Property = Property(name="SUPid", type=StringType)
afpText_MSURG.attributes={afpText_MSURG_SUPid, afpText_MSURG_Reserved, afpText_MSURG_SUPname}

# afpText_NOP class attributes and methods
afpText_NOP_UndfData: Property = Property(name="UndfData", type=StringType)
afpText_NOP.attributes={afpText_NOP_UndfData}

# afpText_OBD class attributes and methods

# afpText_OBP class attributes and methods
afpText_OBP_OAPosID: Property = Property(name="OAPosID", type=StringType)
afpText_OBP_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_OBP_XoaOset: Property = Property(name="XoaOset", type=StringType)
afpText_OBP_YoaOset: Property = Property(name="YoaOset", type=StringType)
afpText_OBP_XoaOrent: Property = Property(name="XoaOrent", type=StringType)
afpText_OBP_YoaOrent: Property = Property(name="YoaOrent", type=StringType)
afpText_OBP_XocaOset: Property = Property(name="XocaOset", type=StringType)
afpText_OBP_YocaOset: Property = Property(name="YocaOset", type=StringType)
afpText_OBP_XocaOrent: Property = Property(name="XocaOrent", type=StringType)
afpText_OBP_YocaOrent: Property = Property(name="YocaOrent", type=StringType)
afpText_OBP_RefCSys: Property = Property(name="RefCSys", type=StringType)
afpText_OBP.attributes={afpText_OBP_YoaOset, afpText_OBP_XoaOrent, afpText_OBP_XocaOset, afpText_OBP_RGLength, afpText_OBP_YocaOrent, afpText_OBP_XocaOrent, afpText_OBP_OAPosID, afpText_OBP_YocaOset, afpText_OBP_YoaOrent, afpText_OBP_XoaOset, afpText_OBP_RefCSys}

# afpText_MMO class attributes and methods
afpText_MMO_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MMO.attributes={afpText_MMO_RGLength}

# afpText_MMORG class attributes and methods
afpText_MMORG_OVLid: Property = Property(name="OVLid", type=StringType)
afpText_MMORG_Flags: Property = Property(name="Flags", type=StringType)
afpText_MMORG_OVLname: Property = Property(name="OVLname", type=StringType)
afpText_MMORG.attributes={afpText_MMORG_OVLid, afpText_MMORG_OVLname, afpText_MMORG_Flags}

# afpText_MMT class attributes and methods

# afpText_MMTRG class attributes and methods
afpText_MMTRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MMTRG.attributes={afpText_MMTRG_RGLength}

# afpText_MPG class attributes and methods

# afpText_MPGRG class attributes and methods
afpText_MPGRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MPGRG.attributes={afpText_MPGRG_RGLength}

# afpText_MPO class attributes and methods

# afpText_MPORG class attributes and methods
afpText_MPORG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MPORG.attributes={afpText_MPORG_RGLength}

# afpText_MPS class attributes and methods
afpText_MPS_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_MPS_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_MPS.attributes={afpText_MPS_RGLength, afpText_MPS_Reserved}

# afpText_MPSRG class attributes and methods
afpText_MPSRG_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_MPSRG_PsegName: Property = Property(name="PsegName", type=StringType)
afpText_MPSRG.attributes={afpText_MPSRG_PsegName, afpText_MPSRG_Reserved}

# afpText_MSU class attributes and methods

# afpText_PGP class attributes and methods
afpText_PGP_Constant: Property = Property(name="Constant", type=StringType)
afpText_PGP.attributes={afpText_PGP_Constant}

# afpText_PGPRG class attributes and methods
afpText_PGPRG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_PGPRG_XmOset: Property = Property(name="XmOset", type=StringType)
afpText_PGPRG_YmOset: Property = Property(name="YmOset", type=StringType)
afpText_PGPRG_PGorient: Property = Property(name="PGorient", type=StringType)
afpText_PGPRG_SHside: Property = Property(name="SHside", type=StringType)
afpText_PGPRG_PgFlgs: Property = Property(name="PgFlgs", type=StringType)
afpText_PGPRG_PMCid: Property = Property(name="PMCid", type=StringType)
afpText_PGPRG.attributes={afpText_PGPRG_YmOset, afpText_PGPRG_PGorient, afpText_PGPRG_SHside, afpText_PGPRG_PgFlgs, afpText_PGPRG_PMCid, afpText_PGPRG_RGLength, afpText_PGPRG_XmOset}

# afpText_PGP1 class attributes and methods
afpText_PGP1_XOset: Property = Property(name="XOset", type=StringType)
afpText_PGP1_YOset: Property = Property(name="YOset", type=StringType)
afpText_PGP1.attributes={afpText_PGP1_YOset, afpText_PGP1_XOset}

# afpText_PMC class attributes and methods
afpText_PMC_PMCid: Property = Property(name="PMCid", type=StringType)
afpText_PMC.attributes={afpText_PMC_PMCid}

# afpText_OCD class attributes and methods
afpText_OCD_ObjCdat: Property = Property(name="ObjCdat", type=StringType)
afpText_OCD.attributes={afpText_OCD_ObjCdat}

# afpText_PEC class attributes and methods

# afpText_PFC class attributes and methods
afpText_PFC_PFCFlgs: Property = Property(name="PFCFlgs", type=StringType)
afpText_PFC.attributes={afpText_PFC_PFCFlgs}

# afpText_PGD class attributes and methods
afpText_PGD_YpgUnits: Property = Property(name="YpgUnits", type=StringType)
afpText_PGD_XpgSize: Property = Property(name="XpgSize", type=StringType)
afpText_PGD_YpgSize: Property = Property(name="YpgSize", type=StringType)
afpText_PGD_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_PGD_XpgBase: Property = Property(name="XpgBase", type=StringType)
afpText_PGD_YpgBase: Property = Property(name="YpgBase", type=StringType)
afpText_PGD_XpgUnits: Property = Property(name="XpgUnits", type=StringType)
afpText_PGD.attributes={afpText_PGD_YpgUnits, afpText_PGD_XpgUnits, afpText_PGD_XpgSize, afpText_PGD_YpgSize, afpText_PGD_Reserved, afpText_PGD_YpgBase, afpText_PGD_XpgBase}

# afpText_PTD class attributes and methods
afpText_PTD_XPBASE: Property = Property(name="XPBASE", type=StringType)
afpText_PTD_YPBASE: Property = Property(name="YPBASE", type=StringType)
afpText_PTD_XPUNITVL: Property = Property(name="XPUNITVL", type=StringType)
afpText_PTD_YPUNITVL: Property = Property(name="YPUNITVL", type=StringType)
afpText_PTD_XPEXTENT: Property = Property(name="XPEXTENT", type=StringType)
afpText_PTD_YPEXTENT: Property = Property(name="YPEXTENT", type=StringType)
afpText_PTD_RESERVED: Property = Property(name="RESERVED", type=StringType)
afpText_PTD.attributes={afpText_PTD_XPBASE, afpText_PTD_YPUNITVL, afpText_PTD_YPBASE, afpText_PTD_XPEXTENT, afpText_PTD_XPUNITVL, afpText_PTD_YPEXTENT, afpText_PTD_RESERVED}

# afpText_PPO class attributes and methods

# afpText_PPORG class attributes and methods
afpText_PPORG_RGLength: Property = Property(name="RGLength", type=StringType)
afpText_PPORG_ObjType: Property = Property(name="ObjType", type=StringType)
afpText_PPORG_ProcFlgs: Property = Property(name="ProcFlgs", type=StringType)
afpText_PPORG_XocaOset: Property = Property(name="XocaOset", type=StringType)
afpText_PPORG_YocaOset: Property = Property(name="YocaOset", type=StringType)
afpText_PPORG.attributes={afpText_PPORG_ObjType, afpText_PPORG_XocaOset, afpText_PPORG_YocaOset, afpText_PPORG_RGLength, afpText_PPORG_ProcFlgs}

# afpText_FGD class attributes and methods
afpText_FGD_ConData: Property = Property(name="ConData", type=StringType)
afpText_FGD.attributes={afpText_FGD_ConData}

# afpText_PTD1 class attributes and methods
afpText_PTD1_XPBASE: Property = Property(name="XPBASE", type=StringType)
afpText_PTD1_YPBASE: Property = Property(name="YPBASE", type=StringType)
afpText_PTD1_XPUNITVL: Property = Property(name="XPUNITVL", type=StringType)
afpText_PTD1_YPUNITVL: Property = Property(name="YPUNITVL", type=StringType)
afpText_PTD1_XPEXTENT: Property = Property(name="XPEXTENT", type=StringType)
afpText_PTD1_YPEXTENT: Property = Property(name="YPEXTENT", type=StringType)
afpText_PTD1_RESERVED: Property = Property(name="RESERVED", type=StringType)
afpText_PTD1.attributes={afpText_PTD1_RESERVED, afpText_PTD1_XPEXTENT, afpText_PTD1_YPUNITVL, afpText_PTD1_XPUNITVL, afpText_PTD1_YPBASE, afpText_PTD1_XPBASE, afpText_PTD1_YPEXTENT}

# afpText_PTX class attributes and methods

# afpText_TLE class attributes and methods

# afpText_BandImageRG class attributes and methods
afpText_BandImageRG_BITCNT: Property = Property(name="BITCNT", type=StringType)
afpText_BandImageRG.attributes={afpText_BandImageRG_BITCNT}

# afpText_TileTOCRG class attributes and methods
afpText_TileTOCRG_XOFFSET: Property = Property(name="XOFFSET", type=StringType)
afpText_TileTOCRG_YOFFSET: Property = Property(name="YOFFSET", type=StringType)
afpText_TileTOCRG_THSIZE: Property = Property(name="THSIZE", type=StringType)
afpText_TileTOCRG_TVSIZE: Property = Property(name="TVSIZE", type=StringType)
afpText_TileTOCRG_RELRES: Property = Property(name="RELRES", type=StringType)
afpText_TileTOCRG_COMPR: Property = Property(name="COMPR", type=StringType)
afpText_TileTOCRG_DATAPOS: Property = Property(name="DATAPOS", type=StringType)
afpText_TileTOCRG.attributes={afpText_TileTOCRG_DATAPOS, afpText_TileTOCRG_COMPR, afpText_TileTOCRG_XOFFSET, afpText_TileTOCRG_YOFFSET, afpText_TileTOCRG_TVSIZE, afpText_TileTOCRG_THSIZE, afpText_TileTOCRG_RELRES}

# afpText_SamplingRatiosRG class attributes and methods
afpText_SamplingRatiosRG_HSAMPLE: Property = Property(name="HSAMPLE", type=StringType)
afpText_SamplingRatiosRG_VSAMPLE: Property = Property(name="VSAMPLE", type=StringType)
afpText_SamplingRatiosRG.attributes={afpText_SamplingRatiosRG_HSAMPLE, afpText_SamplingRatiosRG_VSAMPLE}

# afpText_GFLTRG class attributes and methods
afpText_GFLTRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GFLTRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GFLTRG.attributes={afpText_GFLTRG_XPOS, afpText_GFLTRG_YPOS}

# afpText_GCFLTRG class attributes and methods
afpText_GCFLTRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCFLTRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCFLTRG.attributes={afpText_GCFLTRG_XPOS, afpText_GCFLTRG_YPOS}

# afpText_GLINERG class attributes and methods
afpText_GLINERG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GLINERG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GLINERG.attributes={afpText_GLINERG_XPOS, afpText_GLINERG_YPOS}

# afpText_GCLINERG class attributes and methods
afpText_GCLINERG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCLINERG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCLINERG.attributes={afpText_GCLINERG_YPOS, afpText_GCLINERG_XPOS}

# afpText_ExternalAlgorithmRG class attributes and methods
afpText_ExternalAlgorithmRG_DIRCTN: Property = Property(name="DIRCTN", type=StringType)
afpText_ExternalAlgorithmRG_PADBDRY: Property = Property(name="PADBDRY", type=StringType)
afpText_ExternalAlgorithmRG_PADALMT: Property = Property(name="PADALMT", type=StringType)
afpText_ExternalAlgorithmRG.attributes={afpText_ExternalAlgorithmRG_DIRCTN, afpText_ExternalAlgorithmRG_PADALMT, afpText_ExternalAlgorithmRG_PADBDRY}

# afpText_FNNRG class attributes and methods
afpText_FNNRG_GCGID: Property = Property(name="GCGID", type=StringType)
afpText_FNNRG_TSOffset: Property = Property(name="TSOffset", type=StringType)
afpText_FNNRG.attributes={afpText_FNNRG_TSOffset, afpText_FNNRG_GCGID}

# afpText_GCBEZRG class attributes and methods
afpText_GCBEZRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCBEZRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCBEZRG.attributes={afpText_GCBEZRG_YPOS, afpText_GCBEZRG_XPOS}

# afpText_GCCBEZRG class attributes and methods
afpText_GCCBEZRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCCBEZRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCCBEZRG.attributes={afpText_GCCBEZRG_YPOS, afpText_GCCBEZRG_XPOS}

# afpText_AMB class attributes and methods
afpText_AMB_DSPLCMNT: Property = Property(name="DSPLCMNT", type=StringType)
afpText_AMB.attributes={afpText_AMB_DSPLCMNT}

# triplet class attributes and methods

# afpText_AMI class attributes and methods
afpText_AMI_DSPLCMNT: Property = Property(name="DSPLCMNT", type=StringType)
afpText_AMI.attributes={afpText_AMI_DSPLCMNT}

# afpText_BLN class attributes and methods

# afpText_BSU class attributes and methods
afpText_BSU_LID: Property = Property(name="LID", type=StringType)
afpText_BSU.attributes={afpText_BSU_LID}

# afpText_DBR class attributes and methods
afpText_DBR_RLENGTH: Property = Property(name="RLENGTH", type=StringType)
afpText_DBR_RWIDTH: Property = Property(name="RWIDTH", type=StringType)
afpText_DBR_RWIDTHFRACTION: Property = Property(name="RWIDTHFRACTION", type=StringType)
afpText_DBR.attributes={afpText_DBR_RWIDTHFRACTION, afpText_DBR_RWIDTH, afpText_DBR_RLENGTH}

# afpText_GMRKRG class attributes and methods
afpText_GMRKRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GMRKRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GMRKRG.attributes={afpText_GMRKRG_XPOS, afpText_GMRKRG_YPOS}

# afpText_GCMRKRG class attributes and methods
afpText_GCMRKRG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCMRKRG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCMRKRG.attributes={afpText_GCMRKRG_YPOS, afpText_GCMRKRG_XPOS}

# afpText_GRLINERG class attributes and methods
afpText_GRLINERG_XOSSF: Property = Property(name="XOSSF", type=StringType)
afpText_GRLINERG_YOFFS: Property = Property(name="YOFFS", type=StringType)
afpText_GRLINERG.attributes={afpText_GRLINERG_XOSSF, afpText_GRLINERG_YOFFS}

# afpText_GCRLINERG class attributes and methods
afpText_GCRLINERG_XOSSF: Property = Property(name="XOSSF", type=StringType)
afpText_GCRLINERG_YOFFS: Property = Property(name="YOFFS", type=StringType)
afpText_GCRLINERG.attributes={afpText_GCRLINERG_XOSSF, afpText_GCRLINERG_YOFFS}

# afpText_OVS class attributes and methods
afpText_OVS_BYPSIDEN: Property = Property(name="BYPSIDEN", type=StringType)
afpText_OVS_OVERCHAR: Property = Property(name="OVERCHAR", type=StringType)
afpText_OVS.attributes={afpText_OVS_BYPSIDEN, afpText_OVS_OVERCHAR}

# afpText_RMB class attributes and methods
afpText_RMB_INCRMENT: Property = Property(name="INCRMENT", type=StringType)
afpText_RMB.attributes={afpText_RMB_INCRMENT}

# afpText_DIR class attributes and methods
afpText_DIR_RLENGTH: Property = Property(name="RLENGTH", type=StringType)
afpText_DIR_RWIDTH: Property = Property(name="RWIDTH", type=StringType)
afpText_DIR_RWIDTHFRACTION: Property = Property(name="RWIDTHFRACTION", type=StringType)
afpText_DIR.attributes={afpText_DIR_RWIDTHFRACTION, afpText_DIR_RLENGTH, afpText_DIR_RWIDTH}

# afpText_ESU class attributes and methods
afpText_ESU_LID: Property = Property(name="LID", type=StringType)
afpText_ESU.attributes={afpText_ESU_LID}

# afpText_NOPCS class attributes and methods
afpText_NOPCS_IGNDATA: Property = Property(name="IGNDATA", type=StringType)
afpText_NOPCS.attributes={afpText_NOPCS_IGNDATA}

# afpText_RMI class attributes and methods
afpText_RMI_INCRMENT: Property = Property(name="INCRMENT", type=StringType)
afpText_RMI.attributes={afpText_RMI_INCRMENT}

# afpText_RPS class attributes and methods
afpText_RPS_RLENGTH: Property = Property(name="RLENGTH", type=StringType)
afpText_RPS_RPTDATA: Property = Property(name="RPTDATA", type=StringType)
afpText_RPS.attributes={afpText_RPS_RLENGTH, afpText_RPS_RPTDATA}

# afpText_SBI class attributes and methods
afpText_SBI_INCRMENT: Property = Property(name="INCRMENT", type=StringType)
afpText_SBI.attributes={afpText_SBI_INCRMENT}

# afpText_SCFL class attributes and methods
afpText_SCFL_LID: Property = Property(name="LID", type=StringType)
afpText_SCFL.attributes={afpText_SCFL_LID}

# afpText_SEC class attributes and methods
afpText_SEC_RESERVED: Property = Property(name="RESERVED", type=StringType)
afpText_SEC_COLSPCE: Property = Property(name="COLSPCE", type=StringType)
afpText_SEC_COLSIZE1: Property = Property(name="COLSIZE1", type=StringType)
afpText_SEC_COLSIZE2: Property = Property(name="COLSIZE2", type=StringType)
afpText_SEC_COLSIZE3: Property = Property(name="COLSIZE3", type=StringType)
afpText_SEC_COLSIZE4: Property = Property(name="COLSIZE4", type=StringType)
afpText_SEC_COLVALUE: Property = Property(name="COLVALUE", type=StringType)
afpText_SEC.attributes={afpText_SEC_COLSIZE2, afpText_SEC_RESERVED, afpText_SEC_COLSIZE4, afpText_SEC_COLSIZE1, afpText_SEC_COLSPCE, afpText_SEC_COLVALUE, afpText_SEC_COLSIZE3}

# afpText_SIM class attributes and methods
afpText_SIM_DSPLCMNT: Property = Property(name="DSPLCMNT", type=StringType)
afpText_SIM.attributes={afpText_SIM_DSPLCMNT}

# afpText_STC class attributes and methods
afpText_STC_FRGCOLOR: Property = Property(name="FRGCOLOR", type=StringType)
afpText_STC_PRECSION: Property = Property(name="PRECSION", type=StringType)
afpText_STC.attributes={afpText_STC_FRGCOLOR, afpText_STC_PRECSION}

# afpText_STO class attributes and methods
afpText_STO_IORNTION: Property = Property(name="IORNTION", type=StringType)
afpText_STO_BORNTION: Property = Property(name="BORNTION", type=StringType)
afpText_STO.attributes={afpText_STO_BORNTION, afpText_STO_IORNTION}

# afpText_SVI class attributes and methods
afpText_SVI_INCRMENT: Property = Property(name="INCRMENT", type=StringType)
afpText_SVI.attributes={afpText_SVI_INCRMENT}

# afpText_AttributeValue class attributes and methods
afpText_AttributeValue_Reserved0: Property = Property(name="Reserved0", type=StringType)
afpText_AttributeValue_AttVal: Property = Property(name="AttVal", type=StringType)
afpText_AttributeValue.attributes={afpText_AttributeValue_Reserved0, afpText_AttributeValue_AttVal}

# afpText_SIA class attributes and methods
afpText_SIA_DIRCTION: Property = Property(name="DIRCTION", type=StringType)
afpText_SIA_ADJSTMNT: Property = Property(name="ADJSTMNT", type=StringType)
afpText_SIA.attributes={afpText_SIA_ADJSTMNT, afpText_SIA_DIRCTION}

# afpText_CGCSGID class attributes and methods
afpText_CGCSGID_GCSGID: Property = Property(name="GCSGID", type=StringType)
afpText_CGCSGID_CPGID: Property = Property(name="CPGID", type=StringType)
afpText_CGCSGID.attributes={afpText_CGCSGID_GCSGID, afpText_CGCSGID_CPGID}

# afpText_CRCResourceManagement class attributes and methods
afpText_CRCResourceManagement_FmtQual: Property = Property(name="FmtQual", type=StringType)
afpText_CRCResourceManagement_RMValue: Property = Property(name="RMValue", type=StringType)
afpText_CRCResourceManagement_ResClassFlg: Property = Property(name="ResClassFlg", type=StringType)
afpText_CRCResourceManagement.attributes={afpText_CRCResourceManagement_RMValue, afpText_CRCResourceManagement_FmtQual, afpText_CRCResourceManagement_ResClassFlg}

# afpText_CharacterRotation class attributes and methods
afpText_CharacterRotation_CharRot: Property = Property(name="CharRot", type=StringType)
afpText_CharacterRotation.attributes={afpText_CharacterRotation_CharRot}

# afpText_TBM class attributes and methods
afpText_TBM_DIRCTION: Property = Property(name="DIRCTION", type=StringType)
afpText_TBM_PRECSION: Property = Property(name="PRECSION", type=StringType)
afpText_TBM_INCRMENT: Property = Property(name="INCRMENT", type=StringType)
afpText_TBM.attributes={afpText_TBM_PRECSION, afpText_TBM_INCRMENT, afpText_TBM_DIRCTION}

# afpText_TRN class attributes and methods
afpText_TRN_TRNDATA: Property = Property(name="TRNDATA", type=StringType)
afpText_TRN.attributes={afpText_TRN_TRNDATA}

# afpText_USC class attributes and methods
afpText_USC_BYPSIDEN: Property = Property(name="BYPSIDEN", type=StringType)
afpText_USC.attributes={afpText_USC_BYPSIDEN}

# afpText_AttributeQualifier class attributes and methods
afpText_AttributeQualifier_SeqNum: Property = Property(name="SeqNum", type=StringType)
afpText_AttributeQualifier_LevNum: Property = Property(name="LevNum", type=StringType)
afpText_AttributeQualifier.attributes={afpText_AttributeQualifier_SeqNum, afpText_AttributeQualifier_LevNum}

# afpText_DescriptorPosition class attributes and methods
afpText_DescriptorPosition_DesPosID: Property = Property(name="DesPosID", type=StringType)
afpText_DescriptorPosition.attributes={afpText_DescriptorPosition_DesPosID}

# afpText_EncodingSchemeID class attributes and methods
afpText_EncodingSchemeID_ESidCP: Property = Property(name="ESidCP", type=StringType)
afpText_EncodingSchemeID_ESidUD: Property = Property(name="ESidUD", type=StringType)
afpText_EncodingSchemeID.attributes={afpText_EncodingSchemeID_ESidCP, afpText_EncodingSchemeID_ESidUD}

# afpText_FontResolution class attributes and methods
afpText_FontResolution_MetTech: Property = Property(name="MetTech", type=StringType)
afpText_FontResolution_RPuBase: Property = Property(name="RPuBase", type=StringType)
afpText_FontResolution_RPUnits: Property = Property(name="RPUnits", type=StringType)
afpText_FontResolution.attributes={afpText_FontResolution_RPUnits, afpText_FontResolution_MetTech, afpText_FontResolution_RPuBase}

# afpText_ColorSpecification class attributes and methods
afpText_ColorSpecification_ColSpce: Property = Property(name="ColSpce", type=StringType)
afpText_ColorSpecification_ColSize1: Property = Property(name="ColSize1", type=StringType)
afpText_ColorSpecification_ColSize2: Property = Property(name="ColSize2", type=StringType)
afpText_ColorSpecification_ColSize3: Property = Property(name="ColSize3", type=StringType)
afpText_ColorSpecification_ColSize4: Property = Property(name="ColSize4", type=StringType)
afpText_ColorSpecification_Color: Property = Property(name="Color", type=StringType)
afpText_ColorSpecification.attributes={afpText_ColorSpecification_ColSize1, afpText_ColorSpecification_Color, afpText_ColorSpecification_ColSpce, afpText_ColorSpecification_ColSize3, afpText_ColorSpecification_ColSize4, afpText_ColorSpecification_ColSize2}

# afpText_Comment class attributes and methods
afpText_Comment_Comment: Property = Property(name="Comment", type=StringType)
afpText_Comment.attributes={afpText_Comment_Comment}

# afpText_DataObjectFontDescriptor class attributes and methods
afpText_DataObjectFontDescriptor_FontTech: Property = Property(name="FontTech", type=StringType)
afpText_DataObjectFontDescriptor_VFS: Property = Property(name="VFS", type=StringType)
afpText_DataObjectFontDescriptor_HFS: Property = Property(name="HFS", type=StringType)
afpText_DataObjectFontDescriptor_CharRot: Property = Property(name="CharRot", type=StringType)
afpText_DataObjectFontDescriptor_EncEnv: Property = Property(name="EncEnv", type=StringType)
afpText_DataObjectFontDescriptor_EncID: Property = Property(name="EncID", type=StringType)
afpText_DataObjectFontDescriptor_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_DataObjectFontDescriptor_DOFtFlgs: Property = Property(name="DOFtFlgs", type=StringType)
afpText_DataObjectFontDescriptor.attributes={afpText_DataObjectFontDescriptor_FontTech, afpText_DataObjectFontDescriptor_CharRot, afpText_DataObjectFontDescriptor_HFS, afpText_DataObjectFontDescriptor_Reserved, afpText_DataObjectFontDescriptor_VFS, afpText_DataObjectFontDescriptor_EncID, afpText_DataObjectFontDescriptor_EncEnv, afpText_DataObjectFontDescriptor_DOFtFlgs}

# afpText_UniversalDateAndTimeStamp class attributes and methods
afpText_UniversalDateAndTimeStamp_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_UniversalDateAndTimeStamp_YearAD: Property = Property(name="YearAD", type=StringType)
afpText_UniversalDateAndTimeStamp_Month: Property = Property(name="Month", type=StringType)
afpText_UniversalDateAndTimeStamp_Day: Property = Property(name="Day", type=StringType)
afpText_UniversalDateAndTimeStamp_Hour: Property = Property(name="Hour", type=StringType)
afpText_UniversalDateAndTimeStamp_Minute: Property = Property(name="Minute", type=StringType)
afpText_UniversalDateAndTimeStamp_Second: Property = Property(name="Second", type=StringType)
afpText_UniversalDateAndTimeStamp_TimeZone: Property = Property(name="TimeZone", type=StringType)
afpText_UniversalDateAndTimeStamp_UTCDiffH: Property = Property(name="UTCDiffH", type=StringType)
afpText_UniversalDateAndTimeStamp_UTCDiffM: Property = Property(name="UTCDiffM", type=StringType)
afpText_UniversalDateAndTimeStamp.attributes={afpText_UniversalDateAndTimeStamp_TimeZone, afpText_UniversalDateAndTimeStamp_Day, afpText_UniversalDateAndTimeStamp_Second, afpText_UniversalDateAndTimeStamp_UTCDiffM, afpText_UniversalDateAndTimeStamp_UTCDiffH, afpText_UniversalDateAndTimeStamp_Month, afpText_UniversalDateAndTimeStamp_YearAD, afpText_UniversalDateAndTimeStamp_Hour, afpText_UniversalDateAndTimeStamp_Minute, afpText_UniversalDateAndTimeStamp_Reserved}

# afpText_FullyQualifiedName class attributes and methods
afpText_FullyQualifiedName_FQNType: Property = Property(name="FQNType", type=StringType)
afpText_FullyQualifiedName_FQNFormat: Property = Property(name="FQNFormat", type=StringType)
afpText_FullyQualifiedName_FQName: Property = Property(name="FQName", type=StringType)
afpText_FullyQualifiedName.attributes={afpText_FullyQualifiedName_FQNType, afpText_FullyQualifiedName_FQNFormat, afpText_FullyQualifiedName_FQName}

# afpText_LocalDateAndTimeStamp class attributes and methods
afpText_LocalDateAndTimeStamp_TenYear: Property = Property(name="TenYear", type=StringType)
afpText_LocalDateAndTimeStamp_Day: Property = Property(name="Day", type=StringType)
afpText_LocalDateAndTimeStamp_Hour: Property = Property(name="Hour", type=StringType)
afpText_LocalDateAndTimeStamp_Minute: Property = Property(name="Minute", type=StringType)
afpText_LocalDateAndTimeStamp_Second: Property = Property(name="Second", type=StringType)
afpText_LocalDateAndTimeStamp_HundSec: Property = Property(name="HundSec", type=StringType)
afpText_LocalDateAndTimeStamp_StampType: Property = Property(name="StampType", type=StringType)
afpText_LocalDateAndTimeStamp_THunYear: Property = Property(name="THunYear", type=StringType)
afpText_LocalDateAndTimeStamp.attributes={afpText_LocalDateAndTimeStamp_Second, afpText_LocalDateAndTimeStamp_THunYear, afpText_LocalDateAndTimeStamp_HundSec, afpText_LocalDateAndTimeStamp_Day, afpText_LocalDateAndTimeStamp_Minute, afpText_LocalDateAndTimeStamp_StampType, afpText_LocalDateAndTimeStamp_TenYear, afpText_LocalDateAndTimeStamp_Hour}

# afpText_MediumOrientation class attributes and methods
afpText_MediumOrientation_MedOrient: Property = Property(name="MedOrient", type=StringType)
afpText_MediumOrientation.attributes={afpText_MediumOrientation_MedOrient}

# afpText_MeasurementUnits class attributes and methods
afpText_MeasurementUnits_XoaBase: Property = Property(name="XoaBase", type=StringType)
afpText_MeasurementUnits_YoaBase: Property = Property(name="YoaBase", type=StringType)
afpText_MeasurementUnits_XoaUnits: Property = Property(name="XoaUnits", type=StringType)
afpText_MeasurementUnits_YoaUnits: Property = Property(name="YoaUnits", type=StringType)
afpText_MeasurementUnits.attributes={afpText_MeasurementUnits_YoaUnits, afpText_MeasurementUnits_XoaUnits, afpText_MeasurementUnits_XoaBase, afpText_MeasurementUnits_YoaBase}

# afpText_MODCAInterchangeSet class attributes and methods
afpText_MODCAInterchangeSet_IStype: Property = Property(name="IStype", type=StringType)
afpText_MODCAInterchangeSet_ISid: Property = Property(name="ISid", type=StringType)
afpText_MODCAInterchangeSet.attributes={afpText_MODCAInterchangeSet_IStype, afpText_MODCAInterchangeSet_ISid}

# afpText_ObjectAreaSize class attributes and methods
afpText_ObjectAreaSize_SizeType: Property = Property(name="SizeType", type=StringType)
afpText_ObjectAreaSize_XoaSize: Property = Property(name="XoaSize", type=StringType)
afpText_ObjectAreaSize_YoaSize: Property = Property(name="YoaSize", type=StringType)
afpText_ObjectAreaSize.attributes={afpText_ObjectAreaSize_YoaSize, afpText_ObjectAreaSize_SizeType, afpText_ObjectAreaSize_XoaSize}

# afpText_MappingOption class attributes and methods
afpText_MappingOption_MapValue: Property = Property(name="MapValue", type=StringType)
afpText_MappingOption.attributes={afpText_MappingOption_MapValue}

# afpText_MediaEjectControl class attributes and methods
afpText_MediaEjectControl_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_MediaEjectControl_EjCtrl: Property = Property(name="EjCtrl", type=StringType)
afpText_MediaEjectControl.attributes={afpText_MediaEjectControl_EjCtrl, afpText_MediaEjectControl_Reserved}

# afpText_MediumMapPageNumber class attributes and methods
afpText_MediumMapPageNumber_PageNum: Property = Property(name="PageNum", type=StringType)
afpText_MediumMapPageNumber.attributes={afpText_MediumMapPageNumber_PageNum}

# afpText_ObjectOffset class attributes and methods
afpText_ObjectOffset_ObjTpe: Property = Property(name="ObjTpe", type=StringType)
afpText_ObjectOffset_ObjOset: Property = Property(name="ObjOset", type=StringType)
afpText_ObjectOffset_ObjOstHi: Property = Property(name="ObjOstHi", type=StringType)
afpText_ObjectOffset.attributes={afpText_ObjectOffset_ObjOstHi, afpText_ObjectOffset_ObjOset, afpText_ObjectOffset_ObjTpe}

# afpText_ResourceObjectType class attributes and methods
afpText_ResourceObjectType_ObjType: Property = Property(name="ObjType", type=StringType)
afpText_ResourceObjectType_ConData: Property = Property(name="ConData", type=StringType)
afpText_ResourceObjectType.attributes={afpText_ResourceObjectType_ConData, afpText_ResourceObjectType_ObjType}

# afpText_PagePositionInformation class attributes and methods
afpText_PagePositionInformation_PGPRG: Property = Property(name="PGPRG", type=StringType)
afpText_PagePositionInformation.attributes={afpText_PagePositionInformation_PGPRG}

# afpText_PresentationControl class attributes and methods
afpText_PresentationControl_PRSFlg: Property = Property(name="PRSFlg", type=StringType)
afpText_PresentationControl.attributes={afpText_PresentationControl_PRSFlg}

# afpText_ObjectClassification class attributes and methods
afpText_ObjectClassification_ObjClass: Property = Property(name="ObjClass", type=StringType)
afpText_ObjectClassification_StrucFlgs: Property = Property(name="StrucFlgs", type=StringType)
afpText_ObjectClassification_RegObjId: Property = Property(name="RegObjId", type=StringType)
afpText_ObjectClassification_ObjTpName: Property = Property(name="ObjTpName", type=StringType)
afpText_ObjectClassification_ObjLev: Property = Property(name="ObjLev", type=StringType)
afpText_ObjectClassification_CompName: Property = Property(name="CompName", type=StringType)
afpText_ObjectClassification.attributes={afpText_ObjectClassification_ObjTpName, afpText_ObjectClassification_StrucFlgs, afpText_ObjectClassification_CompName, afpText_ObjectClassification_RegObjId, afpText_ObjectClassification_ObjLev, afpText_ObjectClassification_ObjClass}

# afpText_ObjectFunctionSetSpecification class attributes and methods
afpText_ObjectFunctionSetSpecification_ObjType: Property = Property(name="ObjType", type=StringType)
afpText_ObjectFunctionSetSpecification_ArchVrsn: Property = Property(name="ArchVrsn", type=StringType)
afpText_ObjectFunctionSetSpecification_DCAFnSet: Property = Property(name="DCAFnSet", type=StringType)
afpText_ObjectFunctionSetSpecification_OCAFnSet: Property = Property(name="OCAFnSet", type=StringType)
afpText_ObjectFunctionSetSpecification.attributes={afpText_ObjectFunctionSetSpecification_ArchVrsn, afpText_ObjectFunctionSetSpecification_OCAFnSet, afpText_ObjectFunctionSetSpecification_DCAFnSet, afpText_ObjectFunctionSetSpecification_ObjType}

# afpText_TextOrientation class attributes and methods
afpText_TextOrientation_IAxis: Property = Property(name="IAxis", type=StringType)
afpText_TextOrientation_BAxis: Property = Property(name="BAxis", type=StringType)
afpText_TextOrientation.attributes={afpText_TextOrientation_IAxis, afpText_TextOrientation_BAxis}

# afpText_FontHorizontalScaleFactor class attributes and methods
afpText_FontHorizontalScaleFactor_Hscale: Property = Property(name="Hscale", type=StringType)
afpText_FontHorizontalScaleFactor.attributes={afpText_FontHorizontalScaleFactor_Hscale}

# afpText_FontDescriptorSpecification class attributes and methods
afpText_FontDescriptorSpecification_FtWtClass: Property = Property(name="FtWtClass", type=StringType)
afpText_FontDescriptorSpecification_FtWdClass: Property = Property(name="FtWdClass", type=StringType)
afpText_FontDescriptorSpecification_FtHeight: Property = Property(name="FtHeight", type=StringType)
afpText_FontDescriptorSpecification_FtWidth: Property = Property(name="FtWidth", type=StringType)
afpText_FontDescriptorSpecification_FtDsFlags: Property = Property(name="FtDsFlags", type=StringType)
afpText_FontDescriptorSpecification_FtUsFlags: Property = Property(name="FtUsFlags", type=StringType)
afpText_FontDescriptorSpecification.attributes={afpText_FontDescriptorSpecification_FtWdClass, afpText_FontDescriptorSpecification_FtHeight, afpText_FontDescriptorSpecification_FtWidth, afpText_FontDescriptorSpecification_FtUsFlags, afpText_FontDescriptorSpecification_FtWtClass, afpText_FontDescriptorSpecification_FtDsFlags}

# afpText_PresentationSpaceResetMixing class attributes and methods
afpText_PresentationSpaceResetMixing_BgMxFlag: Property = Property(name="BgMxFlag", type=StringType)
afpText_PresentationSpaceResetMixing.attributes={afpText_PresentationSpaceResetMixing_BgMxFlag}

# afpText_PresentationSpaceMixingRules class attributes and methods

# afpText_ResourceLocalIdentifier class attributes and methods
afpText_ResourceLocalIdentifier_ResType: Property = Property(name="ResType", type=StringType)
afpText_ResourceLocalIdentifier_ResLID: Property = Property(name="ResLID", type=StringType)
afpText_ResourceLocalIdentifier.attributes={afpText_ResourceLocalIdentifier_ResType, afpText_ResourceLocalIdentifier_ResLID}

# afpText_BeginImage class attributes and methods
afpText_BeginImage_OBJTYPE: Property = Property(name="OBJTYPE", type=StringType)
afpText_BeginImage.attributes={afpText_BeginImage_OBJTYPE}

# afpText_ResourceSectionNumber class attributes and methods
afpText_ResourceSectionNumber_ResSNum: Property = Property(name="ResSNum", type=StringType)
afpText_ResourceSectionNumber.attributes={afpText_ResourceSectionNumber_ResSNum}

# afpText_EndImage class attributes and methods

# afpText_ImageSize class attributes and methods
afpText_ImageSize_UNITBASE: Property = Property(name="UNITBASE", type=StringType)
afpText_ImageSize_HRESOL: Property = Property(name="HRESOL", type=StringType)
afpText_ImageSize_VRESOL: Property = Property(name="VRESOL", type=StringType)
afpText_ImageSize_HSIZE: Property = Property(name="HSIZE", type=StringType)
afpText_ImageSize_VSIZE: Property = Property(name="VSIZE", type=StringType)
afpText_ImageSize.attributes={afpText_ImageSize_HSIZE, afpText_ImageSize_VSIZE, afpText_ImageSize_HRESOL, afpText_ImageSize_UNITBASE, afpText_ImageSize_VRESOL}

# afpText_ImageEncoding class attributes and methods
afpText_ImageEncoding_COMPRID: Property = Property(name="COMPRID", type=StringType)
afpText_ImageEncoding_RECID: Property = Property(name="RECID", type=StringType)
afpText_ImageEncoding_BITORDR: Property = Property(name="BITORDR", type=StringType)
afpText_ImageEncoding.attributes={afpText_ImageEncoding_RECID, afpText_ImageEncoding_COMPRID, afpText_ImageEncoding_BITORDR}

# afpText_BeginSegment class attributes and methods
afpText_BeginSegment_SEGNAME: Property = Property(name="SEGNAME", type=StringType)
afpText_BeginSegment.attributes={afpText_BeginSegment_SEGNAME}

# afpText_EndSegment class attributes and methods

# afpText_BeginTile class attributes and methods

# afpText_EndTile class attributes and methods

# afpText_BeginTransparencyMask class attributes and methods

# afpText_EndTransparencyMask class attributes and methods

# afpText_IDEStructure class attributes and methods
afpText_IDEStructure_FLAGS: Property = Property(name="FLAGS", type=StringType)
afpText_IDEStructure_FORMAT: Property = Property(name="FORMAT", type=StringType)
afpText_IDEStructure_SIZE1: Property = Property(name="SIZE1", type=StringType)
afpText_IDEStructure_SIZE2: Property = Property(name="SIZE2", type=StringType)
afpText_IDEStructure_SIZE3: Property = Property(name="SIZE3", type=StringType)
afpText_IDEStructure_SIZE4: Property = Property(name="SIZE4", type=StringType)
afpText_IDEStructure.attributes={afpText_IDEStructure_SIZE3, afpText_IDEStructure_SIZE2, afpText_IDEStructure_FLAGS, afpText_IDEStructure_SIZE1, afpText_IDEStructure_SIZE4, afpText_IDEStructure_FORMAT}

# afpText_ExternalAlgorithm class attributes and methods
afpText_ExternalAlgorithm_ALGTYPE: Property = Property(name="ALGTYPE", type=StringType)
afpText_ExternalAlgorithm.attributes={afpText_ExternalAlgorithm_ALGTYPE}

# afpText_TilePosition class attributes and methods
afpText_TilePosition_XOFFSET: Property = Property(name="XOFFSET", type=StringType)
afpText_TilePosition_YOFFSET: Property = Property(name="YOFFSET", type=StringType)
afpText_TilePosition.attributes={afpText_TilePosition_XOFFSET, afpText_TilePosition_YOFFSET}

# afpText_IDESize class attributes and methods
afpText_IDESize_IDESZ: Property = Property(name="IDESZ", type=StringType)
afpText_IDESize.attributes={afpText_IDESize_IDESZ}

# afpText_ImageLUTID class attributes and methods
afpText_ImageLUTID_LUTID: Property = Property(name="LUTID", type=StringType)
afpText_ImageLUTID.attributes={afpText_ImageLUTID_LUTID}

# afpText_BandImage class attributes and methods
afpText_BandImage_BCOUNT: Property = Property(name="BCOUNT", type=StringType)
afpText_BandImage.attributes={afpText_BandImage_BCOUNT}

# afpText_SetBiLevelImageColor class attributes and methods
afpText_SetBiLevelImageColor_AREA: Property = Property(name="AREA", type=StringType)
afpText_SetBiLevelImageColor_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_SetBiLevelImageColor_NAMECOLR: Property = Property(name="NAMECOLR", type=StringType)
afpText_SetBiLevelImageColor.attributes={afpText_SetBiLevelImageColor_AREA, afpText_SetBiLevelImageColor_Reserved, afpText_SetBiLevelImageColor_NAMECOLR}

# afpText_IOCAFunctionSetIdentification class attributes and methods
afpText_IOCAFunctionSetIdentification_CATEGORY: Property = Property(name="CATEGORY", type=StringType)
afpText_IOCAFunctionSetIdentification_FCNSET: Property = Property(name="FCNSET", type=StringType)
afpText_IOCAFunctionSetIdentification.attributes={afpText_IOCAFunctionSetIdentification_CATEGORY, afpText_IOCAFunctionSetIdentification_FCNSET}

# afpText_TileSize class attributes and methods
afpText_TileSize_THSIZE: Property = Property(name="THSIZE", type=StringType)
afpText_TileSize_TVSIZE: Property = Property(name="TVSIZE", type=StringType)
afpText_TileSize_RELRES: Property = Property(name="RELRES", type=StringType)
afpText_TileSize.attributes={afpText_TileSize_THSIZE, afpText_TileSize_TVSIZE, afpText_TileSize_RELRES}

# afpText_TileSetColor class attributes and methods
afpText_TileSetColor_SIZE1: Property = Property(name="SIZE1", type=StringType)
afpText_TileSetColor_SIZE2: Property = Property(name="SIZE2", type=StringType)
afpText_TileSetColor_SIZE3: Property = Property(name="SIZE3", type=StringType)
afpText_TileSetColor_SIZE4: Property = Property(name="SIZE4", type=StringType)
afpText_TileSetColor_CVAL1: Property = Property(name="CVAL1", type=StringType)
afpText_TileSetColor_CVAL2: Property = Property(name="CVAL2", type=StringType)
afpText_TileSetColor_CVAL3: Property = Property(name="CVAL3", type=StringType)
afpText_TileSetColor_CVAL4: Property = Property(name="CVAL4", type=StringType)
afpText_TileSetColor_CSPACE: Property = Property(name="CSPACE", type=StringType)
afpText_TileSetColor_RESERVED: Property = Property(name="RESERVED", type=StringType)
afpText_TileSetColor.attributes={afpText_TileSetColor_CVAL3, afpText_TileSetColor_RESERVED, afpText_TileSetColor_CVAL4, afpText_TileSetColor_CVAL2, afpText_TileSetColor_SIZE3, afpText_TileSetColor_SIZE2, afpText_TileSetColor_SIZE1, afpText_TileSetColor_CSPACE, afpText_TileSetColor_SIZE4, afpText_TileSetColor_CVAL1}

# afpText_ImageSubsampling class attributes and methods

# afpText_SamplingRatios class attributes and methods

# afpText_TileTOC class attributes and methods
afpText_TileTOC_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_TileTOC.attributes={afpText_TileTOC_Reserved}

# afpText_ImageData class attributes and methods
afpText_ImageData_DATA: Property = Property(name="DATA", type=StringType)
afpText_ImageData.attributes={afpText_ImageData_DATA}

# afpText_BandImageData class attributes and methods
afpText_BandImageData_BANDNUM: Property = Property(name="BANDNUM", type=StringType)
afpText_BandImageData_RESERVED: Property = Property(name="RESERVED", type=StringType)
afpText_BandImageData_DATA: Property = Property(name="DATA", type=StringType)
afpText_BandImageData.attributes={afpText_BandImageData_DATA, afpText_BandImageData_RESERVED, afpText_BandImageData_BANDNUM}

# afpText_IncludeTile class attributes and methods
afpText_IncludeTile_TIRID: Property = Property(name="TIRID", type=StringType)
afpText_IncludeTile.attributes={afpText_IncludeTile_TIRID}

# afpText_GBAR class attributes and methods
afpText_GBAR_FLAGS: Property = Property(name="FLAGS", type=StringType)
afpText_GBAR.attributes={afpText_GBAR_FLAGS}

# afpText_GBIMG class attributes and methods
afpText_GBIMG_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GBIMG_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GBIMG_FORMAT: Property = Property(name="FORMAT", type=StringType)
afpText_GBIMG_RES: Property = Property(name="RES", type=StringType)
afpText_GBIMG_WIDTH: Property = Property(name="WIDTH", type=StringType)
afpText_GBIMG_HEIGHT: Property = Property(name="HEIGHT", type=StringType)
afpText_GBIMG.attributes={afpText_GBIMG_RES, afpText_GBIMG_HEIGHT, afpText_GBIMG_YPOS, afpText_GBIMG_WIDTH, afpText_GBIMG_FORMAT, afpText_GBIMG_XPOS}

# afpText_GCBIMG class attributes and methods
afpText_GCBIMG_FORMAT: Property = Property(name="FORMAT", type=StringType)
afpText_GCBIMG_RES: Property = Property(name="RES", type=StringType)
afpText_GCBIMG_WIDTH: Property = Property(name="WIDTH", type=StringType)
afpText_GCBIMG_HEIGHT: Property = Property(name="HEIGHT", type=StringType)
afpText_GCBIMG.attributes={afpText_GCBIMG_WIDTH, afpText_GCBIMG_RES, afpText_GCBIMG_FORMAT, afpText_GCBIMG_HEIGHT}

# afpText_FNNRG2 class attributes and methods
afpText_FNNRG2_TSIDLen: Property = Property(name="TSIDLen", type=StringType)
afpText_FNNRG2_TSID: Property = Property(name="TSID", type=StringType)
afpText_FNNRG2.attributes={afpText_FNNRG2_TSID, afpText_FNNRG2_TSIDLen}

# afpText_BeginSegmentCommand class attributes and methods
afpText_BeginSegmentCommand_LENGTH: Property = Property(name="LENGTH", type=StringType)
afpText_BeginSegmentCommand_NAME: Property = Property(name="NAME", type=StringType)
afpText_BeginSegmentCommand_FLAG1: Property = Property(name="FLAG1", type=StringType)
afpText_BeginSegmentCommand_FLAG2: Property = Property(name="FLAG2", type=StringType)
afpText_BeginSegmentCommand_SEGL: Property = Property(name="SEGL", type=StringType)
afpText_BeginSegmentCommand_PSNAME: Property = Property(name="PSNAME", type=StringType)
afpText_BeginSegmentCommand.attributes={afpText_BeginSegmentCommand_FLAG1, afpText_BeginSegmentCommand_NAME, afpText_BeginSegmentCommand_SEGL, afpText_BeginSegmentCommand_LENGTH, afpText_BeginSegmentCommand_FLAG2, afpText_BeginSegmentCommand_PSNAME}

# afpText_EndSegmentCommand class attributes and methods

# afpText_GCBOX class attributes and methods
afpText_GCBOX_RES: Property = Property(name="RES", type=StringType)
afpText_GCBOX_XPOS1: Property = Property(name="XPOS1", type=StringType)
afpText_GCBOX_YPOS1: Property = Property(name="YPOS1", type=StringType)
afpText_GCBOX_HAXIS: Property = Property(name="HAXIS", type=StringType)
afpText_GCBOX_VAXIS: Property = Property(name="VAXIS", type=StringType)
afpText_GCBOX.attributes={afpText_GCBOX_HAXIS, afpText_GCBOX_XPOS1, afpText_GCBOX_YPOS1, afpText_GCBOX_VAXIS, afpText_GCBOX_RES}

# afpText_GCHST class attributes and methods
afpText_GCHST_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GCHST_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GCHST_CP: Property = Property(name="CP", type=StringType)
afpText_GCHST.attributes={afpText_GCHST_XPOS, afpText_GCHST_YPOS, afpText_GCHST_CP}

# afpText_GCCHST class attributes and methods
afpText_GCCHST_CP: Property = Property(name="CP", type=StringType)
afpText_GCCHST.attributes={afpText_GCCHST_CP}

# afpText_GCOMT class attributes and methods
afpText_GCOMT_DATA: Property = Property(name="DATA", type=StringType)
afpText_GCOMT.attributes={afpText_GCOMT_DATA}

# afpText_GBOX class attributes and methods
afpText_GBOX_RES: Property = Property(name="RES", type=StringType)
afpText_GBOX_XPOS0: Property = Property(name="XPOS0", type=StringType)
afpText_GBOX_YPOS0: Property = Property(name="YPOS0", type=StringType)
afpText_GBOX_XPOS1: Property = Property(name="XPOS1", type=StringType)
afpText_GBOX_YPOS1: Property = Property(name="YPOS1", type=StringType)
afpText_GBOX_HAXIS: Property = Property(name="HAXIS", type=StringType)
afpText_GBOX_VAXIS: Property = Property(name="VAXIS", type=StringType)
afpText_GBOX.attributes={afpText_GBOX_RES, afpText_GBOX_XPOS1, afpText_GBOX_YPOS0, afpText_GBOX_VAXIS, afpText_GBOX_YPOS1, afpText_GBOX_HAXIS, afpText_GBOX_XPOS0}

# afpText_GCFLT class attributes and methods

# afpText_GFARC class attributes and methods
afpText_GFARC_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GFARC_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GFARC_MH: Property = Property(name="MH", type=StringType)
afpText_GFARC_MFR: Property = Property(name="MFR", type=StringType)
afpText_GFARC.attributes={afpText_GFARC_XPOS, afpText_GFARC_MFR, afpText_GFARC_YPOS, afpText_GFARC_MH}

# afpText_GCFARC class attributes and methods
afpText_GCFARC_MH: Property = Property(name="MH", type=StringType)
afpText_GCFARC_MFR: Property = Property(name="MFR", type=StringType)
afpText_GCFARC.attributes={afpText_GCFARC_MFR, afpText_GCFARC_MH}

# afpText_GEAR class attributes and methods
afpText_GEAR_DATA: Property = Property(name="DATA", type=StringType)
afpText_GEAR.attributes={afpText_GEAR_DATA}

# afpText_GEIMG class attributes and methods
afpText_GEIMG_DATA: Property = Property(name="DATA", type=StringType)
afpText_GEIMG.attributes={afpText_GEIMG_DATA}

# afpText_GEPROL class attributes and methods
afpText_GEPROL_RES: Property = Property(name="RES", type=StringType)
afpText_GEPROL.attributes={afpText_GEPROL_RES}

# afpText_GFLT class attributes and methods

# afpText_GCLINE class attributes and methods

# afpText_GMRK class attributes and methods

# afpText_GCMRK class attributes and methods

# afpText_GNOP1 class attributes and methods

# afpText_GPARC class attributes and methods
afpText_GPARC_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GPARC_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GPARC_XCENT: Property = Property(name="XCENT", type=StringType)
afpText_GPARC_YCENT: Property = Property(name="YCENT", type=StringType)
afpText_GPARC_MH: Property = Property(name="MH", type=StringType)
afpText_GPARC_MFR: Property = Property(name="MFR", type=StringType)
afpText_GPARC_START: Property = Property(name="START", type=StringType)
afpText_GPARC_SWEEP: Property = Property(name="SWEEP", type=StringType)
afpText_GPARC.attributes={afpText_GPARC_MFR, afpText_GPARC_YCENT, afpText_GPARC_SWEEP, afpText_GPARC_START, afpText_GPARC_XCENT, afpText_GPARC_XPOS, afpText_GPARC_YPOS, afpText_GPARC_MH}

# afpText_GIMD class attributes and methods
afpText_GIMD_DATA: Property = Property(name="DATA", type=StringType)
afpText_GIMD.attributes={afpText_GIMD_DATA}

# afpText_GLINE class attributes and methods

# afpText_GRLINE class attributes and methods
afpText_GRLINE_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GRLINE_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GRLINE.attributes={afpText_GRLINE_YPOS, afpText_GRLINE_XPOS}

# afpText_GCRLINE class attributes and methods

# afpText_GCPARC class attributes and methods
afpText_GCPARC_XCENT: Property = Property(name="XCENT", type=StringType)
afpText_GCPARC_YCENT: Property = Property(name="YCENT", type=StringType)
afpText_GCPARC_MH: Property = Property(name="MH", type=StringType)
afpText_GCPARC_MFR: Property = Property(name="MFR", type=StringType)
afpText_GCPARC_START: Property = Property(name="START", type=StringType)
afpText_GCPARC_SWEEP: Property = Property(name="SWEEP", type=StringType)
afpText_GCPARC.attributes={afpText_GCPARC_XCENT, afpText_GCPARC_YCENT, afpText_GCPARC_MFR, afpText_GCPARC_MH, afpText_GCPARC_SWEEP, afpText_GCPARC_START}

# afpText_GSBMX class attributes and methods
afpText_GSBMX_MODE: Property = Property(name="MODE", type=StringType)
afpText_GSBMX.attributes={afpText_GSBMX_MODE}

# afpText_GSCA class attributes and methods
afpText_GSCA_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GSCA_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GSCA.attributes={afpText_GSCA_YPOS, afpText_GSCA_XPOS}

# afpText_GSCC class attributes and methods
afpText_GSCC_CELLWI: Property = Property(name="CELLWI", type=StringType)
afpText_GSCC_CELLHI: Property = Property(name="CELLHI", type=StringType)
afpText_GSCC_CELLWFR: Property = Property(name="CELLWFR", type=StringType)
afpText_GSCC_CELLHFR: Property = Property(name="CELLHFR", type=StringType)
afpText_GSCC.attributes={afpText_GSCC_CELLWI, afpText_GSCC_CELLHI, afpText_GSCC_CELLHFR, afpText_GSCC_CELLWFR}

# afpText_GSCD class attributes and methods
afpText_GSCD_DIRECTION: Property = Property(name="DIRECTION", type=StringType)
afpText_GSCD.attributes={afpText_GSCD_DIRECTION}

# afpText_GSGCH class attributes and methods

# afpText_GSAP class attributes and methods
afpText_GSAP_S: Property = Property(name="S", type=StringType)
afpText_GSAP_P: Property = Property(name="P", type=StringType)
afpText_GSAP_Q: Property = Property(name="Q", type=StringType)
afpText_GSAP_R: Property = Property(name="R", type=StringType)
afpText_GSAP.attributes={afpText_GSAP_S, afpText_GSAP_P, afpText_GSAP_Q, afpText_GSAP_R}

# afpText_GSCOL class attributes and methods
afpText_GSCOL_COL: Property = Property(name="COL", type=StringType)
afpText_GSCOL.attributes={afpText_GSCOL_COL}

# afpText_GSCP class attributes and methods
afpText_GSCP_XPOS: Property = Property(name="XPOS", type=StringType)
afpText_GSCP_YPOS: Property = Property(name="YPOS", type=StringType)
afpText_GSCP.attributes={afpText_GSCP_YPOS, afpText_GSCP_XPOS}

# afpText_GSECOL class attributes and methods
afpText_GSECOL_COLOR: Property = Property(name="COLOR", type=StringType)
afpText_GSECOL.attributes={afpText_GSECOL_COLOR}

# afpText_GSFLW class attributes and methods
afpText_GSFLW_MH: Property = Property(name="MH", type=StringType)
afpText_GSFLW_MFR: Property = Property(name="MFR", type=StringType)
afpText_GSFLW.attributes={afpText_GSFLW_MFR, afpText_GSFLW_MH}

# afpText_GSLT class attributes and methods
afpText_GSLT_LINETYPE: Property = Property(name="LINETYPE", type=StringType)
afpText_GSLT.attributes={afpText_GSLT_LINETYPE}

# afpText_GSCR class attributes and methods
afpText_GSCR_PREC: Property = Property(name="PREC", type=StringType)
afpText_GSCR.attributes={afpText_GSCR_PREC}

# afpText_GSCS class attributes and methods
afpText_GSCS_LCID: Property = Property(name="LCID", type=StringType)
afpText_GSCS.attributes={afpText_GSCS_LCID}

# afpText_GSCH class attributes and methods
afpText_GSCH_HX: Property = Property(name="HX", type=StringType)
afpText_GSCH_HY: Property = Property(name="HY", type=StringType)
afpText_GSCH.attributes={afpText_GSCH_HY, afpText_GSCH_HX}

# afpText_GSMS class attributes and methods
afpText_GSMS_LCID: Property = Property(name="LCID", type=StringType)
afpText_GSMS.attributes={afpText_GSMS_LCID}

# afpText_GSMT class attributes and methods
afpText_GSMT_MCPT: Property = Property(name="MCPT", type=StringType)
afpText_GSMT.attributes={afpText_GSMT_MCPT}

# afpText_GSMX class attributes and methods
afpText_GSMX_MODE: Property = Property(name="MODE", type=StringType)
afpText_GSMX.attributes={afpText_GSMX_MODE}

# afpText_GSPS class attributes and methods
afpText_GSPS_LCID: Property = Property(name="LCID", type=StringType)
afpText_GSPS.attributes={afpText_GSPS_LCID}

# afpText_GSPT class attributes and methods
afpText_GSPT_PATT: Property = Property(name="PATT", type=StringType)
afpText_GSPT.attributes={afpText_GSPT_PATT}

# afpText_GSLW class attributes and methods
afpText_GSLW_MH: Property = Property(name="MH", type=StringType)
afpText_GSLW.attributes={afpText_GSLW_MH}

# afpText_GSMC class attributes and methods
afpText_GSMC_CELLWI: Property = Property(name="CELLWI", type=StringType)
afpText_GSMC_CELLHI: Property = Property(name="CELLHI", type=StringType)
afpText_GSMC.attributes={afpText_GSMC_CELLHI, afpText_GSMC_CELLWI}

# afpText_GSMP class attributes and methods
afpText_GSMP_PREC: Property = Property(name="PREC", type=StringType)
afpText_GSMP.attributes={afpText_GSMP_PREC}

# afpText_GSLE class attributes and methods
afpText_GSLE_LINEEND: Property = Property(name="LINEEND", type=StringType)
afpText_GSLE.attributes={afpText_GSLE_LINEEND}

# afpText_GSLJ class attributes and methods
afpText_GSLJ_LINEJOIN: Property = Property(name="LINEJOIN", type=StringType)
afpText_GSLJ.attributes={afpText_GSLJ_LINEJOIN}

# afpText_GCBEZ class attributes and methods

# afpText_GCCBEZ class attributes and methods

# afpText_GSPCOL class attributes and methods
afpText_GSPCOL_COLVALUE: Property = Property(name="COLVALUE", type=StringType)
afpText_GSPCOL_RES1: Property = Property(name="RES1", type=StringType)
afpText_GSPCOL_COLSPCE: Property = Property(name="COLSPCE", type=StringType)
afpText_GSPCOL_RES2: Property = Property(name="RES2", type=StringType)
afpText_GSPCOL_COLSIZE1: Property = Property(name="COLSIZE1", type=StringType)
afpText_GSPCOL_COLSIZE2: Property = Property(name="COLSIZE2", type=StringType)
afpText_GSPCOL_COLSIZE3: Property = Property(name="COLSIZE3", type=StringType)
afpText_GSPCOL_COLSIZE4: Property = Property(name="COLSIZE4", type=StringType)
afpText_GSPCOL.attributes={afpText_GSPCOL_RES1, afpText_GSPCOL_COLSIZE2, afpText_GSPCOL_COLSPCE, afpText_GSPCOL_COLSIZE1, afpText_GSPCOL_COLVALUE, afpText_GSPCOL_COLSIZE3, afpText_GSPCOL_RES2, afpText_GSPCOL_COLSIZE4}

# afpText_DrawingOrderSubset class attributes and methods

# afpText_TonerSaver class attributes and methods
afpText_TonerSaver_TSvCtrl: Property = Property(name="TSvCtrl", type=StringType)
afpText_TonerSaver.attributes={afpText_TonerSaver_TSvCtrl}

# afpText_ColorFidelity class attributes and methods
afpText_ColorFidelity_StpCoEx: Property = Property(name="StpCoEx", type=StringType)
afpText_ColorFidelity_RepCoEx: Property = Property(name="RepCoEx", type=StringType)
afpText_ColorFidelity_ColSub: Property = Property(name="ColSub", type=StringType)
afpText_ColorFidelity.attributes={afpText_ColorFidelity_StpCoEx, afpText_ColorFidelity_RepCoEx, afpText_ColorFidelity_ColSub}

# afpText_FontFidelity class attributes and methods
afpText_FontFidelity_StpFntEx: Property = Property(name="StpFntEx", type=StringType)
afpText_FontFidelity.attributes={afpText_FontFidelity_StpFntEx}

# afpText_WindowSpecification class attributes and methods
afpText_WindowSpecification_IMGXYRES: Property = Property(name="IMGXYRES", type=StringType)
afpText_WindowSpecification_XLWIND: Property = Property(name="XLWIND", type=StringType)
afpText_WindowSpecification_XRWIND: Property = Property(name="XRWIND", type=StringType)
afpText_WindowSpecification_YBWIND: Property = Property(name="YBWIND", type=StringType)
afpText_WindowSpecification_YTWIND: Property = Property(name="YTWIND", type=StringType)
afpText_WindowSpecification_FLAGS: Property = Property(name="FLAGS", type=StringType)
afpText_WindowSpecification_RES3: Property = Property(name="RES3", type=StringType)
afpText_WindowSpecification_CFORMAT: Property = Property(name="CFORMAT", type=StringType)
afpText_WindowSpecification_UBASE: Property = Property(name="UBASE", type=StringType)
afpText_WindowSpecification_XRESOL: Property = Property(name="XRESOL", type=StringType)
afpText_WindowSpecification_YRESOL: Property = Property(name="YRESOL", type=StringType)
afpText_WindowSpecification.attributes={afpText_WindowSpecification_YRESOL, afpText_WindowSpecification_YBWIND, afpText_WindowSpecification_XLWIND, afpText_WindowSpecification_FLAGS, afpText_WindowSpecification_UBASE, afpText_WindowSpecification_YTWIND, afpText_WindowSpecification_IMGXYRES, afpText_WindowSpecification_XRWIND, afpText_WindowSpecification_RES3, afpText_WindowSpecification_XRESOL, afpText_WindowSpecification_CFORMAT}

# afpText_FinishingFidelity class attributes and methods
afpText_FinishingFidelity_StpFinEx: Property = Property(name="StpFinEx", type=StringType)
afpText_FinishingFidelity_RepFinEx: Property = Property(name="RepFinEx", type=StringType)
afpText_FinishingFidelity.attributes={afpText_FinishingFidelity_RepFinEx, afpText_FinishingFidelity_StpFinEx}

# afpText_CMRFidelity class attributes and methods
afpText_CMRFidelity_StpCMREx: Property = Property(name="StpCMREx", type=StringType)
afpText_CMRFidelity_RepCMREx: Property = Property(name="RepCMREx", type=StringType)
afpText_CMRFidelity.attributes={afpText_CMRFidelity_StpCMREx, afpText_CMRFidelity_RepCMREx}

# afpText_ObjectByteExtent class attributes and methods
afpText_ObjectByteExtent_ByteExt: Property = Property(name="ByteExt", type=StringType)
afpText_ObjectByteExtent_ByteExtHi: Property = Property(name="ByteExtHi", type=StringType)
afpText_ObjectByteExtent.attributes={afpText_ObjectByteExtent_ByteExtHi, afpText_ObjectByteExtent_ByteExt}

# afpText_ObjectByteOffset class attributes and methods
afpText_ObjectByteOffset_DirByOff: Property = Property(name="DirByOff", type=StringType)
afpText_ObjectByteOffset_DirByHi: Property = Property(name="DirByHi", type=StringType)
afpText_ObjectByteOffset.attributes={afpText_ObjectByteOffset_DirByHi, afpText_ObjectByteOffset_DirByOff}

# afpText_ObjectStructuredFieldExtent class attributes and methods
afpText_ObjectStructuredFieldExtent_SFExt: Property = Property(name="SFExt", type=StringType)
afpText_ObjectStructuredFieldExtent_SFExtHi: Property = Property(name="SFExtHi", type=StringType)
afpText_ObjectStructuredFieldExtent.attributes={afpText_ObjectStructuredFieldExtent_SFExt, afpText_ObjectStructuredFieldExtent_SFExtHi}

# afpText_TextFidelity class attributes and methods
afpText_TextFidelity_StpTxtEx: Property = Property(name="StpTxtEx", type=StringType)
afpText_TextFidelity_RepTxtEx: Property = Property(name="RepTxtEx", type=StringType)
afpText_TextFidelity.attributes={afpText_TextFidelity_StpTxtEx, afpText_TextFidelity_RepTxtEx}

# afpText_MediaFidelity class attributes and methods
afpText_MediaFidelity_StpMedEx: Property = Property(name="StpMedEx", type=StringType)
afpText_MediaFidelity_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_MediaFidelity.attributes={afpText_MediaFidelity_Reserved, afpText_MediaFidelity_StpMedEx}

# afpText_ObjectOriginIdentifier class attributes and methods
afpText_ObjectOriginIdentifier_System: Property = Property(name="System", type=StringType)
afpText_ObjectOriginIdentifier_SysID: Property = Property(name="SysID", type=StringType)
afpText_ObjectOriginIdentifier_MedID: Property = Property(name="MedID", type=StringType)
afpText_ObjectOriginIdentifier_DSID: Property = Property(name="DSID", type=StringType)
afpText_ObjectOriginIdentifier.attributes={afpText_ObjectOriginIdentifier_System, afpText_ObjectOriginIdentifier_SysID, afpText_ObjectOriginIdentifier_DSID, afpText_ObjectOriginIdentifier_MedID}

# afpText_LineDataObjectPositionMigration class attributes and methods
afpText_LineDataObjectPositionMigration_TempOrient: Property = Property(name="TempOrient", type=StringType)
afpText_LineDataObjectPositionMigration.attributes={afpText_LineDataObjectPositionMigration_TempOrient}

# afpText_ColorManagementResourceDescriptor class attributes and methods
afpText_ColorManagementResourceDescriptor_ProcMode: Property = Property(name="ProcMode", type=StringType)
afpText_ColorManagementResourceDescriptor_CMRScpe: Property = Property(name="CMRScpe", type=StringType)
afpText_ColorManagementResourceDescriptor.attributes={afpText_ColorManagementResourceDescriptor_ProcMode, afpText_ColorManagementResourceDescriptor_CMRScpe}

# afpText_ObjectStructuredFieldOffset class attributes and methods
afpText_ObjectStructuredFieldOffset_SFOff: Property = Property(name="SFOff", type=StringType)
afpText_ObjectStructuredFieldOffset_SFOffHi: Property = Property(name="SFOffHi", type=StringType)
afpText_ObjectStructuredFieldOffset.attributes={afpText_ObjectStructuredFieldOffset_SFOffHi, afpText_ObjectStructuredFieldOffset_SFOff}

# afpText_ObjectCount class attributes and methods
afpText_ObjectCount_SubObj: Property = Property(name="SubObj", type=StringType)
afpText_ObjectCount_SObjNum: Property = Property(name="SObjNum", type=StringType)
afpText_ObjectCount_SobjNmHi: Property = Property(name="SobjNmHi", type=StringType)
afpText_ObjectCount.attributes={afpText_ObjectCount_SobjNmHi, afpText_ObjectCount_SObjNum, afpText_ObjectCount_SubObj}

# afpText_ExtendedResourceLocalIdentifier class attributes and methods
afpText_ExtendedResourceLocalIdentifier_ResType: Property = Property(name="ResType", type=StringType)
afpText_ExtendedResourceLocalIdentifier_ResLID: Property = Property(name="ResLID", type=StringType)
afpText_ExtendedResourceLocalIdentifier.attributes={afpText_ExtendedResourceLocalIdentifier_ResType, afpText_ExtendedResourceLocalIdentifier_ResLID}

# afpText_MetricAdjustment class attributes and methods
afpText_MetricAdjustment_UnitBase: Property = Property(name="UnitBase", type=StringType)
afpText_MetricAdjustment_XUPUB: Property = Property(name="XUPUB", type=StringType)
afpText_MetricAdjustment_YUPUB: Property = Property(name="YUPUB", type=StringType)
afpText_MetricAdjustment_HUniformIncrement: Property = Property(name="HUniformIncrement", type=StringType)
afpText_MetricAdjustment_VUniformIncrement: Property = Property(name="VUniformIncrement", type=StringType)
afpText_MetricAdjustment_HBaselineIncrement: Property = Property(name="HBaselineIncrement", type=StringType)
afpText_MetricAdjustment_VBaselineIncrement: Property = Property(name="VBaselineIncrement", type=StringType)
afpText_MetricAdjustment.attributes={afpText_MetricAdjustment_HBaselineIncrement, afpText_MetricAdjustment_HUniformIncrement, afpText_MetricAdjustment_XUPUB, afpText_MetricAdjustment_VUniformIncrement, afpText_MetricAdjustment_VBaselineIncrement, afpText_MetricAdjustment_UnitBase, afpText_MetricAdjustment_YUPUB}

# afpText_ExtensionFont class attributes and methods
afpText_ExtensionFont_GCSGID: Property = Property(name="GCSGID", type=StringType)
afpText_ExtensionFont.attributes={afpText_ExtensionFont_GCSGID}

# afpText_ImageResolution class attributes and methods
afpText_ImageResolution_XBase: Property = Property(name="XBase", type=StringType)
afpText_ImageResolution_YBase: Property = Property(name="YBase", type=StringType)
afpText_ImageResolution_XResol: Property = Property(name="XResol", type=StringType)
afpText_ImageResolution_YResol: Property = Property(name="YResol", type=StringType)
afpText_ImageResolution.attributes={afpText_ImageResolution_YBase, afpText_ImageResolution_XBase, afpText_ImageResolution_XResol, afpText_ImageResolution_YResol}

# afpText_ObjectContainerPresentationSpaceSize class attributes and methods
afpText_ObjectContainerPresentationSpaceSize_PDFSize: Property = Property(name="PDFSize", type=StringType)
afpText_ObjectContainerPresentationSpaceSize.attributes={afpText_ObjectContainerPresentationSpaceSize_PDFSize}

# afpText_LocaleSelector class attributes and methods
afpText_LocaleSelector_LocFlgs: Property = Property(name="LocFlgs", type=StringType)
afpText_LocaleSelector_LangCode: Property = Property(name="LangCode", type=StringType)
afpText_LocaleSelector_ScrptCde: Property = Property(name="ScrptCde", type=StringType)
afpText_LocaleSelector_RegCde: Property = Property(name="RegCde", type=StringType)
afpText_LocaleSelector_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_LocaleSelector_VarCde: Property = Property(name="VarCde", type=StringType)
afpText_LocaleSelector.attributes={afpText_LocaleSelector_LocFlgs, afpText_LocaleSelector_LangCode, afpText_LocaleSelector_Reserved, afpText_LocaleSelector_RegCde, afpText_LocaleSelector_ScrptCde, afpText_LocaleSelector_VarCde}

# afpText_FinishingOperation class attributes and methods
afpText_FinishingOperation_FOpType: Property = Property(name="FOpType", type=StringType)
afpText_FinishingOperation_RefEdge: Property = Property(name="RefEdge", type=StringType)
afpText_FinishingOperation_FOpCnt: Property = Property(name="FOpCnt", type=StringType)
afpText_FinishingOperation_AxOffst: Property = Property(name="AxOffst", type=StringType)
afpText_FinishingOperation_OpPos: Property = Property(name="OpPos", type=StringType)
afpText_FinishingOperation.attributes={afpText_FinishingOperation_FOpType, afpText_FinishingOperation_RefEdge, afpText_FinishingOperation_FOpCnt, afpText_FinishingOperation_AxOffst, afpText_FinishingOperation_OpPos}

# afpText_RenderingIntent class attributes and methods
afpText_RenderingIntent_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_RenderingIntent_IOCARI: Property = Property(name="IOCARI", type=StringType)
afpText_RenderingIntent_OCRI: Property = Property(name="OCRI", type=StringType)
afpText_RenderingIntent_PTOCRI: Property = Property(name="PTOCRI", type=StringType)
afpText_RenderingIntent_GOCARI: Property = Property(name="GOCARI", type=StringType)
afpText_RenderingIntent_Reserved2: Property = Property(name="Reserved2", type=StringType)
afpText_RenderingIntent.attributes={afpText_RenderingIntent_Reserved2, afpText_RenderingIntent_Reserved, afpText_RenderingIntent_GOCARI, afpText_RenderingIntent_PTOCRI, afpText_RenderingIntent_IOCARI, afpText_RenderingIntent_OCRI}

# afpText_FontCodedGraphicCharacterSetGlobalIdentifier class attributes and methods
afpText_FontCodedGraphicCharacterSetGlobalIdentifier_GCSGID: Property = Property(name="GCSGID", type=StringType)
afpText_FontCodedGraphicCharacterSetGlobalIdentifier_CPGID: Property = Property(name="CPGID", type=StringType)
afpText_FontCodedGraphicCharacterSetGlobalIdentifier.attributes={afpText_FontCodedGraphicCharacterSetGlobalIdentifier_GCSGID, afpText_FontCodedGraphicCharacterSetGlobalIdentifier_CPGID}

# afpText_PageOverlayConditionalProcessing class attributes and methods
afpText_PageOverlayConditionalProcessing_PgOvType: Property = Property(name="PgOvType", type=StringType)
afpText_PageOverlayConditionalProcessing_Level: Property = Property(name="Level", type=StringType)
afpText_PageOverlayConditionalProcessing.attributes={afpText_PageOverlayConditionalProcessing_Level, afpText_PageOverlayConditionalProcessing_PgOvType}

# afpText_ResourceUsageAttribute class attributes and methods
afpText_ResourceUsageAttribute_Frequency: Property = Property(name="Frequency", type=StringType)
afpText_ResourceUsageAttribute.attributes={afpText_ResourceUsageAttribute_Frequency}

# afpText_UP3iFinishingOperation class attributes and methods
afpText_UP3iFinishingOperation_Seqnum: Property = Property(name="Seqnum", type=StringType)
afpText_UP3iFinishingOperation_UP3iDat: Property = Property(name="UP3iDat", type=StringType)
afpText_UP3iFinishingOperation.attributes={afpText_UP3iFinishingOperation_UP3iDat, afpText_UP3iFinishingOperation_Seqnum}

# afpText_DeviceAppearance class attributes and methods
afpText_DeviceAppearance_DevApp: Property = Property(name="DevApp", type=StringType)
afpText_DeviceAppearance_Reserved: Property = Property(name="Reserved", type=StringType)
afpText_DeviceAppearance.attributes={afpText_DeviceAppearance_Reserved, afpText_DeviceAppearance_DevApp}

# afpText_ResourceObjectInclude class attributes and methods
afpText_ResourceObjectInclude_ObjType: Property = Property(name="ObjType", type=StringType)
afpText_ResourceObjectInclude_ObjName: Property = Property(name="ObjName", type=StringType)
afpText_ResourceObjectInclude_XobjOset: Property = Property(name="XobjOset", type=StringType)
afpText_ResourceObjectInclude_YobjOset: Property = Property(name="YobjOset", type=StringType)
afpText_ResourceObjectInclude_ObOrent: Property = Property(name="ObOrent", type=StringType)
afpText_ResourceObjectInclude.attributes={afpText_ResourceObjectInclude_XobjOset, afpText_ResourceObjectInclude_ObOrent, afpText_ResourceObjectInclude_ObjType, afpText_ResourceObjectInclude_ObjName, afpText_ResourceObjectInclude_YobjOset}

# Relationships
structuredFields0: BinaryAssociation = BinaryAssociation(
    name="structuredFields0",
    ends={
        Property(name="afpText_structuredField", type=afpText_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_Model", type=afpText_structuredField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets1: BinaryAssociation = BinaryAssociation(
    name="triplets1",
    ends={
        Property(name="afpText_triplet", type=afpText_BAG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BAG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets8: BinaryAssociation = BinaryAssociation(
    name="triplets8",
    ends={
        Property(name="afpText_triplet9", type=afpText_BDD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BDD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets2: BinaryAssociation = BinaryAssociation(
    name="triplets2",
    ends={
        Property(name="afpText_triplet3", type=afpText_BBC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BBC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets4: BinaryAssociation = BinaryAssociation(
    name="triplets4",
    ends={
        Property(name="afpText_triplet5", type=afpText_BCA, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BCA", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets6: BinaryAssociation = BinaryAssociation(
    name="triplets6",
    ends={
        Property(name="afpText_triplet7", type=afpText_BCP, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BCP", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets18: BinaryAssociation = BinaryAssociation(
    name="triplets18",
    ends={
        Property(name="afpText_triplet19", type=afpText_BFM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BFM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets20: BinaryAssociation = BinaryAssociation(
    name="triplets20",
    ends={
        Property(name="afpText_triplet21", type=afpText_BFN, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BFN", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets10: BinaryAssociation = BinaryAssociation(
    name="triplets10",
    ends={
        Property(name="afpText_triplet11", type=afpText_BDG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BDG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets12: BinaryAssociation = BinaryAssociation(
    name="triplets12",
    ends={
        Property(name="afpText_triplet13", type=afpText_BDI, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BDI", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets14: BinaryAssociation = BinaryAssociation(
    name="triplets14",
    ends={
        Property(name="afpText_triplet15", type=afpText_BDM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BDM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets32: BinaryAssociation = BinaryAssociation(
    name="triplets32",
    ends={
        Property(name="afpText_BOC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="afpText_triplet33", type=afpText_BOC, multiplicity=Multiplicity(1, 1))
    }
)
triplets16: BinaryAssociation = BinaryAssociation(
    name="triplets16",
    ends={
        Property(name="afpText_triplet17", type=afpText_BDT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BDT", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets34: BinaryAssociation = BinaryAssociation(
    name="triplets34",
    ends={
        Property(name="afpText_triplet35", type=afpText_BOG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BOG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets36: BinaryAssociation = BinaryAssociation(
    name="triplets36",
    ends={
        Property(name="afpText_triplet37", type=afpText_BPF, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BPF", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets38: BinaryAssociation = BinaryAssociation(
    name="triplets38",
    ends={
        Property(name="afpText_triplet39", type=afpText_BPG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BPG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets22: BinaryAssociation = BinaryAssociation(
    name="triplets22",
    ends={
        Property(name="afpText_triplet23", type=afpText_BGR, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BGR", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets24: BinaryAssociation = BinaryAssociation(
    name="triplets24",
    ends={
        Property(name="afpText_triplet25", type=afpText_BIM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BIM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets26: BinaryAssociation = BinaryAssociation(
    name="triplets26",
    ends={
        Property(name="afpText_triplet27", type=afpText_BMM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BMM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets28: BinaryAssociation = BinaryAssociation(
    name="triplets28",
    ends={
        Property(name="afpText_triplet29", type=afpText_BMO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BMO", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets30: BinaryAssociation = BinaryAssociation(
    name="triplets30",
    ends={
        Property(name="afpText_triplet31", type=afpText_BNG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BNG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets48: BinaryAssociation = BinaryAssociation(
    name="triplets48",
    ends={
        Property(name="afpText_triplet49", type=afpText_BSG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BSG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets50: BinaryAssociation = BinaryAssociation(
    name="triplets50",
    ends={
        Property(name="afpText_triplet51", type=afpText_CDD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_CDD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets40: BinaryAssociation = BinaryAssociation(
    name="triplets40",
    ends={
        Property(name="afpText_triplet41", type=afpText_BPS, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BPS", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets42: BinaryAssociation = BinaryAssociation(
    name="triplets42",
    ends={
        Property(name="afpText_triplet43", type=afpText_BPT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BPT", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets44: BinaryAssociation = BinaryAssociation(
    name="triplets44",
    ends={
        Property(name="afpText_triplet45", type=afpText_BRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BRG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets46: BinaryAssociation = BinaryAssociation(
    name="triplets46",
    ends={
        Property(name="afpText_triplet47", type=afpText_BRS, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BRS", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets56: BinaryAssociation = BinaryAssociation(
    name="triplets56",
    ends={
        Property(name="afpText_triplet57", type=afpText_EBC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EBC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets58: BinaryAssociation = BinaryAssociation(
    name="triplets58",
    ends={
        Property(name="afpText_triplet59", type=afpText_ECA, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_ECA", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets52: BinaryAssociation = BinaryAssociation(
    name="triplets52",
    ends={
        Property(name="afpText_triplet53", type=afpText_CFC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_CFC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg54: BinaryAssociation = BinaryAssociation(
    name="rg54",
    ends={
        Property(name="afpText_CFIRG", type=afpText_CFI, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_CFI", type=afpText_CFIRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg55: BinaryAssociation = BinaryAssociation(
    name="rg55",
    ends={
        Property(name="afpText_CPIRG", type=afpText_CPI, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_CPI", type=afpText_CPIRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets64: BinaryAssociation = BinaryAssociation(
    name="triplets64",
    ends={
        Property(name="afpText_triplet65", type=afpText_EGR, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EGR", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets60: BinaryAssociation = BinaryAssociation(
    name="triplets60",
    ends={
        Property(name="afpText_triplet61", type=afpText_EDI, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EDI", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets62: BinaryAssociation = BinaryAssociation(
    name="triplets62",
    ends={
        Property(name="afpText_triplet63", type=afpText_EDT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EDT", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets74: BinaryAssociation = BinaryAssociation(
    name="triplets74",
    ends={
        Property(name="afpText_triplet75", type=afpText_EPF, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EPF", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets76: BinaryAssociation = BinaryAssociation(
    name="triplets76",
    ends={
        Property(name="afpText_triplet77", type=afpText_EPG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EPG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets66: BinaryAssociation = BinaryAssociation(
    name="triplets66",
    ends={
        Property(name="afpText_triplet67", type=afpText_EIM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EIM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets68: BinaryAssociation = BinaryAssociation(
    name="triplets68",
    ends={
        Property(name="afpText_triplet69", type=afpText_EMO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EMO", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets70: BinaryAssociation = BinaryAssociation(
    name="triplets70",
    ends={
        Property(name="afpText_triplet71", type=afpText_ENG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_ENG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets72: BinaryAssociation = BinaryAssociation(
    name="triplets72",
    ends={
        Property(name="afpText_triplet73", type=afpText_EOC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EOC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets78: BinaryAssociation = BinaryAssociation(
    name="triplets78",
    ends={
        Property(name="afpText_triplet79", type=afpText_EPT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_EPT", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets80: BinaryAssociation = BinaryAssociation(
    name="triplets80",
    ends={
        Property(name="afpText_triplet81", type=afpText_ERG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_ERG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg86: BinaryAssociation = BinaryAssociation(
    name="rg86",
    ends={
        Property(name="afpText_FNIRG", type=afpText_FNI, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FNI", type=afpText_FNIRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg87: BinaryAssociation = BinaryAssociation(
    name="rg87",
    ends={
        Property(name="afpText_FNMRG", type=afpText_FNM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FNM", type=afpText_FNMRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets82: BinaryAssociation = BinaryAssociation(
    name="triplets82",
    ends={
        Property(name="afpText_triplet83", type=afpText_FNC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FNC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets84: BinaryAssociation = BinaryAssociation(
    name="triplets84",
    ends={
        Property(name="afpText_triplet85", type=afpText_FND, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FND", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets92: BinaryAssociation = BinaryAssociation(
    name="triplets92",
    ends={
        Property(name="afpText_triplet93", type=afpText_IDD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IDD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets94: BinaryAssociation = BinaryAssociation(
    name="triplets94",
    ends={
        Property(name="afpText_triplet95", type=afpText_IEL, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IEL", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg88: BinaryAssociation = BinaryAssociation(
    name="rg88",
    ends={
        Property(name="afpText_FNORG", type=afpText_FNO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FNO", type=afpText_FNORG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg89: BinaryAssociation = BinaryAssociation(
    name="rg89",
    ends={
        Property(name="afpText_FNPRG", type=afpText_FNP, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_FNP", type=afpText_FNPRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets90: BinaryAssociation = BinaryAssociation(
    name="triplets90",
    ends={
        Property(name="afpText_triplet91", type=afpText_GDD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GDD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets98: BinaryAssociation = BinaryAssociation(
    name="triplets98",
    ends={
        Property(name="afpText_triplet99", type=afpText_IOB, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IOB", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets96: BinaryAssociation = BinaryAssociation(
    name="triplets96",
    ends={
        Property(name="afpText_triplet97", type=afpText_IMM, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IMM", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg106: BinaryAssociation = BinaryAssociation(
    name="rg106",
    ends={
        Property(name="afpText_LLERG", type=afpText_LLE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_LLE", type=afpText_LLERG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets100: BinaryAssociation = BinaryAssociation(
    name="triplets100",
    ends={
        Property(name="afpText_triplet101", type=afpText_IPG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IPG", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets102: BinaryAssociation = BinaryAssociation(
    name="triplets102",
    ends={
        Property(name="afpText_triplet103", type=afpText_IPO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IPO", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets104: BinaryAssociation = BinaryAssociation(
    name="triplets104",
    ends={
        Property(name="afpText_triplet105", type=afpText_IPS, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_IPS", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg112: BinaryAssociation = BinaryAssociation(
    name="rg112",
    ends={
        Property(name="afpText_MCDRG", type=afpText_MCD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCD", type=afpText_MCDRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg113: BinaryAssociation = BinaryAssociation(
    name="rg113",
    ends={
        Property(name="afpText_MCFRG", type=afpText_MCF, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCF", type=afpText_MCFRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg114: BinaryAssociation = BinaryAssociation(
    name="rg114",
    ends={
        Property(name="afpText_MCF1RG", type=afpText_MCF1, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCF1", type=afpText_MCF1RG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets107: BinaryAssociation = BinaryAssociation(
    name="triplets107",
    ends={
        Property(name="afpText_triplet108", type=afpText_LND, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_LND", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg109: BinaryAssociation = BinaryAssociation(
    name="rg109",
    ends={
        Property(name="afpText_MBCRG", type=afpText_MBC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MBC", type=afpText_MBCRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg110: BinaryAssociation = BinaryAssociation(
    name="rg110",
    ends={
        Property(name="afpText_MCARG", type=afpText_MCA, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCA", type=afpText_MCARG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg111: BinaryAssociation = BinaryAssociation(
    name="rg111",
    ends={
        Property(name="afpText_MCCRG", type=afpText_MCC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCC", type=afpText_MCCRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg121: BinaryAssociation = BinaryAssociation(
    name="rg121",
    ends={
        Property(name="afpText_MIO", type=afpText_MIORG, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="afpText_MIORG", type=afpText_MIO, multiplicity=Multiplicity(1, 1))
    }
)
rg122: BinaryAssociation = BinaryAssociation(
    name="rg122",
    ends={
        Property(name="afpText_MMCRG", type=afpText_MMC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMC", type=afpText_MMCRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg123: BinaryAssociation = BinaryAssociation(
    name="rg123",
    ends={
        Property(name="afpText_MMDRG", type=afpText_MMD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMD", type=afpText_MMDRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets115: BinaryAssociation = BinaryAssociation(
    name="triplets115",
    ends={
        Property(name="afpText_triplet116", type=afpText_MDD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MDD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg117: BinaryAssociation = BinaryAssociation(
    name="rg117",
    ends={
        Property(name="afpText_MDRRG", type=afpText_MDR, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MDR", type=afpText_MDRRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets118: BinaryAssociation = BinaryAssociation(
    name="triplets118",
    ends={
        Property(name="afpText_triplet119", type=afpText_MFC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MFC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg120: BinaryAssociation = BinaryAssociation(
    name="rg120",
    ends={
        Property(name="afpText_MGORG", type=afpText_MGO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MGO", type=afpText_MGORG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg129: BinaryAssociation = BinaryAssociation(
    name="rg129",
    ends={
        Property(name="afpText_MSURG", type=afpText_MSU, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MSU", type=afpText_MSURG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets130: BinaryAssociation = BinaryAssociation(
    name="triplets130",
    ends={
        Property(name="afpText_triplet131", type=afpText_OBD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_OBD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg124: BinaryAssociation = BinaryAssociation(
    name="rg124",
    ends={
        Property(name="afpText_MMORG", type=afpText_MMO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMO", type=afpText_MMORG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg125: BinaryAssociation = BinaryAssociation(
    name="rg125",
    ends={
        Property(name="afpText_MMTRG", type=afpText_MMT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMT", type=afpText_MMTRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg126: BinaryAssociation = BinaryAssociation(
    name="rg126",
    ends={
        Property(name="afpText_MPGRG", type=afpText_MPG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MPG", type=afpText_MPGRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg127: BinaryAssociation = BinaryAssociation(
    name="rg127",
    ends={
        Property(name="afpText_MPORG", type=afpText_MPO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MPO", type=afpText_MPORG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg128: BinaryAssociation = BinaryAssociation(
    name="rg128",
    ends={
        Property(name="afpText_MPSRG", type=afpText_MPS, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MPS", type=afpText_MPSRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets136: BinaryAssociation = BinaryAssociation(
    name="triplets136",
    ends={
        Property(name="afpText_triplet137", type=afpText_PGD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PGD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg138: BinaryAssociation = BinaryAssociation(
    name="rg138",
    ends={
        Property(name="afpText_PGPRG", type=afpText_PGP, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PGP", type=afpText_PGPRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets132: BinaryAssociation = BinaryAssociation(
    name="triplets132",
    ends={
        Property(name="afpText_triplet133", type=afpText_PEC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PEC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets134: BinaryAssociation = BinaryAssociation(
    name="triplets134",
    ends={
        Property(name="afpText_triplet135", type=afpText_PFC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PFC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets142: BinaryAssociation = BinaryAssociation(
    name="triplets142",
    ends={
        Property(name="afpText_triplet143", type=afpText_PTD, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PTD", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets139: BinaryAssociation = BinaryAssociation(
    name="triplets139",
    ends={
        Property(name="afpText_triplet140", type=afpText_PMC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PMC", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg141: BinaryAssociation = BinaryAssociation(
    name="rg141",
    ends={
        Property(name="afpText_PPORG", type=afpText_PPO, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PPO", type=afpText_PPORG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets146: BinaryAssociation = BinaryAssociation(
    name="triplets146",
    ends={
        Property(name="afpText_triplet147", type=afpText_TLE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_TLE", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets144: BinaryAssociation = BinaryAssociation(
    name="triplets144",
    ends={
        Property(name="afpText_triplet145", type=afpText_PTX, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PTX", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets148: BinaryAssociation = BinaryAssociation(
    name="triplets148",
    ends={
        Property(name="afpText_triplet150", type=afpText_LLERG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_LLERG149", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets160: BinaryAssociation = BinaryAssociation(
    name="triplets160",
    ends={
        Property(name="afpText_triplet162", type=afpText_MCDRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCDRG161", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets163: BinaryAssociation = BinaryAssociation(
    name="triplets163",
    ends={
        Property(name="afpText_triplet165", type=afpText_MDRRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MDRRG164", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets151: BinaryAssociation = BinaryAssociation(
    name="triplets151",
    ends={
        Property(name="afpText_triplet153", type=afpText_MCFRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCFRG152", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets154: BinaryAssociation = BinaryAssociation(
    name="triplets154",
    ends={
        Property(name="afpText_triplet156", type=afpText_MBCRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MBCRG155", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets157: BinaryAssociation = BinaryAssociation(
    name="triplets157",
    ends={
        Property(name="afpText_triplet159", type=afpText_MCARG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MCARG158", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets172: BinaryAssociation = BinaryAssociation(
    name="triplets172",
    ends={
        Property(name="afpText_triplet174", type=afpText_MMDRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMDRG173", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets175: BinaryAssociation = BinaryAssociation(
    name="triplets175",
    ends={
        Property(name="afpText_triplet177", type=afpText_MMTRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MMTRG176", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets178: BinaryAssociation = BinaryAssociation(
    name="triplets178",
    ends={
        Property(name="afpText_triplet180", type=afpText_MPGRG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MPGRG179", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets166: BinaryAssociation = BinaryAssociation(
    name="triplets166",
    ends={
        Property(name="afpText_triplet168", type=afpText_MGORG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MGORG167", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets169: BinaryAssociation = BinaryAssociation(
    name="triplets169",
    ends={
        Property(name="afpText_triplet171", type=afpText_MIORG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MIORG170", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets184: BinaryAssociation = BinaryAssociation(
    name="triplets184",
    ends={
        Property(name="afpText_triplet186", type=afpText_PPORG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_PPORG185", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triplets181: BinaryAssociation = BinaryAssociation(
    name="triplets181",
    ends={
        Property(name="afpText_triplet183", type=afpText_MPORG, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_MPORG182", type=afpText_triplet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg188: BinaryAssociation = BinaryAssociation(
    name="rg188",
    ends={
        Property(name="afpText_ExternalAlgorithmRG", type=afpText_ExternalAlgorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_ExternalAlgorithm", type=afpText_ExternalAlgorithmRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg187: BinaryAssociation = BinaryAssociation(
    name="rg187",
    ends={
        Property(name="afpText_BandImageRG", type=afpText_BandImage, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_BandImage", type=afpText_BandImageRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg189: BinaryAssociation = BinaryAssociation(
    name="rg189",
    ends={
        Property(name="afpText_SamplingRatiosRG", type=afpText_SamplingRatios, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_SamplingRatios", type=afpText_SamplingRatiosRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg190: BinaryAssociation = BinaryAssociation(
    name="rg190",
    ends={
        Property(name="afpText_TileTOCRG", type=afpText_TileTOC, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_TileTOC", type=afpText_TileTOCRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg191: BinaryAssociation = BinaryAssociation(
    name="rg191",
    ends={
        Property(name="afpText_GFLTRG", type=afpText_GFLT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GFLT", type=afpText_GFLTRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg192: BinaryAssociation = BinaryAssociation(
    name="rg192",
    ends={
        Property(name="afpText_GCFLTRG", type=afpText_GCFLT, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCFLT", type=afpText_GCFLTRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg194: BinaryAssociation = BinaryAssociation(
    name="rg194",
    ends={
        Property(name="afpText_GCLINERG", type=afpText_GCLINE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCLINE", type=afpText_GCLINERG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg195: BinaryAssociation = BinaryAssociation(
    name="rg195",
    ends={
        Property(name="afpText_GMRKRG", type=afpText_GMRK, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GMRK", type=afpText_GMRKRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg196: BinaryAssociation = BinaryAssociation(
    name="rg196",
    ends={
        Property(name="afpText_GCMRKRG", type=afpText_GCMRK, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCMRK", type=afpText_GCMRKRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg193: BinaryAssociation = BinaryAssociation(
    name="rg193",
    ends={
        Property(name="afpText_GLINERG", type=afpText_GLINE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GLINE", type=afpText_GLINERG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg197: BinaryAssociation = BinaryAssociation(
    name="rg197",
    ends={
        Property(name="afpText_GRLINERG", type=afpText_GRLINE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GRLINE", type=afpText_GRLINERG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg198: BinaryAssociation = BinaryAssociation(
    name="rg198",
    ends={
        Property(name="afpText_GCRLINERG", type=afpText_GCRLINE, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCRLINE", type=afpText_GCRLINERG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg199: BinaryAssociation = BinaryAssociation(
    name="rg199",
    ends={
        Property(name="afpText_GCBEZRG", type=afpText_GCBEZ, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCBEZ", type=afpText_GCBEZRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rg200: BinaryAssociation = BinaryAssociation(
    name="rg200",
    ends={
        Property(name="afpText_GCCBEZRG", type=afpText_GCCBEZ, multiplicity=Multiplicity(1, 1)),
        Property(name="afpText_GCCBEZ", type=afpText_GCCBEZRG, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_afpText_LineData_structuredField = Generalization(general=structuredField, specific=afpText_LineData)
gen_afpText_BAG_structuredField = Generalization(general=structuredField, specific=afpText_BAG)
gen_afpText_BBC_structuredField = Generalization(general=structuredField, specific=afpText_BBC)
gen_afpText_BDD_structuredField = Generalization(general=structuredField, specific=afpText_BDD)
gen_afpText_BCA_structuredField = Generalization(general=structuredField, specific=afpText_BCA)
gen_afpText_BCF_structuredField = Generalization(general=structuredField, specific=afpText_BCF)
gen_afpText_BCP_structuredField = Generalization(general=structuredField, specific=afpText_BCP)
gen_afpText_BDA_structuredField = Generalization(general=structuredField, specific=afpText_BDA)
gen_afpText_BDX_structuredField = Generalization(general=structuredField, specific=afpText_BDX)
gen_afpText_BFG_structuredField = Generalization(general=structuredField, specific=afpText_BFG)
gen_afpText_BFM_structuredField = Generalization(general=structuredField, specific=afpText_BFM)
gen_afpText_BFN_structuredField = Generalization(general=structuredField, specific=afpText_BFN)
gen_afpText_BGR_structuredField = Generalization(general=structuredField, specific=afpText_BGR)
gen_afpText_BDG_structuredField = Generalization(general=structuredField, specific=afpText_BDG)
gen_afpText_BDI_structuredField = Generalization(general=structuredField, specific=afpText_BDI)
gen_afpText_BDM_structuredField = Generalization(general=structuredField, specific=afpText_BDM)
gen_afpText_BDT_structuredField = Generalization(general=structuredField, specific=afpText_BDT)
gen_afpText_BOG_structuredField = Generalization(general=structuredField, specific=afpText_BOG)
gen_afpText_BPF_structuredField = Generalization(general=structuredField, specific=afpText_BPF)
gen_afpText_BPG_structuredField = Generalization(general=structuredField, specific=afpText_BPG)
gen_afpText_BII_structuredField = Generalization(general=structuredField, specific=afpText_BII)
gen_afpText_BIM_structuredField = Generalization(general=structuredField, specific=afpText_BIM)
gen_afpText_BMM_structuredField = Generalization(general=structuredField, specific=afpText_BMM)
gen_afpText_BMO_structuredField = Generalization(general=structuredField, specific=afpText_BMO)
gen_afpText_BNG_structuredField = Generalization(general=structuredField, specific=afpText_BNG)
gen_afpText_BOC_structuredField = Generalization(general=structuredField, specific=afpText_BOC)
gen_afpText_CAT_structuredField = Generalization(general=structuredField, specific=afpText_CAT)
gen_afpText_CDD_structuredField = Generalization(general=structuredField, specific=afpText_CDD)
gen_afpText_BPM_structuredField = Generalization(general=structuredField, specific=afpText_BPM)
gen_afpText_BPS_structuredField = Generalization(general=structuredField, specific=afpText_BPS)
gen_afpText_BPT_structuredField = Generalization(general=structuredField, specific=afpText_BPT)
gen_afpText_BRG_structuredField = Generalization(general=structuredField, specific=afpText_BRG)
gen_afpText_BRS_structuredField = Generalization(general=structuredField, specific=afpText_BRS)
gen_afpText_BSG_structuredField = Generalization(general=structuredField, specific=afpText_BSG)
gen_afpText_CTC_structuredField = Generalization(general=structuredField, specific=afpText_CTC)
gen_afpText_DXD_structuredField = Generalization(general=structuredField, specific=afpText_DXD)
gen_afpText_EAG_structuredField = Generalization(general=structuredField, specific=afpText_EAG)
gen_afpText_EBC_structuredField = Generalization(general=structuredField, specific=afpText_EBC)
gen_afpText_ECA_structuredField = Generalization(general=structuredField, specific=afpText_ECA)
gen_afpText_CFC_structuredField = Generalization(general=structuredField, specific=afpText_CFC)
gen_afpText_CFI_structuredField = Generalization(general=structuredField, specific=afpText_CFI)
gen_afpText_CPC_structuredField = Generalization(general=structuredField, specific=afpText_CPC)
gen_afpText_CPD_structuredField = Generalization(general=structuredField, specific=afpText_CPD)
gen_afpText_CPI_structuredField = Generalization(general=structuredField, specific=afpText_CPI)
gen_afpText_EFG_structuredField = Generalization(general=structuredField, specific=afpText_EFG)
gen_afpText_EFM_structuredField = Generalization(general=structuredField, specific=afpText_EFM)
gen_afpText_EFN_structuredField = Generalization(general=structuredField, specific=afpText_EFN)
gen_afpText_EGR_structuredField = Generalization(general=structuredField, specific=afpText_EGR)
gen_afpText_EII_structuredField = Generalization(general=structuredField, specific=afpText_EII)
gen_afpText_ECF_structuredField = Generalization(general=structuredField, specific=afpText_ECF)
gen_afpText_ECP_structuredField = Generalization(general=structuredField, specific=afpText_ECP)
gen_afpText_EDG_structuredField = Generalization(general=structuredField, specific=afpText_EDG)
gen_afpText_EDI_structuredField = Generalization(general=structuredField, specific=afpText_EDI)
gen_afpText_EDM_structuredField = Generalization(general=structuredField, specific=afpText_EDM)
gen_afpText_EDT_structuredField = Generalization(general=structuredField, specific=afpText_EDT)
gen_afpText_EDX_structuredField = Generalization(general=structuredField, specific=afpText_EDX)
gen_afpText_EPF_structuredField = Generalization(general=structuredField, specific=afpText_EPF)
gen_afpText_EPG_structuredField = Generalization(general=structuredField, specific=afpText_EPG)
gen_afpText_EPM_structuredField = Generalization(general=structuredField, specific=afpText_EPM)
gen_afpText_EIM_structuredField = Generalization(general=structuredField, specific=afpText_EIM)
gen_afpText_EMM_structuredField = Generalization(general=structuredField, specific=afpText_EMM)
gen_afpText_EMO_structuredField = Generalization(general=structuredField, specific=afpText_EMO)
gen_afpText_ENG_structuredField = Generalization(general=structuredField, specific=afpText_ENG)
gen_afpText_EOC_structuredField = Generalization(general=structuredField, specific=afpText_EOC)
gen_afpText_EOG_structuredField = Generalization(general=structuredField, specific=afpText_EOG)
gen_afpText_EPS_structuredField = Generalization(general=structuredField, specific=afpText_EPS)
gen_afpText_EPT_structuredField = Generalization(general=structuredField, specific=afpText_EPT)
gen_afpText_ERG_structuredField = Generalization(general=structuredField, specific=afpText_ERG)
gen_afpText_ERS_structuredField = Generalization(general=structuredField, specific=afpText_ERS)
gen_afpText_ESG_structuredField = Generalization(general=structuredField, specific=afpText_ESG)
gen_afpText_FNC_structuredField = Generalization(general=structuredField, specific=afpText_FNC)
gen_afpText_FNG_structuredField = Generalization(general=structuredField, specific=afpText_FNG)
gen_afpText_FNI_structuredField = Generalization(general=structuredField, specific=afpText_FNI)
gen_afpText_FNN_structuredField = Generalization(general=structuredField, specific=afpText_FNN)
gen_afpText_FNM_structuredField = Generalization(general=structuredField, specific=afpText_FNM)
gen_afpText_FND_structuredField = Generalization(general=structuredField, specific=afpText_FND)
gen_afpText_IEL_structuredField = Generalization(general=structuredField, specific=afpText_IEL)
gen_afpText_FNO_structuredField = Generalization(general=structuredField, specific=afpText_FNO)
gen_afpText_FNP_structuredField = Generalization(general=structuredField, specific=afpText_FNP)
gen_afpText_GAD_structuredField = Generalization(general=structuredField, specific=afpText_GAD)
gen_afpText_GDD_structuredField = Generalization(general=structuredField, specific=afpText_GDD)
gen_afpText_ICP_structuredField = Generalization(general=structuredField, specific=afpText_ICP)
gen_afpText_IDD_structuredField = Generalization(general=structuredField, specific=afpText_IDD)
gen_afpText_IOC_structuredField = Generalization(general=structuredField, specific=afpText_IOC)
gen_afpText_IID_structuredField = Generalization(general=structuredField, specific=afpText_IID)
gen_afpText_IMM_structuredField = Generalization(general=structuredField, specific=afpText_IMM)
gen_afpText_IOB_structuredField = Generalization(general=structuredField, specific=afpText_IOB)
gen_afpText_IRD_structuredField = Generalization(general=structuredField, specific=afpText_IRD)
gen_afpText_LLE_structuredField = Generalization(general=structuredField, specific=afpText_LLE)
gen_afpText_LNC_structuredField = Generalization(general=structuredField, specific=afpText_LNC)
gen_afpText_LND_structuredField = Generalization(general=structuredField, specific=afpText_LND)
gen_afpText_IPD_structuredField = Generalization(general=structuredField, specific=afpText_IPD)
gen_afpText_IPG_structuredField = Generalization(general=structuredField, specific=afpText_IPG)
gen_afpText_IPO_structuredField = Generalization(general=structuredField, specific=afpText_IPO)
gen_afpText_IPS_structuredField = Generalization(general=structuredField, specific=afpText_IPS)
gen_afpText_MCF_structuredField = Generalization(general=structuredField, specific=afpText_MCF)
gen_afpText_MCF1_structuredField = Generalization(general=structuredField, specific=afpText_MCF1)
gen_afpText_MDD_structuredField = Generalization(general=structuredField, specific=afpText_MDD)
gen_afpText_MBC_structuredField = Generalization(general=structuredField, specific=afpText_MBC)
gen_afpText_MCA_structuredField = Generalization(general=structuredField, specific=afpText_MCA)
gen_afpText_MCC_structuredField = Generalization(general=structuredField, specific=afpText_MCC)
gen_afpText_MCD_structuredField = Generalization(general=structuredField, specific=afpText_MCD)
gen_afpText_MMC_structuredField = Generalization(general=structuredField, specific=afpText_MMC)
gen_afpText_MMD_structuredField = Generalization(general=structuredField, specific=afpText_MMD)
gen_afpText_MDR_structuredField = Generalization(general=structuredField, specific=afpText_MDR)
gen_afpText_MFC_structuredField = Generalization(general=structuredField, specific=afpText_MFC)
gen_afpText_MGO_structuredField = Generalization(general=structuredField, specific=afpText_MGO)
gen_afpText_MIO_structuredField = Generalization(general=structuredField, specific=afpText_MIO)
gen_afpText_NOP_structuredField = Generalization(general=structuredField, specific=afpText_NOP)
gen_afpText_OBD_structuredField = Generalization(general=structuredField, specific=afpText_OBD)
gen_afpText_OBP_structuredField = Generalization(general=structuredField, specific=afpText_OBP)
gen_afpText_MMO_structuredField = Generalization(general=structuredField, specific=afpText_MMO)
gen_afpText_MMT_structuredField = Generalization(general=structuredField, specific=afpText_MMT)
gen_afpText_MPG_structuredField = Generalization(general=structuredField, specific=afpText_MPG)
gen_afpText_MPO_structuredField = Generalization(general=structuredField, specific=afpText_MPO)
gen_afpText_MPS_structuredField = Generalization(general=structuredField, specific=afpText_MPS)
gen_afpText_MSU_structuredField = Generalization(general=structuredField, specific=afpText_MSU)
gen_afpText_PGP_structuredField = Generalization(general=structuredField, specific=afpText_PGP)
gen_afpText_PGP1_structuredField = Generalization(general=structuredField, specific=afpText_PGP1)
gen_afpText_OCD_structuredField = Generalization(general=structuredField, specific=afpText_OCD)
gen_afpText_PEC_structuredField = Generalization(general=structuredField, specific=afpText_PEC)
gen_afpText_PFC_structuredField = Generalization(general=structuredField, specific=afpText_PFC)
gen_afpText_PGD_structuredField = Generalization(general=structuredField, specific=afpText_PGD)
gen_afpText_PTD_structuredField = Generalization(general=structuredField, specific=afpText_PTD)
gen_afpText_PMC_structuredField = Generalization(general=structuredField, specific=afpText_PMC)
gen_afpText_PPO_structuredField = Generalization(general=structuredField, specific=afpText_PPO)
gen_afpText_FGD_structuredField = Generalization(general=structuredField, specific=afpText_FGD)
gen_afpText_PTD1_structuredField = Generalization(general=structuredField, specific=afpText_PTD1)
gen_afpText_PTX_structuredField = Generalization(general=structuredField, specific=afpText_PTX)
gen_afpText_TLE_structuredField = Generalization(general=structuredField, specific=afpText_TLE)
gen_afpText_AMB_triplet = Generalization(general=triplet, specific=afpText_AMB)
gen_afpText_AMI_triplet = Generalization(general=triplet, specific=afpText_AMI)
gen_afpText_BLN_triplet = Generalization(general=triplet, specific=afpText_BLN)
gen_afpText_BSU_triplet = Generalization(general=triplet, specific=afpText_BSU)
gen_afpText_DBR_triplet = Generalization(general=triplet, specific=afpText_DBR)
gen_afpText_OVS_triplet = Generalization(general=triplet, specific=afpText_OVS)
gen_afpText_RMB_triplet = Generalization(general=triplet, specific=afpText_RMB)
gen_afpText_DIR_triplet = Generalization(general=triplet, specific=afpText_DIR)
gen_afpText_ESU_triplet = Generalization(general=triplet, specific=afpText_ESU)
gen_afpText_NOPCS_triplet = Generalization(general=triplet, specific=afpText_NOPCS)
gen_afpText_RMI_triplet = Generalization(general=triplet, specific=afpText_RMI)
gen_afpText_RPS_triplet = Generalization(general=triplet, specific=afpText_RPS)
gen_afpText_SBI_triplet = Generalization(general=triplet, specific=afpText_SBI)
gen_afpText_SCFL_triplet = Generalization(general=triplet, specific=afpText_SCFL)
gen_afpText_SEC_triplet = Generalization(general=triplet, specific=afpText_SEC)
gen_afpText_SIM_triplet = Generalization(general=triplet, specific=afpText_SIM)
gen_afpText_STC_triplet = Generalization(general=triplet, specific=afpText_STC)
gen_afpText_STO_triplet = Generalization(general=triplet, specific=afpText_STO)
gen_afpText_SVI_triplet = Generalization(general=triplet, specific=afpText_SVI)
gen_afpText_AttributeValue_triplet = Generalization(general=triplet, specific=afpText_AttributeValue)
gen_afpText_SIA_triplet = Generalization(general=triplet, specific=afpText_SIA)
gen_afpText_CGCSGID_triplet = Generalization(general=triplet, specific=afpText_CGCSGID)
gen_afpText_CRCResourceManagement_triplet = Generalization(general=triplet, specific=afpText_CRCResourceManagement)
gen_afpText_CharacterRotation_triplet = Generalization(general=triplet, specific=afpText_CharacterRotation)
gen_afpText_TBM_triplet = Generalization(general=triplet, specific=afpText_TBM)
gen_afpText_TRN_triplet = Generalization(general=triplet, specific=afpText_TRN)
gen_afpText_USC_triplet = Generalization(general=triplet, specific=afpText_USC)
gen_afpText_AttributeQualifier_triplet = Generalization(general=triplet, specific=afpText_AttributeQualifier)
gen_afpText_DescriptorPosition_triplet = Generalization(general=triplet, specific=afpText_DescriptorPosition)
gen_afpText_EncodingSchemeID_triplet = Generalization(general=triplet, specific=afpText_EncodingSchemeID)
gen_afpText_ColorSpecification_triplet = Generalization(general=triplet, specific=afpText_ColorSpecification)
gen_afpText_Comment_triplet = Generalization(general=triplet, specific=afpText_Comment)
gen_afpText_DataObjectFontDescriptor_triplet = Generalization(general=triplet, specific=afpText_DataObjectFontDescriptor)
gen_afpText_UniversalDateAndTimeStamp_triplet = Generalization(general=triplet, specific=afpText_UniversalDateAndTimeStamp)
gen_afpText_FontResolution_triplet = Generalization(general=triplet, specific=afpText_FontResolution)
gen_afpText_FullyQualifiedName_triplet = Generalization(general=triplet, specific=afpText_FullyQualifiedName)
gen_afpText_LocalDateAndTimeStamp_triplet = Generalization(general=triplet, specific=afpText_LocalDateAndTimeStamp)
gen_afpText_MediumOrientation_triplet = Generalization(general=triplet, specific=afpText_MediumOrientation)
gen_afpText_MeasurementUnits_triplet = Generalization(general=triplet, specific=afpText_MeasurementUnits)
gen_afpText_MODCAInterchangeSet_triplet = Generalization(general=triplet, specific=afpText_MODCAInterchangeSet)
gen_afpText_ObjectAreaSize_triplet = Generalization(general=triplet, specific=afpText_ObjectAreaSize)
gen_afpText_MappingOption_triplet = Generalization(general=triplet, specific=afpText_MappingOption)
gen_afpText_MediaEjectControl_triplet = Generalization(general=triplet, specific=afpText_MediaEjectControl)
gen_afpText_MediumMapPageNumber_triplet = Generalization(general=triplet, specific=afpText_MediumMapPageNumber)
gen_afpText_ObjectOffset_triplet = Generalization(general=triplet, specific=afpText_ObjectOffset)
gen_afpText_ResourceObjectType_triplet = Generalization(general=triplet, specific=afpText_ResourceObjectType)
gen_afpText_PagePositionInformation_triplet = Generalization(general=triplet, specific=afpText_PagePositionInformation)
gen_afpText_PresentationControl_triplet = Generalization(general=triplet, specific=afpText_PresentationControl)
gen_afpText_ObjectClassification_triplet = Generalization(general=triplet, specific=afpText_ObjectClassification)
gen_afpText_ResourceSectionNumber_triplet = Generalization(general=triplet, specific=afpText_ResourceSectionNumber)
gen_afpText_ObjectFunctionSetSpecification_triplet = Generalization(general=triplet, specific=afpText_ObjectFunctionSetSpecification)
gen_afpText_TextOrientation_triplet = Generalization(general=triplet, specific=afpText_TextOrientation)
gen_afpText_FontHorizontalScaleFactor_triplet = Generalization(general=triplet, specific=afpText_FontHorizontalScaleFactor)
gen_afpText_FontDescriptorSpecification_triplet = Generalization(general=triplet, specific=afpText_FontDescriptorSpecification)
gen_afpText_PresentationSpaceResetMixing_triplet = Generalization(general=triplet, specific=afpText_PresentationSpaceResetMixing)
gen_afpText_PresentationSpaceMixingRules_triplet = Generalization(general=triplet, specific=afpText_PresentationSpaceMixingRules)
gen_afpText_ResourceLocalIdentifier_triplet = Generalization(general=triplet, specific=afpText_ResourceLocalIdentifier)
gen_afpText_BeginImage_triplet = Generalization(general=triplet, specific=afpText_BeginImage)
gen_afpText_EndImage_triplet = Generalization(general=triplet, specific=afpText_EndImage)
gen_afpText_ImageSize_triplet = Generalization(general=triplet, specific=afpText_ImageSize)
gen_afpText_ImageEncoding_triplet = Generalization(general=triplet, specific=afpText_ImageEncoding)
gen_afpText_BeginSegment_triplet = Generalization(general=triplet, specific=afpText_BeginSegment)
gen_afpText_EndSegment_triplet = Generalization(general=triplet, specific=afpText_EndSegment)
gen_afpText_BeginTile_triplet = Generalization(general=triplet, specific=afpText_BeginTile)
gen_afpText_EndTile_triplet = Generalization(general=triplet, specific=afpText_EndTile)
gen_afpText_BeginTransparencyMask_triplet = Generalization(general=triplet, specific=afpText_BeginTransparencyMask)
gen_afpText_EndTransparencyMask_triplet = Generalization(general=triplet, specific=afpText_EndTransparencyMask)
gen_afpText_IDEStructure_triplet = Generalization(general=triplet, specific=afpText_IDEStructure)
gen_afpText_ExternalAlgorithm_triplet = Generalization(general=triplet, specific=afpText_ExternalAlgorithm)
gen_afpText_TilePosition_triplet = Generalization(general=triplet, specific=afpText_TilePosition)
gen_afpText_IDESize_triplet = Generalization(general=triplet, specific=afpText_IDESize)
gen_afpText_ImageLUTID_triplet = Generalization(general=triplet, specific=afpText_ImageLUTID)
gen_afpText_BandImage_triplet = Generalization(general=triplet, specific=afpText_BandImage)
gen_afpText_SetBiLevelImageColor_triplet = Generalization(general=triplet, specific=afpText_SetBiLevelImageColor)
gen_afpText_IOCAFunctionSetIdentification_triplet = Generalization(general=triplet, specific=afpText_IOCAFunctionSetIdentification)
gen_afpText_TileSize_triplet = Generalization(general=triplet, specific=afpText_TileSize)
gen_afpText_TileSetColor_triplet = Generalization(general=triplet, specific=afpText_TileSetColor)
gen_afpText_ImageSubsampling_triplet = Generalization(general=triplet, specific=afpText_ImageSubsampling)
gen_afpText_SamplingRatios_triplet = Generalization(general=triplet, specific=afpText_SamplingRatios)
gen_afpText_TileTOC_triplet = Generalization(general=triplet, specific=afpText_TileTOC)
gen_afpText_ImageData_triplet = Generalization(general=triplet, specific=afpText_ImageData)
gen_afpText_BandImageData_triplet = Generalization(general=triplet, specific=afpText_BandImageData)
gen_afpText_IncludeTile_triplet = Generalization(general=triplet, specific=afpText_IncludeTile)
gen_afpText_GBAR_triplet = Generalization(general=triplet, specific=afpText_GBAR)
gen_afpText_GBIMG_triplet = Generalization(general=triplet, specific=afpText_GBIMG)
gen_afpText_GCBIMG_triplet = Generalization(general=triplet, specific=afpText_GCBIMG)
gen_afpText_FNNRG2_triplet = Generalization(general=triplet, specific=afpText_FNNRG2)
gen_afpText_BeginSegmentCommand_triplet = Generalization(general=triplet, specific=afpText_BeginSegmentCommand)
gen_afpText_EndSegmentCommand_triplet = Generalization(general=triplet, specific=afpText_EndSegmentCommand)
gen_afpText_GCBOX_triplet = Generalization(general=triplet, specific=afpText_GCBOX)
gen_afpText_GCHST_triplet = Generalization(general=triplet, specific=afpText_GCHST)
gen_afpText_GCCHST_triplet = Generalization(general=triplet, specific=afpText_GCCHST)
gen_afpText_GCOMT_triplet = Generalization(general=triplet, specific=afpText_GCOMT)
gen_afpText_GBOX_triplet = Generalization(general=triplet, specific=afpText_GBOX)
gen_afpText_GCFLT_triplet = Generalization(general=triplet, specific=afpText_GCFLT)
gen_afpText_GFARC_triplet = Generalization(general=triplet, specific=afpText_GFARC)
gen_afpText_GCFARC_triplet = Generalization(general=triplet, specific=afpText_GCFARC)
gen_afpText_GEAR_triplet = Generalization(general=triplet, specific=afpText_GEAR)
gen_afpText_GEIMG_triplet = Generalization(general=triplet, specific=afpText_GEIMG)
gen_afpText_GEPROL_triplet = Generalization(general=triplet, specific=afpText_GEPROL)
gen_afpText_GFLT_triplet = Generalization(general=triplet, specific=afpText_GFLT)
gen_afpText_GCLINE_triplet = Generalization(general=triplet, specific=afpText_GCLINE)
gen_afpText_GMRK_triplet = Generalization(general=triplet, specific=afpText_GMRK)
gen_afpText_GCMRK_triplet = Generalization(general=triplet, specific=afpText_GCMRK)
gen_afpText_GNOP1_triplet = Generalization(general=triplet, specific=afpText_GNOP1)
gen_afpText_GPARC_triplet = Generalization(general=triplet, specific=afpText_GPARC)
gen_afpText_GIMD_triplet = Generalization(general=triplet, specific=afpText_GIMD)
gen_afpText_GLINE_triplet = Generalization(general=triplet, specific=afpText_GLINE)
gen_afpText_GRLINE_triplet = Generalization(general=triplet, specific=afpText_GRLINE)
gen_afpText_GCRLINE_triplet = Generalization(general=triplet, specific=afpText_GCRLINE)
gen_afpText_GCPARC_triplet = Generalization(general=triplet, specific=afpText_GCPARC)
gen_afpText_GSBMX_triplet = Generalization(general=triplet, specific=afpText_GSBMX)
gen_afpText_GSCA_triplet = Generalization(general=triplet, specific=afpText_GSCA)
gen_afpText_GSCC_triplet = Generalization(general=triplet, specific=afpText_GSCC)
gen_afpText_GSCD_triplet = Generalization(general=triplet, specific=afpText_GSCD)
gen_afpText_GSGCH_triplet = Generalization(general=triplet, specific=afpText_GSGCH)
gen_afpText_GSAP_triplet = Generalization(general=triplet, specific=afpText_GSAP)
gen_afpText_GSCOL_triplet = Generalization(general=triplet, specific=afpText_GSCOL)
gen_afpText_GSCP_triplet = Generalization(general=triplet, specific=afpText_GSCP)
gen_afpText_GSECOL_triplet = Generalization(general=triplet, specific=afpText_GSECOL)
gen_afpText_GSFLW_triplet = Generalization(general=triplet, specific=afpText_GSFLW)
gen_afpText_GSLT_triplet = Generalization(general=triplet, specific=afpText_GSLT)
gen_afpText_GSCR_triplet = Generalization(general=triplet, specific=afpText_GSCR)
gen_afpText_GSCS_triplet = Generalization(general=triplet, specific=afpText_GSCS)
gen_afpText_GSCH_triplet = Generalization(general=triplet, specific=afpText_GSCH)
gen_afpText_GSMS_triplet = Generalization(general=triplet, specific=afpText_GSMS)
gen_afpText_GSMT_triplet = Generalization(general=triplet, specific=afpText_GSMT)
gen_afpText_GSMX_triplet = Generalization(general=triplet, specific=afpText_GSMX)
gen_afpText_GSPS_triplet = Generalization(general=triplet, specific=afpText_GSPS)
gen_afpText_GSPT_triplet = Generalization(general=triplet, specific=afpText_GSPT)
gen_afpText_GSLW_triplet = Generalization(general=triplet, specific=afpText_GSLW)
gen_afpText_GSMC_triplet = Generalization(general=triplet, specific=afpText_GSMC)
gen_afpText_GSMP_triplet = Generalization(general=triplet, specific=afpText_GSMP)
gen_afpText_GSLE_triplet = Generalization(general=triplet, specific=afpText_GSLE)
gen_afpText_GSLJ_triplet = Generalization(general=triplet, specific=afpText_GSLJ)
gen_afpText_GCBEZ_triplet = Generalization(general=triplet, specific=afpText_GCBEZ)
gen_afpText_GCCBEZ_triplet = Generalization(general=triplet, specific=afpText_GCCBEZ)
gen_afpText_GSPCOL_triplet = Generalization(general=triplet, specific=afpText_GSPCOL)
gen_afpText_DrawingOrderSubset_triplet = Generalization(general=triplet, specific=afpText_DrawingOrderSubset)
gen_afpText_TonerSaver_triplet = Generalization(general=triplet, specific=afpText_TonerSaver)
gen_afpText_ColorFidelity_triplet = Generalization(general=triplet, specific=afpText_ColorFidelity)
gen_afpText_FontFidelity_triplet = Generalization(general=triplet, specific=afpText_FontFidelity)
gen_afpText_WindowSpecification_triplet = Generalization(general=triplet, specific=afpText_WindowSpecification)
gen_afpText_FinishingFidelity_triplet = Generalization(general=triplet, specific=afpText_FinishingFidelity)
gen_afpText_CMRFidelity_triplet = Generalization(general=triplet, specific=afpText_CMRFidelity)
gen_afpText_ObjectByteExtent_triplet = Generalization(general=triplet, specific=afpText_ObjectByteExtent)
gen_afpText_ObjectByteOffset_triplet = Generalization(general=triplet, specific=afpText_ObjectByteOffset)
gen_afpText_ObjectStructuredFieldExtent_triplet = Generalization(general=triplet, specific=afpText_ObjectStructuredFieldExtent)
gen_afpText_TextFidelity_triplet = Generalization(general=triplet, specific=afpText_TextFidelity)
gen_afpText_MediaFidelity_triplet = Generalization(general=triplet, specific=afpText_MediaFidelity)
gen_afpText_ObjectOriginIdentifier_triplet = Generalization(general=triplet, specific=afpText_ObjectOriginIdentifier)
gen_afpText_LineDataObjectPositionMigration_triplet = Generalization(general=triplet, specific=afpText_LineDataObjectPositionMigration)
gen_afpText_ColorManagementResourceDescriptor_triplet = Generalization(general=triplet, specific=afpText_ColorManagementResourceDescriptor)
gen_afpText_ObjectStructuredFieldOffset_triplet = Generalization(general=triplet, specific=afpText_ObjectStructuredFieldOffset)
gen_afpText_ObjectCount_triplet = Generalization(general=triplet, specific=afpText_ObjectCount)
gen_afpText_ExtendedResourceLocalIdentifier_triplet = Generalization(general=triplet, specific=afpText_ExtendedResourceLocalIdentifier)
gen_afpText_MetricAdjustment_triplet = Generalization(general=triplet, specific=afpText_MetricAdjustment)
gen_afpText_ExtensionFont_triplet = Generalization(general=triplet, specific=afpText_ExtensionFont)
gen_afpText_ImageResolution_triplet = Generalization(general=triplet, specific=afpText_ImageResolution)
gen_afpText_ObjectContainerPresentationSpaceSize_triplet = Generalization(general=triplet, specific=afpText_ObjectContainerPresentationSpaceSize)
gen_afpText_LocaleSelector_triplet = Generalization(general=triplet, specific=afpText_LocaleSelector)
gen_afpText_FinishingOperation_triplet = Generalization(general=triplet, specific=afpText_FinishingOperation)
gen_afpText_RenderingIntent_triplet = Generalization(general=triplet, specific=afpText_RenderingIntent)
gen_afpText_FontCodedGraphicCharacterSetGlobalIdentifier_triplet = Generalization(general=triplet, specific=afpText_FontCodedGraphicCharacterSetGlobalIdentifier)
gen_afpText_PageOverlayConditionalProcessing_triplet = Generalization(general=triplet, specific=afpText_PageOverlayConditionalProcessing)
gen_afpText_ResourceUsageAttribute_triplet = Generalization(general=triplet, specific=afpText_ResourceUsageAttribute)
gen_afpText_UP3iFinishingOperation_triplet = Generalization(general=triplet, specific=afpText_UP3iFinishingOperation)
gen_afpText_DeviceAppearance_triplet = Generalization(general=triplet, specific=afpText_DeviceAppearance)
gen_afpText_ResourceObjectInclude_triplet = Generalization(general=triplet, specific=afpText_ResourceObjectInclude)

# Domain Model
domain_model = DomainModel(
    name="afpText",
    types={afpText_structuredField, afpText_LineData, structuredField, afpText_BAG, afpText_triplet, afpText_BBC, afpText_Model, afpText_BDD, afpText_BCA, afpText_BCF, afpText_BCP, afpText_BDA, afpText_BDX, afpText_BFG, afpText_BFM, afpText_BFN, afpText_BGR, afpText_BDG, afpText_BDI, afpText_BDM, afpText_BDT, afpText_BOG, afpText_BPF, afpText_BPG, afpText_BII, afpText_BIM, afpText_BMM, afpText_BMO, afpText_BNG, afpText_BOC, afpText_CAT, afpText_CDD, afpText_CFC, afpText_BPM, afpText_BPS, afpText_BPT, afpText_BRG, afpText_BRS, afpText_BSG, afpText_CTC, afpText_DXD, afpText_EAG, afpText_EBC, afpText_ECA, afpText_CFI, afpText_CFIRG, afpText_CPC, afpText_CPD, afpText_CPI, afpText_CPIRG, afpText_EFM, afpText_EFN, afpText_EGR, afpText_EII, afpText_EIM, afpText_ECF, afpText_ECP, afpText_EDG, afpText_EDI, afpText_EDM, afpText_EDT, afpText_EDX, afpText_EFG, afpText_EPF, afpText_EPG, afpText_EPM, afpText_EMM, afpText_EMO, afpText_ENG, afpText_EOC, afpText_EOG, afpText_EPS, afpText_EPT, afpText_ERG, afpText_ERS, afpText_ESG, afpText_FNC, afpText_FNG, afpText_FNI, afpText_FNIRG, afpText_FNN, afpText_FNM, afpText_FNMRG, afpText_FND, afpText_IEL, afpText_FNO, afpText_FNORG, afpText_FNP, afpText_FNPRG, afpText_GAD, afpText_GDD, afpText_ICP, afpText_IDD, afpText_IOC, afpText_IID, afpText_IMM, afpText_IOB, afpText_IRD, afpText_LLE, afpText_LLERG, afpText_LNC, afpText_LND, afpText_IPD, afpText_IPG, afpText_IPO, afpText_IPS, afpText_MCDRG, afpText_MCF, afpText_MCFRG, afpText_MCF1, afpText_MCF1RG, afpText_MDD, afpText_MBC, afpText_MBCRG, afpText_MCA, afpText_MCARG, afpText_MCC, afpText_MCCRG, afpText_MCD, afpText_MMC, afpText_MMCRG, afpText_MMD, afpText_MMDRG, afpText_MDR, afpText_MDRRG, afpText_MFC, afpText_MGO, afpText_MGORG, afpText_MIO, afpText_MIORG, afpText_MSURG, afpText_NOP, afpText_OBD, afpText_OBP, afpText_MMO, afpText_MMORG, afpText_MMT, afpText_MMTRG, afpText_MPG, afpText_MPGRG, afpText_MPO, afpText_MPORG, afpText_MPS, afpText_MPSRG, afpText_MSU, afpText_PGP, afpText_PGPRG, afpText_PGP1, afpText_PMC, afpText_OCD, afpText_PEC, afpText_PFC, afpText_PGD, afpText_PTD, afpText_PPO, afpText_PPORG, afpText_FGD, afpText_PTD1, afpText_PTX, afpText_TLE, afpText_BandImageRG, afpText_TileTOCRG, afpText_SamplingRatiosRG, afpText_GFLTRG, afpText_GCFLTRG, afpText_GLINERG, afpText_GCLINERG, afpText_ExternalAlgorithmRG, afpText_FNNRG, afpText_GCBEZRG, afpText_GCCBEZRG, afpText_AMB, triplet, afpText_AMI, afpText_BLN, afpText_BSU, afpText_DBR, afpText_GMRKRG, afpText_GCMRKRG, afpText_GRLINERG, afpText_GCRLINERG, afpText_OVS, afpText_RMB, afpText_DIR, afpText_ESU, afpText_NOPCS, afpText_RMI, afpText_RPS, afpText_SBI, afpText_SCFL, afpText_SEC, afpText_SIM, afpText_STC, afpText_STO, afpText_SVI, afpText_AttributeValue, afpText_SIA, afpText_CGCSGID, afpText_CRCResourceManagement, afpText_CharacterRotation, afpText_TBM, afpText_TRN, afpText_USC, afpText_AttributeQualifier, afpText_DescriptorPosition, afpText_EncodingSchemeID, afpText_FontResolution, afpText_ColorSpecification, afpText_Comment, afpText_DataObjectFontDescriptor, afpText_UniversalDateAndTimeStamp, afpText_FullyQualifiedName, afpText_LocalDateAndTimeStamp, afpText_MediumOrientation, afpText_MeasurementUnits, afpText_MODCAInterchangeSet, afpText_ObjectAreaSize, afpText_MappingOption, afpText_MediaEjectControl, afpText_MediumMapPageNumber, afpText_ObjectOffset, afpText_ResourceObjectType, afpText_PagePositionInformation, afpText_PresentationControl, afpText_ObjectClassification, afpText_ObjectFunctionSetSpecification, afpText_TextOrientation, afpText_FontHorizontalScaleFactor, afpText_FontDescriptorSpecification, afpText_PresentationSpaceResetMixing, afpText_PresentationSpaceMixingRules, afpText_ResourceLocalIdentifier, afpText_BeginImage, afpText_ResourceSectionNumber, afpText_EndImage, afpText_ImageSize, afpText_ImageEncoding, afpText_BeginSegment, afpText_EndSegment, afpText_BeginTile, afpText_EndTile, afpText_BeginTransparencyMask, afpText_EndTransparencyMask, afpText_IDEStructure, afpText_ExternalAlgorithm, afpText_TilePosition, afpText_IDESize, afpText_ImageLUTID, afpText_BandImage, afpText_SetBiLevelImageColor, afpText_IOCAFunctionSetIdentification, afpText_TileSize, afpText_TileSetColor, afpText_ImageSubsampling, afpText_SamplingRatios, afpText_TileTOC, afpText_ImageData, afpText_BandImageData, afpText_IncludeTile, afpText_GBAR, afpText_GBIMG, afpText_GCBIMG, afpText_FNNRG2, afpText_BeginSegmentCommand, afpText_EndSegmentCommand, afpText_GCBOX, afpText_GCHST, afpText_GCCHST, afpText_GCOMT, afpText_GBOX, afpText_GCFLT, afpText_GFARC, afpText_GCFARC, afpText_GEAR, afpText_GEIMG, afpText_GEPROL, afpText_GFLT, afpText_GCLINE, afpText_GMRK, afpText_GCMRK, afpText_GNOP1, afpText_GPARC, afpText_GIMD, afpText_GLINE, afpText_GRLINE, afpText_GCRLINE, afpText_GCPARC, afpText_GSBMX, afpText_GSCA, afpText_GSCC, afpText_GSCD, afpText_GSGCH, afpText_GSAP, afpText_GSCOL, afpText_GSCP, afpText_GSECOL, afpText_GSFLW, afpText_GSLT, afpText_GSCR, afpText_GSCS, afpText_GSCH, afpText_GSMS, afpText_GSMT, afpText_GSMX, afpText_GSPS, afpText_GSPT, afpText_GSLW, afpText_GSMC, afpText_GSMP, afpText_GSLE, afpText_GSLJ, afpText_GCBEZ, afpText_GCCBEZ, afpText_GSPCOL, afpText_DrawingOrderSubset, afpText_TonerSaver, afpText_ColorFidelity, afpText_FontFidelity, afpText_WindowSpecification, afpText_FinishingFidelity, afpText_CMRFidelity, afpText_ObjectByteExtent, afpText_ObjectByteOffset, afpText_ObjectStructuredFieldExtent, afpText_TextFidelity, afpText_MediaFidelity, afpText_ObjectOriginIdentifier, afpText_LineDataObjectPositionMigration, afpText_ColorManagementResourceDescriptor, afpText_ObjectStructuredFieldOffset, afpText_ObjectCount, afpText_ExtendedResourceLocalIdentifier, afpText_MetricAdjustment, afpText_ExtensionFont, afpText_ImageResolution, afpText_ObjectContainerPresentationSpaceSize, afpText_LocaleSelector, afpText_FinishingOperation, afpText_RenderingIntent, afpText_FontCodedGraphicCharacterSetGlobalIdentifier, afpText_PageOverlayConditionalProcessing, afpText_ResourceUsageAttribute, afpText_UP3iFinishingOperation, afpText_DeviceAppearance, afpText_ResourceObjectInclude},
    associations={structuredFields0, triplets1, triplets8, triplets2, triplets4, triplets6, triplets18, triplets20, triplets10, triplets12, triplets14, triplets32, triplets16, triplets34, triplets36, triplets38, triplets22, triplets24, triplets26, triplets28, triplets30, triplets48, triplets50, triplets40, triplets42, triplets44, triplets46, triplets56, triplets58, triplets52, rg54, rg55, triplets64, triplets60, triplets62, triplets74, triplets76, triplets66, triplets68, triplets70, triplets72, triplets78, triplets80, rg86, rg87, triplets82, triplets84, triplets92, triplets94, rg88, rg89, triplets90, triplets98, triplets96, rg106, triplets100, triplets102, triplets104, rg112, rg113, rg114, triplets107, rg109, rg110, rg111, rg121, rg122, rg123, triplets115, rg117, triplets118, rg120, rg129, triplets130, rg124, rg125, rg126, rg127, rg128, triplets136, rg138, triplets132, triplets134, triplets142, triplets139, rg141, triplets146, triplets144, triplets148, triplets160, triplets163, triplets151, triplets154, triplets157, triplets172, triplets175, triplets178, triplets166, triplets169, triplets184, triplets181, rg188, rg187, rg189, rg190, rg191, rg192, rg194, rg195, rg196, rg193, rg197, rg198, rg199, rg200},
    generalizations={gen_afpText_LineData_structuredField, gen_afpText_BAG_structuredField, gen_afpText_BBC_structuredField, gen_afpText_BDD_structuredField, gen_afpText_BCA_structuredField, gen_afpText_BCF_structuredField, gen_afpText_BCP_structuredField, gen_afpText_BDA_structuredField, gen_afpText_BDX_structuredField, gen_afpText_BFG_structuredField, gen_afpText_BFM_structuredField, gen_afpText_BFN_structuredField, gen_afpText_BGR_structuredField, gen_afpText_BDG_structuredField, gen_afpText_BDI_structuredField, gen_afpText_BDM_structuredField, gen_afpText_BDT_structuredField, gen_afpText_BOG_structuredField, gen_afpText_BPF_structuredField, gen_afpText_BPG_structuredField, gen_afpText_BII_structuredField, gen_afpText_BIM_structuredField, gen_afpText_BMM_structuredField, gen_afpText_BMO_structuredField, gen_afpText_BNG_structuredField, gen_afpText_BOC_structuredField, gen_afpText_CAT_structuredField, gen_afpText_CDD_structuredField, gen_afpText_BPM_structuredField, gen_afpText_BPS_structuredField, gen_afpText_BPT_structuredField, gen_afpText_BRG_structuredField, gen_afpText_BRS_structuredField, gen_afpText_BSG_structuredField, gen_afpText_CTC_structuredField, gen_afpText_DXD_structuredField, gen_afpText_EAG_structuredField, gen_afpText_EBC_structuredField, gen_afpText_ECA_structuredField, gen_afpText_CFC_structuredField, gen_afpText_CFI_structuredField, gen_afpText_CPC_structuredField, gen_afpText_CPD_structuredField, gen_afpText_CPI_structuredField, gen_afpText_EFG_structuredField, gen_afpText_EFM_structuredField, gen_afpText_EFN_structuredField, gen_afpText_EGR_structuredField, gen_afpText_EII_structuredField, gen_afpText_ECF_structuredField, gen_afpText_ECP_structuredField, gen_afpText_EDG_structuredField, gen_afpText_EDI_structuredField, gen_afpText_EDM_structuredField, gen_afpText_EDT_structuredField, gen_afpText_EDX_structuredField, gen_afpText_EPF_structuredField, gen_afpText_EPG_structuredField, gen_afpText_EPM_structuredField, gen_afpText_EIM_structuredField, gen_afpText_EMM_structuredField, gen_afpText_EMO_structuredField, gen_afpText_ENG_structuredField, gen_afpText_EOC_structuredField, gen_afpText_EOG_structuredField, gen_afpText_EPS_structuredField, gen_afpText_EPT_structuredField, gen_afpText_ERG_structuredField, gen_afpText_ERS_structuredField, gen_afpText_ESG_structuredField, gen_afpText_FNC_structuredField, gen_afpText_FNG_structuredField, gen_afpText_FNI_structuredField, gen_afpText_FNN_structuredField, gen_afpText_FNM_structuredField, gen_afpText_FND_structuredField, gen_afpText_IEL_structuredField, gen_afpText_FNO_structuredField, gen_afpText_FNP_structuredField, gen_afpText_GAD_structuredField, gen_afpText_GDD_structuredField, gen_afpText_ICP_structuredField, gen_afpText_IDD_structuredField, gen_afpText_IOC_structuredField, gen_afpText_IID_structuredField, gen_afpText_IMM_structuredField, gen_afpText_IOB_structuredField, gen_afpText_IRD_structuredField, gen_afpText_LLE_structuredField, gen_afpText_LNC_structuredField, gen_afpText_LND_structuredField, gen_afpText_IPD_structuredField, gen_afpText_IPG_structuredField, gen_afpText_IPO_structuredField, gen_afpText_IPS_structuredField, gen_afpText_MCF_structuredField, gen_afpText_MCF1_structuredField, gen_afpText_MDD_structuredField, gen_afpText_MBC_structuredField, gen_afpText_MCA_structuredField, gen_afpText_MCC_structuredField, gen_afpText_MCD_structuredField, gen_afpText_MMC_structuredField, gen_afpText_MMD_structuredField, gen_afpText_MDR_structuredField, gen_afpText_MFC_structuredField, gen_afpText_MGO_structuredField, gen_afpText_MIO_structuredField, gen_afpText_NOP_structuredField, gen_afpText_OBD_structuredField, gen_afpText_OBP_structuredField, gen_afpText_MMO_structuredField, gen_afpText_MMT_structuredField, gen_afpText_MPG_structuredField, gen_afpText_MPO_structuredField, gen_afpText_MPS_structuredField, gen_afpText_MSU_structuredField, gen_afpText_PGP_structuredField, gen_afpText_PGP1_structuredField, gen_afpText_OCD_structuredField, gen_afpText_PEC_structuredField, gen_afpText_PFC_structuredField, gen_afpText_PGD_structuredField, gen_afpText_PTD_structuredField, gen_afpText_PMC_structuredField, gen_afpText_PPO_structuredField, gen_afpText_FGD_structuredField, gen_afpText_PTD1_structuredField, gen_afpText_PTX_structuredField, gen_afpText_TLE_structuredField, gen_afpText_AMB_triplet, gen_afpText_AMI_triplet, gen_afpText_BLN_triplet, gen_afpText_BSU_triplet, gen_afpText_DBR_triplet, gen_afpText_OVS_triplet, gen_afpText_RMB_triplet, gen_afpText_DIR_triplet, gen_afpText_ESU_triplet, gen_afpText_NOPCS_triplet, gen_afpText_RMI_triplet, gen_afpText_RPS_triplet, gen_afpText_SBI_triplet, gen_afpText_SCFL_triplet, gen_afpText_SEC_triplet, gen_afpText_SIM_triplet, gen_afpText_STC_triplet, gen_afpText_STO_triplet, gen_afpText_SVI_triplet, gen_afpText_AttributeValue_triplet, gen_afpText_SIA_triplet, gen_afpText_CGCSGID_triplet, gen_afpText_CRCResourceManagement_triplet, gen_afpText_CharacterRotation_triplet, gen_afpText_TBM_triplet, gen_afpText_TRN_triplet, gen_afpText_USC_triplet, gen_afpText_AttributeQualifier_triplet, gen_afpText_DescriptorPosition_triplet, gen_afpText_EncodingSchemeID_triplet, gen_afpText_ColorSpecification_triplet, gen_afpText_Comment_triplet, gen_afpText_DataObjectFontDescriptor_triplet, gen_afpText_UniversalDateAndTimeStamp_triplet, gen_afpText_FontResolution_triplet, gen_afpText_FullyQualifiedName_triplet, gen_afpText_LocalDateAndTimeStamp_triplet, gen_afpText_MediumOrientation_triplet, gen_afpText_MeasurementUnits_triplet, gen_afpText_MODCAInterchangeSet_triplet, gen_afpText_ObjectAreaSize_triplet, gen_afpText_MappingOption_triplet, gen_afpText_MediaEjectControl_triplet, gen_afpText_MediumMapPageNumber_triplet, gen_afpText_ObjectOffset_triplet, gen_afpText_ResourceObjectType_triplet, gen_afpText_PagePositionInformation_triplet, gen_afpText_PresentationControl_triplet, gen_afpText_ObjectClassification_triplet, gen_afpText_ResourceSectionNumber_triplet, gen_afpText_ObjectFunctionSetSpecification_triplet, gen_afpText_TextOrientation_triplet, gen_afpText_FontHorizontalScaleFactor_triplet, gen_afpText_FontDescriptorSpecification_triplet, gen_afpText_PresentationSpaceResetMixing_triplet, gen_afpText_PresentationSpaceMixingRules_triplet, gen_afpText_ResourceLocalIdentifier_triplet, gen_afpText_BeginImage_triplet, gen_afpText_EndImage_triplet, gen_afpText_ImageSize_triplet, gen_afpText_ImageEncoding_triplet, gen_afpText_BeginSegment_triplet, gen_afpText_EndSegment_triplet, gen_afpText_BeginTile_triplet, gen_afpText_EndTile_triplet, gen_afpText_BeginTransparencyMask_triplet, gen_afpText_EndTransparencyMask_triplet, gen_afpText_IDEStructure_triplet, gen_afpText_ExternalAlgorithm_triplet, gen_afpText_TilePosition_triplet, gen_afpText_IDESize_triplet, gen_afpText_ImageLUTID_triplet, gen_afpText_BandImage_triplet, gen_afpText_SetBiLevelImageColor_triplet, gen_afpText_IOCAFunctionSetIdentification_triplet, gen_afpText_TileSize_triplet, gen_afpText_TileSetColor_triplet, gen_afpText_ImageSubsampling_triplet, gen_afpText_SamplingRatios_triplet, gen_afpText_TileTOC_triplet, gen_afpText_ImageData_triplet, gen_afpText_BandImageData_triplet, gen_afpText_IncludeTile_triplet, gen_afpText_GBAR_triplet, gen_afpText_GBIMG_triplet, gen_afpText_GCBIMG_triplet, gen_afpText_FNNRG2_triplet, gen_afpText_BeginSegmentCommand_triplet, gen_afpText_EndSegmentCommand_triplet, gen_afpText_GCBOX_triplet, gen_afpText_GCHST_triplet, gen_afpText_GCCHST_triplet, gen_afpText_GCOMT_triplet, gen_afpText_GBOX_triplet, gen_afpText_GCFLT_triplet, gen_afpText_GFARC_triplet, gen_afpText_GCFARC_triplet, gen_afpText_GEAR_triplet, gen_afpText_GEIMG_triplet, gen_afpText_GEPROL_triplet, gen_afpText_GFLT_triplet, gen_afpText_GCLINE_triplet, gen_afpText_GMRK_triplet, gen_afpText_GCMRK_triplet, gen_afpText_GNOP1_triplet, gen_afpText_GPARC_triplet, gen_afpText_GIMD_triplet, gen_afpText_GLINE_triplet, gen_afpText_GRLINE_triplet, gen_afpText_GCRLINE_triplet, gen_afpText_GCPARC_triplet, gen_afpText_GSBMX_triplet, gen_afpText_GSCA_triplet, gen_afpText_GSCC_triplet, gen_afpText_GSCD_triplet, gen_afpText_GSGCH_triplet, gen_afpText_GSAP_triplet, gen_afpText_GSCOL_triplet, gen_afpText_GSCP_triplet, gen_afpText_GSECOL_triplet, gen_afpText_GSFLW_triplet, gen_afpText_GSLT_triplet, gen_afpText_GSCR_triplet, gen_afpText_GSCS_triplet, gen_afpText_GSCH_triplet, gen_afpText_GSMS_triplet, gen_afpText_GSMT_triplet, gen_afpText_GSMX_triplet, gen_afpText_GSPS_triplet, gen_afpText_GSPT_triplet, gen_afpText_GSLW_triplet, gen_afpText_GSMC_triplet, gen_afpText_GSMP_triplet, gen_afpText_GSLE_triplet, gen_afpText_GSLJ_triplet, gen_afpText_GCBEZ_triplet, gen_afpText_GCCBEZ_triplet, gen_afpText_GSPCOL_triplet, gen_afpText_DrawingOrderSubset_triplet, gen_afpText_TonerSaver_triplet, gen_afpText_ColorFidelity_triplet, gen_afpText_FontFidelity_triplet, gen_afpText_WindowSpecification_triplet, gen_afpText_FinishingFidelity_triplet, gen_afpText_CMRFidelity_triplet, gen_afpText_ObjectByteExtent_triplet, gen_afpText_ObjectByteOffset_triplet, gen_afpText_ObjectStructuredFieldExtent_triplet, gen_afpText_TextFidelity_triplet, gen_afpText_MediaFidelity_triplet, gen_afpText_ObjectOriginIdentifier_triplet, gen_afpText_LineDataObjectPositionMigration_triplet, gen_afpText_ColorManagementResourceDescriptor_triplet, gen_afpText_ObjectStructuredFieldOffset_triplet, gen_afpText_ObjectCount_triplet, gen_afpText_ExtendedResourceLocalIdentifier_triplet, gen_afpText_MetricAdjustment_triplet, gen_afpText_ExtensionFont_triplet, gen_afpText_ImageResolution_triplet, gen_afpText_ObjectContainerPresentationSpaceSize_triplet, gen_afpText_LocaleSelector_triplet, gen_afpText_FinishingOperation_triplet, gen_afpText_RenderingIntent_triplet, gen_afpText_FontCodedGraphicCharacterSetGlobalIdentifier_triplet, gen_afpText_PageOverlayConditionalProcessing_triplet, gen_afpText_ResourceUsageAttribute_triplet, gen_afpText_UP3iFinishingOperation_triplet, gen_afpText_DeviceAppearance_triplet, gen_afpText_ResourceObjectInclude_triplet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)