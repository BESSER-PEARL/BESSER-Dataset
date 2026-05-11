import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ContractResourceLegalStateCodes,
    CareTeamCategory,
    SupplyType,
    HandlingConditionSet,
    CoverageClassCodes,
    FhirDefinedType,
    ProvenanceActivityType,
    AppointmentCancellationReason,
    ListEmptyReasons,
    AuditEventSourceType,
    V3ParticipationMode,
    ProvenanceParticipantType,
    FundsReservationCodes,
    ClaimInformationCategoryCodes,
    MedicationStatusCodes,
    MediaType,
    ImagingStudySeriesPerformerFunction,
    RestfulSecurityService,
    ProcedureFollowUpCodesSnomedcT,
    MedicationDispenseStatusReasonCodes,
    ContractTermSubtypeCodes,
    ContractResourceScopeCodes,
    AuditEventEntityType,
    ConsentScopeCodes,
    MissingToothReasonCodes,
    FacilityTypeCodeValueSet,
    CarePlanActivityOutcome,
    ProcedureNotPerformedReasonSnomeDCT,
    ResearchStudyReasonStopped,
    SnomedctClinicalFindingsA,
    ServiceRequestOrderDetailsCodes,
    DiagnosticServiceSectionCodes,
    CoverageTypeAndSelfPayCodes,
    ResourceType,
    Diet,
    ProcedureCodesSnomedcT,
    ProcedureDeviceActionCodes,
    InsurancePlanType,
    ExampleRelatedClaimRelationshipCodes,
    RejectionCriterion,
    ProcessPriorityCodes,
    SnomedctDrugTherapyStatusCodes,
    ExampleDiagnosisTypeCodes,
    ObservationCategoryCodes,
    ContractResourceScopeCodesB,
    MedicationDispensePerformerFunctionCodes,
    MedicationDispenseCategoryCodes,
    ExampleMessageReasonCodes,
    V20116,
    ContractActorRoleCodes,
    ClaimTypeCodes,
    GoalAchievementStatus,
    UcumCodes,
    ContainerMaterials,
    DocumentSectionCodes,
    AuditEventSubType,
    V3ServiceDeliveryLocationRoleType,
    MedicationKnowledgeCharacteristicCodes,
    AuditEventEntityRole,
    ListOrderCodes,
    EnteralFormulaAdditiveTypeCode,
    DefinitionUseCodes,
    SupplyRequestReason,
    ServiceRequestCategoryCodes,
    ConsentCategoryCodes,
    AccountTypes,
    ExampleProviderQualificationCodes,
    CoverageCopayTypeCodes,
    CoverageEligibilityResponseAuthSupportCodes,
    LoincDiagnosticReportCodes,
    EvidenceVariantState,
    ChargeItemCode,
    CarePlanCategory,
    SpecialArrangements,
    ClaimPayeeTypeCodes,
    ClaimCareTeamRoleCodes,
    DataType,
    MediaModality,
    ConsentContentClass,
    ConsentPolicyRuleCodes,
    EnteralRouteCodes,
    ContractResourceSecurityControlCodes,
    AcquisitionModality,
    SupplementTypeCodes,
    TestScriptProfileOriginType,
    EncounterReasonCodes,
    MediaTypeCode,
    MessageTransport,
    CommunicationTopic,
    ExampleVisionPrescriptionProductCodes,
    V20487,
    ExceptionCodes,
    SnomedctSupplyItem,
    ConsentActionCodes,
    TestScriptProfileDestinationType,
    AuditEventId,
    ObservationMethods,
    SubscriberRelationshipCodes,
    MedicationKnowledgePackageTypeCodes,
    V3ActConsentDirective,
    CertaintySubcomponentRating,
    ContainerCap,
    ClinicalImpressionPrognosis,
    IcD10Codes,
    CommunicationCategory,
    PreparePatient,
    ConditionOutcomeCodes,
    UsageContextType,
    ContractResourceAssetTypeCodes,
    DischargeDisposition,
    V20092,
    ExampleClaimSubTypeCodes,
    TestScriptOperationCode,
    IdentifierTypeCodes,
    ProcedureReasonCodes,
    ContractResourceScopeCodesA,
    ContractTypeCodes,
    EffectEstimateType,
    LocationType,
    MessageEvent,
    OrganizationAffiliationRole,
    ProcedureCategoryCodesSnomedcT,
    ContractResourcePartyRoleCodes,
    V20371,
    Laterality,
    ContractSubtypeCodes,
    ResearchStudyObjectiveType,
    PatientRelationshipType,
    PracticeSettingCodeValueSet,
    ObservationReferenceRangeAppliesToCodes,
    CommunicationNotDoneReason,
    MediaCollectionViewProjection,
    ContractResourceActionStatusCodes,
    V20276,
    AdmitSource,
    SnomedctMedicationCodes,
    ContractResourceDefinitionSubtypeCodes,
    SpecimenCollection,
    SnomedctFormCodes,
    AdverseEventCategory,
    PaymentStatusCodes,
    ContractTermTypeCodes,
    BasicResourceTypes,
    ContractResourceAssetSubTypeCodes,
    ExampleDiagnosisOnAdmissionCodes,
    ResearchStudyPhase,
    SpecialCourtesy,
    ConditionStageType,
    ContractResourceAssetScopeCodes,
    ProvenanceParticipantRole,
    ResearchStudyPrimaryPurposeType,
    ContractResourceAssetContextCodes,
    EnteralFormulaTypeCodes,
    ServiceCategory,
    ParticipationRoleType,
    ObjectLifecycleEvents,
    FhirDocumentTypeCodes,
    ContractContentDerivationCodes,
    DiagnosisRole,
    ContractResourceDecisionModeCodes,
    ContractResourceExpirationTypeCodes,
    ContextOfUseValueSet,
    ConsentContentCodes,
    RiskProbability,
    V3ActPharmacySupplyType,
    PatientMedicineChangeTypes,
    ProcedureOutcomeCodesSnomedcT,
    SpecimenContainerType,
    ExampleCoverageFinancialExceptionCodes,
    ParticipantRoles,
    ObservationReferenceRangeMeaningCodes,
    ContractActionCodes,
    ExampleDiagnosisRelatedGroupCodes,
    V3PurposeOfUse,
    ContractResourceAssetAvailiabilityCodes,
    JurisdictionValueSet,
    BodystructureLocationQualifier,
    ContractResourceDefinitionTypeCodes,
    VaccineAdministeredValueSet,
    ConditionStage,
    NetworkTypeCodes,
    ConditionProblemDiagnosisCodes,
    Verificationresultcommunicationmethod,
    ImmunizationRouteCodes,
    DesignationUse,
    DoseAndRateType,
    ReasonMedicationGivenCodes,
    ActionParticipantRole,
    FhirDeviceTypes,
    EpisodeOfCareType,
    SignatureTypeCodes,
    AdverseEventCausalityMethod,
    Ensembl,
    ImmunizationRecommendationDateCriterionCodes,
    ServiceProvisionConditions,
    ParticipantType,
    MeasureType,
    DetectedIssueCategory,
    SecurityRoleType,
    ImmunizationSubpotentReason,
    CertaintySubcomponentType,
    Validationtype,
    ImmunizationFunctionCodes,
    MeasurePopulationType,
    DocumentReferenceFormatCodeSet,
    ReferralMethod,
    ImmunizationTargetDiseaseCodes,
    FhirDeviceStatusReason,
    CodesForImmunizationSiteOfAdministration,
    DietCodes,
    OrganizationType,
    ImmunizationEvaluationDoseStatusReasonCodes,
    MedicationRequestCourseOfTherapyCodes,
    FormCodes,
    V20916,
    MeasureScoring,
    Pushtypeavailable,
    PractitionerRole,
    SnomedctAdditionalDosageInstructions,
    FlagCategory,
    BenefitTypeCodes,
    MedicationRequestCategoryCodes,
    TimingAbbreviation,
    V3SubstanceAdminSubstitutionReason,
    V3FamilyMember,
    CompositeMeasureScoring,
    OralSiteCodes,
    Program,
    ImmunizationEvaluationDoseStatusCodes,
    Validationprocess,
    ModifierTypeCodes,
    SnomedctAdministrationMethodCodes,
    AdjudicationValueCodes,
    GoalStartEvent,
    BenefitTermCodes,
    FdAStandardSequence,
    QuestionnaireQuestionCodes,
    ProcedurePerformerRoleCodes,
    ExamplePaymentTypeCodes,
    SnomedctClinicalFindings,
    ExpressionLanguage,
    ImmunizationRecommendationReasonCodes,
    FlagCode,
    ManifestationAndSymptomCodes,
    PlanDefinitionType,
    AdjudicationReasonCodes,
    ImmunizationRecommendationStatusCodes,
    PrecisionEstimateType,
    ImmunizationProgramEligibility,
    GoalPriority,
    Canpushupdates,
    LoincCodes,
    FhirSpecimenCollectionMethod,
    SnomedctAnatomicalStructureForAdministrationSiteCodes,
    ExampleUseCodesForList,
    Primarysourcetype,
    EncounterType,
    OperationOutcomeCodes,
    ExampleRevenueCenterCodes,
    Chromosomehuman,
    V20493,
    ExampleServicePlaceCodes,
    ProvenanceHistoryRecordActivityCodes,
    MedicationAdministrationPerformerFunctionCodes,
    ImmunizationStatusReasonCodes,
    GoalCategory,
    V3ActCode,
    SubstanceCode,
    CatalogType,
    ConditionCategoryCodes,
    EndpointConnectionType,
    DataAbsentReason,
    PatientContactRelationship,
    AdverseEventCausalityAssessment,
    ImmunizationFundingSource,
    ImmunizationOriginCodes,
    AllSecurityLabels,
    PaymentTypeCodes,
    ConditionDiagnosisSeverity,
    MedicationAdministrationCategoryCodes,
    ActionType,
    LibraryType,
    ImmunizationRecommendationTargetDiseaseCodes,
    TextureModifiedFoodTypeCodes,
    V3ActIncidentCode,
    V2036027,
    StudyType,
    VitalSigns,
    MedicationRequestStatusReasonCodes,
    V3ActReason,
    TextureModifierCodes,
    Validationstatus,
    SnomedctReasonMedicationNotGivenCodes,
    SnomedctMorphologicAbnormalities,
    SubstanceCategoryCodes,
    AllergyIntoleranceSubstanceProductConditionAndNegationCodes,
    QuestionnaireAnswerCodes,
    DeviceMetricAndComponentTypes,
    V3ActSubstanceAdminSubstitutionCode,
    PaymentAdjustmentReasonCodes,
    SynthesisType,
    SnomedctRouteCodes,
    InvestigationType,
    UnitTypeCodes,
    SnomedctBodyStructures,
    ExampleProcedureTypeCodes,
    DeviceSafety,
    NutrientModifierCodes,
    FoodTypeCodes,
    Failureaction,
    ImmunizationEvaluationTargetDiseaseCodes,
    ContactEntityType,
    ContractSignerTypeCodes,
    DetectedIssueMitigationAction,
    DocumentClassValueSet,
    FamilyHistoryAbsentReason,
    FluidConsistencyTypeCodes,
    ServiceType,
    BenefitCategoryCodes,
    EndpointPayloadType,
    QualityOfEvidenceRating,
    DefinitionTopic,
    IcD10ProcedureCodes,
    DeviceType,
    UsclsCodes,
    SpecimenProcessingProcedure,
    SurfaceCodes,
    MeasureDataUsage,
    RiskEstimateType,
    V3ActEncounterCode,
    AdjudicationErrorCodes,
    SnomedctMedicationAsNeededReasonCodes,
    ImmunizationReasonCodes,
    TaskCode,
    CommonTags,
    MaritalStatusCodes,
    CommonLanguages,
    AdverseEventSeriousness,
    SubjectType,
    ObservationInterpretationCodes,
    ExampleProgramReasonCodes,
    FdAMethod,
    V3ActPriority,
    Need,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================

def test_contractresourcelegalstatecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceLegalStateCodes is not None

def test_contractresourcelegalstatecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceLegalStateCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceLegalStateCodes"

def test_careteamcategory_exists():
    # Check that the Enumeration exists
    assert CareTeamCategory is not None

def test_careteamcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CareTeamCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CareTeamCategory"

def test_supplytype_exists():
    # Check that the Enumeration exists
    assert SupplyType is not None

def test_supplytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SupplyType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SupplyType"

def test_handlingconditionset_exists():
    # Check that the Enumeration exists
    assert HandlingConditionSet is not None

def test_handlingconditionset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HandlingConditionSet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HandlingConditionSet"

def test_coverageclasscodes_exists():
    # Check that the Enumeration exists
    assert CoverageClassCodes is not None

def test_coverageclasscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoverageClassCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoverageClassCodes"

def test_fhirdefinedtype_exists():
    # Check that the Enumeration exists
    assert FhirDefinedType is not None

def test_fhirdefinedtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FhirDefinedType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FhirDefinedType"

def test_provenanceactivitytype_exists():
    # Check that the Enumeration exists
    assert ProvenanceActivityType is not None

