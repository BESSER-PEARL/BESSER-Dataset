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
OperatorType: Enumeration = Enumeration(
    name="OperatorType",
    literals={
            EnumerationLiteral(name="include"),
			EnumerationLiteral(name="exclude")
    }
)

Phase: Enumeration = Enumeration(
    name="Phase",
    literals={
            EnumerationLiteral(name="build"),
			EnumerationLiteral(name="run"),
			EnumerationLiteral(name="both")
    }
)

StatCommand: Enumeration = Enumeration(
    name="StatCommand",
    literals={
            EnumerationLiteral(name="createFolder"),
			EnumerationLiteral(name="removeFolder"),
			EnumerationLiteral(name="listDrives"),
			EnumerationLiteral(name="listFiles"),
			EnumerationLiteral(name="getScreenCapture"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="run"),
			EnumerationLiteral(name="startLogging"),
			EnumerationLiteral(name="stopLogging")
    }
)

# Classes
driver_Build = Class(name="driver_Build")
driver_CmdPC = Class(name="driver_CmdPC")
driver_CmdSymbian = Class(name="driver_CmdSymbian")
driver_DocumentRoot = Class(name="driver_DocumentRoot")
driver_Info = Class(name="driver_Info")
driver_EStringToStringMapEntry = Class(name="driver_EStringToStringMapEntry")
driver_Driver = Class(name="driver_Driver")
driver_DriverInfo = Class(name="driver_DriverInfo")
driver_Task = Class(name="driver_Task")
driver_Rtest = Class(name="driver_Rtest")
driver_ExecuteOnPC = Class(name="driver_ExecuteOnPC")
driver_ExecuteOnSymbian = Class(name="driver_ExecuteOnSymbian")
driver_TestExecuteScript = Class(name="driver_TestExecuteScript")
driver_RetrieveFromSymbian = Class(name="driver_RetrieveFromSymbian")
driver_FlashROM = Class(name="driver_FlashROM")
driver_Reference = Class(name="driver_Reference")
driver_Transfer = Class(name="driver_Transfer")
driver_TransferToSymbian = Class(name="driver_TransferToSymbian")
driver_StartTrace = Class(name="driver_StartTrace")
driver_StopTrace = Class(name="driver_StopTrace")
driver_TestCase = Class(name="driver_TestCase")
driver_TestCasesList = Class(name="driver_TestCasesList")

# driver_Build class attributes and methods
driver_Build_componentName: Property = Property(name="componentName", type=StringType)
driver_Build_testBuild: Property = Property(name="testBuild", type=StringType)
driver_Build_uRI: Property = Property(name="uRI", type=StringType)
driver_Build.attributes={driver_Build_uRI, driver_Build_componentName, driver_Build_testBuild}

# driver_CmdPC class attributes and methods
driver_CmdPC_value: Property = Property(name="value", type=StringType)
driver_CmdPC_phase: Property = Property(name="phase", type=StringType)
driver_CmdPC_sync: Property = Property(name="sync", type=StringType)
driver_CmdPC_uRI: Property = Property(name="uRI", type=StringType)
driver_CmdPC.attributes={driver_CmdPC_value, driver_CmdPC_sync, driver_CmdPC_uRI, driver_CmdPC_phase}

# driver_CmdSymbian class attributes and methods
driver_CmdSymbian_argument: Property = Property(name="argument", type=StringType)
driver_CmdSymbian_output: Property = Property(name="output", type=StringType)
driver_CmdSymbian_statCommand: Property = Property(name="statCommand", type=StringType)
driver_CmdSymbian_sync: Property = Property(name="sync", type=StringType)
driver_CmdSymbian.attributes={driver_CmdSymbian_argument, driver_CmdSymbian_statCommand, driver_CmdSymbian_sync, driver_CmdSymbian_output}

# driver_DocumentRoot class attributes and methods
driver_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
driver_DocumentRoot.attributes={driver_DocumentRoot_mixed}

# driver_Info class attributes and methods
driver_Info_value: Property = Property(name="value", type=StringType)
driver_Info_key: Property = Property(name="key", type=StringType)
driver_Info.attributes={driver_Info_value, driver_Info_key}

# driver_EStringToStringMapEntry class attributes and methods

# driver_Driver class attributes and methods

# driver_DriverInfo class attributes and methods

# driver_Task class attributes and methods
driver_Task_group: Property = Property(name="group", type=StringType)
driver_Task_name: Property = Property(name="name", type=StringType)
driver_Task_preRebootDevice: Property = Property(name="preRebootDevice", type=StringType)
driver_Task_timeout: Property = Property(name="timeout", type=StringType)
driver_Task.attributes={driver_Task_name, driver_Task_preRebootDevice, driver_Task_timeout, driver_Task_group}

