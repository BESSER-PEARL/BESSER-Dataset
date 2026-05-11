from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ImmunizationProgramEligibility(Enum): 
	pass
class AuditEventEntityType(Enum): 
	pass
class RiskProbability(Enum): 
	pass
class ConsentContentCodes(Enum): 
	pass
class ImmunizationReasonCodes(Enum): 
    _429060002 = "_429060002"
    _281657000 = "_281657000"
class EpisodeOfCareType(Enum): 
	pass
class MediaModality(Enum): 
	pass
class ImmunizationOriginCodes(Enum):
    provider = "provider"
    record = "record"
    recall = "recall"
    school = "school"
class CoverageEligibilityResponseAuthSupportCodes(Enum): 
	pass
class ClinicalImpressionPrognosis(Enum): 
	pass
class ListEmptyReasons(Enum): 
	pass
class ImagingStudySeriesPerformerFunction(Enum):
    con = "con"
    vrf = "vrf"
    prf = "prf"
    sprf = "sprf"
    ref = "ref"
class QualityOfEvidenceRating(Enum): 
	pass
class MedicationDispenseStatusReasonCodes(Enum): 
	pass
class ServiceProvisionConditions(Enum): 
	pass
class MediaTypeCode(Enum):
    _110030 = "_110030"
    _110031 = "_110031"
    _110032 = "_110032"
    _110033 = "_110033"
    _110034 = "_110034"
    _110035 = "_110035"
    _110036 = "_110036"
    _110037 = "_110037"
    _110010 = "_110010"
    _110038 = "_110038"
class DischargeDisposition(Enum): 
	pass
class DeviceMetricAndComponentTypes(Enum): 
	pass
class EnteralFormulaAdditiveTypeCode(Enum): 
	pass
class AuditEventSubType(Enum):
    _110132 = "_110132"
    _110133 = "_110133"
    _110120 = "_110120"
    _110121 = "_110121"
    _110122 = "_110122"
    _110123 = "_110123"
    _110124 = "_110124"
    _110125 = "_110125"
    _110126 = "_110126"
    _110127 = "_110127"
    _110128 = "_110128"
    _110129 = "_110129"
    _110130 = "_110130"
    _110131 = "_110131"
    _110134 = "_110134"
    _110135 = "_110135"
    _110136 = "_110136"
    _110137 = "_110137"
    _110138 = "_110138"
    _110139 = "_110139"
    _110140 = "_110140"
    _110141 = "_110141"
    _110142 = "_110142"
class PrecisionEstimateType(Enum): 
	pass
class StudyType(Enum): 
	pass
class EndpointPayloadType(Enum):
    urnihepccedes2007 = "urnihepccedes2007"
    urnihepccaprhandp2008 = "urnihepccaprhandp2008"
    urnihepcchandp2008 = "urnihepcchandp2008"
    urnihepccxphr2007A = "urnihepccxphr2007A"
    urnihepccaps2007 = "urnihepccaps2007"
    urnihepccxdsms2007 = "urnihepccxdsms2007"
    urnihepccxphr2007 = "urnihepccxphr2007"
    urnihepccedr2007 = "urnihepccedr2007"
    urniheitidsgenveloping2014 = "urniheitidsgenveloping2014"
    urnihepccaprlab2008 = "urnihepccaprlab2008"
    urnihepccapredu2008 = "urnihepccapredu2008"
    urnihepccirc2008 = "urnihepccirc2008"
    urnihepcccrc2008 = "urnihepcccrc2008"
    urnihepcccm2008 = "urnihepcccm2008"
    urnihepccic2009 = "urnihepccic2009"
    urnihepcctn2007 = "urnihepcctn2007"
    urnihepccnn2007 = "urnihepccnn2007"
    urnihepccctn2007 = "urnihepccctn2007"
    urnihepccedpn2007 = "urnihepccedpn2007"
    urnihepcchp2008 = "urnihepcchp2008"
    urnihepccldhp2009 = "urnihepccldhp2009"
    urnihepcclds2009 = "urnihepcclds2009"
    urnihepccmds2009 = "urnihepccmds2009"
    urnihepccnds2010 = "urnihepccnds2010"
    urnihepccppvs2010 = "urnihepccppvs2010"
    urnihepcctrs2011 = "urnihepcctrs2011"
    urnihepccets2011 = "urnihepccets2011"
    urnihepccits2011 = "urnihepccits2011"
    urniheitibppc2007 = "urniheitibppc2007"
    urniheitibppcsd2007 = "urniheitibppcsd2007"
    urniheitixdw2011workflowDoc = "urniheitixdw2011workflowDoc"
    urniheitidsgdetached2014 = "urniheitidsgdetached2014"
    urnihepatapsrcancerstomach2010 = "urnihepatapsrcancerstomach2010"
    urnihepatapsrcancerliver2010 = "urnihepatapsrcancerliver2010"
    urniheitixdssdpdf2008 = "urniheitixdssdpdf2008"
    urniheitixdssdtext2008 = "urniheitixdssdtext2008"
    urnihelabxdlab2008 = "urnihelabxdlab2008"
    urniheradText = "urniheradText"
    urniheradPdf = "urniheradPdf"
    urniheradCdAImagingReportStructuredHeadings2013 = "urniheradCdAImagingReportStructuredHeadings2013"
    urnihecardimaging2011 = "urnihecardimaging2011"
    urnihecardCrC2012 = "urnihecardCrC2012"
    urnihecardEprCIE2014 = "urnihecardEprCIE2014"
    urnihedentText = "urnihedentText"
    urnihedentPdf = "urnihedentPdf"
    urnihedentCdAImagingReportStructuredHeadings2013 = "urnihedentCdAImagingReportStructuredHeadings2013"
    urnihepatapsrall2010 = "urnihepatapsrall2010"
    urnihepatapsrcancerall2010 = "urnihepatapsrcancerall2010"
    urnihepatapsrcancerbreast2010 = "urnihepatapsrcancerbreast2010"
    urnihepatapsrcancercolon2010 = "urnihepatapsrcancercolon2010"
    urnihepatapsrcancerprostate2010 = "urnihepatapsrcancerprostate2010"
    urnihepatapsrcancerthyroid2010 = "urnihepatapsrcancerthyroid2010"
    urnihepatapsrcancerlung2010 = "urnihepatapsrcancerlung2010"
    urnihepatapsrcancerskin2010 = "urnihepatapsrcancerskin2010"
    urnihepatapsrcancerkidney2010 = "urnihepatapsrcancerkidney2010"
    urnihepatapsrcancercervix2010 = "urnihepatapsrcancercervix2010"
    urnihepatapsrcancerendometrium2010 = "urnihepatapsrcancerendometrium2010"
    urnihepatapsrcancerovary2010 = "urnihepatapsrcancerovary2010"
    urnihepatapsrcanceresophagus2010 = "urnihepatapsrcanceresophagus2010"
    urnihepatapsrcancerpancreas2010 = "urnihepatapsrcancerpancreas2010"
    urnihepatapsrcancertestis2010 = "urnihepatapsrcancertestis2010"
    urnihepatapsrcancerurinaryBladder2010 = "urnihepatapsrcancerurinaryBladder2010"
    urnihepatapsrcancerlipOralCavity2010 = "urnihepatapsrcancerlipOralCavity2010"
    urnihepatapsrcancerpharynx2010 = "urnihepatapsrcancerpharynx2010"
    urnihepatapsrcancersalivaryGland2010 = "urnihepatapsrcancersalivaryGland2010"
    urnihepatapsrcancerlarynx2010 = "urnihepatapsrcancerlarynx2010"
    urnihepharmpre2010 = "urnihepharmpre2010"
    urnihepharmpadv2010 = "urnihepharmpadv2010"
    urnihepharmdis2010 = "urnihepharmdis2010"
    urnihepharmpml2013 = "urnihepharmpml2013"
    urnhl7orgsdwgccdastructuredBody11 = "urnhl7orgsdwgccdastructuredBody11"
    urnhl7orgsdwgccdanonXmlBody11 = "urnhl7orgsdwgccdanonXmlBody11"