def test_provenanceactivitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProvenanceActivityType]
    expected_literals = [
        "update",
        "append",
        "mask",
        "la",
        "create",
        "delete",
        "label",
        "pseud",
        "deid",
        "nullify",
        "anony",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProvenanceActivityType"

def test_appointmentcancellationreason_exists():
    # Check that the Enumeration exists
    assert AppointmentCancellationReason is not None

def test_appointmentcancellationreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AppointmentCancellationReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AppointmentCancellationReason"

def test_listemptyreasons_exists():
    # Check that the Enumeration exists
    assert ListEmptyReasons is not None

def test_listemptyreasons_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ListEmptyReasons]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ListEmptyReasons"

def test_auditeventsourcetype_exists():
    # Check that the Enumeration exists
    assert AuditEventSourceType is not None

def test_auditeventsourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuditEventSourceType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuditEventSourceType"

def test_v3participationmode_exists():
    # Check that the Enumeration exists
    assert V3ParticipationMode is not None

def test_v3participationmode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ParticipationMode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ParticipationMode"

def test_provenanceparticipanttype_exists():
    # Check that the Enumeration exists
    assert ProvenanceParticipantType is not None

def test_provenanceparticipanttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProvenanceParticipantType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProvenanceParticipantType"

def test_fundsreservationcodes_exists():
    # Check that the Enumeration exists
    assert FundsReservationCodes is not None

def test_fundsreservationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FundsReservationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FundsReservationCodes"

def test_claiminformationcategorycodes_exists():
    # Check that the Enumeration exists
    assert ClaimInformationCategoryCodes is not None

def test_claiminformationcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClaimInformationCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClaimInformationCategoryCodes"

def test_medicationstatuscodes_exists():
    # Check that the Enumeration exists
    assert MedicationStatusCodes is not None

def test_medicationstatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationStatusCodes"

def test_mediatype_exists():
    # Check that the Enumeration exists
    assert MediaType is not None

def test_mediatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaType"

def test_imagingstudyseriesperformerfunction_exists():
    # Check that the Enumeration exists
    assert ImagingStudySeriesPerformerFunction is not None

def test_imagingstudyseriesperformerfunction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImagingStudySeriesPerformerFunction]
    expected_literals = [
        "con",
        "ref",
        "sprf",
        "vrf",
        "prf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImagingStudySeriesPerformerFunction"

def test_restfulsecurityservice_exists():
    # Check that the Enumeration exists
    assert RestfulSecurityService is not None

def test_restfulsecurityservice_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RestfulSecurityService]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RestfulSecurityService"

def test_procedurefollowupcodessnomedct_exists():
    # Check that the Enumeration exists
    assert ProcedureFollowUpCodesSnomedcT is not None

def test_procedurefollowupcodessnomedct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureFollowUpCodesSnomedcT]
    expected_literals = [
        "_18949003",
        "_225164002",
        "_447346005",
        "_229506003",
        "_30549001",
        "_241031001",
        "_35963001",
        "_394725008",
        "_274441001",
        "_359825008",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureFollowUpCodesSnomedcT"

def test_medicationdispensestatusreasoncodes_exists():
    # Check that the Enumeration exists
    assert MedicationDispenseStatusReasonCodes is not None

def test_medicationdispensestatusreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationDispenseStatusReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationDispenseStatusReasonCodes"

def test_contracttermsubtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractTermSubtypeCodes is not None

def test_contracttermsubtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractTermSubtypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractTermSubtypeCodes"

def test_contractresourcescopecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceScopeCodes is not None

def test_contractresourcescopecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceScopeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceScopeCodes"

def test_auditevententitytype_exists():
    # Check that the Enumeration exists
    assert AuditEventEntityType is not None

def test_auditevententitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuditEventEntityType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuditEventEntityType"

def test_consentscopecodes_exists():
    # Check that the Enumeration exists
    assert ConsentScopeCodes is not None

def test_consentscopecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentScopeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentScopeCodes"

def test_missingtoothreasoncodes_exists():
    # Check that the Enumeration exists
    assert MissingToothReasonCodes is not None

def test_missingtoothreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MissingToothReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MissingToothReasonCodes"

def test_facilitytypecodevalueset_exists():
    # Check that the Enumeration exists
    assert FacilityTypeCodeValueSet is not None

def test_facilitytypecodevalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FacilityTypeCodeValueSet]
    expected_literals = [
        "_79993009",
        "_11424001",
        "_90484001",
        "_69362002",
        "_5584006",
        "_46224007",
        "_14866005",
        "_23392004",
        "_394777002",
        "_10531005",
        "_41844007",
        "_78001009",
        "_33022008",
        "_73770003",
        "_52668009",
        "_77931003",
        "_1773006",
        "_10206005",
        "_35971002",
        "_413817003",
        "_310205006",
        "_39350007",
        "_901005",
        "_36125001",
        "_272501009",
        "_275576008",
        "_58482006",
        "_32074000",
        "_225732001",
        "_284546000",
        "_45618002",
        "_2849009",
        "_78088001",
        "_331006",
        "_405607001",
        "_309900005",
        "_20078004",
        "_25681007",
        "_72311000",
        "_73644007",
        "_37550003",
        "_360957003",
        "_419955002",
        "_413456002",
        "_45899008",
        "_51563005",
        "_42665001",
        "_4322002",
        "_31628002",
        "_81234003",
        "_38238005",
        "_48311003",
        "_3729002",
        "_37546005",
        "_19602009",
        "_62480006",
        "_57159002",
        "_409519008",
        "_309898008",
        "_59374000",
        "_36293008",
        "_50569004",
        "_83891005",
        "_56189001",
        "_39913001",
        "_56293002",
        "_2081004",
        "_418518002",
        "_224687002",
        "_6827000",
        "_80522000",
        "_89972002",
        "_394759007",
        "_360966004",
        "_91154008",
        "_22549003",
        "_82242000",
        "_1814000",
        "_79491001",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FacilityTypeCodeValueSet"

def test_careplanactivityoutcome_exists():
    # Check that the Enumeration exists
    assert CarePlanActivityOutcome is not None

def test_careplanactivityoutcome_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CarePlanActivityOutcome]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CarePlanActivityOutcome"

def test_procedurenotperformedreasonsnomedct_exists():
    # Check that the Enumeration exists
    assert ProcedureNotPerformedReasonSnomeDCT is not None

def test_procedurenotperformedreasonsnomedct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureNotPerformedReasonSnomeDCT]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureNotPerformedReasonSnomeDCT"

def test_researchstudyreasonstopped_exists():
    # Check that the Enumeration exists
    assert ResearchStudyReasonStopped is not None

def test_researchstudyreasonstopped_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResearchStudyReasonStopped]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResearchStudyReasonStopped"

def test_snomedctclinicalfindingsa_exists():
    # Check that the Enumeration exists
    assert SnomedctClinicalFindingsA is not None

def test_snomedctclinicalfindingsa_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctClinicalFindingsA]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctClinicalFindingsA"

def test_servicerequestorderdetailscodes_exists():
    # Check that the Enumeration exists
    assert ServiceRequestOrderDetailsCodes is not None

def test_servicerequestorderdetailscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceRequestOrderDetailsCodes]
    expected_literals = [
        "_47545007",
        "_243150007",
        "_243144002",
        "_286812008",
        "_59427005",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceRequestOrderDetailsCodes"

def test_diagnosticservicesectioncodes_exists():
    # Check that the Enumeration exists
    assert DiagnosticServiceSectionCodes is not None

def test_diagnosticservicesectioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagnosticServiceSectionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagnosticServiceSectionCodes"

def test_coveragetypeandselfpaycodes_exists():
    # Check that the Enumeration exists
    assert CoverageTypeAndSelfPayCodes is not None

def test_coveragetypeandselfpaycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoverageTypeAndSelfPayCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoverageTypeAndSelfPayCodes"

def test_resourcetype_exists():
    # Check that the Enumeration exists
    assert ResourceType is not None

def test_resourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResourceType]
    expected_literals = [
        "riskEvidenceSynthesis",
        "detectedIssue",
        "enrollmentResponse",
        "testReport",
        "goal",
        "immunizationEvaluation",
        "media",
        "structureDefinition",
        "diagnosticReport",
        "searchParameter",
        "flag",
        "clinicalImpression",
        "substanceReferenceInformation",
        "substance",
        "medicationRequest",
        "messageDefinition",
        "namingSystem",
        "measureReport",
        "auditEvent",
        "bodyStructure",
        "visionPrescription",
        "familyMemberHistory",
        "researchElementDefinition",
        "compartmentDefinition",
        "subscription",
        "schedule",
        "testScript",
        "messageHeader",
        "episodeOfCare",
        "medicinalProductIndication",
        "researchStudy",
        "medicinalProductInteraction",
        "resource",
        "list",
        "substanceProtein",
        "medicinalProductUndesirableEffect",
        "supplyDelivery",
        "encounter",
        "terminologyCapabilities",
        "binary",
        "slot",
        "deviceMetric",
        "invoice",
        "appointmentResponse",
        "location",
        "organization",
        "bundle",
        "communicationRequest",
        "communication",
        "guidanceResponse",
        "carePlan",
        "questionnaire",
        "molecularSequence",
        "specimenDefinition",
        "evidence",
        "medicationDispense",
        "evidenceVariable",
        "substanceSourceMaterial",
        "medicationStatement",
        "adverseEvent",
        "medicinalProductAuthorization",
        "substanceNucleicAcid",
        "procedure",
        "deviceDefinition",
        "researchDefinition",
        "nutritionOrder",
        "enrollmentRequest",
        "documentManifest",
        "insurancePlan",
        "composition",
        "condition",
        "operationDefinition",
        "observationDefinition",
        "careTeam",
        "contract",
        "structureMap",
        "supplyRequest",
        "conceptMap",
        "catalogEntry",
        "observation",
        "domainResource",
        "medicinalProductPharmaceutical",
        "medicationKnowledge",
        "provenance",
        "group",
        "medication",
        "medicinalProductContraindication",
        "codeSystem",
        "immunization",
        "measure",
        "effectEvidenceSynthesis",
        "paymentNotice",
        "valueSet",
        "deviceUseStatement",
        "parameters",
        "capabilityStatement",
        "coverage",
        "coverageEligibilityResponse",
        "medicationAdministration",
        "planDefinition",
        "substanceSpecification",
        "questionnaireResponse",
        "operationOutcome",
        "chargeItemDefinition",
        "verificationResult",
        "medicinalProduct",
        "linkage",
        "documentReference",
        "practitionerRole",
        "healthcareService",
        "eventDefinition",
        "medicinalProductIngredient",
        "medicinalProductManufactured",
        "implementationGuide",
        "substancePolymer",
        "patient",
        "endpoint",
        "medicinalProductPackaged",
        "exampleScenario",
        "activityDefinition",
        "biologicallyDerivedProduct",
        "explanationOfBenefit",
        "requestGroup",
        "riskAssessment",
        "researchSubject",
        "deviceRequest",
        "person",
        "serviceRequest",
        "appointment",
        "task",
        "chargeItem",
        "account",
        "paymentReconciliation",
        "organizationAffiliation",
        "basic",
        "consent",
        "practitioner",
        "allergyIntolerance",
        "imagingStudy",
        "immunizationRecommendation",
        "coverageEligibilityRequest",
        "claim",
        "specimen",
        "graphDefinition",
        "claimResponse",
        "relatedPerson",
        "device",
        "library",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResourceType"

def test_diet_exists():
    # Check that the Enumeration exists
    assert Diet is not None

def test_diet_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Diet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Diet"

def test_procedurecodessnomedct_exists():
    # Check that the Enumeration exists
    assert ProcedureCodesSnomedcT is not None

def test_procedurecodessnomedct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureCodesSnomedcT]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureCodesSnomedcT"

def test_proceduredeviceactioncodes_exists():
    # Check that the Enumeration exists
    assert ProcedureDeviceActionCodes is not None

def test_proceduredeviceactioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureDeviceActionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureDeviceActionCodes"

def test_insuranceplantype_exists():
    # Check that the Enumeration exists
    assert InsurancePlanType is not None

def test_insuranceplantype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InsurancePlanType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InsurancePlanType"

def test_examplerelatedclaimrelationshipcodes_exists():
    # Check that the Enumeration exists
    assert ExampleRelatedClaimRelationshipCodes is not None

def test_examplerelatedclaimrelationshipcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleRelatedClaimRelationshipCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleRelatedClaimRelationshipCodes"

def test_rejectioncriterion_exists():
    # Check that the Enumeration exists
    assert RejectionCriterion is not None

def test_rejectioncriterion_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RejectionCriterion]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RejectionCriterion"

def test_processprioritycodes_exists():
    # Check that the Enumeration exists
    assert ProcessPriorityCodes is not None

def test_processprioritycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcessPriorityCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessPriorityCodes"

def test_snomedctdrugtherapystatuscodes_exists():
    # Check that the Enumeration exists
    assert SnomedctDrugTherapyStatusCodes is not None

def test_snomedctdrugtherapystatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctDrugTherapyStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctDrugTherapyStatusCodes"

def test_examplediagnosistypecodes_exists():
    # Check that the Enumeration exists
    assert ExampleDiagnosisTypeCodes is not None

def test_examplediagnosistypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleDiagnosisTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleDiagnosisTypeCodes"

def test_observationcategorycodes_exists():
    # Check that the Enumeration exists
    assert ObservationCategoryCodes is not None

