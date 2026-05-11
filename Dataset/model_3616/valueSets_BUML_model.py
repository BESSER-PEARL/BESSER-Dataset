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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="address"),
			EnumerationLiteral(name="age"),
			EnumerationLiteral(name="identifier"),
			EnumerationLiteral(name="marketingStatus"),
			EnumerationLiteral(name="meta"),
			EnumerationLiteral(name="money"),
			EnumerationLiteral(name="moneyQuantity"),
			EnumerationLiteral(name="annotation"),
			EnumerationLiteral(name="attachment"),
			EnumerationLiteral(name="backboneElement"),
			EnumerationLiteral(name="codeableConcept"),
			EnumerationLiteral(name="coding"),
			EnumerationLiteral(name="contactDetail"),
			EnumerationLiteral(name="contactPoint"),
			EnumerationLiteral(name="contributor"),
			EnumerationLiteral(name="count"),
			EnumerationLiteral(name="dataRequirement"),
			EnumerationLiteral(name="distance"),
			EnumerationLiteral(name="dosage"),
			EnumerationLiteral(name="duration"),
			EnumerationLiteral(name="element"),
			EnumerationLiteral(name="elementDefinition"),
			EnumerationLiteral(name="expression"),
			EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="humanName"),
			EnumerationLiteral(name="base64Binary"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="canonical"),
			EnumerationLiteral(name="code"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="dateTime"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="id"),
			EnumerationLiteral(name="instant"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="markdown"),
			EnumerationLiteral(name="narrative"),
			EnumerationLiteral(name="parameterDefinition"),
			EnumerationLiteral(name="period"),
			EnumerationLiteral(name="population"),
			EnumerationLiteral(name="prodCharacteristic"),
			EnumerationLiteral(name="productShelfLife"),
			EnumerationLiteral(name="quantity"),
			EnumerationLiteral(name="range"),
			EnumerationLiteral(name="ratio"),
			EnumerationLiteral(name="reference"),
			EnumerationLiteral(name="relatedArtifact"),
			EnumerationLiteral(name="sampledData"),
			EnumerationLiteral(name="signature"),
			EnumerationLiteral(name="simpleQuantity"),
			EnumerationLiteral(name="substanceAmount"),
			EnumerationLiteral(name="timing"),
			EnumerationLiteral(name="triggerDefinition"),
			EnumerationLiteral(name="usageContext"),
			EnumerationLiteral(name="oid"),
			EnumerationLiteral(name="positiveInt"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="unsignedInt"),
			EnumerationLiteral(name="uri"),
			EnumerationLiteral(name="url"),
			EnumerationLiteral(name="uuid"),
			EnumerationLiteral(name="xhtml")
    }
)

ResourceType: Enumeration = Enumeration(
    name="ResourceType",
    literals={
            EnumerationLiteral(name="careTeam"),
			EnumerationLiteral(name="catalogEntry"),
			EnumerationLiteral(name="account"),
			EnumerationLiteral(name="activityDefinition"),
			EnumerationLiteral(name="adverseEvent"),
			EnumerationLiteral(name="allergyIntolerance"),
			EnumerationLiteral(name="appointment"),
			EnumerationLiteral(name="appointmentResponse"),
			EnumerationLiteral(name="auditEvent"),
			EnumerationLiteral(name="basic"),
			EnumerationLiteral(name="binary"),
			EnumerationLiteral(name="biologicallyDerivedProduct"),
			EnumerationLiteral(name="bodyStructure"),
			EnumerationLiteral(name="bundle"),
			EnumerationLiteral(name="documentManifest"),
			EnumerationLiteral(name="capabilityStatement"),
			EnumerationLiteral(name="documentReference"),
			EnumerationLiteral(name="chargeItem"),
			EnumerationLiteral(name="chargeItemDefinition"),
			EnumerationLiteral(name="carePlan"),
			EnumerationLiteral(name="claim"),
			EnumerationLiteral(name="claimResponse"),
			EnumerationLiteral(name="clinicalImpression"),
			EnumerationLiteral(name="codeSystem"),
			EnumerationLiteral(name="communication"),
			EnumerationLiteral(name="communicationRequest"),
			EnumerationLiteral(name="compartmentDefinition"),
			EnumerationLiteral(name="composition"),
			EnumerationLiteral(name="conceptMap"),
			EnumerationLiteral(name="condition"),
			EnumerationLiteral(name="consent"),
			EnumerationLiteral(name="contract"),
			EnumerationLiteral(name="coverage"),
			EnumerationLiteral(name="coverageEligibilityRequest"),
			EnumerationLiteral(name="coverageEligibilityResponse"),
			EnumerationLiteral(name="detectedIssue"),
			EnumerationLiteral(name="device"),
			EnumerationLiteral(name="deviceDefinition"),
			EnumerationLiteral(name="deviceMetric"),
			EnumerationLiteral(name="deviceRequest"),
			EnumerationLiteral(name="deviceUseStatement"),
			EnumerationLiteral(name="diagnosticReport"),
			EnumerationLiteral(name="immunization"),
			EnumerationLiteral(name="domainResource"),
			EnumerationLiteral(name="effectEvidenceSynthesis"),
			EnumerationLiteral(name="encounter"),
			EnumerationLiteral(name="endpoint"),
			EnumerationLiteral(name="enrollmentRequest"),
			EnumerationLiteral(name="enrollmentResponse"),
			EnumerationLiteral(name="episodeOfCare"),
			EnumerationLiteral(name="eventDefinition"),
			EnumerationLiteral(name="evidence"),
			EnumerationLiteral(name="evidenceVariable"),
			EnumerationLiteral(name="exampleScenario"),
			EnumerationLiteral(name="explanationOfBenefit"),
			EnumerationLiteral(name="familyMemberHistory"),
			EnumerationLiteral(name="flag"),
			EnumerationLiteral(name="goal"),
			EnumerationLiteral(name="graphDefinition"),
			EnumerationLiteral(name="group"),
			EnumerationLiteral(name="guidanceResponse"),
			EnumerationLiteral(name="healthcareService"),
			EnumerationLiteral(name="imagingStudy"),
			EnumerationLiteral(name="medicinalProductContraindication"),
			EnumerationLiteral(name="immunizationEvaluation"),
			EnumerationLiteral(name="immunizationRecommendation"),
			EnumerationLiteral(name="implementationGuide"),
			EnumerationLiteral(name="insurancePlan"),
			EnumerationLiteral(name="invoice"),
			EnumerationLiteral(name="library"),
			EnumerationLiteral(name="linkage"),
			EnumerationLiteral(name="list"),
			EnumerationLiteral(name="location"),
			EnumerationLiteral(name="measure"),
			EnumerationLiteral(name="measureReport"),
			EnumerationLiteral(name="media"),
			EnumerationLiteral(name="medication"),
			EnumerationLiteral(name="medicationAdministration"),
			EnumerationLiteral(name="medicationDispense"),
			EnumerationLiteral(name="medicationKnowledge"),
			EnumerationLiteral(name="medicationRequest"),
			EnumerationLiteral(name="medicationStatement"),
			EnumerationLiteral(name="medicinalProduct"),
			EnumerationLiteral(name="medicinalProductAuthorization"),
			EnumerationLiteral(name="paymentReconciliation"),
			EnumerationLiteral(name="person"),
			EnumerationLiteral(name="medicinalProductIndication"),
			EnumerationLiteral(name="medicinalProductIngredient"),
			EnumerationLiteral(name="medicinalProductInteraction"),
			EnumerationLiteral(name="medicinalProductManufactured"),
			EnumerationLiteral(name="medicinalProductPackaged"),
			EnumerationLiteral(name="medicinalProductPharmaceutical"),
			EnumerationLiteral(name="medicinalProductUndesirableEffect"),
			EnumerationLiteral(name="messageDefinition"),
			EnumerationLiteral(name="messageHeader"),
			EnumerationLiteral(name="molecularSequence"),
			EnumerationLiteral(name="namingSystem"),
			EnumerationLiteral(name="nutritionOrder"),
			EnumerationLiteral(name="observation"),
			EnumerationLiteral(name="observationDefinition"),
			EnumerationLiteral(name="operationDefinition"),
			EnumerationLiteral(name="operationOutcome"),
			EnumerationLiteral(name="organization"),
			EnumerationLiteral(name="organizationAffiliation"),
			EnumerationLiteral(name="parameters"),
			EnumerationLiteral(name="patient"),
			EnumerationLiteral(name="paymentNotice"),
			EnumerationLiteral(name="structureDefinition"),
			EnumerationLiteral(name="planDefinition"),
			EnumerationLiteral(name="practitioner"),
			EnumerationLiteral(name="practitionerRole"),
			EnumerationLiteral(name="procedure"),
			EnumerationLiteral(name="provenance"),
			EnumerationLiteral(name="questionnaire"),
			EnumerationLiteral(name="questionnaireResponse"),
			EnumerationLiteral(name="relatedPerson"),
			EnumerationLiteral(name="requestGroup"),
			EnumerationLiteral(name="researchDefinition"),
			EnumerationLiteral(name="researchElementDefinition"),
			EnumerationLiteral(name="researchStudy"),
			EnumerationLiteral(name="researchSubject"),
			EnumerationLiteral(name="resource"),
			EnumerationLiteral(name="riskAssessment"),
			EnumerationLiteral(name="riskEvidenceSynthesis"),
			EnumerationLiteral(name="schedule"),
			EnumerationLiteral(name="searchParameter"),
			EnumerationLiteral(name="serviceRequest"),
			EnumerationLiteral(name="slot"),
			EnumerationLiteral(name="specimen"),
			EnumerationLiteral(name="specimenDefinition"),
			EnumerationLiteral(name="structureMap"),
			EnumerationLiteral(name="subscription"),
			EnumerationLiteral(name="substance"),
			EnumerationLiteral(name="substanceNucleicAcid"),
			EnumerationLiteral(name="substancePolymer"),
			EnumerationLiteral(name="substanceProtein"),
			EnumerationLiteral(name="substanceReferenceInformation"),
			EnumerationLiteral(name="substanceSourceMaterial"),
			EnumerationLiteral(name="substanceSpecification"),
			EnumerationLiteral(name="supplyDelivery"),
			EnumerationLiteral(name="supplyRequest"),
			EnumerationLiteral(name="task"),
			EnumerationLiteral(name="terminologyCapabilities"),
			EnumerationLiteral(name="testReport"),
			EnumerationLiteral(name="testScript"),
			EnumerationLiteral(name="valueSet"),
			EnumerationLiteral(name="verificationResult"),
			EnumerationLiteral(name="visionPrescription")
    }
)

IdentifierTypeCodes: Enumeration = Enumeration(
    name="IdentifierTypeCodes",
    literals={
            EnumerationLiteral(name="mr"),
			EnumerationLiteral(name="mcn"),
			EnumerationLiteral(name="dl"),
			EnumerationLiteral(name="ppn"),
			EnumerationLiteral(name="brn"),
			EnumerationLiteral(name="en"),
			EnumerationLiteral(name="tax"),
			EnumerationLiteral(name="niip"),
			EnumerationLiteral(name="prn"),
			EnumerationLiteral(name="md"),
			EnumerationLiteral(name="dr"),
			EnumerationLiteral(name="acsn"),
			EnumerationLiteral(name="udi"),
			EnumerationLiteral(name="sno"),
			EnumerationLiteral(name="sb"),
			EnumerationLiteral(name="plac"),
			EnumerationLiteral(name="fill"),
			EnumerationLiteral(name="jhn")
    }
)

UsageContextType: Enumeration = Enumeration(
    name="UsageContextType",
    literals={
            
    }
)

ContextOfUseValueSet: Enumeration = Enumeration(
    name="ContextOfUseValueSet",
    literals={
            
    }
)

JurisdictionValueSet: Enumeration = Enumeration(
    name="JurisdictionValueSet",
    literals={
            
    }
)

DefinitionUseCodes: Enumeration = Enumeration(
    name="DefinitionUseCodes",
    literals={
            
    }
)

FhirDefinedType: Enumeration = Enumeration(
    name="FhirDefinedType",
    literals={
            
    }
)

LoincCodes: Enumeration = Enumeration(
    name="LoincCodes",
    literals={
            
    }
)

CommonLanguages: Enumeration = Enumeration(
    name="CommonLanguages",
    literals={
            EnumerationLiteral(name="de"),
			EnumerationLiteral(name="deAt"),
			EnumerationLiteral(name="deCh"),
			EnumerationLiteral(name="ar"),
			EnumerationLiteral(name="bn"),
			EnumerationLiteral(name="cs"),
			EnumerationLiteral(name="da"),
			EnumerationLiteral(name="noNo"),
			EnumerationLiteral(name="pa"),
			EnumerationLiteral(name="pl"),
			EnumerationLiteral(name="deDe"),
			EnumerationLiteral(name="el"),
			EnumerationLiteral(name="en"),
			EnumerationLiteral(name="enAu"),
			EnumerationLiteral(name="enCa"),
			EnumerationLiteral(name="enGb"),
			EnumerationLiteral(name="enIn"),
			EnumerationLiteral(name="enNz"),
			EnumerationLiteral(name="enSg"),
			EnumerationLiteral(name="enUs"),
			EnumerationLiteral(name="es"),
			EnumerationLiteral(name="esAr"),
			EnumerationLiteral(name="esEs"),
			EnumerationLiteral(name="esUy"),
			EnumerationLiteral(name="fi"),
			EnumerationLiteral(name="fr"),
			EnumerationLiteral(name="frBe"),
			EnumerationLiteral(name="frCh"),
			EnumerationLiteral(name="frFr"),
			EnumerationLiteral(name="fy"),
			EnumerationLiteral(name="fyNl"),
			EnumerationLiteral(name="hi"),
			EnumerationLiteral(name="hr"),
			EnumerationLiteral(name="it"),
			EnumerationLiteral(name="itCh"),
			EnumerationLiteral(name="itIt"),
			EnumerationLiteral(name="ja"),
			EnumerationLiteral(name="ko"),
			EnumerationLiteral(name="nl"),
			EnumerationLiteral(name="nlBe"),
			EnumerationLiteral(name="nlNl"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="pt"),
			EnumerationLiteral(name="ptBr"),
			EnumerationLiteral(name="ru"),
			EnumerationLiteral(name="ruRu"),
			EnumerationLiteral(name="sr"),
			EnumerationLiteral(name="srRs"),
			EnumerationLiteral(name="sv"),
			EnumerationLiteral(name="svSe"),
			EnumerationLiteral(name="te"),
			EnumerationLiteral(name="zh"),
			EnumerationLiteral(name="zhCn"),
			EnumerationLiteral(name="zhHk"),
			EnumerationLiteral(name="zhSg"),
			EnumerationLiteral(name="zhTw")
    }
)

