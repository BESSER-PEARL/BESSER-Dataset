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
safetyDSL_ImplementationDetail = Class(name="safetyDSL::ImplementationDetail")
safetyDSL_HazardViewpoint = Class(name="safetyDSL::HazardViewpoint")
SafetyViewpoint = Class(name="SafetyViewpoint")
safetyDSL_HazardElement = Class(name="safetyDSL::HazardElement")
safetyDSL_HazardRelation = Class(name="safetyDSL::HazardRelation")
safetyDSL_SafetyFramework = Class(name="safetyDSL::SafetyFramework")
safetyDSL_SafetyViewpoint = Class(name="safetyDSL::SafetyViewpoint")
safetyDSL_Consequence = Class(name="safetyDSL::Consequence")
safetyDSL_Fault = Class(name="safetyDSL::Fault")
safetyDSL_FaultTree = Class(name="safetyDSL::FaultTree")
safetyDSL_FaultTreeNode = Class(name="safetyDSL::FaultTreeNode")
safetyDSL_Hazard = Class(name="safetyDSL::Hazard")
HazardElement = Class(name="HazardElement")
safetyDSL_SafetyRequirement = Class(name="safetyDSL::SafetyRequirement")
safetyDSL_CausedBy = Class(name="safetyDSL::CausedBy")
safetyDSL_SafetyTacticViewpoint = Class(name="safetyDSL::SafetyTacticViewpoint")
safetyDSL_SafetyTactic = Class(name="safetyDSL::SafetyTactic")
safetyDSL_FaultAvoidance = Class(name="safetyDSL::FaultAvoidance")
SafetyTactic = Class(name="SafetyTactic")
safetyDSL_DerivedFrom = Class(name="safetyDSL::DerivedFrom")
HazardRelation = Class(name="HazardRelation")
safetyDSL_Causes = Class(name="safetyDSL::Causes")
safetyDSL_SafetyCritical = Class(name="safetyDSL::SafetyCritical")
ArchitecturalElement = Class(name="ArchitecturalElement")
safetyDSL_CriticalityLevel = Class(name="safetyDSL::CriticalityLevel")
safetyDSL_State = Class(name="safetyDSL::State")
safetyDSL_FaultDetection = Class(name="safetyDSL::FaultDetection")
safetyDSL_FaultContainment = Class(name="safetyDSL::FaultContainment")
safetyDSL_SafetyCriticalViewpoint = Class(name="safetyDSL::SafetyCriticalViewpoint")
safetyDSL_ArchitecturalElement = Class(name="safetyDSL::ArchitecturalElement")
safetyDSL_SafetyCriticalRelation = Class(name="safetyDSL::SafetyCriticalRelation")
SafetyCriticalRelation = Class(name="SafetyCriticalRelation")
safetyDSL_MonitorToArchitecturalElement = Class(name="safetyDSL::MonitorToArchitecturalElement")
safetyDSL_ReportsFault = Class(name="safetyDSL::ReportsFault")
safetyDSL_NonSafetyCritical = Class(name="safetyDSL::NonSafetyCritical")
safetyDSL_Monitor = Class(name="safetyDSL::Monitor")
safetyDSL_ArchElementToArchElement = Class(name="safetyDSL::ArchElementToArchElement")
safetyDSL_ClassDef = Class(name="safetyDSL::ClassDef")
safetyDSL_ORNodeExpression = Class(name="safetyDSL::ORNodeExpression")
FaultTreeNode = Class(name="FaultTreeNode")
safetyDSL_ANDNodeExpression = Class(name="safetyDSL::ANDNodeExpression")
safetyDSL_LevelA = Class(name="safetyDSL::LevelA")
CriticalityLevel = Class(name="CriticalityLevel")
safetyDSL_LevelB = Class(name="safetyDSL::LevelB")
safetyDSL_ModuleClassRelation = Class(name="safetyDSL::ModuleClassRelation")
safetyDSL_ClassTestCaseRelation = Class(name="safetyDSL::ClassTestCaseRelation")
safetyDSL_Stops = Class(name="safetyDSL::Stops")
MonitorToArchitecturalElement = Class(name="MonitorToArchitecturalElement")
safetyDSL_Starts = Class(name="safetyDSL::Starts")
safetyDSL_Inits = Class(name="safetyDSL::Inits")
safetyDSL_Restarts = Class(name="safetyDSL::Restarts")
safetyDSL_Monitors = Class(name="safetyDSL::Monitors")
safetyDSL_LevelC = Class(name="safetyDSL::LevelC")
safetyDSL_LevelD = Class(name="safetyDSL::LevelD")
safetyDSL_SafeState = Class(name="safetyDSL::SafeState")
State = Class(name="State")
safetyDSL_Reads = Class(name="safetyDSL::Reads")
ArchElementToArchElement = Class(name="ArchElementToArchElement")
safetyDSL_Writes = Class(name="safetyDSL::Writes")
safetyDSL_Commands = Class(name="safetyDSL::Commands")

