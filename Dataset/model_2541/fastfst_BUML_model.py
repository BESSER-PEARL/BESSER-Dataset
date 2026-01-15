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
fastfst_Section = Class(name="fastfst::Section")
fastfst_bEcho = Class(name="fastfst::bEcho")
fastfst_iADAMSPrep = Class(name="fastfst::iADAMSPrep")
fastfst_iAnalMode = Class(name="fastfst::iAnalMode")
fastfst_iNumBl = Class(name="fastfst::iNumBl")
fastfst_ModelFastfst = Class(name="fastfst::ModelFastfst")
fastfst_Header = Class(name="fastfst::Header")
fastfst_nTHSSBrDp = Class(name="fastfst::nTHSSBrDp")
fastfst_nTiDynBrk = Class(name="fastfst::nTiDynBrk")
fastfst_nTMax = Class(name="fastfst::nTMax")
fastfst_nDT = Class(name="fastfst::nDT")
fastfst_iYCMode = Class(name="fastfst::iYCMode")
fastfst_nTYCOn = Class(name="fastfst::nTYCOn")
fastfst_iPCMode = Class(name="fastfst::iPCMode")
fastfst_nTPCOn = Class(name="fastfst::nTPCOn")
fastfst_iVSContrl = Class(name="fastfst::iVSContrl")
fastfst_nVS_RtGnSp = Class(name="fastfst::nVS::RtGnSp")
fastfst_nVS_RtTq = Class(name="fastfst::nVS::RtTq")
fastfst_nVS_Rgn2K = Class(name="fastfst::nVS::Rgn2K")
fastfst_nVS_SlPc = Class(name="fastfst::nVS::SlPc")
fastfst_iGenModel = Class(name="fastfst::iGenModel")
fastfst_bGenTiStr = Class(name="fastfst::bGenTiStr")
fastfst_bGenTiStp = Class(name="fastfst::bGenTiStp")
fastfst_nSpdGenOn = Class(name="fastfst::nSpdGenOn")
fastfst_nTimGenOn = Class(name="fastfst::nTimGenOn")
fastfst_nTimGenOf = Class(name="fastfst::nTimGenOf")
fastfst_iHSSBrMode = Class(name="fastfst::iHSSBrMode")
fastfst_nTBDepISp_1_ = Class(name="fastfst::nTBDepISp::1::")
fastfst_nTTpBrDp_1_ = Class(name="fastfst::nTTpBrDp::1::")
fastfst_nTTpBrDp_2_ = Class(name="fastfst::nTTpBrDp::2::")
fastfst_nTTpBrDp_3_ = Class(name="fastfst::nTTpBrDp::3::")
fastfst_nNacYawF = Class(name="fastfst::nNacYawF")
fastfst_nTBDepISp_2_ = Class(name="fastfst::nTBDepISp::2::")
fastfst_nTBDepISp_3_ = Class(name="fastfst::nTBDepISp::3::")
fastfst_nTYawManS = Class(name="fastfst::nTYawManS")
fastfst_nTYawManE = Class(name="fastfst::nTYawManE")
fastfst_nTPitManS_1_ = Class(name="fastfst::nTPitManS::1::")
fastfst_nTPitManS_2_ = Class(name="fastfst::nTPitManS::2::")
fastfst_nTPitManS_3_ = Class(name="fastfst::nTPitManS::3::")
fastfst_nTPitManE_1_ = Class(name="fastfst::nTPitManE::1::")
fastfst_nBlPitch_3_ = Class(name="fastfst::nBlPitch::3::")
fastfst_nTPitManE_2_ = Class(name="fastfst::nTPitManE::2::")
fastfst_nTPitManE_3_ = Class(name="fastfst::nTPitManE::3::")
fastfst_nBlPitch_1_ = Class(name="fastfst::nBlPitch::1::")
fastfst_nBlPitch_2_ = Class(name="fastfst::nBlPitch::2::")
fastfst_nGravity = Class(name="fastfst::nGravity")
fastfst_nBlPitchF_1_ = Class(name="fastfst::nBlPitchF::1::")
fastfst_nBlPitchF_2_ = Class(name="fastfst::nBlPitchF::2::")
fastfst_nBlPitchF_3_ = Class(name="fastfst::nBlPitchF::3::")
fastfst_bTwFADOF2 = Class(name="fastfst::bTwFADOF2")
fastfst_bFlapDOF1 = Class(name="fastfst::bFlapDOF1")
fastfst_bFlapDOF2 = Class(name="fastfst::bFlapDOF2")
fastfst_bEdgeDOF = Class(name="fastfst::bEdgeDOF")
fastfst_bTeetDOF = Class(name="fastfst::bTeetDOF")
fastfst_bDrTrDOF = Class(name="fastfst::bDrTrDOF")
fastfst_bGenDOF = Class(name="fastfst::bGenDOF")
fastfst_bYawDOF = Class(name="fastfst::bYawDOF")
fastfst_bTwFADOF1 = Class(name="fastfst::bTwFADOF1")
fastfst_nAzimuth = Class(name="fastfst::nAzimuth")
fastfst_nRotSpeed = Class(name="fastfst::nRotSpeed")
fastfst_bTwSSDOF1 = Class(name="fastfst::bTwSSDOF1")
fastfst_bTwSSDOF2 = Class(name="fastfst::bTwSSDOF2")
fastfst_bCompAero = Class(name="fastfst::bCompAero")
fastfst_bCompNoise = Class(name="fastfst::bCompNoise")
fastfst_nOoPDefl = Class(name="fastfst::nOoPDefl")
fastfst_nIPDefl = Class(name="fastfst::nIPDefl")
fastfst_nTeetDefl = Class(name="fastfst::nTeetDefl")
fastfst_nNacYaw = Class(name="fastfst::nNacYaw")
fastfst_nTTDspFA = Class(name="fastfst::nTTDspFA")
fastfst_nTTDspSS = Class(name="fastfst::nTTDspSS")
fastfst_nTipRad = Class(name="fastfst::nTipRad")
fastfst_nHubRad = Class(name="fastfst::nHubRad")
fastfst_nPSpnElN = Class(name="fastfst::nPSpnElN")
fastfst_nUndSling = Class(name="fastfst::nUndSling")
fastfst_nNacCMzn = Class(name="fastfst::nNacCMzn")
fastfst_nHubCM = Class(name="fastfst::nHubCM")
fastfst_nOverHang = Class(name="fastfst::nOverHang")
fastfst_nTowerHt = Class(name="fastfst::nTowerHt")
fastfst_nTwr2Shft = Class(name="fastfst::nTwr2Shft")
fastfst_nTwrRBHt = Class(name="fastfst::nTwrRBHt")
fastfst_nShftTilt = Class(name="fastfst::nShftTilt")
fastfst_nDelta3 = Class(name="fastfst::nDelta3")
fastfst_nPreCone_1_ = Class(name="fastfst::nPreCone::1::")
fastfst_nPreCone_2_ = Class(name="fastfst::nPreCone::2::")
fastfst_nPreCone_3_ = Class(name="fastfst::nPreCone::3::")
fastfst_nAzimB1Up = Class(name="fastfst::nAzimB1Up")
fastfst_nNacCMxn = Class(name="fastfst::nNacCMxn")
fastfst_nNacCMyn = Class(name="fastfst::nNacCMyn")
fastfst_nNacMass = Class(name="fastfst::nNacMass")
fastfst_nHubMass = Class(name="fastfst::nHubMass")
fastfst_nTipMass_1_ = Class(name="fastfst::nTipMass::1::")
fastfst_nTipMass_2_ = Class(name="fastfst::nTipMass::2::")
fastfst_nTipMass_3_ = Class(name="fastfst::nTipMass::3::")
fastfst_nNacYIner = Class(name="fastfst::nNacYIner")
fastfst_nGenIner = Class(name="fastfst::nGenIner")
fastfst_nHubIner = Class(name="fastfst::nHubIner")
fastfst_nGBoxEff = Class(name="fastfst::nGBoxEff")
fastfst_nGenEff = Class(name="fastfst::nGenEff")
fastfst_nGBRatio = Class(name="fastfst::nGBRatio")
fastfst_nYawBrMass = Class(name="fastfst::nYawBrMass")
fastfst_bGBRevers = Class(name="fastfst::bGBRevers")
fastfst_nHSSBrTqF = Class(name="fastfst::nHSSBrTqF")
fastfst_nHSSBrDT = Class(name="fastfst::nHSSBrDT")
fastfst_fDynBrkFi = Class(name="fastfst::fDynBrkFi")
fastfst_nDTTorSpr = Class(name="fastfst::nDTTorSpr")
fastfst_nDTTorDmp = Class(name="fastfst::nDTTorDmp")
fastfst_nSIG_SlPc = Class(name="fastfst::nSIG::SlPc")
fastfst_nSIG_SySp = Class(name="fastfst::nSIG::SySp")
fastfst_nSIG_RtTq = Class(name="fastfst::nSIG::RtTq")
fastfst_nSIG_PORt = Class(name="fastfst::nSIG::PORt")
fastfst_fPtfmFile = Class(name="fastfst::fPtfmFile")
fastfst_nTEC_Freq = Class(name="fastfst::nTEC::Freq")
fastfst_nTEC_Npol = Class(name="fastfst::nTEC::Npol")
fastfst_nTEC_Sres = Class(name="fastfst::nTEC::Sres")
fastfst_nTEC_Rres = Class(name="fastfst::nTEC::Rres")
fastfst_nTEC_VLL = Class(name="fastfst::nTEC::VLL")
fastfst_nTEC_SLR = Class(name="fastfst::nTEC::SLR")
fastfst_nTEC_RLR = Class(name="fastfst::nTEC::RLR")
fastfst_nTEC_MR = Class(name="fastfst::nTEC::MR")
fastfst_iPtfmModel = Class(name="fastfst::iPtfmModel")
fastfst_iTwrNodes = Class(name="fastfst::iTwrNodes")
fastfst_fTwrFile = Class(name="fastfst::fTwrFile")
fastfst_nYawSpr = Class(name="fastfst::nYawSpr")
fastfst_nYawDamp = Class(name="fastfst::nYawDamp")
fastfst_nYawNeut = Class(name="fastfst::nYawNeut")
fastfst_bFurling = Class(name="fastfst::bFurling")
fastfst_fFurlFile = Class(name="fastfst::fFurlFile")
fastfst_iTeetMod = Class(name="fastfst::iTeetMod")
fastfst_nTeetDmpP = Class(name="fastfst::nTeetDmpP")
fastfst_nTeetDmp = Class(name="fastfst::nTeetDmp")
fastfst_nTeetCDmp = Class(name="fastfst::nTeetCDmp")
fastfst_nTeetSStP = Class(name="fastfst::nTeetSStP")
fastfst_nTeetHStP = Class(name="fastfst::nTeetHStP")
fastfst_nTeetSSSp = Class(name="fastfst::nTeetSSSp")
fastfst_nTeetHSSp = Class(name="fastfst::nTeetHSSp")
fastfst_nTBDrConN = Class(name="fastfst::nTBDrConN")
fastfst_nTBDrConD = Class(name="fastfst::nTBDrConD")
fastfst_nTpBrDT = Class(name="fastfst::nTpBrDT")
fastfst_fBldFile_1_ = Class(name="fastfst::fBldFile::1::")
fastfst_fBldFile_2_ = Class(name="fastfst::fBldFile::2::")
fastfst_fBldFile_3_ = Class(name="fastfst::fBldFile::3::")
fastfst_fADFile = Class(name="fastfst::fADFile")
fastfst_fNoiseFile = Class(name="fastfst::fNoiseFile")
fastfst_fADAMSFile = Class(name="fastfst::fADAMSFile")
fastfst_fLinFile = Class(name="fastfst::fLinFile")
fastfst_bSumPrint = Class(name="fastfst::bSumPrint")
fastfst_bOutFileFmt = Class(name="fastfst::bOutFileFmt")
fastfst_bTabDelim = Class(name="fastfst::bTabDelim")
fastfst_sOutFmt = Class(name="fastfst::sOutFmt")
fastfst_nTStart = Class(name="fastfst::nTStart")
fastfst_iDecFact = Class(name="fastfst::iDecFact")
fastfst_nSttsTime = Class(name="fastfst::nSttsTime")
fastfst_nNcIMUxn = Class(name="fastfst::nNcIMUxn")
fastfst_nNcIMUyn = Class(name="fastfst::nNcIMUyn")
fastfst_nNcIMUzn = Class(name="fastfst::nNcIMUzn")
fastfst_nShftGagL = Class(name="fastfst::nShftGagL")
fastfst_iNTwGages = Class(name="fastfst::iNTwGages")
fastfst_aTwrGagNd = Class(name="fastfst::aTwrGagNd")
fastfst_iNBlGages = Class(name="fastfst::iNBlGages")
fastfst_aBldGagNd = Class(name="fastfst::aBldGagNd")
fastfst_vOutList = Class(name="fastfst::vOutList")