SignatureTypeCodes: Enumeration = Enumeration(
    name="SignatureTypeCodes",
    literals={
            
    }
)

V2036027: Enumeration = Enumeration(
    name="V2036027",
    literals={
            
    }
)

TimingAbbreviation: Enumeration = Enumeration(
    name="TimingAbbreviation",
    literals={
            EnumerationLiteral(name="q6h"),
			EnumerationLiteral(name="q8h"),
			EnumerationLiteral(name="bid"),
			EnumerationLiteral(name="tid"),
			EnumerationLiteral(name="qid"),
			EnumerationLiteral(name="am"),
			EnumerationLiteral(name="pm"),
			EnumerationLiteral(name="qd"),
			EnumerationLiteral(name="qod"),
			EnumerationLiteral(name="q1h"),
			EnumerationLiteral(name="q2h"),
			EnumerationLiteral(name="q3h"),
			EnumerationLiteral(name="q4h"),
			EnumerationLiteral(name="bed"),
			EnumerationLiteral(name="wk"),
			EnumerationLiteral(name="mo")
    }
)

SubjectType: Enumeration = Enumeration(
    name="SubjectType",
    literals={
            EnumerationLiteral(name="patient"),
			EnumerationLiteral(name="practitioner"),
			EnumerationLiteral(name="organization"),
			EnumerationLiteral(name="location"),
			EnumerationLiteral(name="device")
    }
)

DesignationUse: Enumeration = Enumeration(
    name="DesignationUse",
    literals={
            EnumerationLiteral(name="_900000000000003001"),
			EnumerationLiteral(name="_900000000000013009")
    }
)

ExpressionLanguage: Enumeration = Enumeration(
    name="ExpressionLanguage",
    literals={
            
    }
)

SnomedctAdditionalDosageInstructions: Enumeration = Enumeration(
    name="SnomedctAdditionalDosageInstructions",
    literals={
            
    }
)

SnomedctMedicationAsNeededReasonCodes: Enumeration = Enumeration(
    name="SnomedctMedicationAsNeededReasonCodes",
    literals={
            
    }
)

SnomedctAnatomicalStructureForAdministrationSiteCodes: Enumeration = Enumeration(
    name="SnomedctAnatomicalStructureForAdministrationSiteCodes",
    literals={
            
    }
)

SnomedctRouteCodes: Enumeration = Enumeration(
    name="SnomedctRouteCodes",
    literals={
            
    }
)

SnomedctAdministrationMethodCodes: Enumeration = Enumeration(
    name="SnomedctAdministrationMethodCodes",
    literals={
            
    }
)

DoseAndRateType: Enumeration = Enumeration(
    name="DoseAndRateType",
    literals={
            
    }
)

AllSecurityLabels: Enumeration = Enumeration(
    name="AllSecurityLabels",
    literals={
            
    }
)

CommonTags: Enumeration = Enumeration(
    name="CommonTags",
    literals={
            
    }
)

OrganizationType: Enumeration = Enumeration(
    name="OrganizationType",
    literals={
            
    }
)

ContactEntityType: Enumeration = Enumeration(
    name="ContactEntityType",
    literals={
            
    }
)

EndpointConnectionType: Enumeration = Enumeration(
    name="EndpointConnectionType",
    literals={
            
    }
)

EndpointPayloadType: Enumeration = Enumeration(
    name="EndpointPayloadType",
    literals={
            EnumerationLiteral(name="urnihepccedes2007"),
			EnumerationLiteral(name="urnihepccaprhandp2008"),
			EnumerationLiteral(name="urnihepcchandp2008"),
			EnumerationLiteral(name="urnihepccxphr2007A"),
			EnumerationLiteral(name="urnihepccaps2007"),
			EnumerationLiteral(name="urnihepccxdsms2007"),
			EnumerationLiteral(name="urnihepccxphr2007"),
			EnumerationLiteral(name="urnihepccedr2007"),
			EnumerationLiteral(name="urniheitidsgenveloping2014"),
			EnumerationLiteral(name="urnihepccaprlab2008"),
			EnumerationLiteral(name="urnihepccapredu2008"),
			EnumerationLiteral(name="urnihepccirc2008"),
			EnumerationLiteral(name="urnihepcccrc2008"),
			EnumerationLiteral(name="urnihepcccm2008"),
			EnumerationLiteral(name="urnihepccic2009"),
			EnumerationLiteral(name="urnihepcctn2007"),
			EnumerationLiteral(name="urnihepccnn2007"),
			EnumerationLiteral(name="urnihepccctn2007"),
			EnumerationLiteral(name="urnihepccedpn2007"),
			EnumerationLiteral(name="urnihepcchp2008"),
			EnumerationLiteral(name="urnihepccldhp2009"),
			EnumerationLiteral(name="urnihepcclds2009"),
			EnumerationLiteral(name="urnihepccmds2009"),
			EnumerationLiteral(name="urnihepccnds2010"),
			EnumerationLiteral(name="urnihepccppvs2010"),
			EnumerationLiteral(name="urnihepcctrs2011"),
			EnumerationLiteral(name="urnihepccets2011"),
			EnumerationLiteral(name="urnihepccits2011"),
			EnumerationLiteral(name="urniheitibppc2007"),
			EnumerationLiteral(name="urniheitibppcsd2007"),
			EnumerationLiteral(name="urniheitixdw2011workflowDoc"),
			EnumerationLiteral(name="urniheitidsgdetached2014"),
			EnumerationLiteral(name="urnihepatapsrcancerstomach2010"),
			EnumerationLiteral(name="urnihepatapsrcancerliver2010"),
			EnumerationLiteral(name="urniheitixdssdpdf2008"),
			EnumerationLiteral(name="urniheitixdssdtext2008"),
			EnumerationLiteral(name="urnihelabxdlab2008"),
			EnumerationLiteral(name="urniheradText"),
			EnumerationLiteral(name="urniheradPdf"),
			EnumerationLiteral(name="urniheradCdAImagingReportStructuredHeadings2013"),
			EnumerationLiteral(name="urnihecardimaging2011"),
			EnumerationLiteral(name="urnihecardCrC2012"),
			EnumerationLiteral(name="urnihecardEprCIE2014"),
			EnumerationLiteral(name="urnihedentText"),
			EnumerationLiteral(name="urnihedentPdf"),
			EnumerationLiteral(name="urnihedentCdAImagingReportStructuredHeadings2013"),
			EnumerationLiteral(name="urnihepatapsrall2010"),
			EnumerationLiteral(name="urnihepatapsrcancerall2010"),
			EnumerationLiteral(name="urnihepatapsrcancerbreast2010"),
			EnumerationLiteral(name="urnihepatapsrcancercolon2010"),
			EnumerationLiteral(name="urnihepatapsrcancerprostate2010"),
			EnumerationLiteral(name="urnihepatapsrcancerthyroid2010"),
			EnumerationLiteral(name="urnihepatapsrcancerlung2010"),
			EnumerationLiteral(name="urnihepatapsrcancerskin2010"),
			EnumerationLiteral(name="urnihepatapsrcancerkidney2010"),
			EnumerationLiteral(name="urnihepatapsrcancercervix2010"),
			EnumerationLiteral(name="urnihepatapsrcancerendometrium2010"),
			EnumerationLiteral(name="urnihepatapsrcancerovary2010"),
			EnumerationLiteral(name="urnihepatapsrcanceresophagus2010"),
			EnumerationLiteral(name="urnihepatapsrcancerpancreas2010"),
			EnumerationLiteral(name="urnihepatapsrcancertestis2010"),
			EnumerationLiteral(name="urnihepatapsrcancerurinaryBladder2010"),
			EnumerationLiteral(name="urnihepatapsrcancerlipOralCavity2010"),
			EnumerationLiteral(name="urnihepatapsrcancerpharynx2010"),
			EnumerationLiteral(name="urnihepatapsrcancersalivaryGland2010"),
			EnumerationLiteral(name="urnihepatapsrcancerlarynx2010"),
			EnumerationLiteral(name="urnihepharmpre2010"),
			EnumerationLiteral(name="urnihepharmpadv2010"),
			EnumerationLiteral(name="urnihepharmdis2010"),
			EnumerationLiteral(name="urnihepharmpml2013"),
			EnumerationLiteral(name="urnhl7orgsdwgccdastructuredBody11"),
			EnumerationLiteral(name="urnhl7orgsdwgccdanonXmlBody11")
    }
)

LibraryType: Enumeration = Enumeration(
    name="LibraryType",
    literals={
            
    }
)

DefinitionTopic: Enumeration = Enumeration(
    name="DefinitionTopic",
    literals={
            
    }
)

MeasureScoring: Enumeration = Enumeration(
    name="MeasureScoring",
    literals={
            
    }
)

CompositeMeasureScoring: Enumeration = Enumeration(
    name="CompositeMeasureScoring",
    literals={
            
    }
)

GoalPriority: Enumeration = Enumeration(
    name="GoalPriority",
    literals={
            
    }
)

GoalStartEvent: Enumeration = Enumeration(
    name="GoalStartEvent",
    literals={
            EnumerationLiteral(name="_32485007"),
			EnumerationLiteral(name="_308283009"),
			EnumerationLiteral(name="_442137000"),
			EnumerationLiteral(name="_386216000")
    }
)

MeasureType: Enumeration = Enumeration(
    name="MeasureType",
    literals={
            
    }
)

MeasurePopulationType: Enumeration = Enumeration(
    name="MeasurePopulationType",
    literals={
            
    }
)

MeasureDataUsage: Enumeration = Enumeration(
    name="MeasureDataUsage",
    literals={
            
    }
)

MaritalStatusCodes: Enumeration = Enumeration(
    name="MaritalStatusCodes",
    literals={
            EnumerationLiteral(name="unk")
    }
)

PatientContactRelationship: Enumeration = Enumeration(
    name="PatientContactRelationship",
    literals={
            
    }
)

ExampleUseCodesForList: Enumeration = Enumeration(
    name="ExampleUseCodesForList",
    literals={
            
    }
)

V3ActEncounterCode: Enumeration = Enumeration(
    name="V3ActEncounterCode",
    literals={
            
    }
)

EncounterType: Enumeration = Enumeration(
    name="EncounterType",
    literals={
            
    }
)

ServiceType: Enumeration = Enumeration(
    name="ServiceType",
    literals={
            
    }
)

V3ActPriority: Enumeration = Enumeration(
    name="V3ActPriority",
    literals={
            
    }
)

EpisodeOfCareType: Enumeration = Enumeration(
    name="EpisodeOfCareType",
    literals={
            
    }
)

ConditionCategoryCodes: Enumeration = Enumeration(
    name="ConditionCategoryCodes",
    literals={
            
    }
)

ConditionDiagnosisSeverity: Enumeration = Enumeration(
    name="ConditionDiagnosisSeverity",
    literals={
            EnumerationLiteral(name="_24484000"),
			EnumerationLiteral(name="_6736007"),
			EnumerationLiteral(name="_255604002")
    }
)

ConditionProblemDiagnosisCodes: Enumeration = Enumeration(
    name="ConditionProblemDiagnosisCodes",
    literals={
            EnumerationLiteral(name="_160245001")
    }
)

SnomedctBodyStructures: Enumeration = Enumeration(
    name="SnomedctBodyStructures",
    literals={
            
    }
)

ConditionStage: Enumeration = Enumeration(
    name="ConditionStage",
    literals={
            
    }
)

InvestigationType: Enumeration = Enumeration(
    name="InvestigationType",
    literals={
            EnumerationLiteral(name="_271336007"),
			EnumerationLiteral(name="_160237006")
    }
)

PlanDefinitionType: Enumeration = Enumeration(
    name="PlanDefinitionType",
    literals={
            
    }
)

GoalCategory: Enumeration = Enumeration(
    name="GoalCategory",
    literals={
            
    }
)

SnomedctClinicalFindings: Enumeration = Enumeration(
    name="SnomedctClinicalFindings",
    literals={
            
    }
)

ActionParticipantRole: Enumeration = Enumeration(
    name="ActionParticipantRole",
    literals={
            
    }
)

ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            
    }
)

CarePlanCategory: Enumeration = Enumeration(
    name="CarePlanCategory",
    literals={
            
    }
)

CareTeamCategory: Enumeration = Enumeration(
    name="CareTeamCategory",
    literals={
            
    }
)

ParticipantRoles: Enumeration = Enumeration(
    name="ParticipantRoles",
    literals={
            
    }
)

GoalAchievementStatus: Enumeration = Enumeration(
    name="GoalAchievementStatus",
    literals={
            
    }
)

CarePlanActivityOutcome: Enumeration = Enumeration(
    name="CarePlanActivityOutcome",
    literals={
            
    }
)

AppointmentCancellationReason: Enumeration = Enumeration(
    name="AppointmentCancellationReason",
    literals={
            
    }
)

ServiceCategory: Enumeration = Enumeration(
    name="ServiceCategory",
    literals={
            
    }
)

