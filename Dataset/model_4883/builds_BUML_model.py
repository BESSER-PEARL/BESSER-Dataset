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
TestCaseResult: Enumeration = Enumeration(
    name="TestCaseResult",
    literals={
            EnumerationLiteral(name="PASSED"),
			EnumerationLiteral(name="SKIPPED"),
			EnumerationLiteral(name="FAILED"),
			EnumerationLiteral(name="FIXED"),
			EnumerationLiteral(name="REGRESSION")
    }
)

# Classes
builds_StringToStringMap = Class(name="builds::StringToStringMap")
builds_User = Class(name="builds::User")
builds_BuildCause = Class(name="builds::BuildCause")
builds_BuildReference = Class(name="builds::BuildReference")
builds_BuildElement = Class(name="builds::BuildElement", is_abstract=True)
builds_Artifact = Class(name="builds::Artifact")
BuildElement = Class(name="BuildElement")
builds_Build = Class(name="builds::Build")
builds_ChangeSet = Class(name="builds::ChangeSet")
builds_BuildPlan = Class(name="builds::BuildPlan")
builds_BuildServer = Class(name="builds::BuildServer")
builds_TestResult = Class(name="builds::TestResult")
builds_ParameterDefinition = Class(name="builds::ParameterDefinition", is_abstract=True)
builds_HealthReport = Class(name="builds::HealthReport")
builds_BuildModel = Class(name="builds::BuildModel")
builds_ChoiceParameterDefinition = Class(name="builds::ChoiceParameterDefinition")
ParameterDefinition = Class(name="ParameterDefinition")
builds_BooleanParameterDefinition = Class(name="builds::BooleanParameterDefinition")
builds_FileParameterDefinition = Class(name="builds::FileParameterDefinition")
builds_PlanParameterDefinition = Class(name="builds::PlanParameterDefinition")
builds_PasswordParameterDefinition = Class(name="builds::PasswordParameterDefinition")
builds_BuildParameterDefinition = Class(name="builds::BuildParameterDefinition")
builds_Change = Class(name="builds::Change")
builds_ChangeArtifact = Class(name="builds::ChangeArtifact")
TestElement = Class(name="TestElement")
builds_TestCase = Class(name="builds::TestCase")
builds_StringParameterDefinition = Class(name="builds::StringParameterDefinition")
builds_TestSuite = Class(name="builds::TestSuite")
builds_TestElement = Class(name="builds::TestElement")

# builds_StringToStringMap class attributes and methods
builds_StringToStringMap_key: Property = Property(name="key", type=StringType)
builds_StringToStringMap_value: Property = Property(name="value", type=StringType)
builds_StringToStringMap.attributes={builds_StringToStringMap_value, builds_StringToStringMap_key}

# builds_User class attributes and methods
builds_User_id: Property = Property(name="id", type=StringType)
builds_User_email: Property = Property(name="email", type=StringType)
builds_User.attributes={builds_User_id, builds_User_email}

# builds_BuildCause class attributes and methods
builds_BuildCause_description: Property = Property(name="description", type=StringType)
builds_BuildCause.attributes={builds_BuildCause_description}

# builds_BuildReference class attributes and methods
builds_BuildReference_plan: Property = Property(name="plan", type=StringType)
builds_BuildReference_build: Property = Property(name="build", type=StringType)
builds_BuildReference.attributes={builds_BuildReference_plan, builds_BuildReference_build}

# builds_BuildElement class attributes and methods
builds_BuildElement_url: Property = Property(name="url", type=StringType)
builds_BuildElement_name: Property = Property(name="name", type=StringType)
builds_BuildElement_operations: Property = Property(name="operations", type=StringType)
builds_BuildElement_elementStatus: Property = Property(name="elementStatus", type=StringType)
builds_BuildElement_refreshDate: Property = Property(name="refreshDate", type=DateType)
builds_BuildElement_m_getLabel: Method = Method(name="getLabel", parameters={}, type=StringType)
builds_BuildElement_m_getServer: Method = Method(name="getServer", parameters={}, type=StringType)
builds_BuildElement.attributes={builds_BuildElement_url, builds_BuildElement_refreshDate, builds_BuildElement_operations, builds_BuildElement_elementStatus, builds_BuildElement_name}
builds_BuildElement.methods={builds_BuildElement_m_getLabel, builds_BuildElement_m_getServer}