def test_observationcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObservationCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObservationCategoryCodes"

def test_contractresourcescopecodesb_exists():
    # Check that the Enumeration exists
    assert ContractResourceScopeCodesB is not None

def test_contractresourcescopecodesb_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceScopeCodesB]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceScopeCodesB"

def test_medicationdispenseperformerfunctioncodes_exists():
    # Check that the Enumeration exists
    assert MedicationDispensePerformerFunctionCodes is not None

def test_medicationdispenseperformerfunctioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationDispensePerformerFunctionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationDispensePerformerFunctionCodes"

def test_medicationdispensecategorycodes_exists():
    # Check that the Enumeration exists
    assert MedicationDispenseCategoryCodes is not None

def test_medicationdispensecategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationDispenseCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationDispenseCategoryCodes"

def test_examplemessagereasoncodes_exists():
    # Check that the Enumeration exists
    assert ExampleMessageReasonCodes is not None

def test_examplemessagereasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleMessageReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleMessageReasonCodes"

def test_v20116_exists():
    # Check that the Enumeration exists
    assert V20116 is not None

def test_v20116_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20116]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20116"

def test_contractactorrolecodes_exists():
    # Check that the Enumeration exists
    assert ContractActorRoleCodes is not None

def test_contractactorrolecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractActorRoleCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractActorRoleCodes"

def test_claimtypecodes_exists():
    # Check that the Enumeration exists
    assert ClaimTypeCodes is not None

def test_claimtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClaimTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClaimTypeCodes"

def test_goalachievementstatus_exists():
    # Check that the Enumeration exists
    assert GoalAchievementStatus is not None

def test_goalachievementstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoalAchievementStatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoalAchievementStatus"

def test_ucumcodes_exists():
    # Check that the Enumeration exists
    assert UcumCodes is not None

def test_ucumcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UcumCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UcumCodes"

def test_containermaterials_exists():
    # Check that the Enumeration exists
    assert ContainerMaterials is not None

def test_containermaterials_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerMaterials]
    expected_literals = [
        "_61088005",
        "_32039001",
        "_425620007",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerMaterials"

def test_documentsectioncodes_exists():
    # Check that the Enumeration exists
    assert DocumentSectionCodes is not None

def test_documentsectioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocumentSectionCodes]
    expected_literals = [
        "_113480",
        "_597724",
        "_187765",
        "_295543",
        "_518480",
        "_423467",
        "_697300",
        "_87163",
        "_115352",
        "_611509B",
        "_578526",
        "_597765",
        "_86538",
        "_423442",
        "_102103",
        "_101576",
        "_297622",
        "_551226",
        "_551093",
        "_115378",
        "_102186A",
        "_474205",
        "_114934",
        "_101543",
        "_292995",
        "_101642",
        "_597732",
        "_309542",
        "_597690",
        "_102236",
        "_101832",
        "_101840",
        "_295493",
        "_462408",
        "_611491",
        "_102186",
        "_102160",
        "_113290",
        "_597708",
        "_597757",
        "_295451",
        "_487652",
        "_86488",
        "_597682",
        "_462648",
        "_475194",
        "_597716",
        "_611509",
        "_188417",
        "_102228",
        "_487686",
        "_113696",
        "_101873",
        "_423491",
        "_101600",
        "_423483",
        "_462416",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocumentSectionCodes"

def test_auditeventsubtype_exists():
    # Check that the Enumeration exists
    assert AuditEventSubType is not None

def test_auditeventsubtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuditEventSubType]
    expected_literals = [
        "_110131",
        "_110128",
        "_110127",
        "_110132",
        "_110134",
        "_110139",
        "_110121",
        "_110135",
        "_110138",
        "_110122",
        "_110136",
        "_110142",
        "_110120",
        "_110125",
        "_110129",
        "_110140",
        "_110124",
        "_110130",
        "_110137",
        "_110123",
        "_110126",
        "_110133",
        "_110141",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuditEventSubType"

def test_v3servicedeliverylocationroletype_exists():
    # Check that the Enumeration exists
    assert V3ServiceDeliveryLocationRoleType is not None

def test_v3servicedeliverylocationroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ServiceDeliveryLocationRoleType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ServiceDeliveryLocationRoleType"

def test_medicationknowledgecharacteristiccodes_exists():
    # Check that the Enumeration exists
    assert MedicationKnowledgeCharacteristicCodes is not None

def test_medicationknowledgecharacteristiccodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationKnowledgeCharacteristicCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationKnowledgeCharacteristicCodes"

def test_auditevententityrole_exists():
    # Check that the Enumeration exists
    assert AuditEventEntityRole is not None

def test_auditevententityrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuditEventEntityRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuditEventEntityRole"

def test_listordercodes_exists():
    # Check that the Enumeration exists
    assert ListOrderCodes is not None

def test_listordercodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ListOrderCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ListOrderCodes"

def test_enteralformulaadditivetypecode_exists():
    # Check that the Enumeration exists
    assert EnteralFormulaAdditiveTypeCode is not None

def test_enteralformulaadditivetypecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnteralFormulaAdditiveTypeCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnteralFormulaAdditiveTypeCode"

def test_definitionusecodes_exists():
    # Check that the Enumeration exists
    assert DefinitionUseCodes is not None

def test_definitionusecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefinitionUseCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefinitionUseCodes"

def test_supplyrequestreason_exists():
    # Check that the Enumeration exists
    assert SupplyRequestReason is not None

def test_supplyrequestreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SupplyRequestReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SupplyRequestReason"

def test_servicerequestcategorycodes_exists():
    # Check that the Enumeration exists
    assert ServiceRequestCategoryCodes is not None

def test_servicerequestcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceRequestCategoryCodes]
    expected_literals = [
        "_409073007",
        "_387713003",
        "_409063005",
        "_363679005",
        "_108252007",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceRequestCategoryCodes"

def test_consentcategorycodes_exists():
    # Check that the Enumeration exists
    assert ConsentCategoryCodes is not None

def test_consentcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentCategoryCodes]
    expected_literals = [
        "_570168",
        "_642926",
        "_570176",
        "_592840",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentCategoryCodes"

def test_accounttypes_exists():
    # Check that the Enumeration exists
    assert AccountTypes is not None

def test_accounttypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccountTypes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccountTypes"

def test_exampleproviderqualificationcodes_exists():
    # Check that the Enumeration exists
    assert ExampleProviderQualificationCodes is not None

def test_exampleproviderqualificationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleProviderQualificationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleProviderQualificationCodes"

def test_coveragecopaytypecodes_exists():
    # Check that the Enumeration exists
    assert CoverageCopayTypeCodes is not None

def test_coveragecopaytypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoverageCopayTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoverageCopayTypeCodes"

def test_coverageeligibilityresponseauthsupportcodes_exists():
    # Check that the Enumeration exists
    assert CoverageEligibilityResponseAuthSupportCodes is not None

def test_coverageeligibilityresponseauthsupportcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CoverageEligibilityResponseAuthSupportCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CoverageEligibilityResponseAuthSupportCodes"

def test_loincdiagnosticreportcodes_exists():
    # Check that the Enumeration exists
    assert LoincDiagnosticReportCodes is not None

def test_loincdiagnosticreportcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoincDiagnosticReportCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoincDiagnosticReportCodes"

def test_evidencevariantstate_exists():
    # Check that the Enumeration exists
    assert EvidenceVariantState is not None

def test_evidencevariantstate_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EvidenceVariantState]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EvidenceVariantState"

def test_chargeitemcode_exists():
    # Check that the Enumeration exists
    assert ChargeItemCode is not None

def test_chargeitemcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChargeItemCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChargeItemCode"

def test_careplancategory_exists():
    # Check that the Enumeration exists
    assert CarePlanCategory is not None

def test_careplancategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CarePlanCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CarePlanCategory"

def test_specialarrangements_exists():
    # Check that the Enumeration exists
    assert SpecialArrangements is not None

def test_specialarrangements_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialArrangements]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecialArrangements"

def test_claimpayeetypecodes_exists():
    # Check that the Enumeration exists
    assert ClaimPayeeTypeCodes is not None

def test_claimpayeetypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClaimPayeeTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClaimPayeeTypeCodes"

def test_claimcareteamrolecodes_exists():
    # Check that the Enumeration exists
    assert ClaimCareTeamRoleCodes is not None

def test_claimcareteamrolecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClaimCareTeamRoleCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClaimCareTeamRoleCodes"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "money",
        "element",
        "base64Binary",
        "population",
        "quantity",
        "triggerDefinition",
        "code",
        "markdown",
        "backboneElement",
        "productShelfLife",
        "xhtml",
        "marketingStatus",
        "canonical",
        "integer",
        "age",
        "range",
        "codeableConcept",
        "dateTime",
        "time",
        "address",
        "coding",
        "elementDefinition",
        "instant",
        "prodCharacteristic",
        "identifier",
        "narrative",
        "ratio",
        "humanName",
        "sampledData",
        "string",
        "dataRequirement",
        "attachment",
        "date",
        "relatedArtifact",
        "decimal",
        "moneyQuantity",
        "distance",
        "annotation",
        "positiveInt",
        "expression",
        "usageContext",
        "contactDetail",
        "contactPoint",
        "url",
        "count",
        "signature",
        "unsignedInt",
        "period",
        "oid",
        "uuid",
        "boolean",
        "uri",
        "substanceAmount",
        "contributor",
        "parameterDefinition",
        "reference",
        "timing",
        "dosage",
        "simpleQuantity",
        "duration",
        "id",
        "extension",
        "meta",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_mediamodality_exists():
    # Check that the Enumeration exists
    assert MediaModality is not None

def test_mediamodality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaModality]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaModality"

def test_consentcontentclass_exists():
    # Check that the Enumeration exists
    assert ConsentContentClass is not None

def test_consentcontentclass_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentContentClass]
    expected_literals = [
        "applicationhl7cdaxml",
        "httphl7orgfhirStructureDefinitionlipidprofile",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentContentClass"

def test_consentpolicyrulecodes_exists():
    # Check that the Enumeration exists
    assert ConsentPolicyRuleCodes is not None

def test_consentpolicyrulecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentPolicyRuleCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentPolicyRuleCodes"

def test_enteralroutecodes_exists():
    # Check that the Enumeration exists
    assert EnteralRouteCodes is not None

def test_enteralroutecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnteralRouteCodes]
    expected_literals = [
        "jjtinstl",
        "po",
        "gjt",
        "ojj",
        "eft",
        "ngt",
        "ogt",
        "entinstl",
        "gt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnteralRouteCodes"

def test_contractresourcesecuritycontrolcodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceSecurityControlCodes is not None

def test_contractresourcesecuritycontrolcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceSecurityControlCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceSecurityControlCodes"

def test_acquisitionmodality_exists():
    # Check that the Enumeration exists
    assert AcquisitionModality is not None

def test_acquisitionmodality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AcquisitionModality]
    expected_literals = [
        "bdus",
        "px",
        "rf",
        "cr",
        "oss",
        "mr",
        "eps",
        "us",
        "sm",
        "ar",
        "dx",
        "xa",
        "bmd",
        "xc",
        "ivoct",
        "mg",
        "rg",
        "oam",
        "opr",
        "ivus",
        "va",
        "opv",
        "nm",
        "gm",
        "oct",
        "io",
        "ker",
        "pt",
        "opm",
        "es",
        "ct",
        "op",
        "ecg",
        "opt",
        "srf",
        "hd",
        "len",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AcquisitionModality"

def test_supplementtypecodes_exists():
    # Check that the Enumeration exists
    assert SupplementTypeCodes is not None

def test_supplementtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SupplementTypeCodes]
    expected_literals = [
        "_444361000124102",
        "_443011000124100",
        "_442971000124100",
        "_443021000124108",
        "_441531000124102",
        "_443111000124101",
        "_442931000124103",
        "_442651000124102",
        "_442961000124107",
        "_443431000124102",
        "_443441000124107",
        "_441561000124106",
        "_443461000124106",
        "_443361000124100",
        "_443501000124106",
        "_442901000124106",
        "_442911000124109",
        "_444371000124109",
        "_443401000124105",
        "_443561000124107",
        "_441591000124103",
        "_443451000124109",
        "_443031000124106",
        "_443771000124106",
        "_442981000124102",
        "_441601000124106",
        "_442941000124108",
        "_442951000124105",
        "_443391000124108",
        "_443411000124108",
        "_444381000124107",
        "_441671000124100",
        "_443471000124104",
        "_443491000124103",
        "_442991000124104",
        "_441571000124104",
        "_444401000124107",
        "_444431000124104",
        "_444331000124106",
        "_443051000124104",
        "_443351000124102",
        "_443481000124101",
        "_443421000124100",
        "_444321000124108",
        "_442921000124101",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SupplementTypeCodes"

def test_testscriptprofileorigintype_exists():
    # Check that the Enumeration exists
    assert TestScriptProfileOriginType is not None

def test_testscriptprofileorigintype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestScriptProfileOriginType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestScriptProfileOriginType"

def test_encounterreasoncodes_exists():
    # Check that the Enumeration exists
    assert EncounterReasonCodes is not None

def test_encounterreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EncounterReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EncounterReasonCodes"

def test_mediatypecode_exists():
    # Check that the Enumeration exists
    assert MediaTypeCode is not None

def test_mediatypecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaTypeCode]
    expected_literals = [
        "_110035",
        "_110032",
        "_110036",
        "_110034",
        "_110037",
        "_110038",
        "_110030",
        "_110031",
        "_110033",
        "_110010",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaTypeCode"

def test_messagetransport_exists():
    # Check that the Enumeration exists
    assert MessageTransport is not None

def test_messagetransport_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageTransport]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageTransport"