PracticeSettingCodeValueSet: Enumeration = Enumeration(
    name="PracticeSettingCodeValueSet",
    literals={
            EnumerationLiteral(name="_394601005"),
			EnumerationLiteral(name="_394581000"),
			EnumerationLiteral(name="_408467006"),
			EnumerationLiteral(name="_394577000"),
			EnumerationLiteral(name="_394578005"),
			EnumerationLiteral(name="_421661004"),
			EnumerationLiteral(name="_408462000"),
			EnumerationLiteral(name="_394579002"),
			EnumerationLiteral(name="_394804000"),
			EnumerationLiteral(name="_394580004"),
			EnumerationLiteral(name="_394803006"),
			EnumerationLiteral(name="_408480009"),
			EnumerationLiteral(name="_408454008"),
			EnumerationLiteral(name="_394809005"),
			EnumerationLiteral(name="_394592004"),
			EnumerationLiteral(name="_394600006"),
			EnumerationLiteral(name="_419192003"),
			EnumerationLiteral(name="_408478003"),
			EnumerationLiteral(name="_394812008"),
			EnumerationLiteral(name="_408444009"),
			EnumerationLiteral(name="_394582007"),
			EnumerationLiteral(name="_408475000"),
			EnumerationLiteral(name="_410005002"),
			EnumerationLiteral(name="_394583002"),
			EnumerationLiteral(name="_419772000"),
			EnumerationLiteral(name="_394584008"),
			EnumerationLiteral(name="_408443003"),
			EnumerationLiteral(name="_394802001"),
			EnumerationLiteral(name="_394915009"),
			EnumerationLiteral(name="_394814009"),
			EnumerationLiteral(name="_394808002"),
			EnumerationLiteral(name="_394811001"),
			EnumerationLiteral(name="_408446006"),
			EnumerationLiteral(name="_394586005"),
			EnumerationLiteral(name="_394916005"),
			EnumerationLiteral(name="_408472002"),
			EnumerationLiteral(name="_394597005"),
			EnumerationLiteral(name="_394598000"),
			EnumerationLiteral(name="_394807007"),
			EnumerationLiteral(name="_418058008"),
			EnumerationLiteral(name="_420208008"),
			EnumerationLiteral(name="_408468001"),
			EnumerationLiteral(name="_394593009"),
			EnumerationLiteral(name="_394813003"),
			EnumerationLiteral(name="_410001006"),
			EnumerationLiteral(name="_394589003"),
			EnumerationLiteral(name="_394591006"),
			EnumerationLiteral(name="_394599008"),
			EnumerationLiteral(name="_394649004"),
			EnumerationLiteral(name="_408470005"),
			EnumerationLiteral(name="_394585009"),
			EnumerationLiteral(name="_394821009"),
			EnumerationLiteral(name="_422191005"),
			EnumerationLiteral(name="_394594003"),
			EnumerationLiteral(name="_416304004"),
			EnumerationLiteral(name="_418960008"),
			EnumerationLiteral(name="_394882004"),
			EnumerationLiteral(name="_394806003"),
			EnumerationLiteral(name="_394588006"),
			EnumerationLiteral(name="_408459003"),
			EnumerationLiteral(name="_394607009"),
			EnumerationLiteral(name="_419610006"),
			EnumerationLiteral(name="_408476004"),
			EnumerationLiteral(name="_418652005"),
			EnumerationLiteral(name="_418535003"),
			EnumerationLiteral(name="_418862001"),
			EnumerationLiteral(name="_419365004"),
			EnumerationLiteral(name="_418002000"),
			EnumerationLiteral(name="_419983000"),
			EnumerationLiteral(name="_419170002"),
			EnumerationLiteral(name="_419472004"),
			EnumerationLiteral(name="_394539006"),
			EnumerationLiteral(name="_420112009"),
			EnumerationLiteral(name="_409968004"),
			EnumerationLiteral(name="_394587001"),
			EnumerationLiteral(name="_394913002"),
			EnumerationLiteral(name="_408440000"),
			EnumerationLiteral(name="_418112009"),
			EnumerationLiteral(name="_419815003"),
			EnumerationLiteral(name="_394914008"),
			EnumerationLiteral(name="_408455009"),
			EnumerationLiteral(name="_394602003"),
			EnumerationLiteral(name="_408447002"),
			EnumerationLiteral(name="_394810000"),
			EnumerationLiteral(name="_408450004"),
			EnumerationLiteral(name="_394801008"),
			EnumerationLiteral(name="_408463005"),
			EnumerationLiteral(name="_408469009"),
			EnumerationLiteral(name="_408466002"),
			EnumerationLiteral(name="_408471009"),
			EnumerationLiteral(name="_408464004"),
			EnumerationLiteral(name="_408441001"),
			EnumerationLiteral(name="_408465003"),
			EnumerationLiteral(name="_394605001"),
			EnumerationLiteral(name="_394608004a"),
			EnumerationLiteral(name="_408461007"),
			EnumerationLiteral(name="_408460008"),
			EnumerationLiteral(name="_408460008a"),
			EnumerationLiteral(name="_394606000"),
			EnumerationLiteral(name="_408449004"),
			EnumerationLiteral(name="_394608004"),
			EnumerationLiteral(name="_418018006"),
			EnumerationLiteral(name="_394604002"),
			EnumerationLiteral(name="_394609007"),
			EnumerationLiteral(name="_408474001"),
			EnumerationLiteral(name="_394610002"),
			EnumerationLiteral(name="_394611003"),
			EnumerationLiteral(name="_408477008"),
			EnumerationLiteral(name="_419321007"),
			EnumerationLiteral(name="_394576009"),
			EnumerationLiteral(name="_394590007"),
			EnumerationLiteral(name="_409967009"),
			EnumerationLiteral(name="_408448007"),
			EnumerationLiteral(name="_419043006"),
			EnumerationLiteral(name="_394612005"),
			EnumerationLiteral(name="_394733009"),
			EnumerationLiteral(name="_394732004")
    }
)

V20276: Enumeration = Enumeration(
    name="V20276",
    literals={
            
    }
)

EncounterReasonCodes: Enumeration = Enumeration(
    name="EncounterReasonCodes",
    literals={
            
    }
)

ProcedureCodesSnomedcT: Enumeration = Enumeration(
    name="ProcedureCodesSnomedcT",
    literals={
            
    }
)

V20116: Enumeration = Enumeration(
    name="V20116",
    literals={
            
    }
)

V3ServiceDeliveryLocationRoleType: Enumeration = Enumeration(
    name="V3ServiceDeliveryLocationRoleType",
    literals={
            
    }
)

LocationType: Enumeration = Enumeration(
    name="LocationType",
    literals={
            
    }
)

SnomedctMedicationCodes: Enumeration = Enumeration(
    name="SnomedctMedicationCodes",
    literals={
            
    }
)

V20487: Enumeration = Enumeration(
    name="V20487",
    literals={
            
    }
)

PreparePatient: Enumeration = Enumeration(
    name="PreparePatient",
    literals={
            
    }
)

SpecimenCollection: Enumeration = Enumeration(
    name="SpecimenCollection",
    literals={
            EnumerationLiteral(name="_129323009"),
			EnumerationLiteral(name="_73416001"),
			EnumerationLiteral(name="_129316008"),
			EnumerationLiteral(name="_129314006"),
			EnumerationLiteral(name="_129300006"),
			EnumerationLiteral(name="_129304002"),
			EnumerationLiteral(name="_225113003"),
			EnumerationLiteral(name="_70777001"),
			EnumerationLiteral(name="_386089008"),
			EnumerationLiteral(name="_278450005")
    }
)

ContainerMaterials: Enumeration = Enumeration(
    name="ContainerMaterials",
    literals={
            EnumerationLiteral(name="_32039001"),
			EnumerationLiteral(name="_61088005"),
			EnumerationLiteral(name="_425620007")
    }
)

SpecimenContainerType: Enumeration = Enumeration(
    name="SpecimenContainerType",
    literals={
            
    }
)

ContainerCap: Enumeration = Enumeration(
    name="ContainerCap",
    literals={
            
    }
)

V20371: Enumeration = Enumeration(
    name="V20371",
    literals={
            
    }
)

RejectionCriterion: Enumeration = Enumeration(
    name="RejectionCriterion",
    literals={
            
    }
)

HandlingConditionSet: Enumeration = Enumeration(
    name="HandlingConditionSet",
    literals={
            
    }
)

ObservationCategoryCodes: Enumeration = Enumeration(
    name="ObservationCategoryCodes",
    literals={
            
    }
)

ObservationMethods: Enumeration = Enumeration(
    name="ObservationMethods",
    literals={
            
    }
)

UcumCodes: Enumeration = Enumeration(
    name="UcumCodes",
    literals={
            
    }
)

ObservationReferenceRangeMeaningCodes: Enumeration = Enumeration(
    name="ObservationReferenceRangeMeaningCodes",
    literals={
            
    }
)

ObservationReferenceRangeAppliesToCodes: Enumeration = Enumeration(
    name="ObservationReferenceRangeAppliesToCodes",
    literals={
            EnumerationLiteral(name="_248153007"),
			EnumerationLiteral(name="_248152002"),
			EnumerationLiteral(name="_77386006")
    }
)

ServiceRequestCategoryCodes: Enumeration = Enumeration(
    name="ServiceRequestCategoryCodes",
    literals={
            EnumerationLiteral(name="_108252007"),
			EnumerationLiteral(name="_363679005"),
			EnumerationLiteral(name="_409063005"),
			EnumerationLiteral(name="_409073007"),
			EnumerationLiteral(name="_387713003")
    }
)

ServiceRequestOrderDetailsCodes: Enumeration = Enumeration(
    name="ServiceRequestOrderDetailsCodes",
    literals={
            EnumerationLiteral(name="_59427005"),
			EnumerationLiteral(name="_47545007"),
			EnumerationLiteral(name="_286812008"),
			EnumerationLiteral(name="_243144002"),
			EnumerationLiteral(name="_243150007")
    }
)

ProcedureReasonCodes: Enumeration = Enumeration(
    name="ProcedureReasonCodes",
    literals={
            
    }
)

CoverageTypeAndSelfPayCodes: Enumeration = Enumeration(
    name="CoverageTypeAndSelfPayCodes",
    literals={
            
    }
)

SubscriberRelationshipCodes: Enumeration = Enumeration(
    name="SubscriberRelationshipCodes",
    literals={
            
    }
)

CoverageClassCodes: Enumeration = Enumeration(
    name="CoverageClassCodes",
    literals={
            
    }
)

CoverageCopayTypeCodes: Enumeration = Enumeration(
    name="CoverageCopayTypeCodes",
    literals={
            
    }
)

ExampleCoverageFinancialExceptionCodes: Enumeration = Enumeration(
    name="ExampleCoverageFinancialExceptionCodes",
    literals={
            
    }
)

ContractResourceLegalStateCodes: Enumeration = Enumeration(
    name="ContractResourceLegalStateCodes",
    literals={
            
    }
)

ContractContentDerivationCodes: Enumeration = Enumeration(
    name="ContractContentDerivationCodes",
    literals={
            
    }
)

ContractResourceExpirationTypeCodes: Enumeration = Enumeration(
    name="ContractResourceExpirationTypeCodes",
    literals={
            
    }
)

ContractResourceScopeCodes: Enumeration = Enumeration(
    name="ContractResourceScopeCodes",
    literals={
            
    }
)

ContractTypeCodes: Enumeration = Enumeration(
    name="ContractTypeCodes",
    literals={
            
    }
)

ContractSubtypeCodes: Enumeration = Enumeration(
    name="ContractSubtypeCodes",
    literals={
            
    }
)

ContractResourceDefinitionTypeCodes: Enumeration = Enumeration(
    name="ContractResourceDefinitionTypeCodes",
    literals={
            
    }
)

ContractResourceDefinitionSubtypeCodes: Enumeration = Enumeration(
    name="ContractResourceDefinitionSubtypeCodes",
    literals={
            
    }
)

ContractTermTypeCodes: Enumeration = Enumeration(
    name="ContractTermTypeCodes",
    literals={
            
    }
)

ContractTermSubtypeCodes: Enumeration = Enumeration(
    name="ContractTermSubtypeCodes",
    literals={
            
    }
)

ContractResourceScopeCodesA: Enumeration = Enumeration(
    name="ContractResourceScopeCodesA",
    literals={
            
    }
)

ContractResourceScopeCodesB: Enumeration = Enumeration(
    name="ContractResourceScopeCodesB",
    literals={
            
    }
)

ContractResourceSecurityControlCodes: Enumeration = Enumeration(
    name="ContractResourceSecurityControlCodes",
    literals={
            
    }
)

ContractResourcePartyRoleCodes: Enumeration = Enumeration(
    name="ContractResourcePartyRoleCodes",
    literals={
            
    }
)

V3ActConsentDirective: Enumeration = Enumeration(
    name="V3ActConsentDirective",
    literals={
            
    }
)

ContractResourceDecisionModeCodes: Enumeration = Enumeration(
    name="ContractResourceDecisionModeCodes",
    literals={
            
    }
)

ContractResourceAssetScopeCodes: Enumeration = Enumeration(
    name="ContractResourceAssetScopeCodes",
    literals={
            
    }
)

ContractResourceAssetTypeCodes: Enumeration = Enumeration(
    name="ContractResourceAssetTypeCodes",
    literals={
            
    }
)

ContractResourceAssetSubTypeCodes: Enumeration = Enumeration(
    name="ContractResourceAssetSubTypeCodes",
    literals={
            
    }
)

ConsentContentClass: Enumeration = Enumeration(
    name="ConsentContentClass",
    literals={
            EnumerationLiteral(name="httphl7orgfhirStructureDefinitionlipidprofile"),
			EnumerationLiteral(name="applicationhl7cdaxml")
    }
)

ContractResourceAssetContextCodes: Enumeration = Enumeration(
    name="ContractResourceAssetContextCodes",
    literals={
            
    }
)

ContractResourceAssetAvailiabilityCodes: Enumeration = Enumeration(
    name="ContractResourceAssetAvailiabilityCodes",
    literals={
            
    }
)

ContractActionCodes: Enumeration = Enumeration(
    name="ContractActionCodes",
    literals={
            
    }
)

ContractActorRoleCodes: Enumeration = Enumeration(
    name="ContractActorRoleCodes",
    literals={
            
    }
)

V3PurposeOfUse: Enumeration = Enumeration(
    name="V3PurposeOfUse",
    literals={
            
    }
)

ContractResourceActionStatusCodes: Enumeration = Enumeration(
    name="ContractResourceActionStatusCodes",
    literals={
            
    }
)

ProvenanceParticipantType: Enumeration = Enumeration(
    name="ProvenanceParticipantType",
    literals={
            
    }
)

ProvenanceParticipantRole: Enumeration = Enumeration(
    name="ProvenanceParticipantRole",
    literals={
            
    }
)

PatientRelationshipType: Enumeration = Enumeration(
    name="PatientRelationshipType",
    literals={
            
    }
)