# driver_Rtest class attributes and methods
driver_Rtest_resultFile: Property = Property(name="resultFile", type=StringType)
driver_Rtest_symbianPath: Property = Property(name="symbianPath", type=StringType)
driver_Rtest.attributes={driver_Rtest_resultFile, driver_Rtest_symbianPath}

# driver_ExecuteOnPC class attributes and methods
driver_ExecuteOnPC_group: Property = Property(name="group", type=StringType)
driver_ExecuteOnPC.attributes={driver_ExecuteOnPC_group}

# driver_ExecuteOnSymbian class attributes and methods
driver_ExecuteOnSymbian_group: Property = Property(name="group", type=StringType)
driver_ExecuteOnSymbian.attributes={driver_ExecuteOnSymbian_group}

# driver_TestExecuteScript class attributes and methods
driver_TestExecuteScript_pCPath: Property = Property(name="pCPath", type=StringType)
driver_TestExecuteScript_symbianPath: Property = Property(name="symbianPath", type=StringType)
driver_TestExecuteScript.attributes={driver_TestExecuteScript_symbianPath, driver_TestExecuteScript_pCPath}

# driver_RetrieveFromSymbian class attributes and methods
driver_RetrieveFromSymbian_group: Property = Property(name="group", type=StringType)
driver_RetrieveFromSymbian.attributes={driver_RetrieveFromSymbian_group}

# driver_FlashROM class attributes and methods
driver_FlashROM_pCPath: Property = Property(name="pCPath", type=StringType)
driver_FlashROM.attributes={driver_FlashROM_pCPath}

# driver_Reference class attributes and methods

# driver_Transfer class attributes and methods
driver_Transfer_move: Property = Property(name="move", type=StringType)
driver_Transfer_pCPath: Property = Property(name="pCPath", type=StringType)
driver_Transfer_symbianPath: Property = Property(name="symbianPath", type=StringType)
driver_Transfer.attributes={driver_Transfer_symbianPath, driver_Transfer_move, driver_Transfer_pCPath}

# driver_TransferToSymbian class attributes and methods
driver_TransferToSymbian_group: Property = Property(name="group", type=StringType)
driver_TransferToSymbian.attributes={driver_TransferToSymbian_group}

# driver_StartTrace class attributes and methods
driver_StartTrace_enablePrimaryFilters: Property = Property(name="enablePrimaryFilters", type=StringType)
driver_StartTrace_enableSecondaryFilters: Property = Property(name="enableSecondaryFilters", type=StringType)
driver_StartTrace_disablePrimaryFilters: Property = Property(name="disablePrimaryFilters", type=StringType)
driver_StartTrace_disableSecondaryFilters: Property = Property(name="disableSecondaryFilters", type=StringType)
driver_StartTrace_configFilePath: Property = Property(name="configFilePath", type=StringType)
driver_StartTrace.attributes={driver_StartTrace_disablePrimaryFilters, driver_StartTrace_disableSecondaryFilters, driver_StartTrace_enablePrimaryFilters, driver_StartTrace_configFilePath, driver_StartTrace_enableSecondaryFilters}

# driver_StopTrace class attributes and methods

# driver_TestCase class attributes and methods
driver_TestCase_target: Property = Property(name="target", type=StringType)
driver_TestCase.attributes={driver_TestCase_target}