# fastfst_Section class attributes and methods
fastfst_Section_name: Property = Property(name="name", type=StringType)
fastfst_Section.attributes={fastfst_Section_name}

# fastfst_bEcho class attributes and methods
fastfst_bEcho_value: Property = Property(name="value", type=BooleanType)
fastfst_bEcho_name: Property = Property(name="name", type=StringType)
fastfst_bEcho.attributes={fastfst_bEcho_name, fastfst_bEcho_value}

# fastfst_iADAMSPrep class attributes and methods
fastfst_iADAMSPrep_value: Property = Property(name="value", type=IntegerType)
fastfst_iADAMSPrep_name: Property = Property(name="name", type=StringType)
fastfst_iADAMSPrep.attributes={fastfst_iADAMSPrep_value, fastfst_iADAMSPrep_name}

# fastfst_iAnalMode class attributes and methods
fastfst_iAnalMode_value: Property = Property(name="value", type=IntegerType)
fastfst_iAnalMode_name: Property = Property(name="name", type=StringType)
fastfst_iAnalMode.attributes={fastfst_iAnalMode_name, fastfst_iAnalMode_value}

# fastfst_iNumBl class attributes and methods
fastfst_iNumBl_value: Property = Property(name="value", type=IntegerType)
fastfst_iNumBl_name: Property = Property(name="name", type=StringType)
fastfst_iNumBl.attributes={fastfst_iNumBl_value, fastfst_iNumBl_name}

# fastfst_ModelFastfst class attributes and methods

# fastfst_Header class attributes and methods
fastfst_Header_rows: Property = Property(name="rows", type=StringType)
fastfst_Header.attributes={fastfst_Header_rows}

# fastfst_nTHSSBrDp class attributes and methods
fastfst_nTHSSBrDp_value: Property = Property(name="value", type=FloatType)
fastfst_nTHSSBrDp_name: Property = Property(name="name", type=StringType)
fastfst_nTHSSBrDp.attributes={fastfst_nTHSSBrDp_name, fastfst_nTHSSBrDp_value}

# fastfst_nTiDynBrk class attributes and methods
fastfst_nTiDynBrk_value: Property = Property(name="value", type=FloatType)
fastfst_nTiDynBrk_name: Property = Property(name="name", type=StringType)
fastfst_nTiDynBrk.attributes={fastfst_nTiDynBrk_value, fastfst_nTiDynBrk_name}

# fastfst_nTMax class attributes and methods
fastfst_nTMax_value: Property = Property(name="value", type=FloatType)
fastfst_nTMax_name: Property = Property(name="name", type=StringType)
fastfst_nTMax.attributes={fastfst_nTMax_value, fastfst_nTMax_name}

# fastfst_nDT class attributes and methods
fastfst_nDT_value: Property = Property(name="value", type=FloatType)
fastfst_nDT_name: Property = Property(name="name", type=StringType)
fastfst_nDT.attributes={fastfst_nDT_value, fastfst_nDT_name}

# fastfst_iYCMode class attributes and methods
fastfst_iYCMode_value: Property = Property(name="value", type=IntegerType)
fastfst_iYCMode_name: Property = Property(name="name", type=StringType)
fastfst_iYCMode.attributes={fastfst_iYCMode_value, fastfst_iYCMode_name}

# fastfst_nTYCOn class attributes and methods
fastfst_nTYCOn_value: Property = Property(name="value", type=FloatType)
fastfst_nTYCOn_name: Property = Property(name="name", type=StringType)
fastfst_nTYCOn.attributes={fastfst_nTYCOn_name, fastfst_nTYCOn_value}

# fastfst_iPCMode class attributes and methods
fastfst_iPCMode_value: Property = Property(name="value", type=IntegerType)
fastfst_iPCMode_name: Property = Property(name="name", type=StringType)
fastfst_iPCMode.attributes={fastfst_iPCMode_name, fastfst_iPCMode_value}

# fastfst_nTPCOn class attributes and methods
fastfst_nTPCOn_value: Property = Property(name="value", type=FloatType)
fastfst_nTPCOn_name: Property = Property(name="name", type=StringType)
fastfst_nTPCOn.attributes={fastfst_nTPCOn_value, fastfst_nTPCOn_name}

# fastfst_iVSContrl class attributes and methods
fastfst_iVSContrl_value: Property = Property(name="value", type=IntegerType)
fastfst_iVSContrl_name: Property = Property(name="name", type=StringType)
fastfst_iVSContrl.attributes={fastfst_iVSContrl_value, fastfst_iVSContrl_name}

# fastfst_nVS_RtGnSp class attributes and methods
fastfst_nVS_RtGnSp_value: Property = Property(name="value", type=FloatType)
fastfst_nVS_RtGnSp_name: Property = Property(name="name", type=StringType)
fastfst_nVS_RtGnSp.attributes={fastfst_nVS_RtGnSp_value, fastfst_nVS_RtGnSp_name}

# fastfst_nVS_RtTq class attributes and methods
fastfst_nVS_RtTq_value: Property = Property(name="value", type=FloatType)
fastfst_nVS_RtTq_name: Property = Property(name="name", type=StringType)
fastfst_nVS_RtTq.attributes={fastfst_nVS_RtTq_value, fastfst_nVS_RtTq_name}

# fastfst_nVS_Rgn2K class attributes and methods
fastfst_nVS_Rgn2K_value: Property = Property(name="value", type=FloatType)
fastfst_nVS_Rgn2K_name: Property = Property(name="name", type=StringType)
fastfst_nVS_Rgn2K.attributes={fastfst_nVS_Rgn2K_name, fastfst_nVS_Rgn2K_value}

# fastfst_nVS_SlPc class attributes and methods
fastfst_nVS_SlPc_value: Property = Property(name="value", type=FloatType)
fastfst_nVS_SlPc_name: Property = Property(name="name", type=StringType)
fastfst_nVS_SlPc.attributes={fastfst_nVS_SlPc_name, fastfst_nVS_SlPc_value}

# fastfst_iGenModel class attributes and methods
fastfst_iGenModel_value: Property = Property(name="value", type=IntegerType)
fastfst_iGenModel_name: Property = Property(name="name", type=StringType)
fastfst_iGenModel.attributes={fastfst_iGenModel_name, fastfst_iGenModel_value}

# fastfst_bGenTiStr class attributes and methods
fastfst_bGenTiStr_value: Property = Property(name="value", type=BooleanType)
fastfst_bGenTiStr_name: Property = Property(name="name", type=StringType)
fastfst_bGenTiStr.attributes={fastfst_bGenTiStr_name, fastfst_bGenTiStr_value}

# fastfst_bGenTiStp class attributes and methods
fastfst_bGenTiStp_value: Property = Property(name="value", type=BooleanType)
fastfst_bGenTiStp_name: Property = Property(name="name", type=StringType)
fastfst_bGenTiStp.attributes={fastfst_bGenTiStp_value, fastfst_bGenTiStp_name}

# fastfst_nSpdGenOn class attributes and methods
fastfst_nSpdGenOn_value: Property = Property(name="value", type=FloatType)
fastfst_nSpdGenOn_name: Property = Property(name="name", type=StringType)
fastfst_nSpdGenOn.attributes={fastfst_nSpdGenOn_name, fastfst_nSpdGenOn_value}

# fastfst_nTimGenOn class attributes and methods
fastfst_nTimGenOn_value: Property = Property(name="value", type=FloatType)
fastfst_nTimGenOn_name: Property = Property(name="name", type=StringType)
fastfst_nTimGenOn.attributes={fastfst_nTimGenOn_name, fastfst_nTimGenOn_value}

# fastfst_nTimGenOf class attributes and methods
fastfst_nTimGenOf_value: Property = Property(name="value", type=FloatType)
fastfst_nTimGenOf_name: Property = Property(name="name", type=StringType)
fastfst_nTimGenOf.attributes={fastfst_nTimGenOf_value, fastfst_nTimGenOf_name}

# fastfst_iHSSBrMode class attributes and methods
fastfst_iHSSBrMode_value: Property = Property(name="value", type=IntegerType)
fastfst_iHSSBrMode_name: Property = Property(name="name", type=StringType)
fastfst_iHSSBrMode.attributes={fastfst_iHSSBrMode_name, fastfst_iHSSBrMode_value}

# fastfst_nTBDepISp_1_ class attributes and methods
fastfst_nTBDepISp_1__value: Property = Property(name="value", type=FloatType)
fastfst_nTBDepISp_1__name: Property = Property(name="name", type=StringType)
fastfst_nTBDepISp_1_.attributes={fastfst_nTBDepISp_1__value, fastfst_nTBDepISp_1__name}

# fastfst_nTTpBrDp_1_ class attributes and methods
fastfst_nTTpBrDp_1__value: Property = Property(name="value", type=FloatType)
fastfst_nTTpBrDp_1__name: Property = Property(name="name", type=StringType)
fastfst_nTTpBrDp_1_.attributes={fastfst_nTTpBrDp_1__value, fastfst_nTTpBrDp_1__name}

# fastfst_nTTpBrDp_2_ class attributes and methods
fastfst_nTTpBrDp_2__value: Property = Property(name="value", type=FloatType)
fastfst_nTTpBrDp_2__name: Property = Property(name="name", type=StringType)
fastfst_nTTpBrDp_2_.attributes={fastfst_nTTpBrDp_2__value, fastfst_nTTpBrDp_2__name}

# fastfst_nTTpBrDp_3_ class attributes and methods
fastfst_nTTpBrDp_3__value: Property = Property(name="value", type=FloatType)
fastfst_nTTpBrDp_3__name: Property = Property(name="name", type=StringType)
fastfst_nTTpBrDp_3_.attributes={fastfst_nTTpBrDp_3__name, fastfst_nTTpBrDp_3__value}

# fastfst_nNacYawF class attributes and methods
fastfst_nNacYawF_value: Property = Property(name="value", type=FloatType)
fastfst_nNacYawF_name: Property = Property(name="name", type=StringType)
fastfst_nNacYawF.attributes={fastfst_nNacYawF_name, fastfst_nNacYawF_value}

# fastfst_nTBDepISp_2_ class attributes and methods
fastfst_nTBDepISp_2__value: Property = Property(name="value", type=FloatType)
fastfst_nTBDepISp_2__name: Property = Property(name="name", type=StringType)
fastfst_nTBDepISp_2_.attributes={fastfst_nTBDepISp_2__value, fastfst_nTBDepISp_2__name}

# fastfst_nTBDepISp_3_ class attributes and methods
fastfst_nTBDepISp_3__value: Property = Property(name="value", type=FloatType)
fastfst_nTBDepISp_3__name: Property = Property(name="name", type=StringType)
fastfst_nTBDepISp_3_.attributes={fastfst_nTBDepISp_3__name, fastfst_nTBDepISp_3__value}

# fastfst_nTYawManS class attributes and methods
fastfst_nTYawManS_value: Property = Property(name="value", type=FloatType)
fastfst_nTYawManS_name: Property = Property(name="name", type=StringType)
fastfst_nTYawManS.attributes={fastfst_nTYawManS_value, fastfst_nTYawManS_name}

# fastfst_nTYawManE class attributes and methods
fastfst_nTYawManE_value: Property = Property(name="value", type=FloatType)
fastfst_nTYawManE_name: Property = Property(name="name", type=StringType)
fastfst_nTYawManE.attributes={fastfst_nTYawManE_value, fastfst_nTYawManE_name}

# fastfst_nTPitManS_1_ class attributes and methods
fastfst_nTPitManS_1__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManS_1__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManS_1_.attributes={fastfst_nTPitManS_1__value, fastfst_nTPitManS_1__name}

# fastfst_nTPitManS_2_ class attributes and methods
fastfst_nTPitManS_2__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManS_2__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManS_2_.attributes={fastfst_nTPitManS_2__name, fastfst_nTPitManS_2__value}

# fastfst_nTPitManS_3_ class attributes and methods
fastfst_nTPitManS_3__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManS_3__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManS_3_.attributes={fastfst_nTPitManS_3__name, fastfst_nTPitManS_3__value}

# fastfst_nTPitManE_1_ class attributes and methods
fastfst_nTPitManE_1__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManE_1__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManE_1_.attributes={fastfst_nTPitManE_1__value, fastfst_nTPitManE_1__name}

# fastfst_nBlPitch_3_ class attributes and methods
fastfst_nBlPitch_3__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitch_3__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitch_3_.attributes={fastfst_nBlPitch_3__name, fastfst_nBlPitch_3__value}

# fastfst_nTPitManE_2_ class attributes and methods
fastfst_nTPitManE_2__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManE_2__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManE_2_.attributes={fastfst_nTPitManE_2__name, fastfst_nTPitManE_2__value}

# fastfst_nTPitManE_3_ class attributes and methods
fastfst_nTPitManE_3__value: Property = Property(name="value", type=FloatType)
fastfst_nTPitManE_3__name: Property = Property(name="name", type=StringType)
fastfst_nTPitManE_3_.attributes={fastfst_nTPitManE_3__value, fastfst_nTPitManE_3__name}