ProvenanceActivityType: Enumeration = Enumeration(
    name="ProvenanceActivityType",
    literals={
            EnumerationLiteral(name="pseud"),
			EnumerationLiteral(name="create"),
			EnumerationLiteral(name="la"),
			EnumerationLiteral(name="anony"),
			EnumerationLiteral(name="deid"),
			EnumerationLiteral(name="mask"),
			EnumerationLiteral(name="label"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="append"),
			EnumerationLiteral(name="nullify")
    }
)

SecurityRoleType: Enumeration = Enumeration(
    name="SecurityRoleType",
    literals={
            EnumerationLiteral(name="named"),
			EnumerationLiteral(name="nok"),
			EnumerationLiteral(name="amender"),
			EnumerationLiteral(name="coauth"),
			EnumerationLiteral(name="cont"),
			EnumerationLiteral(name="evtwit"),
			EnumerationLiteral(name="primauth"),
			EnumerationLiteral(name="reviewer"),
			EnumerationLiteral(name="source"),
			EnumerationLiteral(name="trans"),
			EnumerationLiteral(name="valid"),
			EnumerationLiteral(name="verf"),
			EnumerationLiteral(name="affl"),
			EnumerationLiteral(name="agnt"),
			EnumerationLiteral(name="assigned"),
			EnumerationLiteral(name="claim"),
			EnumerationLiteral(name="covpty"),
			EnumerationLiteral(name="depen"),
			EnumerationLiteral(name="econ"),
			EnumerationLiteral(name="emp"),
			EnumerationLiteral(name="guard"),
			EnumerationLiteral(name="invsbj"),
			EnumerationLiteral(name="autm"),
			EnumerationLiteral(name="auwa"),
			EnumerationLiteral(name="pat"),
			EnumerationLiteral(name="prov"),
			EnumerationLiteral(name="not_"),
			EnumerationLiteral(name="classifier"),
			EnumerationLiteral(name="consenter"),
			EnumerationLiteral(name="conswit"),
			EnumerationLiteral(name="copart"),
			EnumerationLiteral(name="declassifier"),
			EnumerationLiteral(name="delegatee"),
			EnumerationLiteral(name="delegator"),
			EnumerationLiteral(name="downgrder"),
			EnumerationLiteral(name="dpowatt"),
			EnumerationLiteral(name="excest"),
			EnumerationLiteral(name="grantee"),
			EnumerationLiteral(name="grantor"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="guadltm"),
			EnumerationLiteral(name="hpowatt"),
			EnumerationLiteral(name="intprter"),
			EnumerationLiteral(name="powatt"),
			EnumerationLiteral(name="resprsn"),
			EnumerationLiteral(name="spowatt"),
			EnumerationLiteral(name="aucg"),
			EnumerationLiteral(name="aulr"),
			EnumerationLiteral(name="promsk"),
			EnumerationLiteral(name="aut"),
			EnumerationLiteral(name="cst"),
			EnumerationLiteral(name="inf"),
			EnumerationLiteral(name="ircp"),
			EnumerationLiteral(name="la"),
			EnumerationLiteral(name="ircpa"),
			EnumerationLiteral(name="trc"),
			EnumerationLiteral(name="wit"),
			EnumerationLiteral(name="_110150"),
			EnumerationLiteral(name="_110151"),
			EnumerationLiteral(name="_110152"),
			EnumerationLiteral(name="_110153"),
			EnumerationLiteral(name="_110154"),
			EnumerationLiteral(name="_110155")
    }
)

ContractSignerTypeCodes: Enumeration = Enumeration(
    name="ContractSignerTypeCodes",
    literals={
            
    }
)

FhirSpecimenCollectionMethod: Enumeration = Enumeration(
    name="FhirSpecimenCollectionMethod",
    literals={
            EnumerationLiteral(name="_386089008"),
			EnumerationLiteral(name="_278450005"),
			EnumerationLiteral(name="_129316008"),
			EnumerationLiteral(name="_129314006"),
			EnumerationLiteral(name="_129300006"),
			EnumerationLiteral(name="_129304002"),
			EnumerationLiteral(name="_129323009"),
			EnumerationLiteral(name="_73416001"),
			EnumerationLiteral(name="_225113003"),
			EnumerationLiteral(name="_70777001")
    }
)

FhirDeviceStatusReason: Enumeration = Enumeration(
    name="FhirDeviceStatusReason",
    literals={
            
    }
)

DeviceType: Enumeration = Enumeration(
    name="DeviceType",
    literals={
            
    }
)

V20916: Enumeration = Enumeration(
    name="V20916",
    literals={
            
    }
)

SpecimenProcessingProcedure: Enumeration = Enumeration(
    name="SpecimenProcessingProcedure",
    literals={
            
    }
)

SubstanceCategoryCodes: Enumeration = Enumeration(
    name="SubstanceCategoryCodes",
    literals={
            
    }
)

SubstanceCode: Enumeration = Enumeration(
    name="SubstanceCode",
    literals={
            
    }
)

V20493: Enumeration = Enumeration(
    name="V20493",
    literals={
            
    }
)

ParticipantType: Enumeration = Enumeration(
    name="ParticipantType",
    literals={
            EnumerationLiteral(name="sprf"),
			EnumerationLiteral(name="pprf"),
			EnumerationLiteral(name="part")
    }
)

SnomedctReasonMedicationNotGivenCodes: Enumeration = Enumeration(
    name="SnomedctReasonMedicationNotGivenCodes",
    literals={
            
    }
)

MedicationAdministrationCategoryCodes: Enumeration = Enumeration(
    name="MedicationAdministrationCategoryCodes",
    literals={
            
    }
)

MedicationAdministrationPerformerFunctionCodes: Enumeration = Enumeration(
    name="MedicationAdministrationPerformerFunctionCodes",
    literals={
            
    }
)

ReasonMedicationGivenCodes: Enumeration = Enumeration(
    name="ReasonMedicationGivenCodes",
    literals={
            
    }
)

MedicationRequestStatusReasonCodes: Enumeration = Enumeration(
    name="MedicationRequestStatusReasonCodes",
    literals={
            
    }
)

MedicationRequestCategoryCodes: Enumeration = Enumeration(
    name="MedicationRequestCategoryCodes",
    literals={
            
    }
)

ProcedurePerformerRoleCodes: Enumeration = Enumeration(
    name="ProcedurePerformerRoleCodes",
    literals={
            
    }
)

MedicationRequestCourseOfTherapyCodes: Enumeration = Enumeration(
    name="MedicationRequestCourseOfTherapyCodes",
    literals={
            
    }
)

V3ActSubstanceAdminSubstitutionCode: Enumeration = Enumeration(
    name="V3ActSubstanceAdminSubstitutionCode",
    literals={
            
    }
)

V3SubstanceAdminSubstitutionReason: Enumeration = Enumeration(
    name="V3SubstanceAdminSubstitutionReason",
    literals={
            
    }
)

DetectedIssueCategory: Enumeration = Enumeration(
    name="DetectedIssueCategory",
    literals={
            
    }
)

ManifestationAndSymptomCodes: Enumeration = Enumeration(
    name="ManifestationAndSymptomCodes",
    literals={
            
    }
)

DetectedIssueMitigationAction: Enumeration = Enumeration(
    name="DetectedIssueMitigationAction",
    literals={
            
    }
)

FhirDeviceTypes: Enumeration = Enumeration(
    name="FhirDeviceTypes",
    literals={
            
    }
)

DeviceSafety: Enumeration = Enumeration(
    name="DeviceSafety",
    literals={
            EnumerationLiteral(name="c106046"),
			EnumerationLiteral(name="c106045"),
			EnumerationLiteral(name="c106047"),
			EnumerationLiteral(name="c113844"),
			EnumerationLiteral(name="c101673"),
			EnumerationLiteral(name="c106038")
    }
)

DataAbsentReason: Enumeration = Enumeration(
    name="DataAbsentReason",
    literals={
            
    }
)

ObservationInterpretationCodes: Enumeration = Enumeration(
    name="ObservationInterpretationCodes",
    literals={
            
    }
)

DocumentClassValueSet: Enumeration = Enumeration(
    name="DocumentClassValueSet",
    literals={
            EnumerationLiteral(name="_297515"),
			EnumerationLiteral(name="_297523"),
			EnumerationLiteral(name="_113696"),
			EnumerationLiteral(name="_114850"),
			EnumerationLiteral(name="_114868"),
			EnumerationLiteral(name="_114884"),
			EnumerationLiteral(name="_115063"),
			EnumerationLiteral(name="_115436"),
			EnumerationLiteral(name="_155085"),
			EnumerationLiteral(name="_187260"),
			EnumerationLiteral(name="_187617"),
			EnumerationLiteral(name="_188425"),
			EnumerationLiteral(name="_264366"),
			EnumerationLiteral(name="_264416"),
			EnumerationLiteral(name="_264424"),
			EnumerationLiteral(name="_278952"),
			EnumerationLiteral(name="_278960"),
			EnumerationLiteral(name="_278978"),
			EnumerationLiteral(name="_278986"),
			EnumerationLiteral(name="_285700"),
			EnumerationLiteral(name="_286195"),
			EnumerationLiteral(name="_286344"),
			EnumerationLiteral(name="_297499"),
			EnumerationLiteral(name="_297507"),
			EnumerationLiteral(name="_341099"),
			EnumerationLiteral(name="_341172"),
			EnumerationLiteral(name="_341214"),
			EnumerationLiteral(name="_341222"),
			EnumerationLiteral(name="_341339"),
			EnumerationLiteral(name="_341404"),
			EnumerationLiteral(name="_347484"),
			EnumerationLiteral(name="_347757"),
			EnumerationLiteral(name="_470393"),
			EnumerationLiteral(name="_470427"),
			EnumerationLiteral(name="_470450"),
			EnumerationLiteral(name="_470468"),
			EnumerationLiteral(name="_470492"),
			EnumerationLiteral(name="_570176"),
			EnumerationLiteral(name="_570168"),
			EnumerationLiteral(name="_564450"),
			EnumerationLiteral(name="_535765"),
			EnumerationLiteral(name="_564476"),
			EnumerationLiteral(name="_187484"),
			EnumerationLiteral(name="_115048"),
			EnumerationLiteral(name="_571331")
    }
)

DocumentReferenceFormatCodeSet: Enumeration = Enumeration(
    name="DocumentReferenceFormatCodeSet",
    literals={
            
    }
)

V3ActCode: Enumeration = Enumeration(
    name="V3ActCode",
    literals={
            
    }
)

FacilityTypeCodeValueSet: Enumeration = Enumeration(
    name="FacilityTypeCodeValueSet",
    literals={
            EnumerationLiteral(name="_79993009"),
			EnumerationLiteral(name="_82242000"),
			EnumerationLiteral(name="_225732001"),
			EnumerationLiteral(name="_31628002"),
			EnumerationLiteral(name="_32074000"),
			EnumerationLiteral(name="_4322002"),
			EnumerationLiteral(name="_224687002"),
			EnumerationLiteral(name="_62480006"),
			EnumerationLiteral(name="_80522000"),
			EnumerationLiteral(name="_36125001"),
			EnumerationLiteral(name="_48311003"),
			EnumerationLiteral(name="_284546000"),
			EnumerationLiteral(name="_42665001"),
			EnumerationLiteral(name="_45618002"),
			EnumerationLiteral(name="_418518002"),
			EnumerationLiteral(name="_73770003"),
			EnumerationLiteral(name="_69362002"),
			EnumerationLiteral(name="_52668009"),
			EnumerationLiteral(name="_360957003"),
			EnumerationLiteral(name="_10206005"),
			EnumerationLiteral(name="_37550003"),
			EnumerationLiteral(name="_73644007"),
			EnumerationLiteral(name="_79491001"),
			EnumerationLiteral(name="_33022008"),
			EnumerationLiteral(name="_58482006"),
			EnumerationLiteral(name="_90484001"),
			EnumerationLiteral(name="_1814000"),
			EnumerationLiteral(name="_22549003"),
			EnumerationLiteral(name="_56293002"),
			EnumerationLiteral(name="_360966004"),
			EnumerationLiteral(name="_2849009"),
			EnumerationLiteral(name="_14866005"),
			EnumerationLiteral(name="_38238005"),
			EnumerationLiteral(name="_56189001"),
			EnumerationLiteral(name="_89972002"),
			EnumerationLiteral(name="_78088001"),
			EnumerationLiteral(name="_78001009"),
			EnumerationLiteral(name="_23392004"),
			EnumerationLiteral(name="_36293008"),
			EnumerationLiteral(name="_3729002"),
			EnumerationLiteral(name="_5584006"),
			EnumerationLiteral(name="_37546005"),
			EnumerationLiteral(name="_57159002"),
			EnumerationLiteral(name="_331006"),
			EnumerationLiteral(name="_50569004"),
			EnumerationLiteral(name="_46224007"),
			EnumerationLiteral(name="_81234003"),
			EnumerationLiteral(name="_19602009"),
			EnumerationLiteral(name="_39350007"),
			EnumerationLiteral(name="_83891005"),
			EnumerationLiteral(name="_394759007"),
			EnumerationLiteral(name="_405607001"),
			EnumerationLiteral(name="_309900005"),
			EnumerationLiteral(name="_275576008"),
			EnumerationLiteral(name="_10531005"),
			EnumerationLiteral(name="_91154008"),
			EnumerationLiteral(name="_41844007"),
			EnumerationLiteral(name="_45899008"),
			EnumerationLiteral(name="_51563005"),
			EnumerationLiteral(name="_1773006"),
			EnumerationLiteral(name="_72311000"),
			EnumerationLiteral(name="_6827000"),
			EnumerationLiteral(name="_309898008"),
			EnumerationLiteral(name="_39913001"),
			EnumerationLiteral(name="_77931003"),
			EnumerationLiteral(name="_25681007"),
			EnumerationLiteral(name="_20078004"),
			EnumerationLiteral(name="_35971002"),
			EnumerationLiteral(name="_11424001"),
			EnumerationLiteral(name="_409519008"),
			EnumerationLiteral(name="_901005"),
			EnumerationLiteral(name="_2081004"),
			EnumerationLiteral(name="_59374000"),
			EnumerationLiteral(name="_413456002"),
			EnumerationLiteral(name="_413817003"),
			EnumerationLiteral(name="_310205006"),
			EnumerationLiteral(name="_419955002"),
			EnumerationLiteral(name="_272501009"),
			EnumerationLiteral(name="_394777002")
    }
)

