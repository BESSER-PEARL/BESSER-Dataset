from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ServiceProvisionConditions(Enum):
class ObservationInterpretationCodes(Enum):
class ParticipantType(Enum):
    sprf = "sprf"
    pprf = "pprf"
    part = "part"
class ReasonMedicationGivenCodes(Enum):
class Canpushupdates(Enum):
class ContractResourceDefinitionSubtypeCodes(Enum):
class ConsentScopeCodes(Enum):
class MedicationRequestStatusReasonCodes(Enum):
class SpecimenProcessingProcedure(Enum):
class OrganizationType(Enum):
class ManifestationAndSymptomCodes(Enum):
class BodystructureLocationQualifier(Enum):
    _419161000 = "_419161000"
    _419465000 = "_419465000"
    _264217000 = "_264217000"
    _261089000 = "_261089000"
    _255551008 = "_255551008"
    _351726001 = "_351726001"
    _352730000 = "_352730000"
    _51440002 = "_51440002"
    _261183002 = "_261183002"
    _261122009 = "_261122009"
    _255561001 = "_255561001"
    _49370004 = "_49370004"
class EndpointPayloadType(Enum):
    urnihepccaps2007 = "urnihepccaps2007"
    urnihepccxdsms2007 = "urnihepccxdsms2007"
    urnihepccxphr2007 = "urnihepccxphr2007"
    urnihepcchandp2008 = "urnihepcchandp2008"
    urnihepccxphr2007A = "urnihepccxphr2007A"
    urnihepccldhp2009 = "urnihepccldhp2009"
    urnihepcclds2009 = "urnihepcclds2009"
    urnihepccmds2009 = "urnihepccmds2009"
    urnihepccnds2010 = "urnihepccnds2010"
    urnihepccppvs2010 = "urnihepccppvs2010"
    urnihepccedr2007 = "urnihepccedr2007"
    urnihepcctrs2011 = "urnihepcctrs2011"
    urnihepccedes2007 = "urnihepccedes2007"
    urnihepccets2011 = "urnihepccets2011"
    urnihepccaprhandp2008 = "urnihepccaprhandp2008"
    urnihepccits2011 = "urnihepccits2011"
    urnihepccaprlab2008 = "urnihepccaprlab2008"
    urniheitibppc2007 = "urniheitibppc2007"
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
    urniheitibppcsd2007 = "urniheitibppcsd2007"
    urniheitixdw2011workflowDoc = "urniheitixdw2011workflowDoc"
    urniheitidsgdetached2014 = "urniheitidsgdetached2014"
    urniheitidsgenveloping2014 = "urniheitidsgenveloping2014"
    urniheitixdssdpdf2008 = "urniheitixdssdpdf2008"
    urniheitixdssdtext2008 = "urniheitixdssdtext2008"
    urnihelabxdlab2008 = "urnihelabxdlab2008"
    urniheradText = "urniheradText"
    urniheradPdf = "urniheradPdf"
    urniheradCdAImagingReportStructuredHeadings2013 = "urniheradCdAImagingReportStructuredHeadings2013"
    urnihecardimaging2011 = "urnihecardimaging2011"
    urnihepatapsrcancerliver2010 = "urnihepatapsrcancerliver2010"
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
    urnihepatapsrcancerthyroid2010 = "urnihepatapsrcancerthyroid2010"
    urnihepatapsrcancerlung2010 = "urnihepatapsrcancerlung2010"
    urnihepatapsrcancerskin2010 = "urnihepatapsrcancerskin2010"
    urnihepatapsrcancerkidney2010 = "urnihepatapsrcancerkidney2010"
    urnihepatapsrcancercervix2010 = "urnihepatapsrcancercervix2010"
    urnihepatapsrcancerendometrium2010 = "urnihepatapsrcancerendometrium2010"
    urnihepatapsrcancerovary2010 = "urnihepatapsrcancerovary2010"
    urnihepatapsrcanceresophagus2010 = "urnihepatapsrcanceresophagus2010"
    urnihepatapsrcancerstomach2010 = "urnihepatapsrcancerstomach2010"
    urnihepharmpml2013 = "urnihepharmpml2013"
    urnhl7orgsdwgccdastructuredBody11 = "urnhl7orgsdwgccdastructuredBody11"
    urnhl7orgsdwgccdanonXmlBody11 = "urnhl7orgsdwgccdanonXmlBody11"
class ResearchStudyObjectiveType(Enum):
class AllSecurityLabels(Enum):
class ExampleDiagnosisOnAdmissionCodes(Enum):
class ContactEntityType(Enum):
class MedicationDispensePerformerFunctionCodes(Enum):
class ExampleVisionPrescriptionProductCodes(Enum):
class AdjudicationReasonCodes(Enum):
class ResearchStudyPhase(Enum):
class ExampleDiagnosisRelatedGroupCodes(Enum):
class ContractResourceAssetAvailiabilityCodes(Enum):
class EnteralFormulaAdditiveTypeCode(Enum):
class V3SubstanceAdminSubstitutionReason(Enum):
class DeviceType(Enum):
class SubscriberRelationshipCodes(Enum):
class NutrientModifierCodes(Enum):
    _33463005 = "_33463005"
    _39972003 = "_39972003"
    _88480006 = "_88480006"
class MedicationAdministrationCategoryCodes(Enum):
class PatientContactRelationship(Enum):
class SnomedctBodyStructures(Enum):
class ImmunizationFunctionCodes(Enum):
    op = "op"
    ap = "ap"
class EndpointConnectionType(Enum):
class MedicationRequestCategoryCodes(Enum):
class LoincDiagnosticReportCodes(Enum):
class QuestionnaireAnswerCodes(Enum):
class MediaCollectionViewProjection(Enum):
class VaccineAdministeredValueSet(Enum):
class ContractSignerTypeCodes(Enum):
class DiagnosticServiceSectionCodes(Enum):
class SnomedctAnatomicalStructureForAdministrationSiteCodes(Enum):
class ImmunizationOriginCodes(Enum):
    provider = "provider"
    record = "record"
    recall = "recall"
    school = "school"
