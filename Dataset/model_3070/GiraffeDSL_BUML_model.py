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
giraffeDSL_CloudProviderType = Class(name="giraffeDSL::CloudProviderType")
giraffeDSL_Type = Class(name="giraffeDSL::Type")
giraffeDSL_Create = Class(name="giraffeDSL::Create")
Type = Class(name="Type")
giraffeDSL_VirtualMachineFeature = Class(name="giraffeDSL::VirtualMachineFeature")
giraffeDSL_InitMachinesFeature = Class(name="giraffeDSL::InitMachinesFeature")
giraffeDSL_InitIncrementFeature = Class(name="giraffeDSL::InitIncrementFeature")
giraffeDSL_VirtualMachine = Class(name="giraffeDSL::VirtualMachine")
giraffeDSL_DomainModel = Class(name="giraffeDSL::DomainModel")
giraffeDSL_VirtualMachineTypeFeature = Class(name="giraffeDSL::VirtualMachineTypeFeature")
giraffeDSL_DeployTypeFeature = Class(name="giraffeDSL::DeployTypeFeature")
giraffeDSL_DeployApp = Class(name="giraffeDSL::DeployApp")
giraffeDSL_DeployType = Class(name="giraffeDSL::DeployType")
giraffeDSL_CloudProvider = Class(name="giraffeDSL::CloudProvider")
giraffeDSL_DeployRangeType = Class(name="giraffeDSL::DeployRangeType")
giraffeDSL_CloudType = Class(name="giraffeDSL::CloudType")
giraffeDSL_MgmAddressType = Class(name="giraffeDSL::MgmAddressType")
giraffeDSL_CloudCredentialType = Class(name="giraffeDSL::CloudCredentialType")
giraffeDSL_CloudOptionalTypes = Class(name="giraffeDSL::CloudOptionalTypes")
giraffeDSL_ScriptType = Class(name="giraffeDSL::ScriptType")
CloudOptionalTypes = Class(name="CloudOptionalTypes")
giraffeDSL_GeoZoneType = Class(name="giraffeDSL::GeoZoneType")
giraffeDSL_CloudUserType = Class(name="giraffeDSL::CloudUserType")
giraffeDSL_CloudPasswordType = Class(name="giraffeDSL::CloudPasswordType")
giraffeDSL_Deploy = Class(name="giraffeDSL::Deploy")
giraffeDSL_DeployAppFeature = Class(name="giraffeDSL::DeployAppFeature")
giraffeDSL_Stress = Class(name="giraffeDSL::Stress")
giraffeDSL_StressRangeType = Class(name="giraffeDSL::StressRangeType")
giraffeDSL_StressClassType = Class(name="giraffeDSL::StressClassType")
giraffeDSL_StressMethodType = Class(name="giraffeDSL::StressMethodType")
giraffeDSL_DeployAppClassType = Class(name="giraffeDSL::DeployAppClassType")
giraffeDSL_DeployAppMasterMethodType = Class(name="giraffeDSL::DeployAppMasterMethodType")
giraffeDSL_DeployAppSlaveMethodType = Class(name="giraffeDSL::DeployAppSlaveMethodType")
giraffeDSL_Monitor = Class(name="giraffeDSL::Monitor")
giraffeDSL_MonitorRangeType = Class(name="giraffeDSL::MonitorRangeType")
giraffeDSL_MonitoringType = Class(name="giraffeDSL::MonitoringType")
giraffeDSL_Action = Class(name="giraffeDSL::Action")
giraffeDSL_ActionRangeType = Class(name="giraffeDSL::ActionRangeType")
giraffeDSL_ActionClassType = Class(name="giraffeDSL::ActionClassType")
giraffeDSL_ActionMethodType = Class(name="giraffeDSL::ActionMethodType")
giraffeDSL_Features = Class(name="giraffeDSL::Features")
giraffeDSL_IntFeature = Class(name="giraffeDSL::IntFeature")