def test_communicationtopic_exists():
    # Check that the Enumeration exists
    assert CommunicationTopic is not None

def test_communicationtopic_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommunicationTopic]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommunicationTopic"

def test_examplevisionprescriptionproductcodes_exists():
    # Check that the Enumeration exists
    assert ExampleVisionPrescriptionProductCodes is not None

def test_examplevisionprescriptionproductcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleVisionPrescriptionProductCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleVisionPrescriptionProductCodes"

def test_v20487_exists():
    # Check that the Enumeration exists
    assert V20487 is not None

def test_v20487_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20487]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20487"

def test_exceptioncodes_exists():
    # Check that the Enumeration exists
    assert ExceptionCodes is not None

def test_exceptioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExceptionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExceptionCodes"

def test_snomedctsupplyitem_exists():
    # Check that the Enumeration exists
    assert SnomedctSupplyItem is not None

def test_snomedctsupplyitem_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctSupplyItem]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctSupplyItem"

def test_consentactioncodes_exists():
    # Check that the Enumeration exists
    assert ConsentActionCodes is not None

def test_consentactioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentActionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentActionCodes"

def test_testscriptprofiledestinationtype_exists():
    # Check that the Enumeration exists
    assert TestScriptProfileDestinationType is not None

def test_testscriptprofiledestinationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestScriptProfileDestinationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestScriptProfileDestinationType"

def test_auditeventid_exists():
    # Check that the Enumeration exists
    assert AuditEventId is not None

def test_auditeventid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AuditEventId]
    expected_literals = [
        "_110114",
        "_110101",
        "_110113",
        "_110109",
        "_110106",
        "_110105",
        "_110103",
        "_110110",
        "_110112",
        "_110108",
        "_110100",
        "_110104",
        "_110111",
        "_110107",
        "_110102",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AuditEventId"

def test_observationmethods_exists():
    # Check that the Enumeration exists
    assert ObservationMethods is not None

def test_observationmethods_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObservationMethods]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObservationMethods"

def test_subscriberrelationshipcodes_exists():
    # Check that the Enumeration exists
    assert SubscriberRelationshipCodes is not None

def test_subscriberrelationshipcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubscriberRelationshipCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubscriberRelationshipCodes"

def test_medicationknowledgepackagetypecodes_exists():
    # Check that the Enumeration exists
    assert MedicationKnowledgePackageTypeCodes is not None

def test_medicationknowledgepackagetypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationKnowledgePackageTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationKnowledgePackageTypeCodes"

def test_v3actconsentdirective_exists():
    # Check that the Enumeration exists
    assert V3ActConsentDirective is not None

def test_v3actconsentdirective_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActConsentDirective]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActConsentDirective"

def test_certaintysubcomponentrating_exists():
    # Check that the Enumeration exists
    assert CertaintySubcomponentRating is not None

def test_certaintysubcomponentrating_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CertaintySubcomponentRating]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CertaintySubcomponentRating"

def test_containercap_exists():
    # Check that the Enumeration exists
    assert ContainerCap is not None

def test_containercap_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerCap]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerCap"

def test_clinicalimpressionprognosis_exists():
    # Check that the Enumeration exists
    assert ClinicalImpressionPrognosis is not None

def test_clinicalimpressionprognosis_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ClinicalImpressionPrognosis]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ClinicalImpressionPrognosis"

def test_icd10codes_exists():
    # Check that the Enumeration exists
    assert IcD10Codes is not None

def test_icd10codes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IcD10Codes]
    expected_literals = [
        "_123456",
        "_112233",
        "_123457",
        "_997755",
        "_987654",
        "_321789",
        "_123987",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IcD10Codes"

def test_communicationcategory_exists():
    # Check that the Enumeration exists
    assert CommunicationCategory is not None

def test_communicationcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommunicationCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommunicationCategory"

def test_preparepatient_exists():
    # Check that the Enumeration exists
    assert PreparePatient is not None

def test_preparepatient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PreparePatient]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PreparePatient"

def test_conditionoutcomecodes_exists():
    # Check that the Enumeration exists
    assert ConditionOutcomeCodes is not None

def test_conditionoutcomecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionOutcomeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionOutcomeCodes"

def test_usagecontexttype_exists():
    # Check that the Enumeration exists
    assert UsageContextType is not None

def test_usagecontexttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsageContextType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsageContextType"

def test_contractresourceassettypecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceAssetTypeCodes is not None

def test_contractresourceassettypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceAssetTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceAssetTypeCodes"

def test_dischargedisposition_exists():
    # Check that the Enumeration exists
    assert DischargeDisposition is not None

def test_dischargedisposition_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DischargeDisposition]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DischargeDisposition"

def test_v20092_exists():
    # Check that the Enumeration exists
    assert V20092 is not None

def test_v20092_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20092]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20092"

def test_exampleclaimsubtypecodes_exists():
    # Check that the Enumeration exists
    assert ExampleClaimSubTypeCodes is not None

def test_exampleclaimsubtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleClaimSubTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleClaimSubTypeCodes"

def test_testscriptoperationcode_exists():
    # Check that the Enumeration exists
    assert TestScriptOperationCode is not None

def test_testscriptoperationcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestScriptOperationCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestScriptOperationCode"

def test_identifiertypecodes_exists():
    # Check that the Enumeration exists
    assert IdentifierTypeCodes is not None

def test_identifiertypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IdentifierTypeCodes]
    expected_literals = [
        "ppn",
        "udi",
        "dl",
        "md",
        "sb",
        "plac",
        "tax",
        "mr",
        "prn",
        "fill",
        "jhn",
        "niip",
        "mcn",
        "en",
        "acsn",
        "dr",
        "brn",
        "sno",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IdentifierTypeCodes"

def test_procedurereasoncodes_exists():
    # Check that the Enumeration exists
    assert ProcedureReasonCodes is not None

def test_procedurereasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureReasonCodes"

def test_contractresourcescopecodesa_exists():
    # Check that the Enumeration exists
    assert ContractResourceScopeCodesA is not None

def test_contractresourcescopecodesa_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceScopeCodesA]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceScopeCodesA"

def test_contracttypecodes_exists():
    # Check that the Enumeration exists
    assert ContractTypeCodes is not None

def test_contracttypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractTypeCodes"

def test_effectestimatetype_exists():
    # Check that the Enumeration exists
    assert EffectEstimateType is not None

def test_effectestimatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EffectEstimateType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EffectEstimateType"

def test_locationtype_exists():
    # Check that the Enumeration exists
    assert LocationType is not None

def test_locationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LocationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LocationType"

def test_messageevent_exists():
    # Check that the Enumeration exists
    assert MessageEvent is not None

def test_messageevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageEvent]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageEvent"

def test_organizationaffiliationrole_exists():
    # Check that the Enumeration exists
    assert OrganizationAffiliationRole is not None

def test_organizationaffiliationrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrganizationAffiliationRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrganizationAffiliationRole"

def test_procedurecategorycodessnomedct_exists():
    # Check that the Enumeration exists
    assert ProcedureCategoryCodesSnomedcT is not None

def test_procedurecategorycodessnomedct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureCategoryCodesSnomedcT]
    expected_literals = [
        "_409073007",
        "_103693007",
        "_387713003",
        "_24642003",
        "_409063005",
        "_410606002",
        "_46947000",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureCategoryCodesSnomedcT"

def test_contractresourcepartyrolecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourcePartyRoleCodes is not None

def test_contractresourcepartyrolecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourcePartyRoleCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourcePartyRoleCodes"

def test_v20371_exists():
    # Check that the Enumeration exists
    assert V20371 is not None

def test_v20371_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20371]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20371"

def test_laterality_exists():
    # Check that the Enumeration exists
    assert Laterality is not None

def test_laterality_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Laterality]
    expected_literals = [
        "_419161000",
        "_51440002",
        "_419465000",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Laterality"

def test_contractsubtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractSubtypeCodes is not None

def test_contractsubtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractSubtypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractSubtypeCodes"

def test_researchstudyobjectivetype_exists():
    # Check that the Enumeration exists
    assert ResearchStudyObjectiveType is not None

def test_researchstudyobjectivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResearchStudyObjectiveType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResearchStudyObjectiveType"

def test_patientrelationshiptype_exists():
    # Check that the Enumeration exists
    assert PatientRelationshipType is not None

def test_patientrelationshiptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PatientRelationshipType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PatientRelationshipType"

def test_practicesettingcodevalueset_exists():
    # Check that the Enumeration exists
    assert PracticeSettingCodeValueSet is not None

def test_practicesettingcodevalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PracticeSettingCodeValueSet]
    expected_literals = [
        "_408467006",
        "_408443003",
        "_394612005",
        "_419321007",
        "_419983000",
        "_394587001",
        "_394580004",
        "_419365004",
        "_394589003",
        "_394604002",
        "_420208008",
        "_408455009",
        "_394579002",
        "_422191005",
        "_408460008a",
        "_418652005",
        "_394599008",
        "_408448007",
        "_394812008",
        "_394605001",
        "_394733009",
        "_394810000",
        "_418058008",
        "_418535003",
        "_408470005",
        "_394600006",
        "_394915009",
        "_394592004",
        "_394594003",
        "_408465003",
        "_394802001",
        "_394809005",
        "_394598000",
        "_408454008",
        "_394576009",
        "_394607009",
        "_419772000",
        "_408460008",
        "_394821009",
        "_410005002",
        "_408475000",
        "_394804000",
        "_420112009",
        "_394602003",
        "_418018006",
        "_418862001",
        "_408449004",
        "_394808002",
        "_409967009",
        "_394588006",
        "_421661004",
        "_394593009",
        "_408441001",
        "_394806003",
        "_394608004a",
        "_408472002",
        "_394914008",
        "_419610006",
        "_408450004",
        "_419815003",
        "_394916005",
        "_408480009",
        "_419043006",
        "_408463005",
        "_394801008",
        "_394585009",
        "_418002000",
        "_394583002",
        "_394606000",
        "_408440000",
        "_394601005",
        "_408474001",
        "_394586005",
        "_408446006",
        "_394811001",
        "_408476004",
        "_408471009",
        "_394582007",
        "_394590007",
        "_408444009",
        "_394581000",
        "_394608004",
        "_410001006",
        "_394649004",
        "_409968004",
        "_394611003",
        "_408468001",
        "_394814009",
        "_408459003",
        "_394577000",
        "_419192003",
        "_416304004",
        "_418112009",
        "_408447002",
        "_408464004",
        "_419170002",
        "_394882004",
        "_418960008",
        "_394807007",
        "_394732004",
        "_394539006",
        "_394584008",
        "_394803006",
        "_408477008",
        "_394609007",
        "_419472004",
        "_394610002",
        "_408462000",
        "_408466002",
        "_394597005",
        "_408461007",
        "_394913002",
        "_408478003",
        "_394578005",
        "_394591006",
        "_394813003",
        "_408469009",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PracticeSettingCodeValueSet"

def test_observationreferencerangeappliestocodes_exists():
    # Check that the Enumeration exists
    assert ObservationReferenceRangeAppliesToCodes is not None

def test_observationreferencerangeappliestocodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObservationReferenceRangeAppliesToCodes]
    expected_literals = [
        "_77386006",
        "_248152002",
        "_248153007",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObservationReferenceRangeAppliesToCodes"

def test_communicationnotdonereason_exists():
    # Check that the Enumeration exists
    assert CommunicationNotDoneReason is not None

def test_communicationnotdonereason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommunicationNotDoneReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommunicationNotDoneReason"

def test_mediacollectionviewprojection_exists():
    # Check that the Enumeration exists
    assert MediaCollectionViewProjection is not None

def test_mediacollectionviewprojection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MediaCollectionViewProjection]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MediaCollectionViewProjection"

def test_contractresourceactionstatuscodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceActionStatusCodes is not None

def test_contractresourceactionstatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceActionStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceActionStatusCodes"

def test_v20276_exists():
    # Check that the Enumeration exists
    assert V20276 is not None

def test_v20276_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20276]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20276"

def test_admitsource_exists():
    # Check that the Enumeration exists
    assert AdmitSource is not None

def test_admitsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdmitSource]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdmitSource"

def test_snomedctmedicationcodes_exists():
    # Check that the Enumeration exists
    assert SnomedctMedicationCodes is not None

def test_snomedctmedicationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctMedicationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctMedicationCodes"

def test_contractresourcedefinitionsubtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceDefinitionSubtypeCodes is not None

def test_contractresourcedefinitionsubtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceDefinitionSubtypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceDefinitionSubtypeCodes"

def test_specimencollection_exists():
    # Check that the Enumeration exists
    assert SpecimenCollection is not None