class ResearchStudyReasonStopped(Enum): 
	pass
class LoincDiagnosticReportCodes(Enum): 
	pass
class Diet(Enum): 
	pass
class ImmunizationRouteCodes(Enum):
    im = "im"
    nasinhlc = "nasinhlc"
    ivinj = "ivinj"
    idinj = "idinj"
    po = "po"
    sq = "sq"
    trnsderm = "trnsderm"
class DiagnosisRole(Enum): 
	pass
class ImmunizationFundingSource(Enum): 
	pass
class DefinitionTopic(Enum): 
	pass
class FlagCode(Enum): 
	pass
class DiagnosticServiceSectionCodes(Enum): 
	pass
class EncounterType(Enum): 
	pass
class SnomedctMorphologicAbnormalities(Enum): 
	pass
class VaccineAdministeredValueSet(Enum): 
	pass
class AuditEventSourceType(Enum): 
	pass
class CodesForImmunizationSiteOfAdministration(Enum):
    la = "la"
    ra = "ra"
class MeasureScoring(Enum): 
	pass
class SnomedctDrugTherapyStatusCodes(Enum): 
	pass
class AdverseEventCausalityAssessment(Enum): 
	pass
class CompositeMeasureScoring(Enum): 
	pass
class ProcedureCategoryCodesSnomedcT(Enum): 
	
    _24642003 = "_24642003"
    _409063005 = "_409063005"
    _409073007 = "_409073007"
    _387713003 = "_387713003"
    _103693007 = "_103693007"
    _46947000 = "_46947000"
    _410606002 = "_410606002"
class V3ActReason(Enum): 
	pass 
class AccountTypes(Enum): 
	pass
class ReferralMethod(Enum): 
	pass
class AdjudicationErrorCodes(Enum): 
	pass
class ProcedureNotPerformedReasonSnomeDCT(Enum): 
	pass
class ProcedureDeviceActionCodes(Enum): 
	pass
class EnteralRouteCodes(Enum): 
	
    po = "po"
    eft = "eft"
    entinstl = "entinstl"
    gt = "gt"
    ngt = "ngt"
    ogt = "ogt"
    gjt = "gjt"
    jjtinstl = "jjtinstl"
    ojj = "ojj"
class BasicResourceTypes(Enum): 
	pass
class QuestionnaireQuestionCodes(Enum): 
	pass
class ChargeItemCode(Enum): 
	pass
class FlagCategory(Enum): 
	pass
class MeasureType(Enum): 
	pass
class ConsentScopeCodes(Enum): 
	pass
class ExampleVisionPrescriptionProductCodes(Enum): 
	pass
class MeasureDataUsage(Enum): 
	pass
class TaskCode(Enum): 
	pass
class SpecialArrangements(Enum): 
	pass
class MeasurePopulationType(Enum): 
	pass
class FacilityTypeCodeValueSet(Enum):
    _79993009 = "_79993009"
    _82242000 = "_82242000"
    _225732001 = "_225732001"
    _31628002 = "_31628002"
    _32074000 = "_32074000"
    _4322002 = "_4322002"
    _224687002 = "_224687002"
    _62480006 = "_62480006"
    _80522000 = "_80522000"
    _36125001 = "_36125001"
    _48311003 = "_48311003"
    _284546000 = "_284546000"
    _42665001 = "_42665001"
    _45618002 = "_45618002"
    _418518002 = "_418518002"
    _73770003 = "_73770003"
    _69362002 = "_69362002"
    _52668009 = "_52668009"
    _360957003 = "_360957003"
    _10206005 = "_10206005"
    _37550003 = "_37550003"
    _73644007 = "_73644007"
    _79491001 = "_79491001"
    _33022008 = "_33022008"
    _58482006 = "_58482006"
    _90484001 = "_90484001"
    _1814000 = "_1814000"
    _22549003 = "_22549003"
    _56293002 = "_56293002"
    _360966004 = "_360966004"
    _2849009 = "_2849009"
    _14866005 = "_14866005"
    _38238005 = "_38238005"
    _56189001 = "_56189001"
    _89972002 = "_89972002"
    _78088001 = "_78088001"
    _78001009 = "_78001009"
    _23392004 = "_23392004"
    _36293008 = "_36293008"
    _3729002 = "_3729002"
    _5584006 = "_5584006"
    _37546005 = "_37546005"
    _57159002 = "_57159002"
    _331006 = "_331006"
    _50569004 = "_50569004"
    _46224007 = "_46224007"
    _81234003 = "_81234003"
    _19602009 = "_19602009"
    _39350007 = "_39350007"
    _83891005 = "_83891005"
    _394759007 = "_394759007"
    _405607001 = "_405607001"
    _309900005 = "_309900005"
    _275576008 = "_275576008"
    _10531005 = "_10531005"
    _91154008 = "_91154008"
    _41844007 = "_41844007"
    _45899008 = "_45899008"
    _51563005 = "_51563005"
    _1773006 = "_1773006"
    _72311000 = "_72311000"
    _6827000 = "_6827000"
    _309898008 = "_309898008"
    _39913001 = "_39913001"
    _77931003 = "_77931003"
    _25681007 = "_25681007"
    _20078004 = "_20078004"
    _35971002 = "_35971002"
    _11424001 = "_11424001"
    _409519008 = "_409519008"
    _901005 = "_901005"
    _2081004 = "_2081004"
    _59374000 = "_59374000"
    _413456002 = "_413456002"
    _413817003 = "_413817003"
    _310205006 = "_310205006"
    _419955002 = "_419955002"
    _272501009 = "_272501009"
    _394777002 = "_394777002"