# giraffeDSL_CloudProviderType class attributes and methods
giraffeDSL_CloudProviderType_many: Property = Property(name="many", type=StringType)
giraffeDSL_CloudProviderType_name: Property = Property(name="name", type=StringType)
giraffeDSL_CloudProviderType.attributes={giraffeDSL_CloudProviderType_name, giraffeDSL_CloudProviderType_many}

# giraffeDSL_Type class attributes and methods
giraffeDSL_Type_name: Property = Property(name="name", type=StringType)
giraffeDSL_Type.attributes={giraffeDSL_Type_name}

# giraffeDSL_Create class attributes and methods

# Type class attributes and methods

# giraffeDSL_VirtualMachineFeature class attributes and methods
giraffeDSL_VirtualMachineFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_VirtualMachineFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_VirtualMachineFeature.attributes={giraffeDSL_VirtualMachineFeature_name, giraffeDSL_VirtualMachineFeature_many}

# giraffeDSL_InitMachinesFeature class attributes and methods
giraffeDSL_InitMachinesFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_InitMachinesFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_InitMachinesFeature_type: Property = Property(name="type", type=IntegerType)
giraffeDSL_InitMachinesFeature.attributes={giraffeDSL_InitMachinesFeature_type, giraffeDSL_InitMachinesFeature_many, giraffeDSL_InitMachinesFeature_name}

# giraffeDSL_InitIncrementFeature class attributes and methods
giraffeDSL_InitIncrementFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_InitIncrementFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_InitIncrementFeature_type: Property = Property(name="type", type=IntegerType)
giraffeDSL_InitIncrementFeature.attributes={giraffeDSL_InitIncrementFeature_name, giraffeDSL_InitIncrementFeature_type, giraffeDSL_InitIncrementFeature_many}

# giraffeDSL_VirtualMachine class attributes and methods

# giraffeDSL_DomainModel class attributes and methods

# giraffeDSL_VirtualMachineTypeFeature class attributes and methods
giraffeDSL_VirtualMachineTypeFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_VirtualMachineTypeFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_VirtualMachineTypeFeature_type: Property = Property(name="type", type=StringType)
giraffeDSL_VirtualMachineTypeFeature.attributes={giraffeDSL_VirtualMachineTypeFeature_type, giraffeDSL_VirtualMachineTypeFeature_name, giraffeDSL_VirtualMachineTypeFeature_many}

# giraffeDSL_DeployTypeFeature class attributes and methods
giraffeDSL_DeployTypeFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployTypeFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployTypeFeature.attributes={giraffeDSL_DeployTypeFeature_many, giraffeDSL_DeployTypeFeature_name}

# giraffeDSL_DeployApp class attributes and methods

# giraffeDSL_DeployType class attributes and methods

# giraffeDSL_CloudProvider class attributes and methods

# giraffeDSL_DeployRangeType class attributes and methods
giraffeDSL_DeployRangeType_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployRangeType_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployRangeType_type: Property = Property(name="type", type=StringType)
giraffeDSL_DeployRangeType.attributes={giraffeDSL_DeployRangeType_many, giraffeDSL_DeployRangeType_type, giraffeDSL_DeployRangeType_name}

# giraffeDSL_CloudType class attributes and methods
giraffeDSL_CloudType_many: Property = Property(name="many", type=StringType)
giraffeDSL_CloudType_name: Property = Property(name="name", type=StringType)
giraffeDSL_CloudType_type: Property = Property(name="type", type=StringType)
giraffeDSL_CloudType.attributes={giraffeDSL_CloudType_name, giraffeDSL_CloudType_type, giraffeDSL_CloudType_many}

# giraffeDSL_MgmAddressType class attributes and methods
giraffeDSL_MgmAddressType_many: Property = Property(name="many", type=StringType)
giraffeDSL_MgmAddressType_name: Property = Property(name="name", type=StringType)
giraffeDSL_MgmAddressType_type: Property = Property(name="type", type=StringType)
giraffeDSL_MgmAddressType.attributes={giraffeDSL_MgmAddressType_many, giraffeDSL_MgmAddressType_type, giraffeDSL_MgmAddressType_name}