def test_specimencollection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecimenCollection]
    expected_literals = [
        "_386089008",
        "_129304002",
        "_129314006",
        "_225113003",
        "_70777001",
        "_278450005",
        "_129316008",
        "_129323009",
        "_129300006",
        "_73416001",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecimenCollection"

def test_snomedctformcodes_exists():
    # Check that the Enumeration exists
    assert SnomedctFormCodes is not None

def test_snomedctformcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctFormCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctFormCodes"

def test_adverseeventcategory_exists():
    # Check that the Enumeration exists
    assert AdverseEventCategory is not None

def test_adverseeventcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdverseEventCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdverseEventCategory"

def test_paymentstatuscodes_exists():
    # Check that the Enumeration exists
    assert PaymentStatusCodes is not None

def test_paymentstatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PaymentStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PaymentStatusCodes"

def test_contracttermtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractTermTypeCodes is not None

def test_contracttermtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractTermTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractTermTypeCodes"

def test_basicresourcetypes_exists():
    # Check that the Enumeration exists
    assert BasicResourceTypes is not None

def test_basicresourcetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BasicResourceTypes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BasicResourceTypes"

def test_contractresourceassetsubtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceAssetSubTypeCodes is not None

def test_contractresourceassetsubtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceAssetSubTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceAssetSubTypeCodes"

def test_examplediagnosisonadmissioncodes_exists():
    # Check that the Enumeration exists
    assert ExampleDiagnosisOnAdmissionCodes is not None

def test_examplediagnosisonadmissioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleDiagnosisOnAdmissionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleDiagnosisOnAdmissionCodes"

def test_researchstudyphase_exists():
    # Check that the Enumeration exists
    assert ResearchStudyPhase is not None

def test_researchstudyphase_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResearchStudyPhase]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResearchStudyPhase"

def test_specialcourtesy_exists():
    # Check that the Enumeration exists
    assert SpecialCourtesy is not None

def test_specialcourtesy_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecialCourtesy]
    expected_literals = [
        "vip",
        "ext",
        "unk",
        "nrm",
        "stf",
        "prf",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecialCourtesy"

def test_conditionstagetype_exists():
    # Check that the Enumeration exists
    assert ConditionStageType is not None

def test_conditionstagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionStageType]
    expected_literals = [
        "_261023001",
        "_260998006",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionStageType"

def test_contractresourceassetscopecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceAssetScopeCodes is not None

def test_contractresourceassetscopecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceAssetScopeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceAssetScopeCodes"

def test_provenanceparticipantrole_exists():
    # Check that the Enumeration exists
    assert ProvenanceParticipantRole is not None

def test_provenanceparticipantrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProvenanceParticipantRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProvenanceParticipantRole"

def test_researchstudyprimarypurposetype_exists():
    # Check that the Enumeration exists
    assert ResearchStudyPrimaryPurposeType is not None

def test_researchstudyprimarypurposetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ResearchStudyPrimaryPurposeType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ResearchStudyPrimaryPurposeType"

def test_contractresourceassetcontextcodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceAssetContextCodes is not None

def test_contractresourceassetcontextcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceAssetContextCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceAssetContextCodes"

def test_enteralformulatypecodes_exists():
    # Check that the Enumeration exists
    assert EnteralFormulaTypeCodes is not None

def test_enteralformulatypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnteralFormulaTypeCodes]
    expected_literals = [
        "_442921000124101",
        "_443461000124106",
        "_443031000124106",
        "_442951000124105",
        "_441531000124102",
        "_443051000124104",
        "_443771000124106",
        "_441561000124106",
        "_443351000124102",
        "_443421000124100",
        "_443111000124101",
        "_443471000124104",
        "_441601000124106",
        "_441671000124100",
        "_443451000124109",
        "_441571000124104",
        "_442971000124100",
        "_443481000124101",
        "_442651000124102",
        "_443021000124108",
        "_443491000124103",
        "_443411000124108",
        "_442961000124107",
        "_443561000124107",
        "_441591000124103",
        "_444431000124104",
        "_443361000124100",
        "_442981000124102",
        "_442941000124108",
        "_442931000124103",
        "_443401000124105",
        "_443011000124100",
        "_443431000124102",
        "_443501000124106",
        "_442911000124109",
        "_442991000124104",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnteralFormulaTypeCodes"

def test_servicecategory_exists():
    # Check that the Enumeration exists
    assert ServiceCategory is not None

def test_servicecategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceCategory"

def test_participationroletype_exists():
    # Check that the Enumeration exists
    assert ParticipationRoleType is not None

def test_participationroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParticipationRoleType]
    expected_literals = [
        "declassifier",
        "verf",
        "_110152",
        "intprter",
        "grantor",
        "autm",
        "la",
        "excest",
        "hpowatt",
        "_110153",
        "pat",
        "evtwit",
        "invsbj",
        "coauth",
        "consenter",
        "_110150",
        "affl",
        "covpty",
        "delegatee",
        "guadltm",
        "resprsn",
        "spowatt",
        "source",
        "agnt",
        "assigned",
        "not_",
        "grantee",
        "gt",
        "copart",
        "powatt",
        "promsk",
        "depen",
        "aulr",
        "aut",
        "ircp",
        "wit",
        "valid",
        "_110154",
        "primauth",
        "nok",
        "guard",
        "delegator",
        "classifier",
        "amender",
        "conswit",
        "trc",
        "trans",
        "reviewer",
        "inf",
        "auwa",
        "_110155",
        "downgrder",
        "dpowatt",
        "emp",
        "claim",
        "prov",
        "named",
        "cst",
        "econ",
        "cont",
        "ircpa",
        "aucg",
        "_110151",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParticipationRoleType"

def test_objectlifecycleevents_exists():
    # Check that the Enumeration exists
    assert ObjectLifecycleEvents is not None

def test_objectlifecycleevents_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectLifecycleEvents]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectLifecycleEvents"

def test_fhirdocumenttypecodes_exists():
    # Check that the Enumeration exists
    assert FhirDocumentTypeCodes is not None

def test_fhirdocumenttypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FhirDocumentTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FhirDocumentTypeCodes"

def test_contractcontentderivationcodes_exists():
    # Check that the Enumeration exists
    assert ContractContentDerivationCodes is not None

def test_contractcontentderivationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractContentDerivationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractContentDerivationCodes"

def test_diagnosisrole_exists():
    # Check that the Enumeration exists
    assert DiagnosisRole is not None

def test_diagnosisrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DiagnosisRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DiagnosisRole"

def test_contractresourcedecisionmodecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceDecisionModeCodes is not None

def test_contractresourcedecisionmodecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceDecisionModeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceDecisionModeCodes"

def test_contractresourceexpirationtypecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceExpirationTypeCodes is not None

def test_contractresourceexpirationtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceExpirationTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceExpirationTypeCodes"

def test_contextofusevalueset_exists():
    # Check that the Enumeration exists
    assert ContextOfUseValueSet is not None

def test_contextofusevalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContextOfUseValueSet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContextOfUseValueSet"

def test_consentcontentcodes_exists():
    # Check that the Enumeration exists
    assert ConsentContentCodes is not None

def test_consentcontentcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConsentContentCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConsentContentCodes"

def test_riskprobability_exists():
    # Check that the Enumeration exists
    assert RiskProbability is not None

def test_riskprobability_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RiskProbability]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RiskProbability"

def test_v3actpharmacysupplytype_exists():
    # Check that the Enumeration exists
    assert V3ActPharmacySupplyType is not None

def test_v3actpharmacysupplytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActPharmacySupplyType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActPharmacySupplyType"

def test_patientmedicinechangetypes_exists():
    # Check that the Enumeration exists
    assert PatientMedicineChangeTypes is not None

def test_patientmedicinechangetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PatientMedicineChangeTypes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PatientMedicineChangeTypes"

def test_procedureoutcomecodessnomedct_exists():
    # Check that the Enumeration exists
    assert ProcedureOutcomeCodesSnomedcT is not None

def test_procedureoutcomecodessnomedct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedureOutcomeCodesSnomedcT]
    expected_literals = [
        "_385671000",
        "_385669000",
        "_385670004",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedureOutcomeCodesSnomedcT"

def test_specimencontainertype_exists():
    # Check that the Enumeration exists
    assert SpecimenContainerType is not None

def test_specimencontainertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecimenContainerType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecimenContainerType"

def test_examplecoveragefinancialexceptioncodes_exists():
    # Check that the Enumeration exists
    assert ExampleCoverageFinancialExceptionCodes is not None

def test_examplecoveragefinancialexceptioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleCoverageFinancialExceptionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleCoverageFinancialExceptionCodes"

def test_participantroles_exists():
    # Check that the Enumeration exists
    assert ParticipantRoles is not None

def test_participantroles_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParticipantRoles]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParticipantRoles"

def test_observationreferencerangemeaningcodes_exists():
    # Check that the Enumeration exists
    assert ObservationReferenceRangeMeaningCodes is not None

def test_observationreferencerangemeaningcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObservationReferenceRangeMeaningCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObservationReferenceRangeMeaningCodes"

def test_contractactioncodes_exists():
    # Check that the Enumeration exists
    assert ContractActionCodes is not None

def test_contractactioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractActionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractActionCodes"

def test_examplediagnosisrelatedgroupcodes_exists():
    # Check that the Enumeration exists
    assert ExampleDiagnosisRelatedGroupCodes is not None

def test_examplediagnosisrelatedgroupcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleDiagnosisRelatedGroupCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleDiagnosisRelatedGroupCodes"

def test_v3purposeofuse_exists():
    # Check that the Enumeration exists
    assert V3PurposeOfUse is not None

def test_v3purposeofuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3PurposeOfUse]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3PurposeOfUse"

def test_contractresourceassetavailiabilitycodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceAssetAvailiabilityCodes is not None

def test_contractresourceassetavailiabilitycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceAssetAvailiabilityCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceAssetAvailiabilityCodes"

def test_jurisdictionvalueset_exists():
    # Check that the Enumeration exists
    assert JurisdictionValueSet is not None

def test_jurisdictionvalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JurisdictionValueSet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JurisdictionValueSet"

def test_bodystructurelocationqualifier_exists():
    # Check that the Enumeration exists
    assert BodystructureLocationQualifier is not None

def test_bodystructurelocationqualifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BodystructureLocationQualifier]
    expected_literals = [
        "_255551008",
        "_351726001",
        "_419465000",
        "_255561001",
        "_261183002",
        "_264217000",
        "_51440002",
        "_261122009",
        "_352730000",
        "_261089000",
        "_419161000",
        "_49370004",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BodystructureLocationQualifier"

def test_contractresourcedefinitiontypecodes_exists():
    # Check that the Enumeration exists
    assert ContractResourceDefinitionTypeCodes is not None

def test_contractresourcedefinitiontypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractResourceDefinitionTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractResourceDefinitionTypeCodes"

def test_vaccineadministeredvalueset_exists():
    # Check that the Enumeration exists
    assert VaccineAdministeredValueSet is not None

def test_vaccineadministeredvalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VaccineAdministeredValueSet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VaccineAdministeredValueSet"

def test_conditionstage_exists():
    # Check that the Enumeration exists
    assert ConditionStage is not None

def test_conditionstage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionStage]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionStage"

def test_networktypecodes_exists():
    # Check that the Enumeration exists
    assert NetworkTypeCodes is not None

def test_networktypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NetworkTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NetworkTypeCodes"

def test_conditionproblemdiagnosiscodes_exists():
    # Check that the Enumeration exists
    assert ConditionProblemDiagnosisCodes is not None

def test_conditionproblemdiagnosiscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionProblemDiagnosisCodes]
    expected_literals = [
        "_160245001",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionProblemDiagnosisCodes"

def test_verificationresultcommunicationmethod_exists():
    # Check that the Enumeration exists
    assert Verificationresultcommunicationmethod is not None

def test_verificationresultcommunicationmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Verificationresultcommunicationmethod]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Verificationresultcommunicationmethod"

def test_immunizationroutecodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationRouteCodes is not None

def test_immunizationroutecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationRouteCodes]
    expected_literals = [
        "im",
        "sq",
        "trnsderm",
        "idinj",
        "po",
        "ivinj",
        "nasinhlc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationRouteCodes"

def test_designationuse_exists():
    # Check that the Enumeration exists
    assert DesignationUse is not None

def test_designationuse_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DesignationUse]
    expected_literals = [
        "_900000000000003001",
        "_900000000000013009",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DesignationUse"

def test_doseandratetype_exists():
    # Check that the Enumeration exists
    assert DoseAndRateType is not None

def test_doseandratetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DoseAndRateType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DoseAndRateType"

def test_reasonmedicationgivencodes_exists():
    # Check that the Enumeration exists
    assert ReasonMedicationGivenCodes is not None

def test_reasonmedicationgivencodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReasonMedicationGivenCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReasonMedicationGivenCodes"

def test_actionparticipantrole_exists():
    # Check that the Enumeration exists
    assert ActionParticipantRole is not None

def test_actionparticipantrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionParticipantRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionParticipantRole"

def test_fhirdevicetypes_exists():
    # Check that the Enumeration exists
    assert FhirDeviceTypes is not None

def test_fhirdevicetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FhirDeviceTypes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FhirDeviceTypes"

def test_episodeofcaretype_exists():
    # Check that the Enumeration exists
    assert EpisodeOfCareType is not None

def test_episodeofcaretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EpisodeOfCareType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EpisodeOfCareType"

def test_signaturetypecodes_exists():
    # Check that the Enumeration exists
    assert SignatureTypeCodes is not None

def test_signaturetypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SignatureTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SignatureTypeCodes"

def test_adverseeventcausalitymethod_exists():
    # Check that the Enumeration exists
    assert AdverseEventCausalityMethod is not None

def test_adverseeventcausalitymethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdverseEventCausalityMethod]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdverseEventCausalityMethod"