class ResourceType(Enum):
    careTeam = "careTeam"
    catalogEntry = "catalogEntry"
    account = "account"
    activityDefinition = "activityDefinition"
    adverseEvent = "adverseEvent"
    allergyIntolerance = "allergyIntolerance"
    appointment = "appointment"
    appointmentResponse = "appointmentResponse"
    auditEvent = "auditEvent"
    basic = "basic"
    binary = "binary"
    biologicallyDerivedProduct = "biologicallyDerivedProduct"
    bodyStructure = "bodyStructure"
    bundle = "bundle"
    documentManifest = "documentManifest"
    capabilityStatement = "capabilityStatement"
    documentReference = "documentReference"
    chargeItem = "chargeItem"
    chargeItemDefinition = "chargeItemDefinition"
    carePlan = "carePlan"
    claim = "claim"
    claimResponse = "claimResponse"
    clinicalImpression = "clinicalImpression"
    codeSystem = "codeSystem"
    communication = "communication"
    communicationRequest = "communicationRequest"
    compartmentDefinition = "compartmentDefinition"
    composition = "composition"
    conceptMap = "conceptMap"
    condition = "condition"
    consent = "consent"
    contract = "contract"
    coverage = "coverage"
    coverageEligibilityRequest = "coverageEligibilityRequest"
    coverageEligibilityResponse = "coverageEligibilityResponse"
    detectedIssue = "detectedIssue"
    device = "device"
    deviceDefinition = "deviceDefinition"
    deviceMetric = "deviceMetric"
    deviceRequest = "deviceRequest"
    deviceUseStatement = "deviceUseStatement"
    diagnosticReport = "diagnosticReport"
    immunization = "immunization"
    domainResource = "domainResource"
    effectEvidenceSynthesis = "effectEvidenceSynthesis"
    encounter = "encounter"
    endpoint = "endpoint"
    enrollmentRequest = "enrollmentRequest"
    enrollmentResponse = "enrollmentResponse"
    episodeOfCare = "episodeOfCare"
    eventDefinition = "eventDefinition"
    evidence = "evidence"
    evidenceVariable = "evidenceVariable"
    exampleScenario = "exampleScenario"
    explanationOfBenefit = "explanationOfBenefit"
    familyMemberHistory = "familyMemberHistory"
    flag = "flag"
    goal = "goal"
    graphDefinition = "graphDefinition"
    group = "group"
    guidanceResponse = "guidanceResponse"
    healthcareService = "healthcareService"
    imagingStudy = "imagingStudy"
    medicinalProductContraindication = "medicinalProductContraindication"
    immunizationEvaluation = "immunizationEvaluation"
    immunizationRecommendation = "immunizationRecommendation"
    implementationGuide = "implementationGuide"
    insurancePlan = "insurancePlan"
    invoice = "invoice"
    library = "library"
    linkage = "linkage"
    list = "list"
    location = "location"
    measure = "measure"
    measureReport = "measureReport"
    media = "media"
    medication = "medication"
    medicationAdministration = "medicationAdministration"
    medicationDispense = "medicationDispense"
    medicationKnowledge = "medicationKnowledge"
    medicationRequest = "medicationRequest"
    medicationStatement = "medicationStatement"
    medicinalProduct = "medicinalProduct"
    medicinalProductAuthorization = "medicinalProductAuthorization"
    paymentReconciliation = "paymentReconciliation"
    person = "person"
    medicinalProductIndication = "medicinalProductIndication"
    medicinalProductIngredient = "medicinalProductIngredient"
    medicinalProductInteraction = "medicinalProductInteraction"
    medicinalProductManufactured = "medicinalProductManufactured"
    medicinalProductPackaged = "medicinalProductPackaged"
    medicinalProductPharmaceutical = "medicinalProductPharmaceutical"
    medicinalProductUndesirableEffect = "medicinalProductUndesirableEffect"
    messageDefinition = "messageDefinition"
    messageHeader = "messageHeader"
    molecularSequence = "molecularSequence"
    namingSystem = "namingSystem"
    nutritionOrder = "nutritionOrder"
    observation = "observation"
    observationDefinition = "observationDefinition"
    operationDefinition = "operationDefinition"
    operationOutcome = "operationOutcome"
    organization = "organization"
    organizationAffiliation = "organizationAffiliation"
    parameters = "parameters"
    patient = "patient"
    paymentNotice = "paymentNotice"
    structureDefinition = "structureDefinition"
    planDefinition = "planDefinition"
    practitioner = "practitioner"
    practitionerRole = "practitionerRole"
    procedure = "procedure"
    provenance = "provenance"
    questionnaire = "questionnaire"
    questionnaireResponse = "questionnaireResponse"
    relatedPerson = "relatedPerson"
    requestGroup = "requestGroup"
    researchDefinition = "researchDefinition"
    researchElementDefinition = "researchElementDefinition"
    researchStudy = "researchStudy"
    researchSubject = "researchSubject"
    resource = "resource"
    riskAssessment = "riskAssessment"
    riskEvidenceSynthesis = "riskEvidenceSynthesis"
    schedule = "schedule"
    searchParameter = "searchParameter"
    serviceRequest = "serviceRequest"
    slot = "slot"
    specimen = "specimen"
    specimenDefinition = "specimenDefinition"
    structureMap = "structureMap"
    subscription = "subscription"
    substance = "substance"
    substanceNucleicAcid = "substanceNucleicAcid"
    substancePolymer = "substancePolymer"
    substanceProtein = "substanceProtein"
    substanceReferenceInformation = "substanceReferenceInformation"
    substanceSourceMaterial = "substanceSourceMaterial"
    substanceSpecification = "substanceSpecification"
    supplyDelivery = "supplyDelivery"
    supplyRequest = "supplyRequest"
    task = "task"
    terminologyCapabilities = "terminologyCapabilities"
    testReport = "testReport"
    testScript = "testScript"
    valueSet = "valueSet"
    verificationResult = "verificationResult"
    visionPrescription = "visionPrescription"
class EnteralFormulaTypeCodes(Enum):
    _442961000124107 = "_442961000124107"
    _442951000124105 = "_442951000124105"
    _442941000124108 = "_442941000124108"
    _443031000124106 = "_443031000124106"
    _443051000124104 = "_443051000124104"
    _442911000124109 = "_442911000124109"
    _443021000124108 = "_443021000124108"
    _442971000124100 = "_442971000124100"
    _442981000124102 = "_442981000124102"
    _442991000124104 = "_442991000124104"
    _443111000124101 = "_443111000124101"
    _443011000124100 = "_443011000124100"
    _443431000124102 = "_443431000124102"
    _443411000124108 = "_443411000124108"
    _442921000124101 = "_442921000124101"
    _442931000124103 = "_442931000124103"
    _443361000124100 = "_443361000124100"
    _443401000124105 = "_443401000124105"
    _443491000124103 = "_443491000124103"
    _443501000124106 = "_443501000124106"
    _443421000124100 = "_443421000124100"
    _443471000124104 = "_443471000124104"
    _444431000124104 = "_444431000124104"
    _443451000124109 = "_443451000124109"
    _441561000124106 = "_441561000124106"
    _443461000124106 = "_443461000124106"
    _441531000124102 = "_441531000124102"
    _443561000124107 = "_443561000124107"
    _443481000124101 = "_443481000124101"
    _441571000124104 = "_441571000124104"
    _441591000124103 = "_441591000124103"
    _441601000124106 = "_441601000124106"
    _443351000124102 = "_443351000124102"
    _443771000124106 = "_443771000124106"
    _441671000124100 = "_441671000124100"
    _442651000124102 = "_442651000124102"
class CommunicationNotDoneReason(Enum): 
	pass
class MediaType(Enum): 
	pass
class V3ActPriority(Enum): 
	pass
class ImmunizationStatusReasonCodes(Enum):
    immune = "immune"
    medprec = "medprec"
    ostock = "ostock"
    patobj = "patobj"
class Laterality(Enum):
    _419161000 = "_419161000"
    _419465000 = "_419465000"
    _51440002 = "_51440002"
class PatientContactRelationship(Enum): 
	pass
class V3ActPharmacySupplyType(Enum): 
	pass
class MaritalStatusCodes(Enum):
    unk = "unk"
class VitalSigns(Enum):
    _84806 = "_84806"
    _84624 = "_84624"
    _84780 = "_84780"
    _853531 = "_853531"
    _92791 = "_92791"
    _88674 = "_88674"
    _27086 = "_27086"
    _83105 = "_83105"
    _83022 = "_83022"
    _98434 = "_98434"
    _294637 = "_294637"
    _391565 = "_391565"
    _853549 = "_853549"
class ConsentActionCodes(Enum): 
	pass
class MedicationKnowledgePackageTypeCodes(Enum): 
	pass
class MedicationDispenseCategoryCodes(Enum): 
	pass
class RiskEstimateType(Enum): 
	pass
class QuestionnaireAnswerCodes(Enum): 
	pass
class V20092(Enum): 
	pass
class SpecialCourtesy(Enum):
    unk = "unk"
    ext = "ext"
    nrm = "nrm"
    prf = "prf"
    stf = "stf"
    vip = "vip"
class UnitTypeCodes(Enum): 
	pass
class AdmitSource(Enum): 
	pass