# fastfst_nBlPitch_1_ class attributes and methods
fastfst_nBlPitch_1__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitch_1__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitch_1_.attributes={fastfst_nBlPitch_1__value, fastfst_nBlPitch_1__name}

# fastfst_nBlPitch_2_ class attributes and methods
fastfst_nBlPitch_2__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitch_2__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitch_2_.attributes={fastfst_nBlPitch_2__name, fastfst_nBlPitch_2__value}

# fastfst_nGravity class attributes and methods
fastfst_nGravity_value: Property = Property(name="value", type=FloatType)
fastfst_nGravity_name: Property = Property(name="name", type=StringType)
fastfst_nGravity.attributes={fastfst_nGravity_name, fastfst_nGravity_value}

# fastfst_nBlPitchF_1_ class attributes and methods
fastfst_nBlPitchF_1__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitchF_1__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitchF_1_.attributes={fastfst_nBlPitchF_1__value, fastfst_nBlPitchF_1__name}

# fastfst_nBlPitchF_2_ class attributes and methods
fastfst_nBlPitchF_2__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitchF_2__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitchF_2_.attributes={fastfst_nBlPitchF_2__value, fastfst_nBlPitchF_2__name}

# fastfst_nBlPitchF_3_ class attributes and methods
fastfst_nBlPitchF_3__name: Property = Property(name="name", type=StringType)
fastfst_nBlPitchF_3__value: Property = Property(name="value", type=FloatType)
fastfst_nBlPitchF_3_.attributes={fastfst_nBlPitchF_3__value, fastfst_nBlPitchF_3__name}

# fastfst_bTwFADOF2 class attributes and methods
fastfst_bTwFADOF2_value: Property = Property(name="value", type=BooleanType)
fastfst_bTwFADOF2_name: Property = Property(name="name", type=StringType)
fastfst_bTwFADOF2.attributes={fastfst_bTwFADOF2_value, fastfst_bTwFADOF2_name}

# fastfst_bFlapDOF1 class attributes and methods
fastfst_bFlapDOF1_value: Property = Property(name="value", type=BooleanType)
fastfst_bFlapDOF1_name: Property = Property(name="name", type=StringType)
fastfst_bFlapDOF1.attributes={fastfst_bFlapDOF1_name, fastfst_bFlapDOF1_value}

# fastfst_bFlapDOF2 class attributes and methods
fastfst_bFlapDOF2_value: Property = Property(name="value", type=BooleanType)
fastfst_bFlapDOF2_name: Property = Property(name="name", type=StringType)
fastfst_bFlapDOF2.attributes={fastfst_bFlapDOF2_value, fastfst_bFlapDOF2_name}

# fastfst_bEdgeDOF class attributes and methods
fastfst_bEdgeDOF_value: Property = Property(name="value", type=BooleanType)
fastfst_bEdgeDOF_name: Property = Property(name="name", type=StringType)
fastfst_bEdgeDOF.attributes={fastfst_bEdgeDOF_name, fastfst_bEdgeDOF_value}

# fastfst_bTeetDOF class attributes and methods
fastfst_bTeetDOF_value: Property = Property(name="value", type=BooleanType)
fastfst_bTeetDOF_name: Property = Property(name="name", type=StringType)
fastfst_bTeetDOF.attributes={fastfst_bTeetDOF_value, fastfst_bTeetDOF_name}

# fastfst_bDrTrDOF class attributes and methods
fastfst_bDrTrDOF_value: Property = Property(name="value", type=BooleanType)
fastfst_bDrTrDOF_name: Property = Property(name="name", type=StringType)
fastfst_bDrTrDOF.attributes={fastfst_bDrTrDOF_name, fastfst_bDrTrDOF_value}

# fastfst_bGenDOF class attributes and methods
fastfst_bGenDOF_value: Property = Property(name="value", type=BooleanType)
fastfst_bGenDOF_name: Property = Property(name="name", type=StringType)
fastfst_bGenDOF.attributes={fastfst_bGenDOF_name, fastfst_bGenDOF_value}

# fastfst_bYawDOF class attributes and methods
fastfst_bYawDOF_value: Property = Property(name="value", type=BooleanType)
fastfst_bYawDOF_name: Property = Property(name="name", type=StringType)
fastfst_bYawDOF.attributes={fastfst_bYawDOF_name, fastfst_bYawDOF_value}

# fastfst_bTwFADOF1 class attributes and methods
fastfst_bTwFADOF1_value: Property = Property(name="value", type=BooleanType)
fastfst_bTwFADOF1_name: Property = Property(name="name", type=StringType)
fastfst_bTwFADOF1.attributes={fastfst_bTwFADOF1_name, fastfst_bTwFADOF1_value}

# fastfst_nAzimuth class attributes and methods
fastfst_nAzimuth_value: Property = Property(name="value", type=FloatType)
fastfst_nAzimuth_name: Property = Property(name="name", type=StringType)
fastfst_nAzimuth.attributes={fastfst_nAzimuth_name, fastfst_nAzimuth_value}

# fastfst_nRotSpeed class attributes and methods
fastfst_nRotSpeed_value: Property = Property(name="value", type=FloatType)
fastfst_nRotSpeed_name: Property = Property(name="name", type=StringType)
fastfst_nRotSpeed.attributes={fastfst_nRotSpeed_value, fastfst_nRotSpeed_name}

# fastfst_bTwSSDOF1 class attributes and methods
fastfst_bTwSSDOF1_value: Property = Property(name="value", type=BooleanType)
fastfst_bTwSSDOF1_name: Property = Property(name="name", type=StringType)
fastfst_bTwSSDOF1.attributes={fastfst_bTwSSDOF1_name, fastfst_bTwSSDOF1_value}

# fastfst_bTwSSDOF2 class attributes and methods
fastfst_bTwSSDOF2_value: Property = Property(name="value", type=BooleanType)
fastfst_bTwSSDOF2_name: Property = Property(name="name", type=StringType)
fastfst_bTwSSDOF2.attributes={fastfst_bTwSSDOF2_value, fastfst_bTwSSDOF2_name}

# fastfst_bCompAero class attributes and methods
fastfst_bCompAero_value: Property = Property(name="value", type=BooleanType)
fastfst_bCompAero_name: Property = Property(name="name", type=StringType)
fastfst_bCompAero.attributes={fastfst_bCompAero_value, fastfst_bCompAero_name}

# fastfst_bCompNoise class attributes and methods
fastfst_bCompNoise_value: Property = Property(name="value", type=BooleanType)
fastfst_bCompNoise_name: Property = Property(name="name", type=StringType)
fastfst_bCompNoise.attributes={fastfst_bCompNoise_name, fastfst_bCompNoise_value}

# fastfst_nOoPDefl class attributes and methods
fastfst_nOoPDefl_value: Property = Property(name="value", type=FloatType)
fastfst_nOoPDefl_name: Property = Property(name="name", type=StringType)
fastfst_nOoPDefl.attributes={fastfst_nOoPDefl_name, fastfst_nOoPDefl_value}

# fastfst_nIPDefl class attributes and methods
fastfst_nIPDefl_value: Property = Property(name="value", type=FloatType)
fastfst_nIPDefl_name: Property = Property(name="name", type=StringType)
fastfst_nIPDefl.attributes={fastfst_nIPDefl_value, fastfst_nIPDefl_name}

# fastfst_nTeetDefl class attributes and methods
fastfst_nTeetDefl_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetDefl_name: Property = Property(name="name", type=StringType)
fastfst_nTeetDefl.attributes={fastfst_nTeetDefl_value, fastfst_nTeetDefl_name}

# fastfst_nNacYaw class attributes and methods
fastfst_nNacYaw_value: Property = Property(name="value", type=FloatType)
fastfst_nNacYaw_name: Property = Property(name="name", type=StringType)
fastfst_nNacYaw.attributes={fastfst_nNacYaw_value, fastfst_nNacYaw_name}

# fastfst_nTTDspFA class attributes and methods
fastfst_nTTDspFA_value: Property = Property(name="value", type=FloatType)
fastfst_nTTDspFA_name: Property = Property(name="name", type=StringType)
fastfst_nTTDspFA.attributes={fastfst_nTTDspFA_value, fastfst_nTTDspFA_name}

# fastfst_nTTDspSS class attributes and methods
fastfst_nTTDspSS_value: Property = Property(name="value", type=FloatType)
fastfst_nTTDspSS_name: Property = Property(name="name", type=StringType)
fastfst_nTTDspSS.attributes={fastfst_nTTDspSS_value, fastfst_nTTDspSS_name}

# fastfst_nTipRad class attributes and methods
fastfst_nTipRad_value: Property = Property(name="value", type=FloatType)
fastfst_nTipRad_name: Property = Property(name="name", type=StringType)
fastfst_nTipRad.attributes={fastfst_nTipRad_name, fastfst_nTipRad_value}

# fastfst_nHubRad class attributes and methods
fastfst_nHubRad_value: Property = Property(name="value", type=FloatType)
fastfst_nHubRad_name: Property = Property(name="name", type=StringType)
fastfst_nHubRad.attributes={fastfst_nHubRad_name, fastfst_nHubRad_value}

# fastfst_nPSpnElN class attributes and methods
fastfst_nPSpnElN_value: Property = Property(name="value", type=IntegerType)
fastfst_nPSpnElN_name: Property = Property(name="name", type=StringType)
fastfst_nPSpnElN.attributes={fastfst_nPSpnElN_name, fastfst_nPSpnElN_value}

# fastfst_nUndSling class attributes and methods
fastfst_nUndSling_value: Property = Property(name="value", type=FloatType)
fastfst_nUndSling_name: Property = Property(name="name", type=StringType)
fastfst_nUndSling.attributes={fastfst_nUndSling_value, fastfst_nUndSling_name}

# fastfst_nNacCMzn class attributes and methods
fastfst_nNacCMzn_value: Property = Property(name="value", type=FloatType)
fastfst_nNacCMzn_name: Property = Property(name="name", type=StringType)
fastfst_nNacCMzn.attributes={fastfst_nNacCMzn_name, fastfst_nNacCMzn_value}

# fastfst_nHubCM class attributes and methods
fastfst_nHubCM_value: Property = Property(name="value", type=FloatType)
fastfst_nHubCM_name: Property = Property(name="name", type=StringType)
fastfst_nHubCM.attributes={fastfst_nHubCM_value, fastfst_nHubCM_name}

# fastfst_nOverHang class attributes and methods
fastfst_nOverHang_name: Property = Property(name="name", type=StringType)
fastfst_nOverHang_value: Property = Property(name="value", type=FloatType)
fastfst_nOverHang.attributes={fastfst_nOverHang_name, fastfst_nOverHang_value}

# fastfst_nTowerHt class attributes and methods
fastfst_nTowerHt_value: Property = Property(name="value", type=FloatType)
fastfst_nTowerHt_name: Property = Property(name="name", type=StringType)
fastfst_nTowerHt.attributes={fastfst_nTowerHt_value, fastfst_nTowerHt_name}

# fastfst_nTwr2Shft class attributes and methods
fastfst_nTwr2Shft_value: Property = Property(name="value", type=FloatType)
fastfst_nTwr2Shft_name: Property = Property(name="name", type=StringType)
fastfst_nTwr2Shft.attributes={fastfst_nTwr2Shft_value, fastfst_nTwr2Shft_name}

# fastfst_nTwrRBHt class attributes and methods
fastfst_nTwrRBHt_value: Property = Property(name="value", type=FloatType)
fastfst_nTwrRBHt_name: Property = Property(name="name", type=StringType)
fastfst_nTwrRBHt.attributes={fastfst_nTwrRBHt_name, fastfst_nTwrRBHt_value}

# fastfst_nShftTilt class attributes and methods
fastfst_nShftTilt_value: Property = Property(name="value", type=FloatType)
fastfst_nShftTilt_name: Property = Property(name="name", type=StringType)
fastfst_nShftTilt.attributes={fastfst_nShftTilt_name, fastfst_nShftTilt_value}

# fastfst_nDelta3 class attributes and methods
fastfst_nDelta3_value: Property = Property(name="value", type=FloatType)
fastfst_nDelta3_name: Property = Property(name="name", type=StringType)
fastfst_nDelta3.attributes={fastfst_nDelta3_name, fastfst_nDelta3_value}

# fastfst_nPreCone_1_ class attributes and methods
fastfst_nPreCone_1__value: Property = Property(name="value", type=FloatType)
fastfst_nPreCone_1__name: Property = Property(name="name", type=StringType)
fastfst_nPreCone_1_.attributes={fastfst_nPreCone_1__value, fastfst_nPreCone_1__name}