def test_ensembl_exists():
    # Check that the Enumeration exists
    assert Ensembl is not None

def test_ensembl_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Ensembl]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Ensembl"

def test_immunizationrecommendationdatecriterioncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationRecommendationDateCriterionCodes is not None

def test_immunizationrecommendationdatecriterioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationRecommendationDateCriterionCodes]
    expected_literals = [
        "_309807",
        "_309815",
        "_597781",
        "_597773",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationRecommendationDateCriterionCodes"

def test_serviceprovisionconditions_exists():
    # Check that the Enumeration exists
    assert ServiceProvisionConditions is not None

def test_serviceprovisionconditions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceProvisionConditions]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceProvisionConditions"

def test_participanttype_exists():
    # Check that the Enumeration exists
    assert ParticipantType is not None

def test_participanttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParticipantType]
    expected_literals = [
        "pprf",
        "sprf",
        "part",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParticipantType"

def test_measuretype_exists():
    # Check that the Enumeration exists
    assert MeasureType is not None

def test_measuretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasureType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasureType"

def test_detectedissuecategory_exists():
    # Check that the Enumeration exists
    assert DetectedIssueCategory is not None

def test_detectedissuecategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DetectedIssueCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DetectedIssueCategory"

def test_securityroletype_exists():
    # Check that the Enumeration exists
    assert SecurityRoleType is not None

def test_securityroletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SecurityRoleType]
    expected_literals = [
        "hpowatt",
        "amender",
        "emp",
        "dpowatt",
        "_110151",
        "_110152",
        "ircp",
        "covpty",
        "downgrder",
        "affl",
        "_110154",
        "not_",
        "intprter",
        "prov",
        "invsbj",
        "agnt",
        "conswit",
        "consenter",
        "grantor",
        "aut",
        "auwa",
        "la",
        "depen",
        "coauth",
        "pat",
        "wit",
        "ircpa",
        "aucg",
        "classifier",
        "_110155",
        "copart",
        "autm",
        "delegatee",
        "evtwit",
        "assigned",
        "grantee",
        "cont",
        "aulr",
        "delegator",
        "guadltm",
        "guard",
        "reviewer",
        "claim",
        "_110153",
        "econ",
        "source",
        "promsk",
        "cst",
        "trc",
        "inf",
        "_110150",
        "gt",
        "named",
        "spowatt",
        "trans",
        "declassifier",
        "powatt",
        "excest",
        "verf",
        "nok",
        "primauth",
        "resprsn",
        "valid",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SecurityRoleType"

def test_immunizationsubpotentreason_exists():
    # Check that the Enumeration exists
    assert ImmunizationSubpotentReason is not None

def test_immunizationsubpotentreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationSubpotentReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationSubpotentReason"

def test_certaintysubcomponenttype_exists():
    # Check that the Enumeration exists
    assert CertaintySubcomponentType is not None

def test_certaintysubcomponenttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CertaintySubcomponentType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CertaintySubcomponentType"

def test_validationtype_exists():
    # Check that the Enumeration exists
    assert Validationtype is not None

def test_validationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Validationtype]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Validationtype"

def test_immunizationfunctioncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationFunctionCodes is not None

def test_immunizationfunctioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationFunctionCodes]
    expected_literals = [
        "ap",
        "op",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationFunctionCodes"

def test_measurepopulationtype_exists():
    # Check that the Enumeration exists
    assert MeasurePopulationType is not None

def test_measurepopulationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasurePopulationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasurePopulationType"

def test_documentreferenceformatcodeset_exists():
    # Check that the Enumeration exists
    assert DocumentReferenceFormatCodeSet is not None

def test_documentreferenceformatcodeset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocumentReferenceFormatCodeSet]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocumentReferenceFormatCodeSet"

def test_referralmethod_exists():
    # Check that the Enumeration exists
    assert ReferralMethod is not None

def test_referralmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferralMethod]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferralMethod"

def test_immunizationtargetdiseasecodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationTargetDiseaseCodes is not None

def test_immunizationtargetdiseasecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationTargetDiseaseCodes]
    expected_literals = [
        "_36989005",
        "_398102009",
        "_397430003",
        "_1857005",
        "_14189004",
        "_36653000",
        "_709410003",
        "_76902006",
        "_27836007",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationTargetDiseaseCodes"

def test_fhirdevicestatusreason_exists():
    # Check that the Enumeration exists
    assert FhirDeviceStatusReason is not None

def test_fhirdevicestatusreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FhirDeviceStatusReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FhirDeviceStatusReason"

def test_codesforimmunizationsiteofadministration_exists():
    # Check that the Enumeration exists
    assert CodesForImmunizationSiteOfAdministration is not None

def test_codesforimmunizationsiteofadministration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CodesForImmunizationSiteOfAdministration]
    expected_literals = [
        "ra",
        "la",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CodesForImmunizationSiteOfAdministration"

def test_dietcodes_exists():
    # Check that the Enumeration exists
    assert DietCodes is not None

def test_dietcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DietCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DietCodes"

def test_organizationtype_exists():
    # Check that the Enumeration exists
    assert OrganizationType is not None

def test_organizationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OrganizationType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OrganizationType"

def test_immunizationevaluationdosestatusreasoncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationEvaluationDoseStatusReasonCodes is not None

def test_immunizationevaluationdosestatusreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationEvaluationDoseStatusReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationEvaluationDoseStatusReasonCodes"

def test_medicationrequestcourseoftherapycodes_exists():
    # Check that the Enumeration exists
    assert MedicationRequestCourseOfTherapyCodes is not None

def test_medicationrequestcourseoftherapycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationRequestCourseOfTherapyCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationRequestCourseOfTherapyCodes"

def test_formcodes_exists():
    # Check that the Enumeration exists
    assert FormCodes is not None

def test_formcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FormCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FormCodes"

def test_v20916_exists():
    # Check that the Enumeration exists
    assert V20916 is not None

def test_v20916_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20916]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20916"

def test_measurescoring_exists():
    # Check that the Enumeration exists
    assert MeasureScoring is not None

def test_measurescoring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasureScoring]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasureScoring"

def test_pushtypeavailable_exists():
    # Check that the Enumeration exists
    assert Pushtypeavailable is not None

def test_pushtypeavailable_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Pushtypeavailable]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Pushtypeavailable"

def test_practitionerrole_exists():
    # Check that the Enumeration exists
    assert PractitionerRole is not None

def test_practitionerrole_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PractitionerRole]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PractitionerRole"

def test_snomedctadditionaldosageinstructions_exists():
    # Check that the Enumeration exists
    assert SnomedctAdditionalDosageInstructions is not None

def test_snomedctadditionaldosageinstructions_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctAdditionalDosageInstructions]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctAdditionalDosageInstructions"

def test_flagcategory_exists():
    # Check that the Enumeration exists
    assert FlagCategory is not None

def test_flagcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlagCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlagCategory"

def test_benefittypecodes_exists():
    # Check that the Enumeration exists
    assert BenefitTypeCodes is not None

def test_benefittypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BenefitTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BenefitTypeCodes"

def test_medicationrequestcategorycodes_exists():
    # Check that the Enumeration exists
    assert MedicationRequestCategoryCodes is not None

def test_medicationrequestcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationRequestCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationRequestCategoryCodes"

def test_timingabbreviation_exists():
    # Check that the Enumeration exists
    assert TimingAbbreviation is not None

def test_timingabbreviation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimingAbbreviation]
    expected_literals = [
        "tid",
        "q8h",
        "q3h",
        "bid",
        "bed",
        "pm",
        "qod",
        "q6h",
        "wk",
        "q4h",
        "q2h",
        "mo",
        "am",
        "qid",
        "q1h",
        "qd",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimingAbbreviation"

def test_v3substanceadminsubstitutionreason_exists():
    # Check that the Enumeration exists
    assert V3SubstanceAdminSubstitutionReason is not None

def test_v3substanceadminsubstitutionreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3SubstanceAdminSubstitutionReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3SubstanceAdminSubstitutionReason"

def test_v3familymember_exists():
    # Check that the Enumeration exists
    assert V3FamilyMember is not None

def test_v3familymember_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3FamilyMember]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3FamilyMember"

def test_compositemeasurescoring_exists():
    # Check that the Enumeration exists
    assert CompositeMeasureScoring is not None

def test_compositemeasurescoring_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompositeMeasureScoring]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompositeMeasureScoring"

def test_oralsitecodes_exists():
    # Check that the Enumeration exists
    assert OralSiteCodes is not None

def test_oralsitecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OralSiteCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OralSiteCodes"

def test_program_exists():
    # Check that the Enumeration exists
    assert Program is not None

def test_program_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Program]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Program"

def test_immunizationevaluationdosestatuscodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationEvaluationDoseStatusCodes is not None

def test_immunizationevaluationdosestatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationEvaluationDoseStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationEvaluationDoseStatusCodes"

def test_validationprocess_exists():
    # Check that the Enumeration exists
    assert Validationprocess is not None

def test_validationprocess_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Validationprocess]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Validationprocess"

def test_modifiertypecodes_exists():
    # Check that the Enumeration exists
    assert ModifierTypeCodes is not None

def test_modifiertypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModifierTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModifierTypeCodes"

def test_snomedctadministrationmethodcodes_exists():
    # Check that the Enumeration exists
    assert SnomedctAdministrationMethodCodes is not None

def test_snomedctadministrationmethodcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctAdministrationMethodCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctAdministrationMethodCodes"

def test_adjudicationvaluecodes_exists():
    # Check that the Enumeration exists
    assert AdjudicationValueCodes is not None

def test_adjudicationvaluecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdjudicationValueCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdjudicationValueCodes"

def test_goalstartevent_exists():
    # Check that the Enumeration exists
    assert GoalStartEvent is not None

def test_goalstartevent_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoalStartEvent]
    expected_literals = [
        "_32485007",
        "_442137000",
        "_386216000",
        "_308283009",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoalStartEvent"

def test_benefittermcodes_exists():
    # Check that the Enumeration exists
    assert BenefitTermCodes is not None

def test_benefittermcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BenefitTermCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BenefitTermCodes"

def test_fdastandardsequence_exists():
    # Check that the Enumeration exists
    assert FdAStandardSequence is not None

def test_fdastandardsequence_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FdAStandardSequence]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FdAStandardSequence"

def test_questionnairequestioncodes_exists():
    # Check that the Enumeration exists
    assert QuestionnaireQuestionCodes is not None

def test_questionnairequestioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QuestionnaireQuestionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QuestionnaireQuestionCodes"

def test_procedureperformerrolecodes_exists():
    # Check that the Enumeration exists
    assert ProcedurePerformerRoleCodes is not None

def test_procedureperformerrolecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcedurePerformerRoleCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcedurePerformerRoleCodes"

def test_examplepaymenttypecodes_exists():
    # Check that the Enumeration exists
    assert ExamplePaymentTypeCodes is not None

def test_examplepaymenttypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExamplePaymentTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExamplePaymentTypeCodes"

def test_snomedctclinicalfindings_exists():
    # Check that the Enumeration exists
    assert SnomedctClinicalFindings is not None

def test_snomedctclinicalfindings_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctClinicalFindings]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctClinicalFindings"

def test_expressionlanguage_exists():
    # Check that the Enumeration exists
    assert ExpressionLanguage is not None

def test_expressionlanguage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpressionLanguage]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpressionLanguage"

def test_immunizationrecommendationreasoncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationRecommendationReasonCodes is not None

def test_immunizationrecommendationreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationRecommendationReasonCodes]
    expected_literals = [
        "_77386006",
        "_77176002",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationRecommendationReasonCodes"

def test_flagcode_exists():
    # Check that the Enumeration exists
    assert FlagCode is not None

def test_flagcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FlagCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FlagCode"

def test_manifestationandsymptomcodes_exists():
    # Check that the Enumeration exists
    assert ManifestationAndSymptomCodes is not None

def test_manifestationandsymptomcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ManifestationAndSymptomCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ManifestationAndSymptomCodes"

def test_plandefinitiontype_exists():
    # Check that the Enumeration exists
    assert PlanDefinitionType is not None

def test_plandefinitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PlanDefinitionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PlanDefinitionType"

def test_adjudicationreasoncodes_exists():
    # Check that the Enumeration exists
    assert AdjudicationReasonCodes is not None

def test_adjudicationreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdjudicationReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdjudicationReasonCodes"

def test_immunizationrecommendationstatuscodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationRecommendationStatusCodes is not None

def test_immunizationrecommendationstatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationRecommendationStatusCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationRecommendationStatusCodes"

def test_precisionestimatetype_exists():
    # Check that the Enumeration exists
    assert PrecisionEstimateType is not None

def test_precisionestimatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrecisionEstimateType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrecisionEstimateType"

def test_immunizationprogrameligibility_exists():
    # Check that the Enumeration exists
    assert ImmunizationProgramEligibility is not None

def test_immunizationprogrameligibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationProgramEligibility]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationProgramEligibility"