class ImmunizationSubpotentReason(Enum): 
	pass
class FormCodes(Enum): 
	pass
class GoalPriority(Enum): 
	pass
class ListOrderCodes(Enum): 
	pass
class SynthesisType(Enum): 
	pass
class ResearchStudyObjectiveType(Enum): 
	pass
class NetworkTypeCodes(Enum): 
	pass
class ResearchStudyPhase(Enum): 
	pass
class CertaintySubcomponentType(Enum): 
	pass
class ImmunizationEvaluationTargetDiseaseCodes(Enum):
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
    _27836007 = "_27836007"
    _398102009 = "_398102009"
class Program(Enum): 
	pass
class AcquisitionModality(Enum):
    px = "px"
    srf = "srf"
    opm = "opm"
    opr = "opr"
    mg = "mg"
    sm = "sm"
    opv = "opv"
    dx = "dx"
    opt = "opt"
    bmd = "bmd"
    oam = "oam"
    nm = "nm"
    us = "us"
    oct = "oct"
    op = "op"
    ivoct = "ivoct"
    mr = "mr"
    ecg = "ecg"
    gm = "gm"
    io = "io"
    xa = "xa"
    xc = "xc"
    va = "va"
    ivus = "ivus"
    cr = "cr"
    es = "es"
    ar = "ar"
    ct = "ct"
    oss = "oss"
    len = "len"
    rg = "rg"
    rf = "rf"
    ker = "ker"
    hd = "hd"
    bdus = "bdus"
    pt = "pt"
    eps = "eps"
class ProcedureOutcomeCodesSnomedcT(Enum):
    _385669000 = "_385669000"
    _385671000 = "_385671000"
    _385670004 = "_385670004"
class V3ActEncounterCode(Enum): 
	pass
class MedicationKnowledgeCharacteristicCodes(Enum): 
	pass
class ServiceType(Enum): 
	pass
class IcD10Codes(Enum):
    _123456 = "_123456"
    _123457 = "_123457"
    _987654 = "_987654"
    _123987 = "_123987"
    _112233 = "_112233"
    _997755 = "_997755"
    _321789 = "_321789"
class AdverseEventSeriousness(Enum): 
	pass
class BenefitTypeCodes(Enum): 
	pass
class ExampleUseCodesForList(Enum): 
	pass
class ConditionStageType(Enum):
    _261023001 = "_261023001"
    _260998006 = "_260998006"
class LibraryType(Enum): 
	pass
class ConditionCategoryCodes(Enum): 
	pass
class AuditEventEntityRole(Enum): 
	pass
class ConsentCategoryCodes(Enum):
    _592840 = "_592840"
    _570168 = "_570168"
    _570176 = "_570176"
    _642926 = "_642926"
class BenefitTermCodes(Enum): 
	pass
class MedicationStatusCodes(Enum): 
	pass
class AdverseEventCausalityMethod(Enum): 
	pass
class AuditEventId(Enum):
    _110106 = "_110106"
    _110107 = "_110107"
    _110108 = "_110108"
    _110109 = "_110109"
    _110110 = "_110110"
    _110100 = "_110100"
    _110101 = "_110101"
    _110102 = "_110102"
    _110103 = "_110103"
    _110104 = "_110104"
    _110105 = "_110105"
    _110111 = "_110111"
    _110112 = "_110112"
    _110113 = "_110113"
    _110114 = "_110114"
class ConsentPolicyRuleCodes(Enum): 
	pass
class SnomedctFormCodes(Enum): 
	pass
class PatientMedicineChangeTypes(Enum): 
	pass
class ResearchStudyPrimaryPurposeType(Enum): 
	pass
class ParticipationRoleType(Enum):
    affl = "affl"
    agnt = "agnt"
    assigned = "assigned"
    claim = "claim"
    amender = "amender"
    coauth = "coauth"
    cont = "cont"
    evtwit = "evtwit"
    primauth = "primauth"
    reviewer = "reviewer"
    source = "source"
    trans = "trans"
    valid = "valid"
    verf = "verf"
    dpowatt = "dpowatt"
    excest = "excest"
    covpty = "covpty"
    depen = "depen"
    econ = "econ"
    emp = "emp"
    guard = "guard"
    invsbj = "invsbj"
    named = "named"
    nok = "nok"
    pat = "pat"
    prov = "prov"
    not_ = "not_"
    classifier = "classifier"
    consenter = "consenter"
    conswit = "conswit"
    copart = "copart"
    declassifier = "declassifier"
    delegatee = "delegatee"
    delegator = "delegator"
    downgrder = "downgrder"
    _110150 = "_110150"
    _110151 = "_110151"
    _110152 = "_110152"
    grantee = "grantee"
    grantor = "grantor"
    gt = "gt"
    guadltm = "guadltm"
    hpowatt = "hpowatt"
    intprter = "intprter"
    powatt = "powatt"
    resprsn = "resprsn"
    spowatt = "spowatt"
    aucg = "aucg"
    aulr = "aulr"
    autm = "autm"
    auwa = "auwa"
    promsk = "promsk"
    aut = "aut"
    cst = "cst"
    inf = "inf"
    ircp = "ircp"
    la = "la"
    ircpa = "ircpa"
    trc = "trc"
    wit = "wit"
    _110153 = "_110153"
    _110154 = "_110154"
    _110155 = "_110155"
class GoalStartEvent(Enum):
    _32485007 = "_32485007"
    _308283009 = "_308283009"
    _442137000 = "_442137000"
    _386216000 = "_386216000"
class MediaCollectionViewProjection(Enum): 
	pass
class ImmunizationFunctionCodes(Enum):
    op = "op"
    ap = "ap"
class MedicationDispensePerformerFunctionCodes(Enum): 
	pass
class ObjectLifecycleEvents(Enum): 
	pass
class ProcedureFollowUpCodesSnomedcT(Enum):
    _18949003 = "_18949003"
    _30549001 = "_30549001"
    _241031001 = "_241031001"
    _35963001 = "_35963001"
    _225164002 = "_225164002"
    _447346005 = "_447346005"
    _229506003 = "_229506003"
    _274441001 = "_274441001"
    _394725008 = "_394725008"
    _359825008 = "_359825008"
class ImmunizationEvaluationDoseStatusReasonCodes(Enum): 
	pass
class ContractTermSubtypeCodes(Enum): 
	pass
class DataType(Enum):
    address = "address"
    age = "age"
    identifier = "identifier"
    marketingStatus = "marketingStatus"
    meta = "meta"
    money = "money"
    moneyQuantity = "moneyQuantity"
    annotation = "annotation"
    attachment = "attachment"
    backboneElement = "backboneElement"
    codeableConcept = "codeableConcept"
    coding = "coding"
    contactDetail = "contactDetail"
    contactPoint = "contactPoint"
    contributor = "contributor"
    count = "count"
    dataRequirement = "dataRequirement"
    distance = "distance"
    dosage = "dosage"
    duration = "duration"
    element = "element"
    elementDefinition = "elementDefinition"
    expression = "expression"
    extension = "extension"
    humanName = "humanName"
    base64Binary = "base64Binary"
    boolean = "boolean"
    canonical = "canonical"
    code = "code"
    date = "date"
    dateTime = "dateTime"
    decimal = "decimal"
    id = "id"
    instant = "instant"
    integer = "integer"
    markdown = "markdown"
    narrative = "narrative"
    parameterDefinition = "parameterDefinition"
    period = "period"
    population = "population"
    prodCharacteristic = "prodCharacteristic"
    productShelfLife = "productShelfLife"
    quantity = "quantity"
    range = "range"
    ratio = "ratio"
    reference = "reference"
    relatedArtifact = "relatedArtifact"
    sampledData = "sampledData"
    signature = "signature"
    simpleQuantity = "simpleQuantity"
    substanceAmount = "substanceAmount"
    timing = "timing"
    triggerDefinition = "triggerDefinition"
    usageContext = "usageContext"
    oid = "oid"
    positiveInt = "positiveInt"
    string = "string"
    time = "time"
    unsignedInt = "unsignedInt"
    uri = "uri"
    url = "url"
    uuid = "uuid"
    xhtml = "xhtml"