# fastfst_nPreCone_2_ class attributes and methods
fastfst_nPreCone_2__value: Property = Property(name="value", type=FloatType)
fastfst_nPreCone_2__name: Property = Property(name="name", type=StringType)
fastfst_nPreCone_2_.attributes={fastfst_nPreCone_2__name, fastfst_nPreCone_2__value}

# fastfst_nPreCone_3_ class attributes and methods
fastfst_nPreCone_3__value: Property = Property(name="value", type=FloatType)
fastfst_nPreCone_3__name: Property = Property(name="name", type=StringType)
fastfst_nPreCone_3_.attributes={fastfst_nPreCone_3__value, fastfst_nPreCone_3__name}

# fastfst_nAzimB1Up class attributes and methods
fastfst_nAzimB1Up_value: Property = Property(name="value", type=FloatType)
fastfst_nAzimB1Up_name: Property = Property(name="name", type=StringType)
fastfst_nAzimB1Up.attributes={fastfst_nAzimB1Up_name, fastfst_nAzimB1Up_value}

# fastfst_nNacCMxn class attributes and methods
fastfst_nNacCMxn_value: Property = Property(name="value", type=FloatType)
fastfst_nNacCMxn_name: Property = Property(name="name", type=StringType)
fastfst_nNacCMxn.attributes={fastfst_nNacCMxn_name, fastfst_nNacCMxn_value}

# fastfst_nNacCMyn class attributes and methods
fastfst_nNacCMyn_value: Property = Property(name="value", type=FloatType)
fastfst_nNacCMyn_name: Property = Property(name="name", type=StringType)
fastfst_nNacCMyn.attributes={fastfst_nNacCMyn_value, fastfst_nNacCMyn_name}

# fastfst_nNacMass class attributes and methods
fastfst_nNacMass_value: Property = Property(name="value", type=FloatType)
fastfst_nNacMass_name: Property = Property(name="name", type=StringType)
fastfst_nNacMass.attributes={fastfst_nNacMass_value, fastfst_nNacMass_name}

# fastfst_nHubMass class attributes and methods
fastfst_nHubMass_value: Property = Property(name="value", type=FloatType)
fastfst_nHubMass_name: Property = Property(name="name", type=StringType)
fastfst_nHubMass.attributes={fastfst_nHubMass_value, fastfst_nHubMass_name}

# fastfst_nTipMass_1_ class attributes and methods
fastfst_nTipMass_1__value: Property = Property(name="value", type=FloatType)
fastfst_nTipMass_1__name: Property = Property(name="name", type=StringType)
fastfst_nTipMass_1_.attributes={fastfst_nTipMass_1__name, fastfst_nTipMass_1__value}

# fastfst_nTipMass_2_ class attributes and methods
fastfst_nTipMass_2__value: Property = Property(name="value", type=FloatType)
fastfst_nTipMass_2__name: Property = Property(name="name", type=StringType)
fastfst_nTipMass_2_.attributes={fastfst_nTipMass_2__name, fastfst_nTipMass_2__value}

# fastfst_nTipMass_3_ class attributes and methods
fastfst_nTipMass_3__value: Property = Property(name="value", type=FloatType)
fastfst_nTipMass_3__name: Property = Property(name="name", type=StringType)
fastfst_nTipMass_3_.attributes={fastfst_nTipMass_3__name, fastfst_nTipMass_3__value}

# fastfst_nNacYIner class attributes and methods
fastfst_nNacYIner_value: Property = Property(name="value", type=FloatType)
fastfst_nNacYIner_name: Property = Property(name="name", type=StringType)
fastfst_nNacYIner.attributes={fastfst_nNacYIner_value, fastfst_nNacYIner_name}

# fastfst_nGenIner class attributes and methods
fastfst_nGenIner_value: Property = Property(name="value", type=FloatType)
fastfst_nGenIner_name: Property = Property(name="name", type=StringType)
fastfst_nGenIner.attributes={fastfst_nGenIner_value, fastfst_nGenIner_name}

# fastfst_nHubIner class attributes and methods
fastfst_nHubIner_value: Property = Property(name="value", type=FloatType)
fastfst_nHubIner_name: Property = Property(name="name", type=StringType)
fastfst_nHubIner.attributes={fastfst_nHubIner_name, fastfst_nHubIner_value}

# fastfst_nGBoxEff class attributes and methods
fastfst_nGBoxEff_value: Property = Property(name="value", type=FloatType)
fastfst_nGBoxEff_name: Property = Property(name="name", type=StringType)
fastfst_nGBoxEff.attributes={fastfst_nGBoxEff_name, fastfst_nGBoxEff_value}

# fastfst_nGenEff class attributes and methods
fastfst_nGenEff_value: Property = Property(name="value", type=FloatType)
fastfst_nGenEff_name: Property = Property(name="name", type=StringType)
fastfst_nGenEff.attributes={fastfst_nGenEff_name, fastfst_nGenEff_value}

# fastfst_nGBRatio class attributes and methods
fastfst_nGBRatio_value: Property = Property(name="value", type=FloatType)
fastfst_nGBRatio_name: Property = Property(name="name", type=StringType)
fastfst_nGBRatio.attributes={fastfst_nGBRatio_name, fastfst_nGBRatio_value}

# fastfst_nYawBrMass class attributes and methods
fastfst_nYawBrMass_value: Property = Property(name="value", type=FloatType)
fastfst_nYawBrMass_name: Property = Property(name="name", type=StringType)
fastfst_nYawBrMass.attributes={fastfst_nYawBrMass_value, fastfst_nYawBrMass_name}

# fastfst_bGBRevers class attributes and methods
fastfst_bGBRevers_value: Property = Property(name="value", type=BooleanType)
fastfst_bGBRevers_name: Property = Property(name="name", type=StringType)
fastfst_bGBRevers.attributes={fastfst_bGBRevers_name, fastfst_bGBRevers_value}

# fastfst_nHSSBrTqF class attributes and methods
fastfst_nHSSBrTqF_value: Property = Property(name="value", type=FloatType)
fastfst_nHSSBrTqF_name: Property = Property(name="name", type=StringType)
fastfst_nHSSBrTqF.attributes={fastfst_nHSSBrTqF_value, fastfst_nHSSBrTqF_name}

# fastfst_nHSSBrDT class attributes and methods
fastfst_nHSSBrDT_value: Property = Property(name="value", type=FloatType)
fastfst_nHSSBrDT_name: Property = Property(name="name", type=StringType)
fastfst_nHSSBrDT.attributes={fastfst_nHSSBrDT_name, fastfst_nHSSBrDT_value}

# fastfst_fDynBrkFi class attributes and methods
fastfst_fDynBrkFi_value: Property = Property(name="value", type=StringType)
fastfst_fDynBrkFi_name: Property = Property(name="name", type=StringType)
fastfst_fDynBrkFi.attributes={fastfst_fDynBrkFi_name, fastfst_fDynBrkFi_value}

# fastfst_nDTTorSpr class attributes and methods
fastfst_nDTTorSpr_value: Property = Property(name="value", type=FloatType)
fastfst_nDTTorSpr_name: Property = Property(name="name", type=StringType)
fastfst_nDTTorSpr.attributes={fastfst_nDTTorSpr_value, fastfst_nDTTorSpr_name}

# fastfst_nDTTorDmp class attributes and methods
fastfst_nDTTorDmp_value: Property = Property(name="value", type=FloatType)
fastfst_nDTTorDmp_name: Property = Property(name="name", type=StringType)
fastfst_nDTTorDmp.attributes={fastfst_nDTTorDmp_value, fastfst_nDTTorDmp_name}

# fastfst_nSIG_SlPc class attributes and methods
fastfst_nSIG_SlPc_value: Property = Property(name="value", type=FloatType)
fastfst_nSIG_SlPc_name: Property = Property(name="name", type=StringType)
fastfst_nSIG_SlPc.attributes={fastfst_nSIG_SlPc_name, fastfst_nSIG_SlPc_value}

# fastfst_nSIG_SySp class attributes and methods
fastfst_nSIG_SySp_value: Property = Property(name="value", type=FloatType)
fastfst_nSIG_SySp_name: Property = Property(name="name", type=StringType)
fastfst_nSIG_SySp.attributes={fastfst_nSIG_SySp_value, fastfst_nSIG_SySp_name}

# fastfst_nSIG_RtTq class attributes and methods
fastfst_nSIG_RtTq_value: Property = Property(name="value", type=FloatType)
fastfst_nSIG_RtTq_name: Property = Property(name="name", type=StringType)
fastfst_nSIG_RtTq.attributes={fastfst_nSIG_RtTq_value, fastfst_nSIG_RtTq_name}

# fastfst_nSIG_PORt class attributes and methods
fastfst_nSIG_PORt_value: Property = Property(name="value", type=FloatType)
fastfst_nSIG_PORt_name: Property = Property(name="name", type=StringType)
fastfst_nSIG_PORt.attributes={fastfst_nSIG_PORt_value, fastfst_nSIG_PORt_name}

# fastfst_fPtfmFile class attributes and methods
fastfst_fPtfmFile_value: Property = Property(name="value", type=StringType)
fastfst_fPtfmFile_name: Property = Property(name="name", type=StringType)
fastfst_fPtfmFile.attributes={fastfst_fPtfmFile_value, fastfst_fPtfmFile_name}

# fastfst_nTEC_Freq class attributes and methods
fastfst_nTEC_Freq_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_Freq_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_Freq.attributes={fastfst_nTEC_Freq_value, fastfst_nTEC_Freq_name}

# fastfst_nTEC_Npol class attributes and methods
fastfst_nTEC_Npol_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_Npol_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_Npol.attributes={fastfst_nTEC_Npol_value, fastfst_nTEC_Npol_name}

# fastfst_nTEC_Sres class attributes and methods
fastfst_nTEC_Sres_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_Sres_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_Sres.attributes={fastfst_nTEC_Sres_value, fastfst_nTEC_Sres_name}

# fastfst_nTEC_Rres class attributes and methods
fastfst_nTEC_Rres_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_Rres_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_Rres.attributes={fastfst_nTEC_Rres_value, fastfst_nTEC_Rres_name}

# fastfst_nTEC_VLL class attributes and methods
fastfst_nTEC_VLL_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_VLL_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_VLL.attributes={fastfst_nTEC_VLL_name, fastfst_nTEC_VLL_value}

# fastfst_nTEC_SLR class attributes and methods
fastfst_nTEC_SLR_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_SLR_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_SLR.attributes={fastfst_nTEC_SLR_value, fastfst_nTEC_SLR_name}

# fastfst_nTEC_RLR class attributes and methods
fastfst_nTEC_RLR_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_RLR_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_RLR.attributes={fastfst_nTEC_RLR_name, fastfst_nTEC_RLR_value}

# fastfst_nTEC_MR class attributes and methods
fastfst_nTEC_MR_value: Property = Property(name="value", type=FloatType)
fastfst_nTEC_MR_name: Property = Property(name="name", type=StringType)
fastfst_nTEC_MR.attributes={fastfst_nTEC_MR_name, fastfst_nTEC_MR_value}

# fastfst_iPtfmModel class attributes and methods
fastfst_iPtfmModel_value: Property = Property(name="value", type=IntegerType)
fastfst_iPtfmModel_name: Property = Property(name="name", type=StringType)
fastfst_iPtfmModel.attributes={fastfst_iPtfmModel_value, fastfst_iPtfmModel_name}

# fastfst_iTwrNodes class attributes and methods
fastfst_iTwrNodes_value: Property = Property(name="value", type=IntegerType)
fastfst_iTwrNodes_name: Property = Property(name="name", type=StringType)
fastfst_iTwrNodes.attributes={fastfst_iTwrNodes_name, fastfst_iTwrNodes_value}

# fastfst_fTwrFile class attributes and methods
fastfst_fTwrFile_value: Property = Property(name="value", type=StringType)
fastfst_fTwrFile_name: Property = Property(name="name", type=StringType)
fastfst_fTwrFile.attributes={fastfst_fTwrFile_name, fastfst_fTwrFile_value}

# fastfst_nYawSpr class attributes and methods
fastfst_nYawSpr_value: Property = Property(name="value", type=FloatType)
fastfst_nYawSpr_name: Property = Property(name="name", type=StringType)
fastfst_nYawSpr.attributes={fastfst_nYawSpr_name, fastfst_nYawSpr_value}

# fastfst_nYawDamp class attributes and methods
fastfst_nYawDamp_value: Property = Property(name="value", type=FloatType)
fastfst_nYawDamp_name: Property = Property(name="name", type=StringType)
fastfst_nYawDamp.attributes={fastfst_nYawDamp_value, fastfst_nYawDamp_name}

# fastfst_nYawNeut class attributes and methods
fastfst_nYawNeut_value: Property = Property(name="value", type=FloatType)
fastfst_nYawNeut_name: Property = Property(name="name", type=StringType)
fastfst_nYawNeut.attributes={fastfst_nYawNeut_name, fastfst_nYawNeut_value}