# safetyDSL_ImplementationDetail class attributes and methods

# safetyDSL_HazardViewpoint class attributes and methods

# SafetyViewpoint class attributes and methods

# safetyDSL_HazardElement class attributes and methods
safetyDSL_HazardElement_name: Property = Property(name="name", type=StringType)
safetyDSL_HazardElement.attributes={safetyDSL_HazardElement_name}

# safetyDSL_HazardRelation class attributes and methods

# safetyDSL_SafetyFramework class attributes and methods

# safetyDSL_SafetyViewpoint class attributes and methods
safetyDSL_SafetyViewpoint_name: Property = Property(name="name", type=StringType)
safetyDSL_SafetyViewpoint.attributes={safetyDSL_SafetyViewpoint_name}

# safetyDSL_Consequence class attributes and methods

# safetyDSL_Fault class attributes and methods

# safetyDSL_FaultTree class attributes and methods

# safetyDSL_FaultTreeNode class attributes and methods

# safetyDSL_Hazard class attributes and methods

# HazardElement class attributes and methods

# safetyDSL_SafetyRequirement class attributes and methods

# safetyDSL_CausedBy class attributes and methods

# safetyDSL_SafetyTacticViewpoint class attributes and methods

# safetyDSL_SafetyTactic class attributes and methods
safetyDSL_SafetyTactic_name: Property = Property(name="name", type=StringType)
safetyDSL_SafetyTactic_type: Property = Property(name="type", type=StringType)
safetyDSL_SafetyTactic.attributes={safetyDSL_SafetyTactic_type, safetyDSL_SafetyTactic_name}

# safetyDSL_FaultAvoidance class attributes and methods

# SafetyTactic class attributes and methods

# safetyDSL_DerivedFrom class attributes and methods

# HazardRelation class attributes and methods

# safetyDSL_Causes class attributes and methods

# safetyDSL_SafetyCritical class attributes and methods

# ArchitecturalElement class attributes and methods

# safetyDSL_CriticalityLevel class attributes and methods

# safetyDSL_State class attributes and methods
safetyDSL_State_name: Property = Property(name="name", type=StringType)
safetyDSL_State.attributes={safetyDSL_State_name}

# safetyDSL_FaultDetection class attributes and methods

# safetyDSL_FaultContainment class attributes and methods

# safetyDSL_SafetyCriticalViewpoint class attributes and methods

# safetyDSL_ArchitecturalElement class attributes and methods
safetyDSL_ArchitecturalElement_name: Property = Property(name="name", type=StringType)
safetyDSL_ArchitecturalElement.attributes={safetyDSL_ArchitecturalElement_name}

# safetyDSL_SafetyCriticalRelation class attributes and methods

# SafetyCriticalRelation class attributes and methods

# safetyDSL_MonitorToArchitecturalElement class attributes and methods

# safetyDSL_ReportsFault class attributes and methods

# safetyDSL_NonSafetyCritical class attributes and methods

# safetyDSL_Monitor class attributes and methods

# safetyDSL_ArchElementToArchElement class attributes and methods

# safetyDSL_ClassDef class attributes and methods
safetyDSL_ClassDef_name: Property = Property(name="name", type=StringType)
safetyDSL_ClassDef.attributes={safetyDSL_ClassDef_name}

# safetyDSL_ORNodeExpression class attributes and methods

# FaultTreeNode class attributes and methods