class SupplyRequestReason(Enum): 
	pass
class TimingAbbreviation(Enum): 
	
    q6h = "q6h"
    q8h = "q8h"
    bid = "bid"
    tid = "tid"
    qid = "qid"
    am = "am"
    pm = "pm"
    qd = "qd"
    qod = "qod"
    q1h = "q1h"
    q2h = "q2h"
    q3h = "q3h"
    q4h = "q4h"
    bed = "bed"
    wk = "wk"
    mo = "mo"
class V3SubstanceAdminSubstitutionReason(Enum): 
	pass
class ImmunizationRecommendationTargetDiseaseCodes(Enum):
    _27836007 = "_27836007"
    _398102009 = "_398102009"
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
class ExampleMessageReasonCodes(Enum): 
	pass
class ExamplePaymentTypeCodes(Enum): 
	pass
class ContactEntityType(Enum): 
	pass
class SpecimenProcessingProcedure(Enum): 
	pass
class DetectedIssueMitigationAction(Enum): 
	pass
class AppointmentCancellationReason(Enum): 
	pass
class ExampleDiagnosisOnAdmissionCodes(Enum): 
	pass
class ActionType(Enum): 
	pass
class SubscriberRelationshipCodes(Enum): 
	pass
class FoodTypeCodes(Enum): 
	pass
class TextureModifierCodes(Enum):
    _228053002 = "_228053002"
    _439091000124107 = "_439091000124107"
    _228049004 = "_228049004"
    _441881000124103 = "_441881000124103"
    _441761000124103 = "_441761000124103"
    _441751000124100 = "_441751000124100"
    _228059003 = "_228059003"
    _441791000124106 = "_441791000124106"
    _228055009 = "_228055009"
    _228056005 = "_228056005"
    _441771000124105 = "_441771000124105"
    _228057001 = "_228057001"
    _228058006 = "_228058006"
    _228060008 = "_228060008"
class ConditionProblemDiagnosisCodes(Enum):
    _160245001 = "_160245001"
class SnomedctMedicationAsNeededReasonCodes(Enum): 
	pass
class ExampleRelatedClaimRelationshipCodes(Enum): 
	pass
class PractitionerRole(Enum): 
	pass
class ExceptionCodes(Enum): 
	pass
class PatientRelationshipType(Enum): 
	pass
class AllSecurityLabels(Enum): 
	pass
class SnomedctBodyStructures(Enum): 
	pass
class CareTeamCategory(Enum): 
	pass
class ObservationMethods(Enum): 
	pass
class MedicationRequestCourseOfTherapyCodes(Enum): 
	pass
class SnomedctSupplyItem(Enum): 
	pass
class ImmunizationRecommendationDateCriterionCodes(Enum):
    _309815 = "_309815"
    _309807 = "_309807"
    _597773 = "_597773"
    _597781 = "_597781"
class ProcedureCodesSnomedcT(Enum): 
	pass
class ContractResourceDecisionModeCodes(Enum): 
	pass
class V3PurposeOfUse(Enum): 
	pass
class ExampleDiagnosisTypeCodes(Enum): 
	pass
class PreparePatient(Enum): 
	pass
class ConditionOutcomeCodes(Enum): 
	pass
class ContractResourceDefinitionTypeCodes(Enum): 
	pass
class SubstanceCode(Enum): 
	pass
class ClaimInformationCategoryCodes(Enum): 
	pass
class DataAbsentReason(Enum): 
	pass
class DocumentReferenceFormatCodeSet(Enum): 
	pass
class OrganizationType(Enum): 
	pass
class Validationstatus(Enum): 
	pass
class V2036027(Enum): 
	pass
class CommunicationTopic(Enum): 
	pass
class OperationOutcomeCodes(Enum): 
	pass
class ContractResourceExpirationTypeCodes(Enum): 
	pass
class ActionParticipantRole(Enum): 
	pass
class CoverageTypeAndSelfPayCodes(Enum): 
	pass
class ContractActionCodes(Enum): 
	pass
class HandlingConditionSet(Enum): 
	pass
class Failureaction(Enum): 
	pass
class ContractResourceDefinitionSubtypeCodes(Enum): 
	pass
class ContractResourceAssetScopeCodes(Enum): 
	pass
class SnomedctClinicalFindings(Enum): 
	pass
class FhirSpecimenCollectionMethod(Enum):
    _386089008 = "_386089008"
    _278450005 = "_278450005"
    _129316008 = "_129316008"
    _129314006 = "_129314006"
    _129300006 = "_129300006"
    _129304002 = "_129304002"
    _129323009 = "_129323009"
    _73416001 = "_73416001"
    _225113003 = "_225113003"
    _70777001 = "_70777001"
class ReasonMedicationGivenCodes(Enum): 
	pass
class V3ActCode(Enum): 
	pass
class FdAStandardSequence(Enum): 
	pass
class V20916(Enum): 
	pass
class UcumCodes(Enum): 
	pass
class ImmunizationRecommendationReasonCodes(Enum):
    _77176002 = "_77176002"
    _77386006 = "_77386006"
class LocationType(Enum): 
	pass
class ObservationCategoryCodes(Enum): 
	pass
class ExampleRevenueCenterCodes(Enum): 
	pass
class AllergyIntoleranceSubstanceProductConditionAndNegationCodes(Enum): 
	pass
class ClaimPayeeTypeCodes(Enum): 
	pass
class ContainerCap(Enum): 
	pass
class Need(Enum): 
	pass
class AdverseEventCategory(Enum): 
	pass
class FhirDeviceTypes(Enum): 
	pass
class ObservationInterpretationCodes(Enum): 
	pass
class ProvenanceParticipantRole(Enum): 
	pass
class PaymentTypeCodes(Enum): 
	pass
class ContractResourceActionStatusCodes(Enum): 
	pass
class V20487(Enum): 
	pass
class ServiceRequestCategoryCodes(Enum): 
	
    _108252007 = "_108252007"
    _363679005 = "_363679005"
    _409063005 = "_409063005"
    _409073007 = "_409073007"
    _387713003 = "_387713003"
class V3ActSubstanceAdminSubstitutionCode(Enum): 
	pass
class OrganizationAffiliationRole(Enum): 
	pass
class OralSiteCodes(Enum): 
	pass
class NutrientModifierCodes(Enum):
    _33463005 = "_33463005"
    _39972003 = "_39972003"
    _88480006 = "_88480006"
class InvestigationType(Enum): 
	
    _271336007 = "_271336007"
    _160237006 = "_160237006"
class Ensembl(Enum): 
	pass
class TestScriptProfileOriginType(Enum): 
	pass