SpecialArrangements: Enumeration = Enumeration(
    name="SpecialArrangements",
    literals={
            
    }
)

DischargeDisposition: Enumeration = Enumeration(
    name="DischargeDisposition",
    literals={
            
    }
)

ClinicalImpressionPrognosis: Enumeration = Enumeration(
    name="ClinicalImpressionPrognosis",
    literals={
            
    }
)

RiskProbability: Enumeration = Enumeration(
    name="RiskProbability",
    literals={
            
    }
)

ConditionStageType: Enumeration = Enumeration(
    name="ConditionStageType",
    literals={
            EnumerationLiteral(name="_261023001"),
			EnumerationLiteral(name="_260998006")
    }
)

DiagnosisRole: Enumeration = Enumeration(
    name="DiagnosisRole",
    literals={
            
    }
)

AccountTypes: Enumeration = Enumeration(
    name="AccountTypes",
    literals={
            
    }
)

AdmitSource: Enumeration = Enumeration(
    name="AdmitSource",
    literals={
            
    }
)

V20092: Enumeration = Enumeration(
    name="V20092",
    literals={
            
    }
)

Diet: Enumeration = Enumeration(
    name="Diet",
    literals={
            
    }
)

SpecialCourtesy: Enumeration = Enumeration(
    name="SpecialCourtesy",
    literals={
            EnumerationLiteral(name="unk"),
			EnumerationLiteral(name="ext"),
			EnumerationLiteral(name="nrm"),
			EnumerationLiteral(name="prf"),
			EnumerationLiteral(name="stf"),
			EnumerationLiteral(name="vip")
    }
)

ListOrderCodes: Enumeration = Enumeration(
    name="ListOrderCodes",
    literals={
            
    }
)

PatientMedicineChangeTypes: Enumeration = Enumeration(
    name="PatientMedicineChangeTypes",
    literals={
            
    }
)

ListEmptyReasons: Enumeration = Enumeration(
    name="ListEmptyReasons",
    literals={
            
    }
)

ResearchStudyPrimaryPurposeType: Enumeration = Enumeration(
    name="ResearchStudyPrimaryPurposeType",
    literals={
            
    }
)

ResearchStudyPhase: Enumeration = Enumeration(
    name="ResearchStudyPhase",
    literals={
            
    }
)

ResearchStudyReasonStopped: Enumeration = Enumeration(
    name="ResearchStudyReasonStopped",
    literals={
            
    }
)

ResearchStudyObjectiveType: Enumeration = Enumeration(
    name="ResearchStudyObjectiveType",
    literals={
            
    }
)

ConsentScopeCodes: Enumeration = Enumeration(
    name="ConsentScopeCodes",
    literals={
            
    }
)

ConsentCategoryCodes: Enumeration = Enumeration(
    name="ConsentCategoryCodes",
    literals={
            EnumerationLiteral(name="_592840"),
			EnumerationLiteral(name="_570168"),
			EnumerationLiteral(name="_570176"),
			EnumerationLiteral(name="_642926")
    }
)

ConsentPolicyRuleCodes: Enumeration = Enumeration(
    name="ConsentPolicyRuleCodes",
    literals={
            
    }
)

ConsentActionCodes: Enumeration = Enumeration(
    name="ConsentActionCodes",
    literals={
            
    }
)

ConsentContentCodes: Enumeration = Enumeration(
    name="ConsentContentCodes",
    literals={
            
    }
)

ChargeItemCode: Enumeration = Enumeration(
    name="ChargeItemCode",
    literals={
            
    }
)

SnomedctFormCodes: Enumeration = Enumeration(
    name="SnomedctFormCodes",
    literals={
            
    }
)

IcD10Codes: Enumeration = Enumeration(
    name="IcD10Codes",
    literals={
            EnumerationLiteral(name="_123456"),
			EnumerationLiteral(name="_123457"),
			EnumerationLiteral(name="_987654"),
			EnumerationLiteral(name="_123987"),
			EnumerationLiteral(name="_112233"),
			EnumerationLiteral(name="_997755"),
			EnumerationLiteral(name="_321789")
    }
)

DiagnosticServiceSectionCodes: Enumeration = Enumeration(
    name="DiagnosticServiceSectionCodes",
    literals={
            
    }
)

LoincDiagnosticReportCodes: Enumeration = Enumeration(
    name="LoincDiagnosticReportCodes",
    literals={
            
    }
)

AcquisitionModality: Enumeration = Enumeration(
    name="AcquisitionModality",
    literals={
            EnumerationLiteral(name="mg"),
			EnumerationLiteral(name="sm"),
			EnumerationLiteral(name="opv"),
			EnumerationLiteral(name="dx"),
			EnumerationLiteral(name="opt"),
			EnumerationLiteral(name="bmd"),
			EnumerationLiteral(name="oam"),
			EnumerationLiteral(name="nm"),
			EnumerationLiteral(name="us"),
			EnumerationLiteral(name="oct"),
			EnumerationLiteral(name="op"),
			EnumerationLiteral(name="ivoct"),
			EnumerationLiteral(name="mr"),
			EnumerationLiteral(name="ecg"),
			EnumerationLiteral(name="gm"),
			EnumerationLiteral(name="io"),
			EnumerationLiteral(name="xa"),
			EnumerationLiteral(name="xc"),
			EnumerationLiteral(name="va"),
			EnumerationLiteral(name="ivus"),
			EnumerationLiteral(name="cr"),
			EnumerationLiteral(name="es"),
			EnumerationLiteral(name="ar"),
			EnumerationLiteral(name="ct"),
			EnumerationLiteral(name="oss"),
			EnumerationLiteral(name="len"),
			EnumerationLiteral(name="rg"),
			EnumerationLiteral(name="rf"),
			EnumerationLiteral(name="ker"),
			EnumerationLiteral(name="hd"),
			EnumerationLiteral(name="bdus"),
			EnumerationLiteral(name="pt"),
			EnumerationLiteral(name="eps"),
			EnumerationLiteral(name="px"),
			EnumerationLiteral(name="srf"),
			EnumerationLiteral(name="opm"),
			EnumerationLiteral(name="opr")
    }
)

ProcedureNotPerformedReasonSnomeDCT: Enumeration = Enumeration(
    name="ProcedureNotPerformedReasonSnomeDCT",
    literals={
            
    }
)

ProcedureCategoryCodesSnomedcT: Enumeration = Enumeration(
    name="ProcedureCategoryCodesSnomedcT",
    literals={
            EnumerationLiteral(name="_24642003"),
			EnumerationLiteral(name="_409063005"),
			EnumerationLiteral(name="_409073007"),
			EnumerationLiteral(name="_387713003"),
			EnumerationLiteral(name="_103693007"),
			EnumerationLiteral(name="_46947000"),
			EnumerationLiteral(name="_410606002")
    }
)

ProcedureOutcomeCodesSnomedcT: Enumeration = Enumeration(
    name="ProcedureOutcomeCodesSnomedcT",
    literals={
            EnumerationLiteral(name="_385669000"),
			EnumerationLiteral(name="_385671000"),
			EnumerationLiteral(name="_385670004")
    }
)

ProcedureFollowUpCodesSnomedcT: Enumeration = Enumeration(
    name="ProcedureFollowUpCodesSnomedcT",
    literals={
            EnumerationLiteral(name="_18949003"),
			EnumerationLiteral(name="_30549001"),
			EnumerationLiteral(name="_241031001"),
			EnumerationLiteral(name="_35963001"),
			EnumerationLiteral(name="_225164002"),
			EnumerationLiteral(name="_447346005"),
			EnumerationLiteral(name="_229506003"),
			EnumerationLiteral(name="_274441001"),
			EnumerationLiteral(name="_394725008"),
			EnumerationLiteral(name="_359825008")
    }
)

MediaType: Enumeration = Enumeration(
    name="MediaType",
    literals={
            
    }
)

MediaModality: Enumeration = Enumeration(
    name="MediaModality",
    literals={
            
    }
)

MediaCollectionViewProjection: Enumeration = Enumeration(
    name="MediaCollectionViewProjection",
    literals={
            
    }
)

CommunicationNotDoneReason: Enumeration = Enumeration(
    name="CommunicationNotDoneReason",
    literals={
            
    }
)

ProcedureDeviceActionCodes: Enumeration = Enumeration(
    name="ProcedureDeviceActionCodes",
    literals={
            
    }
)

Laterality: Enumeration = Enumeration(
    name="Laterality",
    literals={
            EnumerationLiteral(name="_419161000"),
			EnumerationLiteral(name="_419465000"),
			EnumerationLiteral(name="_51440002")
    }
)

ImagingStudySeriesPerformerFunction: Enumeration = Enumeration(
    name="ImagingStudySeriesPerformerFunction",
    literals={
            EnumerationLiteral(name="con"),
			EnumerationLiteral(name="vrf"),
			EnumerationLiteral(name="prf"),
			EnumerationLiteral(name="sprf"),
			EnumerationLiteral(name="ref")
    }
)

BodystructureLocationQualifier: Enumeration = Enumeration(
    name="BodystructureLocationQualifier",
    literals={
            EnumerationLiteral(name="_419161000"),
			EnumerationLiteral(name="_419465000"),
			EnumerationLiteral(name="_51440002"),
			EnumerationLiteral(name="_261183002"),
			EnumerationLiteral(name="_261122009"),
			EnumerationLiteral(name="_255561001"),
			EnumerationLiteral(name="_49370004"),
			EnumerationLiteral(name="_264217000"),
			EnumerationLiteral(name="_261089000"),
			EnumerationLiteral(name="_255551008"),
			EnumerationLiteral(name="_351726001"),
			EnumerationLiteral(name="_352730000")
    }
)

CommunicationCategory: Enumeration = Enumeration(
    name="CommunicationCategory",
    literals={
            
    }
)

V3ParticipationMode: Enumeration = Enumeration(
    name="V3ParticipationMode",
    literals={
            
    }
)

CommunicationTopic: Enumeration = Enumeration(
    name="CommunicationTopic",
    literals={
            
    }
)

ClaimTypeCodes: Enumeration = Enumeration(
    name="ClaimTypeCodes",
    literals={
            
    }
)

ExampleClaimSubTypeCodes: Enumeration = Enumeration(
    name="ExampleClaimSubTypeCodes",
    literals={
            
    }
)

ProcessPriorityCodes: Enumeration = Enumeration(
    name="ProcessPriorityCodes",
    literals={
            
    }
)

FundsReservationCodes: Enumeration = Enumeration(
    name="FundsReservationCodes",
    literals={
            
    }
)

ExampleRelatedClaimRelationshipCodes: Enumeration = Enumeration(
    name="ExampleRelatedClaimRelationshipCodes",
    literals={
            
    }
)

ClaimPayeeTypeCodes: Enumeration = Enumeration(
    name="ClaimPayeeTypeCodes",
    literals={
            
    }
)

ClaimCareTeamRoleCodes: Enumeration = Enumeration(
    name="ClaimCareTeamRoleCodes",
    literals={
            
    }
)

ExampleProviderQualificationCodes: Enumeration = Enumeration(
    name="ExampleProviderQualificationCodes",
    literals={
            
    }
)

ClaimInformationCategoryCodes: Enumeration = Enumeration(
    name="ClaimInformationCategoryCodes",
    literals={
            
    }
)

ExceptionCodes: Enumeration = Enumeration(
    name="ExceptionCodes",
    literals={
            
    }
)

MissingToothReasonCodes: Enumeration = Enumeration(
    name="MissingToothReasonCodes",
    literals={
            
    }
)

ExampleDiagnosisTypeCodes: Enumeration = Enumeration(
    name="ExampleDiagnosisTypeCodes",
    literals={
            
    }
)

ExampleDiagnosisOnAdmissionCodes: Enumeration = Enumeration(
    name="ExampleDiagnosisOnAdmissionCodes",
    literals={
            
    }
)

ExampleDiagnosisRelatedGroupCodes: Enumeration = Enumeration(
    name="ExampleDiagnosisRelatedGroupCodes",
    literals={
            
    }
)

ExampleProcedureTypeCodes: Enumeration = Enumeration(
    name="ExampleProcedureTypeCodes",
    literals={
            
    }
)

IcD10ProcedureCodes: Enumeration = Enumeration(
    name="IcD10ProcedureCodes",
    literals={
            
    }
)

V3ActIncidentCode: Enumeration = Enumeration(
    name="V3ActIncidentCode",
    literals={
            
    }
)

ExampleRevenueCenterCodes: Enumeration = Enumeration(
    name="ExampleRevenueCenterCodes",
    literals={
            
    }
)

BenefitCategoryCodes: Enumeration = Enumeration(
    name="BenefitCategoryCodes",
    literals={
            
    }
)

UsclsCodes: Enumeration = Enumeration(
    name="UsclsCodes",
    literals={
            
    }
)

ModifierTypeCodes: Enumeration = Enumeration(
    name="ModifierTypeCodes",
    literals={
            
    }
)

ExampleProgramReasonCodes: Enumeration = Enumeration(
    name="ExampleProgramReasonCodes",
    literals={
            
    }
)

ExampleServicePlaceCodes: Enumeration = Enumeration(
    name="ExampleServicePlaceCodes",
    literals={
            
    }
)

OralSiteCodes: Enumeration = Enumeration(
    name="OralSiteCodes",
    literals={
            
    }
)

SurfaceCodes: Enumeration = Enumeration(
    name="SurfaceCodes",
    literals={
            
    }
)

AdjudicationValueCodes: Enumeration = Enumeration(
    name="AdjudicationValueCodes",
    literals={
            
    }
)

AdjudicationReasonCodes: Enumeration = Enumeration(
    name="AdjudicationReasonCodes",
    literals={
            
    }
)

ExamplePaymentTypeCodes: Enumeration = Enumeration(
    name="ExamplePaymentTypeCodes",
    literals={
            
    }
)

PaymentAdjustmentReasonCodes: Enumeration = Enumeration(
    name="PaymentAdjustmentReasonCodes",
    literals={
            
    }
)

FormCodes: Enumeration = Enumeration(
    name="FormCodes",
    literals={
            
    }
)

V3ActReason: Enumeration = Enumeration(
    name="V3ActReason",
    literals={
            
    }
)

AdjudicationErrorCodes: Enumeration = Enumeration(
    name="AdjudicationErrorCodes",
    literals={
            
    }
)