# safetyDSL_ANDNodeExpression class attributes and methods

# safetyDSL_LevelA class attributes and methods

# CriticalityLevel class attributes and methods

# safetyDSL_LevelB class attributes and methods

# safetyDSL_ModuleClassRelation class attributes and methods

# safetyDSL_ClassTestCaseRelation class attributes and methods
safetyDSL_ClassTestCaseRelation_testCases: Property = Property(name="testCases", type=StringType)
safetyDSL_ClassTestCaseRelation.attributes={safetyDSL_ClassTestCaseRelation_testCases}

# safetyDSL_Stops class attributes and methods

# MonitorToArchitecturalElement class attributes and methods

# safetyDSL_Starts class attributes and methods

# safetyDSL_Inits class attributes and methods

# safetyDSL_Restarts class attributes and methods

# safetyDSL_Monitors class attributes and methods

# safetyDSL_LevelC class attributes and methods

# safetyDSL_LevelD class attributes and methods

# safetyDSL_SafeState class attributes and methods

# State class attributes and methods

# safetyDSL_Reads class attributes and methods

# ArchElementToArchElement class attributes and methods

# safetyDSL_Writes class attributes and methods

# safetyDSL_Commands class attributes and methods

# Relationships
views0: BinaryAssociation = BinaryAssociation(
    name="views0",
    ends={
        Property(name="safetyDSL_SafetyFramework", type=safetyDSL_SafetyViewpoint, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="safetyDSL_SafetyViewpoint", type=safetyDSL_SafetyFramework, multiplicity=Multiplicity(1, 1))
    }
)
detail1: BinaryAssociation = BinaryAssociation(
    name="detail1",
    ends={
        Property(name="safetyDSL_ImplementationDetail", type=safetyDSL_SafetyFramework, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyFramework2", type=safetyDSL_ImplementationDetail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="safetyDSL_HazardElement", type=safetyDSL_HazardViewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_HazardViewpoint", type=safetyDSL_HazardElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations4: BinaryAssociation = BinaryAssociation(
    name="relations4",
    ends={
        Property(name="safetyDSL_HazardRelation", type=safetyDSL_HazardViewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_HazardViewpoint5", type=safetyDSL_HazardRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrequirements7: BinaryAssociation = BinaryAssociation(
    name="subrequirements7",
    ends={
        Property(name="safetyDSL_SafetyRequirement", type=safetyDSL_SafetyRequirement, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyRequirement6", type=safetyDSL_SafetyRequirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootNode8: BinaryAssociation = BinaryAssociation(
    name="rootNode8",
    ends={
        Property(name="safetyDSL_FaultTreeNode", type=safetyDSL_FaultTree, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_FaultTree", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value9: BinaryAssociation = BinaryAssociation(
    name="value9",
    ends={
        Property(name="safetyDSL_Fault", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_FaultTreeNode10", type=safetyDSL_Fault, multiplicity=Multiplicity(0, 1))
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="safetyDSL_FaultTreeNode13", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_FaultTreeNode11", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right15: BinaryAssociation = BinaryAssociation(
    name="right15",
    ends={
        Property(name="safetyDSL_FaultTreeNode16", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_FaultTreeNode14", type=safetyDSL_FaultTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fault22: BinaryAssociation = BinaryAssociation(
    name="fault22",
    ends={
        Property(name="safetyDSL_FaultTree23", type=safetyDSL_CausedBy, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_CausedBy", type=safetyDSL_FaultTree, multiplicity=Multiplicity(0, 1))
    }
)
safetyTactics24: BinaryAssociation = BinaryAssociation(
    name="safetyTactics24",
    ends={
        Property(name="safetyDSL_SafetyTactic", type=safetyDSL_SafetyTacticViewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyTacticViewpoint", type=safetyDSL_SafetyTactic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handledFaults25: BinaryAssociation = BinaryAssociation(
    name="handledFaults25",
    ends={
        Property(name="safetyDSL_Fault27", type=safetyDSL_SafetyTactic, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyTactic26", type=safetyDSL_Fault, multiplicity=Multiplicity(0, 9999))
    }
)
hazard17: BinaryAssociation = BinaryAssociation(
    name="hazard17",
    ends={
        Property(name="safetyDSL_Hazard", type=safetyDSL_HazardRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_HazardRelation18", type=safetyDSL_Hazard, multiplicity=Multiplicity(0, 1))
    }
)
safetyRequirements19: BinaryAssociation = BinaryAssociation(
    name="safetyRequirements19",
    ends={
        Property(name="safetyDSL_SafetyRequirement20", type=safetyDSL_DerivedFrom, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_DerivedFrom", type=safetyDSL_SafetyRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
consequences21: BinaryAssociation = BinaryAssociation(
    name="consequences21",
    ends={
        Property(name="safetyDSL_Consequence", type=safetyDSL_Causes, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_Causes", type=safetyDSL_Consequence, multiplicity=Multiplicity(0, 9999))
    }
)
level31: BinaryAssociation = BinaryAssociation(
    name="level31",
    ends={
        Property(name="safetyDSL_CriticalityLevel", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCritical", type=safetyDSL_CriticalityLevel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementedSafetyRequirements32: BinaryAssociation = BinaryAssociation(
    name="implementedSafetyRequirements32",
    ends={
        Property(name="safetyDSL_SafetyRequirement34", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCritical33", type=safetyDSL_SafetyRequirement, multiplicity=Multiplicity(0, 9999))
    }
)
implementedTactics35: BinaryAssociation = BinaryAssociation(
    name="implementedTactics35",
    ends={
        Property(name="safetyDSL_SafetyTactic37", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCritical36", type=safetyDSL_SafetyTactic, multiplicity=Multiplicity(0, 9999))
    }
)
subelements39: BinaryAssociation = BinaryAssociation(
    name="subelements39",
    ends={
        Property(name="safetyDSL_SafetyCritical40", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCritical38", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(0, 9999))
    }
)
states41: BinaryAssociation = BinaryAssociation(
    name="states41",
    ends={
        Property(name="safetyDSL_State", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCritical42", type=safetyDSL_State, multiplicity=Multiplicity(0, 9999))
    }
)
elements28: BinaryAssociation = BinaryAssociation(
    name="elements28",
    ends={
        Property(name="safetyDSL_ArchitecturalElement", type=safetyDSL_SafetyCriticalViewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCriticalViewpoint", type=safetyDSL_ArchitecturalElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations29: BinaryAssociation = BinaryAssociation(
    name="relations29",
    ends={
        Property(name="safetyDSL_SafetyCriticalRelation", type=safetyDSL_SafetyCriticalViewpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_SafetyCriticalViewpoint30", type=safetyDSL_SafetyCriticalRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element147: BinaryAssociation = BinaryAssociation(
    name="element147",
    ends={
        Property(name="safetyDSL_ArchitecturalElement48", type=safetyDSL_ArchElementToArchElement, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ArchElementToArchElement", type=safetyDSL_ArchitecturalElement, multiplicity=Multiplicity(0, 1))
    }
)
element249: BinaryAssociation = BinaryAssociation(
    name="element249",
    ends={
        Property(name="safetyDSL_ArchitecturalElement51", type=safetyDSL_ArchElementToArchElement, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ArchElementToArchElement50", type=safetyDSL_ArchitecturalElement, multiplicity=Multiplicity(0, 9999))
    }
)
monitor52: BinaryAssociation = BinaryAssociation(
    name="monitor52",
    ends={
        Property(name="safetyDSL_Monitor53", type=safetyDSL_MonitorToArchitecturalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_MonitorToArchitecturalElement", type=safetyDSL_Monitor, multiplicity=Multiplicity(0, 1))
    }
)
safetyCritical54: BinaryAssociation = BinaryAssociation(
    name="safetyCritical54",
    ends={
        Property(name="safetyDSL_SafetyCritical56", type=safetyDSL_MonitorToArchitecturalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_MonitorToArchitecturalElement55", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(0, 9999))
    }
)
safetyCritical157: BinaryAssociation = BinaryAssociation(
    name="safetyCritical157",
    ends={
        Property(name="safetyDSL_SafetyCritical58", type=safetyDSL_ReportsFault, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ReportsFault", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(0, 1))
    }
)
subelements44: BinaryAssociation = BinaryAssociation(
    name="subelements44",
    ends={
        Property(name="safetyDSL_NonSafetyCritical", type=safetyDSL_NonSafetyCritical, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_NonSafetyCritical43", type=safetyDSL_NonSafetyCritical, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implementedTactics45: BinaryAssociation = BinaryAssociation(
    name="implementedTactics45",
    ends={
        Property(name="safetyDSL_SafetyTactic46", type=safetyDSL_Monitor, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_Monitor", type=safetyDSL_SafetyTactic, multiplicity=Multiplicity(0, 9999))
    }
)
classes69: BinaryAssociation = BinaryAssociation(
    name="classes69",
    ends={
        Property(name="safetyDSL_ClassDef", type=safetyDSL_ModuleClassRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ModuleClassRelation70", type=safetyDSL_ClassDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clazz71: BinaryAssociation = BinaryAssociation(
    name="clazz71",
    ends={
        Property(name="safetyDSL_ClassDef73", type=safetyDSL_ClassTestCaseRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ClassTestCaseRelation72", type=safetyDSL_ClassDef, multiplicity=Multiplicity(0, 1))
    }
)
safetyCritical259: BinaryAssociation = BinaryAssociation(
    name="safetyCritical259",
    ends={
        Property(name="safetyDSL_SafetyCritical61", type=safetyDSL_ReportsFault, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ReportsFault60", type=safetyDSL_SafetyCritical, multiplicity=Multiplicity(0, 9999))
    }
)
moduleClassRelations62: BinaryAssociation = BinaryAssociation(
    name="moduleClassRelations62",
    ends={
        Property(name="safetyDSL_ModuleClassRelation", type=safetyDSL_ImplementationDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ImplementationDetail63", type=safetyDSL_ModuleClassRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classTestCaseRelations64: BinaryAssociation = BinaryAssociation(
    name="classTestCaseRelations64",
    ends={
        Property(name="safetyDSL_ClassTestCaseRelation", type=safetyDSL_ImplementationDetail, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ImplementationDetail65", type=safetyDSL_ClassTestCaseRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module66: BinaryAssociation = BinaryAssociation(
    name="module66",
    ends={
        Property(name="safetyDSL_ArchitecturalElement68", type=safetyDSL_ModuleClassRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="safetyDSL_ModuleClassRelation67", type=safetyDSL_ArchitecturalElement, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_safetyDSL_HazardViewpoint_SafetyViewpoint = Generalization(general=SafetyViewpoint, specific=safetyDSL_HazardViewpoint)
gen_safetyDSL_Consequence_HazardElement = Generalization(general=HazardElement, specific=safetyDSL_Consequence)
gen_safetyDSL_Fault_HazardElement = Generalization(general=HazardElement, specific=safetyDSL_Fault)
gen_safetyDSL_FaultTree_HazardElement = Generalization(general=HazardElement, specific=safetyDSL_FaultTree)
gen_safetyDSL_Hazard_HazardElement = Generalization(general=HazardElement, specific=safetyDSL_Hazard)
gen_safetyDSL_SafetyRequirement_HazardElement = Generalization(general=HazardElement, specific=safetyDSL_SafetyRequirement)
gen_safetyDSL_CausedBy_HazardRelation = Generalization(general=HazardRelation, specific=safetyDSL_CausedBy)
gen_safetyDSL_SafetyTacticViewpoint_SafetyViewpoint = Generalization(general=SafetyViewpoint, specific=safetyDSL_SafetyTacticViewpoint)
gen_safetyDSL_FaultAvoidance_SafetyTactic = Generalization(general=SafetyTactic, specific=safetyDSL_FaultAvoidance)
gen_safetyDSL_DerivedFrom_HazardRelation = Generalization(general=HazardRelation, specific=safetyDSL_DerivedFrom)
gen_safetyDSL_Causes_HazardRelation = Generalization(general=HazardRelation, specific=safetyDSL_Causes)
gen_safetyDSL_SafetyCritical_ArchitecturalElement = Generalization(general=ArchitecturalElement, specific=safetyDSL_SafetyCritical)
gen_safetyDSL_FaultDetection_SafetyTactic = Generalization(general=SafetyTactic, specific=safetyDSL_FaultDetection)
gen_safetyDSL_FaultContainment_SafetyTactic = Generalization(general=SafetyTactic, specific=safetyDSL_FaultContainment)
gen_safetyDSL_SafetyCriticalViewpoint_SafetyViewpoint = Generalization(general=SafetyViewpoint, specific=safetyDSL_SafetyCriticalViewpoint)
gen_safetyDSL_ArchElementToArchElement_SafetyCriticalRelation = Generalization(general=SafetyCriticalRelation, specific=safetyDSL_ArchElementToArchElement)
gen_safetyDSL_MonitorToArchitecturalElement_SafetyCriticalRelation = Generalization(general=SafetyCriticalRelation, specific=safetyDSL_MonitorToArchitecturalElement)
gen_safetyDSL_ReportsFault_SafetyCriticalRelation = Generalization(general=SafetyCriticalRelation, specific=safetyDSL_ReportsFault)
gen_safetyDSL_NonSafetyCritical_ArchitecturalElement = Generalization(general=ArchitecturalElement, specific=safetyDSL_NonSafetyCritical)
gen_safetyDSL_Monitor_ArchitecturalElement = Generalization(general=ArchitecturalElement, specific=safetyDSL_Monitor)
gen_safetyDSL_ORNodeExpression_FaultTreeNode = Generalization(general=FaultTreeNode, specific=safetyDSL_ORNodeExpression)
gen_safetyDSL_ANDNodeExpression_FaultTreeNode = Generalization(general=FaultTreeNode, specific=safetyDSL_ANDNodeExpression)
gen_safetyDSL_LevelA_CriticalityLevel = Generalization(general=CriticalityLevel, specific=safetyDSL_LevelA)
gen_safetyDSL_LevelB_CriticalityLevel = Generalization(general=CriticalityLevel, specific=safetyDSL_LevelB)
gen_safetyDSL_Stops_MonitorToArchitecturalElement = Generalization(general=MonitorToArchitecturalElement, specific=safetyDSL_Stops)
gen_safetyDSL_Starts_MonitorToArchitecturalElement = Generalization(general=MonitorToArchitecturalElement, specific=safetyDSL_Starts)
gen_safetyDSL_Inits_MonitorToArchitecturalElement = Generalization(general=MonitorToArchitecturalElement, specific=safetyDSL_Inits)
gen_safetyDSL_Restarts_MonitorToArchitecturalElement = Generalization(general=MonitorToArchitecturalElement, specific=safetyDSL_Restarts)
gen_safetyDSL_Monitors_MonitorToArchitecturalElement = Generalization(general=MonitorToArchitecturalElement, specific=safetyDSL_Monitors)
gen_safetyDSL_LevelC_CriticalityLevel = Generalization(general=CriticalityLevel, specific=safetyDSL_LevelC)
gen_safetyDSL_LevelD_CriticalityLevel = Generalization(general=CriticalityLevel, specific=safetyDSL_LevelD)
gen_safetyDSL_SafeState_State = Generalization(general=State, specific=safetyDSL_SafeState)
gen_safetyDSL_Reads_ArchElementToArchElement = Generalization(general=ArchElementToArchElement, specific=safetyDSL_Reads)
gen_safetyDSL_Writes_ArchElementToArchElement = Generalization(general=ArchElementToArchElement, specific=safetyDSL_Writes)
gen_safetyDSL_Commands_ArchElementToArchElement = Generalization(general=ArchElementToArchElement, specific=safetyDSL_Commands)

# Domain Model
domain_model = DomainModel(
    name="safetyDSL",
    types={safetyDSL_ImplementationDetail, safetyDSL_HazardViewpoint, SafetyViewpoint, safetyDSL_HazardElement, safetyDSL_HazardRelation, safetyDSL_SafetyFramework, safetyDSL_SafetyViewpoint, safetyDSL_Consequence, safetyDSL_Fault, safetyDSL_FaultTree, safetyDSL_FaultTreeNode, safetyDSL_Hazard, HazardElement, safetyDSL_SafetyRequirement, safetyDSL_CausedBy, safetyDSL_SafetyTacticViewpoint, safetyDSL_SafetyTactic, safetyDSL_FaultAvoidance, SafetyTactic, safetyDSL_DerivedFrom, HazardRelation, safetyDSL_Causes, safetyDSL_SafetyCritical, ArchitecturalElement, safetyDSL_CriticalityLevel, safetyDSL_State, safetyDSL_FaultDetection, safetyDSL_FaultContainment, safetyDSL_SafetyCriticalViewpoint, safetyDSL_ArchitecturalElement, safetyDSL_SafetyCriticalRelation, SafetyCriticalRelation, safetyDSL_MonitorToArchitecturalElement, safetyDSL_ReportsFault, safetyDSL_NonSafetyCritical, safetyDSL_Monitor, safetyDSL_ArchElementToArchElement, safetyDSL_ClassDef, safetyDSL_ORNodeExpression, FaultTreeNode, safetyDSL_ANDNodeExpression, safetyDSL_LevelA, CriticalityLevel, safetyDSL_LevelB, safetyDSL_ModuleClassRelation, safetyDSL_ClassTestCaseRelation, safetyDSL_Stops, MonitorToArchitecturalElement, safetyDSL_Starts, safetyDSL_Inits, safetyDSL_Restarts, safetyDSL_Monitors, safetyDSL_LevelC, safetyDSL_LevelD, safetyDSL_SafeState, State, safetyDSL_Reads, ArchElementToArchElement, safetyDSL_Writes, safetyDSL_Commands},
    associations={views0, detail1, elements3, relations4, subrequirements7, rootNode8, value9, left12, right15, fault22, safetyTactics24, handledFaults25, hazard17, safetyRequirements19, consequences21, level31, implementedSafetyRequirements32, implementedTactics35, subelements39, states41, elements28, relations29, element147, element249, monitor52, safetyCritical54, safetyCritical157, subelements44, implementedTactics45, classes69, clazz71, safetyCritical259, moduleClassRelations62, classTestCaseRelations64, module66},
    generalizations={gen_safetyDSL_HazardViewpoint_SafetyViewpoint, gen_safetyDSL_Consequence_HazardElement, gen_safetyDSL_Fault_HazardElement, gen_safetyDSL_FaultTree_HazardElement, gen_safetyDSL_Hazard_HazardElement, gen_safetyDSL_SafetyRequirement_HazardElement, gen_safetyDSL_CausedBy_HazardRelation, gen_safetyDSL_SafetyTacticViewpoint_SafetyViewpoint, gen_safetyDSL_FaultAvoidance_SafetyTactic, gen_safetyDSL_DerivedFrom_HazardRelation, gen_safetyDSL_Causes_HazardRelation, gen_safetyDSL_SafetyCritical_ArchitecturalElement, gen_safetyDSL_FaultDetection_SafetyTactic, gen_safetyDSL_FaultContainment_SafetyTactic, gen_safetyDSL_SafetyCriticalViewpoint_SafetyViewpoint, gen_safetyDSL_ArchElementToArchElement_SafetyCriticalRelation, gen_safetyDSL_MonitorToArchitecturalElement_SafetyCriticalRelation, gen_safetyDSL_ReportsFault_SafetyCriticalRelation, gen_safetyDSL_NonSafetyCritical_ArchitecturalElement, gen_safetyDSL_Monitor_ArchitecturalElement, gen_safetyDSL_ORNodeExpression_FaultTreeNode, gen_safetyDSL_ANDNodeExpression_FaultTreeNode, gen_safetyDSL_LevelA_CriticalityLevel, gen_safetyDSL_LevelB_CriticalityLevel, gen_safetyDSL_Stops_MonitorToArchitecturalElement, gen_safetyDSL_Starts_MonitorToArchitecturalElement, gen_safetyDSL_Inits_MonitorToArchitecturalElement, gen_safetyDSL_Restarts_MonitorToArchitecturalElement, gen_safetyDSL_Monitors_MonitorToArchitecturalElement, gen_safetyDSL_LevelC_CriticalityLevel, gen_safetyDSL_LevelD_CriticalityLevel, gen_safetyDSL_SafeState_State, gen_safetyDSL_Reads_ArchElementToArchElement, gen_safetyDSL_Writes_ArchElementToArchElement, gen_safetyDSL_Commands_ArchElementToArchElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)