class ContractResourceAssetContextCodes(Enum):
class ClaimInformationCategoryCodes(Enum):
class ProcedurePerformerRoleCodes(Enum):
class TaskCode(Enum):
class SecurityRoleType(Enum):
    primauth = "primauth"
    reviewer = "reviewer"
    source = "source"
    trans = "trans"
    valid = "valid"
    verf = "verf"
    affl = "affl"
    amender = "amender"
    coauth = "coauth"
    cont = "cont"
    evtwit = "evtwit"
    guard = "guard"
    invsbj = "invsbj"
    named = "named"
    nok = "nok"
    pat = "pat"
    prov = "prov"
    not = "not"
    agnt = "agnt"
    assigned = "assigned"
    claim = "claim"
    covpty = "covpty"
    depen = "depen"
    econ = "econ"
    emp = "emp"
    delegator = "delegator"
    downgrder = "downgrder"
    dpowatt = "dpowatt"
    excest = "excest"
    grantee = "grantee"
    grantor = "grantor"
    gt = "gt"
    classifier = "classifier"
    consenter = "consenter"
    conswit = "conswit"
    copart = "copart"
    declassifier = "declassifier"
    delegatee = "delegatee"
    aulr = "aulr"
    autm = "autm"
    auwa = "auwa"
    promsk = "promsk"
    aut = "aut"
    cst = "cst"
    inf = "inf"
    guadltm = "guadltm"
    hpowatt = "hpowatt"
    intprter = "intprter"
    powatt = "powatt"
    resprsn = "resprsn"
    spowatt = "spowatt"
    aucg = "aucg"
    _110151 = "_110151"
    _110152 = "_110152"
    _110153 = "_110153"
    _110154 = "_110154"
    _110155 = "_110155"
    ircp = "ircp"
    la = "la"
    ircpa = "ircpa"
    trc = "trc"
    wit = "wit"
    _110150 = "_110150"
class Validationprocess(Enum):
class Pushtypeavailable(Enum):
class MeasureDataUsage(Enum):
class ConsentContentClass(Enum):
    httphl7orgfhirStructureDefinitionlipidprofile = "httphl7orgfhirStructureDefinitionlipidprofile"
    applicationhl7cdaxml = "applicationhl7cdaxml"
class MeasureScoring(Enum):
class Validationstatus(Enum):
class FhirDeviceTypes(Enum):
class ContractResourcePartyRoleCodes(Enum):
class AdjudicationErrorCodes(Enum):
class PaymentAdjustmentReasonCodes(Enum):
class ProcedureDeviceActionCodes(Enum):
class ImmunizationRouteCodes(Enum):
    nasinhlc = "nasinhlc"
    ivinj = "ivinj"
    po = "po"
    sq = "sq"
    trnsderm = "trnsderm"
    idinj = "idinj"
    im = "im"
class ContractResourceExpirationTypeCodes(Enum):
class DetectedIssueMitigationAction(Enum):
class CommunicationCategory(Enum):
class ProcessPriorityCodes(Enum):
class TextureModifiedFoodTypeCodes(Enum):
    _226760005 = "_226760005"
    _226887002 = "_226887002"
    _102263004 = "_102263004"
    _74242007 = "_74242007"
    _227415002 = "_227415002"
    _264331002 = "_264331002"
    _227518002 = "_227518002"
    _44027008 = "_44027008"
    _255620007 = "_255620007"
    _28647000 = "_28647000"
    _22836000 = "_22836000"
    _72511004 = "_72511004"
    _226529007 = "_226529007"
    _227210005 = "_227210005"
class ConditionStageType(Enum):
    _261023001 = "_261023001"
    _260998006 = "_260998006"
class ContractTermTypeCodes(Enum):
class HandlingConditionSet(Enum):
class RiskProbability(Enum):
class ContractSubtypeCodes(Enum):
class SupplementTypeCodes(Enum):
    _442901000124106 = "_442901000124106"
    _443031000124106 = "_443031000124106"
    _443051000124104 = "_443051000124104"
    _442911000124109 = "_442911000124109"
    _443021000124108 = "_443021000124108"
    _442971000124100 = "_442971000124100"
    _442981000124102 = "_442981000124102"
    _442991000124104 = "_442991000124104"
    _443011000124100 = "_443011000124100"
    _442961000124107 = "_442961000124107"
    _442921000124101 = "_442921000124101"
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
    _442951000124105 = "_442951000124105"
    _442941000124108 = "_442941000124108"
    _444321000124108 = "_444321000124108"
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
    _443111000124101 = "_443111000124101"
    _443451000124109 = "_443451000124109"
    _443411000124108 = "_443411000124108"
    _444361000124102 = "_444361000124102"
    _444401000124107 = "_444401000124107"
    _444381000124107 = "_444381000124107"
    _444371000124109 = "_444371000124109"
    _443441000124107 = "_443441000124107"
    _442651000124102 = "_442651000124102"
    _443431000124102 = "_443431000124102"
class NetworkTypeCodes(Enum):
class ConditionProblemDiagnosisCodes(Enum):
    _160245001 = "_160245001"
class AdmitSource(Enum):
class Laterality(Enum):
    _419161000 = "_419161000"
    _419465000 = "_419465000"
    _51440002 = "_51440002"
class ProvenanceParticipantType(Enum):
class CommonTags(Enum):
class ProvenanceActivityType(Enum):
    deid = "deid"
    mask = "mask"
    label = "label"
    pseud = "pseud"
    create = "create"
    delete = "delete"
    update = "update"
    la = "la"
    anony = "anony"
    append = "append"
    nullify = "nullify"
class V20493(Enum):
class AccountTypes(Enum):
class ExampleRelatedClaimRelationshipCodes(Enum):
class ExampleProcedureTypeCodes(Enum):
class Program(Enum):
class CommunicationNotDoneReason(Enum):
class SpecialCourtesy(Enum):
    ext = "ext"
    nrm = "nrm"
    prf = "prf"
    stf = "stf"
    vip = "vip"
    unk = "unk"