ServiceProvisionConditions: Enumeration = Enumeration(
    name="ServiceProvisionConditions",
    literals={
            
    }
)

Program: Enumeration = Enumeration(
    name="Program",
    literals={
            
    }
)

ReferralMethod: Enumeration = Enumeration(
    name="ReferralMethod",
    literals={
            
    }
)

SnomedctMorphologicAbnormalities: Enumeration = Enumeration(
    name="SnomedctMorphologicAbnormalities",
    literals={
            
    }
)

TaskCode: Enumeration = Enumeration(
    name="TaskCode",
    literals={
            
    }
)

QuestionnaireQuestionCodes: Enumeration = Enumeration(
    name="QuestionnaireQuestionCodes",
    literals={
            
    }
)

QuestionnaireAnswerCodes: Enumeration = Enumeration(
    name="QuestionnaireAnswerCodes",
    literals={
            
    }
)

NetworkTypeCodes: Enumeration = Enumeration(
    name="NetworkTypeCodes",
    literals={
            
    }
)

UnitTypeCodes: Enumeration = Enumeration(
    name="UnitTypeCodes",
    literals={
            
    }
)

BenefitTermCodes: Enumeration = Enumeration(
    name="BenefitTermCodes",
    literals={
            
    }
)

BenefitTypeCodes: Enumeration = Enumeration(
    name="BenefitTypeCodes",
    literals={
            
    }
)

VitalSigns: Enumeration = Enumeration(
    name="VitalSigns",
    literals={
            EnumerationLiteral(name="_84806"),
			EnumerationLiteral(name="_84624"),
			EnumerationLiteral(name="_84780"),
			EnumerationLiteral(name="_853531"),
			EnumerationLiteral(name="_92791"),
			EnumerationLiteral(name="_88674"),
			EnumerationLiteral(name="_27086"),
			EnumerationLiteral(name="_83105"),
			EnumerationLiteral(name="_83022"),
			EnumerationLiteral(name="_98434"),
			EnumerationLiteral(name="_294637"),
			EnumerationLiteral(name="_391565"),
			EnumerationLiteral(name="_853549")
    }
)

DeviceMetricAndComponentTypes: Enumeration = Enumeration(
    name="DeviceMetricAndComponentTypes",
    literals={
            
    }
)

FlagCategory: Enumeration = Enumeration(
    name="FlagCategory",
    literals={
            
    }
)

FlagCode: Enumeration = Enumeration(
    name="FlagCode",
    literals={
            
    }
)

ImmunizationEvaluationTargetDiseaseCodes: Enumeration = Enumeration(
    name="ImmunizationEvaluationTargetDiseaseCodes",
    literals={
            EnumerationLiteral(name="_1857005"),
			EnumerationLiteral(name="_397430003"),
			EnumerationLiteral(name="_14189004"),
			EnumerationLiteral(name="_36989005"),
			EnumerationLiteral(name="_36653000"),
			EnumerationLiteral(name="_76902006"),
			EnumerationLiteral(name="_709410003"),
			EnumerationLiteral(name="_27836007"),
			EnumerationLiteral(name="_398102009")
    }
)

ImmunizationStatusReasonCodes: Enumeration = Enumeration(
    name="ImmunizationStatusReasonCodes",
    literals={
            EnumerationLiteral(name="immune"),
			EnumerationLiteral(name="medprec"),
			EnumerationLiteral(name="ostock"),
			EnumerationLiteral(name="patobj")
    }
)

VaccineAdministeredValueSet: Enumeration = Enumeration(
    name="VaccineAdministeredValueSet",
    literals={
            
    }
)

ImmunizationOriginCodes: Enumeration = Enumeration(
    name="ImmunizationOriginCodes",
    literals={
            EnumerationLiteral(name="provider"),
			EnumerationLiteral(name="record"),
			EnumerationLiteral(name="recall"),
			EnumerationLiteral(name="school")
    }
)

CodesForImmunizationSiteOfAdministration: Enumeration = Enumeration(
    name="CodesForImmunizationSiteOfAdministration",
    literals={
            EnumerationLiteral(name="la"),
			EnumerationLiteral(name="ra")
    }
)

AdverseEventSeriousness: Enumeration = Enumeration(
    name="AdverseEventSeriousness",
    literals={
            
    }
)

AdverseEventCausalityAssessment: Enumeration = Enumeration(
    name="AdverseEventCausalityAssessment",
    literals={
            
    }
)

ImmunizationRouteCodes: Enumeration = Enumeration(
    name="ImmunizationRouteCodes",
    literals={
            EnumerationLiteral(name="im"),
			EnumerationLiteral(name="nasinhlc"),
			EnumerationLiteral(name="ivinj"),
			EnumerationLiteral(name="idinj"),
			EnumerationLiteral(name="po"),
			EnumerationLiteral(name="sq"),
			EnumerationLiteral(name="trnsderm")
    }
)

AdverseEventCausalityMethod: Enumeration = Enumeration(
    name="AdverseEventCausalityMethod",
    literals={
            
    }
)

SynthesisType: Enumeration = Enumeration(
    name="SynthesisType",
    literals={
            
    }
)

StudyType: Enumeration = Enumeration(
    name="StudyType",
    literals={
            
    }
)

RiskEstimateType: Enumeration = Enumeration(
    name="RiskEstimateType",
    literals={
            
    }
)

PrecisionEstimateType: Enumeration = Enumeration(
    name="PrecisionEstimateType",
    literals={
            
    }
)

QualityOfEvidenceRating: Enumeration = Enumeration(
    name="QualityOfEvidenceRating",
    literals={
            
    }
)

CertaintySubcomponentType: Enumeration = Enumeration(
    name="CertaintySubcomponentType",
    literals={
            
    }
)

ImmunizationFunctionCodes: Enumeration = Enumeration(
    name="ImmunizationFunctionCodes",
    literals={
            EnumerationLiteral(name="op"),
			EnumerationLiteral(name="ap")
    }
)

ImmunizationReasonCodes: Enumeration = Enumeration(
    name="ImmunizationReasonCodes",
    literals={
            EnumerationLiteral(name="_429060002"),
			EnumerationLiteral(name="_281657000")
    }
)

ImmunizationSubpotentReason: Enumeration = Enumeration(
    name="ImmunizationSubpotentReason",
    literals={
            
    }
)

ImmunizationProgramEligibility: Enumeration = Enumeration(
    name="ImmunizationProgramEligibility",
    literals={
            
    }
)

ImmunizationFundingSource: Enumeration = Enumeration(
    name="ImmunizationFundingSource",
    literals={
            
    }
)

ImmunizationTargetDiseaseCodes: Enumeration = Enumeration(
    name="ImmunizationTargetDiseaseCodes",
    literals={
            EnumerationLiteral(name="_1857005"),
			EnumerationLiteral(name="_397430003"),
			EnumerationLiteral(name="_14189004"),
			EnumerationLiteral(name="_36989005"),
			EnumerationLiteral(name="_36653000"),
			EnumerationLiteral(name="_76902006"),
			EnumerationLiteral(name="_709410003"),
			EnumerationLiteral(name="_27836007"),
			EnumerationLiteral(name="_398102009")
    }
)

ImmunizationEvaluationDoseStatusCodes: Enumeration = Enumeration(
    name="ImmunizationEvaluationDoseStatusCodes",
    literals={
            
    }
)

ImmunizationEvaluationDoseStatusReasonCodes: Enumeration = Enumeration(
    name="ImmunizationEvaluationDoseStatusReasonCodes",
    literals={
            
    }
)

OperationOutcomeCodes: Enumeration = Enumeration(
    name="OperationOutcomeCodes",
    literals={
            
    }
)

PaymentTypeCodes: Enumeration = Enumeration(
    name="PaymentTypeCodes",
    literals={
            
    }
)

PractitionerRole: Enumeration = Enumeration(
    name="PractitionerRole",
    literals={
            
    }
)

FamilyHistoryAbsentReason: Enumeration = Enumeration(
    name="FamilyHistoryAbsentReason",
    literals={
            
    }
)

V3FamilyMember: Enumeration = Enumeration(
    name="V3FamilyMember",
    literals={
            
    }
)

ConditionOutcomeCodes: Enumeration = Enumeration(
    name="ConditionOutcomeCodes",
    literals={
            
    }
)

OrganizationAffiliationRole: Enumeration = Enumeration(
    name="OrganizationAffiliationRole",
    literals={
            
    }
)

AdverseEventCategory: Enumeration = Enumeration(
    name="AdverseEventCategory",
    literals={
            
    }
)

SnomedctClinicalFindingsA: Enumeration = Enumeration(
    name="SnomedctClinicalFindingsA",
    literals={
            
    }
)

CertaintySubcomponentRating: Enumeration = Enumeration(
    name="CertaintySubcomponentRating",
    literals={
            
    }
)

TestScriptProfileOriginType: Enumeration = Enumeration(
    name="TestScriptProfileOriginType",
    literals={
            
    }
)

TestScriptProfileDestinationType: Enumeration = Enumeration(
    name="TestScriptProfileDestinationType",
    literals={
            
    }
)

RestfulSecurityService: Enumeration = Enumeration(
    name="RestfulSecurityService",
    literals={
            
    }
)

MessageTransport: Enumeration = Enumeration(
    name="MessageTransport",
    literals={
            
    }
)

MessageEvent: Enumeration = Enumeration(
    name="MessageEvent",
    literals={
            
    }
)

TestScriptOperationCode: Enumeration = Enumeration(
    name="TestScriptOperationCode",
    literals={
            
    }
)

ExampleMessageReasonCodes: Enumeration = Enumeration(
    name="ExampleMessageReasonCodes",
    literals={
            
    }
)

PaymentStatusCodes: Enumeration = Enumeration(
    name="PaymentStatusCodes",
    literals={
            
    }
)

FhirDocumentTypeCodes: Enumeration = Enumeration(
    name="FhirDocumentTypeCodes",
    literals={
            
    }
)

DocumentSectionCodes: Enumeration = Enumeration(
    name="DocumentSectionCodes",
    literals={
            EnumerationLiteral(name="_113696"),
			EnumerationLiteral(name="_578526"),
			EnumerationLiteral(name="_101543"),
			EnumerationLiteral(name="_101576"),
			EnumerationLiteral(name="_101600"),
			EnumerationLiteral(name="_101642"),
			EnumerationLiteral(name="_101832"),
			EnumerationLiteral(name="_101840"),
			EnumerationLiteral(name="_101873"),
			EnumerationLiteral(name="_102103"),
			EnumerationLiteral(name="_102160"),
			EnumerationLiteral(name="_102186"),
			EnumerationLiteral(name="_102186A"),
			EnumerationLiteral(name="_102236"),
			EnumerationLiteral(name="_102228"),
			EnumerationLiteral(name="_113290"),
			EnumerationLiteral(name="_113480"),
			EnumerationLiteral(name="_518480"),
			EnumerationLiteral(name="_551093"),
			EnumerationLiteral(name="_114934"),
			EnumerationLiteral(name="_551226"),
			EnumerationLiteral(name="_115352"),
			EnumerationLiteral(name="_115378"),
			EnumerationLiteral(name="_187765"),
			EnumerationLiteral(name="_188417"),
			EnumerationLiteral(name="_292995"),
			EnumerationLiteral(name="_295451"),
			EnumerationLiteral(name="_295493"),
			EnumerationLiteral(name="_295543"),
			EnumerationLiteral(name="_297622"),
			EnumerationLiteral(name="_309542"),
			EnumerationLiteral(name="_423442"),
			EnumerationLiteral(name="_423467"),
			EnumerationLiteral(name="_423483"),
			EnumerationLiteral(name="_423491"),
			EnumerationLiteral(name="_462408"),
			EnumerationLiteral(name="_462416"),
			EnumerationLiteral(name="_462648"),
			EnumerationLiteral(name="_474205"),
			EnumerationLiteral(name="_475194"),
			EnumerationLiteral(name="_487652"),
			EnumerationLiteral(name="_487686"),
			EnumerationLiteral(name="_597682"),
			EnumerationLiteral(name="_597690"),
			EnumerationLiteral(name="_597708"),
			EnumerationLiteral(name="_597716"),
			EnumerationLiteral(name="_597724"),
			EnumerationLiteral(name="_597732"),
			EnumerationLiteral(name="_597757"),
			EnumerationLiteral(name="_597765"),
			EnumerationLiteral(name="_611491"),
			EnumerationLiteral(name="_611509"),
			EnumerationLiteral(name="_611509B"),
			EnumerationLiteral(name="_697300"),
			EnumerationLiteral(name="_86488"),
			EnumerationLiteral(name="_86538"),
			EnumerationLiteral(name="_87163")
    }
)

SupplyType: Enumeration = Enumeration(
    name="SupplyType",
    literals={
            
    }
)

SnomedctSupplyItem: Enumeration = Enumeration(
    name="SnomedctSupplyItem",
    literals={
            
    }
)

SupplyRequestReason: Enumeration = Enumeration(
    name="SupplyRequestReason",
    literals={
            
    }
)

EvidenceVariantState: Enumeration = Enumeration(
    name="EvidenceVariantState",
    literals={
            
    }
)

EffectEstimateType: Enumeration = Enumeration(
    name="EffectEstimateType",
    literals={
            
    }
)

InsurancePlanType: Enumeration = Enumeration(
    name="InsurancePlanType",
    literals={
            
    }
)

ProvenanceHistoryRecordActivityCodes: Enumeration = Enumeration(
    name="ProvenanceHistoryRecordActivityCodes",
    literals={
            EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="abort"),
			EnumerationLiteral(name="hold"),
			EnumerationLiteral(name="create"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="release"),
			EnumerationLiteral(name="cancel"),
			EnumerationLiteral(name="activate"),
			EnumerationLiteral(name="suspend"),
			EnumerationLiteral(name="resume"),
			EnumerationLiteral(name="complete"),
			EnumerationLiteral(name="nullify"),
			EnumerationLiteral(name="obsolete"),
			EnumerationLiteral(name="reactivate")
    }
)

ImmunizationRecommendationStatusCodes: Enumeration = Enumeration(
    name="ImmunizationRecommendationStatusCodes",
    literals={
            
    }
)

Chromosomehuman: Enumeration = Enumeration(
    name="Chromosomehuman",
    literals={
            
    }
)