# giraffeDSL_CloudCredentialType class attributes and methods
giraffeDSL_CloudCredentialType_many: Property = Property(name="many", type=StringType)
giraffeDSL_CloudCredentialType_name: Property = Property(name="name", type=StringType)
giraffeDSL_CloudCredentialType_type: Property = Property(name="type", type=StringType)
giraffeDSL_CloudCredentialType.attributes={giraffeDSL_CloudCredentialType_many, giraffeDSL_CloudCredentialType_name, giraffeDSL_CloudCredentialType_type}

# giraffeDSL_CloudOptionalTypes class attributes and methods
giraffeDSL_CloudOptionalTypes_many: Property = Property(name="many", type=StringType)
giraffeDSL_CloudOptionalTypes_name: Property = Property(name="name", type=StringType)
giraffeDSL_CloudOptionalTypes_type: Property = Property(name="type", type=StringType)
giraffeDSL_CloudOptionalTypes.attributes={giraffeDSL_CloudOptionalTypes_many, giraffeDSL_CloudOptionalTypes_type, giraffeDSL_CloudOptionalTypes_name}

# giraffeDSL_ScriptType class attributes and methods

# CloudOptionalTypes class attributes and methods

# giraffeDSL_GeoZoneType class attributes and methods

# giraffeDSL_CloudUserType class attributes and methods

# giraffeDSL_CloudPasswordType class attributes and methods

# giraffeDSL_Deploy class attributes and methods

# giraffeDSL_DeployAppFeature class attributes and methods
giraffeDSL_DeployAppFeature_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployAppFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployAppFeature.attributes={giraffeDSL_DeployAppFeature_many, giraffeDSL_DeployAppFeature_name}

# giraffeDSL_Stress class attributes and methods

# giraffeDSL_StressRangeType class attributes and methods
giraffeDSL_StressRangeType_many: Property = Property(name="many", type=StringType)
giraffeDSL_StressRangeType_name: Property = Property(name="name", type=StringType)
giraffeDSL_StressRangeType_type: Property = Property(name="type", type=StringType)
giraffeDSL_StressRangeType.attributes={giraffeDSL_StressRangeType_name, giraffeDSL_StressRangeType_type, giraffeDSL_StressRangeType_many}

# giraffeDSL_StressClassType class attributes and methods
giraffeDSL_StressClassType_many: Property = Property(name="many", type=StringType)
giraffeDSL_StressClassType_name: Property = Property(name="name", type=StringType)
giraffeDSL_StressClassType_type: Property = Property(name="type", type=StringType)
giraffeDSL_StressClassType.attributes={giraffeDSL_StressClassType_many, giraffeDSL_StressClassType_name, giraffeDSL_StressClassType_type}

# giraffeDSL_StressMethodType class attributes and methods
giraffeDSL_StressMethodType_many: Property = Property(name="many", type=StringType)
giraffeDSL_StressMethodType_name: Property = Property(name="name", type=StringType)
giraffeDSL_StressMethodType_type: Property = Property(name="type", type=StringType)
giraffeDSL_StressMethodType.attributes={giraffeDSL_StressMethodType_name, giraffeDSL_StressMethodType_many, giraffeDSL_StressMethodType_type}

# giraffeDSL_DeployAppClassType class attributes and methods
giraffeDSL_DeployAppClassType_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployAppClassType_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployAppClassType_type: Property = Property(name="type", type=StringType)
giraffeDSL_DeployAppClassType.attributes={giraffeDSL_DeployAppClassType_type, giraffeDSL_DeployAppClassType_many, giraffeDSL_DeployAppClassType_name}