class V3ActPriority(Enum):
class BenefitTypeCodes(Enum):
class DischargeDisposition(Enum):
class MedicationKnowledgeCharacteristicCodes(Enum):
class DoseAndRateType(Enum):
class SurfaceCodes(Enum):
class EpisodeOfCareType(Enum):
class SnomedctMorphologicAbnormalities(Enum):
class SnomedctAdditionalDosageInstructions(Enum):
class ExampleUseCodesForList(Enum):
class FhirDeviceStatusReason(Enum):
class ConditionDiagnosisSeverity(Enum):
    _24484000 = "_24484000"
    _6736007 = "_6736007"
    _255604002 = "_255604002"
class ModifierTypeCodes(Enum):
class ContractResourceScopeCodesA(Enum):
class ImmunizationStatusReasonCodes(Enum):
    immune = "immune"
    medprec = "medprec"
    ostock = "ostock"
    patobj = "patobj"
class ContractResourceSecurityControlCodes(Enum):
class DocumentClassValueSet(Enum):
    _113696 = "_113696"
    _114850 = "_114850"
    _114868 = "_114868"
    _114884 = "_114884"
    _115063 = "_115063"
    _115436 = "_115436"
    _278952 = "_278952"
    _278960 = "_278960"
    _278978 = "_278978"
    _278986 = "_278986"
    _285700 = "_285700"
    _286195 = "_286195"
    _286344 = "_286344"
    _155085 = "_155085"
    _187260 = "_187260"
    _187617 = "_187617"
    _188425 = "_188425"
    _264366 = "_264366"
    _264416 = "_264416"
    _264424 = "_264424"
    _341214 = "_341214"
    _341222 = "_341222"
    _341339 = "_341339"
    _341404 = "_341404"
    _347484 = "_347484"
    _347757 = "_347757"
    _297499 = "_297499"
    _297507 = "_297507"
    _297515 = "_297515"
    _297523 = "_297523"
    _341099 = "_341099"
    _341172 = "_341172"
    _570168 = "_570168"
    _564450 = "_564450"
    _535765 = "_535765"
    _564476 = "_564476"
    _187484 = "_187484"
    _115048 = "_115048"
    _470393 = "_470393"
    _571331 = "_571331"
    _470427 = "_470427"
    _470450 = "_470450"
    _470468 = "_470468"
    _470492 = "_470492"
    _570176 = "_570176"
class DiagnosisRole(Enum):
class AuditEventEntityType(Enum):
class SnomedctMedicationAsNeededReasonCodes(Enum):
class FhirSpecimenCollectionMethod(Enum):
    _129316008 = "_129316008"
    _70777001 = "_70777001"
    _386089008 = "_386089008"
    _278450005 = "_278450005"
    _129314006 = "_129314006"
    _129300006 = "_129300006"
    _129304002 = "_129304002"
    _129323009 = "_129323009"
    _73416001 = "_73416001"
    _225113003 = "_225113003"
class CompositeMeasureScoring(Enum):
class QuestionnaireQuestionCodes(Enum):
class DeviceMetricAndComponentTypes(Enum):
class Verificationresultcommunicationmethod(Enum):
class CoverageEligibilityResponseAuthSupportCodes(Enum):
class ExampleProviderQualificationCodes(Enum):
class FlagCategory(Enum):
class ServiceRequestOrderDetailsCodes(Enum):
    _47545007 = "_47545007"
    _286812008 = "_286812008"
    _243144002 = "_243144002"
    _243150007 = "_243150007"
    _59427005 = "_59427005"
class ObjectLifecycleEvents(Enum):
class ProcedureFollowUpCodesSnomedcT(Enum):
    _35963001 = "_35963001"
    _225164002 = "_225164002"
    _447346005 = "_447346005"
    _229506003 = "_229506003"
    _274441001 = "_274441001"
    _394725008 = "_394725008"
    _359825008 = "_359825008"
    _18949003 = "_18949003"
    _30549001 = "_30549001"
    _241031001 = "_241031001"
class DataAbsentReason(Enum):
class RejectionCriterion(Enum):
class ConsentContentCodes(Enum):
class DietCodes(Enum):
class MaritalStatusCodes(Enum):
    unk = "unk"
class ObservationReferenceRangeMeaningCodes(Enum):
class ConditionCategoryCodes(Enum):
class IcD10Codes(Enum):
    _123456 = "_123456"
    _123457 = "_123457"
    _987654 = "_987654"
    _123987 = "_123987"
    _112233 = "_112233"
    _997755 = "_997755"
    _321789 = "_321789"
class SubstanceCategoryCodes(Enum):
class Validationtype(Enum):
class ContractActionCodes(Enum):
class CoverageCopayTypeCodes(Enum):
class ExampleDiagnosisTypeCodes(Enum):
class ProcedureReasonCodes(Enum):
class V3ActConsentDirective(Enum):
class V3ParticipationMode(Enum):
class V3ActReason(Enum):
class SnomedctDrugTherapyStatusCodes(Enum):
class ContractResourceAssetScopeCodes(Enum):
class ContractTermSubtypeCodes(Enum):
class MedicationKnowledgePackageTypeCodes(Enum):
class ContractResourceScopeCodesB(Enum):
class MeasurePopulationType(Enum):
class FundsReservationCodes(Enum):
class MediaModality(Enum):
class VitalSigns(Enum):
    _853531 = "_853531"
    _92791 = "_92791"
    _88674 = "_88674"
    _294637 = "_294637"
    _391565 = "_391565"
    _853549 = "_853549"
    _84806 = "_84806"
    _84624 = "_84624"
    _84780 = "_84780"
    _27086 = "_27086"
    _83105 = "_83105"
    _83022 = "_83022"
    _98434 = "_98434"