Ensembl: Enumeration = Enumeration(
    name="Ensembl",
    literals={
            
    }
)

FdAStandardSequence: Enumeration = Enumeration(
    name="FdAStandardSequence",
    literals={
            
    }
)

FdAMethod: Enumeration = Enumeration(
    name="FdAMethod",
    literals={
            
    }
)

AllergyIntoleranceSubstanceProductConditionAndNegationCodes: Enumeration = Enumeration(
    name="AllergyIntoleranceSubstanceProductConditionAndNegationCodes",
    literals={
            
    }
)

CatalogType: Enumeration = Enumeration(
    name="CatalogType",
    literals={
            
    }
)

ImmunizationRecommendationTargetDiseaseCodes: Enumeration = Enumeration(
    name="ImmunizationRecommendationTargetDiseaseCodes",
    literals={
            EnumerationLiteral(name="_27836007"),
			EnumerationLiteral(name="_398102009"),
			EnumerationLiteral(name="_1857005"),
			EnumerationLiteral(name="_397430003"),
			EnumerationLiteral(name="_14189004"),
			EnumerationLiteral(name="_36989005"),
			EnumerationLiteral(name="_36653000"),
			EnumerationLiteral(name="_76902006"),
			EnumerationLiteral(name="_709410003")
    }
)

ImmunizationRecommendationReasonCodes: Enumeration = Enumeration(
    name="ImmunizationRecommendationReasonCodes",
    literals={
            EnumerationLiteral(name="_77176002"),
			EnumerationLiteral(name="_77386006")
    }
)

TextureModifierCodes: Enumeration = Enumeration(
    name="TextureModifierCodes",
    literals={
            EnumerationLiteral(name="_228053002"),
			EnumerationLiteral(name="_439091000124107"),
			EnumerationLiteral(name="_228049004"),
			EnumerationLiteral(name="_441881000124103"),
			EnumerationLiteral(name="_441761000124103"),
			EnumerationLiteral(name="_441751000124100"),
			EnumerationLiteral(name="_228059003"),
			EnumerationLiteral(name="_441791000124106"),
			EnumerationLiteral(name="_228055009"),
			EnumerationLiteral(name="_228056005"),
			EnumerationLiteral(name="_441771000124105"),
			EnumerationLiteral(name="_228057001"),
			EnumerationLiteral(name="_228058006"),
			EnumerationLiteral(name="_228060008")
    }
)

ImmunizationRecommendationDateCriterionCodes: Enumeration = Enumeration(
    name="ImmunizationRecommendationDateCriterionCodes",
    literals={
            EnumerationLiteral(name="_309815"),
			EnumerationLiteral(name="_309807"),
			EnumerationLiteral(name="_597773"),
			EnumerationLiteral(name="_597781")
    }
)

Need: Enumeration = Enumeration(
    name="Need",
    literals={
            
    }
)

Validationtype: Enumeration = Enumeration(
    name="Validationtype",
    literals={
            
    }
)

Validationprocess: Enumeration = Enumeration(
    name="Validationprocess",
    literals={
            
    }
)

Failureaction: Enumeration = Enumeration(
    name="Failureaction",
    literals={
            
    }
)

Primarysourcetype: Enumeration = Enumeration(
    name="Primarysourcetype",
    literals={
            
    }
)

Verificationresultcommunicationmethod: Enumeration = Enumeration(
    name="Verificationresultcommunicationmethod",
    literals={
            
    }
)

Validationstatus: Enumeration = Enumeration(
    name="Validationstatus",
    literals={
            
    }
)

Canpushupdates: Enumeration = Enumeration(
    name="Canpushupdates",
    literals={
            
    }
)

Pushtypeavailable: Enumeration = Enumeration(
    name="Pushtypeavailable",
    literals={
            
    }
)

FoodTypeCodes: Enumeration = Enumeration(
    name="FoodTypeCodes",
    literals={
            
    }
)

DietCodes: Enumeration = Enumeration(
    name="DietCodes",
    literals={
            
    }
)

NutrientModifierCodes: Enumeration = Enumeration(
    name="NutrientModifierCodes",
    literals={
            EnumerationLiteral(name="_33463005"),
			EnumerationLiteral(name="_39972003"),
			EnumerationLiteral(name="_88480006")
    }
)

TextureModifiedFoodTypeCodes: Enumeration = Enumeration(
    name="TextureModifiedFoodTypeCodes",
    literals={
            EnumerationLiteral(name="_226760005"),
			EnumerationLiteral(name="_226887002"),
			EnumerationLiteral(name="_102263004"),
			EnumerationLiteral(name="_74242007"),
			EnumerationLiteral(name="_227415002"),
			EnumerationLiteral(name="_255620007"),
			EnumerationLiteral(name="_28647000"),
			EnumerationLiteral(name="_22836000"),
			EnumerationLiteral(name="_72511004"),
			EnumerationLiteral(name="_264331002"),
			EnumerationLiteral(name="_227518002"),
			EnumerationLiteral(name="_44027008"),
			EnumerationLiteral(name="_226529007"),
			EnumerationLiteral(name="_227210005")
    }
)

FluidConsistencyTypeCodes: Enumeration = Enumeration(
    name="FluidConsistencyTypeCodes",
    literals={
            EnumerationLiteral(name="_439031000124108"),
			EnumerationLiteral(name="_439021000124105"),
			EnumerationLiteral(name="_439041000124103"),
			EnumerationLiteral(name="_439081000124109")
    }
)

SupplementTypeCodes: Enumeration = Enumeration(
    name="SupplementTypeCodes",
    literals={
            EnumerationLiteral(name="_442991000124104"),
			EnumerationLiteral(name="_443011000124100"),
			EnumerationLiteral(name="_442961000124107"),
			EnumerationLiteral(name="_442951000124105"),
			EnumerationLiteral(name="_442941000124108"),
			EnumerationLiteral(name="_442921000124101"),
			EnumerationLiteral(name="_442901000124106"),
			EnumerationLiteral(name="_443031000124106"),
			EnumerationLiteral(name="_443051000124104"),
			EnumerationLiteral(name="_442911000124109"),
			EnumerationLiteral(name="_443021000124108"),
			EnumerationLiteral(name="_442971000124100"),
			EnumerationLiteral(name="_442981000124102"),
			EnumerationLiteral(name="_441591000124103"),
			EnumerationLiteral(name="_441601000124106"),
			EnumerationLiteral(name="_443351000124102"),
			EnumerationLiteral(name="_443771000124106"),
			EnumerationLiteral(name="_441671000124100"),
			EnumerationLiteral(name="_442931000124103"),
			EnumerationLiteral(name="_444331000124106"),
			EnumerationLiteral(name="_443361000124100"),
			EnumerationLiteral(name="_443391000124108"),
			EnumerationLiteral(name="_443401000124105"),
			EnumerationLiteral(name="_443491000124103"),
			EnumerationLiteral(name="_443501000124106"),
			EnumerationLiteral(name="_443421000124100"),
			EnumerationLiteral(name="_443471000124104"),
			EnumerationLiteral(name="_444431000124104"),
			EnumerationLiteral(name="_443451000124109"),
			EnumerationLiteral(name="_444321000124108"),
			EnumerationLiteral(name="_441561000124106"),
			EnumerationLiteral(name="_443461000124106"),
			EnumerationLiteral(name="_441531000124102"),
			EnumerationLiteral(name="_443561000124107"),
			EnumerationLiteral(name="_443481000124101"),
			EnumerationLiteral(name="_441571000124104"),
			EnumerationLiteral(name="_443111000124101"),
			EnumerationLiteral(name="_443431000124102"),
			EnumerationLiteral(name="_443411000124108"),
			EnumerationLiteral(name="_444361000124102"),
			EnumerationLiteral(name="_444401000124107"),
			EnumerationLiteral(name="_444381000124107"),
			EnumerationLiteral(name="_444371000124109"),
			EnumerationLiteral(name="_443441000124107"),
			EnumerationLiteral(name="_442651000124102")
    }
)

EnteralFormulaTypeCodes: Enumeration = Enumeration(
    name="EnteralFormulaTypeCodes",
    literals={
            EnumerationLiteral(name="_442961000124107"),
			EnumerationLiteral(name="_442951000124105"),
			EnumerationLiteral(name="_442941000124108"),
			EnumerationLiteral(name="_443031000124106"),
			EnumerationLiteral(name="_443051000124104"),
			EnumerationLiteral(name="_442911000124109"),
			EnumerationLiteral(name="_443021000124108"),
			EnumerationLiteral(name="_442971000124100"),
			EnumerationLiteral(name="_442981000124102"),
			EnumerationLiteral(name="_442991000124104"),
			EnumerationLiteral(name="_443111000124101"),
			EnumerationLiteral(name="_443011000124100"),
			EnumerationLiteral(name="_443431000124102"),
			EnumerationLiteral(name="_443411000124108"),
			EnumerationLiteral(name="_442921000124101"),
			EnumerationLiteral(name="_442931000124103"),
			EnumerationLiteral(name="_443361000124100"),
			EnumerationLiteral(name="_443401000124105"),
			EnumerationLiteral(name="_443491000124103"),
			EnumerationLiteral(name="_443501000124106"),
			EnumerationLiteral(name="_443421000124100"),
			EnumerationLiteral(name="_443471000124104"),
			EnumerationLiteral(name="_444431000124104"),
			EnumerationLiteral(name="_443451000124109"),
			EnumerationLiteral(name="_441561000124106"),
			EnumerationLiteral(name="_443461000124106"),
			EnumerationLiteral(name="_441531000124102"),
			EnumerationLiteral(name="_443561000124107"),
			EnumerationLiteral(name="_443481000124101"),
			EnumerationLiteral(name="_441571000124104"),
			EnumerationLiteral(name="_441591000124103"),
			EnumerationLiteral(name="_441601000124106"),
			EnumerationLiteral(name="_443351000124102"),
			EnumerationLiteral(name="_443771000124106"),
			EnumerationLiteral(name="_441671000124100"),
			EnumerationLiteral(name="_442651000124102")
    }
)

EnteralFormulaAdditiveTypeCode: Enumeration = Enumeration(
    name="EnteralFormulaAdditiveTypeCode",
    literals={
            
    }
)

EnteralRouteCodes: Enumeration = Enumeration(
    name="EnteralRouteCodes",
    literals={
            EnumerationLiteral(name="po"),
			EnumerationLiteral(name="eft"),
			EnumerationLiteral(name="entinstl"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="ngt"),
			EnumerationLiteral(name="ogt"),
			EnumerationLiteral(name="gjt"),
			EnumerationLiteral(name="jjtinstl"),
			EnumerationLiteral(name="ojj")
    }
)

SnomedctDrugTherapyStatusCodes: Enumeration = Enumeration(
    name="SnomedctDrugTherapyStatusCodes",
    literals={
            
    }
)

MedicationStatusCodes: Enumeration = Enumeration(
    name="MedicationStatusCodes",
    literals={
            
    }
)

AuditEventId: Enumeration = Enumeration(
    name="AuditEventId",
    literals={
            EnumerationLiteral(name="_110106"),
			EnumerationLiteral(name="_110107"),
			EnumerationLiteral(name="_110108"),
			EnumerationLiteral(name="_110109"),
			EnumerationLiteral(name="_110110"),
			EnumerationLiteral(name="_110100"),
			EnumerationLiteral(name="_110101"),
			EnumerationLiteral(name="_110102"),
			EnumerationLiteral(name="_110103"),
			EnumerationLiteral(name="_110104"),
			EnumerationLiteral(name="_110105"),
			EnumerationLiteral(name="_110111"),
			EnumerationLiteral(name="_110112"),
			EnumerationLiteral(name="_110113"),
			EnumerationLiteral(name="_110114")
    }
)

AuditEventSubType: Enumeration = Enumeration(
    name="AuditEventSubType",
    literals={
            EnumerationLiteral(name="_110132"),
			EnumerationLiteral(name="_110133"),
			EnumerationLiteral(name="_110120"),
			EnumerationLiteral(name="_110121"),
			EnumerationLiteral(name="_110122"),
			EnumerationLiteral(name="_110123"),
			EnumerationLiteral(name="_110124"),
			EnumerationLiteral(name="_110125"),
			EnumerationLiteral(name="_110126"),
			EnumerationLiteral(name="_110127"),
			EnumerationLiteral(name="_110128"),
			EnumerationLiteral(name="_110129"),
			EnumerationLiteral(name="_110130"),
			EnumerationLiteral(name="_110131"),
			EnumerationLiteral(name="_110134"),
			EnumerationLiteral(name="_110135"),
			EnumerationLiteral(name="_110136"),
			EnumerationLiteral(name="_110137"),
			EnumerationLiteral(name="_110138"),
			EnumerationLiteral(name="_110139"),
			EnumerationLiteral(name="_110140"),
			EnumerationLiteral(name="_110141"),
			EnumerationLiteral(name="_110142")
    }
)