class DocumentClassValueSet(Enum): 
	
    _297515 = "_297515"
    _297523 = "_297523"
    _113696 = "_113696"
    _114850 = "_114850"
    _114868 = "_114868"
    _114884 = "_114884"
    _115063 = "_115063"
    _115436 = "_115436"
    _155085 = "_155085"
    _187260 = "_187260"
    _187617 = "_187617"
    _188425 = "_188425"
    _264366 = "_264366"
    _264416 = "_264416"
    _264424 = "_264424"
    _278952 = "_278952"
    _278960 = "_278960"
    _278978 = "_278978"
    _278986 = "_278986"
    _285700 = "_285700"
    _286195 = "_286195"
    _286344 = "_286344"
    _297499 = "_297499"
    _297507 = "_297507"
    _341099 = "_341099"
    _341172 = "_341172"
    _341214 = "_341214"
    _341222 = "_341222"
    _341339 = "_341339"
    _341404 = "_341404"
    _347484 = "_347484"
    _347757 = "_347757"
    _470393 = "_470393"
    _470427 = "_470427"
    _470450 = "_470450"
    _470468 = "_470468"
    _470492 = "_470492"
    _570176 = "_570176"
    _570168 = "_570168"
    _564450 = "_564450"
    _535765 = "_535765"
    _564476 = "_564476"
    _187484 = "_187484"
    _115048 = "_115048"
    _571331 = "_571331"
class Primarysourcetype(Enum): 
	pass
class V3ServiceDeliveryLocationRoleType(Enum): 
	pass
class PaymentAdjustmentReasonCodes(Enum): 
	pass
class SubstanceCategoryCodes(Enum): 
	pass
class ExampleProgramReasonCodes(Enum): 
	pass
class DesignationUse(Enum):
    _900000000000003001 = "_900000000000003001"
    _900000000000013009 = "_900000000000013009"
class ObservationReferenceRangeMeaningCodes(Enum): 
	pass
class SurfaceCodes(Enum): 
	pass
class MissingToothReasonCodes(Enum): 
	pass
class ConditionDiagnosisSeverity(Enum): 
	
    _24484000 = "_24484000"
    _6736007 = "_6736007"
    _255604002 = "_255604002"
class ImmunizationRecommendationStatusCodes(Enum): 
	pass
class EffectEstimateType(Enum): 
	pass
class InsurancePlanType(Enum): 
	pass
class RejectionCriterion(Enum): 
	pass
class DoseAndRateType(Enum): 
	pass
class MessageEvent(Enum): 
	pass
class ProcessPriorityCodes(Enum): 
	pass
class DeviceSafety(Enum):
    c106046 = "c106046"
    c106045 = "c106045"
    c106047 = "c106047"
    c113844 = "c113844"
    c101673 = "c101673"
    c106038 = "c106038"
class V20493(Enum): 
	pass
class UsageContextType(Enum): 
	pass
class SnomedctReasonMedicationNotGivenCodes(Enum): 
	pass
class ContractResourceAssetSubTypeCodes(Enum): 
	pass
class ExampleProviderQualificationCodes(Enum): 
	pass
class IcD10ProcedureCodes(Enum): 
	pass
class ContractResourceAssetContextCodes(Enum): 
	pass
class FdAMethod(Enum): 
	pass
class PlanDefinitionType(Enum): 
	pass
class MedicationAdministrationCategoryCodes(Enum): 
	pass
class Validationprocess(Enum): 
	pass
class DeviceType(Enum): 
	pass
class ConsentContentClass(Enum): 
	
    httphl7orgfhirStructureDefinitionlipidprofile = "httphl7orgfhirStructureDefinitionlipidprofile"
    applicationhl7cdaxml = "applicationhl7cdaxml"
class SignatureTypeCodes(Enum): 
	pass
class Chromosomehuman(Enum): 
	pass
class V3ParticipationMode(Enum): 
	pass
class ContractResourceScopeCodesA(Enum): 
	pass
class EndpointConnectionType(Enum): 
	pass
class V20116(Enum): 
	pass
class ExampleDiagnosisRelatedGroupCodes(Enum): 
	pass
class FhirDocumentTypeCodes(Enum): 
	pass
class GoalAchievementStatus(Enum): 
	pass
class ContainerMaterials(Enum): 
	
    _32039001 = "_32039001"
    _61088005 = "_61088005"
    _425620007 = "_425620007"
class ContractTypeCodes(Enum): 
	pass
class ClaimCareTeamRoleCodes(Enum): 
	pass
class CarePlanActivityOutcome(Enum): 
	pass
class ContractTermTypeCodes(Enum): 
	pass
class ContractSubtypeCodes(Enum): 
	pass
class SupplementTypeCodes(Enum):
    _442991000124104 = "_442991000124104"
    _443011000124100 = "_443011000124100"
    _442961000124107 = "_442961000124107"
    _442951000124105 = "_442951000124105"
    _442941000124108 = "_442941000124108"
    _442921000124101 = "_442921000124101"
    _442901000124106 = "_442901000124106"
    _443031000124106 = "_443031000124106"
    _443051000124104 = "_443051000124104"
    _442911000124109 = "_442911000124109"
    _443021000124108 = "_443021000124108"
    _442971000124100 = "_442971000124100"
    _442981000124102 = "_442981000124102"
    _441591000124103 = "_441591000124103"
    _441601000124106 = "_441601000124106"
    _443351000124102 = "_443351000124102"
    _443771000124106 = "_443771000124106"
    _441671000124100 = "_441671000124100"
    _442931000124103 = "_442931000124103"
    _444331000124106 = "_444331000124106"
    _443361000124100 = "_443361000124100"
    _443391000124108 = "_443391000124108"
    _443401000124105 = "_443401000124105"
    _443491000124103 = "_443491000124103"
    _443501000124106 = "_443501000124106"
    _443421000124100 = "_443421000124100"
    _443471000124104 = "_443471000124104"
    _444431000124104 = "_444431000124104"
    _443451000124109 = "_443451000124109"
    _444321000124108 = "_444321000124108"
    _441561000124106 = "_441561000124106"
    _443461000124106 = "_443461000124106"
    _441531000124102 = "_441531000124102"
    _443561000124107 = "_443561000124107"
    _443481000124101 = "_443481000124101"
    _441571000124104 = "_441571000124104"
    _443111000124101 = "_443111000124101"
    _443431000124102 = "_443431000124102"
    _443411000124108 = "_443411000124108"
    _444361000124102 = "_444361000124102"
    _444401000124107 = "_444401000124107"
    _444381000124107 = "_444381000124107"
    _444371000124109 = "_444371000124109"
    _443441000124107 = "_443441000124107"
    _442651000124102 = "_442651000124102"
class EncounterReasonCodes(Enum): 
	pass
class ContractResourceScopeCodesB(Enum): 
	pass
class ProcedurePerformerRoleCodes(Enum): 
	pass
class CarePlanCategory(Enum): 
	pass
class FhirDefinedType(Enum): 
	pass
class SnomedctAdditionalDosageInstructions(Enum): 
	pass
class V3FamilyMember(Enum): 
	pass
class ExampleServicePlaceCodes(Enum): 
	pass
class ContractResourceAssetTypeCodes(Enum): 
	pass
class Pushtypeavailable(Enum): 
	pass
class SnomedctClinicalFindingsA(Enum): 
	pass
class ProvenanceHistoryRecordActivityCodes(Enum): 
	
    delete = "delete"
    abort = "abort"
    hold = "hold"
    create = "create"
    update = "update"
    release = "release"
    cancel = "cancel"
    activate = "activate"
    suspend = "suspend"
    resume = "resume"
    complete = "complete"
    nullify = "nullify"
    obsolete = "obsolete"
    reactivate = "reactivate"