class ContractResourceActionStatusCodes(Enum):
class MissingToothReasonCodes(Enum):
class ExceptionCodes(Enum):
class Need(Enum):
class ClaimPayeeTypeCodes(Enum):
class V20092(Enum):
class MedicationDispenseCategoryCodes(Enum):
class FacilityTypeCodeValueSet(Enum):
    _32074000 = "_32074000"
    _4322002 = "_4322002"
    _224687002 = "_224687002"
    _62480006 = "_62480006"
    _80522000 = "_80522000"
    _36125001 = "_36125001"
    _48311003 = "_48311003"
    _284546000 = "_284546000"
    _42665001 = "_42665001"
    _82242000 = "_82242000"
    _225732001 = "_225732001"
    _79993009 = "_79993009"
    _360957003 = "_360957003"
    _10206005 = "_10206005"
    _37550003 = "_37550003"
    _73644007 = "_73644007"
    _31628002 = "_31628002"
    _58482006 = "_58482006"
    _90484001 = "_90484001"
    _1814000 = "_1814000"
    _22549003 = "_22549003"
    _45618002 = "_45618002"
    _418518002 = "_418518002"
    _73770003 = "_73770003"
    _69362002 = "_69362002"
    _52668009 = "_52668009"
    _38238005 = "_38238005"
    _56189001 = "_56189001"
    _89972002 = "_89972002"
    _78088001 = "_78088001"
    _78001009 = "_78001009"
    _23392004 = "_23392004"
    _36293008 = "_36293008"
    _3729002 = "_3729002"
    _5584006 = "_5584006"
    _56293002 = "_56293002"
    _360966004 = "_360966004"
    _2849009 = "_2849009"
    _14866005 = "_14866005"
    _79491001 = "_79491001"
    _33022008 = "_33022008"
    _19602009 = "_19602009"
    _39350007 = "_39350007"
    _83891005 = "_83891005"
    _394759007 = "_394759007"
    _405607001 = "_405607001"
    _309900005 = "_309900005"
    _275576008 = "_275576008"
    _37546005 = "_37546005"
    _57159002 = "_57159002"
    _331006 = "_331006"
    _50569004 = "_50569004"
    _1773006 = "_1773006"
    _72311000 = "_72311000"
    _6827000 = "_6827000"
    _309898008 = "_309898008"
    _39913001 = "_39913001"
    _77931003 = "_77931003"
    _25681007 = "_25681007"
    _20078004 = "_20078004"
    _10531005 = "_10531005"
    _91154008 = "_91154008"
    _41844007 = "_41844007"
    _45899008 = "_45899008"
    _51563005 = "_51563005"
    _409519008 = "_409519008"
    _901005 = "_901005"
    _2081004 = "_2081004"
    _59374000 = "_59374000"
    _413456002 = "_413456002"
    _413817003 = "_413817003"
    _310205006 = "_310205006"
    _419955002 = "_419955002"
    _272501009 = "_272501009"
    _46224007 = "_46224007"
    _81234003 = "_81234003"
    _35971002 = "_35971002"
    _11424001 = "_11424001"
    _394777002 = "_394777002"
class BenefitTermCodes(Enum):
class ExampleProgramReasonCodes(Enum):
class MedicationStatusCodes(Enum):
class ContractResourceAssetTypeCodes(Enum):
class ContractActorRoleCodes(Enum):
class ResearchStudyPrimaryPurposeType(Enum):
class IcD10ProcedureCodes(Enum):
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
class ContractTypeCodes(Enum):
class LibraryType(Enum):
class ProcedureNotPerformedReasonSnomeDCT(Enum):
class SnomedctReasonMedicationNotGivenCodes(Enum):
class TextureModifierCodes(Enum):
    _441761000124103 = "_441761000124103"
    _441751000124100 = "_441751000124100"
    _228059003 = "_228059003"
    _441791000124106 = "_441791000124106"
    _228055009 = "_228055009"
    _228056005 = "_228056005"
    _441771000124105 = "_441771000124105"
    _228057001 = "_228057001"
    _228058006 = "_228058006"
    _228053002 = "_228053002"
    _439091000124107 = "_439091000124107"
    _228049004 = "_228049004"
    _441881000124103 = "_441881000124103"
    _228060008 = "_228060008"
class ContractResourceDecisionModeCodes(Enum):
class ImmunizationReasonCodes(Enum):
    _429060002 = "_429060002"
    _281657000 = "_281657000"
class FluidConsistencyTypeCodes(Enum):
    _439041000124103 = "_439041000124103"
    _439081000124109 = "_439081000124109"
    _439031000124108 = "_439031000124108"
    _439021000124105 = "_439021000124105"
class ListEmptyReasons(Enum):
class SubstanceCode(Enum):
class CodesForImmunizationSiteOfAdministration(Enum):
    la = "la"
    ra = "ra"
class V3PurposeOfUse(Enum):
class FlagCode(Enum):
class ProcedureCategoryCodesSnomedcT(Enum):
    _409063005 = "_409063005"
    _409073007 = "_409073007"
    _387713003 = "_387713003"
    _103693007 = "_103693007"
    _46947000 = "_46947000"
    _410606002 = "_410606002"
    _24642003 = "_24642003"
class ServiceRequestCategoryCodes(Enum):
    _108252007 = "_108252007"
    _363679005 = "_363679005"
    _409063005 = "_409063005"
    _409073007 = "_409073007"
    _387713003 = "_387713003"
class ExampleClaimSubTypeCodes(Enum):
class FoodTypeCodes(Enum):
class UcumCodes(Enum):
class ExampleRevenueCenterCodes(Enum):
class UsclsCodes(Enum):
class CoverageClassCodes(Enum):
class V3ActCode(Enum):
class CoverageTypeAndSelfPayCodes(Enum):
class ClaimCareTeamRoleCodes(Enum):
class ObservationCategoryCodes(Enum):
class MedicationRequestCourseOfTherapyCodes(Enum):
class Primarysourcetype(Enum):
class Failureaction(Enum):
class MedicationDispenseStatusReasonCodes(Enum):
class V3ActPharmacySupplyType(Enum):
class DetectedIssueCategory(Enum):
class ReferralMethod(Enum):
class ImagingStudySeriesPerformerFunction(Enum):
    sprf = "sprf"
    ref = "ref"
    con = "con"
    vrf = "vrf"
    prf = "prf"