# builds_Artifact class attributes and methods
builds_Artifact_relativePath: Property = Property(name="relativePath", type=StringType)
builds_Artifact.attributes={builds_Artifact_relativePath}

# BuildElement class attributes and methods

# builds_Build class attributes and methods
builds_Build_summary: Property = Property(name="summary", type=StringType)
builds_Build_id: Property = Property(name="id", type=StringType)
builds_Build_buildNumber: Property = Property(name="buildNumber", type=IntegerType)
builds_Build_timestamp: Property = Property(name="timestamp", type=StringType)
builds_Build_duration: Property = Property(name="duration", type=StringType)
builds_Build_displayName: Property = Property(name="displayName", type=StringType)
builds_Build_state: Property = Property(name="state", type=StringType)
builds_Build_status: Property = Property(name="status", type=StringType)
builds_Build_label: Property = Property(name="label", type=StringType)
builds_Build.attributes={builds_Build_duration, builds_Build_label, builds_Build_id, builds_Build_summary, builds_Build_state, builds_Build_timestamp, builds_Build_displayName, builds_Build_status, builds_Build_buildNumber}

# builds_ChangeSet class attributes and methods
builds_ChangeSet_kind: Property = Property(name="kind", type=StringType)
builds_ChangeSet.attributes={builds_ChangeSet_kind}

# builds_BuildPlan class attributes and methods
builds_BuildPlan_flags: Property = Property(name="flags", type=StringType)
builds_BuildPlan_health: Property = Property(name="health", type=IntegerType)
builds_BuildPlan_id: Property = Property(name="id", type=StringType)
builds_BuildPlan_info: Property = Property(name="info", type=StringType)
builds_BuildPlan_selected: Property = Property(name="selected", type=BooleanType)
builds_BuildPlan_summary: Property = Property(name="summary", type=StringType)
builds_BuildPlan_state: Property = Property(name="state", type=StringType)
builds_BuildPlan_status: Property = Property(name="status", type=StringType)
builds_BuildPlan_description: Property = Property(name="description", type=StringType)
builds_BuildPlan.attributes={builds_BuildPlan_summary, builds_BuildPlan_info, builds_BuildPlan_selected, builds_BuildPlan_status, builds_BuildPlan_flags, builds_BuildPlan_description, builds_BuildPlan_state, builds_BuildPlan_health, builds_BuildPlan_id}

# builds_BuildServer class attributes and methods
builds_BuildServer_location: Property = Property(name="location", type=StringType)
builds_BuildServer_connectorKind: Property = Property(name="connectorKind", type=StringType)
builds_BuildServer_repositoryUrl: Property = Property(name="repositoryUrl", type=StringType)
builds_BuildServer.attributes={builds_BuildServer_repositoryUrl, builds_BuildServer_connectorKind, builds_BuildServer_location}

# builds_TestResult class attributes and methods
builds_TestResult_duration: Property = Property(name="duration", type=StringType)
builds_TestResult_failCount: Property = Property(name="failCount", type=IntegerType)
builds_TestResult_passCount: Property = Property(name="passCount", type=IntegerType)
builds_TestResult_ignoredCount: Property = Property(name="ignoredCount", type=IntegerType)
builds_TestResult_errorCount: Property = Property(name="errorCount", type=IntegerType)
builds_TestResult.attributes={builds_TestResult_duration, builds_TestResult_errorCount, builds_TestResult_passCount, builds_TestResult_ignoredCount, builds_TestResult_failCount}

# builds_ParameterDefinition class attributes and methods
builds_ParameterDefinition_name: Property = Property(name="name", type=StringType)
builds_ParameterDefinition_description: Property = Property(name="description", type=StringType)
builds_ParameterDefinition.attributes={builds_ParameterDefinition_name, builds_ParameterDefinition_description}

# builds_HealthReport class attributes and methods
builds_HealthReport_health: Property = Property(name="health", type=IntegerType)
builds_HealthReport_description: Property = Property(name="description", type=StringType)
builds_HealthReport.attributes={builds_HealthReport_health, builds_HealthReport_description}

# builds_BuildModel class attributes and methods

# builds_ChoiceParameterDefinition class attributes and methods
builds_ChoiceParameterDefinition_options: Property = Property(name="options", type=StringType)
builds_ChoiceParameterDefinition_defaultValue: Property = Property(name="defaultValue", type=StringType)
builds_ChoiceParameterDefinition.attributes={builds_ChoiceParameterDefinition_options, builds_ChoiceParameterDefinition_defaultValue}