# giraffeDSL_DeployAppMasterMethodType class attributes and methods
giraffeDSL_DeployAppMasterMethodType_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployAppMasterMethodType_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployAppMasterMethodType_type: Property = Property(name="type", type=StringType)
giraffeDSL_DeployAppMasterMethodType.attributes={giraffeDSL_DeployAppMasterMethodType_type, giraffeDSL_DeployAppMasterMethodType_many, giraffeDSL_DeployAppMasterMethodType_name}

# giraffeDSL_DeployAppSlaveMethodType class attributes and methods
giraffeDSL_DeployAppSlaveMethodType_many: Property = Property(name="many", type=StringType)
giraffeDSL_DeployAppSlaveMethodType_name: Property = Property(name="name", type=StringType)
giraffeDSL_DeployAppSlaveMethodType_type: Property = Property(name="type", type=StringType)
giraffeDSL_DeployAppSlaveMethodType.attributes={giraffeDSL_DeployAppSlaveMethodType_many, giraffeDSL_DeployAppSlaveMethodType_name, giraffeDSL_DeployAppSlaveMethodType_type}

# giraffeDSL_Monitor class attributes and methods

# giraffeDSL_MonitorRangeType class attributes and methods
giraffeDSL_MonitorRangeType_many: Property = Property(name="many", type=StringType)
giraffeDSL_MonitorRangeType_name: Property = Property(name="name", type=StringType)
giraffeDSL_MonitorRangeType_type: Property = Property(name="type", type=StringType)
giraffeDSL_MonitorRangeType.attributes={giraffeDSL_MonitorRangeType_name, giraffeDSL_MonitorRangeType_many, giraffeDSL_MonitorRangeType_type}

# giraffeDSL_MonitoringType class attributes and methods
giraffeDSL_MonitoringType_many: Property = Property(name="many", type=StringType)
giraffeDSL_MonitoringType_name: Property = Property(name="name", type=StringType)
giraffeDSL_MonitoringType_type: Property = Property(name="type", type=StringType)
giraffeDSL_MonitoringType.attributes={giraffeDSL_MonitoringType_type, giraffeDSL_MonitoringType_name, giraffeDSL_MonitoringType_many}

# giraffeDSL_Action class attributes and methods

# giraffeDSL_ActionRangeType class attributes and methods
giraffeDSL_ActionRangeType_many: Property = Property(name="many", type=StringType)
giraffeDSL_ActionRangeType_name: Property = Property(name="name", type=StringType)
giraffeDSL_ActionRangeType_type: Property = Property(name="type", type=StringType)
giraffeDSL_ActionRangeType.attributes={giraffeDSL_ActionRangeType_name, giraffeDSL_ActionRangeType_many, giraffeDSL_ActionRangeType_type}

# giraffeDSL_ActionClassType class attributes and methods
giraffeDSL_ActionClassType_many: Property = Property(name="many", type=StringType)
giraffeDSL_ActionClassType_name: Property = Property(name="name", type=StringType)
giraffeDSL_ActionClassType_type: Property = Property(name="type", type=StringType)
giraffeDSL_ActionClassType.attributes={giraffeDSL_ActionClassType_type, giraffeDSL_ActionClassType_many, giraffeDSL_ActionClassType_name}

# giraffeDSL_ActionMethodType class attributes and methods
giraffeDSL_ActionMethodType_many: Property = Property(name="many", type=StringType)
giraffeDSL_ActionMethodType_name: Property = Property(name="name", type=StringType)
giraffeDSL_ActionMethodType_type: Property = Property(name="type", type=StringType)
giraffeDSL_ActionMethodType.attributes={giraffeDSL_ActionMethodType_type, giraffeDSL_ActionMethodType_many, giraffeDSL_ActionMethodType_name}

# giraffeDSL_Features class attributes and methods
giraffeDSL_Features_name: Property = Property(name="name", type=StringType)
giraffeDSL_Features.attributes={giraffeDSL_Features_name}