def test_goalpriority_exists():
    # Check that the Enumeration exists
    assert GoalPriority is not None

def test_goalpriority_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoalPriority]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoalPriority"

def test_canpushupdates_exists():
    # Check that the Enumeration exists
    assert Canpushupdates is not None

def test_canpushupdates_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Canpushupdates]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Canpushupdates"

def test_loinccodes_exists():
    # Check that the Enumeration exists
    assert LoincCodes is not None

def test_loinccodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoincCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoincCodes"

def test_fhirspecimencollectionmethod_exists():
    # Check that the Enumeration exists
    assert FhirSpecimenCollectionMethod is not None

def test_fhirspecimencollectionmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FhirSpecimenCollectionMethod]
    expected_literals = [
        "_129300006",
        "_73416001",
        "_129323009",
        "_129314006",
        "_386089008",
        "_129316008",
        "_225113003",
        "_70777001",
        "_129304002",
        "_278450005",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FhirSpecimenCollectionMethod"

def test_snomedctanatomicalstructureforadministrationsitecodes_exists():
    # Check that the Enumeration exists
    assert SnomedctAnatomicalStructureForAdministrationSiteCodes is not None

def test_snomedctanatomicalstructureforadministrationsitecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctAnatomicalStructureForAdministrationSiteCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctAnatomicalStructureForAdministrationSiteCodes"

def test_exampleusecodesforlist_exists():
    # Check that the Enumeration exists
    assert ExampleUseCodesForList is not None

def test_exampleusecodesforlist_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleUseCodesForList]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleUseCodesForList"

def test_primarysourcetype_exists():
    # Check that the Enumeration exists
    assert Primarysourcetype is not None

def test_primarysourcetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Primarysourcetype]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Primarysourcetype"

def test_encountertype_exists():
    # Check that the Enumeration exists
    assert EncounterType is not None

def test_encountertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EncounterType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EncounterType"

def test_operationoutcomecodes_exists():
    # Check that the Enumeration exists
    assert OperationOutcomeCodes is not None

def test_operationoutcomecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperationOutcomeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperationOutcomeCodes"

def test_examplerevenuecentercodes_exists():
    # Check that the Enumeration exists
    assert ExampleRevenueCenterCodes is not None

def test_examplerevenuecentercodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleRevenueCenterCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleRevenueCenterCodes"

def test_chromosomehuman_exists():
    # Check that the Enumeration exists
    assert Chromosomehuman is not None

def test_chromosomehuman_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Chromosomehuman]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Chromosomehuman"

def test_v20493_exists():
    # Check that the Enumeration exists
    assert V20493 is not None

def test_v20493_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V20493]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V20493"

def test_exampleserviceplacecodes_exists():
    # Check that the Enumeration exists
    assert ExampleServicePlaceCodes is not None

def test_exampleserviceplacecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleServicePlaceCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleServicePlaceCodes"

def test_provenancehistoryrecordactivitycodes_exists():
    # Check that the Enumeration exists
    assert ProvenanceHistoryRecordActivityCodes is not None

def test_provenancehistoryrecordactivitycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProvenanceHistoryRecordActivityCodes]
    expected_literals = [
        "create",
        "reactivate",
        "abort",
        "delete",
        "activate",
        "release",
        "nullify",
        "suspend",
        "resume",
        "complete",
        "cancel",
        "hold",
        "update",
        "obsolete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProvenanceHistoryRecordActivityCodes"

def test_medicationadministrationperformerfunctioncodes_exists():
    # Check that the Enumeration exists
    assert MedicationAdministrationPerformerFunctionCodes is not None

def test_medicationadministrationperformerfunctioncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationAdministrationPerformerFunctionCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationAdministrationPerformerFunctionCodes"

def test_immunizationstatusreasoncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationStatusReasonCodes is not None

def test_immunizationstatusreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationStatusReasonCodes]
    expected_literals = [
        "ostock",
        "immune",
        "medprec",
        "patobj",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationStatusReasonCodes"

def test_goalcategory_exists():
    # Check that the Enumeration exists
    assert GoalCategory is not None

def test_goalcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GoalCategory]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GoalCategory"

def test_v3actcode_exists():
    # Check that the Enumeration exists
    assert V3ActCode is not None

def test_v3actcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActCode"

def test_substancecode_exists():
    # Check that the Enumeration exists
    assert SubstanceCode is not None

def test_substancecode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubstanceCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubstanceCode"

def test_catalogtype_exists():
    # Check that the Enumeration exists
    assert CatalogType is not None

def test_catalogtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CatalogType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CatalogType"

def test_conditioncategorycodes_exists():
    # Check that the Enumeration exists
    assert ConditionCategoryCodes is not None

def test_conditioncategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionCategoryCodes"

def test_endpointconnectiontype_exists():
    # Check that the Enumeration exists
    assert EndpointConnectionType is not None

def test_endpointconnectiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EndpointConnectionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EndpointConnectionType"

def test_dataabsentreason_exists():
    # Check that the Enumeration exists
    assert DataAbsentReason is not None

def test_dataabsentreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataAbsentReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataAbsentReason"

def test_patientcontactrelationship_exists():
    # Check that the Enumeration exists
    assert PatientContactRelationship is not None

def test_patientcontactrelationship_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PatientContactRelationship]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PatientContactRelationship"

def test_adverseeventcausalityassessment_exists():
    # Check that the Enumeration exists
    assert AdverseEventCausalityAssessment is not None

def test_adverseeventcausalityassessment_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdverseEventCausalityAssessment]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdverseEventCausalityAssessment"

def test_immunizationfundingsource_exists():
    # Check that the Enumeration exists
    assert ImmunizationFundingSource is not None

def test_immunizationfundingsource_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationFundingSource]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationFundingSource"

def test_immunizationorigincodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationOriginCodes is not None

def test_immunizationorigincodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationOriginCodes]
    expected_literals = [
        "record",
        "recall",
        "school",
        "provider",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationOriginCodes"

def test_allsecuritylabels_exists():
    # Check that the Enumeration exists
    assert AllSecurityLabels is not None

def test_allsecuritylabels_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllSecurityLabels]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllSecurityLabels"

def test_paymenttypecodes_exists():
    # Check that the Enumeration exists
    assert PaymentTypeCodes is not None

def test_paymenttypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PaymentTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PaymentTypeCodes"

def test_conditiondiagnosisseverity_exists():
    # Check that the Enumeration exists
    assert ConditionDiagnosisSeverity is not None

def test_conditiondiagnosisseverity_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConditionDiagnosisSeverity]
    expected_literals = [
        "_255604002",
        "_24484000",
        "_6736007",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConditionDiagnosisSeverity"

def test_medicationadministrationcategorycodes_exists():
    # Check that the Enumeration exists
    assert MedicationAdministrationCategoryCodes is not None

def test_medicationadministrationcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationAdministrationCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationAdministrationCategoryCodes"

def test_actiontype_exists():
    # Check that the Enumeration exists
    assert ActionType is not None

def test_actiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionType"

def test_librarytype_exists():
    # Check that the Enumeration exists
    assert LibraryType is not None

def test_librarytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LibraryType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LibraryType"

def test_immunizationrecommendationtargetdiseasecodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationRecommendationTargetDiseaseCodes is not None

def test_immunizationrecommendationtargetdiseasecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationRecommendationTargetDiseaseCodes]
    expected_literals = [
        "_36653000",
        "_36989005",
        "_76902006",
        "_1857005",
        "_397430003",
        "_709410003",
        "_27836007",
        "_398102009",
        "_14189004",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationRecommendationTargetDiseaseCodes"

def test_texturemodifiedfoodtypecodes_exists():
    # Check that the Enumeration exists
    assert TextureModifiedFoodTypeCodes is not None

def test_texturemodifiedfoodtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextureModifiedFoodTypeCodes]
    expected_literals = [
        "_264331002",
        "_72511004",
        "_227518002",
        "_226760005",
        "_255620007",
        "_226529007",
        "_74242007",
        "_227210005",
        "_28647000",
        "_22836000",
        "_226887002",
        "_102263004",
        "_44027008",
        "_227415002",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextureModifiedFoodTypeCodes"

def test_v3actincidentcode_exists():
    # Check that the Enumeration exists
    assert V3ActIncidentCode is not None

def test_v3actincidentcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActIncidentCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActIncidentCode"

def test_v2036027_exists():
    # Check that the Enumeration exists
    assert V2036027 is not None

def test_v2036027_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V2036027]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V2036027"

def test_studytype_exists():
    # Check that the Enumeration exists
    assert StudyType is not None

def test_studytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StudyType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StudyType"

def test_vitalsigns_exists():
    # Check that the Enumeration exists
    assert VitalSigns is not None

def test_vitalsigns_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VitalSigns]
    expected_literals = [
        "_27086",
        "_84780",
        "_294637",
        "_853531",
        "_92791",
        "_88674",
        "_83105",
        "_84806",
        "_391565",
        "_84624",
        "_98434",
        "_83022",
        "_853549",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VitalSigns"

def test_medicationrequeststatusreasoncodes_exists():
    # Check that the Enumeration exists
    assert MedicationRequestStatusReasonCodes is not None

def test_medicationrequeststatusreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MedicationRequestStatusReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MedicationRequestStatusReasonCodes"

def test_v3actreason_exists():
    # Check that the Enumeration exists
    assert V3ActReason is not None

def test_v3actreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActReason"

def test_texturemodifiercodes_exists():
    # Check that the Enumeration exists
    assert TextureModifierCodes is not None

def test_texturemodifiercodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TextureModifierCodes]
    expected_literals = [
        "_228060008",
        "_228053002",
        "_441761000124103",
        "_228059003",
        "_228049004",
        "_439091000124107",
        "_441881000124103",
        "_228057001",
        "_441791000124106",
        "_228058006",
        "_228056005",
        "_228055009",
        "_441771000124105",
        "_441751000124100",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TextureModifierCodes"

def test_validationstatus_exists():
    # Check that the Enumeration exists
    assert Validationstatus is not None

def test_validationstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Validationstatus]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Validationstatus"

def test_snomedctreasonmedicationnotgivencodes_exists():
    # Check that the Enumeration exists
    assert SnomedctReasonMedicationNotGivenCodes is not None

def test_snomedctreasonmedicationnotgivencodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctReasonMedicationNotGivenCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctReasonMedicationNotGivenCodes"

def test_snomedctmorphologicabnormalities_exists():
    # Check that the Enumeration exists
    assert SnomedctMorphologicAbnormalities is not None

def test_snomedctmorphologicabnormalities_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctMorphologicAbnormalities]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctMorphologicAbnormalities"

def test_substancecategorycodes_exists():
    # Check that the Enumeration exists
    assert SubstanceCategoryCodes is not None

def test_substancecategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubstanceCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubstanceCategoryCodes"

def test_allergyintolerancesubstanceproductconditionandnegationcodes_exists():
    # Check that the Enumeration exists
    assert AllergyIntoleranceSubstanceProductConditionAndNegationCodes is not None

def test_allergyintolerancesubstanceproductconditionandnegationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AllergyIntoleranceSubstanceProductConditionAndNegationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AllergyIntoleranceSubstanceProductConditionAndNegationCodes"

def test_questionnaireanswercodes_exists():
    # Check that the Enumeration exists
    assert QuestionnaireAnswerCodes is not None

def test_questionnaireanswercodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QuestionnaireAnswerCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QuestionnaireAnswerCodes"

def test_devicemetricandcomponenttypes_exists():
    # Check that the Enumeration exists
    assert DeviceMetricAndComponentTypes is not None

def test_devicemetricandcomponenttypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeviceMetricAndComponentTypes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeviceMetricAndComponentTypes"

def test_v3actsubstanceadminsubstitutioncode_exists():
    # Check that the Enumeration exists
    assert V3ActSubstanceAdminSubstitutionCode is not None

def test_v3actsubstanceadminsubstitutioncode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActSubstanceAdminSubstitutionCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActSubstanceAdminSubstitutionCode"

def test_paymentadjustmentreasoncodes_exists():
    # Check that the Enumeration exists
    assert PaymentAdjustmentReasonCodes is not None

def test_paymentadjustmentreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PaymentAdjustmentReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PaymentAdjustmentReasonCodes"

def test_synthesistype_exists():
    # Check that the Enumeration exists
    assert SynthesisType is not None

def test_synthesistype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SynthesisType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SynthesisType"

def test_snomedctroutecodes_exists():
    # Check that the Enumeration exists
    assert SnomedctRouteCodes is not None

def test_snomedctroutecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctRouteCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctRouteCodes"

def test_investigationtype_exists():
    # Check that the Enumeration exists
    assert InvestigationType is not None