class AuditEventEntityRole(Enum):
class ImmunizationSubpotentReason(Enum):
class ContractResourceAssetSubTypeCodes(Enum):
class SpecialArrangements(Enum):
class ContractResourceDefinitionTypeCodes(Enum):
class BenefitCategoryCodes(Enum):
class BasicResourceTypes(Enum):
class PatientRelationshipType(Enum):
class ConsentCategoryCodes(Enum):
    _570168 = "_570168"
    _570176 = "_570176"
    _642926 = "_642926"
    _592840 = "_592840"
class V20371(Enum):
class ObservationMethods(Enum):
class EnteralFormulaTypeCodes(Enum):
    _443031000124106 = "_443031000124106"
    _443051000124104 = "_443051000124104"
    _442911000124109 = "_442911000124109"
    _443021000124108 = "_443021000124108"
    _442971000124100 = "_442971000124100"
    _442991000124104 = "_442991000124104"
    _443011000124100 = "_443011000124100"
    _442961000124107 = "_442961000124107"
    _442951000124105 = "_442951000124105"
    _442941000124108 = "_442941000124108"
    _442921000124101 = "_442921000124101"
    _442931000124103 = "_442931000124103"
    _443361000124100 = "_443361000124100"
    _443401000124105 = "_443401000124105"
    _443491000124103 = "_443491000124103"
    _443501000124106 = "_443501000124106"
    _443421000124100 = "_443421000124100"
    _443471000124104 = "_443471000124104"
    _442981000124102 = "_442981000124102"
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
    _443111000124101 = "_443111000124101"
    _444431000124104 = "_444431000124104"
    _443411000124108 = "_443411000124108"
    _442651000124102 = "_442651000124102"
    _443431000124102 = "_443431000124102"
class SubjectType(Enum):
    patient = "patient"
    practitioner = "practitioner"
    organization = "organization"
    location = "location"
    device = "device"
class ExampleCoverageFinancialExceptionCodes(Enum):
class TimingAbbreviation(Enum):
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
    q6h = "q6h"
    q8h = "q8h"
    bed = "bed"
    wk = "wk"
    mo = "mo"
class SnomedctAdministrationMethodCodes(Enum):
class ConsentActionCodes(Enum):
class AcquisitionModality(Enum):
    opv = "opv"
    dx = "dx"
    opt = "opt"
    bmd = "bmd"
    mg = "mg"
    sm = "sm"
    us = "us"
    op = "op"
    xa = "xa"
    xc = "xc"
    va = "va"
    ivus = "ivus"
    cr = "cr"
    es = "es"
    ar = "ar"
    ct = "ct"
    oss = "oss"
    ivoct = "ivoct"
    mr = "mr"
    ecg = "ecg"
    gm = "gm"
    io = "io"
    hd = "hd"
    oam = "oam"
    nm = "nm"
    oct = "oct"
    bdus = "bdus"
    pt = "pt"
    eps = "eps"
    px = "px"
    srf = "srf"
    opm = "opm"
    len = "len"
    rg = "rg"
    rf = "rf"
    ker = "ker"
    opr = "opr"
class DeviceSafety(Enum):
    c106046 = "c106046"
    c106045 = "c106045"
    c106047 = "c106047"
    c113844 = "c113844"
    c101673 = "c101673"
    c106038 = "c106038"
class ExampleServicePlaceCodes(Enum):
class V3ActSubstanceAdminSubstitutionCode(Enum):
class ConsentPolicyRuleCodes(Enum):
class EncounterType(Enum):
class ChargeItemCode(Enum):
class V3ActIncidentCode(Enum):
class DefinitionTopic(Enum):
class DocumentReferenceFormatCodeSet(Enum):
class ProcedureOutcomeCodesSnomedcT(Enum):
    _385669000 = "_385669000"
    _385671000 = "_385671000"
    _385670004 = "_385670004"
class ResearchStudyReasonStopped(Enum):
class ExamplePaymentTypeCodes(Enum):
class FormCodes(Enum):
class SnomedctRouteCodes(Enum):
class AdjudicationValueCodes(Enum):
class ClaimTypeCodes(Enum):
class ImmunizationRecommendationDateCriterionCodes(Enum):
    _309815 = "_309815"
    _309807 = "_309807"
    _597773 = "_597773"
    _597781 = "_597781"
class ContractResourceLegalStateCodes(Enum):
class OralSiteCodes(Enum):
class ClinicalImpressionPrognosis(Enum):
class ContractResourceScopeCodes(Enum):
class ListOrderCodes(Enum):
class ExpressionLanguage(Enum):
class V3ActEncounterCode(Enum):
class UnitTypeCodes(Enum):
class ServiceType(Enum):
class MediaType(Enum):
class ObservationReferenceRangeAppliesToCodes(Enum):
    _248153007 = "_248153007"
    _248152002 = "_248152002"
    _77386006 = "_77386006"
class MeasureType(Enum):
class DesignationUse(Enum):
    _900000000000003001 = "_900000000000003001"
    _900000000000013009 = "_900000000000013009"