# driver_TestCasesList class attributes and methods
driver_TestCasesList_operator: Property = Property(name="operator", type=StringType)
driver_TestCasesList.attributes={driver_TestCasesList_operator}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="driver_EStringToStringMapEntry", type=driver_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_DocumentRoot", type=driver_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="driver_EStringToStringMapEntry3", type=driver_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_DocumentRoot2", type=driver_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driver4: BinaryAssociation = BinaryAssociation(
    name="driver4",
    ends={
        Property(name="driver_Driver", type=driver_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_DocumentRoot5", type=driver_Driver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driverInfo6: BinaryAssociation = BinaryAssociation(
    name="driverInfo6",
    ends={
        Property(name="driver_DriverInfo", type=driver_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Driver7", type=driver_DriverInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task8: BinaryAssociation = BinaryAssociation(
    name="task8",
    ends={
        Property(name="driver_Task", type=driver_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Driver9", type=driver_Task, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rtest18: BinaryAssociation = BinaryAssociation(
    name="rtest18",
    ends={
        Property(name="driver_Rtest", type=driver_ExecuteOnSymbian, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_ExecuteOnSymbian19", type=driver_Rtest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
info10: BinaryAssociation = BinaryAssociation(
    name="info10",
    ends={
        Property(name="driver_Info", type=driver_DriverInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_DriverInfo11", type=driver_Info, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
cmd12: BinaryAssociation = BinaryAssociation(
    name="cmd12",
    ends={
        Property(name="driver_CmdPC", type=driver_ExecuteOnPC, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_ExecuteOnPC", type=driver_CmdPC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build13: BinaryAssociation = BinaryAssociation(
    name="build13",
    ends={
        Property(name="driver_Build", type=driver_ExecuteOnPC, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_ExecuteOnPC14", type=driver_Build, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmd15: BinaryAssociation = BinaryAssociation(
    name="cmd15",
    ends={
        Property(name="driver_CmdSymbian", type=driver_ExecuteOnSymbian, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_ExecuteOnSymbian", type=driver_CmdSymbian, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testExecuteScript16: BinaryAssociation = BinaryAssociation(
    name="testExecuteScript16",
    ends={
        Property(name="driver_TestExecuteScript", type=driver_ExecuteOnSymbian, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_ExecuteOnSymbian17", type=driver_TestExecuteScript, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uri20: BinaryAssociation = BinaryAssociation(
    name="uri20",
    ends={
        Property(name="driver_Task21", type=driver_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Reference", type=driver_Task, multiplicity=Multiplicity(0, 1))
    }
)
transfer22: BinaryAssociation = BinaryAssociation(
    name="transfer22",
    ends={
        Property(name="driver_Transfer", type=driver_RetrieveFromSymbian, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_RetrieveFromSymbian", type=driver_Transfer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
flashrom40: BinaryAssociation = BinaryAssociation(
    name="flashrom40",
    ends={
        Property(name="driver_FlashROM", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task41", type=driver_FlashROM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executeOnPC23: BinaryAssociation = BinaryAssociation(
    name="executeOnPC23",
    ends={
        Property(name="driver_ExecuteOnPC25", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task24", type=driver_ExecuteOnPC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transferToSymbian26: BinaryAssociation = BinaryAssociation(
    name="transferToSymbian26",
    ends={
        Property(name="driver_TransferToSymbian", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task27", type=driver_TransferToSymbian, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executeOnSymbian28: BinaryAssociation = BinaryAssociation(
    name="executeOnSymbian28",
    ends={
        Property(name="driver_ExecuteOnSymbian30", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task29", type=driver_ExecuteOnSymbian, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
retrieveFromSymbian31: BinaryAssociation = BinaryAssociation(
    name="retrieveFromSymbian31",
    ends={
        Property(name="driver_RetrieveFromSymbian33", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task32", type=driver_RetrieveFromSymbian, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference34: BinaryAssociation = BinaryAssociation(
    name="reference34",
    ends={
        Property(name="driver_Reference36", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task35", type=driver_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task38: BinaryAssociation = BinaryAssociation(
    name="task38",
    ends={
        Property(name="driver_Task39", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task37", type=driver_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startTrace42: BinaryAssociation = BinaryAssociation(
    name="startTrace42",
    ends={
        Property(name="driver_StartTrace", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task43", type=driver_StartTrace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stopTrace44: BinaryAssociation = BinaryAssociation(
    name="stopTrace44",
    ends={
        Property(name="driver_StopTrace", type=driver_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_Task45", type=driver_StopTrace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testCase46: BinaryAssociation = BinaryAssociation(
    name="testCase46",
    ends={
        Property(name="driver_TestCase", type=driver_TestCasesList, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_TestCasesList", type=driver_TestCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
testCasesList47: BinaryAssociation = BinaryAssociation(
    name="testCasesList47",
    ends={
        Property(name="driver_TestCasesList49", type=driver_TestExecuteScript, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_TestExecuteScript48", type=driver_TestCasesList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transfer50: BinaryAssociation = BinaryAssociation(
    name="transfer50",
    ends={
        Property(name="driver_Transfer52", type=driver_TransferToSymbian, multiplicity=Multiplicity(1, 1)),
        Property(name="driver_TransferToSymbian51", type=driver_Transfer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="driver",
    types={driver_Build, driver_CmdPC, driver_CmdSymbian, driver_DocumentRoot, driver_Info, driver_EStringToStringMapEntry, driver_Driver, driver_DriverInfo, driver_Task, driver_Rtest, driver_ExecuteOnPC, driver_ExecuteOnSymbian, driver_TestExecuteScript, driver_RetrieveFromSymbian, driver_FlashROM, driver_Reference, driver_Transfer, driver_TransferToSymbian, driver_StartTrace, driver_StopTrace, driver_TestCase, driver_TestCasesList, OperatorType, Phase, StatCommand},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, driver4, driverInfo6, task8, rtest18, info10, cmd12, build13, cmd15, testExecuteScript16, uri20, transfer22, flashrom40, executeOnPC23, transferToSymbian26, executeOnSymbian28, retrieveFromSymbian31, reference34, task38, startTrace42, stopTrace44, testCase46, testCasesList47, transfer50},
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