class CommonLanguages(Enum): 
	
    de = "de"
    deAt = "deAt"
    deCh = "deCh"
    ar = "ar"
    bn = "bn"
    cs = "cs"
    da = "da"
    noNo = "noNo"
    pa = "pa"
    pl = "pl"
    deDe = "deDe"
    el = "el"
    en = "en"
    enAu = "enAu"
    enCa = "enCa"
    enGb = "enGb"
    enIn = "enIn"
    enNz = "enNz"
    enSg = "enSg"
    enUs = "enUs"
    es = "es"
    esAr = "esAr"
    esEs = "esEs"
    esUy = "esUy"
    fi = "fi"
    fr = "fr"
    frBe = "frBe"
    frCh = "frCh"
    frFr = "frFr"
    fy = "fy"
    fyNl = "fyNl"
    hi = "hi"
    hr = "hr"
    it = "it"
    itCh = "itCh"
    itIt = "itIt"
    ja = "ja"
    ko = "ko"
    nl = "nl"
    nlBe = "nlBe"
    nlNl = "nlNl"
    no = "no"
    pt = "pt"
    ptBr = "ptBr"
    ru = "ru"
    ruRu = "ruRu"
    sr = "sr"
    srRs = "srRs"
    sv = "sv"
    svSe = "svSe"
    te = "te"
    zh = "zh"
    zhCn = "zhCn"
    zhHk = "zhHk"
    zhSg = "zhSg"
    zhTw = "zhTw"
class MessageTransport(Enum): 
	pass
class Validationtype(Enum): 
	pass
class SnomedctAnatomicalStructureForAdministrationSiteCodes(Enum): 
	pass
class SpecimenContainerType(Enum): 
	pass
class ProvenanceActivityType(Enum):
    pseud = "pseud"
    create = "create"
    la = "la"
    anony = "anony"
    deid = "deid"
    mask = "mask"
    label = "label"
    delete = "delete"
    update = "update"
    append = "append"
    nullify = "nullify"
class ContractResourcePartyRoleCodes(Enum): 
	pass
class JurisdictionValueSet(Enum): 
	pass
class ConditionStage(Enum): 
	pass
class SnomedctAdministrationMethodCodes(Enum): 
	pass
class ProvenanceParticipantType(Enum): 
	pass
class ExampleClaimSubTypeCodes(Enum): 
	pass
class SubjectType(Enum):
    patient = "patient"
    practitioner = "practitioner"
    organization = "organization"
    location = "location"
    device = "device"
class ContractActorRoleCodes(Enum): 
	pass
class ContractSignerTypeCodes(Enum): 
	pass
class ExampleProcedureTypeCodes(Enum): 
	pass
class SpecimenCollection(Enum):
    _129323009 = "_129323009"
    _73416001 = "_73416001"
    _129316008 = "_129316008"
    _129314006 = "_129314006"
    _129300006 = "_129300006"
    _129304002 = "_129304002"
    _225113003 = "_225113003"
    _70777001 = "_70777001"
    _386089008 = "_386089008"
    _278450005 = "_278450005"
class ContextOfUseValueSet(Enum): 
	pass
class CommunicationCategory(Enum): 
	pass
class ContractResourceSecurityControlCodes(Enum): 
	pass
class ParticipantType(Enum):
    sprf = "sprf"
    pprf = "pprf"
    part = "part"
class TestScriptOperationCode(Enum): 
	pass
class SnomedctMedicationCodes(Enum): 
	pass
class ContractResourceLegalStateCodes(Enum): 
	pass
class MedicationRequestStatusReasonCodes(Enum): 
	pass
class RestfulSecurityService(Enum): 
	pass
class ServiceRequestOrderDetailsCodes(Enum):
    _286812008 = "_286812008"
    _243144002 = "_243144002"
    _243150007 = "_243150007"
    _59427005 = "_59427005"
    _47545007 = "_47545007"
class Canpushupdates(Enum): 
	pass
class BodystructureLocationQualifier(Enum):
    _419161000 = "_419161000"
    _419465000 = "_419465000"
    _51440002 = "_51440002"
    _261183002 = "_261183002"
    _261122009 = "_261122009"
    _255561001 = "_255561001"
    _49370004 = "_49370004"
    _264217000 = "_264217000"
    _261089000 = "_261089000"
    _255551008 = "_255551008"
    _351726001 = "_351726001"
    _352730000 = "_352730000"
class TextureModifiedFoodTypeCodes(Enum): 
	
    _226760005 = "_226760005"
    _226887002 = "_226887002"
    _102263004 = "_102263004"
    _74242007 = "_74242007"
    _227415002 = "_227415002"
    _255620007 = "_255620007"
    _28647000 = "_28647000"
    _22836000 = "_22836000"
    _72511004 = "_72511004"
    _264331002 = "_264331002"
    _227518002 = "_227518002"
    _44027008 = "_44027008"
    _226529007 = "_226529007"
    _227210005 = "_227210005"
class PracticeSettingCodeValueSet(Enum): 
	
    _394601005 = "_394601005"
    _394581000 = "_394581000"
    _408467006 = "_408467006"
    _394577000 = "_394577000"
    _394578005 = "_394578005"
    _421661004 = "_421661004"
    _408462000 = "_408462000"
    _394579002 = "_394579002"
    _394804000 = "_394804000"
    _394580004 = "_394580004"
    _394803006 = "_394803006"
    _408480009 = "_408480009"
    _408454008 = "_408454008"
    _394809005 = "_394809005"
    _394592004 = "_394592004"
    _394600006 = "_394600006"
    _419192003 = "_419192003"
    _408478003 = "_408478003"
    _394812008 = "_394812008"
    _408444009 = "_408444009"
    _394582007 = "_394582007"
    _408475000 = "_408475000"
    _410005002 = "_410005002"
    _394583002 = "_394583002"
    _419772000 = "_419772000"
    _394584008 = "_394584008"
    _408443003 = "_408443003"
    _394802001 = "_394802001"
    _394915009 = "_394915009"
    _394814009 = "_394814009"
    _394808002 = "_394808002"
    _394811001 = "_394811001"
    _408446006 = "_408446006"
    _394586005 = "_394586005"
    _394916005 = "_394916005"
    _408472002 = "_408472002"
    _394597005 = "_394597005"
    _394598000 = "_394598000"
    _394807007 = "_394807007"
    _418058008 = "_418058008"
    _420208008 = "_420208008"
    _408468001 = "_408468001"
    _394593009 = "_394593009"
    _394813003 = "_394813003"
    _410001006 = "_410001006"
    _394589003 = "_394589003"
    _394591006 = "_394591006"
    _394599008 = "_394599008"
    _394649004 = "_394649004"
    _408470005 = "_408470005"
    _394585009 = "_394585009"
    _394821009 = "_394821009"
    _422191005 = "_422191005"
    _394594003 = "_394594003"
    _416304004 = "_416304004"
    _418960008 = "_418960008"
    _394882004 = "_394882004"
    _394806003 = "_394806003"
    _394588006 = "_394588006"
    _408459003 = "_408459003"
    _394607009 = "_394607009"
    _419610006 = "_419610006"
    _408476004 = "_408476004"
    _418652005 = "_418652005"
    _418535003 = "_418535003"
    _418862001 = "_418862001"
    _419365004 = "_419365004"
    _418002000 = "_418002000"
    _419983000 = "_419983000"
    _419170002 = "_419170002"
    _419472004 = "_419472004"
    _394539006 = "_394539006"
    _420112009 = "_420112009"
    _409968004 = "_409968004"
    _394587001 = "_394587001"
    _394913002 = "_394913002"
    _408440000 = "_408440000"
    _418112009 = "_418112009"
    _419815003 = "_419815003"
    _394914008 = "_394914008"
    _408455009 = "_408455009"
    _394602003 = "_394602003"
    _408447002 = "_408447002"
    _394810000 = "_394810000"
    _408450004 = "_408450004"
    _394801008 = "_394801008"
    _408463005 = "_408463005"
    _408469009 = "_408469009"
    _408466002 = "_408466002"
    _408471009 = "_408471009"
    _408464004 = "_408464004"
    _408441001 = "_408441001"
    _408465003 = "_408465003"
    _394605001 = "_394605001"
    _394608004a = "_394608004a"
    _408461007 = "_408461007"
    _408460008 = "_408460008"
    _408460008a = "_408460008a"
    _394606000 = "_394606000"
    _408449004 = "_408449004"
    _394608004 = "_394608004"
    _418018006 = "_418018006"
    _394604002 = "_394604002"
    _394609007 = "_394609007"
    _408474001 = "_408474001"
    _394610002 = "_394610002"
    _394611003 = "_394611003"
    _408477008 = "_408477008"
    _419321007 = "_419321007"
    _394576009 = "_394576009"
    _394590007 = "_394590007"
    _409967009 = "_409967009"
    _408448007 = "_408448007"
    _419043006 = "_419043006"
    _394612005 = "_394612005"
    _394733009 = "_394733009"
    _394732004 = "_394732004"