# ParameterDefinition class attributes and methods

# builds_BooleanParameterDefinition class attributes and methods
builds_BooleanParameterDefinition_defaultValue: Property = Property(name="defaultValue", type=BooleanType)
builds_BooleanParameterDefinition.attributes={builds_BooleanParameterDefinition_defaultValue}

# builds_FileParameterDefinition class attributes and methods

# builds_PlanParameterDefinition class attributes and methods

# builds_PasswordParameterDefinition class attributes and methods
builds_PasswordParameterDefinition_defaultValue: Property = Property(name="defaultValue", type=StringType)
builds_PasswordParameterDefinition.attributes={builds_PasswordParameterDefinition_defaultValue}

# builds_BuildParameterDefinition class attributes and methods
builds_BuildParameterDefinition_buildPlanId: Property = Property(name="buildPlanId", type=StringType)
builds_BuildParameterDefinition.attributes={builds_BuildParameterDefinition_buildPlanId}

# builds_Change class attributes and methods
builds_Change_message: Property = Property(name="message", type=StringType)
builds_Change_date: Property = Property(name="date", type=StringType)
builds_Change_revision: Property = Property(name="revision", type=StringType)
builds_Change.attributes={builds_Change_revision, builds_Change_message, builds_Change_date}

# builds_ChangeArtifact class attributes and methods
builds_ChangeArtifact_file: Property = Property(name="file", type=StringType)
builds_ChangeArtifact_relativePath: Property = Property(name="relativePath", type=StringType)
builds_ChangeArtifact_prevRevision: Property = Property(name="prevRevision", type=StringType)
builds_ChangeArtifact_revision: Property = Property(name="revision", type=StringType)
builds_ChangeArtifact_dead: Property = Property(name="dead", type=BooleanType)
builds_ChangeArtifact_editType: Property = Property(name="editType", type=StringType)
builds_ChangeArtifact.attributes={builds_ChangeArtifact_editType, builds_ChangeArtifact_revision, builds_ChangeArtifact_dead, builds_ChangeArtifact_file, builds_ChangeArtifact_relativePath, builds_ChangeArtifact_prevRevision}

# TestElement class attributes and methods

# builds_TestCase class attributes and methods
builds_TestCase_className: Property = Property(name="className", type=StringType)
builds_TestCase_skipped: Property = Property(name="skipped", type=BooleanType)
builds_TestCase_status: Property = Property(name="status", type=StringType)
builds_TestCase_message: Property = Property(name="message", type=StringType)
builds_TestCase_stackTrace: Property = Property(name="stackTrace", type=StringType)
builds_TestCase.attributes={builds_TestCase_stackTrace, builds_TestCase_status, builds_TestCase_skipped, builds_TestCase_className, builds_TestCase_message}

# builds_StringParameterDefinition class attributes and methods
builds_StringParameterDefinition_defaultValue: Property = Property(name="defaultValue", type=StringType)
builds_StringParameterDefinition.attributes={builds_StringParameterDefinition_defaultValue}

# builds_TestSuite class attributes and methods

# builds_TestElement class attributes and methods
builds_TestElement_duration: Property = Property(name="duration", type=StringType)
builds_TestElement_errorOutput: Property = Property(name="errorOutput", type=StringType)
builds_TestElement_output: Property = Property(name="output", type=StringType)
builds_TestElement_label: Property = Property(name="label", type=StringType)
builds_TestElement.attributes={builds_TestElement_label, builds_TestElement_duration, builds_TestElement_errorOutput, builds_TestElement_output}