ParticipationRoleType: Enumeration = Enumeration(
    name="ParticipationRoleType",
    literals={
            EnumerationLiteral(name="affl"),
			EnumerationLiteral(name="agnt"),
			EnumerationLiteral(name="assigned"),
			EnumerationLiteral(name="claim"),
			EnumerationLiteral(name="amender"),
			EnumerationLiteral(name="coauth"),
			EnumerationLiteral(name="cont"),
			EnumerationLiteral(name="evtwit"),
			EnumerationLiteral(name="primauth"),
			EnumerationLiteral(name="reviewer"),
			EnumerationLiteral(name="source"),
			EnumerationLiteral(name="trans"),
			EnumerationLiteral(name="valid"),
			EnumerationLiteral(name="verf"),
			EnumerationLiteral(name="dpowatt"),
			EnumerationLiteral(name="excest"),
			EnumerationLiteral(name="covpty"),
			EnumerationLiteral(name="depen"),
			EnumerationLiteral(name="econ"),
			EnumerationLiteral(name="emp"),
			EnumerationLiteral(name="guard"),
			EnumerationLiteral(name="invsbj"),
			EnumerationLiteral(name="named"),
			EnumerationLiteral(name="nok"),
			EnumerationLiteral(name="pat"),
			EnumerationLiteral(name="prov"),
			EnumerationLiteral(name="not_"),
			EnumerationLiteral(name="classifier"),
			EnumerationLiteral(name="consenter"),
			EnumerationLiteral(name="conswit"),
			EnumerationLiteral(name="copart"),
			EnumerationLiteral(name="declassifier"),
			EnumerationLiteral(name="delegatee"),
			EnumerationLiteral(name="delegator"),
			EnumerationLiteral(name="downgrder"),
			EnumerationLiteral(name="_110150"),
			EnumerationLiteral(name="_110151"),
			EnumerationLiteral(name="_110152"),
			EnumerationLiteral(name="grantee"),
			EnumerationLiteral(name="grantor"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="guadltm"),
			EnumerationLiteral(name="hpowatt"),
			EnumerationLiteral(name="intprter"),
			EnumerationLiteral(name="powatt"),
			EnumerationLiteral(name="resprsn"),
			EnumerationLiteral(name="spowatt"),
			EnumerationLiteral(name="aucg"),
			EnumerationLiteral(name="aulr"),
			EnumerationLiteral(name="autm"),
			EnumerationLiteral(name="auwa"),
			EnumerationLiteral(name="promsk"),
			EnumerationLiteral(name="aut"),
			EnumerationLiteral(name="cst"),
			EnumerationLiteral(name="inf"),
			EnumerationLiteral(name="ircp"),
			EnumerationLiteral(name="la"),
			EnumerationLiteral(name="ircpa"),
			EnumerationLiteral(name="trc"),
			EnumerationLiteral(name="wit"),
			EnumerationLiteral(name="_110153"),
			EnumerationLiteral(name="_110154"),
			EnumerationLiteral(name="_110155")
    }
)

MedicationKnowledgeCharacteristicCodes: Enumeration = Enumeration(
    name="MedicationKnowledgeCharacteristicCodes",
    literals={
            
    }
)

CoverageEligibilityResponseAuthSupportCodes: Enumeration = Enumeration(
    name="CoverageEligibilityResponseAuthSupportCodes",
    literals={
            
    }
)

MediaTypeCode: Enumeration = Enumeration(
    name="MediaTypeCode",
    literals={
            EnumerationLiteral(name="_110030"),
			EnumerationLiteral(name="_110031"),
			EnumerationLiteral(name="_110032"),
			EnumerationLiteral(name="_110033"),
			EnumerationLiteral(name="_110034"),
			EnumerationLiteral(name="_110035"),
			EnumerationLiteral(name="_110036"),
			EnumerationLiteral(name="_110037"),
			EnumerationLiteral(name="_110010"),
			EnumerationLiteral(name="_110038")
    }
)

AuditEventSourceType: Enumeration = Enumeration(
    name="AuditEventSourceType",
    literals={
            
    }
)

AuditEventEntityType: Enumeration = Enumeration(
    name="AuditEventEntityType",
    literals={
            
    }
)

AuditEventEntityRole: Enumeration = Enumeration(
    name="AuditEventEntityRole",
    literals={
            
    }
)

ObjectLifecycleEvents: Enumeration = Enumeration(
    name="ObjectLifecycleEvents",
    literals={
            
    }
)

BasicResourceTypes: Enumeration = Enumeration(
    name="BasicResourceTypes",
    literals={
            
    }
)

ExampleVisionPrescriptionProductCodes: Enumeration = Enumeration(
    name="ExampleVisionPrescriptionProductCodes",
    literals={
            
    }
)

MedicationDispenseStatusReasonCodes: Enumeration = Enumeration(
    name="MedicationDispenseStatusReasonCodes",
    literals={
            
    }
)

MedicationDispenseCategoryCodes: Enumeration = Enumeration(
    name="MedicationDispenseCategoryCodes",
    literals={
            
    }
)

MedicationDispensePerformerFunctionCodes: Enumeration = Enumeration(
    name="MedicationDispensePerformerFunctionCodes",
    literals={
            
    }
)

V3ActPharmacySupplyType: Enumeration = Enumeration(
    name="V3ActPharmacySupplyType",
    literals={
            
    }
)

MedicationKnowledgePackageTypeCodes: Enumeration = Enumeration(
    name="MedicationKnowledgePackageTypeCodes",
    literals={
            
    }
)

# Classes

# Domain Model
domain_model = DomainModel(
    name="valueSets",
    types={DataType, ResourceType, IdentifierTypeCodes, UsageContextType, ContextOfUseValueSet, JurisdictionValueSet, DefinitionUseCodes, FhirDefinedType, LoincCodes, CommonLanguages, SignatureTypeCodes, V2036027, TimingAbbreviation, SubjectType, DesignationUse, ExpressionLanguage, SnomedctAdditionalDosageInstructions, SnomedctMedicationAsNeededReasonCodes, SnomedctAnatomicalStructureForAdministrationSiteCodes, SnomedctRouteCodes, SnomedctAdministrationMethodCodes, DoseAndRateType, AllSecurityLabels, CommonTags, OrganizationType, ContactEntityType, EndpointConnectionType, EndpointPayloadType, LibraryType, DefinitionTopic, MeasureScoring, CompositeMeasureScoring, GoalPriority, GoalStartEvent, MeasureType, MeasurePopulationType, MeasureDataUsage, MaritalStatusCodes, PatientContactRelationship, ExampleUseCodesForList, V3ActEncounterCode, EncounterType, ServiceType, V3ActPriority, EpisodeOfCareType, ConditionCategoryCodes, ConditionDiagnosisSeverity, ConditionProblemDiagnosisCodes, SnomedctBodyStructures, ConditionStage, InvestigationType, PlanDefinitionType, GoalCategory, SnomedctClinicalFindings, ActionParticipantRole, ActionType, CarePlanCategory, CareTeamCategory, ParticipantRoles, GoalAchievementStatus, CarePlanActivityOutcome, AppointmentCancellationReason, ServiceCategory, PracticeSettingCodeValueSet, V20276, EncounterReasonCodes, ProcedureCodesSnomedcT, V20116, V3ServiceDeliveryLocationRoleType, LocationType, SnomedctMedicationCodes, V20487, PreparePatient, SpecimenCollection, ContainerMaterials, SpecimenContainerType, ContainerCap, V20371, RejectionCriterion, HandlingConditionSet, ObservationCategoryCodes, ObservationMethods, UcumCodes, ObservationReferenceRangeMeaningCodes, ObservationReferenceRangeAppliesToCodes, ServiceRequestCategoryCodes, ServiceRequestOrderDetailsCodes, ProcedureReasonCodes, CoverageTypeAndSelfPayCodes, SubscriberRelationshipCodes, CoverageClassCodes, CoverageCopayTypeCodes, ExampleCoverageFinancialExceptionCodes, ContractResourceLegalStateCodes, ContractContentDerivationCodes, ContractResourceExpirationTypeCodes, ContractResourceScopeCodes, ContractTypeCodes, ContractSubtypeCodes, ContractResourceDefinitionTypeCodes, ContractResourceDefinitionSubtypeCodes, ContractTermTypeCodes, ContractTermSubtypeCodes, ContractResourceScopeCodesA, ContractResourceScopeCodesB, ContractResourceSecurityControlCodes, ContractResourcePartyRoleCodes, V3ActConsentDirective, ContractResourceDecisionModeCodes, ContractResourceAssetScopeCodes, ContractResourceAssetTypeCodes, ContractResourceAssetSubTypeCodes, ConsentContentClass, ContractResourceAssetContextCodes, ContractResourceAssetAvailiabilityCodes, ContractActionCodes, ContractActorRoleCodes, V3PurposeOfUse, ContractResourceActionStatusCodes, ProvenanceParticipantType, ProvenanceParticipantRole, PatientRelationshipType, ProvenanceActivityType, SecurityRoleType, ContractSignerTypeCodes, FhirSpecimenCollectionMethod, FhirDeviceStatusReason, DeviceType, V20916, SpecimenProcessingProcedure, SubstanceCategoryCodes, SubstanceCode, V20493, ParticipantType, SnomedctReasonMedicationNotGivenCodes, MedicationAdministrationCategoryCodes, MedicationAdministrationPerformerFunctionCodes, ReasonMedicationGivenCodes, MedicationRequestStatusReasonCodes, MedicationRequestCategoryCodes, ProcedurePerformerRoleCodes, MedicationRequestCourseOfTherapyCodes, V3ActSubstanceAdminSubstitutionCode, V3SubstanceAdminSubstitutionReason, DetectedIssueCategory, ManifestationAndSymptomCodes, DetectedIssueMitigationAction, FhirDeviceTypes, DeviceSafety, DataAbsentReason, ObservationInterpretationCodes, DocumentClassValueSet, DocumentReferenceFormatCodeSet, V3ActCode, FacilityTypeCodeValueSet, SpecialArrangements, DischargeDisposition, ClinicalImpressionPrognosis, RiskProbability, ConditionStageType, DiagnosisRole, AccountTypes, AdmitSource, V20092, Diet, SpecialCourtesy, ListOrderCodes, PatientMedicineChangeTypes, ListEmptyReasons, ResearchStudyPrimaryPurposeType, ResearchStudyPhase, ResearchStudyReasonStopped, ResearchStudyObjectiveType, ConsentScopeCodes, ConsentCategoryCodes, ConsentPolicyRuleCodes, ConsentActionCodes, ConsentContentCodes, ChargeItemCode, SnomedctFormCodes, IcD10Codes, DiagnosticServiceSectionCodes, LoincDiagnosticReportCodes, AcquisitionModality, ProcedureNotPerformedReasonSnomeDCT, ProcedureCategoryCodesSnomedcT, ProcedureOutcomeCodesSnomedcT, ProcedureFollowUpCodesSnomedcT, MediaType, MediaModality, MediaCollectionViewProjection, CommunicationNotDoneReason, ProcedureDeviceActionCodes, Laterality, ImagingStudySeriesPerformerFunction, BodystructureLocationQualifier, CommunicationCategory, V3ParticipationMode, CommunicationTopic, ClaimTypeCodes, ExampleClaimSubTypeCodes, ProcessPriorityCodes, FundsReservationCodes, ExampleRelatedClaimRelationshipCodes, ClaimPayeeTypeCodes, ClaimCareTeamRoleCodes, ExampleProviderQualificationCodes, ClaimInformationCategoryCodes, ExceptionCodes, MissingToothReasonCodes, ExampleDiagnosisTypeCodes, ExampleDiagnosisOnAdmissionCodes, ExampleDiagnosisRelatedGroupCodes, ExampleProcedureTypeCodes, IcD10ProcedureCodes, V3ActIncidentCode, ExampleRevenueCenterCodes, BenefitCategoryCodes, UsclsCodes, ModifierTypeCodes, ExampleProgramReasonCodes, ExampleServicePlaceCodes, OralSiteCodes, SurfaceCodes, AdjudicationValueCodes, AdjudicationReasonCodes, ExamplePaymentTypeCodes, PaymentAdjustmentReasonCodes, FormCodes, V3ActReason, AdjudicationErrorCodes, ServiceProvisionConditions, Program, ReferralMethod, SnomedctMorphologicAbnormalities, TaskCode, QuestionnaireQuestionCodes, QuestionnaireAnswerCodes, NetworkTypeCodes, UnitTypeCodes, BenefitTermCodes, BenefitTypeCodes, VitalSigns, DeviceMetricAndComponentTypes, FlagCategory, FlagCode, ImmunizationEvaluationTargetDiseaseCodes, ImmunizationStatusReasonCodes, VaccineAdministeredValueSet, ImmunizationOriginCodes, CodesForImmunizationSiteOfAdministration, AdverseEventSeriousness, AdverseEventCausalityAssessment, ImmunizationRouteCodes, AdverseEventCausalityMethod, SynthesisType, StudyType, RiskEstimateType, PrecisionEstimateType, QualityOfEvidenceRating, CertaintySubcomponentType, ImmunizationFunctionCodes, ImmunizationReasonCodes, ImmunizationSubpotentReason, ImmunizationProgramEligibility, ImmunizationFundingSource, ImmunizationTargetDiseaseCodes, ImmunizationEvaluationDoseStatusCodes, ImmunizationEvaluationDoseStatusReasonCodes, OperationOutcomeCodes, PaymentTypeCodes, PractitionerRole, FamilyHistoryAbsentReason, V3FamilyMember, ConditionOutcomeCodes, OrganizationAffiliationRole, AdverseEventCategory, SnomedctClinicalFindingsA, CertaintySubcomponentRating, TestScriptProfileOriginType, TestScriptProfileDestinationType, RestfulSecurityService, MessageTransport, MessageEvent, TestScriptOperationCode, ExampleMessageReasonCodes, PaymentStatusCodes, FhirDocumentTypeCodes, DocumentSectionCodes, SupplyType, SnomedctSupplyItem, SupplyRequestReason, EvidenceVariantState, EffectEstimateType, InsurancePlanType, ProvenanceHistoryRecordActivityCodes, ImmunizationRecommendationStatusCodes, Chromosomehuman, Ensembl, FdAStandardSequence, FdAMethod, AllergyIntoleranceSubstanceProductConditionAndNegationCodes, CatalogType, ImmunizationRecommendationTargetDiseaseCodes, ImmunizationRecommendationReasonCodes, TextureModifierCodes, ImmunizationRecommendationDateCriterionCodes, Need, Validationtype, Validationprocess, Failureaction, Primarysourcetype, Verificationresultcommunicationmethod, Validationstatus, Canpushupdates, Pushtypeavailable, FoodTypeCodes, DietCodes, NutrientModifierCodes, TextureModifiedFoodTypeCodes, FluidConsistencyTypeCodes, SupplementTypeCodes, EnteralFormulaTypeCodes, EnteralFormulaAdditiveTypeCode, EnteralRouteCodes, SnomedctDrugTherapyStatusCodes, MedicationStatusCodes, AuditEventId, AuditEventSubType, ParticipationRoleType, MedicationKnowledgeCharacteristicCodes, CoverageEligibilityResponseAuthSupportCodes, MediaTypeCode, AuditEventSourceType, AuditEventEntityType, AuditEventEntityRole, ObjectLifecycleEvents, BasicResourceTypes, ExampleVisionPrescriptionProductCodes, MedicationDispenseStatusReasonCodes, MedicationDispenseCategoryCodes, MedicationDispensePerformerFunctionCodes, V3ActPharmacySupplyType, MedicationKnowledgePackageTypeCodes},
    associations={},
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