# giraffeDSL_IntFeature class attributes and methods
giraffeDSL_IntFeature_name: Property = Property(name="name", type=StringType)
giraffeDSL_IntFeature.attributes={giraffeDSL_IntFeature_name}

# Relationships
cloudProvider10: BinaryAssociation = BinaryAssociation(
    name="cloudProvider10",
    ends={
        Property(name="giraffeDSL_CloudProviderType", type=giraffeDSL_VirtualMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_VirtualMachine11", type=giraffeDSL_CloudProviderType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="giraffeDSL_Type", type=giraffeDSL_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DomainModel", type=giraffeDSL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vMachine1: BinaryAssociation = BinaryAssociation(
    name="vMachine1",
    ends={
        Property(name="giraffeDSL_VirtualMachineFeature", type=giraffeDSL_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Create", type=giraffeDSL_VirtualMachineFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initMachines2: BinaryAssociation = BinaryAssociation(
    name="initMachines2",
    ends={
        Property(name="giraffeDSL_InitMachinesFeature", type=giraffeDSL_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Create3", type=giraffeDSL_InitMachinesFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initIncrement4: BinaryAssociation = BinaryAssociation(
    name="initIncrement4",
    ends={
        Property(name="giraffeDSL_InitIncrementFeature", type=giraffeDSL_Create, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Create5", type=giraffeDSL_InitIncrementFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="giraffeDSL_VirtualMachine", type=giraffeDSL_VirtualMachineFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_VirtualMachineFeature7", type=giraffeDSL_VirtualMachine, multiplicity=Multiplicity(0, 1))
    }
)
vM8: BinaryAssociation = BinaryAssociation(
    name="vM8",
    ends={
        Property(name="giraffeDSL_VirtualMachineTypeFeature", type=giraffeDSL_VirtualMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_VirtualMachine9", type=giraffeDSL_VirtualMachineTypeFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployOne22: BinaryAssociation = BinaryAssociation(
    name="deployOne22",
    ends={
        Property(name="giraffeDSL_DeployAppFeature", type=giraffeDSL_Deploy, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Deploy", type=giraffeDSL_DeployAppFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployTwo23: BinaryAssociation = BinaryAssociation(
    name="deployTwo23",
    ends={
        Property(name="giraffeDSL_DeployTypeFeature", type=giraffeDSL_Deploy, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Deploy24", type=giraffeDSL_DeployTypeFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="giraffeDSL_DeployApp", type=giraffeDSL_DeployAppFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployAppFeature26", type=giraffeDSL_DeployApp, multiplicity=Multiplicity(0, 1))
    }
)
type27: BinaryAssociation = BinaryAssociation(
    name="type27",
    ends={
        Property(name="giraffeDSL_DeployType", type=giraffeDSL_DeployTypeFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployTypeFeature28", type=giraffeDSL_DeployType, multiplicity=Multiplicity(0, 1))
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="giraffeDSL_CloudProvider", type=giraffeDSL_CloudProviderType, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_CloudProviderType13", type=giraffeDSL_CloudProvider, multiplicity=Multiplicity(0, 1))
    }
)
range29: BinaryAssociation = BinaryAssociation(
    name="range29",
    ends={
        Property(name="giraffeDSL_DeployRangeType", type=giraffeDSL_DeployType, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployType30", type=giraffeDSL_DeployRangeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudType14: BinaryAssociation = BinaryAssociation(
    name="cloudType14",
    ends={
        Property(name="giraffeDSL_CloudType", type=giraffeDSL_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_CloudProvider15", type=giraffeDSL_CloudType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudAddress16: BinaryAssociation = BinaryAssociation(
    name="cloudAddress16",
    ends={
        Property(name="giraffeDSL_MgmAddressType", type=giraffeDSL_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_CloudProvider17", type=giraffeDSL_MgmAddressType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudCredential18: BinaryAssociation = BinaryAssociation(
    name="cloudCredential18",
    ends={
        Property(name="giraffeDSL_CloudCredentialType", type=giraffeDSL_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_CloudProvider19", type=giraffeDSL_CloudCredentialType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cloudOptionalTypes20: BinaryAssociation = BinaryAssociation(
    name="cloudOptionalTypes20",
    ends={
        Property(name="giraffeDSL_CloudOptionalTypes", type=giraffeDSL_CloudProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_CloudProvider21", type=giraffeDSL_CloudOptionalTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range40: BinaryAssociation = BinaryAssociation(
    name="range40",
    ends={
        Property(name="giraffeDSL_StressRangeType", type=giraffeDSL_Stress, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Stress", type=giraffeDSL_StressRangeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stressClass41: BinaryAssociation = BinaryAssociation(
    name="stressClass41",
    ends={
        Property(name="giraffeDSL_StressClassType", type=giraffeDSL_Stress, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Stress42", type=giraffeDSL_StressClassType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stressMethod43: BinaryAssociation = BinaryAssociation(
    name="stressMethod43",
    ends={
        Property(name="giraffeDSL_StressMethodType", type=giraffeDSL_Stress, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Stress44", type=giraffeDSL_StressMethodType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class31: BinaryAssociation = BinaryAssociation(
    name="class31",
    ends={
        Property(name="giraffeDSL_DeployAppClassType", type=giraffeDSL_DeployApp, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployApp32", type=giraffeDSL_DeployAppClassType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deployMasterMethod33: BinaryAssociation = BinaryAssociation(
    name="deployMasterMethod33",
    ends={
        Property(name="giraffeDSL_DeployAppMasterMethodType", type=giraffeDSL_DeployApp, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployApp34", type=giraffeDSL_DeployAppMasterMethodType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deploySlaveMethod35: BinaryAssociation = BinaryAssociation(
    name="deploySlaveMethod35",
    ends={
        Property(name="giraffeDSL_DeployAppSlaveMethodType", type=giraffeDSL_DeployApp, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_DeployApp36", type=giraffeDSL_DeployAppSlaveMethodType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range37: BinaryAssociation = BinaryAssociation(
    name="range37",
    ends={
        Property(name="giraffeDSL_MonitorRangeType", type=giraffeDSL_Monitor, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Monitor", type=giraffeDSL_MonitorRangeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
monitoringType38: BinaryAssociation = BinaryAssociation(
    name="monitoringType38",
    ends={
        Property(name="giraffeDSL_MonitoringType", type=giraffeDSL_Monitor, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Monitor39", type=giraffeDSL_MonitoringType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
range45: BinaryAssociation = BinaryAssociation(
    name="range45",
    ends={
        Property(name="giraffeDSL_ActionRangeType", type=giraffeDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Action", type=giraffeDSL_ActionRangeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class46: BinaryAssociation = BinaryAssociation(
    name="class46",
    ends={
        Property(name="giraffeDSL_ActionClassType", type=giraffeDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Action47", type=giraffeDSL_ActionClassType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method48: BinaryAssociation = BinaryAssociation(
    name="method48",
    ends={
        Property(name="giraffeDSL_ActionMethodType", type=giraffeDSL_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="giraffeDSL_Action49", type=giraffeDSL_ActionMethodType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_giraffeDSL_Create_Type = Generalization(general=Type, specific=giraffeDSL_Create)
gen_giraffeDSL_VirtualMachine_Type = Generalization(general=Type, specific=giraffeDSL_VirtualMachine)
gen_giraffeDSL_DeployType_Type = Generalization(general=Type, specific=giraffeDSL_DeployType)
gen_giraffeDSL_CloudProvider_Type = Generalization(general=Type, specific=giraffeDSL_CloudProvider)
gen_giraffeDSL_ScriptType_CloudOptionalTypes = Generalization(general=CloudOptionalTypes, specific=giraffeDSL_ScriptType)
gen_giraffeDSL_GeoZoneType_CloudOptionalTypes = Generalization(general=CloudOptionalTypes, specific=giraffeDSL_GeoZoneType)
gen_giraffeDSL_CloudUserType_CloudOptionalTypes = Generalization(general=CloudOptionalTypes, specific=giraffeDSL_CloudUserType)
gen_giraffeDSL_CloudPasswordType_CloudOptionalTypes = Generalization(general=CloudOptionalTypes, specific=giraffeDSL_CloudPasswordType)
gen_giraffeDSL_Deploy_Type = Generalization(general=Type, specific=giraffeDSL_Deploy)
gen_giraffeDSL_Stress_Type = Generalization(general=Type, specific=giraffeDSL_Stress)
gen_giraffeDSL_DeployApp_Type = Generalization(general=Type, specific=giraffeDSL_DeployApp)
gen_giraffeDSL_Monitor_Type = Generalization(general=Type, specific=giraffeDSL_Monitor)
gen_giraffeDSL_Action_Type = Generalization(general=Type, specific=giraffeDSL_Action)

# Domain Model
domain_model = DomainModel(
    name="giraffeDSL",
    types={giraffeDSL_CloudProviderType, giraffeDSL_Type, giraffeDSL_Create, Type, giraffeDSL_VirtualMachineFeature, giraffeDSL_InitMachinesFeature, giraffeDSL_InitIncrementFeature, giraffeDSL_VirtualMachine, giraffeDSL_DomainModel, giraffeDSL_VirtualMachineTypeFeature, giraffeDSL_DeployTypeFeature, giraffeDSL_DeployApp, giraffeDSL_DeployType, giraffeDSL_CloudProvider, giraffeDSL_DeployRangeType, giraffeDSL_CloudType, giraffeDSL_MgmAddressType, giraffeDSL_CloudCredentialType, giraffeDSL_CloudOptionalTypes, giraffeDSL_ScriptType, CloudOptionalTypes, giraffeDSL_GeoZoneType, giraffeDSL_CloudUserType, giraffeDSL_CloudPasswordType, giraffeDSL_Deploy, giraffeDSL_DeployAppFeature, giraffeDSL_Stress, giraffeDSL_StressRangeType, giraffeDSL_StressClassType, giraffeDSL_StressMethodType, giraffeDSL_DeployAppClassType, giraffeDSL_DeployAppMasterMethodType, giraffeDSL_DeployAppSlaveMethodType, giraffeDSL_Monitor, giraffeDSL_MonitorRangeType, giraffeDSL_MonitoringType, giraffeDSL_Action, giraffeDSL_ActionRangeType, giraffeDSL_ActionClassType, giraffeDSL_ActionMethodType, giraffeDSL_Features, giraffeDSL_IntFeature},
    associations={cloudProvider10, elements0, vMachine1, initMachines2, initIncrement4, type6, vM8, deployOne22, deployTwo23, type25, type27, type12, range29, cloudType14, cloudAddress16, cloudCredential18, cloudOptionalTypes20, range40, stressClass41, stressMethod43, class31, deployMasterMethod33, deploySlaveMethod35, range37, monitoringType38, range45, class46, method48},
    generalizations={gen_giraffeDSL_Create_Type, gen_giraffeDSL_VirtualMachine_Type, gen_giraffeDSL_DeployType_Type, gen_giraffeDSL_CloudProvider_Type, gen_giraffeDSL_ScriptType_CloudOptionalTypes, gen_giraffeDSL_GeoZoneType_CloudOptionalTypes, gen_giraffeDSL_CloudUserType_CloudOptionalTypes, gen_giraffeDSL_CloudPasswordType_CloudOptionalTypes, gen_giraffeDSL_Deploy_Type, gen_giraffeDSL_Stress_Type, gen_giraffeDSL_DeployApp_Type, gen_giraffeDSL_Monitor_Type, gen_giraffeDSL_Action_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)