class MedicationAdministrationPerformerFunctionCodes(Enum): 
	pass
class CoverageCopayTypeCodes(Enum): 
	pass
class ExampleCoverageFinancialExceptionCodes(Enum): 
	pass
class IdentifierTypeCodes(Enum):
    mr = "mr"
    mcn = "mcn"
    dl = "dl"
    ppn = "ppn"
    brn = "brn"
    en = "en"
    tax = "tax"
    niip = "niip"
    prn = "prn"
    md = "md"
    dr = "dr"
    acsn = "acsn"
    udi = "udi"
    sno = "sno"
    sb = "sb"
    plac = "plac"
    fill = "fill"
    jhn = "jhn"
class SecurityRoleType(Enum):
    named = "named"
    nok = "nok"
    amender = "amender"
    coauth = "coauth"
    cont = "cont"
    evtwit = "evtwit"
    primauth = "primauth"
    reviewer = "reviewer"
    source = "source"
    trans = "trans"
    valid = "valid"
    verf = "verf"
    affl = "affl"
    agnt = "agnt"
    assigned = "assigned"
    claim = "claim"
    covpty = "covpty"
    depen = "depen"
    econ = "econ"
    emp = "emp"
    guard = "guard"
    invsbj = "invsbj"
    autm = "autm"
    auwa = "auwa"
    pat = "pat"
    prov = "prov"
    not_ = "not_"
    classifier = "classifier"
    consenter = "consenter"
    conswit = "conswit"
    copart = "copart"
    declassifier = "declassifier"
    delegatee = "delegatee"
    delegator = "delegator"
    downgrder = "downgrder"
    dpowatt = "dpowatt"
    excest = "excest"
    grantee = "grantee"
    grantor = "grantor"
    gt = "gt"
    guadltm = "guadltm"
    hpowatt = "hpowatt"
    intprter = "intprter"
    powatt = "powatt"
    resprsn = "resprsn"
    spowatt = "spowatt"
    aucg = "aucg"
    aulr = "aulr"
    promsk = "promsk"
    aut = "aut"
    cst = "cst"
    inf = "inf"
    ircp = "ircp"
    la = "la"
    ircpa = "ircpa"
    trc = "trc"
    wit = "wit"
    _110150 = "_110150"
    _110151 = "_110151"
    _110152 = "_110152"
    _110153 = "_110153"
    _110154 = "_110154"
    _110155 = "_110155"
class ImmunizationEvaluationDoseStatusCodes(Enum): 
	pass
class CertaintySubcomponentRating(Enum): 
	pass
class DietCodes(Enum): 
	pass
class LoincCodes(Enum): 
	pass
class V20276(Enum): 
	pass
class SnomedctRouteCodes(Enum): 
	pass
class ContractResourceScopeCodes(Enum): 
	pass
class V3ActConsentDirective(Enum): 
	pass
class MedicationRequestCategoryCodes(Enum): 
	pass
class TestScriptProfileDestinationType(Enum): 
	pass
class FamilyHistoryAbsentReason(Enum): 
	pass
class AdjudicationValueCodes(Enum): 
	pass
class ImmunizationTargetDiseaseCodes(Enum):
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
    _27836007 = "_27836007"
    _398102009 = "_398102009"
class ContractResourceAssetAvailiabilityCodes(Enum): 
	pass
class DetectedIssueCategory(Enum): 
	pass
class ModifierTypeCodes(Enum): 
	pass
class V20371(Enum): 
	pass
class DefinitionUseCodes(Enum): 
	pass
class AdjudicationReasonCodes(Enum): 
	pass
class ServiceCategory(Enum): 
	pass
class CommonTags(Enum): 
	pass
class ProcedureReasonCodes(Enum): 
	pass
class BenefitCategoryCodes(Enum): 
	pass
class V3ActIncidentCode(Enum): 
	pass
class Verificationresultcommunicationmethod(Enum): 
	pass
class ExpressionLanguage(Enum): 
	pass
class ManifestationAndSymptomCodes(Enum): 
	pass
class EvidenceVariantState(Enum): 
	pass
class FundsReservationCodes(Enum): 
	pass
class GoalCategory(Enum): 
	pass
class ParticipantRoles(Enum): 
	pass
class CatalogType(Enum): 
	pass
class ContractContentDerivationCodes(Enum): 
	pass
class DocumentSectionCodes(Enum):
    _113696 = "_113696"
    _578526 = "_578526"
    _101543 = "_101543"
    _101576 = "_101576"
    _101600 = "_101600"
    _101642 = "_101642"
    _101832 = "_101832"
    _101840 = "_101840"
    _101873 = "_101873"
    _102103 = "_102103"
    _102160 = "_102160"
    _102186 = "_102186"
    _102186A = "_102186A"
    _102236 = "_102236"
    _102228 = "_102228"
    _113290 = "_113290"
    _113480 = "_113480"
    _518480 = "_518480"
    _551093 = "_551093"
    _114934 = "_114934"
    _551226 = "_551226"
    _115352 = "_115352"
    _115378 = "_115378"
    _187765 = "_187765"
    _188417 = "_188417"
    _292995 = "_292995"
    _295451 = "_295451"
    _295493 = "_295493"
    _295543 = "_295543"
    _297622 = "_297622"
    _309542 = "_309542"
    _423442 = "_423442"
    _423467 = "_423467"
    _423483 = "_423483"
    _423491 = "_423491"
    _462408 = "_462408"
    _462416 = "_462416"
    _462648 = "_462648"
    _474205 = "_474205"
    _475194 = "_475194"
    _487652 = "_487652"
    _487686 = "_487686"
    _597682 = "_597682"
    _597690 = "_597690"
    _597708 = "_597708"
    _597716 = "_597716"
    _597724 = "_597724"
    _597732 = "_597732"
    _597757 = "_597757"
    _597765 = "_597765"
    _611491 = "_611491"
    _611509 = "_611509"
    _611509B = "_611509B"
    _697300 = "_697300"
    _86488 = "_86488"
    _86538 = "_86538"
    _87163 = "_87163"
class ClaimTypeCodes(Enum): 
	pass
class FluidConsistencyTypeCodes(Enum):
    _439021000124105 = "_439021000124105"
    _439041000124103 = "_439041000124103"
    _439081000124109 = "_439081000124109"
    _439031000124108 = "_439031000124108"
class UsclsCodes(Enum): 
	pass
class CoverageClassCodes(Enum): 
	pass
class SupplyType(Enum): 
	pass
class ObservationReferenceRangeAppliesToCodes(Enum):
    _248153007 = "_248153007"
    _248152002 = "_248152002"
    _77386006 = "_77386006"
class PaymentStatusCodes(Enum): 
	pass
class FhirDeviceStatusReason(Enum): 
	pass


############################################
# Definition of Classes
############################################