def test_investigationtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InvestigationType]
    expected_literals = [
        "_271336007",
        "_160237006",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InvestigationType"

def test_unittypecodes_exists():
    # Check that the Enumeration exists
    assert UnitTypeCodes is not None

def test_unittypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnitTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnitTypeCodes"

def test_snomedctbodystructures_exists():
    # Check that the Enumeration exists
    assert SnomedctBodyStructures is not None

def test_snomedctbodystructures_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctBodyStructures]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctBodyStructures"

def test_exampleproceduretypecodes_exists():
    # Check that the Enumeration exists
    assert ExampleProcedureTypeCodes is not None

def test_exampleproceduretypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleProcedureTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleProcedureTypeCodes"

def test_devicesafety_exists():
    # Check that the Enumeration exists
    assert DeviceSafety is not None

def test_devicesafety_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeviceSafety]
    expected_literals = [
        "c106038",
        "c101673",
        "c113844",
        "c106045",
        "c106047",
        "c106046",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeviceSafety"

def test_nutrientmodifiercodes_exists():
    # Check that the Enumeration exists
    assert NutrientModifierCodes is not None

def test_nutrientmodifiercodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NutrientModifierCodes]
    expected_literals = [
        "_39972003",
        "_33463005",
        "_88480006",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NutrientModifierCodes"

def test_foodtypecodes_exists():
    # Check that the Enumeration exists
    assert FoodTypeCodes is not None

def test_foodtypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FoodTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FoodTypeCodes"

def test_failureaction_exists():
    # Check that the Enumeration exists
    assert Failureaction is not None

def test_failureaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Failureaction]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Failureaction"

def test_immunizationevaluationtargetdiseasecodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationEvaluationTargetDiseaseCodes is not None

def test_immunizationevaluationtargetdiseasecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationEvaluationTargetDiseaseCodes]
    expected_literals = [
        "_709410003",
        "_36653000",
        "_76902006",
        "_398102009",
        "_1857005",
        "_36989005",
        "_14189004",
        "_27836007",
        "_397430003",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationEvaluationTargetDiseaseCodes"

def test_contactentitytype_exists():
    # Check that the Enumeration exists
    assert ContactEntityType is not None

def test_contactentitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContactEntityType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContactEntityType"

def test_contractsignertypecodes_exists():
    # Check that the Enumeration exists
    assert ContractSignerTypeCodes is not None

def test_contractsignertypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContractSignerTypeCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContractSignerTypeCodes"

def test_detectedissuemitigationaction_exists():
    # Check that the Enumeration exists
    assert DetectedIssueMitigationAction is not None

def test_detectedissuemitigationaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DetectedIssueMitigationAction]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DetectedIssueMitigationAction"

def test_documentclassvalueset_exists():
    # Check that the Enumeration exists
    assert DocumentClassValueSet is not None

def test_documentclassvalueset_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocumentClassValueSet]
    expected_literals = [
        "_278952",
        "_264366",
        "_341222",
        "_115436",
        "_114884",
        "_297523",
        "_564476",
        "_297515",
        "_115063",
        "_470427",
        "_264424",
        "_188425",
        "_341404",
        "_286344",
        "_347484",
        "_155085",
        "_278978",
        "_285700",
        "_347757",
        "_535765",
        "_187617",
        "_470393",
        "_341172",
        "_564450",
        "_570168",
        "_297507",
        "_278986",
        "_341214",
        "_114850",
        "_571331",
        "_470468",
        "_114868",
        "_341339",
        "_470492",
        "_286195",
        "_113696",
        "_470450",
        "_187260",
        "_187484",
        "_278960",
        "_264416",
        "_570176",
        "_297499",
        "_115048",
        "_341099",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocumentClassValueSet"

def test_familyhistoryabsentreason_exists():
    # Check that the Enumeration exists
    assert FamilyHistoryAbsentReason is not None

def test_familyhistoryabsentreason_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FamilyHistoryAbsentReason]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FamilyHistoryAbsentReason"

def test_fluidconsistencytypecodes_exists():
    # Check that the Enumeration exists
    assert FluidConsistencyTypeCodes is not None

def test_fluidconsistencytypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FluidConsistencyTypeCodes]
    expected_literals = [
        "_439021000124105",
        "_439081000124109",
        "_439041000124103",
        "_439031000124108",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FluidConsistencyTypeCodes"

def test_servicetype_exists():
    # Check that the Enumeration exists
    assert ServiceType is not None

def test_servicetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ServiceType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ServiceType"

def test_benefitcategorycodes_exists():
    # Check that the Enumeration exists
    assert BenefitCategoryCodes is not None

def test_benefitcategorycodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BenefitCategoryCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BenefitCategoryCodes"

def test_endpointpayloadtype_exists():
    # Check that the Enumeration exists
    assert EndpointPayloadType is not None

def test_endpointpayloadtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EndpointPayloadType]
    expected_literals = [
        "urnihepatapsrcancerendometrium2010",
        "urnihecardimaging2011",
        "urnihepccaps2007",
        "urnihepccnn2007",
        "urnihedentPdf",
        "urnihepharmpadv2010",
        "urnhl7orgsdwgccdanonXmlBody11",
        "urnihepccedpn2007",
        "urnihepcccm2008",
        "urnihepccmds2009",
        "urnihepatapsrcancerall2010",
        "urnihepccppvs2010",
        "urnihepccic2009",
        "urnihepcctrs2011",
        "urnihelabxdlab2008",
        "urnihepccirc2008",
        "urnihecardCrC2012",
        "urnihepatapsrcancersalivaryGland2010",
        "urnihepatapsrcancerprostate2010",
        "urnihepatapsrcancerliver2010",
        "urnihepatapsrcancerkidney2010",
        "urnihepccets2011",
        "urnihepatapsrcancercervix2010",
        "urnihecardEprCIE2014",
        "urnihepccxphr2007A",
        "urnihepatapsrcanceresophagus2010",
        "urnihepccedr2007",
        "urnihepatapsrcancerthyroid2010",
        "urniheradPdf",
        "urnihepatapsrcancertestis2010",
        "urnihepharmpml2013",
        "urnhl7orgsdwgccdastructuredBody11",
        "urniheitixdw2011workflowDoc",
        "urnihepatapsrcancercolon2010",
        "urnihedentText",
        "urnihepccxphr2007",
        "urnihepharmdis2010",
        "urnihepatapsrcancerbreast2010",
        "urniheitidsgenveloping2014",
        "urnihepatapsrall2010",
        "urnihepccxdsms2007",
        "urnihepatapsrcancerlipOralCavity2010",
        "urnihepccits2011",
        "urnihepatapsrcancerstomach2010",
        "urniheitixdssdpdf2008",
        "urnihepcclds2009",
        "urnihepccnds2010",
        "urnihepccldhp2009",
        "urnihepatapsrcancerpharynx2010",
        "urniheradText",
        "urnihepccaprhandp2008",
        "urnihepatapsrcancerlung2010",
        "urnihepcccrc2008",
        "urnihepatapsrcancerpancreas2010",
        "urnihepatapsrcancerlarynx2010",
        "urnihepccaprlab2008",
        "urnihepccapredu2008",
        "urniheitibppc2007",
        "urniheitixdssdtext2008",
        "urnihepatapsrcancerskin2010",
        "urnihepccctn2007",
        "urnihepatapsrcancerurinaryBladder2010",
        "urnihepcchp2008",
        "urnihepatapsrcancerovary2010",
        "urnihepcctn2007",
        "urnihepcchandp2008",
        "urnihedentCdAImagingReportStructuredHeadings2013",
        "urnihepharmpre2010",
        "urniheradCdAImagingReportStructuredHeadings2013",
        "urnihepccedes2007",
        "urniheitibppcsd2007",
        "urniheitidsgdetached2014",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EndpointPayloadType"

def test_qualityofevidencerating_exists():
    # Check that the Enumeration exists
    assert QualityOfEvidenceRating is not None

def test_qualityofevidencerating_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QualityOfEvidenceRating]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QualityOfEvidenceRating"

def test_definitiontopic_exists():
    # Check that the Enumeration exists
    assert DefinitionTopic is not None

def test_definitiontopic_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefinitionTopic]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefinitionTopic"

def test_icd10procedurecodes_exists():
    # Check that the Enumeration exists
    assert IcD10ProcedureCodes is not None

def test_icd10procedurecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IcD10ProcedureCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IcD10ProcedureCodes"

def test_devicetype_exists():
    # Check that the Enumeration exists
    assert DeviceType is not None

def test_devicetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeviceType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeviceType"

def test_usclscodes_exists():
    # Check that the Enumeration exists
    assert UsclsCodes is not None

def test_usclscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UsclsCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UsclsCodes"

def test_specimenprocessingprocedure_exists():
    # Check that the Enumeration exists
    assert SpecimenProcessingProcedure is not None

def test_specimenprocessingprocedure_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SpecimenProcessingProcedure]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SpecimenProcessingProcedure"

def test_surfacecodes_exists():
    # Check that the Enumeration exists
    assert SurfaceCodes is not None

def test_surfacecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SurfaceCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SurfaceCodes"

def test_measuredatausage_exists():
    # Check that the Enumeration exists
    assert MeasureDataUsage is not None

def test_measuredatausage_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MeasureDataUsage]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MeasureDataUsage"

def test_riskestimatetype_exists():
    # Check that the Enumeration exists
    assert RiskEstimateType is not None

def test_riskestimatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RiskEstimateType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RiskEstimateType"

def test_v3actencountercode_exists():
    # Check that the Enumeration exists
    assert V3ActEncounterCode is not None

def test_v3actencountercode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActEncounterCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActEncounterCode"

def test_adjudicationerrorcodes_exists():
    # Check that the Enumeration exists
    assert AdjudicationErrorCodes is not None

def test_adjudicationerrorcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdjudicationErrorCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdjudicationErrorCodes"

def test_snomedctmedicationasneededreasoncodes_exists():
    # Check that the Enumeration exists
    assert SnomedctMedicationAsNeededReasonCodes is not None

def test_snomedctmedicationasneededreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SnomedctMedicationAsNeededReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SnomedctMedicationAsNeededReasonCodes"

def test_immunizationreasoncodes_exists():
    # Check that the Enumeration exists
    assert ImmunizationReasonCodes is not None

def test_immunizationreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ImmunizationReasonCodes]
    expected_literals = [
        "_429060002",
        "_281657000",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ImmunizationReasonCodes"

def test_taskcode_exists():
    # Check that the Enumeration exists
    assert TaskCode is not None

def test_taskcode_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TaskCode]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TaskCode"

def test_commontags_exists():
    # Check that the Enumeration exists
    assert CommonTags is not None

def test_commontags_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommonTags]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommonTags"

def test_maritalstatuscodes_exists():
    # Check that the Enumeration exists
    assert MaritalStatusCodes is not None

def test_maritalstatuscodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MaritalStatusCodes]
    expected_literals = [
        "unk",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MaritalStatusCodes"

def test_commonlanguages_exists():
    # Check that the Enumeration exists
    assert CommonLanguages is not None

def test_commonlanguages_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CommonLanguages]
    expected_literals = [
        "fr",
        "da",
        "zhSg",
        "cs",
        "no",
        "nlBe",
        "enGb",
        "frCh",
        "enAu",
        "ruRu",
        "deDe",
        "sr",
        "zh",
        "es",
        "hr",
        "sv",
        "esAr",
        "itIt",
        "pl",
        "en",
        "hi",
        "pa",
        "enSg",
        "ja",
        "zhTw",
        "noNo",
        "enUs",
        "fyNl",
        "srRs",
        "de",
        "bn",
        "zhHk",
        "enNz",
        "frFr",
        "fi",
        "ptBr",
        "el",
        "enIn",
        "nl",
        "deAt",
        "fy",
        "esUy",
        "ru",
        "ko",
        "deCh",
        "zhCn",
        "pt",
        "esEs",
        "itCh",
        "nlNl",
        "ar",
        "te",
        "enCa",
        "svSe",
        "it",
        "frBe",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CommonLanguages"

def test_adverseeventseriousness_exists():
    # Check that the Enumeration exists
    assert AdverseEventSeriousness is not None

def test_adverseeventseriousness_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdverseEventSeriousness]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdverseEventSeriousness"

def test_subjecttype_exists():
    # Check that the Enumeration exists
    assert SubjectType is not None

def test_subjecttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SubjectType]
    expected_literals = [
        "location",
        "device",
        "patient",
        "practitioner",
        "organization",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SubjectType"

def test_observationinterpretationcodes_exists():
    # Check that the Enumeration exists
    assert ObservationInterpretationCodes is not None

def test_observationinterpretationcodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObservationInterpretationCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObservationInterpretationCodes"

def test_exampleprogramreasoncodes_exists():
    # Check that the Enumeration exists
    assert ExampleProgramReasonCodes is not None

def test_exampleprogramreasoncodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExampleProgramReasonCodes]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExampleProgramReasonCodes"

def test_fdamethod_exists():
    # Check that the Enumeration exists
    assert FdAMethod is not None

def test_fdamethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FdAMethod]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FdAMethod"

def test_v3actpriority_exists():
    # Check that the Enumeration exists
    assert V3ActPriority is not None

def test_v3actpriority_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in V3ActPriority]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in V3ActPriority"

def test_need_exists():
    # Check that the Enumeration exists
    assert Need is not None

def test_need_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Need]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Need"


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