class MedicationAdministrationPerformerFunctionCodes(Enum):
class ImmunizationProgramEligibility(Enum):
class V20916(Enum):
class SnomedctFormCodes(Enum):
class ProvenanceParticipantRole(Enum):
class Diet(Enum):
class ImmunizationEvaluationTargetDiseaseCodes(Enum):
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
    _27836007 = "_27836007"
    _398102009 = "_398102009"
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
class ContractContentDerivationCodes(Enum):
class PatientMedicineChangeTypes(Enum):
class CommunicationTopic(Enum):
class MessageTransport(Enum):
class FdAStandardSequence(Enum):
class GoalAchievementStatus(Enum):
class OrganizationAffiliationRole(Enum):
class InsurancePlanType(Enum):
class UsageContextType(Enum):
class ContextOfUseValueSet(Enum):
class PreparePatient(Enum):
class DocumentSectionCodes(Enum):
    _101543 = "_101543"
    _101576 = "_101576"
    _101600 = "_101600"
    _101642 = "_101642"
    _102103 = "_102103"
    _102160 = "_102160"
    _102186 = "_102186"
    _102186A = "_102186A"
    _102236 = "_102236"
    _102228 = "_102228"
    _113290 = "_113290"
    _113480 = "_113480"
    _113696 = "_113696"
    _578526 = "_578526"
    _101832 = "_101832"
    _101840 = "_101840"
    _101873 = "_101873"
    _187765 = "_187765"
    _188417 = "_188417"
    _292995 = "_292995"
    _295451 = "_295451"
    _295493 = "_295493"
    _295543 = "_295543"
    _297622 = "_297622"
    _309542 = "_309542"
    _423442 = "_423442"
    _114934 = "_114934"
    _462416 = "_462416"
    _115352 = "_115352"
    _462648 = "_462648"
    _115378 = "_115378"
    _474205 = "_474205"
    _475194 = "_475194"
    _487652 = "_487652"
    _487686 = "_487686"
    _518480 = "_518480"
    _551093 = "_551093"
    _551226 = "_551226"
    _423467 = "_423467"
    _423483 = "_423483"
    _423491 = "_423491"
    _462408 = "_462408"
    _597732 = "_597732"
    _597757 = "_597757"
    _597765 = "_597765"
    _611491 = "_611491"
    _611509 = "_611509"
    _611509B = "_611509B"
    _697300 = "_697300"
    _86488 = "_86488"
    _86538 = "_86538"
    _597682 = "_597682"
    _597690 = "_597690"
    _597708 = "_597708"
    _597716 = "_597716"
    _597724 = "_597724"
    _87163 = "_87163"
class ServiceCategory(Enum):
class AllergyIntoleranceSubstanceProductConditionAndNegationCodes(Enum):
class LocationType(Enum):
class ProvenanceHistoryRecordActivityCodes(Enum):
    create = "create"
    update = "update"
    delete = "delete"
    abort = "abort"
    hold = "hold"
    release = "release"
    cancel = "cancel"
    activate = "activate"
    suspend = "suspend"
    resume = "resume"
    complete = "complete"
    nullify = "nullify"
    obsolete = "obsolete"
    reactivate = "reactivate"
class CertaintySubcomponentType(Enum):
class DefinitionUseCodes(Enum):
class SpecimenCollection(Enum):
    _129316008 = "_129316008"
    _129314006 = "_129314006"
    _129300006 = "_129300006"
    _129304002 = "_129304002"
    _129323009 = "_129323009"
    _73416001 = "_73416001"
    _225113003 = "_225113003"
    _70777001 = "_70777001"
    _386089008 = "_386089008"
    _278450005 = "_278450005"
class SnomedctClinicalFindings(Enum):
class SupplyRequestReason(Enum):
class ImmunizationRecommendationReasonCodes(Enum):
    _77176002 = "_77176002"
    _77386006 = "_77386006"
class IdentifierTypeCodes(Enum):
    dl = "dl"
    ppn = "ppn"
    brn = "brn"
    mr = "mr"
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
    mcn = "mcn"
    en = "en"
    fill = "fill"
    jhn = "jhn"