# fastfst_bFurling class attributes and methods
fastfst_bFurling_value: Property = Property(name="value", type=BooleanType)
fastfst_bFurling_name: Property = Property(name="name", type=StringType)
fastfst_bFurling.attributes={fastfst_bFurling_name, fastfst_bFurling_value}

# fastfst_fFurlFile class attributes and methods
fastfst_fFurlFile_value: Property = Property(name="value", type=StringType)
fastfst_fFurlFile_name: Property = Property(name="name", type=StringType)
fastfst_fFurlFile.attributes={fastfst_fFurlFile_name, fastfst_fFurlFile_value}

# fastfst_iTeetMod class attributes and methods
fastfst_iTeetMod_value: Property = Property(name="value", type=IntegerType)
fastfst_iTeetMod_name: Property = Property(name="name", type=StringType)
fastfst_iTeetMod.attributes={fastfst_iTeetMod_name, fastfst_iTeetMod_value}

# fastfst_nTeetDmpP class attributes and methods
fastfst_nTeetDmpP_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetDmpP_name: Property = Property(name="name", type=StringType)
fastfst_nTeetDmpP.attributes={fastfst_nTeetDmpP_value, fastfst_nTeetDmpP_name}

# fastfst_nTeetDmp class attributes and methods
fastfst_nTeetDmp_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetDmp_name: Property = Property(name="name", type=StringType)
fastfst_nTeetDmp.attributes={fastfst_nTeetDmp_name, fastfst_nTeetDmp_value}

# fastfst_nTeetCDmp class attributes and methods
fastfst_nTeetCDmp_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetCDmp_name: Property = Property(name="name", type=StringType)
fastfst_nTeetCDmp.attributes={fastfst_nTeetCDmp_name, fastfst_nTeetCDmp_value}

# fastfst_nTeetSStP class attributes and methods
fastfst_nTeetSStP_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetSStP_name: Property = Property(name="name", type=StringType)
fastfst_nTeetSStP.attributes={fastfst_nTeetSStP_value, fastfst_nTeetSStP_name}

# fastfst_nTeetHStP class attributes and methods
fastfst_nTeetHStP_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetHStP_name: Property = Property(name="name", type=StringType)
fastfst_nTeetHStP.attributes={fastfst_nTeetHStP_value, fastfst_nTeetHStP_name}

# fastfst_nTeetSSSp class attributes and methods
fastfst_nTeetSSSp_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetSSSp_name: Property = Property(name="name", type=StringType)
fastfst_nTeetSSSp.attributes={fastfst_nTeetSSSp_name, fastfst_nTeetSSSp_value}

# fastfst_nTeetHSSp class attributes and methods
fastfst_nTeetHSSp_value: Property = Property(name="value", type=FloatType)
fastfst_nTeetHSSp_name: Property = Property(name="name", type=StringType)
fastfst_nTeetHSSp.attributes={fastfst_nTeetHSSp_name, fastfst_nTeetHSSp_value}

# fastfst_nTBDrConN class attributes and methods
fastfst_nTBDrConN_value: Property = Property(name="value", type=FloatType)
fastfst_nTBDrConN_name: Property = Property(name="name", type=StringType)
fastfst_nTBDrConN.attributes={fastfst_nTBDrConN_name, fastfst_nTBDrConN_value}

# fastfst_nTBDrConD class attributes and methods
fastfst_nTBDrConD_value: Property = Property(name="value", type=FloatType)
fastfst_nTBDrConD_name: Property = Property(name="name", type=StringType)
fastfst_nTBDrConD.attributes={fastfst_nTBDrConD_value, fastfst_nTBDrConD_name}

# fastfst_nTpBrDT class attributes and methods
fastfst_nTpBrDT_value: Property = Property(name="value", type=FloatType)
fastfst_nTpBrDT_name: Property = Property(name="name", type=StringType)
fastfst_nTpBrDT.attributes={fastfst_nTpBrDT_value, fastfst_nTpBrDT_name}

# fastfst_fBldFile_1_ class attributes and methods
fastfst_fBldFile_1__value: Property = Property(name="value", type=StringType)
fastfst_fBldFile_1__name: Property = Property(name="name", type=StringType)
fastfst_fBldFile_1_.attributes={fastfst_fBldFile_1__name, fastfst_fBldFile_1__value}

# fastfst_fBldFile_2_ class attributes and methods
fastfst_fBldFile_2__value: Property = Property(name="value", type=StringType)
fastfst_fBldFile_2__name: Property = Property(name="name", type=StringType)
fastfst_fBldFile_2_.attributes={fastfst_fBldFile_2__value, fastfst_fBldFile_2__name}

# fastfst_fBldFile_3_ class attributes and methods
fastfst_fBldFile_3__value: Property = Property(name="value", type=StringType)
fastfst_fBldFile_3__name: Property = Property(name="name", type=StringType)
fastfst_fBldFile_3_.attributes={fastfst_fBldFile_3__name, fastfst_fBldFile_3__value}

# fastfst_fADFile class attributes and methods
fastfst_fADFile_value: Property = Property(name="value", type=StringType)
fastfst_fADFile_name: Property = Property(name="name", type=StringType)
fastfst_fADFile.attributes={fastfst_fADFile_value, fastfst_fADFile_name}

# fastfst_fNoiseFile class attributes and methods
fastfst_fNoiseFile_value: Property = Property(name="value", type=StringType)
fastfst_fNoiseFile_name: Property = Property(name="name", type=StringType)
fastfst_fNoiseFile.attributes={fastfst_fNoiseFile_name, fastfst_fNoiseFile_value}

# fastfst_fADAMSFile class attributes and methods
fastfst_fADAMSFile_value: Property = Property(name="value", type=StringType)
fastfst_fADAMSFile_name: Property = Property(name="name", type=StringType)
fastfst_fADAMSFile.attributes={fastfst_fADAMSFile_value, fastfst_fADAMSFile_name}

# fastfst_fLinFile class attributes and methods
fastfst_fLinFile_value: Property = Property(name="value", type=StringType)
fastfst_fLinFile_name: Property = Property(name="name", type=StringType)
fastfst_fLinFile.attributes={fastfst_fLinFile_value, fastfst_fLinFile_name}

# fastfst_bSumPrint class attributes and methods
fastfst_bSumPrint_value: Property = Property(name="value", type=BooleanType)
fastfst_bSumPrint_name: Property = Property(name="name", type=StringType)
fastfst_bSumPrint.attributes={fastfst_bSumPrint_name, fastfst_bSumPrint_value}

# fastfst_bOutFileFmt class attributes and methods
fastfst_bOutFileFmt_value: Property = Property(name="value", type=FloatType)
fastfst_bOutFileFmt_name: Property = Property(name="name", type=StringType)
fastfst_bOutFileFmt.attributes={fastfst_bOutFileFmt_name, fastfst_bOutFileFmt_value}

# fastfst_bTabDelim class attributes and methods
fastfst_bTabDelim_value: Property = Property(name="value", type=BooleanType)
fastfst_bTabDelim_name: Property = Property(name="name", type=StringType)
fastfst_bTabDelim.attributes={fastfst_bTabDelim_value, fastfst_bTabDelim_name}

# fastfst_sOutFmt class attributes and methods
fastfst_sOutFmt_value: Property = Property(name="value", type=StringType)
fastfst_sOutFmt_name: Property = Property(name="name", type=StringType)
fastfst_sOutFmt.attributes={fastfst_sOutFmt_name, fastfst_sOutFmt_value}

# fastfst_nTStart class attributes and methods
fastfst_nTStart_value: Property = Property(name="value", type=FloatType)
fastfst_nTStart_name: Property = Property(name="name", type=StringType)
fastfst_nTStart.attributes={fastfst_nTStart_name, fastfst_nTStart_value}

# fastfst_iDecFact class attributes and methods
fastfst_iDecFact_value: Property = Property(name="value", type=IntegerType)
fastfst_iDecFact_name: Property = Property(name="name", type=StringType)
fastfst_iDecFact.attributes={fastfst_iDecFact_value, fastfst_iDecFact_name}

# fastfst_nSttsTime class attributes and methods
fastfst_nSttsTime_value: Property = Property(name="value", type=FloatType)
fastfst_nSttsTime_name: Property = Property(name="name", type=StringType)
fastfst_nSttsTime.attributes={fastfst_nSttsTime_value, fastfst_nSttsTime_name}

# fastfst_nNcIMUxn class attributes and methods
fastfst_nNcIMUxn_value: Property = Property(name="value", type=FloatType)
fastfst_nNcIMUxn_name: Property = Property(name="name", type=StringType)
fastfst_nNcIMUxn.attributes={fastfst_nNcIMUxn_name, fastfst_nNcIMUxn_value}

# fastfst_nNcIMUyn class attributes and methods
fastfst_nNcIMUyn_value: Property = Property(name="value", type=FloatType)
fastfst_nNcIMUyn_name: Property = Property(name="name", type=StringType)
fastfst_nNcIMUyn.attributes={fastfst_nNcIMUyn_value, fastfst_nNcIMUyn_name}

# fastfst_nNcIMUzn class attributes and methods
fastfst_nNcIMUzn_value: Property = Property(name="value", type=FloatType)
fastfst_nNcIMUzn_name: Property = Property(name="name", type=StringType)
fastfst_nNcIMUzn.attributes={fastfst_nNcIMUzn_value, fastfst_nNcIMUzn_name}

# fastfst_nShftGagL class attributes and methods
fastfst_nShftGagL_value: Property = Property(name="value", type=FloatType)
fastfst_nShftGagL_name: Property = Property(name="name", type=StringType)
fastfst_nShftGagL.attributes={fastfst_nShftGagL_name, fastfst_nShftGagL_value}

# fastfst_iNTwGages class attributes and methods
fastfst_iNTwGages_value: Property = Property(name="value", type=IntegerType)
fastfst_iNTwGages_name: Property = Property(name="name", type=StringType)
fastfst_iNTwGages.attributes={fastfst_iNTwGages_name, fastfst_iNTwGages_value}

# fastfst_aTwrGagNd class attributes and methods
fastfst_aTwrGagNd_value: Property = Property(name="value", type=StringType)
fastfst_aTwrGagNd_name: Property = Property(name="name", type=StringType)
fastfst_aTwrGagNd.attributes={fastfst_aTwrGagNd_value, fastfst_aTwrGagNd_name}

# fastfst_iNBlGages class attributes and methods
fastfst_iNBlGages_value: Property = Property(name="value", type=IntegerType)
fastfst_iNBlGages_name: Property = Property(name="name", type=StringType)
fastfst_iNBlGages.attributes={fastfst_iNBlGages_value, fastfst_iNBlGages_name}

# fastfst_aBldGagNd class attributes and methods
fastfst_aBldGagNd_value: Property = Property(name="value", type=StringType)
fastfst_aBldGagNd_name: Property = Property(name="name", type=StringType)
fastfst_aBldGagNd.attributes={fastfst_aBldGagNd_value, fastfst_aBldGagNd_name}

# fastfst_vOutList class attributes and methods
fastfst_vOutList_name: Property = Property(name="name", type=StringType)
fastfst_vOutList_value: Property = Property(name="value", type=StringType)
fastfst_vOutList.attributes={fastfst_vOutList_value, fastfst_vOutList_name}