# Relationships
testResult7: BinaryAssociation = BinaryAssociation(
    name="testResult7",
    ends={
        Property(name="TestResult", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="build", type=builds_TestResult, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
culprits8: BinaryAssociation = BinaryAssociation(
    name="culprits8",
    ends={
        Property(name="builds_User", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build9", type=builds_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cause10: BinaryAssociation = BinaryAssociation(
    name="cause10",
    ends={
        Property(name="builds_BuildCause", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build11", type=builds_BuildCause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build12: BinaryAssociation = BinaryAssociation(
    name="build12",
    ends={
        Property(name="builds_BuildReference", type=builds_BuildCause, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildCause13", type=builds_BuildReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
user14: BinaryAssociation = BinaryAssociation(
    name="user14",
    ends={
        Property(name="builds_User16", type=builds_BuildCause, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildCause15", type=builds_User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
artifacts0: BinaryAssociation = BinaryAssociation(
    name="artifacts0",
    ends={
        Property(name="builds_Artifact", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build", type=builds_Artifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
changeSet1: BinaryAssociation = BinaryAssociation(
    name="changeSet1",
    ends={
        Property(name="builds_ChangeSet", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build2", type=builds_ChangeSet, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plan3: BinaryAssociation = BinaryAssociation(
    name="plan3",
    ends={
        Property(name="builds_BuildPlan", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build4", type=builds_BuildPlan, multiplicity=Multiplicity(0, 1))
    }
)
server5: BinaryAssociation = BinaryAssociation(
    name="server5",
    ends={
        Property(name="builds_BuildServer", type=builds_Build, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Build6", type=builds_BuildServer, multiplicity=Multiplicity(0, 1))
    }
)
parameterDefinitions29: BinaryAssociation = BinaryAssociation(
    name="parameterDefinitions29",
    ends={
        Property(name="ParameterDefinition", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="containingBuildPlan", type=builds_ParameterDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
healthReports30: BinaryAssociation = BinaryAssociation(
    name="healthReports30",
    ends={
        Property(name="builds_HealthReport", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildPlan31", type=builds_HealthReport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
servers32: BinaryAssociation = BinaryAssociation(
    name="servers32",
    ends={
        Property(name="builds_BuildServer33", type=builds_BuildModel, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildModel", type=builds_BuildServer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plans34: BinaryAssociation = BinaryAssociation(
    name="plans34",
    ends={
        Property(name="builds_BuildPlan36", type=builds_BuildModel, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildModel35", type=builds_BuildPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
builds37: BinaryAssociation = BinaryAssociation(
    name="builds37",
    ends={
        Property(name="builds_Build39", type=builds_BuildModel, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildModel38", type=builds_Build, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes17: BinaryAssociation = BinaryAssociation(
    name="attributes17",
    ends={
        Property(name="builds_StringToStringMap", type=builds_BuildElement, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildElement", type=builds_StringToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
server18: BinaryAssociation = BinaryAssociation(
    name="server18",
    ends={
        Property(name="builds_BuildServer20", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildPlan19", type=builds_BuildServer, multiplicity=Multiplicity(1, 1))
    }
)
children22: BinaryAssociation = BinaryAssociation(
    name="children22",
    ends={
        Property(name="BuildPlan", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=builds_BuildPlan, multiplicity=Multiplicity(0, 9999))
    }
)
parent24: BinaryAssociation = BinaryAssociation(
    name="parent24",
    ends={
        Property(name="BuildPlan25", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=builds_BuildPlan, multiplicity=Multiplicity(0, 1))
    }
)
lastBuild26: BinaryAssociation = BinaryAssociation(
    name="lastBuild26",
    ends={
        Property(name="builds_Build28", type=builds_BuildPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildPlan27", type=builds_Build, multiplicity=Multiplicity(0, 1))
    }
)
containingBuildPlan47: BinaryAssociation = BinaryAssociation(
    name="containingBuildPlan47",
    ends={
        Property(name="BuildPlan48", type=builds_ParameterDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterDefinitions", type=builds_BuildPlan, multiplicity=Multiplicity(0, 1))
    }
)
artifacts40: BinaryAssociation = BinaryAssociation(
    name="artifacts40",
    ends={
        Property(name="builds_ChangeArtifact", type=builds_Change, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Change", type=builds_ChangeArtifact, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author41: BinaryAssociation = BinaryAssociation(
    name="author41",
    ends={
        Property(name="builds_User43", type=builds_Change, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_Change42", type=builds_User, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
changes44: BinaryAssociation = BinaryAssociation(
    name="changes44",
    ends={
        Property(name="builds_Change46", type=builds_ChangeSet, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_ChangeSet45", type=builds_Change, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases53: BinaryAssociation = BinaryAssociation(
    name="cases53",
    ends={
        Property(name="TestCase", type=builds_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="suite", type=builds_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result54: BinaryAssociation = BinaryAssociation(
    name="result54",
    ends={
        Property(name="TestResult55", type=builds_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="suites", type=builds_TestResult, multiplicity=Multiplicity(0, 1))
    }
)
suite56: BinaryAssociation = BinaryAssociation(
    name="suite56",
    ends={
        Property(name="TestSuite57", type=builds_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="cases", type=builds_TestSuite, multiplicity=Multiplicity(0, 1))
    }
)
buildPlan49: BinaryAssociation = BinaryAssociation(
    name="buildPlan49",
    ends={
        Property(name="builds_BuildPlan50", type=builds_BuildParameterDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="builds_BuildParameterDefinition", type=builds_BuildPlan, multiplicity=Multiplicity(0, 1))
    }
)
build51: BinaryAssociation = BinaryAssociation(
    name="build51",
    ends={
        Property(name="Build", type=builds_TestResult, multiplicity=Multiplicity(1, 1)),
        Property(name="testResult", type=builds_Build, multiplicity=Multiplicity(0, 1))
    }
)
suites52: BinaryAssociation = BinaryAssociation(
    name="suites52",
    ends={
        Property(name="TestSuite", type=builds_TestResult, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=builds_TestSuite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_builds_Artifact_BuildElement = Generalization(general=BuildElement, specific=builds_Artifact)
gen_builds_Build_BuildElement = Generalization(general=BuildElement, specific=builds_Build)
gen_builds_BuildServer_BuildElement = Generalization(general=BuildElement, specific=builds_BuildServer)
gen_builds_BuildPlan_BuildElement = Generalization(general=BuildElement, specific=builds_BuildPlan)
gen_builds_ChoiceParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_ChoiceParameterDefinition)
gen_builds_BooleanParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_BooleanParameterDefinition)
gen_builds_FileParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_FileParameterDefinition)
gen_builds_PlanParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_PlanParameterDefinition)
gen_builds_PasswordParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_PasswordParameterDefinition)
gen_builds_BuildParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_BuildParameterDefinition)
gen_builds_User_BuildElement = Generalization(general=BuildElement, specific=builds_User)
gen_builds_TestSuite_TestElement = Generalization(general=TestElement, specific=builds_TestSuite)
gen_builds_TestCase_TestElement = Generalization(general=TestElement, specific=builds_TestCase)
gen_builds_StringParameterDefinition_ParameterDefinition = Generalization(general=ParameterDefinition, specific=builds_StringParameterDefinition)

# Domain Model
domain_model = DomainModel(
    name="builds",
    types={builds_StringToStringMap, builds_User, builds_BuildCause, builds_BuildReference, builds_BuildElement, builds_Artifact, BuildElement, builds_Build, builds_ChangeSet, builds_BuildPlan, builds_BuildServer, builds_TestResult, builds_ParameterDefinition, builds_HealthReport, builds_BuildModel, builds_ChoiceParameterDefinition, ParameterDefinition, builds_BooleanParameterDefinition, builds_FileParameterDefinition, builds_PlanParameterDefinition, builds_PasswordParameterDefinition, builds_BuildParameterDefinition, builds_Change, builds_ChangeArtifact, TestElement, builds_TestCase, builds_StringParameterDefinition, builds_TestSuite, builds_TestElement, TestCaseResult},
    associations={testResult7, culprits8, cause10, build12, user14, artifacts0, changeSet1, plan3, server5, parameterDefinitions29, healthReports30, servers32, plans34, builds37, attributes17, server18, children22, parent24, lastBuild26, containingBuildPlan47, artifacts40, author41, changes44, cases53, result54, suite56, buildPlan49, build51, suites52},
    generalizations={gen_builds_Artifact_BuildElement, gen_builds_Build_BuildElement, gen_builds_BuildServer_BuildElement, gen_builds_BuildPlan_BuildElement, gen_builds_ChoiceParameterDefinition_ParameterDefinition, gen_builds_BooleanParameterDefinition_ParameterDefinition, gen_builds_FileParameterDefinition_ParameterDefinition, gen_builds_PlanParameterDefinition_ParameterDefinition, gen_builds_PasswordParameterDefinition_ParameterDefinition, gen_builds_BuildParameterDefinition_ParameterDefinition, gen_builds_User_BuildElement, gen_builds_TestSuite_TestElement, gen_builds_TestCase_TestElement, gen_builds_StringParameterDefinition_ParameterDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)