class V2036027(Enum):
class ResourceType(Enum):
    account = "account"
    activityDefinition = "activityDefinition"
    adverseEvent = "adverseEvent"
    careTeam = "careTeam"
    catalogEntry = "catalogEntry"
    chargeItem = "chargeItem"
    chargeItemDefinition = "chargeItemDefinition"
    claim = "claim"
    allergyIntolerance = "allergyIntolerance"
    appointment = "appointment"
    appointmentResponse = "appointmentResponse"
    auditEvent = "auditEvent"
    basic = "basic"
    binary = "binary"
    biologicallyDerivedProduct = "biologicallyDerivedProduct"
    bodyStructure = "bodyStructure"
    bundle = "bundle"
    capabilityStatement = "capabilityStatement"
    carePlan = "carePlan"
    condition = "condition"
    consent = "consent"
    contract = "contract"
    coverage = "coverage"
    claimResponse = "claimResponse"
    clinicalImpression = "clinicalImpression"
    codeSystem = "codeSystem"
    communication = "communication"
    communicationRequest = "communicationRequest"
    compartmentDefinition = "compartmentDefinition"
    composition = "composition"
    conceptMap = "conceptMap"
    diagnosticReport = "diagnosticReport"
    documentManifest = "documentManifest"
    documentReference = "documentReference"
    domainResource = "domainResource"
    effectEvidenceSynthesis = "effectEvidenceSynthesis"
    coverageEligibilityRequest = "coverageEligibilityRequest"
    coverageEligibilityResponse = "coverageEligibilityResponse"
    detectedIssue = "detectedIssue"
    device = "device"
    deviceDefinition = "deviceDefinition"
    deviceMetric = "deviceMetric"
    deviceRequest = "deviceRequest"
    deviceUseStatement = "deviceUseStatement"
    exampleScenario = "exampleScenario"
    explanationOfBenefit = "explanationOfBenefit"
    familyMemberHistory = "familyMemberHistory"
    flag = "flag"
    goal = "goal"
    encounter = "encounter"
    endpoint = "endpoint"
    enrollmentRequest = "enrollmentRequest"
    enrollmentResponse = "enrollmentResponse"
    episodeOfCare = "episodeOfCare"
    eventDefinition = "eventDefinition"
    evidence = "evidence"
    evidenceVariable = "evidenceVariable"
    immunizationRecommendation = "immunizationRecommendation"
    implementationGuide = "implementationGuide"
    insurancePlan = "insurancePlan"
    invoice = "invoice"
    graphDefinition = "graphDefinition"
    group = "group"
    guidanceResponse = "guidanceResponse"
    healthcareService = "healthcareService"
    imagingStudy = "imagingStudy"
    immunization = "immunization"
    immunizationEvaluation = "immunizationEvaluation"
    medicationAdministration = "medicationAdministration"
    medicationDispense = "medicationDispense"
    medicationKnowledge = "medicationKnowledge"
    medicationRequest = "medicationRequest"
    medicationStatement = "medicationStatement"
    library = "library"
    linkage = "linkage"
    list = "list"
    location = "location"
    measure = "measure"
    measureReport = "measureReport"
    media = "media"
    medication = "medication"
    medicinalProductPackaged = "medicinalProductPackaged"
    medicinalProductPharmaceutical = "medicinalProductPharmaceutical"
    medicinalProductUndesirableEffect = "medicinalProductUndesirableEffect"
    messageDefinition = "messageDefinition"
    messageHeader = "messageHeader"
    medicinalProduct = "medicinalProduct"
    medicinalProductAuthorization = "medicinalProductAuthorization"
    medicinalProductContraindication = "medicinalProductContraindication"
    medicinalProductIndication = "medicinalProductIndication"
    medicinalProductIngredient = "medicinalProductIngredient"
    medicinalProductInteraction = "medicinalProductInteraction"
    medicinalProductManufactured = "medicinalProductManufactured"
    organization = "organization"
    organizationAffiliation = "organizationAffiliation"
    parameters = "parameters"
    patient = "patient"
    paymentNotice = "paymentNotice"
    molecularSequence = "molecularSequence"
    namingSystem = "namingSystem"
    nutritionOrder = "nutritionOrder"
    observation = "observation"
    observationDefinition = "observationDefinition"
    operationDefinition = "operationDefinition"
    operationOutcome = "operationOutcome"
    questionnaire = "questionnaire"
    questionnaireResponse = "questionnaireResponse"
    relatedPerson = "relatedPerson"
    paymentReconciliation = "paymentReconciliation"
    person = "person"
    planDefinition = "planDefinition"
    practitioner = "practitioner"
    practitionerRole = "practitionerRole"
    procedure = "procedure"
    riskEvidenceSynthesis = "riskEvidenceSynthesis"
    provenance = "provenance"
    schedule = "schedule"
    searchParameter = "searchParameter"
    requestGroup = "requestGroup"
    researchDefinition = "researchDefinition"
    researchElementDefinition = "researchElementDefinition"
    researchStudy = "researchStudy"
    researchSubject = "researchSubject"
    resource = "resource"
    riskAssessment = "riskAssessment"
    serviceRequest = "serviceRequest"
    slot = "slot"
    specimen = "specimen"
    substanceNucleicAcid = "substanceNucleicAcid"
    specimenDefinition = "specimenDefinition"
    substancePolymer = "substancePolymer"
    structureDefinition = "structureDefinition"
    substanceProtein = "substanceProtein"
    structureMap = "structureMap"
    substanceReferenceInformation = "substanceReferenceInformation"
    substanceSourceMaterial = "substanceSourceMaterial"
    substanceSpecification = "substanceSpecification"
    supplyDelivery = "supplyDelivery"
    supplyRequest = "supplyRequest"
    task = "task"
    terminologyCapabilities = "terminologyCapabilities"
    subscription = "subscription"
    substance = "substance"
    testScript = "testScript"
    valueSet = "valueSet"
    verificationResult = "verificationResult"
    visionPrescription = "visionPrescription"
    testReport = "testReport"
class ExampleMessageReasonCodes(Enum):
class PractitionerRole(Enum):
class ImmunizationEvaluationDoseStatusCodes(Enum):
class OperationOutcomeCodes(Enum):
class RiskEstimateType(Enum):
class AdverseEventCausalityMethod(Enum):
class AuditEventSourceType(Enum):
class V20487(Enum):
class SnomedctClinicalFindingsA(Enum):
class DataType(Enum):
    contactPoint = "contactPoint"
    contributor = "contributor"
    count = "count"
    address = "address"
    age = "age"
    annotation = "annotation"
    attachment = "attachment"
    backboneElement = "backboneElement"
    marketingStatus = "marketingStatus"
    codeableConcept = "codeableConcept"
    meta = "meta"
    coding = "coding"
    contactDetail = "contactDetail"
    money = "money"
    moneyQuantity = "moneyQuantity"
    dataRequirement = "dataRequirement"
    distance = "distance"
    dosage = "dosage"
    duration = "duration"
    element = "element"
    elementDefinition = "elementDefinition"
    expression = "expression"
    extension = "extension"
    humanName = "humanName"
    identifier = "identifier"
    sampledData = "sampledData"
    signature = "signature"
    simpleQuantity = "simpleQuantity"
    substanceAmount = "substanceAmount"
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
    uuid = "uuid"
    xhtml = "xhtml"
    timing = "timing"
    triggerDefinition = "triggerDefinition"
    usageContext = "usageContext"
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
    oid = "oid"
    positiveInt = "positiveInt"
    string = "string"
    time = "time"
    unsignedInt = "unsignedInt"
    uri = "uri"
    url = "url"
class PlanDefinitionType(Enum):
class V20116(Enum):
class FhirDefinedType(Enum):
class EncounterReasonCodes(Enum):
class ImmunizationRecommendationTargetDiseaseCodes(Enum):
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
    _398102009 = "_398102009"
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
    _27836007 = "_27836007"
class TestScriptOperationCode(Enum):
class V3FamilyMember(Enum):
class PaymentTypeCodes(Enum):
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
class FamilyHistoryAbsentReason(Enum):
class SupplyType(Enum):
class ImmunizationFundingSource(Enum):
class AdverseEventCausalityAssessment(Enum):
class V20276(Enum):
class MessageEvent(Enum):
class FdAMethod(Enum):
class Ensembl(Enum):
class ImmunizationTargetDiseaseCodes(Enum):
    _36989005 = "_36989005"
    _36653000 = "_36653000"
    _76902006 = "_76902006"
    _709410003 = "_709410003"
    _27836007 = "_27836007"
    _398102009 = "_398102009"
    _1857005 = "_1857005"
    _397430003 = "_397430003"
    _14189004 = "_14189004"