# Relationships
Head0: BinaryAssociation = BinaryAssociation(
    name="Head0",
    ends={
        Property(name="fastfst_Header", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst", type=fastfst_Header, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sections1: BinaryAssociation = BinaryAssociation(
    name="sections1",
    ends={
        Property(name="fastfst_Section", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst2", type=fastfst_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Echo3: BinaryAssociation = BinaryAssociation(
    name="Echo3",
    ends={
        Property(name="fastfst_bEcho", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst4", type=fastfst_bEcho, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ADAMSPrep5: BinaryAssociation = BinaryAssociation(
    name="ADAMSPrep5",
    ends={
        Property(name="fastfst_iADAMSPrep", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst6", type=fastfst_iADAMSPrep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AnalMode7: BinaryAssociation = BinaryAssociation(
    name="AnalMode7",
    ends={
        Property(name="fastfst_iAnalMode", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst8", type=fastfst_iAnalMode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HSSBrMode45: BinaryAssociation = BinaryAssociation(
    name="HSSBrMode45",
    ends={
        Property(name="fastfst_ModelFastfst46", type=fastfst_iHSSBrMode, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="fastfst_iHSSBrMode", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1))
    }
)
THSSBrDp47: BinaryAssociation = BinaryAssociation(
    name="THSSBrDp47",
    ends={
        Property(name="fastfst_nTHSSBrDp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst48", type=fastfst_nTHSSBrDp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TiDynBrk49: BinaryAssociation = BinaryAssociation(
    name="TiDynBrk49",
    ends={
        Property(name="fastfst_nTiDynBrk", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst50", type=fastfst_nTiDynBrk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NumBl9: BinaryAssociation = BinaryAssociation(
    name="NumBl9",
    ends={
        Property(name="fastfst_iNumBl", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst10", type=fastfst_iNumBl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TMax11: BinaryAssociation = BinaryAssociation(
    name="TMax11",
    ends={
        Property(name="fastfst_nTMax", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst12", type=fastfst_nTMax, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DT13: BinaryAssociation = BinaryAssociation(
    name="DT13",
    ends={
        Property(name="fastfst_nDT", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst14", type=fastfst_nDT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YCMode15: BinaryAssociation = BinaryAssociation(
    name="YCMode15",
    ends={
        Property(name="fastfst_iYCMode", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst16", type=fastfst_iYCMode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TYCOn17: BinaryAssociation = BinaryAssociation(
    name="TYCOn17",
    ends={
        Property(name="fastfst_nTYCOn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst18", type=fastfst_nTYCOn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PCMode19: BinaryAssociation = BinaryAssociation(
    name="PCMode19",
    ends={
        Property(name="fastfst_iPCMode", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst20", type=fastfst_iPCMode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPCOn21: BinaryAssociation = BinaryAssociation(
    name="TPCOn21",
    ends={
        Property(name="fastfst_nTPCOn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst22", type=fastfst_nTPCOn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VSContrl23: BinaryAssociation = BinaryAssociation(
    name="VSContrl23",
    ends={
        Property(name="fastfst_iVSContrl", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst24", type=fastfst_iVSContrl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VS_RtGnSp25: BinaryAssociation = BinaryAssociation(
    name="VS_RtGnSp25",
    ends={
        Property(name="fastfst_nVS_RtGnSp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst26", type=fastfst_nVS_RtGnSp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VS_RtTq27: BinaryAssociation = BinaryAssociation(
    name="VS_RtTq27",
    ends={
        Property(name="fastfst_nVS_RtTq", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst28", type=fastfst_nVS_RtTq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VS_Rgn2K29: BinaryAssociation = BinaryAssociation(
    name="VS_Rgn2K29",
    ends={
        Property(name="fastfst_nVS_Rgn2K", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst30", type=fastfst_nVS_Rgn2K, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
VS_SlPc31: BinaryAssociation = BinaryAssociation(
    name="VS_SlPc31",
    ends={
        Property(name="fastfst_nVS_SlPc", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst32", type=fastfst_nVS_SlPc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenModel33: BinaryAssociation = BinaryAssociation(
    name="GenModel33",
    ends={
        Property(name="fastfst_iGenModel", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst34", type=fastfst_iGenModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenTiStr35: BinaryAssociation = BinaryAssociation(
    name="GenTiStr35",
    ends={
        Property(name="fastfst_bGenTiStr", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst36", type=fastfst_bGenTiStr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenTiStp37: BinaryAssociation = BinaryAssociation(
    name="GenTiStp37",
    ends={
        Property(name="fastfst_bGenTiStp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst38", type=fastfst_bGenTiStp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SpdGenOn39: BinaryAssociation = BinaryAssociation(
    name="SpdGenOn39",
    ends={
        Property(name="fastfst_nSpdGenOn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst40", type=fastfst_nSpdGenOn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TimGenOn41: BinaryAssociation = BinaryAssociation(
    name="TimGenOn41",
    ends={
        Property(name="fastfst_nTimGenOn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst42", type=fastfst_nTimGenOn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TimGenOf43: BinaryAssociation = BinaryAssociation(
    name="TimGenOf43",
    ends={
        Property(name="fastfst_nTimGenOf", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst44", type=fastfst_nTimGenOf, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TBDepISp_1_57: BinaryAssociation = BinaryAssociation(
    name="TBDepISp_1_57",
    ends={
        Property(name="fastfst_nTBDepISp_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst58", type=fastfst_nTBDepISp_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TTpBrDp_1_51: BinaryAssociation = BinaryAssociation(
    name="TTpBrDp_1_51",
    ends={
        Property(name="fastfst_nTTpBrDp_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst52", type=fastfst_nTTpBrDp_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TTpBrDp_2_53: BinaryAssociation = BinaryAssociation(
    name="TTpBrDp_2_53",
    ends={
        Property(name="fastfst_nTTpBrDp_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst54", type=fastfst_nTTpBrDp_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TTpBrDp_3_55: BinaryAssociation = BinaryAssociation(
    name="TTpBrDp_3_55",
    ends={
        Property(name="fastfst_nTTpBrDp_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst56", type=fastfst_nTTpBrDp_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacYawF67: BinaryAssociation = BinaryAssociation(
    name="NacYawF67",
    ends={
        Property(name="fastfst_nNacYawF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst68", type=fastfst_nNacYawF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TBDepISp_2_59: BinaryAssociation = BinaryAssociation(
    name="TBDepISp_2_59",
    ends={
        Property(name="fastfst_nTBDepISp_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst60", type=fastfst_nTBDepISp_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TBDepISp_3_61: BinaryAssociation = BinaryAssociation(
    name="TBDepISp_3_61",
    ends={
        Property(name="fastfst_nTBDepISp_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst62", type=fastfst_nTBDepISp_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TYawManS63: BinaryAssociation = BinaryAssociation(
    name="TYawManS63",
    ends={
        Property(name="fastfst_nTYawManS", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst64", type=fastfst_nTYawManS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TYawManE65: BinaryAssociation = BinaryAssociation(
    name="TYawManE65",
    ends={
        Property(name="fastfst_nTYawManE", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst66", type=fastfst_nTYawManE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPitManE_1_75: BinaryAssociation = BinaryAssociation(
    name="TPitManE_1_75",
    ends={
        Property(name="fastfst_ModelFastfst76", type=fastfst_nTPitManE_1_, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="fastfst_nTPitManE_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1))
    }
)
TPitManS_1_69: BinaryAssociation = BinaryAssociation(
    name="TPitManS_1_69",
    ends={
        Property(name="fastfst_nTPitManS_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst70", type=fastfst_nTPitManS_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPitManS_2_71: BinaryAssociation = BinaryAssociation(
    name="TPitManS_2_71",
    ends={
        Property(name="fastfst_nTPitManS_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst72", type=fastfst_nTPitManS_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPitManS_3_73: BinaryAssociation = BinaryAssociation(
    name="TPitManS_3_73",
    ends={
        Property(name="fastfst_nTPitManS_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst74", type=fastfst_nTPitManS_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitch_3_85: BinaryAssociation = BinaryAssociation(
    name="BlPitch_3_85",
    ends={
        Property(name="fastfst_nBlPitch_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst86", type=fastfst_nBlPitch_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPitManE_2_77: BinaryAssociation = BinaryAssociation(
    name="TPitManE_2_77",
    ends={
        Property(name="fastfst_nTPitManE_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst78", type=fastfst_nTPitManE_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TPitManE_3_79: BinaryAssociation = BinaryAssociation(
    name="TPitManE_3_79",
    ends={
        Property(name="fastfst_nTPitManE_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst80", type=fastfst_nTPitManE_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitch_1_81: BinaryAssociation = BinaryAssociation(
    name="BlPitch_1_81",
    ends={
        Property(name="fastfst_nBlPitch_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst82", type=fastfst_nBlPitch_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitch_2_83: BinaryAssociation = BinaryAssociation(
    name="BlPitch_2_83",
    ends={
        Property(name="fastfst_nBlPitch_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst84", type=fastfst_nBlPitch_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Gravity93: BinaryAssociation = BinaryAssociation(
    name="Gravity93",
    ends={
        Property(name="fastfst_nGravity", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst94", type=fastfst_nGravity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitchF_1_87: BinaryAssociation = BinaryAssociation(
    name="BlPitchF_1_87",
    ends={
        Property(name="fastfst_nBlPitchF_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst88", type=fastfst_nBlPitchF_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitchF_2_89: BinaryAssociation = BinaryAssociation(
    name="BlPitchF_2_89",
    ends={
        Property(name="fastfst_nBlPitchF_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst90", type=fastfst_nBlPitchF_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BlPitchF_3_91: BinaryAssociation = BinaryAssociation(
    name="BlPitchF_3_91",
    ends={
        Property(name="fastfst_nBlPitchF_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst92", type=fastfst_nBlPitchF_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwFADOF2111: BinaryAssociation = BinaryAssociation(
    name="TwFADOF2111",
    ends={
        Property(name="fastfst_bTwFADOF2", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst112", type=fastfst_bTwFADOF2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FlapDOF195: BinaryAssociation = BinaryAssociation(
    name="FlapDOF195",
    ends={
        Property(name="fastfst_bFlapDOF1", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst96", type=fastfst_bFlapDOF1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FlapDOF297: BinaryAssociation = BinaryAssociation(
    name="FlapDOF297",
    ends={
        Property(name="fastfst_bFlapDOF2", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst98", type=fastfst_bFlapDOF2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
EdgeDOF99: BinaryAssociation = BinaryAssociation(
    name="EdgeDOF99",
    ends={
        Property(name="fastfst_bEdgeDOF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst100", type=fastfst_bEdgeDOF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetDOF101: BinaryAssociation = BinaryAssociation(
    name="TeetDOF101",
    ends={
        Property(name="fastfst_bTeetDOF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst102", type=fastfst_bTeetDOF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DrTrDOF103: BinaryAssociation = BinaryAssociation(
    name="DrTrDOF103",
    ends={
        Property(name="fastfst_bDrTrDOF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst104", type=fastfst_bDrTrDOF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenDOF105: BinaryAssociation = BinaryAssociation(
    name="GenDOF105",
    ends={
        Property(name="fastfst_bGenDOF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst106", type=fastfst_bGenDOF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YawDOF107: BinaryAssociation = BinaryAssociation(
    name="YawDOF107",
    ends={
        Property(name="fastfst_bYawDOF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst108", type=fastfst_bYawDOF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwFADOF1109: BinaryAssociation = BinaryAssociation(
    name="TwFADOF1109",
    ends={
        Property(name="fastfst_bTwFADOF1", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst110", type=fastfst_bTwFADOF1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Azimuth127: BinaryAssociation = BinaryAssociation(
    name="Azimuth127",
    ends={
        Property(name="fastfst_nAzimuth", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst128", type=fastfst_nAzimuth, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwSSDOF1113: BinaryAssociation = BinaryAssociation(
    name="TwSSDOF1113",
    ends={
        Property(name="fastfst_bTwSSDOF1", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst114", type=fastfst_bTwSSDOF1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwSSDOF2115: BinaryAssociation = BinaryAssociation(
    name="TwSSDOF2115",
    ends={
        Property(name="fastfst_bTwSSDOF2", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst116", type=fastfst_bTwSSDOF2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CompAero117: BinaryAssociation = BinaryAssociation(
    name="CompAero117",
    ends={
        Property(name="fastfst_bCompAero", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst118", type=fastfst_bCompAero, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CompNoise119: BinaryAssociation = BinaryAssociation(
    name="CompNoise119",
    ends={
        Property(name="fastfst_bCompNoise", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst120", type=fastfst_bCompNoise, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OoPDefl121: BinaryAssociation = BinaryAssociation(
    name="OoPDefl121",
    ends={
        Property(name="fastfst_nOoPDefl", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst122", type=fastfst_nOoPDefl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
IPDefl123: BinaryAssociation = BinaryAssociation(
    name="IPDefl123",
    ends={
        Property(name="fastfst_nIPDefl", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst124", type=fastfst_nIPDefl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetDefl125: BinaryAssociation = BinaryAssociation(
    name="TeetDefl125",
    ends={
        Property(name="fastfst_nTeetDefl", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst126", type=fastfst_nTeetDefl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RotSpeed129: BinaryAssociation = BinaryAssociation(
    name="RotSpeed129",
    ends={
        Property(name="fastfst_nRotSpeed", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst130", type=fastfst_nRotSpeed, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacYaw131: BinaryAssociation = BinaryAssociation(
    name="NacYaw131",
    ends={
        Property(name="fastfst_nNacYaw", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst132", type=fastfst_nNacYaw, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TTDspFA133: BinaryAssociation = BinaryAssociation(
    name="TTDspFA133",
    ends={
        Property(name="fastfst_nTTDspFA", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst134", type=fastfst_nTTDspFA, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TTDspSS135: BinaryAssociation = BinaryAssociation(
    name="TTDspSS135",
    ends={
        Property(name="fastfst_nTTDspSS", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst136", type=fastfst_nTTDspSS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TipRad137: BinaryAssociation = BinaryAssociation(
    name="TipRad137",
    ends={
        Property(name="fastfst_nTipRad", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst138", type=fastfst_nTipRad, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HubRad139: BinaryAssociation = BinaryAssociation(
    name="HubRad139",
    ends={
        Property(name="fastfst_nHubRad", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst140", type=fastfst_nHubRad, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PSpnElN141: BinaryAssociation = BinaryAssociation(
    name="PSpnElN141",
    ends={
        Property(name="fastfst_nPSpnElN", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst142", type=fastfst_nPSpnElN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
UndSling143: BinaryAssociation = BinaryAssociation(
    name="UndSling143",
    ends={
        Property(name="fastfst_nUndSling", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst144", type=fastfst_nUndSling, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacCMyn151: BinaryAssociation = BinaryAssociation(
    name="NacCMyn151",
    ends={
        Property(name="fastfst_ModelFastfst152", type=fastfst_nNacCMyn, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="fastfst_nNacCMyn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1))
    }
)
NacCMzn153: BinaryAssociation = BinaryAssociation(
    name="NacCMzn153",
    ends={
        Property(name="fastfst_nNacCMzn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst154", type=fastfst_nNacCMzn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HubCM145: BinaryAssociation = BinaryAssociation(
    name="HubCM145",
    ends={
        Property(name="fastfst_nHubCM", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst146", type=fastfst_nHubCM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TowerHt155: BinaryAssociation = BinaryAssociation(
    name="TowerHt155",
    ends={
        Property(name="fastfst_nTowerHt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst156", type=fastfst_nTowerHt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Twr2Shft157: BinaryAssociation = BinaryAssociation(
    name="Twr2Shft157",
    ends={
        Property(name="fastfst_nTwr2Shft", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst158", type=fastfst_nTwr2Shft, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwrRBHt159: BinaryAssociation = BinaryAssociation(
    name="TwrRBHt159",
    ends={
        Property(name="fastfst_nTwrRBHt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst160", type=fastfst_nTwrRBHt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ShftTilt161: BinaryAssociation = BinaryAssociation(
    name="ShftTilt161",
    ends={
        Property(name="fastfst_nShftTilt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst162", type=fastfst_nShftTilt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Delta3163: BinaryAssociation = BinaryAssociation(
    name="Delta3163",
    ends={
        Property(name="fastfst_nDelta3", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst164", type=fastfst_nDelta3, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PreCone_1_165: BinaryAssociation = BinaryAssociation(
    name="PreCone_1_165",
    ends={
        Property(name="fastfst_nPreCone_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst166", type=fastfst_nPreCone_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PreCone_2_167: BinaryAssociation = BinaryAssociation(
    name="PreCone_2_167",
    ends={
        Property(name="fastfst_nPreCone_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst168", type=fastfst_nPreCone_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PreCone_3_169: BinaryAssociation = BinaryAssociation(
    name="PreCone_3_169",
    ends={
        Property(name="fastfst_nPreCone_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst170", type=fastfst_nPreCone_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OverHang147: BinaryAssociation = BinaryAssociation(
    name="OverHang147",
    ends={
        Property(name="fastfst_nOverHang", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst148", type=fastfst_nOverHang, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AzimB1Up171: BinaryAssociation = BinaryAssociation(
    name="AzimB1Up171",
    ends={
        Property(name="fastfst_nAzimB1Up", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst172", type=fastfst_nAzimB1Up, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacCMxn149: BinaryAssociation = BinaryAssociation(
    name="NacCMxn149",
    ends={
        Property(name="fastfst_nNacCMxn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst150", type=fastfst_nNacCMxn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacMass175: BinaryAssociation = BinaryAssociation(
    name="NacMass175",
    ends={
        Property(name="fastfst_nNacMass", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst176", type=fastfst_nNacMass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HubMass177: BinaryAssociation = BinaryAssociation(
    name="HubMass177",
    ends={
        Property(name="fastfst_nHubMass", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst178", type=fastfst_nHubMass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TipMass_1_179: BinaryAssociation = BinaryAssociation(
    name="TipMass_1_179",
    ends={
        Property(name="fastfst_nTipMass_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst180", type=fastfst_nTipMass_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TipMass_2_181: BinaryAssociation = BinaryAssociation(
    name="TipMass_2_181",
    ends={
        Property(name="fastfst_nTipMass_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst182", type=fastfst_nTipMass_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TipMass_3_183: BinaryAssociation = BinaryAssociation(
    name="TipMass_3_183",
    ends={
        Property(name="fastfst_nTipMass_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst184", type=fastfst_nTipMass_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NacYIner185: BinaryAssociation = BinaryAssociation(
    name="NacYIner185",
    ends={
        Property(name="fastfst_nNacYIner", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst186", type=fastfst_nNacYIner, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenIner187: BinaryAssociation = BinaryAssociation(
    name="GenIner187",
    ends={
        Property(name="fastfst_nGenIner", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst188", type=fastfst_nGenIner, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HubIner189: BinaryAssociation = BinaryAssociation(
    name="HubIner189",
    ends={
        Property(name="fastfst_nHubIner", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst190", type=fastfst_nHubIner, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GBoxEff191: BinaryAssociation = BinaryAssociation(
    name="GBoxEff191",
    ends={
        Property(name="fastfst_nGBoxEff", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst192", type=fastfst_nGBoxEff, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GenEff193: BinaryAssociation = BinaryAssociation(
    name="GenEff193",
    ends={
        Property(name="fastfst_nGenEff", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst194", type=fastfst_nGenEff, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YawBrMass173: BinaryAssociation = BinaryAssociation(
    name="YawBrMass173",
    ends={
        Property(name="fastfst_nYawBrMass", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst174", type=fastfst_nYawBrMass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GBRevers197: BinaryAssociation = BinaryAssociation(
    name="GBRevers197",
    ends={
        Property(name="fastfst_bGBRevers", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst198", type=fastfst_bGBRevers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HSSBrTqF199: BinaryAssociation = BinaryAssociation(
    name="HSSBrTqF199",
    ends={
        Property(name="fastfst_nHSSBrTqF", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst200", type=fastfst_nHSSBrTqF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
HSSBrDT201: BinaryAssociation = BinaryAssociation(
    name="HSSBrDT201",
    ends={
        Property(name="fastfst_nHSSBrDT", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst202", type=fastfst_nHSSBrDT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DynBrkFi203: BinaryAssociation = BinaryAssociation(
    name="DynBrkFi203",
    ends={
        Property(name="fastfst_fDynBrkFi", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst204", type=fastfst_fDynBrkFi, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DTTorSpr205: BinaryAssociation = BinaryAssociation(
    name="DTTorSpr205",
    ends={
        Property(name="fastfst_nDTTorSpr", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst206", type=fastfst_nDTTorSpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DTTorDmp207: BinaryAssociation = BinaryAssociation(
    name="DTTorDmp207",
    ends={
        Property(name="fastfst_nDTTorDmp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst208", type=fastfst_nDTTorDmp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SIG_SlPc209: BinaryAssociation = BinaryAssociation(
    name="SIG_SlPc209",
    ends={
        Property(name="fastfst_nSIG_SlPc", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst210", type=fastfst_nSIG_SlPc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SIG_SySp211: BinaryAssociation = BinaryAssociation(
    name="SIG_SySp211",
    ends={
        Property(name="fastfst_nSIG_SySp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst212", type=fastfst_nSIG_SySp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SIG_RtTq213: BinaryAssociation = BinaryAssociation(
    name="SIG_RtTq213",
    ends={
        Property(name="fastfst_nSIG_RtTq", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst214", type=fastfst_nSIG_RtTq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
GBRatio195: BinaryAssociation = BinaryAssociation(
    name="GBRatio195",
    ends={
        Property(name="fastfst_nGBRatio", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst196", type=fastfst_nGBRatio, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SIG_PORt215: BinaryAssociation = BinaryAssociation(
    name="SIG_PORt215",
    ends={
        Property(name="fastfst_nSIG_PORt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst216", type=fastfst_nSIG_PORt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_Freq217: BinaryAssociation = BinaryAssociation(
    name="TEC_Freq217",
    ends={
        Property(name="fastfst_nTEC_Freq", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst218", type=fastfst_nTEC_Freq, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_Npol219: BinaryAssociation = BinaryAssociation(
    name="TEC_Npol219",
    ends={
        Property(name="fastfst_nTEC_Npol", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst220", type=fastfst_nTEC_Npol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_Sres221: BinaryAssociation = BinaryAssociation(
    name="TEC_Sres221",
    ends={
        Property(name="fastfst_nTEC_Sres", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst222", type=fastfst_nTEC_Sres, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_Rres223: BinaryAssociation = BinaryAssociation(
    name="TEC_Rres223",
    ends={
        Property(name="fastfst_nTEC_Rres", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst224", type=fastfst_nTEC_Rres, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_VLL225: BinaryAssociation = BinaryAssociation(
    name="TEC_VLL225",
    ends={
        Property(name="fastfst_nTEC_VLL", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst226", type=fastfst_nTEC_VLL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_SLR227: BinaryAssociation = BinaryAssociation(
    name="TEC_SLR227",
    ends={
        Property(name="fastfst_nTEC_SLR", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst228", type=fastfst_nTEC_SLR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_RLR229: BinaryAssociation = BinaryAssociation(
    name="TEC_RLR229",
    ends={
        Property(name="fastfst_nTEC_RLR", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst230", type=fastfst_nTEC_RLR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TEC_MR231: BinaryAssociation = BinaryAssociation(
    name="TEC_MR231",
    ends={
        Property(name="fastfst_nTEC_MR", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst232", type=fastfst_nTEC_MR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PtfmModel233: BinaryAssociation = BinaryAssociation(
    name="PtfmModel233",
    ends={
        Property(name="fastfst_iPtfmModel", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst234", type=fastfst_iPtfmModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PtfmFile235: BinaryAssociation = BinaryAssociation(
    name="PtfmFile235",
    ends={
        Property(name="fastfst_fPtfmFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst236", type=fastfst_fPtfmFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwrNodes237: BinaryAssociation = BinaryAssociation(
    name="TwrNodes237",
    ends={
        Property(name="fastfst_iTwrNodes", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst238", type=fastfst_iTwrNodes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwrFile239: BinaryAssociation = BinaryAssociation(
    name="TwrFile239",
    ends={
        Property(name="fastfst_fTwrFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst240", type=fastfst_fTwrFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YawSpr241: BinaryAssociation = BinaryAssociation(
    name="YawSpr241",
    ends={
        Property(name="fastfst_nYawSpr", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst242", type=fastfst_nYawSpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YawDamp243: BinaryAssociation = BinaryAssociation(
    name="YawDamp243",
    ends={
        Property(name="fastfst_nYawDamp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst244", type=fastfst_nYawDamp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
YawNeut245: BinaryAssociation = BinaryAssociation(
    name="YawNeut245",
    ends={
        Property(name="fastfst_nYawNeut", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst246", type=fastfst_nYawNeut, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Furling247: BinaryAssociation = BinaryAssociation(
    name="Furling247",
    ends={
        Property(name="fastfst_bFurling", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst248", type=fastfst_bFurling, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
FurlFile249: BinaryAssociation = BinaryAssociation(
    name="FurlFile249",
    ends={
        Property(name="fastfst_fFurlFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst250", type=fastfst_fFurlFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetMod251: BinaryAssociation = BinaryAssociation(
    name="TeetMod251",
    ends={
        Property(name="fastfst_iTeetMod", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst252", type=fastfst_iTeetMod, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetDmpP253: BinaryAssociation = BinaryAssociation(
    name="TeetDmpP253",
    ends={
        Property(name="fastfst_nTeetDmpP", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst254", type=fastfst_nTeetDmpP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetDmp255: BinaryAssociation = BinaryAssociation(
    name="TeetDmp255",
    ends={
        Property(name="fastfst_nTeetDmp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst256", type=fastfst_nTeetDmp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetCDmp257: BinaryAssociation = BinaryAssociation(
    name="TeetCDmp257",
    ends={
        Property(name="fastfst_nTeetCDmp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst258", type=fastfst_nTeetCDmp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetSStP259: BinaryAssociation = BinaryAssociation(
    name="TeetSStP259",
    ends={
        Property(name="fastfst_nTeetSStP", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst260", type=fastfst_nTeetSStP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetHStP261: BinaryAssociation = BinaryAssociation(
    name="TeetHStP261",
    ends={
        Property(name="fastfst_nTeetHStP", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst262", type=fastfst_nTeetHStP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetSSSp263: BinaryAssociation = BinaryAssociation(
    name="TeetSSSp263",
    ends={
        Property(name="fastfst_nTeetSSSp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst264", type=fastfst_nTeetSSSp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TeetHSSp265: BinaryAssociation = BinaryAssociation(
    name="TeetHSSp265",
    ends={
        Property(name="fastfst_nTeetHSSp", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst266", type=fastfst_nTeetHSSp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TBDrConN267: BinaryAssociation = BinaryAssociation(
    name="TBDrConN267",
    ends={
        Property(name="fastfst_nTBDrConN", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst268", type=fastfst_nTBDrConN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TBDrConD269: BinaryAssociation = BinaryAssociation(
    name="TBDrConD269",
    ends={
        Property(name="fastfst_nTBDrConD", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst270", type=fastfst_nTBDrConD, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TpBrDT271: BinaryAssociation = BinaryAssociation(
    name="TpBrDT271",
    ends={
        Property(name="fastfst_nTpBrDT", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst272", type=fastfst_nTpBrDT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BldFile_1_273: BinaryAssociation = BinaryAssociation(
    name="BldFile_1_273",
    ends={
        Property(name="fastfst_fBldFile_1_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst274", type=fastfst_fBldFile_1_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BldFile_2_275: BinaryAssociation = BinaryAssociation(
    name="BldFile_2_275",
    ends={
        Property(name="fastfst_fBldFile_2_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst276", type=fastfst_fBldFile_2_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BldFile_3_277: BinaryAssociation = BinaryAssociation(
    name="BldFile_3_277",
    ends={
        Property(name="fastfst_fBldFile_3_", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst278", type=fastfst_fBldFile_3_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ADFile279: BinaryAssociation = BinaryAssociation(
    name="ADFile279",
    ends={
        Property(name="fastfst_fADFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst280", type=fastfst_fADFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NoiseFile281: BinaryAssociation = BinaryAssociation(
    name="NoiseFile281",
    ends={
        Property(name="fastfst_fNoiseFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst282", type=fastfst_fNoiseFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ADAMSFile283: BinaryAssociation = BinaryAssociation(
    name="ADAMSFile283",
    ends={
        Property(name="fastfst_fADAMSFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst284", type=fastfst_fADAMSFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LinFile285: BinaryAssociation = BinaryAssociation(
    name="LinFile285",
    ends={
        Property(name="fastfst_fLinFile", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst286", type=fastfst_fLinFile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SumPrint287: BinaryAssociation = BinaryAssociation(
    name="SumPrint287",
    ends={
        Property(name="fastfst_bSumPrint", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst288", type=fastfst_bSumPrint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutFileFmt289: BinaryAssociation = BinaryAssociation(
    name="OutFileFmt289",
    ends={
        Property(name="fastfst_bOutFileFmt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst290", type=fastfst_bOutFileFmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TabDelim291: BinaryAssociation = BinaryAssociation(
    name="TabDelim291",
    ends={
        Property(name="fastfst_bTabDelim", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst292", type=fastfst_bTabDelim, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutFmt293: BinaryAssociation = BinaryAssociation(
    name="OutFmt293",
    ends={
        Property(name="fastfst_sOutFmt", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst294", type=fastfst_sOutFmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TStart295: BinaryAssociation = BinaryAssociation(
    name="TStart295",
    ends={
        Property(name="fastfst_nTStart", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst296", type=fastfst_nTStart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DecFact297: BinaryAssociation = BinaryAssociation(
    name="DecFact297",
    ends={
        Property(name="fastfst_iDecFact", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst298", type=fastfst_iDecFact, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SttsTime299: BinaryAssociation = BinaryAssociation(
    name="SttsTime299",
    ends={
        Property(name="fastfst_nSttsTime", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst300", type=fastfst_nSttsTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NcIMUxn301: BinaryAssociation = BinaryAssociation(
    name="NcIMUxn301",
    ends={
        Property(name="fastfst_nNcIMUxn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst302", type=fastfst_nNcIMUxn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NcIMUyn303: BinaryAssociation = BinaryAssociation(
    name="NcIMUyn303",
    ends={
        Property(name="fastfst_nNcIMUyn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst304", type=fastfst_nNcIMUyn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NcIMUzn305: BinaryAssociation = BinaryAssociation(
    name="NcIMUzn305",
    ends={
        Property(name="fastfst_nNcIMUzn", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst306", type=fastfst_nNcIMUzn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ShftGagL307: BinaryAssociation = BinaryAssociation(
    name="ShftGagL307",
    ends={
        Property(name="fastfst_nShftGagL", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst308", type=fastfst_nShftGagL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NTwGages309: BinaryAssociation = BinaryAssociation(
    name="NTwGages309",
    ends={
        Property(name="fastfst_iNTwGages", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst310", type=fastfst_iNTwGages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TwrGagNd311: BinaryAssociation = BinaryAssociation(
    name="TwrGagNd311",
    ends={
        Property(name="fastfst_aTwrGagNd", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst312", type=fastfst_aTwrGagNd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
NBlGages313: BinaryAssociation = BinaryAssociation(
    name="NBlGages313",
    ends={
        Property(name="fastfst_iNBlGages", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst314", type=fastfst_iNBlGages, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BldGagNd315: BinaryAssociation = BinaryAssociation(
    name="BldGagNd315",
    ends={
        Property(name="fastfst_aBldGagNd", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst316", type=fastfst_aBldGagNd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutList317: BinaryAssociation = BinaryAssociation(
    name="OutList317",
    ends={
        Property(name="fastfst_vOutList", type=fastfst_ModelFastfst, multiplicity=Multiplicity(1, 1)),
        Property(name="fastfst_ModelFastfst318", type=fastfst_vOutList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="fastfst",
    types={fastfst_Section, fastfst_bEcho, fastfst_iADAMSPrep, fastfst_iAnalMode, fastfst_iNumBl, fastfst_ModelFastfst, fastfst_Header, fastfst_nTHSSBrDp, fastfst_nTiDynBrk, fastfst_nTMax, fastfst_nDT, fastfst_iYCMode, fastfst_nTYCOn, fastfst_iPCMode, fastfst_nTPCOn, fastfst_iVSContrl, fastfst_nVS_RtGnSp, fastfst_nVS_RtTq, fastfst_nVS_Rgn2K, fastfst_nVS_SlPc, fastfst_iGenModel, fastfst_bGenTiStr, fastfst_bGenTiStp, fastfst_nSpdGenOn, fastfst_nTimGenOn, fastfst_nTimGenOf, fastfst_iHSSBrMode, fastfst_nTBDepISp_1_, fastfst_nTTpBrDp_1_, fastfst_nTTpBrDp_2_, fastfst_nTTpBrDp_3_, fastfst_nNacYawF, fastfst_nTBDepISp_2_, fastfst_nTBDepISp_3_, fastfst_nTYawManS, fastfst_nTYawManE, fastfst_nTPitManS_1_, fastfst_nTPitManS_2_, fastfst_nTPitManS_3_, fastfst_nTPitManE_1_, fastfst_nBlPitch_3_, fastfst_nTPitManE_2_, fastfst_nTPitManE_3_, fastfst_nBlPitch_1_, fastfst_nBlPitch_2_, fastfst_nGravity, fastfst_nBlPitchF_1_, fastfst_nBlPitchF_2_, fastfst_nBlPitchF_3_, fastfst_bTwFADOF2, fastfst_bFlapDOF1, fastfst_bFlapDOF2, fastfst_bEdgeDOF, fastfst_bTeetDOF, fastfst_bDrTrDOF, fastfst_bGenDOF, fastfst_bYawDOF, fastfst_bTwFADOF1, fastfst_nAzimuth, fastfst_nRotSpeed, fastfst_bTwSSDOF1, fastfst_bTwSSDOF2, fastfst_bCompAero, fastfst_bCompNoise, fastfst_nOoPDefl, fastfst_nIPDefl, fastfst_nTeetDefl, fastfst_nNacYaw, fastfst_nTTDspFA, fastfst_nTTDspSS, fastfst_nTipRad, fastfst_nHubRad, fastfst_nPSpnElN, fastfst_nUndSling, fastfst_nNacCMzn, fastfst_nHubCM, fastfst_nOverHang, fastfst_nTowerHt, fastfst_nTwr2Shft, fastfst_nTwrRBHt, fastfst_nShftTilt, fastfst_nDelta3, fastfst_nPreCone_1_, fastfst_nPreCone_2_, fastfst_nPreCone_3_, fastfst_nAzimB1Up, fastfst_nNacCMxn, fastfst_nNacCMyn, fastfst_nNacMass, fastfst_nHubMass, fastfst_nTipMass_1_, fastfst_nTipMass_2_, fastfst_nTipMass_3_, fastfst_nNacYIner, fastfst_nGenIner, fastfst_nHubIner, fastfst_nGBoxEff, fastfst_nGenEff, fastfst_nGBRatio, fastfst_nYawBrMass, fastfst_bGBRevers, fastfst_nHSSBrTqF, fastfst_nHSSBrDT, fastfst_fDynBrkFi, fastfst_nDTTorSpr, fastfst_nDTTorDmp, fastfst_nSIG_SlPc, fastfst_nSIG_SySp, fastfst_nSIG_RtTq, fastfst_nSIG_PORt, fastfst_fPtfmFile, fastfst_nTEC_Freq, fastfst_nTEC_Npol, fastfst_nTEC_Sres, fastfst_nTEC_Rres, fastfst_nTEC_VLL, fastfst_nTEC_SLR, fastfst_nTEC_RLR, fastfst_nTEC_MR, fastfst_iPtfmModel, fastfst_iTwrNodes, fastfst_fTwrFile, fastfst_nYawSpr, fastfst_nYawDamp, fastfst_nYawNeut, fastfst_bFurling, fastfst_fFurlFile, fastfst_iTeetMod, fastfst_nTeetDmpP, fastfst_nTeetDmp, fastfst_nTeetCDmp, fastfst_nTeetSStP, fastfst_nTeetHStP, fastfst_nTeetSSSp, fastfst_nTeetHSSp, fastfst_nTBDrConN, fastfst_nTBDrConD, fastfst_nTpBrDT, fastfst_fBldFile_1_, fastfst_fBldFile_2_, fastfst_fBldFile_3_, fastfst_fADFile, fastfst_fNoiseFile, fastfst_fADAMSFile, fastfst_fLinFile, fastfst_bSumPrint, fastfst_bOutFileFmt, fastfst_bTabDelim, fastfst_sOutFmt, fastfst_nTStart, fastfst_iDecFact, fastfst_nSttsTime, fastfst_nNcIMUxn, fastfst_nNcIMUyn, fastfst_nNcIMUzn, fastfst_nShftGagL, fastfst_iNTwGages, fastfst_aTwrGagNd, fastfst_iNBlGages, fastfst_aBldGagNd, fastfst_vOutList},
    associations={Head0, sections1, Echo3, ADAMSPrep5, AnalMode7, HSSBrMode45, THSSBrDp47, TiDynBrk49, NumBl9, TMax11, DT13, YCMode15, TYCOn17, PCMode19, TPCOn21, VSContrl23, VS_RtGnSp25, VS_RtTq27, VS_Rgn2K29, VS_SlPc31, GenModel33, GenTiStr35, GenTiStp37, SpdGenOn39, TimGenOn41, TimGenOf43, TBDepISp_1_57, TTpBrDp_1_51, TTpBrDp_2_53, TTpBrDp_3_55, NacYawF67, TBDepISp_2_59, TBDepISp_3_61, TYawManS63, TYawManE65, TPitManE_1_75, TPitManS_1_69, TPitManS_2_71, TPitManS_3_73, BlPitch_3_85, TPitManE_2_77, TPitManE_3_79, BlPitch_1_81, BlPitch_2_83, Gravity93, BlPitchF_1_87, BlPitchF_2_89, BlPitchF_3_91, TwFADOF2111, FlapDOF195, FlapDOF297, EdgeDOF99, TeetDOF101, DrTrDOF103, GenDOF105, YawDOF107, TwFADOF1109, Azimuth127, TwSSDOF1113, TwSSDOF2115, CompAero117, CompNoise119, OoPDefl121, IPDefl123, TeetDefl125, RotSpeed129, NacYaw131, TTDspFA133, TTDspSS135, TipRad137, HubRad139, PSpnElN141, UndSling143, NacCMyn151, NacCMzn153, HubCM145, TowerHt155, Twr2Shft157, TwrRBHt159, ShftTilt161, Delta3163, PreCone_1_165, PreCone_2_167, PreCone_3_169, OverHang147, AzimB1Up171, NacCMxn149, NacMass175, HubMass177, TipMass_1_179, TipMass_2_181, TipMass_3_183, NacYIner185, GenIner187, HubIner189, GBoxEff191, GenEff193, YawBrMass173, GBRevers197, HSSBrTqF199, HSSBrDT201, DynBrkFi203, DTTorSpr205, DTTorDmp207, SIG_SlPc209, SIG_SySp211, SIG_RtTq213, GBRatio195, SIG_PORt215, TEC_Freq217, TEC_Npol219, TEC_Sres221, TEC_Rres223, TEC_VLL225, TEC_SLR227, TEC_RLR229, TEC_MR231, PtfmModel233, PtfmFile235, TwrNodes237, TwrFile239, YawSpr241, YawDamp243, YawNeut245, Furling247, FurlFile249, TeetMod251, TeetDmpP253, TeetDmp255, TeetCDmp257, TeetSStP259, TeetHStP261, TeetSSSp263, TeetHSSp265, TBDrConN267, TBDrConD269, TpBrDT271, BldFile_1_273, BldFile_2_275, BldFile_3_277, ADFile279, NoiseFile281, ADAMSFile283, LinFile285, SumPrint287, OutFileFmt289, TabDelim291, OutFmt293, TStart295, DecFact297, SttsTime299, NcIMUxn301, NcIMUyn303, NcIMUzn305, ShftGagL307, NTwGages309, TwrGagNd311, NBlGages313, BldGagNd315, OutList317},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)