class ContainerCap(Enum):
class StudyType(Enum):
class CertaintySubcomponentRating(Enum):
class GoalCategory(Enum):
class SnomedctMedicationCodes(Enum):
class TestScriptProfileOriginType(Enum):
class LoincCodes(Enum):
class V3ServiceDeliveryLocationRoleType(Enum):
class ParticipantRoles(Enum):
class EffectEstimateType(Enum):
class RestfulSecurityService(Enum):
class GoalStartEvent(Enum):
    _32485007 = "_32485007"
    _308283009 = "_308283009"
    _442137000 = "_442137000"
    _386216000 = "_386216000"
class JurisdictionValueSet(Enum):
class ConditionOutcomeCodes(Enum):
class ActionType(Enum):
class AdverseEventCategory(Enum):
class EvidenceVariantState(Enum):
class QualityOfEvidenceRating(Enum):
class ActionParticipantRole(Enum):
class SignatureTypeCodes(Enum):
class PracticeSettingCodeValueSet(Enum):
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
    _408467006 = "_408467006"
    _394577000 = "_394577000"
    _394578005 = "_394578005"
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
    _394601005 = "_394601005"
    _394581000 = "_394581000"
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
    _394598000 = "_394598000"
    _394807007 = "_394807007"
    _419192003 = "_419192003"
    _408468001 = "_408468001"
    _394593009 = "_394593009"
    _394813003 = "_394813003"
    _410001006 = "_410001006"
    _394589003 = "_394589003"
    _394591006 = "_394591006"
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
    _394806003 = "_394806003"
    _394588006 = "_394588006"
    _408459003 = "_408459003"
    _394607009 = "_394607009"
    _419610006 = "_419610006"
    _418058008 = "_418058008"
    _420208008 = "_420208008"
    _418652005 = "_418652005"
    _418535003 = "_418535003"
    _418862001 = "_418862001"
    _419365004 = "_419365004"
    _418002000 = "_418002000"
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
    _394914008 = "_394914008"
    _408455009 = "_408455009"
    _394602003 = "_394602003"
    _408447002 = "_408447002"
    _394810000 = "_394810000"
    _408450004 = "_408450004"
    _408476004 = "_408476004"
    _408469009 = "_408469009"
    _408466002 = "_408466002"
    _408471009 = "_408471009"
    _408464004 = "_408464004"
    _409967009 = "_409967009"
    _408448007 = "_408448007"
    _419043006 = "_419043006"
    _394612005 = "_394612005"
    _394733009 = "_394733009"
    _394732004 = "_394732004"
    _394604002 = "_394604002"
    _394609007 = "_394609007"
    _408474001 = "_408474001"
    _394610002 = "_394610002"
    _394611003 = "_394611003"
    _408477008 = "_408477008"
    _394801008 = "_394801008"
    _408463005 = "_408463005"
    _419321007 = "_419321007"
    _394576009 = "_394576009"
    _394590007 = "_394590007"
class SpecimenContainerType(Enum):
class AuditEventId(Enum):
    _110100 = "_110100"
    _110101 = "_110101"
    _110102 = "_110102"
    _110103 = "_110103"
    _110104 = "_110104"
    _110105 = "_110105"
    _110106 = "_110106"
    _110107 = "_110107"
    _110108 = "_110108"
    _110109 = "_110109"
    _110110 = "_110110"
    _110111 = "_110111"
    _110114 = "_110114"
    _110112 = "_110112"
    _110113 = "_110113"
class CareTeamCategory(Enum):
class AppointmentCancellationReason(Enum):
class TestScriptProfileDestinationType(Enum):
class CommonLanguages(Enum):
    ar = "ar"
    bn = "bn"
    cs = "cs"
    da = "da"
    de = "de"
    deAt = "deAt"
    deCh = "deCh"
    deDe = "deDe"
    el = "el"
    en = "en"
    enAu = "enAu"
    enCa = "enCa"
    enGb = "enGb"
    enIn = "enIn"
    enNz = "enNz"
    enSg = "enSg"
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
    noNo = "noNo"
    pa = "pa"
    pl = "pl"
    pt = "pt"
    ptBr = "ptBr"
    ru = "ru"
    ruRu = "ruRu"
    sr = "sr"
    enUs = "enUs"
    es = "es"
    esAr = "esAr"
    esEs = "esEs"
    zhHk = "zhHk"
    zhSg = "zhSg"
    zhTw = "zhTw"
    srRs = "srRs"
    sv = "sv"
    svSe = "svSe"
    te = "te"
    zh = "zh"
    zhCn = "zhCn"
class GoalPriority(Enum):
class ImmunizationRecommendationStatusCodes(Enum):
class PaymentStatusCodes(Enum):
class SnomedctSupplyItem(Enum):
class CarePlanCategory(Enum):
class ContainerMaterials(Enum):
    _32039001 = "_32039001"
    _61088005 = "_61088005"
    _425620007 = "_425620007"
class SynthesisType(Enum):
class ConditionStage(Enum):
class PrecisionEstimateType(Enum):
class ProcedureCodesSnomedcT(Enum):
class AdverseEventSeriousness(Enum):
class AuditEventSubType(Enum):
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
    _110132 = "_110132"
    _110134 = "_110134"
    _110135 = "_110135"
    _110136 = "_110136"
    _110137 = "_110137"
    _110138 = "_110138"
    _110139 = "_110139"
    _110140 = "_110140"
    _110141 = "_110141"
    _110142 = "_110142"
    _110133 = "_110133"
class CatalogType(Enum):
class Chromosomehuman(Enum):
class CarePlanActivityOutcome(Enum):
class FhirDocumentTypeCodes(Enum):
class InvestigationType(Enum):
    _271336007 = "_271336007"
    _160237006 = "_160237006"
class ImmunizationEvaluationDoseStatusReasonCodes(Enum):
class ParticipationRoleType(Enum):
    amender = "amender"
    coauth = "coauth"
    cont = "cont"
    evtwit = "evtwit"
    primauth = "primauth"
    reviewer = "reviewer"
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
    named = "named"
    source = "source"
    prov = "prov"
    not = "not"
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
    nok = "nok"
    pat = "pat"
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
    grantee = "grantee"
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
    aut = "aut"
    _110155 = "_110155"


############################################
# Definition of Classes
############################################
