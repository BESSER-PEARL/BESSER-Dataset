import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MachineLibrary_RobotToWinCC,
    MachineLibrary_RobotWinCCToRobot,
    MachineLibrary_RobotConfSendOrder,
    MachineLibrary_RobotVarToBusycode,
    MachineLibrary_RobotVarToErrorbit,
    MachineLibrary_PlainMoveEntrySend,
    MachineLibrary_TransferFileSection,
    MachineLibrary_RobotConfiguration,
    MachineLibrary_RobotVarToErrorbits,
    MachineLibrary_RobotWarningONDelete,
    MachineLibrary_RobotToWinccs,
    MachineLibrary_RobotWinCCToRobots,
    MachineLibrary_RobotConfSendOrders,
    MachineLibrary_RobotVarToBusyCodes,
    MachineLibrary_Parameter,
    MachineLibrary_PlainMove,
    MachineLibrary_Transfer,
    MachineLibrary_ParamPrint,
    MachineLibrary_NodeProgram,
    MachineLibrary_Command,
    MachineLibrary_UnitProgParameters,
    MachineLibrary_UnitProgram,
    MachineLibrary_Position,
    MachineLibrary_Button,
    MachineLibrary_CheckAddSID_Values_PM2PM,
    MachineLibrary_SepByComma_ID_Scanner,
    MachineLibrary_SepByComma_Field_Scanner,
    MachineLibrary_StatusBit,
    MachineLibrary_HistoryConfig_AccuPyc,
    MachineLibrary_CheckSampleConfig_SuperQXRF,
    MachineLibrary_InsertRemove_Keywords_Host,
    MachineLibrary_InsertRemove_Types_Host,
    MachineLibrary_InsertRemove_Entry_Host,
    MachineLibrary_CheckSampleRunTimeParams_SuperQXRF,
    MachineLibrary_OES_XRF_Condition,
    MachineLibrary_InsertRemove_Host,
    MachineLibrary_Moved_Host,
    MachineLibrary_WS_Update_Host,
    MachineLibrary_Report_Host,
    MachineLibrary_Settings_ARL_XRF_OES,
    MachineLibrary_DisableSCT_ARL_XRF_OES,
    MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES,
    MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES,
    MachineLibrary_ExePrepUnit_ARL_XRF_OES,
    MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES,
    MachineLibrary_ExecuteFiling_ARL_XRF_OES,
    MachineLibrary_CheckFilling_ARL_XRF_OES,
    MachineLibrary_CheckSample_SuperQXRF,
    MachineLibrary_CheckSampleRunTime_SuperQXRF,
    MachineLibrary_Communication_SuperQXRF,
    MachineLibrary_ControlSamples_SuperQXRF,
    MachineLibrary_File_Sample_ARL_XRF_OES,
    MachineLibrary_PS_Process_Finished_ARL_XRF_OES,
    MachineLibrary_GeneralSetting_ARL_XRF_OES,
    MachineLibrary_CheckAddSID_PM2PM,
    MachineLibrary_SepByComma_Scanner,
    MachineLibrary_History_AccuPycMeter,
    MachineLibrary_UnitConfig_Host,
    MachineLibrary_UnitConfig_ARL_XRF_OES,
    MachineLibrary_UnitConfig_SuperQ_XRF,
    MachineLibrary_UnitConfig_OBLF_OES,
    MachineLibrary_UnitConfig_Terminal,
    MachineLibrary_GeneralParameter_SuperQXRF,
    MachineLibrary_ErrorMessage_OBLFOES,
    MachineLibrary_RecalRequest_OBLFOES,
    MachineLibrary_TestRequest_OBLFOES,
    MachineLibrary_OutputRequest_OBLFOES,
    MachineLibrary_Translate_Terminal,
    MachineLibrary_UnitGeneral_Scanner,
    MachineLibrary_UnitGeneral_RigakuXRF,
    MachineLibrary_UnitGeneral_SuperQ,
    MachineLibrary_UnitGeneral_AccPyc,
    MachineLibrary_UnitGeneral_PM2PM,
    MachineLibrary_UnitGeneral_Remote,
    MachineLibrary_UnitGeneral_HostPC,
    MachineLibrary_UnitGeneral_Terminal,
    MachineLibrary_PLCtoPmMatrix,
    MachineLibrary_StausBits,
    MachineLibrary_Positions,
    MachineLibrary_WinCCAddTag,
    MachineLibrary_UnitGeneralParameters,
    MachineLibrary_UnitSpecialConfiguration,
    MachineLibrary_UnitGeneralSpecial,
    MachineLibrary_UnitGeneral,
    MachineLibrary_Buttons,
    MachineLibrary_UnitPrograms,
    MachineLibrary_NodeGeneral_RigakuXRF,
    MachineLibrary_NodeGeneral_AccuPycMeter,
    MachineLibrary_NodeGeneral_WinCC2WinCC,
    MachineLibrary_NodeGeneral_RemotePM,
    MachineLibrary_NodeGeneral_PM2PM,
    MachineLibrary_NodeGeneral_Terminal,
    MachineLibrary_NodeGeneralSpecial,
    MachineLibrary_NodeGeneral,
    MachineLibrary_NodeSpecialConfiguration,
    MachineLibrary_CommunicationData,
    MachineLibrary_Parameters,
    MachineLibrary_NodePrograms,
    MachineLibrary_Commands,
    MachineLibrary_Units,
    MachineLibrary_DPbase_Node,
    MachineLibrary_Compac_Link,
    MachineLibrary_FileTransfer_Link,
    MachineLibrary_Serial_Link,
    MachineLibrary_TCPIP_Link,
    MachineLibrary_WinCCLnk,
    MachineLibrary_LinkConfig,
    MachineLibrary_NodeConfig,
    MachineLibrary_Link2,
    MachineLibrary_DPbase_Link,
    MachineLibrary_IBMWebsphereMQ,
    MachineLibrary_LabMachine,
    MachineLibrary_LabMachines,
    MachineLibrary_PMMachineLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_machinelibrary_robottowincc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotToWinCC)


def test_machinelibrary_robottowincc_constructor_exists():
    assert callable(MachineLibrary_RobotToWinCC.__init__)


def test_machinelibrary_robottowincc_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotToWinCC.__init__)
    params = list(sig.parameters.keys())
    assert "robotToWinccSeq_X" in params, "Missing parameter 'robotToWinccSeq_X'"
    assert "robotToWinccType_X" in params, "Missing parameter 'robotToWinccType_X'"
    assert "robotToWinccTo_X" in params, "Missing parameter 'robotToWinccTo_X'"
    assert "robotToWinccFrom_X" in params, "Missing parameter 'robotToWinccFrom_X'"

def test_machinelibrary_robottowincc_has_robotToWinccSeq_X():
    assert hasattr(MachineLibrary_RobotToWinCC, "robotToWinccSeq_X")
    descriptor = None
    for klass in MachineLibrary_RobotToWinCC.__mro__:
        if "robotToWinccSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robottowincc_has_robotToWinccType_X():
    assert hasattr(MachineLibrary_RobotToWinCC, "robotToWinccType_X")
    descriptor = None
    for klass in MachineLibrary_RobotToWinCC.__mro__:
        if "robotToWinccType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robottowincc_has_robotToWinccTo_X():
    assert hasattr(MachineLibrary_RobotToWinCC, "robotToWinccTo_X")
    descriptor = None
    for klass in MachineLibrary_RobotToWinCC.__mro__:
        if "robotToWinccTo_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccTo_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robottowincc_has_robotToWinccFrom_X():
    assert hasattr(MachineLibrary_RobotToWinCC, "robotToWinccFrom_X")
    descriptor = None
    for klass in MachineLibrary_RobotToWinCC.__mro__:
        if "robotToWinccFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccFrom_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotwincctorobot_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotWinCCToRobot)


def test_machinelibrary_robotwincctorobot_constructor_exists():
    assert callable(MachineLibrary_RobotWinCCToRobot.__init__)


def test_machinelibrary_robotwincctorobot_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotWinCCToRobot.__init__)
    params = list(sig.parameters.keys())
    assert "robotwincctorobotTo_X" in params, "Missing parameter 'robotwincctorobotTo_X'"
    assert "robotwincctorobootType_X" in params, "Missing parameter 'robotwincctorobootType_X'"
    assert "robotwincctorobotFrom_X" in params, "Missing parameter 'robotwincctorobotFrom_X'"
    assert "robotwincctorobootSeq_X" in params, "Missing parameter 'robotwincctorobootSeq_X'"

def test_machinelibrary_robotwincctorobot_has_robotwincctorobotTo_X():
    assert hasattr(MachineLibrary_RobotWinCCToRobot, "robotwincctorobotTo_X")
    descriptor = None
    for klass in MachineLibrary_RobotWinCCToRobot.__mro__:
        if "robotwincctorobotTo_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobotTo_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwincctorobot_has_robotwincctorobootType_X():
    assert hasattr(MachineLibrary_RobotWinCCToRobot, "robotwincctorobootType_X")
    descriptor = None
    for klass in MachineLibrary_RobotWinCCToRobot.__mro__:
        if "robotwincctorobootType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobootType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwincctorobot_has_robotwincctorobotFrom_X():
    assert hasattr(MachineLibrary_RobotWinCCToRobot, "robotwincctorobotFrom_X")
    descriptor = None
    for klass in MachineLibrary_RobotWinCCToRobot.__mro__:
        if "robotwincctorobotFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobotFrom_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwincctorobot_has_robotwincctorobootSeq_X():
    assert hasattr(MachineLibrary_RobotWinCCToRobot, "robotwincctorobootSeq_X")
    descriptor = None
    for klass in MachineLibrary_RobotWinCCToRobot.__mro__:
        if "robotwincctorobootSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobootSeq_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotconfsendorder_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotConfSendOrder)


def test_machinelibrary_robotconfsendorder_constructor_exists():
    assert callable(MachineLibrary_RobotConfSendOrder.__init__)


def test_machinelibrary_robotconfsendorder_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotConfSendOrder.__init__)
    params = list(sig.parameters.keys())
    assert "robotconfsendorderVar_X" in params, "Missing parameter 'robotconfsendorderVar_X'"
    assert "robotconfsendorderType_X" in params, "Missing parameter 'robotconfsendorderType_X'"
    assert "robotconfsendorderSeq_X" in params, "Missing parameter 'robotconfsendorderSeq_X'"
    assert "robotconfsendorderFrom_X" in params, "Missing parameter 'robotconfsendorderFrom_X'"

def test_machinelibrary_robotconfsendorder_has_robotconfsendorderVar_X():
    assert hasattr(MachineLibrary_RobotConfSendOrder, "robotconfsendorderVar_X")
    descriptor = None
    for klass in MachineLibrary_RobotConfSendOrder.__mro__:
        if "robotconfsendorderVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderVar_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfsendorder_has_robotconfsendorderType_X():
    assert hasattr(MachineLibrary_RobotConfSendOrder, "robotconfsendorderType_X")
    descriptor = None
    for klass in MachineLibrary_RobotConfSendOrder.__mro__:
        if "robotconfsendorderType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfsendorder_has_robotconfsendorderSeq_X():
    assert hasattr(MachineLibrary_RobotConfSendOrder, "robotconfsendorderSeq_X")
    descriptor = None
    for klass in MachineLibrary_RobotConfSendOrder.__mro__:
        if "robotconfsendorderSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfsendorder_has_robotconfsendorderFrom_X():
    assert hasattr(MachineLibrary_RobotConfSendOrder, "robotconfsendorderFrom_X")
    descriptor = None
    for klass in MachineLibrary_RobotConfSendOrder.__mro__:
        if "robotconfsendorderFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderFrom_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotvartobusycode_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotVarToBusycode)


def test_machinelibrary_robotvartobusycode_constructor_exists():
    assert callable(MachineLibrary_RobotVarToBusycode.__init__)


def test_machinelibrary_robotvartobusycode_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotVarToBusycode.__init__)
    params = list(sig.parameters.keys())
    assert "robotvartobusycodeSeq_X" in params, "Missing parameter 'robotvartobusycodeSeq_X'"
    assert "robotvartobusycodeType_X" in params, "Missing parameter 'robotvartobusycodeType_X'"
    assert "robotvartobusycodeVar_X" in params, "Missing parameter 'robotvartobusycodeVar_X'"
    assert "robotvartobusycodeUnit_X" in params, "Missing parameter 'robotvartobusycodeUnit_X'"
    assert "robotvartobusycodeBit_X" in params, "Missing parameter 'robotvartobusycodeBit_X'"

def test_machinelibrary_robotvartobusycode_has_robotvartobusycodeSeq_X():
    assert hasattr(MachineLibrary_RobotVarToBusycode, "robotvartobusycodeSeq_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToBusycode.__mro__:
        if "robotvartobusycodeSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartobusycode_has_robotvartobusycodeType_X():
    assert hasattr(MachineLibrary_RobotVarToBusycode, "robotvartobusycodeType_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToBusycode.__mro__:
        if "robotvartobusycodeType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartobusycode_has_robotvartobusycodeVar_X():
    assert hasattr(MachineLibrary_RobotVarToBusycode, "robotvartobusycodeVar_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToBusycode.__mro__:
        if "robotvartobusycodeVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeVar_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartobusycode_has_robotvartobusycodeUnit_X():
    assert hasattr(MachineLibrary_RobotVarToBusycode, "robotvartobusycodeUnit_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToBusycode.__mro__:
        if "robotvartobusycodeUnit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeUnit_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartobusycode_has_robotvartobusycodeBit_X():
    assert hasattr(MachineLibrary_RobotVarToBusycode, "robotvartobusycodeBit_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToBusycode.__mro__:
        if "robotvartobusycodeBit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeBit_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotvartoerrorbit_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotVarToErrorbit)


def test_machinelibrary_robotvartoerrorbit_constructor_exists():
    assert callable(MachineLibrary_RobotVarToErrorbit.__init__)


def test_machinelibrary_robotvartoerrorbit_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotVarToErrorbit.__init__)
    params = list(sig.parameters.keys())
    assert "robotvartoerrorbitSeq_X" in params, "Missing parameter 'robotvartoerrorbitSeq_X'"
    assert "robotvartoerrorbitType_X" in params, "Missing parameter 'robotvartoerrorbitType_X'"
    assert "robotvartoerrorbitBit_X" in params, "Missing parameter 'robotvartoerrorbitBit_X'"
    assert "robotvartoerrorbitVar_X" in params, "Missing parameter 'robotvartoerrorbitVar_X'"
    assert "robotvartoerrorbitInv_X" in params, "Missing parameter 'robotvartoerrorbitInv_X'"

def test_machinelibrary_robotvartoerrorbit_has_robotvartoerrorbitSeq_X():
    assert hasattr(MachineLibrary_RobotVarToErrorbit, "robotvartoerrorbitSeq_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartoerrorbit_has_robotvartoerrorbitType_X():
    assert hasattr(MachineLibrary_RobotVarToErrorbit, "robotvartoerrorbitType_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartoerrorbit_has_robotvartoerrorbitBit_X():
    assert hasattr(MachineLibrary_RobotVarToErrorbit, "robotvartoerrorbitBit_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitBit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitBit_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartoerrorbit_has_robotvartoerrorbitVar_X():
    assert hasattr(MachineLibrary_RobotVarToErrorbit, "robotvartoerrorbitVar_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitVar_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotvartoerrorbit_has_robotvartoerrorbitInv_X():
    assert hasattr(MachineLibrary_RobotVarToErrorbit, "robotvartoerrorbitInv_X")
    descriptor = None
    for klass in MachineLibrary_RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitInv_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitInv_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_plainmoveentrysend_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_PlainMoveEntrySend)


def test_machinelibrary_plainmoveentrysend_constructor_exists():
    assert callable(MachineLibrary_PlainMoveEntrySend.__init__)


def test_machinelibrary_plainmoveentrysend_constructor_args():
    sig = inspect.signature(MachineLibrary_PlainMoveEntrySend.__init__)
    params = list(sig.parameters.keys())
    assert "plainmoveSeq" in params, "Missing parameter 'plainmoveSeq'"
    assert "plainmoveEntry" in params, "Missing parameter 'plainmoveEntry'"
    assert "plainmoveSend" in params, "Missing parameter 'plainmoveSend'"

def test_machinelibrary_plainmoveentrysend_has_plainmoveSeq():
    assert hasattr(MachineLibrary_PlainMoveEntrySend, "plainmoveSeq")
    descriptor = None
    for klass in MachineLibrary_PlainMoveEntrySend.__mro__:
        if "plainmoveSeq" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSeq"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plainmoveentrysend_has_plainmoveEntry():
    assert hasattr(MachineLibrary_PlainMoveEntrySend, "plainmoveEntry")
    descriptor = None
    for klass in MachineLibrary_PlainMoveEntrySend.__mro__:
        if "plainmoveEntry" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveEntry"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plainmoveentrysend_has_plainmoveSend():
    assert hasattr(MachineLibrary_PlainMoveEntrySend, "plainmoveSend")
    descriptor = None
    for klass in MachineLibrary_PlainMoveEntrySend.__mro__:
        if "plainmoveSend" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSend"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_transferfilesection_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_TransferFileSection)


def test_machinelibrary_transferfilesection_constructor_exists():
    assert callable(MachineLibrary_TransferFileSection.__init__)


def test_machinelibrary_transferfilesection_constructor_args():
    sig = inspect.signature(MachineLibrary_TransferFileSection.__init__)
    params = list(sig.parameters.keys())
    assert "transferSection" in params, "Missing parameter 'transferSection'"
    assert "transferFile" in params, "Missing parameter 'transferFile'"
    assert "transferSeq" in params, "Missing parameter 'transferSeq'"

def test_machinelibrary_transferfilesection_has_transferSection():
    assert hasattr(MachineLibrary_TransferFileSection, "transferSection")
    descriptor = None
    for klass in MachineLibrary_TransferFileSection.__mro__:
        if "transferSection" in klass.__dict__:
            descriptor = klass.__dict__["transferSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_transferfilesection_has_transferFile():
    assert hasattr(MachineLibrary_TransferFileSection, "transferFile")
    descriptor = None
    for klass in MachineLibrary_TransferFileSection.__mro__:
        if "transferFile" in klass.__dict__:
            descriptor = klass.__dict__["transferFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_transferfilesection_has_transferSeq():
    assert hasattr(MachineLibrary_TransferFileSection, "transferSeq")
    descriptor = None
    for klass in MachineLibrary_TransferFileSection.__mro__:
        if "transferSeq" in klass.__dict__:
            descriptor = klass.__dict__["transferSeq"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotConfiguration)


def test_machinelibrary_robotconfiguration_constructor_exists():
    assert callable(MachineLibrary_RobotConfiguration.__init__)


def test_machinelibrary_robotconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "robotIPAddress" in params, "Missing parameter 'robotIPAddress'"
    assert "robotSystemID" in params, "Missing parameter 'robotSystemID'"
    assert "robotActivate" in params, "Missing parameter 'robotActivate'"
    assert "robotID" in params, "Missing parameter 'robotID'"

def test_machinelibrary_robotconfiguration_has_robotIPAddress():
    assert hasattr(MachineLibrary_RobotConfiguration, "robotIPAddress")
    descriptor = None
    for klass in MachineLibrary_RobotConfiguration.__mro__:
        if "robotIPAddress" in klass.__dict__:
            descriptor = klass.__dict__["robotIPAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfiguration_has_robotSystemID():
    assert hasattr(MachineLibrary_RobotConfiguration, "robotSystemID")
    descriptor = None
    for klass in MachineLibrary_RobotConfiguration.__mro__:
        if "robotSystemID" in klass.__dict__:
            descriptor = klass.__dict__["robotSystemID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfiguration_has_robotActivate():
    assert hasattr(MachineLibrary_RobotConfiguration, "robotActivate")
    descriptor = None
    for klass in MachineLibrary_RobotConfiguration.__mro__:
        if "robotActivate" in klass.__dict__:
            descriptor = klass.__dict__["robotActivate"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotconfiguration_has_robotID():
    assert hasattr(MachineLibrary_RobotConfiguration, "robotID")
    descriptor = None
    for klass in MachineLibrary_RobotConfiguration.__mro__:
        if "robotID" in klass.__dict__:
            descriptor = klass.__dict__["robotID"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robotvartoerrorbits_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotVarToErrorbits)


def test_machinelibrary_robotvartoerrorbits_constructor_exists():
    assert callable(MachineLibrary_RobotVarToErrorbits.__init__)


def test_machinelibrary_robotvartoerrorbits_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotVarToErrorbits.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_robotwarningondelete_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotWarningONDelete)


def test_machinelibrary_robotwarningondelete_constructor_exists():
    assert callable(MachineLibrary_RobotWarningONDelete.__init__)


def test_machinelibrary_robotwarningondelete_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotWarningONDelete.__init__)
    params = list(sig.parameters.keys())
    assert "robotExtraUnit_2" in params, "Missing parameter 'robotExtraUnit_2'"
    assert "robotExtraPos_1" in params, "Missing parameter 'robotExtraPos_1'"
    assert "robotErrBitWhenConfirmationIsNeededFor_PM" in params, "Missing parameter 'robotErrBitWhenConfirmationIsNeededFor_PM'"
    assert "robotErrBitWhenConfirmationIsNeededFor_Robot" in params, "Missing parameter 'robotErrBitWhenConfirmationIsNeededFor_Robot'"

def test_machinelibrary_robotwarningondelete_has_robotExtraUnit_2():
    assert hasattr(MachineLibrary_RobotWarningONDelete, "robotExtraUnit_2")
    descriptor = None
    for klass in MachineLibrary_RobotWarningONDelete.__mro__:
        if "robotExtraUnit_2" in klass.__dict__:
            descriptor = klass.__dict__["robotExtraUnit_2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwarningondelete_has_robotExtraPos_1():
    assert hasattr(MachineLibrary_RobotWarningONDelete, "robotExtraPos_1")
    descriptor = None
    for klass in MachineLibrary_RobotWarningONDelete.__mro__:
        if "robotExtraPos_1" in klass.__dict__:
            descriptor = klass.__dict__["robotExtraPos_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwarningondelete_has_robotErrBitWhenConfirmationIsNeededFor_PM():
    assert hasattr(MachineLibrary_RobotWarningONDelete, "robotErrBitWhenConfirmationIsNeededFor_PM")
    descriptor = None
    for klass in MachineLibrary_RobotWarningONDelete.__mro__:
        if "robotErrBitWhenConfirmationIsNeededFor_PM" in klass.__dict__:
            descriptor = klass.__dict__["robotErrBitWhenConfirmationIsNeededFor_PM"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_robotwarningondelete_has_robotErrBitWhenConfirmationIsNeededFor_Robot():
    assert hasattr(MachineLibrary_RobotWarningONDelete, "robotErrBitWhenConfirmationIsNeededFor_Robot")
    descriptor = None
    for klass in MachineLibrary_RobotWarningONDelete.__mro__:
        if "robotErrBitWhenConfirmationIsNeededFor_Robot" in klass.__dict__:
            descriptor = klass.__dict__["robotErrBitWhenConfirmationIsNeededFor_Robot"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_robottowinccs_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotToWinccs)


def test_machinelibrary_robottowinccs_constructor_exists():
    assert callable(MachineLibrary_RobotToWinccs.__init__)


def test_machinelibrary_robottowinccs_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotToWinccs.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_robotwincctorobots_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotWinCCToRobots)


def test_machinelibrary_robotwincctorobots_constructor_exists():
    assert callable(MachineLibrary_RobotWinCCToRobots.__init__)


def test_machinelibrary_robotwincctorobots_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotWinCCToRobots.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_robotconfsendorders_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotConfSendOrders)


def test_machinelibrary_robotconfsendorders_constructor_exists():
    assert callable(MachineLibrary_RobotConfSendOrders.__init__)


def test_machinelibrary_robotconfsendorders_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotConfSendOrders.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_robotvartobusycodes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RobotVarToBusyCodes)


def test_machinelibrary_robotvartobusycodes_constructor_exists():
    assert callable(MachineLibrary_RobotVarToBusyCodes.__init__)


def test_machinelibrary_robotvartobusycodes_constructor_args():
    sig = inspect.signature(MachineLibrary_RobotVarToBusyCodes.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_parameter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Parameter)


def test_machinelibrary_parameter_constructor_exists():
    assert callable(MachineLibrary_Parameter.__init__)


def test_machinelibrary_parameter_constructor_args():
    sig = inspect.signature(MachineLibrary_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterConfig" in params, "Missing parameter 'parameterConfig'"
    assert "parameterParaLen" in params, "Missing parameter 'parameterParaLen'"
    assert "parameterT1" in params, "Missing parameter 'parameterT1'"
    assert "parameterMin" in params, "Missing parameter 'parameterMin'"
    assert "parameterT2" in params, "Missing parameter 'parameterT2'"
    assert "parameterV" in params, "Missing parameter 'parameterV'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"
    assert "parameterV0" in params, "Missing parameter 'parameterV0'"
    assert "parameterV1" in params, "Missing parameter 'parameterV1'"
    assert "parameterMax" in params, "Missing parameter 'parameterMax'"
    assert "parameterType" in params, "Missing parameter 'parameterType'"

def test_machinelibrary_parameter_has_parameterConfig():
    assert hasattr(MachineLibrary_Parameter, "parameterConfig")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterConfig" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterParaLen():
    assert hasattr(MachineLibrary_Parameter, "parameterParaLen")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterParaLen" in klass.__dict__:
            descriptor = klass.__dict__["parameterParaLen"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterT1():
    assert hasattr(MachineLibrary_Parameter, "parameterT1")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterT1" in klass.__dict__:
            descriptor = klass.__dict__["parameterT1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterMin():
    assert hasattr(MachineLibrary_Parameter, "parameterMin")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterMin" in klass.__dict__:
            descriptor = klass.__dict__["parameterMin"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterT2():
    assert hasattr(MachineLibrary_Parameter, "parameterT2")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterT2" in klass.__dict__:
            descriptor = klass.__dict__["parameterT2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterV():
    assert hasattr(MachineLibrary_Parameter, "parameterV")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterV" in klass.__dict__:
            descriptor = klass.__dict__["parameterV"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterName():
    assert hasattr(MachineLibrary_Parameter, "parameterName")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterV0():
    assert hasattr(MachineLibrary_Parameter, "parameterV0")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterV0" in klass.__dict__:
            descriptor = klass.__dict__["parameterV0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterV1():
    assert hasattr(MachineLibrary_Parameter, "parameterV1")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterV1" in klass.__dict__:
            descriptor = klass.__dict__["parameterV1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterMax():
    assert hasattr(MachineLibrary_Parameter, "parameterMax")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterMax" in klass.__dict__:
            descriptor = klass.__dict__["parameterMax"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameter_has_parameterType():
    assert hasattr(MachineLibrary_Parameter, "parameterType")
    descriptor = None
    for klass in MachineLibrary_Parameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_plainmove_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_PlainMove)


def test_machinelibrary_plainmove_constructor_exists():
    assert callable(MachineLibrary_PlainMove.__init__)


def test_machinelibrary_plainmove_constructor_args():
    sig = inspect.signature(MachineLibrary_PlainMove.__init__)
    params = list(sig.parameters.keys())
    assert "plainmovePreDefWS" in params, "Missing parameter 'plainmovePreDefWS'"
    assert "plainmoveSID_REF" in params, "Missing parameter 'plainmoveSID_REF'"
    assert "plainmoveType" in params, "Missing parameter 'plainmoveType'"

def test_machinelibrary_plainmove_has_plainmovePreDefWS():
    assert hasattr(MachineLibrary_PlainMove, "plainmovePreDefWS")
    descriptor = None
    for klass in MachineLibrary_PlainMove.__mro__:
        if "plainmovePreDefWS" in klass.__dict__:
            descriptor = klass.__dict__["plainmovePreDefWS"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plainmove_has_plainmoveSID_REF():
    assert hasattr(MachineLibrary_PlainMove, "plainmoveSID_REF")
    descriptor = None
    for klass in MachineLibrary_PlainMove.__mro__:
        if "plainmoveSID_REF" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSID_REF"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plainmove_has_plainmoveType():
    assert hasattr(MachineLibrary_PlainMove, "plainmoveType")
    descriptor = None
    for klass in MachineLibrary_PlainMove.__mro__:
        if "plainmoveType" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_transfer_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Transfer)


def test_machinelibrary_transfer_constructor_exists():
    assert callable(MachineLibrary_Transfer.__init__)


def test_machinelibrary_transfer_constructor_args():
    sig = inspect.signature(MachineLibrary_Transfer.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_paramprint_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ParamPrint)


def test_machinelibrary_paramprint_constructor_exists():
    assert callable(MachineLibrary_ParamPrint.__init__)


def test_machinelibrary_paramprint_constructor_args():
    sig = inspect.signature(MachineLibrary_ParamPrint.__init__)
    params = list(sig.parameters.keys())
    assert "vertPosData" in params, "Missing parameter 'vertPosData'"
    assert "horzPosValues" in params, "Missing parameter 'horzPosValues'"
    assert "horzPosLeftBorder" in params, "Missing parameter 'horzPosLeftBorder'"
    assert "vertPosHeader" in params, "Missing parameter 'vertPosHeader'"
    assert "dateStamp" in params, "Missing parameter 'dateStamp'"
    assert "vertLineSpace" in params, "Missing parameter 'vertLineSpace'"
    assert "fontHightData" in params, "Missing parameter 'fontHightData'"
    assert "fontHightHeader" in params, "Missing parameter 'fontHightHeader'"

def test_machinelibrary_paramprint_has_vertPosData():
    assert hasattr(MachineLibrary_ParamPrint, "vertPosData")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "vertPosData" in klass.__dict__:
            descriptor = klass.__dict__["vertPosData"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_horzPosValues():
    assert hasattr(MachineLibrary_ParamPrint, "horzPosValues")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "horzPosValues" in klass.__dict__:
            descriptor = klass.__dict__["horzPosValues"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_horzPosLeftBorder():
    assert hasattr(MachineLibrary_ParamPrint, "horzPosLeftBorder")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "horzPosLeftBorder" in klass.__dict__:
            descriptor = klass.__dict__["horzPosLeftBorder"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_vertPosHeader():
    assert hasattr(MachineLibrary_ParamPrint, "vertPosHeader")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "vertPosHeader" in klass.__dict__:
            descriptor = klass.__dict__["vertPosHeader"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_dateStamp():
    assert hasattr(MachineLibrary_ParamPrint, "dateStamp")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "dateStamp" in klass.__dict__:
            descriptor = klass.__dict__["dateStamp"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_vertLineSpace():
    assert hasattr(MachineLibrary_ParamPrint, "vertLineSpace")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "vertLineSpace" in klass.__dict__:
            descriptor = klass.__dict__["vertLineSpace"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_fontHightData():
    assert hasattr(MachineLibrary_ParamPrint, "fontHightData")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "fontHightData" in klass.__dict__:
            descriptor = klass.__dict__["fontHightData"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_paramprint_has_fontHightHeader():
    assert hasattr(MachineLibrary_ParamPrint, "fontHightHeader")
    descriptor = None
    for klass in MachineLibrary_ParamPrint.__mro__:
        if "fontHightHeader" in klass.__dict__:
            descriptor = klass.__dict__["fontHightHeader"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodeprogram_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeProgram)


def test_machinelibrary_nodeprogram_constructor_exists():
    assert callable(MachineLibrary_NodeProgram.__init__)


def test_machinelibrary_nodeprogram_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeProgram.__init__)
    params = list(sig.parameters.keys())
    assert "programSection" in params, "Missing parameter 'programSection'"
    assert "programNo" in params, "Missing parameter 'programNo'"
    assert "programAddress" in params, "Missing parameter 'programAddress'"
    assert "programName" in params, "Missing parameter 'programName'"
    assert "programLenPerParam" in params, "Missing parameter 'programLenPerParam'"

def test_machinelibrary_nodeprogram_has_programSection():
    assert hasattr(MachineLibrary_NodeProgram, "programSection")
    descriptor = None
    for klass in MachineLibrary_NodeProgram.__mro__:
        if "programSection" in klass.__dict__:
            descriptor = klass.__dict__["programSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeprogram_has_programNo():
    assert hasattr(MachineLibrary_NodeProgram, "programNo")
    descriptor = None
    for klass in MachineLibrary_NodeProgram.__mro__:
        if "programNo" in klass.__dict__:
            descriptor = klass.__dict__["programNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeprogram_has_programAddress():
    assert hasattr(MachineLibrary_NodeProgram, "programAddress")
    descriptor = None
    for klass in MachineLibrary_NodeProgram.__mro__:
        if "programAddress" in klass.__dict__:
            descriptor = klass.__dict__["programAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeprogram_has_programName():
    assert hasattr(MachineLibrary_NodeProgram, "programName")
    descriptor = None
    for klass in MachineLibrary_NodeProgram.__mro__:
        if "programName" in klass.__dict__:
            descriptor = klass.__dict__["programName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeprogram_has_programLenPerParam():
    assert hasattr(MachineLibrary_NodeProgram, "programLenPerParam")
    descriptor = None
    for klass in MachineLibrary_NodeProgram.__mro__:
        if "programLenPerParam" in klass.__dict__:
            descriptor = klass.__dict__["programLenPerParam"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_command_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Command)


def test_machinelibrary_command_constructor_exists():
    assert callable(MachineLibrary_Command.__init__)


def test_machinelibrary_command_constructor_args():
    sig = inspect.signature(MachineLibrary_Command.__init__)
    params = list(sig.parameters.keys())
    assert "commandNo" in params, "Missing parameter 'commandNo'"
    assert "commandName" in params, "Missing parameter 'commandName'"
    assert "commandProgParameter" in params, "Missing parameter 'commandProgParameter'"

def test_machinelibrary_command_has_commandNo():
    assert hasattr(MachineLibrary_Command, "commandNo")
    descriptor = None
    for klass in MachineLibrary_Command.__mro__:
        if "commandNo" in klass.__dict__:
            descriptor = klass.__dict__["commandNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_command_has_commandName():
    assert hasattr(MachineLibrary_Command, "commandName")
    descriptor = None
    for klass in MachineLibrary_Command.__mro__:
        if "commandName" in klass.__dict__:
            descriptor = klass.__dict__["commandName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_command_has_commandProgParameter():
    assert hasattr(MachineLibrary_Command, "commandProgParameter")
    descriptor = None
    for klass in MachineLibrary_Command.__mro__:
        if "commandProgParameter" in klass.__dict__:
            descriptor = klass.__dict__["commandProgParameter"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitprogparameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitProgParameters)


def test_machinelibrary_unitprogparameters_constructor_exists():
    assert callable(MachineLibrary_UnitProgParameters.__init__)


def test_machinelibrary_unitprogparameters_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitProgParameters.__init__)
    params = list(sig.parameters.keys())
    assert "parameterNo" in params, "Missing parameter 'parameterNo'"
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_machinelibrary_unitprogparameters_has_parameterNo():
    assert hasattr(MachineLibrary_UnitProgParameters, "parameterNo")
    descriptor = None
    for klass in MachineLibrary_UnitProgParameters.__mro__:
        if "parameterNo" in klass.__dict__:
            descriptor = klass.__dict__["parameterNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitprogparameters_has_parameter():
    assert hasattr(MachineLibrary_UnitProgParameters, "parameter")
    descriptor = None
    for klass in MachineLibrary_UnitProgParameters.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitprogram_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitProgram)


def test_machinelibrary_unitprogram_constructor_exists():
    assert callable(MachineLibrary_UnitProgram.__init__)


def test_machinelibrary_unitprogram_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitProgram.__init__)
    params = list(sig.parameters.keys())
    assert "unitProgName" in params, "Missing parameter 'unitProgName'"

def test_machinelibrary_unitprogram_has_unitProgName():
    assert hasattr(MachineLibrary_UnitProgram, "unitProgName")
    descriptor = None
    for klass in MachineLibrary_UnitProgram.__mro__:
        if "unitProgName" in klass.__dict__:
            descriptor = klass.__dict__["unitProgName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_position_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Position)


def test_machinelibrary_position_constructor_exists():
    assert callable(MachineLibrary_Position.__init__)


def test_machinelibrary_position_constructor_args():
    sig = inspect.signature(MachineLibrary_Position.__init__)
    params = list(sig.parameters.keys())
    assert "posExit" in params, "Missing parameter 'posExit'"
    assert "posIndex" in params, "Missing parameter 'posIndex'"
    assert "posName" in params, "Missing parameter 'posName'"
    assert "posRemark" in params, "Missing parameter 'posRemark'"
    assert "posNo" in params, "Missing parameter 'posNo'"
    assert "posWarningOnDelete" in params, "Missing parameter 'posWarningOnDelete'"

def test_machinelibrary_position_has_posExit():
    assert hasattr(MachineLibrary_Position, "posExit")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posExit" in klass.__dict__:
            descriptor = klass.__dict__["posExit"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_position_has_posIndex():
    assert hasattr(MachineLibrary_Position, "posIndex")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posIndex" in klass.__dict__:
            descriptor = klass.__dict__["posIndex"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_position_has_posName():
    assert hasattr(MachineLibrary_Position, "posName")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posName" in klass.__dict__:
            descriptor = klass.__dict__["posName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_position_has_posRemark():
    assert hasattr(MachineLibrary_Position, "posRemark")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posRemark" in klass.__dict__:
            descriptor = klass.__dict__["posRemark"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_position_has_posNo():
    assert hasattr(MachineLibrary_Position, "posNo")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posNo" in klass.__dict__:
            descriptor = klass.__dict__["posNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_position_has_posWarningOnDelete():
    assert hasattr(MachineLibrary_Position, "posWarningOnDelete")
    descriptor = None
    for klass in MachineLibrary_Position.__mro__:
        if "posWarningOnDelete" in klass.__dict__:
            descriptor = klass.__dict__["posWarningOnDelete"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_button_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Button)


def test_machinelibrary_button_constructor_exists():
    assert callable(MachineLibrary_Button.__init__)


def test_machinelibrary_button_constructor_args():
    sig = inspect.signature(MachineLibrary_Button.__init__)
    params = list(sig.parameters.keys())
    assert "buttonText" in params, "Missing parameter 'buttonText'"
    assert "commandNo" in params, "Missing parameter 'commandNo'"
    assert "buttonNo" in params, "Missing parameter 'buttonNo'"

def test_machinelibrary_button_has_buttonText():
    assert hasattr(MachineLibrary_Button, "buttonText")
    descriptor = None
    for klass in MachineLibrary_Button.__mro__:
        if "buttonText" in klass.__dict__:
            descriptor = klass.__dict__["buttonText"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_button_has_commandNo():
    assert hasattr(MachineLibrary_Button, "commandNo")
    descriptor = None
    for klass in MachineLibrary_Button.__mro__:
        if "commandNo" in klass.__dict__:
            descriptor = klass.__dict__["commandNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_button_has_buttonNo():
    assert hasattr(MachineLibrary_Button, "buttonNo")
    descriptor = None
    for klass in MachineLibrary_Button.__mro__:
        if "buttonNo" in klass.__dict__:
            descriptor = klass.__dict__["buttonNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checkaddsid_values_pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckAddSID_Values_PM2PM)


def test_machinelibrary_checkaddsid_values_pm2pm_constructor_exists():
    assert callable(MachineLibrary_CheckAddSID_Values_PM2PM.__init__)


def test_machinelibrary_checkaddsid_values_pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckAddSID_Values_PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "optionNo" in params, "Missing parameter 'optionNo'"
    assert "optonValue" in params, "Missing parameter 'optonValue'"

def test_machinelibrary_checkaddsid_values_pm2pm_has_optionNo():
    assert hasattr(MachineLibrary_CheckAddSID_Values_PM2PM, "optionNo")
    descriptor = None
    for klass in MachineLibrary_CheckAddSID_Values_PM2PM.__mro__:
        if "optionNo" in klass.__dict__:
            descriptor = klass.__dict__["optionNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checkaddsid_values_pm2pm_has_optonValue():
    assert hasattr(MachineLibrary_CheckAddSID_Values_PM2PM, "optonValue")
    descriptor = None
    for klass in MachineLibrary_CheckAddSID_Values_PM2PM.__mro__:
        if "optonValue" in klass.__dict__:
            descriptor = klass.__dict__["optonValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_sepbycomma_id_scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_SepByComma_ID_Scanner)


def test_machinelibrary_sepbycomma_id_scanner_constructor_exists():
    assert callable(MachineLibrary_SepByComma_ID_Scanner.__init__)


def test_machinelibrary_sepbycomma_id_scanner_constructor_args():
    sig = inspect.signature(MachineLibrary_SepByComma_ID_Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "idPrevValue" in params, "Missing parameter 'idPrevValue'"
    assert "idCharValue" in params, "Missing parameter 'idCharValue'"
    assert "idSeq_X" in params, "Missing parameter 'idSeq_X'"
    assert "idValue" in params, "Missing parameter 'idValue'"

def test_machinelibrary_sepbycomma_id_scanner_has_idPrevValue():
    assert hasattr(MachineLibrary_SepByComma_ID_Scanner, "idPrevValue")
    descriptor = None
    for klass in MachineLibrary_SepByComma_ID_Scanner.__mro__:
        if "idPrevValue" in klass.__dict__:
            descriptor = klass.__dict__["idPrevValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_sepbycomma_id_scanner_has_idCharValue():
    assert hasattr(MachineLibrary_SepByComma_ID_Scanner, "idCharValue")
    descriptor = None
    for klass in MachineLibrary_SepByComma_ID_Scanner.__mro__:
        if "idCharValue" in klass.__dict__:
            descriptor = klass.__dict__["idCharValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_sepbycomma_id_scanner_has_idSeq_X():
    assert hasattr(MachineLibrary_SepByComma_ID_Scanner, "idSeq_X")
    descriptor = None
    for klass in MachineLibrary_SepByComma_ID_Scanner.__mro__:
        if "idSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["idSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_sepbycomma_id_scanner_has_idValue():
    assert hasattr(MachineLibrary_SepByComma_ID_Scanner, "idValue")
    descriptor = None
    for klass in MachineLibrary_SepByComma_ID_Scanner.__mro__:
        if "idValue" in klass.__dict__:
            descriptor = klass.__dict__["idValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_sepbycomma_field_scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_SepByComma_Field_Scanner)


def test_machinelibrary_sepbycomma_field_scanner_constructor_exists():
    assert callable(MachineLibrary_SepByComma_Field_Scanner.__init__)


def test_machinelibrary_sepbycomma_field_scanner_constructor_args():
    sig = inspect.signature(MachineLibrary_SepByComma_Field_Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "fieldNo" in params, "Missing parameter 'fieldNo'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_machinelibrary_sepbycomma_field_scanner_has_fieldNo():
    assert hasattr(MachineLibrary_SepByComma_Field_Scanner, "fieldNo")
    descriptor = None
    for klass in MachineLibrary_SepByComma_Field_Scanner.__mro__:
        if "fieldNo" in klass.__dict__:
            descriptor = klass.__dict__["fieldNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_sepbycomma_field_scanner_has_fieldName():
    assert hasattr(MachineLibrary_SepByComma_Field_Scanner, "fieldName")
    descriptor = None
    for klass in MachineLibrary_SepByComma_Field_Scanner.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_statusbit_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_StatusBit)


def test_machinelibrary_statusbit_constructor_exists():
    assert callable(MachineLibrary_StatusBit.__init__)


def test_machinelibrary_statusbit_constructor_args():
    sig = inspect.signature(MachineLibrary_StatusBit.__init__)
    params = list(sig.parameters.keys())
    assert "bitName" in params, "Missing parameter 'bitName'"
    assert "bitNo" in params, "Missing parameter 'bitNo'"

def test_machinelibrary_statusbit_has_bitName():
    assert hasattr(MachineLibrary_StatusBit, "bitName")
    descriptor = None
    for klass in MachineLibrary_StatusBit.__mro__:
        if "bitName" in klass.__dict__:
            descriptor = klass.__dict__["bitName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_statusbit_has_bitNo():
    assert hasattr(MachineLibrary_StatusBit, "bitNo")
    descriptor = None
    for klass in MachineLibrary_StatusBit.__mro__:
        if "bitNo" in klass.__dict__:
            descriptor = klass.__dict__["bitNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_historyconfig_accupyc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_HistoryConfig_AccuPyc)


def test_machinelibrary_historyconfig_accupyc_constructor_exists():
    assert callable(MachineLibrary_HistoryConfig_AccuPyc.__init__)


def test_machinelibrary_historyconfig_accupyc_constructor_args():
    sig = inspect.signature(MachineLibrary_HistoryConfig_AccuPyc.__init__)
    params = list(sig.parameters.keys())
    assert "sampleCupWeight" in params, "Missing parameter 'sampleCupWeight'"
    assert "currentSample" in params, "Missing parameter 'currentSample'"
    assert "currentSampleID" in params, "Missing parameter 'currentSampleID'"

def test_machinelibrary_historyconfig_accupyc_has_sampleCupWeight():
    assert hasattr(MachineLibrary_HistoryConfig_AccuPyc, "sampleCupWeight")
    descriptor = None
    for klass in MachineLibrary_HistoryConfig_AccuPyc.__mro__:
        if "sampleCupWeight" in klass.__dict__:
            descriptor = klass.__dict__["sampleCupWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_historyconfig_accupyc_has_currentSample():
    assert hasattr(MachineLibrary_HistoryConfig_AccuPyc, "currentSample")
    descriptor = None
    for klass in MachineLibrary_HistoryConfig_AccuPyc.__mro__:
        if "currentSample" in klass.__dict__:
            descriptor = klass.__dict__["currentSample"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_historyconfig_accupyc_has_currentSampleID():
    assert hasattr(MachineLibrary_HistoryConfig_AccuPyc, "currentSampleID")
    descriptor = None
    for klass in MachineLibrary_HistoryConfig_AccuPyc.__mro__:
        if "currentSampleID" in klass.__dict__:
            descriptor = klass.__dict__["currentSampleID"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checksampleconfig_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckSampleConfig_SuperQXRF)


def test_machinelibrary_checksampleconfig_superqxrf_constructor_exists():
    assert callable(MachineLibrary_CheckSampleConfig_SuperQXRF.__init__)


def test_machinelibrary_checksampleconfig_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckSampleConfig_SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "anaProg" in params, "Missing parameter 'anaProg'"
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "program" in params, "Missing parameter 'program'"
    assert "sampleID" in params, "Missing parameter 'sampleID'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"
    assert "samples" in params, "Missing parameter 'samples'"

def test_machinelibrary_checksampleconfig_superqxrf_has_anaProg():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "anaProg")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "anaProg" in klass.__dict__:
            descriptor = klass.__dict__["anaProg"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleconfig_superqxrf_has_minutes():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "minutes")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleconfig_superqxrf_has_program():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "program")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "program" in klass.__dict__:
            descriptor = klass.__dict__["program"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleconfig_superqxrf_has_sampleID():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "sampleID")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "sampleID" in klass.__dict__:
            descriptor = klass.__dict__["sampleID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleconfig_superqxrf_has_seq_X():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "seq_X")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleconfig_superqxrf_has_samples():
    assert hasattr(MachineLibrary_CheckSampleConfig_SuperQXRF, "samples")
    descriptor = None
    for klass in MachineLibrary_CheckSampleConfig_SuperQXRF.__mro__:
        if "samples" in klass.__dict__:
            descriptor = klass.__dict__["samples"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_insertremove_keywords_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_InsertRemove_Keywords_Host)


def test_machinelibrary_insertremove_keywords_host_constructor_exists():
    assert callable(MachineLibrary_InsertRemove_Keywords_Host.__init__)


def test_machinelibrary_insertremove_keywords_host_constructor_args():
    sig = inspect.signature(MachineLibrary_InsertRemove_Keywords_Host.__init__)
    params = list(sig.parameters.keys())
    assert "keywordKey" in params, "Missing parameter 'keywordKey'"
    assert "keywordValue" in params, "Missing parameter 'keywordValue'"

def test_machinelibrary_insertremove_keywords_host_has_keywordKey():
    assert hasattr(MachineLibrary_InsertRemove_Keywords_Host, "keywordKey")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Keywords_Host.__mro__:
        if "keywordKey" in klass.__dict__:
            descriptor = klass.__dict__["keywordKey"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_insertremove_keywords_host_has_keywordValue():
    assert hasattr(MachineLibrary_InsertRemove_Keywords_Host, "keywordValue")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Keywords_Host.__mro__:
        if "keywordValue" in klass.__dict__:
            descriptor = klass.__dict__["keywordValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_insertremove_types_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_InsertRemove_Types_Host)


def test_machinelibrary_insertremove_types_host_constructor_exists():
    assert callable(MachineLibrary_InsertRemove_Types_Host.__init__)


def test_machinelibrary_insertremove_types_host_constructor_args():
    sig = inspect.signature(MachineLibrary_InsertRemove_Types_Host.__init__)
    params = list(sig.parameters.keys())
    assert "typeNo" in params, "Missing parameter 'typeNo'"
    assert "typeValue" in params, "Missing parameter 'typeValue'"

def test_machinelibrary_insertremove_types_host_has_typeNo():
    assert hasattr(MachineLibrary_InsertRemove_Types_Host, "typeNo")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Types_Host.__mro__:
        if "typeNo" in klass.__dict__:
            descriptor = klass.__dict__["typeNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_insertremove_types_host_has_typeValue():
    assert hasattr(MachineLibrary_InsertRemove_Types_Host, "typeValue")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Types_Host.__mro__:
        if "typeValue" in klass.__dict__:
            descriptor = klass.__dict__["typeValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_insertremove_entry_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_InsertRemove_Entry_Host)


def test_machinelibrary_insertremove_entry_host_constructor_exists():
    assert callable(MachineLibrary_InsertRemove_Entry_Host.__init__)


def test_machinelibrary_insertremove_entry_host_constructor_args():
    sig = inspect.signature(MachineLibrary_InsertRemove_Entry_Host.__init__)
    params = list(sig.parameters.keys())
    assert "entryName" in params, "Missing parameter 'entryName'"
    assert "entryNo" in params, "Missing parameter 'entryNo'"

def test_machinelibrary_insertremove_entry_host_has_entryName():
    assert hasattr(MachineLibrary_InsertRemove_Entry_Host, "entryName")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Entry_Host.__mro__:
        if "entryName" in klass.__dict__:
            descriptor = klass.__dict__["entryName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_insertremove_entry_host_has_entryNo():
    assert hasattr(MachineLibrary_InsertRemove_Entry_Host, "entryNo")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Entry_Host.__mro__:
        if "entryNo" in klass.__dict__:
            descriptor = klass.__dict__["entryNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checksampleruntimeparams_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckSampleRunTimeParams_SuperQXRF)


def test_machinelibrary_checksampleruntimeparams_superqxrf_constructor_exists():
    assert callable(MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.__init__)


def test_machinelibrary_checksampleruntimeparams_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "sampleType" in params, "Missing parameter 'sampleType'"

def test_machinelibrary_checksampleruntimeparams_superqxrf_has_value():
    assert hasattr(MachineLibrary_CheckSampleRunTimeParams_SuperQXRF, "value")
    descriptor = None
    for klass in MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_checksampleruntimeparams_superqxrf_has_sampleType():
    assert hasattr(MachineLibrary_CheckSampleRunTimeParams_SuperQXRF, "sampleType")
    descriptor = None
    for klass in MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.__mro__:
        if "sampleType" in klass.__dict__:
            descriptor = klass.__dict__["sampleType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_oes_xrf_condition_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_OES_XRF_Condition)


def test_machinelibrary_oes_xrf_condition_constructor_exists():
    assert callable(MachineLibrary_OES_XRF_Condition.__init__)


def test_machinelibrary_oes_xrf_condition_constructor_args():
    sig = inspect.signature(MachineLibrary_OES_XRF_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "para" in params, "Missing parameter 'para'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"
    assert "paraName" in params, "Missing parameter 'paraName'"

def test_machinelibrary_oes_xrf_condition_has_comment():
    assert hasattr(MachineLibrary_OES_XRF_Condition, "comment")
    descriptor = None
    for klass in MachineLibrary_OES_XRF_Condition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_oes_xrf_condition_has_para():
    assert hasattr(MachineLibrary_OES_XRF_Condition, "para")
    descriptor = None
    for klass in MachineLibrary_OES_XRF_Condition.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_oes_xrf_condition_has_seq_X():
    assert hasattr(MachineLibrary_OES_XRF_Condition, "seq_X")
    descriptor = None
    for klass in MachineLibrary_OES_XRF_Condition.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_oes_xrf_condition_has_paraName():
    assert hasattr(MachineLibrary_OES_XRF_Condition, "paraName")
    descriptor = None
    for klass in MachineLibrary_OES_XRF_Condition.__mro__:
        if "paraName" in klass.__dict__:
            descriptor = klass.__dict__["paraName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_insertremove_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_InsertRemove_Host)


def test_machinelibrary_insertremove_host_constructor_exists():
    assert callable(MachineLibrary_InsertRemove_Host.__init__)


def test_machinelibrary_insertremove_host_constructor_args():
    sig = inspect.signature(MachineLibrary_InsertRemove_Host.__init__)
    params = list(sig.parameters.keys())
    assert "report_All" in params, "Missing parameter 'report_All'"

def test_machinelibrary_insertremove_host_has_report_All():
    assert hasattr(MachineLibrary_InsertRemove_Host, "report_All")
    descriptor = None
    for klass in MachineLibrary_InsertRemove_Host.__mro__:
        if "report_All" in klass.__dict__:
            descriptor = klass.__dict__["report_All"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_moved_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Moved_Host)


def test_machinelibrary_moved_host_constructor_exists():
    assert callable(MachineLibrary_Moved_Host.__init__)


def test_machinelibrary_moved_host_constructor_args():
    sig = inspect.signature(MachineLibrary_Moved_Host.__init__)
    params = list(sig.parameters.keys())
    assert "pos0" in params, "Missing parameter 'pos0'"
    assert "report_ALL" in params, "Missing parameter 'report_ALL'"
    assert "writePositionNameInFile" in params, "Missing parameter 'writePositionNameInFile'"
    assert "type0" in params, "Missing parameter 'type0'"

def test_machinelibrary_moved_host_has_pos0():
    assert hasattr(MachineLibrary_Moved_Host, "pos0")
    descriptor = None
    for klass in MachineLibrary_Moved_Host.__mro__:
        if "pos0" in klass.__dict__:
            descriptor = klass.__dict__["pos0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_moved_host_has_report_ALL():
    assert hasattr(MachineLibrary_Moved_Host, "report_ALL")
    descriptor = None
    for klass in MachineLibrary_Moved_Host.__mro__:
        if "report_ALL" in klass.__dict__:
            descriptor = klass.__dict__["report_ALL"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_moved_host_has_writePositionNameInFile():
    assert hasattr(MachineLibrary_Moved_Host, "writePositionNameInFile")
    descriptor = None
    for klass in MachineLibrary_Moved_Host.__mro__:
        if "writePositionNameInFile" in klass.__dict__:
            descriptor = klass.__dict__["writePositionNameInFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_moved_host_has_type0():
    assert hasattr(MachineLibrary_Moved_Host, "type0")
    descriptor = None
    for klass in MachineLibrary_Moved_Host.__mro__:
        if "type0" in klass.__dict__:
            descriptor = klass.__dict__["type0"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_ws_update_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_WS_Update_Host)


def test_machinelibrary_ws_update_host_constructor_exists():
    assert callable(MachineLibrary_WS_Update_Host.__init__)


def test_machinelibrary_ws_update_host_constructor_args():
    sig = inspect.signature(MachineLibrary_WS_Update_Host.__init__)
    params = list(sig.parameters.keys())
    assert "AllowUnit0" in params, "Missing parameter 'AllowUnit0'"
    assert "checkUnit" in params, "Missing parameter 'checkUnit'"

def test_machinelibrary_ws_update_host_has_AllowUnit0():
    assert hasattr(MachineLibrary_WS_Update_Host, "AllowUnit0")
    descriptor = None
    for klass in MachineLibrary_WS_Update_Host.__mro__:
        if "AllowUnit0" in klass.__dict__:
            descriptor = klass.__dict__["AllowUnit0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ws_update_host_has_checkUnit():
    assert hasattr(MachineLibrary_WS_Update_Host, "checkUnit")
    descriptor = None
    for klass in MachineLibrary_WS_Update_Host.__mro__:
        if "checkUnit" in klass.__dict__:
            descriptor = klass.__dict__["checkUnit"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_report_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Report_Host)


def test_machinelibrary_report_host_constructor_exists():
    assert callable(MachineLibrary_Report_Host.__init__)


def test_machinelibrary_report_host_constructor_args():
    sig = inspect.signature(MachineLibrary_Report_Host.__init__)
    params = list(sig.parameters.keys())
    assert "note1" in params, "Missing parameter 'note1'"
    assert "sendErrorWarningsMsgOnly" in params, "Missing parameter 'sendErrorWarningsMsgOnly'"
    assert "maxType" in params, "Missing parameter 'maxType'"
    assert "stateChanged" in params, "Missing parameter 'stateChanged'"
    assert "sampleInsert" in params, "Missing parameter 'sampleInsert'"
    assert "timeStamp" in params, "Missing parameter 'timeStamp'"
    assert "sampleRemoved" in params, "Missing parameter 'sampleRemoved'"
    assert "rawData" in params, "Missing parameter 'rawData'"
    assert "sendLifeMessages" in params, "Missing parameter 'sendLifeMessages'"
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "sampleMoved" in params, "Missing parameter 'sampleMoved'"
    assert "internal" in params, "Missing parameter 'internal'"
    assert "minType" in params, "Missing parameter 'minType'"
    assert "note" in params, "Missing parameter 'note'"

def test_machinelibrary_report_host_has_note1():
    assert hasattr(MachineLibrary_Report_Host, "note1")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "note1" in klass.__dict__:
            descriptor = klass.__dict__["note1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_sendErrorWarningsMsgOnly():
    assert hasattr(MachineLibrary_Report_Host, "sendErrorWarningsMsgOnly")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "sendErrorWarningsMsgOnly" in klass.__dict__:
            descriptor = klass.__dict__["sendErrorWarningsMsgOnly"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_maxType():
    assert hasattr(MachineLibrary_Report_Host, "maxType")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "maxType" in klass.__dict__:
            descriptor = klass.__dict__["maxType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_stateChanged():
    assert hasattr(MachineLibrary_Report_Host, "stateChanged")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "stateChanged" in klass.__dict__:
            descriptor = klass.__dict__["stateChanged"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_sampleInsert():
    assert hasattr(MachineLibrary_Report_Host, "sampleInsert")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "sampleInsert" in klass.__dict__:
            descriptor = klass.__dict__["sampleInsert"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_timeStamp():
    assert hasattr(MachineLibrary_Report_Host, "timeStamp")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "timeStamp" in klass.__dict__:
            descriptor = klass.__dict__["timeStamp"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_sampleRemoved():
    assert hasattr(MachineLibrary_Report_Host, "sampleRemoved")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "sampleRemoved" in klass.__dict__:
            descriptor = klass.__dict__["sampleRemoved"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_rawData():
    assert hasattr(MachineLibrary_Report_Host, "rawData")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "rawData" in klass.__dict__:
            descriptor = klass.__dict__["rawData"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_sendLifeMessages():
    assert hasattr(MachineLibrary_Report_Host, "sendLifeMessages")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "sendLifeMessages" in klass.__dict__:
            descriptor = klass.__dict__["sendLifeMessages"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_fileName():
    assert hasattr(MachineLibrary_Report_Host, "fileName")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_sampleMoved():
    assert hasattr(MachineLibrary_Report_Host, "sampleMoved")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "sampleMoved" in klass.__dict__:
            descriptor = klass.__dict__["sampleMoved"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_internal():
    assert hasattr(MachineLibrary_Report_Host, "internal")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "internal" in klass.__dict__:
            descriptor = klass.__dict__["internal"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_minType():
    assert hasattr(MachineLibrary_Report_Host, "minType")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "minType" in klass.__dict__:
            descriptor = klass.__dict__["minType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_report_host_has_note():
    assert hasattr(MachineLibrary_Report_Host, "note")
    descriptor = None
    for klass in MachineLibrary_Report_Host.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_settings_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Settings_ARL_XRF_OES)


def test_machinelibrary_settings_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_Settings_ARL_XRF_OES.__init__)


def test_machinelibrary_settings_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_Settings_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_settings_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_Settings_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_Settings_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_disablesct_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_DisableSCT_ARL_XRF_OES)


def test_machinelibrary_disablesct_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_DisableSCT_ARL_XRF_OES.__init__)


def test_machinelibrary_disablesct_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_DisableSCT_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_disablesct_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_DisableSCT_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_DisableSCT_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_exeaskprepunit_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES)


def test_machinelibrary_exeaskprepunit_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES.__init__)


def test_machinelibrary_exeaskprepunit_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_exeaskprepunit_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checkaskprepunit_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES)


def test_machinelibrary_checkaskprepunit_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES.__init__)


def test_machinelibrary_checkaskprepunit_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_checkaskprepunit_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_exeprepunit_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ExePrepUnit_ARL_XRF_OES)


def test_machinelibrary_exeprepunit_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_ExePrepUnit_ARL_XRF_OES.__init__)


def test_machinelibrary_exeprepunit_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_ExePrepUnit_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_exeprepunit_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_ExePrepUnit_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_ExePrepUnit_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checkreqprepunit_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES)


def test_machinelibrary_checkreqprepunit_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES.__init__)


def test_machinelibrary_checkreqprepunit_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_checkreqprepunit_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_executefiling_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ExecuteFiling_ARL_XRF_OES)


def test_machinelibrary_executefiling_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_ExecuteFiling_ARL_XRF_OES.__init__)


def test_machinelibrary_executefiling_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_ExecuteFiling_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_executefiling_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_ExecuteFiling_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_ExecuteFiling_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checkfilling_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckFilling_ARL_XRF_OES)


def test_machinelibrary_checkfilling_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_CheckFilling_ARL_XRF_OES.__init__)


def test_machinelibrary_checkfilling_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckFilling_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_checkfilling_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_CheckFilling_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_CheckFilling_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checksample_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckSample_SuperQXRF)


def test_machinelibrary_checksample_superqxrf_constructor_exists():
    assert callable(MachineLibrary_CheckSample_SuperQXRF.__init__)


def test_machinelibrary_checksample_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckSample_SuperQXRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_checksampleruntime_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckSampleRunTime_SuperQXRF)


def test_machinelibrary_checksampleruntime_superqxrf_constructor_exists():
    assert callable(MachineLibrary_CheckSampleRunTime_SuperQXRF.__init__)


def test_machinelibrary_checksampleruntime_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckSampleRunTime_SuperQXRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_communication_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Communication_SuperQXRF)


def test_machinelibrary_communication_superqxrf_constructor_exists():
    assert callable(MachineLibrary_Communication_SuperQXRF.__init__)


def test_machinelibrary_communication_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_Communication_SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "enq_ACK_Protocol" in params, "Missing parameter 'enq_ACK_Protocol'"

def test_machinelibrary_communication_superqxrf_has_enq_ACK_Protocol():
    assert hasattr(MachineLibrary_Communication_SuperQXRF, "enq_ACK_Protocol")
    descriptor = None
    for klass in MachineLibrary_Communication_SuperQXRF.__mro__:
        if "enq_ACK_Protocol" in klass.__dict__:
            descriptor = klass.__dict__["enq_ACK_Protocol"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_controlsamples_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ControlSamples_SuperQXRF)


def test_machinelibrary_controlsamples_superqxrf_constructor_exists():
    assert callable(MachineLibrary_ControlSamples_SuperQXRF.__init__)


def test_machinelibrary_controlsamples_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_ControlSamples_SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "outOfControl" in params, "Missing parameter 'outOfControl'"

def test_machinelibrary_controlsamples_superqxrf_has_outOfControl():
    assert hasattr(MachineLibrary_ControlSamples_SuperQXRF, "outOfControl")
    descriptor = None
    for klass in MachineLibrary_ControlSamples_SuperQXRF.__mro__:
        if "outOfControl" in klass.__dict__:
            descriptor = klass.__dict__["outOfControl"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_file_sample_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_File_Sample_ARL_XRF_OES)


def test_machinelibrary_file_sample_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_File_Sample_ARL_XRF_OES.__init__)


def test_machinelibrary_file_sample_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_File_Sample_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "noSuccess" in params, "Missing parameter 'noSuccess'"

def test_machinelibrary_file_sample_arl_xrf_oes_has_noSuccess():
    assert hasattr(MachineLibrary_File_Sample_ARL_XRF_OES, "noSuccess")
    descriptor = None
    for klass in MachineLibrary_File_Sample_ARL_XRF_OES.__mro__:
        if "noSuccess" in klass.__dict__:
            descriptor = klass.__dict__["noSuccess"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_ps_process_finished_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_PS_Process_Finished_ARL_XRF_OES)


def test_machinelibrary_ps_process_finished_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_PS_Process_Finished_ARL_XRF_OES.__init__)


def test_machinelibrary_ps_process_finished_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_PS_Process_Finished_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "noSuccess" in params, "Missing parameter 'noSuccess'"

def test_machinelibrary_ps_process_finished_arl_xrf_oes_has_noSuccess():
    assert hasattr(MachineLibrary_PS_Process_Finished_ARL_XRF_OES, "noSuccess")
    descriptor = None
    for klass in MachineLibrary_PS_Process_Finished_ARL_XRF_OES.__mro__:
        if "noSuccess" in klass.__dict__:
            descriptor = klass.__dict__["noSuccess"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_generalsetting_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_GeneralSetting_ARL_XRF_OES)


def test_machinelibrary_generalsetting_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_GeneralSetting_ARL_XRF_OES.__init__)


def test_machinelibrary_generalsetting_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_GeneralSetting_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_generalsetting_arl_xrf_oes_has_name():
    assert hasattr(MachineLibrary_GeneralSetting_ARL_XRF_OES, "name")
    descriptor = None
    for klass in MachineLibrary_GeneralSetting_ARL_XRF_OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_checkaddsid_pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CheckAddSID_PM2PM)


def test_machinelibrary_checkaddsid_pm2pm_constructor_exists():
    assert callable(MachineLibrary_CheckAddSID_PM2PM.__init__)


def test_machinelibrary_checkaddsid_pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary_CheckAddSID_PM2PM.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_sepbycomma_scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_SepByComma_Scanner)


def test_machinelibrary_sepbycomma_scanner_constructor_exists():
    assert callable(MachineLibrary_SepByComma_Scanner.__init__)


def test_machinelibrary_sepbycomma_scanner_constructor_args():
    sig = inspect.signature(MachineLibrary_SepByComma_Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "preDefWS" in params, "Missing parameter 'preDefWS'"
    assert "activ" in params, "Missing parameter 'activ'"

def test_machinelibrary_sepbycomma_scanner_has_preDefWS():
    assert hasattr(MachineLibrary_SepByComma_Scanner, "preDefWS")
    descriptor = None
    for klass in MachineLibrary_SepByComma_Scanner.__mro__:
        if "preDefWS" in klass.__dict__:
            descriptor = klass.__dict__["preDefWS"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_sepbycomma_scanner_has_activ():
    assert hasattr(MachineLibrary_SepByComma_Scanner, "activ")
    descriptor = None
    for klass in MachineLibrary_SepByComma_Scanner.__mro__:
        if "activ" in klass.__dict__:
            descriptor = klass.__dict__["activ"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_history_accupycmeter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_History_AccuPycMeter)


def test_machinelibrary_history_accupycmeter_constructor_exists():
    assert callable(MachineLibrary_History_AccuPycMeter.__init__)


def test_machinelibrary_history_accupycmeter_constructor_args():
    sig = inspect.signature(MachineLibrary_History_AccuPycMeter.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitconfig_host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitConfig_Host)


def test_machinelibrary_unitconfig_host_constructor_exists():
    assert callable(MachineLibrary_UnitConfig_Host.__init__)


def test_machinelibrary_unitconfig_host_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitConfig_Host.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitconfig_arl_xrf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitConfig_ARL_XRF_OES)


def test_machinelibrary_unitconfig_arl_xrf_oes_constructor_exists():
    assert callable(MachineLibrary_UnitConfig_ARL_XRF_OES.__init__)


def test_machinelibrary_unitconfig_arl_xrf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitConfig_ARL_XRF_OES.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitconfig_superq_xrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitConfig_SuperQ_XRF)


def test_machinelibrary_unitconfig_superq_xrf_constructor_exists():
    assert callable(MachineLibrary_UnitConfig_SuperQ_XRF.__init__)


def test_machinelibrary_unitconfig_superq_xrf_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitConfig_SuperQ_XRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitconfig_oblf_oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitConfig_OBLF_OES)


def test_machinelibrary_unitconfig_oblf_oes_constructor_exists():
    assert callable(MachineLibrary_UnitConfig_OBLF_OES.__init__)


def test_machinelibrary_unitconfig_oblf_oes_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitConfig_OBLF_OES.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitconfig_terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitConfig_Terminal)


def test_machinelibrary_unitconfig_terminal_constructor_exists():
    assert callable(MachineLibrary_UnitConfig_Terminal.__init__)


def test_machinelibrary_unitconfig_terminal_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitConfig_Terminal.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_generalparameter_superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_GeneralParameter_SuperQXRF)


def test_machinelibrary_generalparameter_superqxrf_constructor_exists():
    assert callable(MachineLibrary_GeneralParameter_SuperQXRF.__init__)


def test_machinelibrary_generalparameter_superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_GeneralParameter_SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "startList" in params, "Missing parameter 'startList'"
    assert "listName" in params, "Missing parameter 'listName'"
    assert "switchRemote" in params, "Missing parameter 'switchRemote'"

def test_machinelibrary_generalparameter_superqxrf_has_startList():
    assert hasattr(MachineLibrary_GeneralParameter_SuperQXRF, "startList")
    descriptor = None
    for klass in MachineLibrary_GeneralParameter_SuperQXRF.__mro__:
        if "startList" in klass.__dict__:
            descriptor = klass.__dict__["startList"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_generalparameter_superqxrf_has_listName():
    assert hasattr(MachineLibrary_GeneralParameter_SuperQXRF, "listName")
    descriptor = None
    for klass in MachineLibrary_GeneralParameter_SuperQXRF.__mro__:
        if "listName" in klass.__dict__:
            descriptor = klass.__dict__["listName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_generalparameter_superqxrf_has_switchRemote():
    assert hasattr(MachineLibrary_GeneralParameter_SuperQXRF, "switchRemote")
    descriptor = None
    for klass in MachineLibrary_GeneralParameter_SuperQXRF.__mro__:
        if "switchRemote" in klass.__dict__:
            descriptor = klass.__dict__["switchRemote"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_errormessage_oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_ErrorMessage_OBLFOES)


def test_machinelibrary_errormessage_oblfoes_constructor_exists():
    assert callable(MachineLibrary_ErrorMessage_OBLFOES.__init__)


def test_machinelibrary_errormessage_oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary_ErrorMessage_OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "errorMessage" in params, "Missing parameter 'errorMessage'"

def test_machinelibrary_errormessage_oblfoes_has_errorMessage():
    assert hasattr(MachineLibrary_ErrorMessage_OBLFOES, "errorMessage")
    descriptor = None
    for klass in MachineLibrary_ErrorMessage_OBLFOES.__mro__:
        if "errorMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorMessage"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_recalrequest_oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_RecalRequest_OBLFOES)


def test_machinelibrary_recalrequest_oblfoes_constructor_exists():
    assert callable(MachineLibrary_RecalRequest_OBLFOES.__init__)


def test_machinelibrary_recalrequest_oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary_RecalRequest_OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_recalrequest_oblfoes_has_name():
    assert hasattr(MachineLibrary_RecalRequest_OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary_RecalRequest_OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_testrequest_oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_TestRequest_OBLFOES)


def test_machinelibrary_testrequest_oblfoes_constructor_exists():
    assert callable(MachineLibrary_TestRequest_OBLFOES.__init__)


def test_machinelibrary_testrequest_oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary_TestRequest_OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_testrequest_oblfoes_has_name():
    assert hasattr(MachineLibrary_TestRequest_OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary_TestRequest_OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_outputrequest_oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_OutputRequest_OBLFOES)


def test_machinelibrary_outputrequest_oblfoes_constructor_exists():
    assert callable(MachineLibrary_OutputRequest_OBLFOES.__init__)


def test_machinelibrary_outputrequest_oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary_OutputRequest_OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary_outputrequest_oblfoes_has_name():
    assert hasattr(MachineLibrary_OutputRequest_OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary_OutputRequest_OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_translate_terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Translate_Terminal)


def test_machinelibrary_translate_terminal_constructor_exists():
    assert callable(MachineLibrary_Translate_Terminal.__init__)


def test_machinelibrary_translate_terminal_constructor_args():
    sig = inspect.signature(MachineLibrary_Translate_Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "man_Busy" in params, "Missing parameter 'man_Busy'"
    assert "man_Ready" in params, "Missing parameter 'man_Ready'"
    assert "auto_Busy" in params, "Missing parameter 'auto_Busy'"
    assert "auto_Ready" in params, "Missing parameter 'auto_Ready'"

def test_machinelibrary_translate_terminal_has_man_Busy():
    assert hasattr(MachineLibrary_Translate_Terminal, "man_Busy")
    descriptor = None
    for klass in MachineLibrary_Translate_Terminal.__mro__:
        if "man_Busy" in klass.__dict__:
            descriptor = klass.__dict__["man_Busy"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_translate_terminal_has_man_Ready():
    assert hasattr(MachineLibrary_Translate_Terminal, "man_Ready")
    descriptor = None
    for klass in MachineLibrary_Translate_Terminal.__mro__:
        if "man_Ready" in klass.__dict__:
            descriptor = klass.__dict__["man_Ready"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_translate_terminal_has_auto_Busy():
    assert hasattr(MachineLibrary_Translate_Terminal, "auto_Busy")
    descriptor = None
    for klass in MachineLibrary_Translate_Terminal.__mro__:
        if "auto_Busy" in klass.__dict__:
            descriptor = klass.__dict__["auto_Busy"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_translate_terminal_has_auto_Ready():
    assert hasattr(MachineLibrary_Translate_Terminal, "auto_Ready")
    descriptor = None
    for klass in MachineLibrary_Translate_Terminal.__mro__:
        if "auto_Ready" in klass.__dict__:
            descriptor = klass.__dict__["auto_Ready"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_Scanner)


def test_machinelibrary_unitgeneral_scanner_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_Scanner.__init__)


def test_machinelibrary_unitgeneral_scanner_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "addString" in params, "Missing parameter 'addString'"
    assert "preString" in params, "Missing parameter 'preString'"
    assert "forcedSampleType" in params, "Missing parameter 'forcedSampleType'"
    assert "registerSample" in params, "Missing parameter 'registerSample'"
    assert "length" in params, "Missing parameter 'length'"
    assert "fillWith" in params, "Missing parameter 'fillWith'"

def test_machinelibrary_unitgeneral_scanner_has_start():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "start")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_addString():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "addString")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "addString" in klass.__dict__:
            descriptor = klass.__dict__["addString"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_preString():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "preString")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "preString" in klass.__dict__:
            descriptor = klass.__dict__["preString"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_forcedSampleType():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "forcedSampleType")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "forcedSampleType" in klass.__dict__:
            descriptor = klass.__dict__["forcedSampleType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_registerSample():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "registerSample")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "registerSample" in klass.__dict__:
            descriptor = klass.__dict__["registerSample"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_length():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "length")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_scanner_has_fillWith():
    assert hasattr(MachineLibrary_UnitGeneral_Scanner, "fillWith")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Scanner.__mro__:
        if "fillWith" in klass.__dict__:
            descriptor = klass.__dict__["fillWith"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_rigakuxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_RigakuXRF)


def test_machinelibrary_unitgeneral_rigakuxrf_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_RigakuXRF.__init__)


def test_machinelibrary_unitgeneral_rigakuxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_RigakuXRF.__init__)
    params = list(sig.parameters.keys())
    assert "lastPosInInstrument" in params, "Missing parameter 'lastPosInInstrument'"
    assert "lastPosAnalyHAG_SIg" in params, "Missing parameter 'lastPosAnalyHAG_SIg'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "lastPoHAG_SIInstrument" in params, "Missing parameter 'lastPoHAG_SIInstrument'"

def test_machinelibrary_unitgeneral_rigakuxrf_has_lastPosInInstrument():
    assert hasattr(MachineLibrary_UnitGeneral_RigakuXRF, "lastPosInInstrument")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_RigakuXRF.__mro__:
        if "lastPosInInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPosInInstrument"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_rigakuxrf_has_lastPosAnalyHAG_SIg():
    assert hasattr(MachineLibrary_UnitGeneral_RigakuXRF, "lastPosAnalyHAG_SIg")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_RigakuXRF.__mro__:
        if "lastPosAnalyHAG_SIg" in klass.__dict__:
            descriptor = klass.__dict__["lastPosAnalyHAG_SIg"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_rigakuxrf_has_separator():
    assert hasattr(MachineLibrary_UnitGeneral_RigakuXRF, "separator")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_RigakuXRF.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_rigakuxrf_has_lastPoHAG_SIInstrument():
    assert hasattr(MachineLibrary_UnitGeneral_RigakuXRF, "lastPoHAG_SIInstrument")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_RigakuXRF.__mro__:
        if "lastPoHAG_SIInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPoHAG_SIInstrument"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_superq_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_SuperQ)


def test_machinelibrary_unitgeneral_superq_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_SuperQ.__init__)


def test_machinelibrary_unitgeneral_superq_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_SuperQ.__init__)
    params = list(sig.parameters.keys())
    assert "lastPosAnalysing" in params, "Missing parameter 'lastPosAnalysing'"
    assert "lastPosInInstrument" in params, "Missing parameter 'lastPosInInstrument'"

def test_machinelibrary_unitgeneral_superq_has_lastPosAnalysing():
    assert hasattr(MachineLibrary_UnitGeneral_SuperQ, "lastPosAnalysing")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_SuperQ.__mro__:
        if "lastPosAnalysing" in klass.__dict__:
            descriptor = klass.__dict__["lastPosAnalysing"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_superq_has_lastPosInInstrument():
    assert hasattr(MachineLibrary_UnitGeneral_SuperQ, "lastPosInInstrument")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_SuperQ.__mro__:
        if "lastPosInInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPosInInstrument"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_accpyc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_AccPyc)


def test_machinelibrary_unitgeneral_accpyc_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_AccPyc.__init__)


def test_machinelibrary_unitgeneral_accpyc_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_AccPyc.__init__)
    params = list(sig.parameters.keys())
    assert "cupWeight" in params, "Missing parameter 'cupWeight'"
    assert "minSampleWeight" in params, "Missing parameter 'minSampleWeight'"

def test_machinelibrary_unitgeneral_accpyc_has_cupWeight():
    assert hasattr(MachineLibrary_UnitGeneral_AccPyc, "cupWeight")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_AccPyc.__mro__:
        if "cupWeight" in klass.__dict__:
            descriptor = klass.__dict__["cupWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_accpyc_has_minSampleWeight():
    assert hasattr(MachineLibrary_UnitGeneral_AccPyc, "minSampleWeight")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_AccPyc.__mro__:
        if "minSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["minSampleWeight"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_PM2PM)


def test_machinelibrary_unitgeneral_pm2pm_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_PM2PM.__init__)


def test_machinelibrary_unitgeneral_pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "processFeedBack" in params, "Missing parameter 'processFeedBack'"
    assert "sid_Mask" in params, "Missing parameter 'sid_Mask'"

def test_machinelibrary_unitgeneral_pm2pm_has_processFeedBack():
    assert hasattr(MachineLibrary_UnitGeneral_PM2PM, "processFeedBack")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_PM2PM.__mro__:
        if "processFeedBack" in klass.__dict__:
            descriptor = klass.__dict__["processFeedBack"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_pm2pm_has_sid_Mask():
    assert hasattr(MachineLibrary_UnitGeneral_PM2PM, "sid_Mask")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_PM2PM.__mro__:
        if "sid_Mask" in klass.__dict__:
            descriptor = klass.__dict__["sid_Mask"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_remote_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_Remote)


def test_machinelibrary_unitgeneral_remote_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_Remote.__init__)


def test_machinelibrary_unitgeneral_remote_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_Remote.__init__)
    params = list(sig.parameters.keys())
    assert "editWSDB" in params, "Missing parameter 'editWSDB'"
    assert "handshakeT" in params, "Missing parameter 'handshakeT'"
    assert "handshakeQ" in params, "Missing parameter 'handshakeQ'"
    assert "handshakeA" in params, "Missing parameter 'handshakeA'"

def test_machinelibrary_unitgeneral_remote_has_editWSDB():
    assert hasattr(MachineLibrary_UnitGeneral_Remote, "editWSDB")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Remote.__mro__:
        if "editWSDB" in klass.__dict__:
            descriptor = klass.__dict__["editWSDB"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_remote_has_handshakeT():
    assert hasattr(MachineLibrary_UnitGeneral_Remote, "handshakeT")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Remote.__mro__:
        if "handshakeT" in klass.__dict__:
            descriptor = klass.__dict__["handshakeT"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_remote_has_handshakeQ():
    assert hasattr(MachineLibrary_UnitGeneral_Remote, "handshakeQ")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Remote.__mro__:
        if "handshakeQ" in klass.__dict__:
            descriptor = klass.__dict__["handshakeQ"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_remote_has_handshakeA():
    assert hasattr(MachineLibrary_UnitGeneral_Remote, "handshakeA")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Remote.__mro__:
        if "handshakeA" in klass.__dict__:
            descriptor = klass.__dict__["handshakeA"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_hostpc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_HostPC)


def test_machinelibrary_unitgeneral_hostpc_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_HostPC.__init__)


def test_machinelibrary_unitgeneral_hostpc_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_HostPC.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "replyOnLink" in params, "Missing parameter 'replyOnLink'"
    assert "writeDumyIfNoDataExist" in params, "Missing parameter 'writeDumyIfNoDataExist'"
    assert "maxIndex" in params, "Missing parameter 'maxIndex'"

def test_machinelibrary_unitgeneral_hostpc_has_index():
    assert hasattr(MachineLibrary_UnitGeneral_HostPC, "index")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_HostPC.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_hostpc_has_replyOnLink():
    assert hasattr(MachineLibrary_UnitGeneral_HostPC, "replyOnLink")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_HostPC.__mro__:
        if "replyOnLink" in klass.__dict__:
            descriptor = klass.__dict__["replyOnLink"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_hostpc_has_writeDumyIfNoDataExist():
    assert hasattr(MachineLibrary_UnitGeneral_HostPC, "writeDumyIfNoDataExist")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_HostPC.__mro__:
        if "writeDumyIfNoDataExist" in klass.__dict__:
            descriptor = klass.__dict__["writeDumyIfNoDataExist"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_hostpc_has_maxIndex():
    assert hasattr(MachineLibrary_UnitGeneral_HostPC, "maxIndex")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_HostPC.__mro__:
        if "maxIndex" in klass.__dict__:
            descriptor = klass.__dict__["maxIndex"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneral_terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral_Terminal)


def test_machinelibrary_unitgeneral_terminal_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral_Terminal.__init__)


def test_machinelibrary_unitgeneral_terminal_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral_Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "station1" in params, "Missing parameter 'station1'"
    assert "station5" in params, "Missing parameter 'station5'"
    assert "station2" in params, "Missing parameter 'station2'"
    assert "thisStation" in params, "Missing parameter 'thisStation'"
    assert "station4" in params, "Missing parameter 'station4'"
    assert "station3" in params, "Missing parameter 'station3'"

def test_machinelibrary_unitgeneral_terminal_has_station1():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "station1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "station1" in klass.__dict__:
            descriptor = klass.__dict__["station1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_terminal_has_station5():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "station5")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "station5" in klass.__dict__:
            descriptor = klass.__dict__["station5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_terminal_has_station2():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "station2")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "station2" in klass.__dict__:
            descriptor = klass.__dict__["station2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_terminal_has_thisStation():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "thisStation")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "thisStation" in klass.__dict__:
            descriptor = klass.__dict__["thisStation"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_terminal_has_station4():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "station4")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "station4" in klass.__dict__:
            descriptor = klass.__dict__["station4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneral_terminal_has_station3():
    assert hasattr(MachineLibrary_UnitGeneral_Terminal, "station3")
    descriptor = None
    for klass in MachineLibrary_UnitGeneral_Terminal.__mro__:
        if "station3" in klass.__dict__:
            descriptor = klass.__dict__["station3"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_plctopmmatrix_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_PLCtoPmMatrix)


def test_machinelibrary_plctopmmatrix_constructor_exists():
    assert callable(MachineLibrary_PLCtoPmMatrix.__init__)


def test_machinelibrary_plctopmmatrix_constructor_args():
    sig = inspect.signature(MachineLibrary_PLCtoPmMatrix.__init__)
    params = list(sig.parameters.keys())
    assert "plcpmmatrixBit0" in params, "Missing parameter 'plcpmmatrixBit0'"
    assert "plcpmmatrixBit14" in params, "Missing parameter 'plcpmmatrixBit14'"
    assert "plcpmmatrixBit7" in params, "Missing parameter 'plcpmmatrixBit7'"
    assert "plcpmmatrixBit12" in params, "Missing parameter 'plcpmmatrixBit12'"
    assert "plcpmmatrixBit4" in params, "Missing parameter 'plcpmmatrixBit4'"
    assert "plcpmmatrixBit1" in params, "Missing parameter 'plcpmmatrixBit1'"
    assert "plcpmmatrixBit5" in params, "Missing parameter 'plcpmmatrixBit5'"
    assert "plcpmmatrixBit10" in params, "Missing parameter 'plcpmmatrixBit10'"
    assert "plcpmmatrixBit6" in params, "Missing parameter 'plcpmmatrixBit6'"
    assert "plcpmmatrixBit13" in params, "Missing parameter 'plcpmmatrixBit13'"
    assert "plcpmmatrixBit15" in params, "Missing parameter 'plcpmmatrixBit15'"
    assert "plcpmmatrixBit8" in params, "Missing parameter 'plcpmmatrixBit8'"
    assert "plcpmmatrixBit9" in params, "Missing parameter 'plcpmmatrixBit9'"
    assert "plcpmmatrixBit11" in params, "Missing parameter 'plcpmmatrixBit11'"
    assert "plcpmmatrixBit3" in params, "Missing parameter 'plcpmmatrixBit3'"
    assert "plcpmmatrixBit2" in params, "Missing parameter 'plcpmmatrixBit2'"

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit0():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit0")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit0" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit14():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit14")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit14" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit14"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit7():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit7")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit7" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit7"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit12():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit12")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit12" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit12"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit4():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit4")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit4" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit1():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit1")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit1" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit5():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit5")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit5" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit10():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit10")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit10" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit10"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit6():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit6")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit6" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit13():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit13")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit13" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit13"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit15():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit15")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit15" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit15"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit8():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit8")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit8" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit8"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit9():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit9")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit9" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit9"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit11():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit11")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit11" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit11"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit3():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit3")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit3" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_plctopmmatrix_has_plcpmmatrixBit2():
    assert hasattr(MachineLibrary_PLCtoPmMatrix, "plcpmmatrixBit2")
    descriptor = None
    for klass in MachineLibrary_PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit2" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit2"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_stausbits_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_StausBits)


def test_machinelibrary_stausbits_constructor_exists():
    assert callable(MachineLibrary_StausBits.__init__)


def test_machinelibrary_stausbits_constructor_args():
    sig = inspect.signature(MachineLibrary_StausBits.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_positions_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Positions)


def test_machinelibrary_positions_constructor_exists():
    assert callable(MachineLibrary_Positions.__init__)


def test_machinelibrary_positions_constructor_args():
    sig = inspect.signature(MachineLibrary_Positions.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_winccaddtag_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_WinCCAddTag)


def test_machinelibrary_winccaddtag_constructor_exists():
    assert callable(MachineLibrary_WinCCAddTag.__init__)


def test_machinelibrary_winccaddtag_constructor_args():
    sig = inspect.signature(MachineLibrary_WinCCAddTag.__init__)
    params = list(sig.parameters.keys())
    assert "winCCTag" in params, "Missing parameter 'winCCTag'"

def test_machinelibrary_winccaddtag_has_winCCTag():
    assert hasattr(MachineLibrary_WinCCAddTag, "winCCTag")
    descriptor = None
    for klass in MachineLibrary_WinCCAddTag.__mro__:
        if "winCCTag" in klass.__dict__:
            descriptor = klass.__dict__["winCCTag"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitgeneralparameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneralParameters)


def test_machinelibrary_unitgeneralparameters_constructor_exists():
    assert callable(MachineLibrary_UnitGeneralParameters.__init__)


def test_machinelibrary_unitgeneralparameters_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneralParameters.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue_1" in params, "Missing parameter 'defaultValue_1'"
    assert "UseWith_1" in params, "Missing parameter 'UseWith_1'"
    assert "visibleType_1" in params, "Missing parameter 'visibleType_1'"
    assert "comment_1" in params, "Missing parameter 'comment_1'"
    assert "unit_1" in params, "Missing parameter 'unit_1'"
    assert "maxValue_1" in params, "Missing parameter 'maxValue_1'"
    assert "minValue_1" in params, "Missing parameter 'minValue_1'"
    assert "canBeChange_1" in params, "Missing parameter 'canBeChange_1'"
    assert "KeyWord_1" in params, "Missing parameter 'KeyWord_1'"
    assert "paraName_1" in params, "Missing parameter 'paraName_1'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"

def test_machinelibrary_unitgeneralparameters_has_defaultValue_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "defaultValue_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "defaultValue_1" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_UseWith_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "UseWith_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "UseWith_1" in klass.__dict__:
            descriptor = klass.__dict__["UseWith_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_visibleType_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "visibleType_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "visibleType_1" in klass.__dict__:
            descriptor = klass.__dict__["visibleType_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_comment_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "comment_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "comment_1" in klass.__dict__:
            descriptor = klass.__dict__["comment_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_unit_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "unit_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "unit_1" in klass.__dict__:
            descriptor = klass.__dict__["unit_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_maxValue_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "maxValue_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "maxValue_1" in klass.__dict__:
            descriptor = klass.__dict__["maxValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_minValue_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "minValue_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "minValue_1" in klass.__dict__:
            descriptor = klass.__dict__["minValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_canBeChange_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "canBeChange_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "canBeChange_1" in klass.__dict__:
            descriptor = klass.__dict__["canBeChange_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_KeyWord_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "KeyWord_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "KeyWord_1" in klass.__dict__:
            descriptor = klass.__dict__["KeyWord_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_paraName_1():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "paraName_1")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "paraName_1" in klass.__dict__:
            descriptor = klass.__dict__["paraName_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_unitgeneralparameters_has_seq_X():
    assert hasattr(MachineLibrary_UnitGeneralParameters, "seq_X")
    descriptor = None
    for klass in MachineLibrary_UnitGeneralParameters.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_unitspecialconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitSpecialConfiguration)


def test_machinelibrary_unitspecialconfiguration_constructor_exists():
    assert callable(MachineLibrary_UnitSpecialConfiguration.__init__)


def test_machinelibrary_unitspecialconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitSpecialConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitgeneralspecial_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneralSpecial)


def test_machinelibrary_unitgeneralspecial_constructor_exists():
    assert callable(MachineLibrary_UnitGeneralSpecial.__init__)


def test_machinelibrary_unitgeneralspecial_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneralSpecial.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitgeneral_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitGeneral)


def test_machinelibrary_unitgeneral_constructor_exists():
    assert callable(MachineLibrary_UnitGeneral.__init__)


def test_machinelibrary_unitgeneral_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitGeneral.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_buttons_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Buttons)


def test_machinelibrary_buttons_constructor_exists():
    assert callable(MachineLibrary_Buttons.__init__)


def test_machinelibrary_buttons_constructor_args():
    sig = inspect.signature(MachineLibrary_Buttons.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_unitprograms_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_UnitPrograms)


def test_machinelibrary_unitprograms_constructor_exists():
    assert callable(MachineLibrary_UnitPrograms.__init__)


def test_machinelibrary_unitprograms_constructor_args():
    sig = inspect.signature(MachineLibrary_UnitPrograms.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_nodegeneral_rigakuxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_RigakuXRF)


def test_machinelibrary_nodegeneral_rigakuxrf_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_RigakuXRF.__init__)


def test_machinelibrary_nodegeneral_rigakuxrf_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_RigakuXRF.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "timerToSendStatus" in params, "Missing parameter 'timerToSendStatus'"
    assert "bDoNotshiftAtExit" in params, "Missing parameter 'bDoNotshiftAtExit'"
    assert "timeoutResponce" in params, "Missing parameter 'timeoutResponce'"

def test_machinelibrary_nodegeneral_rigakuxrf_has_timeout():
    assert hasattr(MachineLibrary_NodeGeneral_RigakuXRF, "timeout")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RigakuXRF.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_rigakuxrf_has_timerToSendStatus():
    assert hasattr(MachineLibrary_NodeGeneral_RigakuXRF, "timerToSendStatus")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RigakuXRF.__mro__:
        if "timerToSendStatus" in klass.__dict__:
            descriptor = klass.__dict__["timerToSendStatus"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_rigakuxrf_has_bDoNotshiftAtExit():
    assert hasattr(MachineLibrary_NodeGeneral_RigakuXRF, "bDoNotshiftAtExit")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RigakuXRF.__mro__:
        if "bDoNotshiftAtExit" in klass.__dict__:
            descriptor = klass.__dict__["bDoNotshiftAtExit"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_rigakuxrf_has_timeoutResponce():
    assert hasattr(MachineLibrary_NodeGeneral_RigakuXRF, "timeoutResponce")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RigakuXRF.__mro__:
        if "timeoutResponce" in klass.__dict__:
            descriptor = klass.__dict__["timeoutResponce"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneral_accupycmeter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_AccuPycMeter)


def test_machinelibrary_nodegeneral_accupycmeter_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_AccuPycMeter.__init__)


def test_machinelibrary_nodegeneral_accupycmeter_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_AccuPycMeter.__init__)
    params = list(sig.parameters.keys())
    assert "runTimout" in params, "Missing parameter 'runTimout'"
    assert "expectSampleWeight" in params, "Missing parameter 'expectSampleWeight'"
    assert "polling" in params, "Missing parameter 'polling'"
    assert "sendSampleWeight" in params, "Missing parameter 'sendSampleWeight'"

def test_machinelibrary_nodegeneral_accupycmeter_has_runTimout():
    assert hasattr(MachineLibrary_NodeGeneral_AccuPycMeter, "runTimout")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_AccuPycMeter.__mro__:
        if "runTimout" in klass.__dict__:
            descriptor = klass.__dict__["runTimout"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_accupycmeter_has_expectSampleWeight():
    assert hasattr(MachineLibrary_NodeGeneral_AccuPycMeter, "expectSampleWeight")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_AccuPycMeter.__mro__:
        if "expectSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["expectSampleWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_accupycmeter_has_polling():
    assert hasattr(MachineLibrary_NodeGeneral_AccuPycMeter, "polling")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_AccuPycMeter.__mro__:
        if "polling" in klass.__dict__:
            descriptor = klass.__dict__["polling"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_accupycmeter_has_sendSampleWeight():
    assert hasattr(MachineLibrary_NodeGeneral_AccuPycMeter, "sendSampleWeight")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_AccuPycMeter.__mro__:
        if "sendSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["sendSampleWeight"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneral_wincc2wincc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_WinCC2WinCC)


def test_machinelibrary_nodegeneral_wincc2wincc_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_WinCC2WinCC.__init__)


def test_machinelibrary_nodegeneral_wincc2wincc_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_WinCC2WinCC.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_machinelibrary_nodegeneral_wincc2wincc_has_prefix():
    assert hasattr(MachineLibrary_NodeGeneral_WinCC2WinCC, "prefix")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_WinCC2WinCC.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneral_remotepm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_RemotePM)


def test_machinelibrary_nodegeneral_remotepm_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_RemotePM.__init__)


def test_machinelibrary_nodegeneral_remotepm_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_RemotePM.__init__)
    params = list(sig.parameters.keys())
    assert "system" in params, "Missing parameter 'system'"
    assert "timeServer" in params, "Missing parameter 'timeServer'"

def test_machinelibrary_nodegeneral_remotepm_has_system():
    assert hasattr(MachineLibrary_NodeGeneral_RemotePM, "system")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RemotePM.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_remotepm_has_timeServer():
    assert hasattr(MachineLibrary_NodeGeneral_RemotePM, "timeServer")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_RemotePM.__mro__:
        if "timeServer" in klass.__dict__:
            descriptor = klass.__dict__["timeServer"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneral_pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_PM2PM)


def test_machinelibrary_nodegeneral_pm2pm_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_PM2PM.__init__)


def test_machinelibrary_nodegeneral_pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "timeServer" in params, "Missing parameter 'timeServer'"
    assert "type" in params, "Missing parameter 'type'"

def test_machinelibrary_nodegeneral_pm2pm_has_timeServer():
    assert hasattr(MachineLibrary_NodeGeneral_PM2PM, "timeServer")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_PM2PM.__mro__:
        if "timeServer" in klass.__dict__:
            descriptor = klass.__dict__["timeServer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_pm2pm_has_type():
    assert hasattr(MachineLibrary_NodeGeneral_PM2PM, "type")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_PM2PM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneral_terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral_Terminal)


def test_machinelibrary_nodegeneral_terminal_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral_Terminal.__init__)


def test_machinelibrary_nodegeneral_terminal_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral_Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "name_3" in params, "Missing parameter 'name_3'"
    assert "signalCarrierPresent" in params, "Missing parameter 'signalCarrierPresent'"
    assert "steelCarrier" in params, "Missing parameter 'steelCarrier'"
    assert "keyBoardSignalCarrierPresent" in params, "Missing parameter 'keyBoardSignalCarrierPresent'"
    assert "maxScreens" in params, "Missing parameter 'maxScreens'"
    assert "name_5" in params, "Missing parameter 'name_5'"
    assert "name_6" in params, "Missing parameter 'name_6'"
    assert "stationAuto" in params, "Missing parameter 'stationAuto'"
    assert "terminalType" in params, "Missing parameter 'terminalType'"
    assert "name_4" in params, "Missing parameter 'name_4'"
    assert "customTimer1" in params, "Missing parameter 'customTimer1'"
    assert "maxXValue" in params, "Missing parameter 'maxXValue'"
    assert "maxYValue" in params, "Missing parameter 'maxYValue'"
    assert "name_2" in params, "Missing parameter 'name_2'"
    assert "displayTime" in params, "Missing parameter 'displayTime'"
    assert "stationReady" in params, "Missing parameter 'stationReady'"
    assert "name_1" in params, "Missing parameter 'name_1'"
    assert "customTimer2" in params, "Missing parameter 'customTimer2'"
    assert "lenOfPlanID" in params, "Missing parameter 'lenOfPlanID'"
    assert "stationType" in params, "Missing parameter 'stationType'"

def test_machinelibrary_nodegeneral_terminal_has_name_3():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_3")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_3" in klass.__dict__:
            descriptor = klass.__dict__["name_3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_signalCarrierPresent():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "signalCarrierPresent")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "signalCarrierPresent" in klass.__dict__:
            descriptor = klass.__dict__["signalCarrierPresent"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_steelCarrier():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "steelCarrier")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "steelCarrier" in klass.__dict__:
            descriptor = klass.__dict__["steelCarrier"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_keyBoardSignalCarrierPresent():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "keyBoardSignalCarrierPresent")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "keyBoardSignalCarrierPresent" in klass.__dict__:
            descriptor = klass.__dict__["keyBoardSignalCarrierPresent"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_maxScreens():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "maxScreens")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "maxScreens" in klass.__dict__:
            descriptor = klass.__dict__["maxScreens"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_name_5():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_5")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_5" in klass.__dict__:
            descriptor = klass.__dict__["name_5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_name_6():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_6")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_6" in klass.__dict__:
            descriptor = klass.__dict__["name_6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_stationAuto():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "stationAuto")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "stationAuto" in klass.__dict__:
            descriptor = klass.__dict__["stationAuto"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_terminalType():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "terminalType")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "terminalType" in klass.__dict__:
            descriptor = klass.__dict__["terminalType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_name_4():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_4")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_4" in klass.__dict__:
            descriptor = klass.__dict__["name_4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_customTimer1():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "customTimer1")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "customTimer1" in klass.__dict__:
            descriptor = klass.__dict__["customTimer1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_maxXValue():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "maxXValue")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "maxXValue" in klass.__dict__:
            descriptor = klass.__dict__["maxXValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_maxYValue():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "maxYValue")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "maxYValue" in klass.__dict__:
            descriptor = klass.__dict__["maxYValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_name_2():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_2")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_2" in klass.__dict__:
            descriptor = klass.__dict__["name_2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_displayTime():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "displayTime")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "displayTime" in klass.__dict__:
            descriptor = klass.__dict__["displayTime"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_stationReady():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "stationReady")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "stationReady" in klass.__dict__:
            descriptor = klass.__dict__["stationReady"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_name_1():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "name_1")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "name_1" in klass.__dict__:
            descriptor = klass.__dict__["name_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_customTimer2():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "customTimer2")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "customTimer2" in klass.__dict__:
            descriptor = klass.__dict__["customTimer2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_lenOfPlanID():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "lenOfPlanID")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "lenOfPlanID" in klass.__dict__:
            descriptor = klass.__dict__["lenOfPlanID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_terminal_has_stationType():
    assert hasattr(MachineLibrary_NodeGeneral_Terminal, "stationType")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral_Terminal.__mro__:
        if "stationType" in klass.__dict__:
            descriptor = klass.__dict__["stationType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodegeneralspecial_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneralSpecial)


def test_machinelibrary_nodegeneralspecial_constructor_exists():
    assert callable(MachineLibrary_NodeGeneralSpecial.__init__)


def test_machinelibrary_nodegeneralspecial_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneralSpecial.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_nodegeneral_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeGeneral)


def test_machinelibrary_nodegeneral_constructor_exists():
    assert callable(MachineLibrary_NodeGeneral.__init__)


def test_machinelibrary_nodegeneral_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeGeneral.__init__)
    params = list(sig.parameters.keys())
    assert "canCreateErrorTag" in params, "Missing parameter 'canCreateErrorTag'"
    assert "canCreateStateTag" in params, "Missing parameter 'canCreateStateTag'"

def test_machinelibrary_nodegeneral_has_canCreateErrorTag():
    assert hasattr(MachineLibrary_NodeGeneral, "canCreateErrorTag")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral.__mro__:
        if "canCreateErrorTag" in klass.__dict__:
            descriptor = klass.__dict__["canCreateErrorTag"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodegeneral_has_canCreateStateTag():
    assert hasattr(MachineLibrary_NodeGeneral, "canCreateStateTag")
    descriptor = None
    for klass in MachineLibrary_NodeGeneral.__mro__:
        if "canCreateStateTag" in klass.__dict__:
            descriptor = klass.__dict__["canCreateStateTag"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodespecialconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeSpecialConfiguration)


def test_machinelibrary_nodespecialconfiguration_constructor_exists():
    assert callable(MachineLibrary_NodeSpecialConfiguration.__init__)


def test_machinelibrary_nodespecialconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeSpecialConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_communicationdata_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_CommunicationData)


def test_machinelibrary_communicationdata_constructor_exists():
    assert callable(MachineLibrary_CommunicationData.__init__)


def test_machinelibrary_communicationdata_constructor_args():
    sig = inspect.signature(MachineLibrary_CommunicationData.__init__)
    params = list(sig.parameters.keys())
    assert "comErrorDataLength" in params, "Missing parameter 'comErrorDataLength'"
    assert "comSendDataAddress" in params, "Missing parameter 'comSendDataAddress'"
    assert "comErrorDataAddress" in params, "Missing parameter 'comErrorDataAddress'"
    assert "comRequestDataLength" in params, "Missing parameter 'comRequestDataLength'"
    assert "comSIDDataLength" in params, "Missing parameter 'comSIDDataLength'"
    assert "comProgressIndDataLength" in params, "Missing parameter 'comProgressIndDataLength'"
    assert "comSendDataLength" in params, "Missing parameter 'comSendDataLength'"
    assert "comRequestDataAddress" in params, "Missing parameter 'comRequestDataAddress'"
    assert "comSIDDataAddress" in params, "Missing parameter 'comSIDDataAddress'"
    assert "comProgressIndDataAddress" in params, "Missing parameter 'comProgressIndDataAddress'"

def test_machinelibrary_communicationdata_has_comErrorDataLength():
    assert hasattr(MachineLibrary_CommunicationData, "comErrorDataLength")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comErrorDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comErrorDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comSendDataAddress():
    assert hasattr(MachineLibrary_CommunicationData, "comSendDataAddress")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comSendDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comSendDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comErrorDataAddress():
    assert hasattr(MachineLibrary_CommunicationData, "comErrorDataAddress")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comErrorDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comErrorDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comRequestDataLength():
    assert hasattr(MachineLibrary_CommunicationData, "comRequestDataLength")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comRequestDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comRequestDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comSIDDataLength():
    assert hasattr(MachineLibrary_CommunicationData, "comSIDDataLength")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comSIDDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comSIDDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comProgressIndDataLength():
    assert hasattr(MachineLibrary_CommunicationData, "comProgressIndDataLength")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comProgressIndDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comProgressIndDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comSendDataLength():
    assert hasattr(MachineLibrary_CommunicationData, "comSendDataLength")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comSendDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comSendDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comRequestDataAddress():
    assert hasattr(MachineLibrary_CommunicationData, "comRequestDataAddress")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comRequestDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comRequestDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comSIDDataAddress():
    assert hasattr(MachineLibrary_CommunicationData, "comSIDDataAddress")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comSIDDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comSIDDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_communicationdata_has_comProgressIndDataAddress():
    assert hasattr(MachineLibrary_CommunicationData, "comProgressIndDataAddress")
    descriptor = None
    for klass in MachineLibrary_CommunicationData.__mro__:
        if "comProgressIndDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comProgressIndDataAddress"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_parameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Parameters)


def test_machinelibrary_parameters_constructor_exists():
    assert callable(MachineLibrary_Parameters.__init__)


def test_machinelibrary_parameters_constructor_args():
    sig = inspect.signature(MachineLibrary_Parameters.__init__)
    params = list(sig.parameters.keys())
    assert "parameterConfigNo" in params, "Missing parameter 'parameterConfigNo'"
    assert "parameterConfigYes" in params, "Missing parameter 'parameterConfigYes'"

def test_machinelibrary_parameters_has_parameterConfigNo():
    assert hasattr(MachineLibrary_Parameters, "parameterConfigNo")
    descriptor = None
    for klass in MachineLibrary_Parameters.__mro__:
        if "parameterConfigNo" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfigNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_parameters_has_parameterConfigYes():
    assert hasattr(MachineLibrary_Parameters, "parameterConfigYes")
    descriptor = None
    for klass in MachineLibrary_Parameters.__mro__:
        if "parameterConfigYes" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfigYes"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_nodeprograms_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodePrograms)


def test_machinelibrary_nodeprograms_constructor_exists():
    assert callable(MachineLibrary_NodePrograms.__init__)


def test_machinelibrary_nodeprograms_constructor_args():
    sig = inspect.signature(MachineLibrary_NodePrograms.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_commands_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Commands)


def test_machinelibrary_commands_constructor_exists():
    assert callable(MachineLibrary_Commands.__init__)


def test_machinelibrary_commands_constructor_args():
    sig = inspect.signature(MachineLibrary_Commands.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_units_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Units)


def test_machinelibrary_units_constructor_exists():
    assert callable(MachineLibrary_Units.__init__)


def test_machinelibrary_units_constructor_args():
    sig = inspect.signature(MachineLibrary_Units.__init__)
    params = list(sig.parameters.keys())
    assert "unitNo" in params, "Missing parameter 'unitNo'"
    assert "unitName" in params, "Missing parameter 'unitName'"
    assert "internalUniNo" in params, "Missing parameter 'internalUniNo'"

def test_machinelibrary_units_has_unitNo():
    assert hasattr(MachineLibrary_Units, "unitNo")
    descriptor = None
    for klass in MachineLibrary_Units.__mro__:
        if "unitNo" in klass.__dict__:
            descriptor = klass.__dict__["unitNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_units_has_unitName():
    assert hasattr(MachineLibrary_Units, "unitName")
    descriptor = None
    for klass in MachineLibrary_Units.__mro__:
        if "unitName" in klass.__dict__:
            descriptor = klass.__dict__["unitName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_units_has_internalUniNo():
    assert hasattr(MachineLibrary_Units, "internalUniNo")
    descriptor = None
    for klass in MachineLibrary_Units.__mro__:
        if "internalUniNo" in klass.__dict__:
            descriptor = klass.__dict__["internalUniNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_dpbase_node_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_DPbase_Node)


def test_machinelibrary_dpbase_node_constructor_exists():
    assert callable(MachineLibrary_DPbase_Node.__init__)


def test_machinelibrary_dpbase_node_constructor_args():
    sig = inspect.signature(MachineLibrary_DPbase_Node.__init__)
    params = list(sig.parameters.keys())
    assert "isXPS" in params, "Missing parameter 'isXPS'"
    assert "nodeNo" in params, "Missing parameter 'nodeNo'"

def test_machinelibrary_dpbase_node_has_isXPS():
    assert hasattr(MachineLibrary_DPbase_Node, "isXPS")
    descriptor = None
    for klass in MachineLibrary_DPbase_Node.__mro__:
        if "isXPS" in klass.__dict__:
            descriptor = klass.__dict__["isXPS"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_dpbase_node_has_nodeNo():
    assert hasattr(MachineLibrary_DPbase_Node, "nodeNo")
    descriptor = None
    for klass in MachineLibrary_DPbase_Node.__mro__:
        if "nodeNo" in klass.__dict__:
            descriptor = klass.__dict__["nodeNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_compac_link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Compac_Link)


def test_machinelibrary_compac_link_constructor_exists():
    assert callable(MachineLibrary_Compac_Link.__init__)


def test_machinelibrary_compac_link_constructor_args():
    sig = inspect.signature(MachineLibrary_Compac_Link.__init__)
    params = list(sig.parameters.keys())
    assert "checksumCode" in params, "Missing parameter 'checksumCode'"
    assert "splitLongMessage" in params, "Missing parameter 'splitLongMessage'"
    assert "retry" in params, "Missing parameter 'retry'"
    assert "bytecountcode" in params, "Missing parameter 'bytecountcode'"
    assert "checksum" in params, "Missing parameter 'checksum'"
    assert "bcc" in params, "Missing parameter 'bcc'"
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "commConfig" in params, "Missing parameter 'commConfig'"
    assert "useNotACK_NAK" in params, "Missing parameter 'useNotACK_NAK'"
    assert "useNotENQ" in params, "Missing parameter 'useNotENQ'"
    assert "byteCount" in params, "Missing parameter 'byteCount'"
    assert "port" in params, "Missing parameter 'port'"
    assert "maxDataLength" in params, "Missing parameter 'maxDataLength'"
    assert "params" in params, "Missing parameter 'params'"

def test_machinelibrary_compac_link_has_checksumCode():
    assert hasattr(MachineLibrary_Compac_Link, "checksumCode")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "checksumCode" in klass.__dict__:
            descriptor = klass.__dict__["checksumCode"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_splitLongMessage():
    assert hasattr(MachineLibrary_Compac_Link, "splitLongMessage")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "splitLongMessage" in klass.__dict__:
            descriptor = klass.__dict__["splitLongMessage"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_retry():
    assert hasattr(MachineLibrary_Compac_Link, "retry")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "retry" in klass.__dict__:
            descriptor = klass.__dict__["retry"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_bytecountcode():
    assert hasattr(MachineLibrary_Compac_Link, "bytecountcode")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "bytecountcode" in klass.__dict__:
            descriptor = klass.__dict__["bytecountcode"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_checksum():
    assert hasattr(MachineLibrary_Compac_Link, "checksum")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "checksum" in klass.__dict__:
            descriptor = klass.__dict__["checksum"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_bcc():
    assert hasattr(MachineLibrary_Compac_Link, "bcc")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "bcc" in klass.__dict__:
            descriptor = klass.__dict__["bcc"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_timeout():
    assert hasattr(MachineLibrary_Compac_Link, "timeout")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_commConfig():
    assert hasattr(MachineLibrary_Compac_Link, "commConfig")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "commConfig" in klass.__dict__:
            descriptor = klass.__dict__["commConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_useNotACK_NAK():
    assert hasattr(MachineLibrary_Compac_Link, "useNotACK_NAK")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "useNotACK_NAK" in klass.__dict__:
            descriptor = klass.__dict__["useNotACK_NAK"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_useNotENQ():
    assert hasattr(MachineLibrary_Compac_Link, "useNotENQ")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "useNotENQ" in klass.__dict__:
            descriptor = klass.__dict__["useNotENQ"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_byteCount():
    assert hasattr(MachineLibrary_Compac_Link, "byteCount")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "byteCount" in klass.__dict__:
            descriptor = klass.__dict__["byteCount"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_port():
    assert hasattr(MachineLibrary_Compac_Link, "port")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_maxDataLength():
    assert hasattr(MachineLibrary_Compac_Link, "maxDataLength")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "maxDataLength" in klass.__dict__:
            descriptor = klass.__dict__["maxDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_compac_link_has_params():
    assert hasattr(MachineLibrary_Compac_Link, "params")
    descriptor = None
    for klass in MachineLibrary_Compac_Link.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_filetransfer_link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_FileTransfer_Link)


def test_machinelibrary_filetransfer_link_constructor_exists():
    assert callable(MachineLibrary_FileTransfer_Link.__init__)


def test_machinelibrary_filetransfer_link_constructor_args():
    sig = inspect.signature(MachineLibrary_FileTransfer_Link.__init__)
    params = list(sig.parameters.keys())
    assert "flagToWriteWaitFor" in params, "Missing parameter 'flagToWriteWaitFor'"
    assert "flagWriteAfterReading" in params, "Missing parameter 'flagWriteAfterReading'"
    assert "timeoutwrite" in params, "Missing parameter 'timeoutwrite'"
    assert "pollTime" in params, "Missing parameter 'pollTime'"
    assert "delimter" in params, "Missing parameter 'delimter'"
    assert "flagDelAfterReading" in params, "Missing parameter 'flagDelAfterReading'"
    assert "writeAfterReading" in params, "Missing parameter 'writeAfterReading'"
    assert "toWriteWaitFor" in params, "Missing parameter 'toWriteWaitFor'"
    assert "flagToWriteWaitForDeleted" in params, "Missing parameter 'flagToWriteWaitForDeleted'"
    assert "writePath" in params, "Missing parameter 'writePath'"
    assert "translation" in params, "Missing parameter 'translation'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "readPath" in params, "Missing parameter 'readPath'"
    assert "delimiter" in params, "Missing parameter 'delimiter'"
    assert "maxDataLength" in params, "Missing parameter 'maxDataLength'"

def test_machinelibrary_filetransfer_link_has_flagToWriteWaitFor():
    assert hasattr(MachineLibrary_FileTransfer_Link, "flagToWriteWaitFor")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "flagToWriteWaitFor" in klass.__dict__:
            descriptor = klass.__dict__["flagToWriteWaitFor"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_flagWriteAfterReading():
    assert hasattr(MachineLibrary_FileTransfer_Link, "flagWriteAfterReading")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "flagWriteAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["flagWriteAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_timeoutwrite():
    assert hasattr(MachineLibrary_FileTransfer_Link, "timeoutwrite")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "timeoutwrite" in klass.__dict__:
            descriptor = klass.__dict__["timeoutwrite"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_pollTime():
    assert hasattr(MachineLibrary_FileTransfer_Link, "pollTime")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "pollTime" in klass.__dict__:
            descriptor = klass.__dict__["pollTime"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_delimter():
    assert hasattr(MachineLibrary_FileTransfer_Link, "delimter")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "delimter" in klass.__dict__:
            descriptor = klass.__dict__["delimter"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_flagDelAfterReading():
    assert hasattr(MachineLibrary_FileTransfer_Link, "flagDelAfterReading")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "flagDelAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["flagDelAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_writeAfterReading():
    assert hasattr(MachineLibrary_FileTransfer_Link, "writeAfterReading")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "writeAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["writeAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_toWriteWaitFor():
    assert hasattr(MachineLibrary_FileTransfer_Link, "toWriteWaitFor")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "toWriteWaitFor" in klass.__dict__:
            descriptor = klass.__dict__["toWriteWaitFor"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_flagToWriteWaitForDeleted():
    assert hasattr(MachineLibrary_FileTransfer_Link, "flagToWriteWaitForDeleted")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "flagToWriteWaitForDeleted" in klass.__dict__:
            descriptor = klass.__dict__["flagToWriteWaitForDeleted"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_writePath():
    assert hasattr(MachineLibrary_FileTransfer_Link, "writePath")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "writePath" in klass.__dict__:
            descriptor = klass.__dict__["writePath"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_translation():
    assert hasattr(MachineLibrary_FileTransfer_Link, "translation")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_sendBuffer():
    assert hasattr(MachineLibrary_FileTransfer_Link, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_receiveBuffer():
    assert hasattr(MachineLibrary_FileTransfer_Link, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_readPath():
    assert hasattr(MachineLibrary_FileTransfer_Link, "readPath")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "readPath" in klass.__dict__:
            descriptor = klass.__dict__["readPath"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_delimiter():
    assert hasattr(MachineLibrary_FileTransfer_Link, "delimiter")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_filetransfer_link_has_maxDataLength():
    assert hasattr(MachineLibrary_FileTransfer_Link, "maxDataLength")
    descriptor = None
    for klass in MachineLibrary_FileTransfer_Link.__mro__:
        if "maxDataLength" in klass.__dict__:
            descriptor = klass.__dict__["maxDataLength"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_serial_link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Serial_Link)


def test_machinelibrary_serial_link_constructor_exists():
    assert callable(MachineLibrary_Serial_Link.__init__)


def test_machinelibrary_serial_link_constructor_args():
    sig = inspect.signature(MachineLibrary_Serial_Link.__init__)
    params = list(sig.parameters.keys())
    assert "maxCharDelay" in params, "Missing parameter 'maxCharDelay'"
    assert "commConfig" in params, "Missing parameter 'commConfig'"
    assert "params" in params, "Missing parameter 'params'"
    assert "port" in params, "Missing parameter 'port'"
    assert "endChar" in params, "Missing parameter 'endChar'"
    assert "startChar" in params, "Missing parameter 'startChar'"
    assert "bufferLenght" in params, "Missing parameter 'bufferLenght'"
    assert "logging" in params, "Missing parameter 'logging'"

def test_machinelibrary_serial_link_has_maxCharDelay():
    assert hasattr(MachineLibrary_Serial_Link, "maxCharDelay")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "maxCharDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxCharDelay"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_commConfig():
    assert hasattr(MachineLibrary_Serial_Link, "commConfig")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "commConfig" in klass.__dict__:
            descriptor = klass.__dict__["commConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_params():
    assert hasattr(MachineLibrary_Serial_Link, "params")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_port():
    assert hasattr(MachineLibrary_Serial_Link, "port")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_endChar():
    assert hasattr(MachineLibrary_Serial_Link, "endChar")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "endChar" in klass.__dict__:
            descriptor = klass.__dict__["endChar"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_startChar():
    assert hasattr(MachineLibrary_Serial_Link, "startChar")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "startChar" in klass.__dict__:
            descriptor = klass.__dict__["startChar"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_bufferLenght():
    assert hasattr(MachineLibrary_Serial_Link, "bufferLenght")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "bufferLenght" in klass.__dict__:
            descriptor = klass.__dict__["bufferLenght"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_serial_link_has_logging():
    assert hasattr(MachineLibrary_Serial_Link, "logging")
    descriptor = None
    for klass in MachineLibrary_Serial_Link.__mro__:
        if "logging" in klass.__dict__:
            descriptor = klass.__dict__["logging"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_tcpip_link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_TCPIP_Link)


def test_machinelibrary_tcpip_link_constructor_exists():
    assert callable(MachineLibrary_TCPIP_Link.__init__)


def test_machinelibrary_tcpip_link_constructor_args():
    sig = inspect.signature(MachineLibrary_TCPIP_Link.__init__)
    params = list(sig.parameters.keys())
    assert "address_1" in params, "Missing parameter 'address_1'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "msgDelay" in params, "Missing parameter 'msgDelay'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "port" in params, "Missing parameter 'port'"
    assert "address_5" in params, "Missing parameter 'address_5'"
    assert "maxDataSize" in params, "Missing parameter 'maxDataSize'"
    assert "address_6" in params, "Missing parameter 'address_6'"
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "address_3" in params, "Missing parameter 'address_3'"
    assert "termChar" in params, "Missing parameter 'termChar'"
    assert "address_2" in params, "Missing parameter 'address_2'"
    assert "address_4" in params, "Missing parameter 'address_4'"

def test_machinelibrary_tcpip_link_has_address_1():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_1")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_1" in klass.__dict__:
            descriptor = klass.__dict__["address_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_sendBuffer():
    assert hasattr(MachineLibrary_TCPIP_Link, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_msgDelay():
    assert hasattr(MachineLibrary_TCPIP_Link, "msgDelay")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "msgDelay" in klass.__dict__:
            descriptor = klass.__dict__["msgDelay"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_receiveBuffer():
    assert hasattr(MachineLibrary_TCPIP_Link, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_port():
    assert hasattr(MachineLibrary_TCPIP_Link, "port")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_address_5():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_5")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_5" in klass.__dict__:
            descriptor = klass.__dict__["address_5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_maxDataSize():
    assert hasattr(MachineLibrary_TCPIP_Link, "maxDataSize")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "maxDataSize" in klass.__dict__:
            descriptor = klass.__dict__["maxDataSize"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_address_6():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_6")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_6" in klass.__dict__:
            descriptor = klass.__dict__["address_6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_protocol():
    assert hasattr(MachineLibrary_TCPIP_Link, "protocol")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_address_3():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_3")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_3" in klass.__dict__:
            descriptor = klass.__dict__["address_3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_termChar():
    assert hasattr(MachineLibrary_TCPIP_Link, "termChar")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "termChar" in klass.__dict__:
            descriptor = klass.__dict__["termChar"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_address_2():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_2")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_2" in klass.__dict__:
            descriptor = klass.__dict__["address_2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_tcpip_link_has_address_4():
    assert hasattr(MachineLibrary_TCPIP_Link, "address_4")
    descriptor = None
    for klass in MachineLibrary_TCPIP_Link.__mro__:
        if "address_4" in klass.__dict__:
            descriptor = klass.__dict__["address_4"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_wincclnk_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_WinCCLnk)


def test_machinelibrary_wincclnk_constructor_exists():
    assert callable(MachineLibrary_WinCCLnk.__init__)


def test_machinelibrary_wincclnk_constructor_args():
    sig = inspect.signature(MachineLibrary_WinCCLnk.__init__)
    params = list(sig.parameters.keys())
    assert "updateCycle" in params, "Missing parameter 'updateCycle'"
    assert "canCreateTags" in params, "Missing parameter 'canCreateTags'"
    assert "updateCycle_Help" in params, "Missing parameter 'updateCycle_Help'"
    assert "canModifyTag" in params, "Missing parameter 'canModifyTag'"
    assert "connectionName" in params, "Missing parameter 'connectionName'"

def test_machinelibrary_wincclnk_has_updateCycle():
    assert hasattr(MachineLibrary_WinCCLnk, "updateCycle")
    descriptor = None
    for klass in MachineLibrary_WinCCLnk.__mro__:
        if "updateCycle" in klass.__dict__:
            descriptor = klass.__dict__["updateCycle"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_wincclnk_has_canCreateTags():
    assert hasattr(MachineLibrary_WinCCLnk, "canCreateTags")
    descriptor = None
    for klass in MachineLibrary_WinCCLnk.__mro__:
        if "canCreateTags" in klass.__dict__:
            descriptor = klass.__dict__["canCreateTags"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_wincclnk_has_updateCycle_Help():
    assert hasattr(MachineLibrary_WinCCLnk, "updateCycle_Help")
    descriptor = None
    for klass in MachineLibrary_WinCCLnk.__mro__:
        if "updateCycle_Help" in klass.__dict__:
            descriptor = klass.__dict__["updateCycle_Help"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_wincclnk_has_canModifyTag():
    assert hasattr(MachineLibrary_WinCCLnk, "canModifyTag")
    descriptor = None
    for klass in MachineLibrary_WinCCLnk.__mro__:
        if "canModifyTag" in klass.__dict__:
            descriptor = klass.__dict__["canModifyTag"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_wincclnk_has_connectionName():
    assert hasattr(MachineLibrary_WinCCLnk, "connectionName")
    descriptor = None
    for klass in MachineLibrary_WinCCLnk.__mro__:
        if "connectionName" in klass.__dict__:
            descriptor = klass.__dict__["connectionName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_linkconfig_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_LinkConfig)


def test_machinelibrary_linkconfig_constructor_exists():
    assert callable(MachineLibrary_LinkConfig.__init__)


def test_machinelibrary_linkconfig_constructor_args():
    sig = inspect.signature(MachineLibrary_LinkConfig.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_nodeconfig_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_NodeConfig)


def test_machinelibrary_nodeconfig_constructor_exists():
    assert callable(MachineLibrary_NodeConfig.__init__)


def test_machinelibrary_nodeconfig_constructor_args():
    sig = inspect.signature(MachineLibrary_NodeConfig.__init__)
    params = list(sig.parameters.keys())
    assert "nodeName" in params, "Missing parameter 'nodeName'"
    assert "simFileName" in params, "Missing parameter 'simFileName'"
    assert "nodeNo" in params, "Missing parameter 'nodeNo'"

def test_machinelibrary_nodeconfig_has_nodeName():
    assert hasattr(MachineLibrary_NodeConfig, "nodeName")
    descriptor = None
    for klass in MachineLibrary_NodeConfig.__mro__:
        if "nodeName" in klass.__dict__:
            descriptor = klass.__dict__["nodeName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeconfig_has_simFileName():
    assert hasattr(MachineLibrary_NodeConfig, "simFileName")
    descriptor = None
    for klass in MachineLibrary_NodeConfig.__mro__:
        if "simFileName" in klass.__dict__:
            descriptor = klass.__dict__["simFileName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_nodeconfig_has_nodeNo():
    assert hasattr(MachineLibrary_NodeConfig, "nodeNo")
    descriptor = None
    for klass in MachineLibrary_NodeConfig.__mro__:
        if "nodeNo" in klass.__dict__:
            descriptor = klass.__dict__["nodeNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_link2_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_Link2)


def test_machinelibrary_link2_constructor_exists():
    assert callable(MachineLibrary_Link2.__init__)


def test_machinelibrary_link2_constructor_args():
    sig = inspect.signature(MachineLibrary_Link2.__init__)
    params = list(sig.parameters.keys())
    assert "link2ParamSection" in params, "Missing parameter 'link2ParamSection'"
    assert "link2Type" in params, "Missing parameter 'link2Type'"
    assert "link2ParamFile" in params, "Missing parameter 'link2ParamFile'"

def test_machinelibrary_link2_has_link2ParamSection():
    assert hasattr(MachineLibrary_Link2, "link2ParamSection")
    descriptor = None
    for klass in MachineLibrary_Link2.__mro__:
        if "link2ParamSection" in klass.__dict__:
            descriptor = klass.__dict__["link2ParamSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_link2_has_link2Type():
    assert hasattr(MachineLibrary_Link2, "link2Type")
    descriptor = None
    for klass in MachineLibrary_Link2.__mro__:
        if "link2Type" in klass.__dict__:
            descriptor = klass.__dict__["link2Type"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_link2_has_link2ParamFile():
    assert hasattr(MachineLibrary_Link2, "link2ParamFile")
    descriptor = None
    for klass in MachineLibrary_Link2.__mro__:
        if "link2ParamFile" in klass.__dict__:
            descriptor = klass.__dict__["link2ParamFile"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_dpbase_link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_DPbase_Link)


def test_machinelibrary_dpbase_link_constructor_exists():
    assert callable(MachineLibrary_DPbase_Link.__init__)


def test_machinelibrary_dpbase_link_constructor_args():
    sig = inspect.signature(MachineLibrary_DPbase_Link.__init__)
    params = list(sig.parameters.keys())
    assert "cp_name" in params, "Missing parameter 'cp_name'"
    assert "speed" in params, "Missing parameter 'speed'"
    assert "maxNodes" in params, "Missing parameter 'maxNodes'"

def test_machinelibrary_dpbase_link_has_cp_name():
    assert hasattr(MachineLibrary_DPbase_Link, "cp_name")
    descriptor = None
    for klass in MachineLibrary_DPbase_Link.__mro__:
        if "cp_name" in klass.__dict__:
            descriptor = klass.__dict__["cp_name"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_dpbase_link_has_speed():
    assert hasattr(MachineLibrary_DPbase_Link, "speed")
    descriptor = None
    for klass in MachineLibrary_DPbase_Link.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_dpbase_link_has_maxNodes():
    assert hasattr(MachineLibrary_DPbase_Link, "maxNodes")
    descriptor = None
    for klass in MachineLibrary_DPbase_Link.__mro__:
        if "maxNodes" in klass.__dict__:
            descriptor = klass.__dict__["maxNodes"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_ibmwebspheremq_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_IBMWebsphereMQ)


def test_machinelibrary_ibmwebspheremq_constructor_exists():
    assert callable(MachineLibrary_IBMWebsphereMQ.__init__)


def test_machinelibrary_ibmwebspheremq_constructor_args():
    sig = inspect.signature(MachineLibrary_IBMWebsphereMQ.__init__)
    params = list(sig.parameters.keys())
    assert "qName" in params, "Missing parameter 'qName'"
    assert "sendDynamicQueName" in params, "Missing parameter 'sendDynamicQueName'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "sendQueName" in params, "Missing parameter 'sendQueName'"
    assert "maxDataSize" in params, "Missing parameter 'maxDataSize'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "sendQueMgrName" in params, "Missing parameter 'sendQueMgrName'"
    assert "readDynamicQueName" in params, "Missing parameter 'readDynamicQueName'"
    assert "readQueMgrName" in params, "Missing parameter 'readQueMgrName'"
    assert "readQueName" in params, "Missing parameter 'readQueName'"

def test_machinelibrary_ibmwebspheremq_has_qName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "qName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "qName" in klass.__dict__:
            descriptor = klass.__dict__["qName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_sendDynamicQueName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "sendDynamicQueName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "sendDynamicQueName" in klass.__dict__:
            descriptor = klass.__dict__["sendDynamicQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_sendBuffer():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_sendQueName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "sendQueName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "sendQueName" in klass.__dict__:
            descriptor = klass.__dict__["sendQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_maxDataSize():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "maxDataSize")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "maxDataSize" in klass.__dict__:
            descriptor = klass.__dict__["maxDataSize"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_receiveBuffer():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_sendQueMgrName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "sendQueMgrName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "sendQueMgrName" in klass.__dict__:
            descriptor = klass.__dict__["sendQueMgrName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_readDynamicQueName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "readDynamicQueName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "readDynamicQueName" in klass.__dict__:
            descriptor = klass.__dict__["readDynamicQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_readQueMgrName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "readQueMgrName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "readQueMgrName" in klass.__dict__:
            descriptor = klass.__dict__["readQueMgrName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_ibmwebspheremq_has_readQueName():
    assert hasattr(MachineLibrary_IBMWebsphereMQ, "readQueName")
    descriptor = None
    for klass in MachineLibrary_IBMWebsphereMQ.__mro__:
        if "readQueName" in klass.__dict__:
            descriptor = klass.__dict__["readQueName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_labmachine_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_LabMachine)


def test_machinelibrary_labmachine_constructor_exists():
    assert callable(MachineLibrary_LabMachine.__init__)


def test_machinelibrary_labmachine_constructor_args():
    sig = inspect.signature(MachineLibrary_LabMachine.__init__)
    params = list(sig.parameters.keys())
    assert "linkParamFile" in params, "Missing parameter 'linkParamFile'"
    assert "versionRemark" in params, "Missing parameter 'versionRemark'"
    assert "machineVersionNo" in params, "Missing parameter 'machineVersionNo'"
    assert "linkParamSection" in params, "Missing parameter 'linkParamSection'"
    assert "driver" in params, "Missing parameter 'driver'"
    assert "machineName" in params, "Missing parameter 'machineName'"
    assert "createWinCCTags" in params, "Missing parameter 'createWinCCTags'"
    assert "linkType" in params, "Missing parameter 'linkType'"

def test_machinelibrary_labmachine_has_linkParamFile():
    assert hasattr(MachineLibrary_LabMachine, "linkParamFile")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "linkParamFile" in klass.__dict__:
            descriptor = klass.__dict__["linkParamFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_versionRemark():
    assert hasattr(MachineLibrary_LabMachine, "versionRemark")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "versionRemark" in klass.__dict__:
            descriptor = klass.__dict__["versionRemark"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_machineVersionNo():
    assert hasattr(MachineLibrary_LabMachine, "machineVersionNo")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "machineVersionNo" in klass.__dict__:
            descriptor = klass.__dict__["machineVersionNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_linkParamSection():
    assert hasattr(MachineLibrary_LabMachine, "linkParamSection")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "linkParamSection" in klass.__dict__:
            descriptor = klass.__dict__["linkParamSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_driver():
    assert hasattr(MachineLibrary_LabMachine, "driver")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "driver" in klass.__dict__:
            descriptor = klass.__dict__["driver"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_machineName():
    assert hasattr(MachineLibrary_LabMachine, "machineName")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "machineName" in klass.__dict__:
            descriptor = klass.__dict__["machineName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_createWinCCTags():
    assert hasattr(MachineLibrary_LabMachine, "createWinCCTags")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "createWinCCTags" in klass.__dict__:
            descriptor = klass.__dict__["createWinCCTags"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_labmachine_has_linkType():
    assert hasattr(MachineLibrary_LabMachine, "linkType")
    descriptor = None
    for klass in MachineLibrary_LabMachine.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary_labmachines_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_LabMachines)


def test_machinelibrary_labmachines_constructor_exists():
    assert callable(MachineLibrary_LabMachines.__init__)


def test_machinelibrary_labmachines_constructor_args():
    sig = inspect.signature(MachineLibrary_LabMachines.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary_pmmachinelibrary_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary_PMMachineLibrary)


def test_machinelibrary_pmmachinelibrary_constructor_exists():
    assert callable(MachineLibrary_PMMachineLibrary.__init__)


def test_machinelibrary_pmmachinelibrary_constructor_args():
    sig = inspect.signature(MachineLibrary_PMMachineLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "libraryVersion" in params, "Missing parameter 'libraryVersion'"
    assert "libraryVersionRemark" in params, "Missing parameter 'libraryVersionRemark'"

def test_machinelibrary_pmmachinelibrary_has_libraryVersion():
    assert hasattr(MachineLibrary_PMMachineLibrary, "libraryVersion")
    descriptor = None
    for klass in MachineLibrary_PMMachineLibrary.__mro__:
        if "libraryVersion" in klass.__dict__:
            descriptor = klass.__dict__["libraryVersion"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary_pmmachinelibrary_has_libraryVersionRemark():
    assert hasattr(MachineLibrary_PMMachineLibrary, "libraryVersionRemark")
    descriptor = None
    for klass in MachineLibrary_PMMachineLibrary.__mro__:
        if "libraryVersionRemark" in klass.__dict__:
            descriptor = klass.__dict__["libraryVersionRemark"]
            break
    assert isinstance(descriptor, property)


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
MachineLibrary_RobotToWinCC_strategy = st.builds(
    MachineLibrary_RobotToWinCC,
    robotToWinccSeq_X=
        st.integers(),
    robotToWinccType_X=
        safe_text,
    robotToWinccTo_X=
        safe_text,
    robotToWinccFrom_X=
        safe_text
)
MachineLibrary_RobotWinCCToRobot_strategy = st.builds(
    MachineLibrary_RobotWinCCToRobot,
    robotwincctorobotTo_X=
        safe_text,
    robotwincctorobootType_X=
        safe_text,
    robotwincctorobotFrom_X=
        safe_text,
    robotwincctorobootSeq_X=
        st.integers()
)
MachineLibrary_RobotConfSendOrder_strategy = st.builds(
    MachineLibrary_RobotConfSendOrder,
    robotconfsendorderVar_X=
        safe_text,
    robotconfsendorderType_X=
        safe_text,
    robotconfsendorderSeq_X=
        st.integers(),
    robotconfsendorderFrom_X=
        safe_text
)
MachineLibrary_RobotVarToBusycode_strategy = st.builds(
    MachineLibrary_RobotVarToBusycode,
    robotvartobusycodeSeq_X=
        st.integers(),
    robotvartobusycodeType_X=
        safe_text,
    robotvartobusycodeVar_X=
        safe_text,
    robotvartobusycodeUnit_X=
        st.integers(),
    robotvartobusycodeBit_X=
        st.integers()
)
MachineLibrary_RobotVarToErrorbit_strategy = st.builds(
    MachineLibrary_RobotVarToErrorbit,
    robotvartoerrorbitSeq_X=
        st.integers(),
    robotvartoerrorbitType_X=
        safe_text,
    robotvartoerrorbitBit_X=
        st.integers(),
    robotvartoerrorbitVar_X=
        safe_text,
    robotvartoerrorbitInv_X=
        st.integers()
)
MachineLibrary_PlainMoveEntrySend_strategy = st.builds(
    MachineLibrary_PlainMoveEntrySend,
    plainmoveSeq=
        st.integers(),
    plainmoveEntry=
        safe_text,
    plainmoveSend=
        safe_text
)
MachineLibrary_TransferFileSection_strategy = st.builds(
    MachineLibrary_TransferFileSection,
    transferSection=
        safe_text,
    transferFile=
        safe_text,
    transferSeq=
        st.integers()
)
MachineLibrary_RobotConfiguration_strategy = st.builds(
    MachineLibrary_RobotConfiguration,
    robotIPAddress=
        safe_text,
    robotSystemID=
        safe_text,
    robotActivate=
        st.integers(),
    robotID=
        safe_text
)
MachineLibrary_RobotVarToErrorbits_strategy = st.builds(
    MachineLibrary_RobotVarToErrorbits,
)
MachineLibrary_RobotWarningONDelete_strategy = st.builds(
    MachineLibrary_RobotWarningONDelete,
    robotExtraUnit_2=
        safe_text,
    robotExtraPos_1=
        safe_text,
    robotErrBitWhenConfirmationIsNeededFor_PM=
        st.integers(),
    robotErrBitWhenConfirmationIsNeededFor_Robot=
        st.integers()
)
MachineLibrary_RobotToWinccs_strategy = st.builds(
    MachineLibrary_RobotToWinccs,
)
MachineLibrary_RobotWinCCToRobots_strategy = st.builds(
    MachineLibrary_RobotWinCCToRobots,
)
MachineLibrary_RobotConfSendOrders_strategy = st.builds(
    MachineLibrary_RobotConfSendOrders,
)
MachineLibrary_RobotVarToBusyCodes_strategy = st.builds(
    MachineLibrary_RobotVarToBusyCodes,
)
MachineLibrary_Parameter_strategy = st.builds(
    MachineLibrary_Parameter,
    parameterConfig=
        safe_text,
    parameterParaLen=
        st.integers(),
    parameterT1=
        safe_text,
    parameterMin=
        st.integers(),
    parameterT2=
        safe_text,
    parameterV=
        safe_text,
    parameterName=
        safe_text,
    parameterV0=
        safe_text,
    parameterV1=
        safe_text,
    parameterMax=
        st.integers(),
    parameterType=
        safe_text
)
MachineLibrary_PlainMove_strategy = st.builds(
    MachineLibrary_PlainMove,
    plainmovePreDefWS=
        safe_text,
    plainmoveSID_REF=
        safe_text,
    plainmoveType=
        st.integers()
)
MachineLibrary_Transfer_strategy = st.builds(
    MachineLibrary_Transfer,
)
MachineLibrary_ParamPrint_strategy = st.builds(
    MachineLibrary_ParamPrint,
    vertPosData=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    horzPosValues=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    horzPosLeftBorder=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    vertPosHeader=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dateStamp=
        safe_text,
    vertLineSpace=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fontHightData=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fontHightHeader=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MachineLibrary_NodeProgram_strategy = st.builds(
    MachineLibrary_NodeProgram,
    programSection=
        safe_text,
    programNo=
        st.integers(),
    programAddress=
        safe_text,
    programName=
        safe_text,
    programLenPerParam=
        safe_text
)
MachineLibrary_Command_strategy = st.builds(
    MachineLibrary_Command,
    commandNo=
        safe_text,
    commandName=
        safe_text,
    commandProgParameter=
        st.integers()
)
MachineLibrary_UnitProgParameters_strategy = st.builds(
    MachineLibrary_UnitProgParameters,
    parameterNo=
        st.integers(),
    parameter=
        safe_text
)
MachineLibrary_UnitProgram_strategy = st.builds(
    MachineLibrary_UnitProgram,
    unitProgName=
        safe_text
)
MachineLibrary_Position_strategy = st.builds(
    MachineLibrary_Position,
    posExit=
        st.integers(),
    posIndex=
        st.integers(),
    posName=
        safe_text,
    posRemark=
        safe_text,
    posNo=
        st.integers(),
    posWarningOnDelete=
        st.integers()
)
MachineLibrary_Button_strategy = st.builds(
    MachineLibrary_Button,
    buttonText=
        safe_text,
    commandNo=
        st.integers(),
    buttonNo=
        st.integers()
)
MachineLibrary_CheckAddSID_Values_PM2PM_strategy = st.builds(
    MachineLibrary_CheckAddSID_Values_PM2PM,
    optionNo=
        st.integers(),
    optonValue=
        safe_text
)
MachineLibrary_SepByComma_ID_Scanner_strategy = st.builds(
    MachineLibrary_SepByComma_ID_Scanner,
    idPrevValue=
        safe_text,
    idCharValue=
        safe_text,
    idSeq_X=
        st.integers(),
    idValue=
        st.integers()
)
MachineLibrary_SepByComma_Field_Scanner_strategy = st.builds(
    MachineLibrary_SepByComma_Field_Scanner,
    fieldNo=
        st.integers(),
    fieldName=
        safe_text
)
MachineLibrary_StatusBit_strategy = st.builds(
    MachineLibrary_StatusBit,
    bitName=
        safe_text,
    bitNo=
        st.integers()
)
MachineLibrary_HistoryConfig_AccuPyc_strategy = st.builds(
    MachineLibrary_HistoryConfig_AccuPyc,
    sampleCupWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    currentSample=
        safe_text,
    currentSampleID=
        safe_text
)
MachineLibrary_CheckSampleConfig_SuperQXRF_strategy = st.builds(
    MachineLibrary_CheckSampleConfig_SuperQXRF,
    anaProg=
        safe_text,
    minutes=
        safe_text,
    program=
        safe_text,
    sampleID=
        safe_text,
    seq_X=
        st.integers(),
    samples=
        safe_text
)
MachineLibrary_InsertRemove_Keywords_Host_strategy = st.builds(
    MachineLibrary_InsertRemove_Keywords_Host,
    keywordKey=
        safe_text,
    keywordValue=
        safe_text
)
MachineLibrary_InsertRemove_Types_Host_strategy = st.builds(
    MachineLibrary_InsertRemove_Types_Host,
    typeNo=
        st.integers(),
    typeValue=
        safe_text
)
MachineLibrary_InsertRemove_Entry_Host_strategy = st.builds(
    MachineLibrary_InsertRemove_Entry_Host,
    entryName=
        safe_text,
    entryNo=
        st.integers()
)
MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_strategy = st.builds(
    MachineLibrary_CheckSampleRunTimeParams_SuperQXRF,
    value=
        st.integers(),
    sampleType=
        st.integers()
)
MachineLibrary_OES_XRF_Condition_strategy = st.builds(
    MachineLibrary_OES_XRF_Condition,
    comment=
        safe_text,
    para=
        safe_text,
    seq_X=
        st.integers(),
    paraName=
        safe_text
)
MachineLibrary_InsertRemove_Host_strategy = st.builds(
    MachineLibrary_InsertRemove_Host,
    report_All=
        st.integers()
)
MachineLibrary_Moved_Host_strategy = st.builds(
    MachineLibrary_Moved_Host,
    pos0=
        st.integers(),
    report_ALL=
        st.integers(),
    writePositionNameInFile=
        st.integers(),
    type0=
        st.integers()
)
MachineLibrary_WS_Update_Host_strategy = st.builds(
    MachineLibrary_WS_Update_Host,
    AllowUnit0=
        st.integers(),
    checkUnit=
        st.integers()
)
MachineLibrary_Report_Host_strategy = st.builds(
    MachineLibrary_Report_Host,
    note1=
        safe_text,
    sendErrorWarningsMsgOnly=
        st.integers(),
    maxType=
        st.integers(),
    stateChanged=
        st.integers(),
    sampleInsert=
        st.integers(),
    timeStamp=
        st.integers(),
    sampleRemoved=
        st.integers(),
    rawData=
        st.integers(),
    sendLifeMessages=
        st.integers(),
    fileName=
        safe_text,
    sampleMoved=
        st.integers(),
    internal=
        st.integers(),
    minType=
        st.integers(),
    note=
        safe_text
)
MachineLibrary_Settings_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_Settings_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_DisableSCT_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_DisableSCT_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_ExePrepUnit_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_ExePrepUnit_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_ExecuteFiling_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_ExecuteFiling_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_CheckFilling_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_CheckFilling_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_CheckSample_SuperQXRF_strategy = st.builds(
    MachineLibrary_CheckSample_SuperQXRF,
)
MachineLibrary_CheckSampleRunTime_SuperQXRF_strategy = st.builds(
    MachineLibrary_CheckSampleRunTime_SuperQXRF,
)
MachineLibrary_Communication_SuperQXRF_strategy = st.builds(
    MachineLibrary_Communication_SuperQXRF,
    enq_ACK_Protocol=
        st.integers()
)
MachineLibrary_ControlSamples_SuperQXRF_strategy = st.builds(
    MachineLibrary_ControlSamples_SuperQXRF,
    outOfControl=
        st.integers()
)
MachineLibrary_File_Sample_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_File_Sample_ARL_XRF_OES,
    noSuccess=
        safe_text
)
MachineLibrary_PS_Process_Finished_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_PS_Process_Finished_ARL_XRF_OES,
    noSuccess=
        safe_text
)
MachineLibrary_GeneralSetting_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_GeneralSetting_ARL_XRF_OES,
    name=
        safe_text
)
MachineLibrary_CheckAddSID_PM2PM_strategy = st.builds(
    MachineLibrary_CheckAddSID_PM2PM,
)
MachineLibrary_SepByComma_Scanner_strategy = st.builds(
    MachineLibrary_SepByComma_Scanner,
    preDefWS=
        st.integers(),
    activ=
        st.integers()
)
MachineLibrary_History_AccuPycMeter_strategy = st.builds(
    MachineLibrary_History_AccuPycMeter,
)
MachineLibrary_UnitConfig_Host_strategy = st.builds(
    MachineLibrary_UnitConfig_Host,
)
MachineLibrary_UnitConfig_ARL_XRF_OES_strategy = st.builds(
    MachineLibrary_UnitConfig_ARL_XRF_OES,
)
MachineLibrary_UnitConfig_SuperQ_XRF_strategy = st.builds(
    MachineLibrary_UnitConfig_SuperQ_XRF,
)
MachineLibrary_UnitConfig_OBLF_OES_strategy = st.builds(
    MachineLibrary_UnitConfig_OBLF_OES,
)
MachineLibrary_UnitConfig_Terminal_strategy = st.builds(
    MachineLibrary_UnitConfig_Terminal,
)
MachineLibrary_GeneralParameter_SuperQXRF_strategy = st.builds(
    MachineLibrary_GeneralParameter_SuperQXRF,
    startList=
        safe_text,
    listName=
        safe_text,
    switchRemote=
        safe_text
)
MachineLibrary_ErrorMessage_OBLFOES_strategy = st.builds(
    MachineLibrary_ErrorMessage_OBLFOES,
    errorMessage=
        safe_text
)
MachineLibrary_RecalRequest_OBLFOES_strategy = st.builds(
    MachineLibrary_RecalRequest_OBLFOES,
    name=
        safe_text
)
MachineLibrary_TestRequest_OBLFOES_strategy = st.builds(
    MachineLibrary_TestRequest_OBLFOES,
    name=
        safe_text
)
MachineLibrary_OutputRequest_OBLFOES_strategy = st.builds(
    MachineLibrary_OutputRequest_OBLFOES,
    name=
        safe_text
)
MachineLibrary_Translate_Terminal_strategy = st.builds(
    MachineLibrary_Translate_Terminal,
    man_Busy=
        safe_text,
    man_Ready=
        safe_text,
    auto_Busy=
        safe_text,
    auto_Ready=
        safe_text
)
MachineLibrary_UnitGeneral_Scanner_strategy = st.builds(
    MachineLibrary_UnitGeneral_Scanner,
    start=
        st.integers(),
    addString=
        safe_text,
    preString=
        safe_text,
    forcedSampleType=
        st.integers(),
    registerSample=
        st.integers(),
    length=
        st.integers(),
    fillWith=
        safe_text
)
MachineLibrary_UnitGeneral_RigakuXRF_strategy = st.builds(
    MachineLibrary_UnitGeneral_RigakuXRF,
    lastPosInInstrument=
        st.integers(),
    lastPosAnalyHAG_SIg=
        st.integers(),
    separator=
        st.integers(),
    lastPoHAG_SIInstrument=
        st.integers()
)
MachineLibrary_UnitGeneral_SuperQ_strategy = st.builds(
    MachineLibrary_UnitGeneral_SuperQ,
    lastPosAnalysing=
        st.integers(),
    lastPosInInstrument=
        st.integers()
)
MachineLibrary_UnitGeneral_AccPyc_strategy = st.builds(
    MachineLibrary_UnitGeneral_AccPyc,
    cupWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minSampleWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MachineLibrary_UnitGeneral_PM2PM_strategy = st.builds(
    MachineLibrary_UnitGeneral_PM2PM,
    processFeedBack=
        safe_text,
    sid_Mask=
        safe_text
)
MachineLibrary_UnitGeneral_Remote_strategy = st.builds(
    MachineLibrary_UnitGeneral_Remote,
    editWSDB=
        st.booleans(),
    handshakeT=
        st.integers(),
    handshakeQ=
        safe_text,
    handshakeA=
        safe_text
)
MachineLibrary_UnitGeneral_HostPC_strategy = st.builds(
    MachineLibrary_UnitGeneral_HostPC,
    index=
        st.integers(),
    replyOnLink=
        st.integers(),
    writeDumyIfNoDataExist=
        st.integers(),
    maxIndex=
        st.integers()
)
MachineLibrary_UnitGeneral_Terminal_strategy = st.builds(
    MachineLibrary_UnitGeneral_Terminal,
    station1=
        safe_text,
    station5=
        safe_text,
    station2=
        safe_text,
    thisStation=
        safe_text,
    station4=
        safe_text,
    station3=
        safe_text
)
MachineLibrary_PLCtoPmMatrix_strategy = st.builds(
    MachineLibrary_PLCtoPmMatrix,
    plcpmmatrixBit0=
        st.integers(),
    plcpmmatrixBit14=
        st.integers(),
    plcpmmatrixBit7=
        st.integers(),
    plcpmmatrixBit12=
        st.integers(),
    plcpmmatrixBit4=
        st.integers(),
    plcpmmatrixBit1=
        st.integers(),
    plcpmmatrixBit5=
        st.integers(),
    plcpmmatrixBit10=
        st.integers(),
    plcpmmatrixBit6=
        st.integers(),
    plcpmmatrixBit13=
        st.integers(),
    plcpmmatrixBit15=
        st.integers(),
    plcpmmatrixBit8=
        st.integers(),
    plcpmmatrixBit9=
        st.integers(),
    plcpmmatrixBit11=
        st.integers(),
    plcpmmatrixBit3=
        st.integers(),
    plcpmmatrixBit2=
        st.integers()
)
MachineLibrary_StausBits_strategy = st.builds(
    MachineLibrary_StausBits,
)
MachineLibrary_Positions_strategy = st.builds(
    MachineLibrary_Positions,
)
MachineLibrary_WinCCAddTag_strategy = st.builds(
    MachineLibrary_WinCCAddTag,
    winCCTag=
        safe_text
)
MachineLibrary_UnitGeneralParameters_strategy = st.builds(
    MachineLibrary_UnitGeneralParameters,
    defaultValue_1=
        st.integers(),
    UseWith_1=
        safe_text,
    visibleType_1=
        st.integers(),
    comment_1=
        safe_text,
    unit_1=
        safe_text,
    maxValue_1=
        st.integers(),
    minValue_1=
        st.integers(),
    canBeChange_1=
        st.integers(),
    KeyWord_1=
        safe_text,
    paraName_1=
        safe_text,
    seq_X=
        st.integers()
)
MachineLibrary_UnitSpecialConfiguration_strategy = st.builds(
    MachineLibrary_UnitSpecialConfiguration,
)
MachineLibrary_UnitGeneralSpecial_strategy = st.builds(
    MachineLibrary_UnitGeneralSpecial,
)
MachineLibrary_UnitGeneral_strategy = st.builds(
    MachineLibrary_UnitGeneral,
)
MachineLibrary_Buttons_strategy = st.builds(
    MachineLibrary_Buttons,
)
MachineLibrary_UnitPrograms_strategy = st.builds(
    MachineLibrary_UnitPrograms,
)
MachineLibrary_NodeGeneral_RigakuXRF_strategy = st.builds(
    MachineLibrary_NodeGeneral_RigakuXRF,
    timeout=
        st.integers(),
    timerToSendStatus=
        st.integers(),
    bDoNotshiftAtExit=
        st.integers(),
    timeoutResponce=
        st.integers()
)
MachineLibrary_NodeGeneral_AccuPycMeter_strategy = st.builds(
    MachineLibrary_NodeGeneral_AccuPycMeter,
    runTimout=
        st.integers(),
    expectSampleWeight=
        st.integers(),
    polling=
        st.integers(),
    sendSampleWeight=
        st.integers()
)
MachineLibrary_NodeGeneral_WinCC2WinCC_strategy = st.builds(
    MachineLibrary_NodeGeneral_WinCC2WinCC,
    prefix=
        safe_text
)
MachineLibrary_NodeGeneral_RemotePM_strategy = st.builds(
    MachineLibrary_NodeGeneral_RemotePM,
    system=
        safe_text,
    timeServer=
        st.integers()
)
MachineLibrary_NodeGeneral_PM2PM_strategy = st.builds(
    MachineLibrary_NodeGeneral_PM2PM,
    timeServer=
        st.integers(),
    type=
        st.integers()
)
MachineLibrary_NodeGeneral_Terminal_strategy = st.builds(
    MachineLibrary_NodeGeneral_Terminal,
    name_3=
        safe_text,
    signalCarrierPresent=
        st.integers(),
    steelCarrier=
        safe_text,
    keyBoardSignalCarrierPresent=
        st.integers(),
    maxScreens=
        st.integers(),
    name_5=
        safe_text,
    name_6=
        safe_text,
    stationAuto=
        safe_text,
    terminalType=
        st.integers(),
    name_4=
        safe_text,
    customTimer1=
        st.integers(),
    maxXValue=
        st.integers(),
    maxYValue=
        st.integers(),
    name_2=
        safe_text,
    displayTime=
        st.integers(),
    stationReady=
        safe_text,
    name_1=
        safe_text,
    customTimer2=
        st.integers(),
    lenOfPlanID=
        st.integers(),
    stationType=
        st.integers()
)
MachineLibrary_NodeGeneralSpecial_strategy = st.builds(
    MachineLibrary_NodeGeneralSpecial,
)
MachineLibrary_NodeGeneral_strategy = st.builds(
    MachineLibrary_NodeGeneral,
    canCreateErrorTag=
        safe_text,
    canCreateStateTag=
        safe_text
)
MachineLibrary_NodeSpecialConfiguration_strategy = st.builds(
    MachineLibrary_NodeSpecialConfiguration,
)
MachineLibrary_CommunicationData_strategy = st.builds(
    MachineLibrary_CommunicationData,
    comErrorDataLength=
        st.integers(),
    comSendDataAddress=
        safe_text,
    comErrorDataAddress=
        safe_text,
    comRequestDataLength=
        st.integers(),
    comSIDDataLength=
        st.integers(),
    comProgressIndDataLength=
        st.integers(),
    comSendDataLength=
        st.integers(),
    comRequestDataAddress=
        safe_text,
    comSIDDataAddress=
        safe_text,
    comProgressIndDataAddress=
        safe_text
)
MachineLibrary_Parameters_strategy = st.builds(
    MachineLibrary_Parameters,
    parameterConfigNo=
        safe_text,
    parameterConfigYes=
        safe_text
)
MachineLibrary_NodePrograms_strategy = st.builds(
    MachineLibrary_NodePrograms,
)
MachineLibrary_Commands_strategy = st.builds(
    MachineLibrary_Commands,
)
MachineLibrary_Units_strategy = st.builds(
    MachineLibrary_Units,
    unitNo=
        st.integers(),
    unitName=
        safe_text,
    internalUniNo=
        st.integers()
)
MachineLibrary_DPbase_Node_strategy = st.builds(
    MachineLibrary_DPbase_Node,
    isXPS=
        st.integers(),
    nodeNo=
        st.integers()
)
MachineLibrary_Compac_Link_strategy = st.builds(
    MachineLibrary_Compac_Link,
    checksumCode=
        st.integers(),
    splitLongMessage=
        st.integers(),
    retry=
        st.integers(),
    bytecountcode=
        st.integers(),
    checksum=
        st.integers(),
    bcc=
        st.integers(),
    timeout=
        st.integers(),
    commConfig=
        safe_text,
    useNotACK_NAK=
        st.integers(),
    useNotENQ=
        st.integers(),
    byteCount=
        st.integers(),
    port=
        safe_text,
    maxDataLength=
        st.integers(),
    params=
        safe_text
)
MachineLibrary_FileTransfer_Link_strategy = st.builds(
    MachineLibrary_FileTransfer_Link,
    flagToWriteWaitFor=
        st.integers(),
    flagWriteAfterReading=
        st.integers(),
    timeoutwrite=
        safe_text,
    pollTime=
        st.integers(),
    delimter=
        safe_text,
    flagDelAfterReading=
        st.integers(),
    writeAfterReading=
        st.integers(),
    toWriteWaitFor=
        safe_text,
    flagToWriteWaitForDeleted=
        st.integers(),
    writePath=
        safe_text,
    translation=
        st.integers(),
    sendBuffer=
        st.integers(),
    receiveBuffer=
        st.integers(),
    readPath=
        safe_text,
    delimiter=
        safe_text,
    maxDataLength=
        st.integers()
)
MachineLibrary_Serial_Link_strategy = st.builds(
    MachineLibrary_Serial_Link,
    maxCharDelay=
        safe_text,
    commConfig=
        safe_text,
    params=
        safe_text,
    port=
        safe_text,
    endChar=
        safe_text,
    startChar=
        safe_text,
    bufferLenght=
        safe_text,
    logging=
        st.integers()
)
MachineLibrary_TCPIP_Link_strategy = st.builds(
    MachineLibrary_TCPIP_Link,
    address_1=
        safe_text,
    sendBuffer=
        st.integers(),
    msgDelay=
        st.integers(),
    receiveBuffer=
        st.integers(),
    port=
        st.integers(),
    address_5=
        safe_text,
    maxDataSize=
        st.integers(),
    address_6=
        safe_text,
    protocol=
        st.integers(),
    address_3=
        safe_text,
    termChar=
        st.integers(),
    address_2=
        safe_text,
    address_4=
        safe_text
)
MachineLibrary_WinCCLnk_strategy = st.builds(
    MachineLibrary_WinCCLnk,
    updateCycle=
        st.integers(),
    canCreateTags=
        st.integers(),
    updateCycle_Help=
        safe_text,
    canModifyTag=
        st.integers(),
    connectionName=
        safe_text
)
MachineLibrary_LinkConfig_strategy = st.builds(
    MachineLibrary_LinkConfig,
)
MachineLibrary_NodeConfig_strategy = st.builds(
    MachineLibrary_NodeConfig,
    nodeName=
        safe_text,
    simFileName=
        safe_text,
    nodeNo=
        st.integers()
)
MachineLibrary_Link2_strategy = st.builds(
    MachineLibrary_Link2,
    link2ParamSection=
        safe_text,
    link2Type=
        safe_text,
    link2ParamFile=
        safe_text
)
MachineLibrary_DPbase_Link_strategy = st.builds(
    MachineLibrary_DPbase_Link,
    cp_name=
        safe_text,
    speed=
        st.integers(),
    maxNodes=
        st.integers()
)
MachineLibrary_IBMWebsphereMQ_strategy = st.builds(
    MachineLibrary_IBMWebsphereMQ,
    qName=
        safe_text,
    sendDynamicQueName=
        safe_text,
    sendBuffer=
        st.integers(),
    sendQueName=
        safe_text,
    maxDataSize=
        st.integers(),
    receiveBuffer=
        st.integers(),
    sendQueMgrName=
        safe_text,
    readDynamicQueName=
        safe_text,
    readQueMgrName=
        safe_text,
    readQueName=
        safe_text
)
MachineLibrary_LabMachine_strategy = st.builds(
    MachineLibrary_LabMachine,
    linkParamFile=
        safe_text,
    versionRemark=
        safe_text,
    machineVersionNo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    linkParamSection=
        safe_text,
    driver=
        safe_text,
    machineName=
        safe_text,
    createWinCCTags=
        safe_text,
    linkType=
        safe_text
)
MachineLibrary_LabMachines_strategy = st.builds(
    MachineLibrary_LabMachines,
)
MachineLibrary_PMMachineLibrary_strategy = st.builds(
    MachineLibrary_PMMachineLibrary,
    libraryVersion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    libraryVersionRemark=
        safe_text
)

@given(instance=MachineLibrary_RobotToWinCC_strategy)
@settings(max_examples=50)
def test_machinelibrary_robottowincc_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotToWinCC)



@given(instance=MachineLibrary_RobotToWinCC_strategy)
def test_machinelibrary_robottowincc_robotToWinccSeq_X_setter(instance):
    original = instance.robotToWinccSeq_X
    instance.robotToWinccSeq_X = original
    assert instance.robotToWinccSeq_X == original



@given(instance=MachineLibrary_RobotToWinCC_strategy)
def test_machinelibrary_robottowincc_robotToWinccType_X_setter(instance):
    original = instance.robotToWinccType_X
    instance.robotToWinccType_X = original
    assert instance.robotToWinccType_X == original



@given(instance=MachineLibrary_RobotToWinCC_strategy)
def test_machinelibrary_robottowincc_robotToWinccTo_X_setter(instance):
    original = instance.robotToWinccTo_X
    instance.robotToWinccTo_X = original
    assert instance.robotToWinccTo_X == original



@given(instance=MachineLibrary_RobotToWinCC_strategy)
def test_machinelibrary_robottowincc_robotToWinccFrom_X_setter(instance):
    original = instance.robotToWinccFrom_X
    instance.robotToWinccFrom_X = original
    assert instance.robotToWinccFrom_X == original

@given(instance=MachineLibrary_RobotWinCCToRobot_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotwincctorobot_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotWinCCToRobot)



@given(instance=MachineLibrary_RobotWinCCToRobot_strategy)
def test_machinelibrary_robotwincctorobot_robotwincctorobotTo_X_setter(instance):
    original = instance.robotwincctorobotTo_X
    instance.robotwincctorobotTo_X = original
    assert instance.robotwincctorobotTo_X == original



@given(instance=MachineLibrary_RobotWinCCToRobot_strategy)
def test_machinelibrary_robotwincctorobot_robotwincctorobootType_X_setter(instance):
    original = instance.robotwincctorobootType_X
    instance.robotwincctorobootType_X = original
    assert instance.robotwincctorobootType_X == original



@given(instance=MachineLibrary_RobotWinCCToRobot_strategy)
def test_machinelibrary_robotwincctorobot_robotwincctorobotFrom_X_setter(instance):
    original = instance.robotwincctorobotFrom_X
    instance.robotwincctorobotFrom_X = original
    assert instance.robotwincctorobotFrom_X == original



@given(instance=MachineLibrary_RobotWinCCToRobot_strategy)
def test_machinelibrary_robotwincctorobot_robotwincctorobootSeq_X_setter(instance):
    original = instance.robotwincctorobootSeq_X
    instance.robotwincctorobootSeq_X = original
    assert instance.robotwincctorobootSeq_X == original

@given(instance=MachineLibrary_RobotConfSendOrder_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotconfsendorder_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotConfSendOrder)



@given(instance=MachineLibrary_RobotConfSendOrder_strategy)
def test_machinelibrary_robotconfsendorder_robotconfsendorderVar_X_setter(instance):
    original = instance.robotconfsendorderVar_X
    instance.robotconfsendorderVar_X = original
    assert instance.robotconfsendorderVar_X == original



@given(instance=MachineLibrary_RobotConfSendOrder_strategy)
def test_machinelibrary_robotconfsendorder_robotconfsendorderType_X_setter(instance):
    original = instance.robotconfsendorderType_X
    instance.robotconfsendorderType_X = original
    assert instance.robotconfsendorderType_X == original



@given(instance=MachineLibrary_RobotConfSendOrder_strategy)
def test_machinelibrary_robotconfsendorder_robotconfsendorderSeq_X_setter(instance):
    original = instance.robotconfsendorderSeq_X
    instance.robotconfsendorderSeq_X = original
    assert instance.robotconfsendorderSeq_X == original



@given(instance=MachineLibrary_RobotConfSendOrder_strategy)
def test_machinelibrary_robotconfsendorder_robotconfsendorderFrom_X_setter(instance):
    original = instance.robotconfsendorderFrom_X
    instance.robotconfsendorderFrom_X = original
    assert instance.robotconfsendorderFrom_X == original

@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotvartobusycode_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotVarToBusycode)



@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
def test_machinelibrary_robotvartobusycode_robotvartobusycodeSeq_X_setter(instance):
    original = instance.robotvartobusycodeSeq_X
    instance.robotvartobusycodeSeq_X = original
    assert instance.robotvartobusycodeSeq_X == original



@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
def test_machinelibrary_robotvartobusycode_robotvartobusycodeType_X_setter(instance):
    original = instance.robotvartobusycodeType_X
    instance.robotvartobusycodeType_X = original
    assert instance.robotvartobusycodeType_X == original



@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
def test_machinelibrary_robotvartobusycode_robotvartobusycodeVar_X_setter(instance):
    original = instance.robotvartobusycodeVar_X
    instance.robotvartobusycodeVar_X = original
    assert instance.robotvartobusycodeVar_X == original



@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
def test_machinelibrary_robotvartobusycode_robotvartobusycodeUnit_X_setter(instance):
    original = instance.robotvartobusycodeUnit_X
    instance.robotvartobusycodeUnit_X = original
    assert instance.robotvartobusycodeUnit_X == original



@given(instance=MachineLibrary_RobotVarToBusycode_strategy)
def test_machinelibrary_robotvartobusycode_robotvartobusycodeBit_X_setter(instance):
    original = instance.robotvartobusycodeBit_X
    instance.robotvartobusycodeBit_X = original
    assert instance.robotvartobusycodeBit_X == original

@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotvartoerrorbit_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotVarToErrorbit)



@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
def test_machinelibrary_robotvartoerrorbit_robotvartoerrorbitSeq_X_setter(instance):
    original = instance.robotvartoerrorbitSeq_X
    instance.robotvartoerrorbitSeq_X = original
    assert instance.robotvartoerrorbitSeq_X == original



@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
def test_machinelibrary_robotvartoerrorbit_robotvartoerrorbitType_X_setter(instance):
    original = instance.robotvartoerrorbitType_X
    instance.robotvartoerrorbitType_X = original
    assert instance.robotvartoerrorbitType_X == original



@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
def test_machinelibrary_robotvartoerrorbit_robotvartoerrorbitBit_X_setter(instance):
    original = instance.robotvartoerrorbitBit_X
    instance.robotvartoerrorbitBit_X = original
    assert instance.robotvartoerrorbitBit_X == original



@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
def test_machinelibrary_robotvartoerrorbit_robotvartoerrorbitVar_X_setter(instance):
    original = instance.robotvartoerrorbitVar_X
    instance.robotvartoerrorbitVar_X = original
    assert instance.robotvartoerrorbitVar_X == original



@given(instance=MachineLibrary_RobotVarToErrorbit_strategy)
def test_machinelibrary_robotvartoerrorbit_robotvartoerrorbitInv_X_setter(instance):
    original = instance.robotvartoerrorbitInv_X
    instance.robotvartoerrorbitInv_X = original
    assert instance.robotvartoerrorbitInv_X == original

@given(instance=MachineLibrary_PlainMoveEntrySend_strategy)
@settings(max_examples=50)
def test_machinelibrary_plainmoveentrysend_instantiation(instance):
    assert isinstance(instance, MachineLibrary_PlainMoveEntrySend)



@given(instance=MachineLibrary_PlainMoveEntrySend_strategy)
def test_machinelibrary_plainmoveentrysend_plainmoveSeq_setter(instance):
    original = instance.plainmoveSeq
    instance.plainmoveSeq = original
    assert instance.plainmoveSeq == original



@given(instance=MachineLibrary_PlainMoveEntrySend_strategy)
def test_machinelibrary_plainmoveentrysend_plainmoveEntry_setter(instance):
    original = instance.plainmoveEntry
    instance.plainmoveEntry = original
    assert instance.plainmoveEntry == original



@given(instance=MachineLibrary_PlainMoveEntrySend_strategy)
def test_machinelibrary_plainmoveentrysend_plainmoveSend_setter(instance):
    original = instance.plainmoveSend
    instance.plainmoveSend = original
    assert instance.plainmoveSend == original

@given(instance=MachineLibrary_TransferFileSection_strategy)
@settings(max_examples=50)
def test_machinelibrary_transferfilesection_instantiation(instance):
    assert isinstance(instance, MachineLibrary_TransferFileSection)



@given(instance=MachineLibrary_TransferFileSection_strategy)
def test_machinelibrary_transferfilesection_transferSection_setter(instance):
    original = instance.transferSection
    instance.transferSection = original
    assert instance.transferSection == original



@given(instance=MachineLibrary_TransferFileSection_strategy)
def test_machinelibrary_transferfilesection_transferFile_setter(instance):
    original = instance.transferFile
    instance.transferFile = original
    assert instance.transferFile == original



@given(instance=MachineLibrary_TransferFileSection_strategy)
def test_machinelibrary_transferfilesection_transferSeq_setter(instance):
    original = instance.transferSeq
    instance.transferSeq = original
    assert instance.transferSeq == original

@given(instance=MachineLibrary_RobotConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotConfiguration)



@given(instance=MachineLibrary_RobotConfiguration_strategy)
def test_machinelibrary_robotconfiguration_robotIPAddress_setter(instance):
    original = instance.robotIPAddress
    instance.robotIPAddress = original
    assert instance.robotIPAddress == original



@given(instance=MachineLibrary_RobotConfiguration_strategy)
def test_machinelibrary_robotconfiguration_robotSystemID_setter(instance):
    original = instance.robotSystemID
    instance.robotSystemID = original
    assert instance.robotSystemID == original



@given(instance=MachineLibrary_RobotConfiguration_strategy)
def test_machinelibrary_robotconfiguration_robotActivate_setter(instance):
    original = instance.robotActivate
    instance.robotActivate = original
    assert instance.robotActivate == original



@given(instance=MachineLibrary_RobotConfiguration_strategy)
def test_machinelibrary_robotconfiguration_robotID_setter(instance):
    original = instance.robotID
    instance.robotID = original
    assert instance.robotID == original

@given(instance=MachineLibrary_RobotVarToErrorbits_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotvartoerrorbits_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotVarToErrorbits)

@given(instance=MachineLibrary_RobotWarningONDelete_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotwarningondelete_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotWarningONDelete)



@given(instance=MachineLibrary_RobotWarningONDelete_strategy)
def test_machinelibrary_robotwarningondelete_robotExtraUnit_2_setter(instance):
    original = instance.robotExtraUnit_2
    instance.robotExtraUnit_2 = original
    assert instance.robotExtraUnit_2 == original



@given(instance=MachineLibrary_RobotWarningONDelete_strategy)
def test_machinelibrary_robotwarningondelete_robotExtraPos_1_setter(instance):
    original = instance.robotExtraPos_1
    instance.robotExtraPos_1 = original
    assert instance.robotExtraPos_1 == original



@given(instance=MachineLibrary_RobotWarningONDelete_strategy)
def test_machinelibrary_robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_PM_setter(instance):
    original = instance.robotErrBitWhenConfirmationIsNeededFor_PM
    instance.robotErrBitWhenConfirmationIsNeededFor_PM = original
    assert instance.robotErrBitWhenConfirmationIsNeededFor_PM == original



@given(instance=MachineLibrary_RobotWarningONDelete_strategy)
def test_machinelibrary_robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_Robot_setter(instance):
    original = instance.robotErrBitWhenConfirmationIsNeededFor_Robot
    instance.robotErrBitWhenConfirmationIsNeededFor_Robot = original
    assert instance.robotErrBitWhenConfirmationIsNeededFor_Robot == original

@given(instance=MachineLibrary_RobotToWinccs_strategy)
@settings(max_examples=50)
def test_machinelibrary_robottowinccs_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotToWinccs)

@given(instance=MachineLibrary_RobotWinCCToRobots_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotwincctorobots_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotWinCCToRobots)

@given(instance=MachineLibrary_RobotConfSendOrders_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotconfsendorders_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotConfSendOrders)

@given(instance=MachineLibrary_RobotVarToBusyCodes_strategy)
@settings(max_examples=50)
def test_machinelibrary_robotvartobusycodes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RobotVarToBusyCodes)

@given(instance=MachineLibrary_Parameter_strategy)
@settings(max_examples=50)
def test_machinelibrary_parameter_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Parameter)



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterConfig_setter(instance):
    original = instance.parameterConfig
    instance.parameterConfig = original
    assert instance.parameterConfig == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterParaLen_setter(instance):
    original = instance.parameterParaLen
    instance.parameterParaLen = original
    assert instance.parameterParaLen == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterT1_setter(instance):
    original = instance.parameterT1
    instance.parameterT1 = original
    assert instance.parameterT1 == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterMin_setter(instance):
    original = instance.parameterMin
    instance.parameterMin = original
    assert instance.parameterMin == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterT2_setter(instance):
    original = instance.parameterT2
    instance.parameterT2 = original
    assert instance.parameterT2 == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterV_setter(instance):
    original = instance.parameterV
    instance.parameterV = original
    assert instance.parameterV == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterV0_setter(instance):
    original = instance.parameterV0
    instance.parameterV0 = original
    assert instance.parameterV0 == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterV1_setter(instance):
    original = instance.parameterV1
    instance.parameterV1 = original
    assert instance.parameterV1 == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterMax_setter(instance):
    original = instance.parameterMax
    instance.parameterMax = original
    assert instance.parameterMax == original



@given(instance=MachineLibrary_Parameter_strategy)
def test_machinelibrary_parameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=MachineLibrary_PlainMove_strategy)
@settings(max_examples=50)
def test_machinelibrary_plainmove_instantiation(instance):
    assert isinstance(instance, MachineLibrary_PlainMove)



@given(instance=MachineLibrary_PlainMove_strategy)
def test_machinelibrary_plainmove_plainmovePreDefWS_setter(instance):
    original = instance.plainmovePreDefWS
    instance.plainmovePreDefWS = original
    assert instance.plainmovePreDefWS == original



@given(instance=MachineLibrary_PlainMove_strategy)
def test_machinelibrary_plainmove_plainmoveSID_REF_setter(instance):
    original = instance.plainmoveSID_REF
    instance.plainmoveSID_REF = original
    assert instance.plainmoveSID_REF == original



@given(instance=MachineLibrary_PlainMove_strategy)
def test_machinelibrary_plainmove_plainmoveType_setter(instance):
    original = instance.plainmoveType
    instance.plainmoveType = original
    assert instance.plainmoveType == original

@given(instance=MachineLibrary_Transfer_strategy)
@settings(max_examples=50)
def test_machinelibrary_transfer_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Transfer)

@given(instance=MachineLibrary_ParamPrint_strategy)
@settings(max_examples=50)
def test_machinelibrary_paramprint_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ParamPrint)



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_vertPosData_setter(instance):
    original = instance.vertPosData
    instance.vertPosData = original
    assert instance.vertPosData == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_horzPosValues_setter(instance):
    original = instance.horzPosValues
    instance.horzPosValues = original
    assert instance.horzPosValues == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_horzPosLeftBorder_setter(instance):
    original = instance.horzPosLeftBorder
    instance.horzPosLeftBorder = original
    assert instance.horzPosLeftBorder == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_vertPosHeader_setter(instance):
    original = instance.vertPosHeader
    instance.vertPosHeader = original
    assert instance.vertPosHeader == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_dateStamp_setter(instance):
    original = instance.dateStamp
    instance.dateStamp = original
    assert instance.dateStamp == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_vertLineSpace_setter(instance):
    original = instance.vertLineSpace
    instance.vertLineSpace = original
    assert instance.vertLineSpace == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_fontHightData_setter(instance):
    original = instance.fontHightData
    instance.fontHightData = original
    assert instance.fontHightData == original



@given(instance=MachineLibrary_ParamPrint_strategy)
def test_machinelibrary_paramprint_fontHightHeader_setter(instance):
    original = instance.fontHightHeader
    instance.fontHightHeader = original
    assert instance.fontHightHeader == original

@given(instance=MachineLibrary_NodeProgram_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodeprogram_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeProgram)



@given(instance=MachineLibrary_NodeProgram_strategy)
def test_machinelibrary_nodeprogram_programSection_setter(instance):
    original = instance.programSection
    instance.programSection = original
    assert instance.programSection == original



@given(instance=MachineLibrary_NodeProgram_strategy)
def test_machinelibrary_nodeprogram_programNo_setter(instance):
    original = instance.programNo
    instance.programNo = original
    assert instance.programNo == original



@given(instance=MachineLibrary_NodeProgram_strategy)
def test_machinelibrary_nodeprogram_programAddress_setter(instance):
    original = instance.programAddress
    instance.programAddress = original
    assert instance.programAddress == original



@given(instance=MachineLibrary_NodeProgram_strategy)
def test_machinelibrary_nodeprogram_programName_setter(instance):
    original = instance.programName
    instance.programName = original
    assert instance.programName == original



@given(instance=MachineLibrary_NodeProgram_strategy)
def test_machinelibrary_nodeprogram_programLenPerParam_setter(instance):
    original = instance.programLenPerParam
    instance.programLenPerParam = original
    assert instance.programLenPerParam == original

@given(instance=MachineLibrary_Command_strategy)
@settings(max_examples=50)
def test_machinelibrary_command_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Command)



@given(instance=MachineLibrary_Command_strategy)
def test_machinelibrary_command_commandNo_setter(instance):
    original = instance.commandNo
    instance.commandNo = original
    assert instance.commandNo == original



@given(instance=MachineLibrary_Command_strategy)
def test_machinelibrary_command_commandName_setter(instance):
    original = instance.commandName
    instance.commandName = original
    assert instance.commandName == original



@given(instance=MachineLibrary_Command_strategy)
def test_machinelibrary_command_commandProgParameter_setter(instance):
    original = instance.commandProgParameter
    instance.commandProgParameter = original
    assert instance.commandProgParameter == original

@given(instance=MachineLibrary_UnitProgParameters_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitprogparameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitProgParameters)



@given(instance=MachineLibrary_UnitProgParameters_strategy)
def test_machinelibrary_unitprogparameters_parameterNo_setter(instance):
    original = instance.parameterNo
    instance.parameterNo = original
    assert instance.parameterNo == original



@given(instance=MachineLibrary_UnitProgParameters_strategy)
def test_machinelibrary_unitprogparameters_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=MachineLibrary_UnitProgram_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitprogram_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitProgram)



@given(instance=MachineLibrary_UnitProgram_strategy)
def test_machinelibrary_unitprogram_unitProgName_setter(instance):
    original = instance.unitProgName
    instance.unitProgName = original
    assert instance.unitProgName == original

@given(instance=MachineLibrary_Position_strategy)
@settings(max_examples=50)
def test_machinelibrary_position_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Position)



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posExit_setter(instance):
    original = instance.posExit
    instance.posExit = original
    assert instance.posExit == original



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posIndex_setter(instance):
    original = instance.posIndex
    instance.posIndex = original
    assert instance.posIndex == original



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posName_setter(instance):
    original = instance.posName
    instance.posName = original
    assert instance.posName == original



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posRemark_setter(instance):
    original = instance.posRemark
    instance.posRemark = original
    assert instance.posRemark == original



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posNo_setter(instance):
    original = instance.posNo
    instance.posNo = original
    assert instance.posNo == original



@given(instance=MachineLibrary_Position_strategy)
def test_machinelibrary_position_posWarningOnDelete_setter(instance):
    original = instance.posWarningOnDelete
    instance.posWarningOnDelete = original
    assert instance.posWarningOnDelete == original

@given(instance=MachineLibrary_Button_strategy)
@settings(max_examples=50)
def test_machinelibrary_button_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Button)



@given(instance=MachineLibrary_Button_strategy)
def test_machinelibrary_button_buttonText_setter(instance):
    original = instance.buttonText
    instance.buttonText = original
    assert instance.buttonText == original



@given(instance=MachineLibrary_Button_strategy)
def test_machinelibrary_button_commandNo_setter(instance):
    original = instance.commandNo
    instance.commandNo = original
    assert instance.commandNo == original



@given(instance=MachineLibrary_Button_strategy)
def test_machinelibrary_button_buttonNo_setter(instance):
    original = instance.buttonNo
    instance.buttonNo = original
    assert instance.buttonNo == original

@given(instance=MachineLibrary_CheckAddSID_Values_PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary_checkaddsid_values_pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckAddSID_Values_PM2PM)



@given(instance=MachineLibrary_CheckAddSID_Values_PM2PM_strategy)
def test_machinelibrary_checkaddsid_values_pm2pm_optionNo_setter(instance):
    original = instance.optionNo
    instance.optionNo = original
    assert instance.optionNo == original



@given(instance=MachineLibrary_CheckAddSID_Values_PM2PM_strategy)
def test_machinelibrary_checkaddsid_values_pm2pm_optonValue_setter(instance):
    original = instance.optonValue
    instance.optonValue = original
    assert instance.optonValue == original

@given(instance=MachineLibrary_SepByComma_ID_Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary_sepbycomma_id_scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary_SepByComma_ID_Scanner)



@given(instance=MachineLibrary_SepByComma_ID_Scanner_strategy)
def test_machinelibrary_sepbycomma_id_scanner_idPrevValue_setter(instance):
    original = instance.idPrevValue
    instance.idPrevValue = original
    assert instance.idPrevValue == original



@given(instance=MachineLibrary_SepByComma_ID_Scanner_strategy)
def test_machinelibrary_sepbycomma_id_scanner_idCharValue_setter(instance):
    original = instance.idCharValue
    instance.idCharValue = original
    assert instance.idCharValue == original



@given(instance=MachineLibrary_SepByComma_ID_Scanner_strategy)
def test_machinelibrary_sepbycomma_id_scanner_idSeq_X_setter(instance):
    original = instance.idSeq_X
    instance.idSeq_X = original
    assert instance.idSeq_X == original



@given(instance=MachineLibrary_SepByComma_ID_Scanner_strategy)
def test_machinelibrary_sepbycomma_id_scanner_idValue_setter(instance):
    original = instance.idValue
    instance.idValue = original
    assert instance.idValue == original

@given(instance=MachineLibrary_SepByComma_Field_Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary_sepbycomma_field_scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary_SepByComma_Field_Scanner)



@given(instance=MachineLibrary_SepByComma_Field_Scanner_strategy)
def test_machinelibrary_sepbycomma_field_scanner_fieldNo_setter(instance):
    original = instance.fieldNo
    instance.fieldNo = original
    assert instance.fieldNo == original



@given(instance=MachineLibrary_SepByComma_Field_Scanner_strategy)
def test_machinelibrary_sepbycomma_field_scanner_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=MachineLibrary_StatusBit_strategy)
@settings(max_examples=50)
def test_machinelibrary_statusbit_instantiation(instance):
    assert isinstance(instance, MachineLibrary_StatusBit)



@given(instance=MachineLibrary_StatusBit_strategy)
def test_machinelibrary_statusbit_bitName_setter(instance):
    original = instance.bitName
    instance.bitName = original
    assert instance.bitName == original



@given(instance=MachineLibrary_StatusBit_strategy)
def test_machinelibrary_statusbit_bitNo_setter(instance):
    original = instance.bitNo
    instance.bitNo = original
    assert instance.bitNo == original

@given(instance=MachineLibrary_HistoryConfig_AccuPyc_strategy)
@settings(max_examples=50)
def test_machinelibrary_historyconfig_accupyc_instantiation(instance):
    assert isinstance(instance, MachineLibrary_HistoryConfig_AccuPyc)



@given(instance=MachineLibrary_HistoryConfig_AccuPyc_strategy)
def test_machinelibrary_historyconfig_accupyc_sampleCupWeight_setter(instance):
    original = instance.sampleCupWeight
    instance.sampleCupWeight = original
    assert instance.sampleCupWeight == original



@given(instance=MachineLibrary_HistoryConfig_AccuPyc_strategy)
def test_machinelibrary_historyconfig_accupyc_currentSample_setter(instance):
    original = instance.currentSample
    instance.currentSample = original
    assert instance.currentSample == original



@given(instance=MachineLibrary_HistoryConfig_AccuPyc_strategy)
def test_machinelibrary_historyconfig_accupyc_currentSampleID_setter(instance):
    original = instance.currentSampleID
    instance.currentSampleID = original
    assert instance.currentSampleID == original

@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_checksampleconfig_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckSampleConfig_SuperQXRF)



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_anaProg_setter(instance):
    original = instance.anaProg
    instance.anaProg = original
    assert instance.anaProg == original



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_program_setter(instance):
    original = instance.program
    instance.program = original
    assert instance.program == original



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_sampleID_setter(instance):
    original = instance.sampleID
    instance.sampleID = original
    assert instance.sampleID == original



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original



@given(instance=MachineLibrary_CheckSampleConfig_SuperQXRF_strategy)
def test_machinelibrary_checksampleconfig_superqxrf_samples_setter(instance):
    original = instance.samples
    instance.samples = original
    assert instance.samples == original

@given(instance=MachineLibrary_InsertRemove_Keywords_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_insertremove_keywords_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_InsertRemove_Keywords_Host)



@given(instance=MachineLibrary_InsertRemove_Keywords_Host_strategy)
def test_machinelibrary_insertremove_keywords_host_keywordKey_setter(instance):
    original = instance.keywordKey
    instance.keywordKey = original
    assert instance.keywordKey == original



@given(instance=MachineLibrary_InsertRemove_Keywords_Host_strategy)
def test_machinelibrary_insertremove_keywords_host_keywordValue_setter(instance):
    original = instance.keywordValue
    instance.keywordValue = original
    assert instance.keywordValue == original

@given(instance=MachineLibrary_InsertRemove_Types_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_insertremove_types_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_InsertRemove_Types_Host)



@given(instance=MachineLibrary_InsertRemove_Types_Host_strategy)
def test_machinelibrary_insertremove_types_host_typeNo_setter(instance):
    original = instance.typeNo
    instance.typeNo = original
    assert instance.typeNo == original



@given(instance=MachineLibrary_InsertRemove_Types_Host_strategy)
def test_machinelibrary_insertremove_types_host_typeValue_setter(instance):
    original = instance.typeValue
    instance.typeValue = original
    assert instance.typeValue == original

@given(instance=MachineLibrary_InsertRemove_Entry_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_insertremove_entry_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_InsertRemove_Entry_Host)



@given(instance=MachineLibrary_InsertRemove_Entry_Host_strategy)
def test_machinelibrary_insertremove_entry_host_entryName_setter(instance):
    original = instance.entryName
    instance.entryName = original
    assert instance.entryName == original



@given(instance=MachineLibrary_InsertRemove_Entry_Host_strategy)
def test_machinelibrary_insertremove_entry_host_entryNo_setter(instance):
    original = instance.entryNo
    instance.entryNo = original
    assert instance.entryNo == original

@given(instance=MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_checksampleruntimeparams_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckSampleRunTimeParams_SuperQXRF)



@given(instance=MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_strategy)
def test_machinelibrary_checksampleruntimeparams_superqxrf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_strategy)
def test_machinelibrary_checksampleruntimeparams_superqxrf_sampleType_setter(instance):
    original = instance.sampleType
    instance.sampleType = original
    assert instance.sampleType == original

@given(instance=MachineLibrary_OES_XRF_Condition_strategy)
@settings(max_examples=50)
def test_machinelibrary_oes_xrf_condition_instantiation(instance):
    assert isinstance(instance, MachineLibrary_OES_XRF_Condition)



@given(instance=MachineLibrary_OES_XRF_Condition_strategy)
def test_machinelibrary_oes_xrf_condition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=MachineLibrary_OES_XRF_Condition_strategy)
def test_machinelibrary_oes_xrf_condition_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original



@given(instance=MachineLibrary_OES_XRF_Condition_strategy)
def test_machinelibrary_oes_xrf_condition_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original



@given(instance=MachineLibrary_OES_XRF_Condition_strategy)
def test_machinelibrary_oes_xrf_condition_paraName_setter(instance):
    original = instance.paraName
    instance.paraName = original
    assert instance.paraName == original

@given(instance=MachineLibrary_InsertRemove_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_insertremove_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_InsertRemove_Host)



@given(instance=MachineLibrary_InsertRemove_Host_strategy)
def test_machinelibrary_insertremove_host_report_All_setter(instance):
    original = instance.report_All
    instance.report_All = original
    assert instance.report_All == original

@given(instance=MachineLibrary_Moved_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_moved_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Moved_Host)



@given(instance=MachineLibrary_Moved_Host_strategy)
def test_machinelibrary_moved_host_pos0_setter(instance):
    original = instance.pos0
    instance.pos0 = original
    assert instance.pos0 == original



@given(instance=MachineLibrary_Moved_Host_strategy)
def test_machinelibrary_moved_host_report_ALL_setter(instance):
    original = instance.report_ALL
    instance.report_ALL = original
    assert instance.report_ALL == original



@given(instance=MachineLibrary_Moved_Host_strategy)
def test_machinelibrary_moved_host_writePositionNameInFile_setter(instance):
    original = instance.writePositionNameInFile
    instance.writePositionNameInFile = original
    assert instance.writePositionNameInFile == original



@given(instance=MachineLibrary_Moved_Host_strategy)
def test_machinelibrary_moved_host_type0_setter(instance):
    original = instance.type0
    instance.type0 = original
    assert instance.type0 == original

@given(instance=MachineLibrary_WS_Update_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_ws_update_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_WS_Update_Host)



@given(instance=MachineLibrary_WS_Update_Host_strategy)
def test_machinelibrary_ws_update_host_AllowUnit0_setter(instance):
    original = instance.AllowUnit0
    instance.AllowUnit0 = original
    assert instance.AllowUnit0 == original



@given(instance=MachineLibrary_WS_Update_Host_strategy)
def test_machinelibrary_ws_update_host_checkUnit_setter(instance):
    original = instance.checkUnit
    instance.checkUnit = original
    assert instance.checkUnit == original

@given(instance=MachineLibrary_Report_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_report_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Report_Host)



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_note1_setter(instance):
    original = instance.note1
    instance.note1 = original
    assert instance.note1 == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_sendErrorWarningsMsgOnly_setter(instance):
    original = instance.sendErrorWarningsMsgOnly
    instance.sendErrorWarningsMsgOnly = original
    assert instance.sendErrorWarningsMsgOnly == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_maxType_setter(instance):
    original = instance.maxType
    instance.maxType = original
    assert instance.maxType == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_stateChanged_setter(instance):
    original = instance.stateChanged
    instance.stateChanged = original
    assert instance.stateChanged == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_sampleInsert_setter(instance):
    original = instance.sampleInsert
    instance.sampleInsert = original
    assert instance.sampleInsert == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_timeStamp_setter(instance):
    original = instance.timeStamp
    instance.timeStamp = original
    assert instance.timeStamp == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_sampleRemoved_setter(instance):
    original = instance.sampleRemoved
    instance.sampleRemoved = original
    assert instance.sampleRemoved == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_rawData_setter(instance):
    original = instance.rawData
    instance.rawData = original
    assert instance.rawData == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_sendLifeMessages_setter(instance):
    original = instance.sendLifeMessages
    instance.sendLifeMessages = original
    assert instance.sendLifeMessages == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_sampleMoved_setter(instance):
    original = instance.sampleMoved
    instance.sampleMoved = original
    assert instance.sampleMoved == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_internal_setter(instance):
    original = instance.internal
    instance.internal = original
    assert instance.internal == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_minType_setter(instance):
    original = instance.minType
    instance.minType = original
    assert instance.minType == original



@given(instance=MachineLibrary_Report_Host_strategy)
def test_machinelibrary_report_host_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=MachineLibrary_Settings_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_settings_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Settings_ARL_XRF_OES)



@given(instance=MachineLibrary_Settings_ARL_XRF_OES_strategy)
def test_machinelibrary_settings_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_DisableSCT_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_disablesct_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_DisableSCT_ARL_XRF_OES)



@given(instance=MachineLibrary_DisableSCT_ARL_XRF_OES_strategy)
def test_machinelibrary_disablesct_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_exeaskprepunit_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES)



@given(instance=MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES_strategy)
def test_machinelibrary_exeaskprepunit_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_checkaskprepunit_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES)



@given(instance=MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES_strategy)
def test_machinelibrary_checkaskprepunit_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_ExePrepUnit_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_exeprepunit_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ExePrepUnit_ARL_XRF_OES)



@given(instance=MachineLibrary_ExePrepUnit_ARL_XRF_OES_strategy)
def test_machinelibrary_exeprepunit_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_checkreqprepunit_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES)



@given(instance=MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES_strategy)
def test_machinelibrary_checkreqprepunit_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_ExecuteFiling_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_executefiling_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ExecuteFiling_ARL_XRF_OES)



@given(instance=MachineLibrary_ExecuteFiling_ARL_XRF_OES_strategy)
def test_machinelibrary_executefiling_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_CheckFilling_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_checkfilling_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckFilling_ARL_XRF_OES)



@given(instance=MachineLibrary_CheckFilling_ARL_XRF_OES_strategy)
def test_machinelibrary_checkfilling_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_CheckSample_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_checksample_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckSample_SuperQXRF)

@given(instance=MachineLibrary_CheckSampleRunTime_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_checksampleruntime_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckSampleRunTime_SuperQXRF)

@given(instance=MachineLibrary_Communication_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_communication_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Communication_SuperQXRF)



@given(instance=MachineLibrary_Communication_SuperQXRF_strategy)
def test_machinelibrary_communication_superqxrf_enq_ACK_Protocol_setter(instance):
    original = instance.enq_ACK_Protocol
    instance.enq_ACK_Protocol = original
    assert instance.enq_ACK_Protocol == original

@given(instance=MachineLibrary_ControlSamples_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_controlsamples_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ControlSamples_SuperQXRF)



@given(instance=MachineLibrary_ControlSamples_SuperQXRF_strategy)
def test_machinelibrary_controlsamples_superqxrf_outOfControl_setter(instance):
    original = instance.outOfControl
    instance.outOfControl = original
    assert instance.outOfControl == original

@given(instance=MachineLibrary_File_Sample_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_file_sample_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_File_Sample_ARL_XRF_OES)



@given(instance=MachineLibrary_File_Sample_ARL_XRF_OES_strategy)
def test_machinelibrary_file_sample_arl_xrf_oes_noSuccess_setter(instance):
    original = instance.noSuccess
    instance.noSuccess = original
    assert instance.noSuccess == original

@given(instance=MachineLibrary_PS_Process_Finished_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_ps_process_finished_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_PS_Process_Finished_ARL_XRF_OES)



@given(instance=MachineLibrary_PS_Process_Finished_ARL_XRF_OES_strategy)
def test_machinelibrary_ps_process_finished_arl_xrf_oes_noSuccess_setter(instance):
    original = instance.noSuccess
    instance.noSuccess = original
    assert instance.noSuccess == original

@given(instance=MachineLibrary_GeneralSetting_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_generalsetting_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_GeneralSetting_ARL_XRF_OES)



@given(instance=MachineLibrary_GeneralSetting_ARL_XRF_OES_strategy)
def test_machinelibrary_generalsetting_arl_xrf_oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_CheckAddSID_PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary_checkaddsid_pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CheckAddSID_PM2PM)

@given(instance=MachineLibrary_SepByComma_Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary_sepbycomma_scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary_SepByComma_Scanner)



@given(instance=MachineLibrary_SepByComma_Scanner_strategy)
def test_machinelibrary_sepbycomma_scanner_preDefWS_setter(instance):
    original = instance.preDefWS
    instance.preDefWS = original
    assert instance.preDefWS == original



@given(instance=MachineLibrary_SepByComma_Scanner_strategy)
def test_machinelibrary_sepbycomma_scanner_activ_setter(instance):
    original = instance.activ
    instance.activ = original
    assert instance.activ == original

@given(instance=MachineLibrary_History_AccuPycMeter_strategy)
@settings(max_examples=50)
def test_machinelibrary_history_accupycmeter_instantiation(instance):
    assert isinstance(instance, MachineLibrary_History_AccuPycMeter)

@given(instance=MachineLibrary_UnitConfig_Host_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitconfig_host_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitConfig_Host)

@given(instance=MachineLibrary_UnitConfig_ARL_XRF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitconfig_arl_xrf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitConfig_ARL_XRF_OES)

@given(instance=MachineLibrary_UnitConfig_SuperQ_XRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitconfig_superq_xrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitConfig_SuperQ_XRF)

@given(instance=MachineLibrary_UnitConfig_OBLF_OES_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitconfig_oblf_oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitConfig_OBLF_OES)

@given(instance=MachineLibrary_UnitConfig_Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitconfig_terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitConfig_Terminal)

@given(instance=MachineLibrary_GeneralParameter_SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_generalparameter_superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_GeneralParameter_SuperQXRF)



@given(instance=MachineLibrary_GeneralParameter_SuperQXRF_strategy)
def test_machinelibrary_generalparameter_superqxrf_startList_setter(instance):
    original = instance.startList
    instance.startList = original
    assert instance.startList == original



@given(instance=MachineLibrary_GeneralParameter_SuperQXRF_strategy)
def test_machinelibrary_generalparameter_superqxrf_listName_setter(instance):
    original = instance.listName
    instance.listName = original
    assert instance.listName == original



@given(instance=MachineLibrary_GeneralParameter_SuperQXRF_strategy)
def test_machinelibrary_generalparameter_superqxrf_switchRemote_setter(instance):
    original = instance.switchRemote
    instance.switchRemote = original
    assert instance.switchRemote == original

@given(instance=MachineLibrary_ErrorMessage_OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary_errormessage_oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_ErrorMessage_OBLFOES)



@given(instance=MachineLibrary_ErrorMessage_OBLFOES_strategy)
def test_machinelibrary_errormessage_oblfoes_errorMessage_setter(instance):
    original = instance.errorMessage
    instance.errorMessage = original
    assert instance.errorMessage == original

@given(instance=MachineLibrary_RecalRequest_OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary_recalrequest_oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_RecalRequest_OBLFOES)



@given(instance=MachineLibrary_RecalRequest_OBLFOES_strategy)
def test_machinelibrary_recalrequest_oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_TestRequest_OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary_testrequest_oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_TestRequest_OBLFOES)



@given(instance=MachineLibrary_TestRequest_OBLFOES_strategy)
def test_machinelibrary_testrequest_oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_OutputRequest_OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary_outputrequest_oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary_OutputRequest_OBLFOES)



@given(instance=MachineLibrary_OutputRequest_OBLFOES_strategy)
def test_machinelibrary_outputrequest_oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary_Translate_Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary_translate_terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Translate_Terminal)



@given(instance=MachineLibrary_Translate_Terminal_strategy)
def test_machinelibrary_translate_terminal_man_Busy_setter(instance):
    original = instance.man_Busy
    instance.man_Busy = original
    assert instance.man_Busy == original



@given(instance=MachineLibrary_Translate_Terminal_strategy)
def test_machinelibrary_translate_terminal_man_Ready_setter(instance):
    original = instance.man_Ready
    instance.man_Ready = original
    assert instance.man_Ready == original



@given(instance=MachineLibrary_Translate_Terminal_strategy)
def test_machinelibrary_translate_terminal_auto_Busy_setter(instance):
    original = instance.auto_Busy
    instance.auto_Busy = original
    assert instance.auto_Busy == original



@given(instance=MachineLibrary_Translate_Terminal_strategy)
def test_machinelibrary_translate_terminal_auto_Ready_setter(instance):
    original = instance.auto_Ready
    instance.auto_Ready = original
    assert instance.auto_Ready == original

@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_Scanner)



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_addString_setter(instance):
    original = instance.addString
    instance.addString = original
    assert instance.addString == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_preString_setter(instance):
    original = instance.preString
    instance.preString = original
    assert instance.preString == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_forcedSampleType_setter(instance):
    original = instance.forcedSampleType
    instance.forcedSampleType = original
    assert instance.forcedSampleType == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_registerSample_setter(instance):
    original = instance.registerSample
    instance.registerSample = original
    assert instance.registerSample == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=MachineLibrary_UnitGeneral_Scanner_strategy)
def test_machinelibrary_unitgeneral_scanner_fillWith_setter(instance):
    original = instance.fillWith
    instance.fillWith = original
    assert instance.fillWith == original

@given(instance=MachineLibrary_UnitGeneral_RigakuXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_rigakuxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_RigakuXRF)



@given(instance=MachineLibrary_UnitGeneral_RigakuXRF_strategy)
def test_machinelibrary_unitgeneral_rigakuxrf_lastPosInInstrument_setter(instance):
    original = instance.lastPosInInstrument
    instance.lastPosInInstrument = original
    assert instance.lastPosInInstrument == original



@given(instance=MachineLibrary_UnitGeneral_RigakuXRF_strategy)
def test_machinelibrary_unitgeneral_rigakuxrf_lastPosAnalyHAG_SIg_setter(instance):
    original = instance.lastPosAnalyHAG_SIg
    instance.lastPosAnalyHAG_SIg = original
    assert instance.lastPosAnalyHAG_SIg == original



@given(instance=MachineLibrary_UnitGeneral_RigakuXRF_strategy)
def test_machinelibrary_unitgeneral_rigakuxrf_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original



@given(instance=MachineLibrary_UnitGeneral_RigakuXRF_strategy)
def test_machinelibrary_unitgeneral_rigakuxrf_lastPoHAG_SIInstrument_setter(instance):
    original = instance.lastPoHAG_SIInstrument
    instance.lastPoHAG_SIInstrument = original
    assert instance.lastPoHAG_SIInstrument == original

@given(instance=MachineLibrary_UnitGeneral_SuperQ_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_superq_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_SuperQ)



@given(instance=MachineLibrary_UnitGeneral_SuperQ_strategy)
def test_machinelibrary_unitgeneral_superq_lastPosAnalysing_setter(instance):
    original = instance.lastPosAnalysing
    instance.lastPosAnalysing = original
    assert instance.lastPosAnalysing == original



@given(instance=MachineLibrary_UnitGeneral_SuperQ_strategy)
def test_machinelibrary_unitgeneral_superq_lastPosInInstrument_setter(instance):
    original = instance.lastPosInInstrument
    instance.lastPosInInstrument = original
    assert instance.lastPosInInstrument == original

@given(instance=MachineLibrary_UnitGeneral_AccPyc_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_accpyc_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_AccPyc)



@given(instance=MachineLibrary_UnitGeneral_AccPyc_strategy)
def test_machinelibrary_unitgeneral_accpyc_cupWeight_setter(instance):
    original = instance.cupWeight
    instance.cupWeight = original
    assert instance.cupWeight == original



@given(instance=MachineLibrary_UnitGeneral_AccPyc_strategy)
def test_machinelibrary_unitgeneral_accpyc_minSampleWeight_setter(instance):
    original = instance.minSampleWeight
    instance.minSampleWeight = original
    assert instance.minSampleWeight == original

@given(instance=MachineLibrary_UnitGeneral_PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_PM2PM)



@given(instance=MachineLibrary_UnitGeneral_PM2PM_strategy)
def test_machinelibrary_unitgeneral_pm2pm_processFeedBack_setter(instance):
    original = instance.processFeedBack
    instance.processFeedBack = original
    assert instance.processFeedBack == original



@given(instance=MachineLibrary_UnitGeneral_PM2PM_strategy)
def test_machinelibrary_unitgeneral_pm2pm_sid_Mask_setter(instance):
    original = instance.sid_Mask
    instance.sid_Mask = original
    assert instance.sid_Mask == original

@given(instance=MachineLibrary_UnitGeneral_Remote_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_remote_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_Remote)



@given(instance=MachineLibrary_UnitGeneral_Remote_strategy)
def test_machinelibrary_unitgeneral_remote_editWSDB_setter(instance):
    original = instance.editWSDB
    instance.editWSDB = original
    assert instance.editWSDB == original



@given(instance=MachineLibrary_UnitGeneral_Remote_strategy)
def test_machinelibrary_unitgeneral_remote_handshakeT_setter(instance):
    original = instance.handshakeT
    instance.handshakeT = original
    assert instance.handshakeT == original



@given(instance=MachineLibrary_UnitGeneral_Remote_strategy)
def test_machinelibrary_unitgeneral_remote_handshakeQ_setter(instance):
    original = instance.handshakeQ
    instance.handshakeQ = original
    assert instance.handshakeQ == original



@given(instance=MachineLibrary_UnitGeneral_Remote_strategy)
def test_machinelibrary_unitgeneral_remote_handshakeA_setter(instance):
    original = instance.handshakeA
    instance.handshakeA = original
    assert instance.handshakeA == original

@given(instance=MachineLibrary_UnitGeneral_HostPC_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_hostpc_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_HostPC)



@given(instance=MachineLibrary_UnitGeneral_HostPC_strategy)
def test_machinelibrary_unitgeneral_hostpc_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=MachineLibrary_UnitGeneral_HostPC_strategy)
def test_machinelibrary_unitgeneral_hostpc_replyOnLink_setter(instance):
    original = instance.replyOnLink
    instance.replyOnLink = original
    assert instance.replyOnLink == original



@given(instance=MachineLibrary_UnitGeneral_HostPC_strategy)
def test_machinelibrary_unitgeneral_hostpc_writeDumyIfNoDataExist_setter(instance):
    original = instance.writeDumyIfNoDataExist
    instance.writeDumyIfNoDataExist = original
    assert instance.writeDumyIfNoDataExist == original



@given(instance=MachineLibrary_UnitGeneral_HostPC_strategy)
def test_machinelibrary_unitgeneral_hostpc_maxIndex_setter(instance):
    original = instance.maxIndex
    instance.maxIndex = original
    assert instance.maxIndex == original

@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral_Terminal)



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_station1_setter(instance):
    original = instance.station1
    instance.station1 = original
    assert instance.station1 == original



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_station5_setter(instance):
    original = instance.station5
    instance.station5 = original
    assert instance.station5 == original



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_station2_setter(instance):
    original = instance.station2
    instance.station2 = original
    assert instance.station2 == original



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_thisStation_setter(instance):
    original = instance.thisStation
    instance.thisStation = original
    assert instance.thisStation == original



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_station4_setter(instance):
    original = instance.station4
    instance.station4 = original
    assert instance.station4 == original



@given(instance=MachineLibrary_UnitGeneral_Terminal_strategy)
def test_machinelibrary_unitgeneral_terminal_station3_setter(instance):
    original = instance.station3
    instance.station3 = original
    assert instance.station3 == original

@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
@settings(max_examples=50)
def test_machinelibrary_plctopmmatrix_instantiation(instance):
    assert isinstance(instance, MachineLibrary_PLCtoPmMatrix)



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit0_setter(instance):
    original = instance.plcpmmatrixBit0
    instance.plcpmmatrixBit0 = original
    assert instance.plcpmmatrixBit0 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit14_setter(instance):
    original = instance.plcpmmatrixBit14
    instance.plcpmmatrixBit14 = original
    assert instance.plcpmmatrixBit14 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit7_setter(instance):
    original = instance.plcpmmatrixBit7
    instance.plcpmmatrixBit7 = original
    assert instance.plcpmmatrixBit7 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit12_setter(instance):
    original = instance.plcpmmatrixBit12
    instance.plcpmmatrixBit12 = original
    assert instance.plcpmmatrixBit12 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit4_setter(instance):
    original = instance.plcpmmatrixBit4
    instance.plcpmmatrixBit4 = original
    assert instance.plcpmmatrixBit4 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit1_setter(instance):
    original = instance.plcpmmatrixBit1
    instance.plcpmmatrixBit1 = original
    assert instance.plcpmmatrixBit1 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit5_setter(instance):
    original = instance.plcpmmatrixBit5
    instance.plcpmmatrixBit5 = original
    assert instance.plcpmmatrixBit5 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit10_setter(instance):
    original = instance.plcpmmatrixBit10
    instance.plcpmmatrixBit10 = original
    assert instance.plcpmmatrixBit10 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit6_setter(instance):
    original = instance.plcpmmatrixBit6
    instance.plcpmmatrixBit6 = original
    assert instance.plcpmmatrixBit6 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit13_setter(instance):
    original = instance.plcpmmatrixBit13
    instance.plcpmmatrixBit13 = original
    assert instance.plcpmmatrixBit13 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit15_setter(instance):
    original = instance.plcpmmatrixBit15
    instance.plcpmmatrixBit15 = original
    assert instance.plcpmmatrixBit15 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit8_setter(instance):
    original = instance.plcpmmatrixBit8
    instance.plcpmmatrixBit8 = original
    assert instance.plcpmmatrixBit8 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit9_setter(instance):
    original = instance.plcpmmatrixBit9
    instance.plcpmmatrixBit9 = original
    assert instance.plcpmmatrixBit9 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit11_setter(instance):
    original = instance.plcpmmatrixBit11
    instance.plcpmmatrixBit11 = original
    assert instance.plcpmmatrixBit11 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit3_setter(instance):
    original = instance.plcpmmatrixBit3
    instance.plcpmmatrixBit3 = original
    assert instance.plcpmmatrixBit3 == original



@given(instance=MachineLibrary_PLCtoPmMatrix_strategy)
def test_machinelibrary_plctopmmatrix_plcpmmatrixBit2_setter(instance):
    original = instance.plcpmmatrixBit2
    instance.plcpmmatrixBit2 = original
    assert instance.plcpmmatrixBit2 == original

@given(instance=MachineLibrary_StausBits_strategy)
@settings(max_examples=50)
def test_machinelibrary_stausbits_instantiation(instance):
    assert isinstance(instance, MachineLibrary_StausBits)

@given(instance=MachineLibrary_Positions_strategy)
@settings(max_examples=50)
def test_machinelibrary_positions_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Positions)

@given(instance=MachineLibrary_WinCCAddTag_strategy)
@settings(max_examples=50)
def test_machinelibrary_winccaddtag_instantiation(instance):
    assert isinstance(instance, MachineLibrary_WinCCAddTag)



@given(instance=MachineLibrary_WinCCAddTag_strategy)
def test_machinelibrary_winccaddtag_winCCTag_setter(instance):
    original = instance.winCCTag
    instance.winCCTag = original
    assert instance.winCCTag == original

@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneralparameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneralParameters)



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_defaultValue_1_setter(instance):
    original = instance.defaultValue_1
    instance.defaultValue_1 = original
    assert instance.defaultValue_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_UseWith_1_setter(instance):
    original = instance.UseWith_1
    instance.UseWith_1 = original
    assert instance.UseWith_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_visibleType_1_setter(instance):
    original = instance.visibleType_1
    instance.visibleType_1 = original
    assert instance.visibleType_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_comment_1_setter(instance):
    original = instance.comment_1
    instance.comment_1 = original
    assert instance.comment_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_unit_1_setter(instance):
    original = instance.unit_1
    instance.unit_1 = original
    assert instance.unit_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_maxValue_1_setter(instance):
    original = instance.maxValue_1
    instance.maxValue_1 = original
    assert instance.maxValue_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_minValue_1_setter(instance):
    original = instance.minValue_1
    instance.minValue_1 = original
    assert instance.minValue_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_canBeChange_1_setter(instance):
    original = instance.canBeChange_1
    instance.canBeChange_1 = original
    assert instance.canBeChange_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_KeyWord_1_setter(instance):
    original = instance.KeyWord_1
    instance.KeyWord_1 = original
    assert instance.KeyWord_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_paraName_1_setter(instance):
    original = instance.paraName_1
    instance.paraName_1 = original
    assert instance.paraName_1 == original



@given(instance=MachineLibrary_UnitGeneralParameters_strategy)
def test_machinelibrary_unitgeneralparameters_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original

@given(instance=MachineLibrary_UnitSpecialConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitspecialconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitSpecialConfiguration)

@given(instance=MachineLibrary_UnitGeneralSpecial_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneralspecial_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneralSpecial)

@given(instance=MachineLibrary_UnitGeneral_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitgeneral_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitGeneral)

@given(instance=MachineLibrary_Buttons_strategy)
@settings(max_examples=50)
def test_machinelibrary_buttons_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Buttons)

@given(instance=MachineLibrary_UnitPrograms_strategy)
@settings(max_examples=50)
def test_machinelibrary_unitprograms_instantiation(instance):
    assert isinstance(instance, MachineLibrary_UnitPrograms)

@given(instance=MachineLibrary_NodeGeneral_RigakuXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_rigakuxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_RigakuXRF)



@given(instance=MachineLibrary_NodeGeneral_RigakuXRF_strategy)
def test_machinelibrary_nodegeneral_rigakuxrf_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original



@given(instance=MachineLibrary_NodeGeneral_RigakuXRF_strategy)
def test_machinelibrary_nodegeneral_rigakuxrf_timerToSendStatus_setter(instance):
    original = instance.timerToSendStatus
    instance.timerToSendStatus = original
    assert instance.timerToSendStatus == original



@given(instance=MachineLibrary_NodeGeneral_RigakuXRF_strategy)
def test_machinelibrary_nodegeneral_rigakuxrf_bDoNotshiftAtExit_setter(instance):
    original = instance.bDoNotshiftAtExit
    instance.bDoNotshiftAtExit = original
    assert instance.bDoNotshiftAtExit == original



@given(instance=MachineLibrary_NodeGeneral_RigakuXRF_strategy)
def test_machinelibrary_nodegeneral_rigakuxrf_timeoutResponce_setter(instance):
    original = instance.timeoutResponce
    instance.timeoutResponce = original
    assert instance.timeoutResponce == original

@given(instance=MachineLibrary_NodeGeneral_AccuPycMeter_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_accupycmeter_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_AccuPycMeter)



@given(instance=MachineLibrary_NodeGeneral_AccuPycMeter_strategy)
def test_machinelibrary_nodegeneral_accupycmeter_runTimout_setter(instance):
    original = instance.runTimout
    instance.runTimout = original
    assert instance.runTimout == original



@given(instance=MachineLibrary_NodeGeneral_AccuPycMeter_strategy)
def test_machinelibrary_nodegeneral_accupycmeter_expectSampleWeight_setter(instance):
    original = instance.expectSampleWeight
    instance.expectSampleWeight = original
    assert instance.expectSampleWeight == original



@given(instance=MachineLibrary_NodeGeneral_AccuPycMeter_strategy)
def test_machinelibrary_nodegeneral_accupycmeter_polling_setter(instance):
    original = instance.polling
    instance.polling = original
    assert instance.polling == original



@given(instance=MachineLibrary_NodeGeneral_AccuPycMeter_strategy)
def test_machinelibrary_nodegeneral_accupycmeter_sendSampleWeight_setter(instance):
    original = instance.sendSampleWeight
    instance.sendSampleWeight = original
    assert instance.sendSampleWeight == original

@given(instance=MachineLibrary_NodeGeneral_WinCC2WinCC_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_wincc2wincc_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_WinCC2WinCC)



@given(instance=MachineLibrary_NodeGeneral_WinCC2WinCC_strategy)
def test_machinelibrary_nodegeneral_wincc2wincc_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=MachineLibrary_NodeGeneral_RemotePM_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_remotepm_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_RemotePM)



@given(instance=MachineLibrary_NodeGeneral_RemotePM_strategy)
def test_machinelibrary_nodegeneral_remotepm_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original



@given(instance=MachineLibrary_NodeGeneral_RemotePM_strategy)
def test_machinelibrary_nodegeneral_remotepm_timeServer_setter(instance):
    original = instance.timeServer
    instance.timeServer = original
    assert instance.timeServer == original

@given(instance=MachineLibrary_NodeGeneral_PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_PM2PM)



@given(instance=MachineLibrary_NodeGeneral_PM2PM_strategy)
def test_machinelibrary_nodegeneral_pm2pm_timeServer_setter(instance):
    original = instance.timeServer
    instance.timeServer = original
    assert instance.timeServer == original



@given(instance=MachineLibrary_NodeGeneral_PM2PM_strategy)
def test_machinelibrary_nodegeneral_pm2pm_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral_Terminal)



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_3_setter(instance):
    original = instance.name_3
    instance.name_3 = original
    assert instance.name_3 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_signalCarrierPresent_setter(instance):
    original = instance.signalCarrierPresent
    instance.signalCarrierPresent = original
    assert instance.signalCarrierPresent == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_steelCarrier_setter(instance):
    original = instance.steelCarrier
    instance.steelCarrier = original
    assert instance.steelCarrier == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_keyBoardSignalCarrierPresent_setter(instance):
    original = instance.keyBoardSignalCarrierPresent
    instance.keyBoardSignalCarrierPresent = original
    assert instance.keyBoardSignalCarrierPresent == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_maxScreens_setter(instance):
    original = instance.maxScreens
    instance.maxScreens = original
    assert instance.maxScreens == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_5_setter(instance):
    original = instance.name_5
    instance.name_5 = original
    assert instance.name_5 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_6_setter(instance):
    original = instance.name_6
    instance.name_6 = original
    assert instance.name_6 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_stationAuto_setter(instance):
    original = instance.stationAuto
    instance.stationAuto = original
    assert instance.stationAuto == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_terminalType_setter(instance):
    original = instance.terminalType
    instance.terminalType = original
    assert instance.terminalType == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_4_setter(instance):
    original = instance.name_4
    instance.name_4 = original
    assert instance.name_4 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_customTimer1_setter(instance):
    original = instance.customTimer1
    instance.customTimer1 = original
    assert instance.customTimer1 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_maxXValue_setter(instance):
    original = instance.maxXValue
    instance.maxXValue = original
    assert instance.maxXValue == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_maxYValue_setter(instance):
    original = instance.maxYValue
    instance.maxYValue = original
    assert instance.maxYValue == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_2_setter(instance):
    original = instance.name_2
    instance.name_2 = original
    assert instance.name_2 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_displayTime_setter(instance):
    original = instance.displayTime
    instance.displayTime = original
    assert instance.displayTime == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_stationReady_setter(instance):
    original = instance.stationReady
    instance.stationReady = original
    assert instance.stationReady == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_name_1_setter(instance):
    original = instance.name_1
    instance.name_1 = original
    assert instance.name_1 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_customTimer2_setter(instance):
    original = instance.customTimer2
    instance.customTimer2 = original
    assert instance.customTimer2 == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_lenOfPlanID_setter(instance):
    original = instance.lenOfPlanID
    instance.lenOfPlanID = original
    assert instance.lenOfPlanID == original



@given(instance=MachineLibrary_NodeGeneral_Terminal_strategy)
def test_machinelibrary_nodegeneral_terminal_stationType_setter(instance):
    original = instance.stationType
    instance.stationType = original
    assert instance.stationType == original

@given(instance=MachineLibrary_NodeGeneralSpecial_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneralspecial_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneralSpecial)

@given(instance=MachineLibrary_NodeGeneral_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodegeneral_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeGeneral)



@given(instance=MachineLibrary_NodeGeneral_strategy)
def test_machinelibrary_nodegeneral_canCreateErrorTag_setter(instance):
    original = instance.canCreateErrorTag
    instance.canCreateErrorTag = original
    assert instance.canCreateErrorTag == original



@given(instance=MachineLibrary_NodeGeneral_strategy)
def test_machinelibrary_nodegeneral_canCreateStateTag_setter(instance):
    original = instance.canCreateStateTag
    instance.canCreateStateTag = original
    assert instance.canCreateStateTag == original

@given(instance=MachineLibrary_NodeSpecialConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodespecialconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeSpecialConfiguration)

@given(instance=MachineLibrary_CommunicationData_strategy)
@settings(max_examples=50)
def test_machinelibrary_communicationdata_instantiation(instance):
    assert isinstance(instance, MachineLibrary_CommunicationData)



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comErrorDataLength_setter(instance):
    original = instance.comErrorDataLength
    instance.comErrorDataLength = original
    assert instance.comErrorDataLength == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comSendDataAddress_setter(instance):
    original = instance.comSendDataAddress
    instance.comSendDataAddress = original
    assert instance.comSendDataAddress == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comErrorDataAddress_setter(instance):
    original = instance.comErrorDataAddress
    instance.comErrorDataAddress = original
    assert instance.comErrorDataAddress == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comRequestDataLength_setter(instance):
    original = instance.comRequestDataLength
    instance.comRequestDataLength = original
    assert instance.comRequestDataLength == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comSIDDataLength_setter(instance):
    original = instance.comSIDDataLength
    instance.comSIDDataLength = original
    assert instance.comSIDDataLength == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comProgressIndDataLength_setter(instance):
    original = instance.comProgressIndDataLength
    instance.comProgressIndDataLength = original
    assert instance.comProgressIndDataLength == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comSendDataLength_setter(instance):
    original = instance.comSendDataLength
    instance.comSendDataLength = original
    assert instance.comSendDataLength == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comRequestDataAddress_setter(instance):
    original = instance.comRequestDataAddress
    instance.comRequestDataAddress = original
    assert instance.comRequestDataAddress == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comSIDDataAddress_setter(instance):
    original = instance.comSIDDataAddress
    instance.comSIDDataAddress = original
    assert instance.comSIDDataAddress == original



@given(instance=MachineLibrary_CommunicationData_strategy)
def test_machinelibrary_communicationdata_comProgressIndDataAddress_setter(instance):
    original = instance.comProgressIndDataAddress
    instance.comProgressIndDataAddress = original
    assert instance.comProgressIndDataAddress == original

@given(instance=MachineLibrary_Parameters_strategy)
@settings(max_examples=50)
def test_machinelibrary_parameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Parameters)



@given(instance=MachineLibrary_Parameters_strategy)
def test_machinelibrary_parameters_parameterConfigNo_setter(instance):
    original = instance.parameterConfigNo
    instance.parameterConfigNo = original
    assert instance.parameterConfigNo == original



@given(instance=MachineLibrary_Parameters_strategy)
def test_machinelibrary_parameters_parameterConfigYes_setter(instance):
    original = instance.parameterConfigYes
    instance.parameterConfigYes = original
    assert instance.parameterConfigYes == original

@given(instance=MachineLibrary_NodePrograms_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodeprograms_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodePrograms)

@given(instance=MachineLibrary_Commands_strategy)
@settings(max_examples=50)
def test_machinelibrary_commands_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Commands)

@given(instance=MachineLibrary_Units_strategy)
@settings(max_examples=50)
def test_machinelibrary_units_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Units)



@given(instance=MachineLibrary_Units_strategy)
def test_machinelibrary_units_unitNo_setter(instance):
    original = instance.unitNo
    instance.unitNo = original
    assert instance.unitNo == original



@given(instance=MachineLibrary_Units_strategy)
def test_machinelibrary_units_unitName_setter(instance):
    original = instance.unitName
    instance.unitName = original
    assert instance.unitName == original



@given(instance=MachineLibrary_Units_strategy)
def test_machinelibrary_units_internalUniNo_setter(instance):
    original = instance.internalUniNo
    instance.internalUniNo = original
    assert instance.internalUniNo == original

@given(instance=MachineLibrary_DPbase_Node_strategy)
@settings(max_examples=50)
def test_machinelibrary_dpbase_node_instantiation(instance):
    assert isinstance(instance, MachineLibrary_DPbase_Node)



@given(instance=MachineLibrary_DPbase_Node_strategy)
def test_machinelibrary_dpbase_node_isXPS_setter(instance):
    original = instance.isXPS
    instance.isXPS = original
    assert instance.isXPS == original



@given(instance=MachineLibrary_DPbase_Node_strategy)
def test_machinelibrary_dpbase_node_nodeNo_setter(instance):
    original = instance.nodeNo
    instance.nodeNo = original
    assert instance.nodeNo == original

@given(instance=MachineLibrary_Compac_Link_strategy)
@settings(max_examples=50)
def test_machinelibrary_compac_link_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Compac_Link)



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_checksumCode_setter(instance):
    original = instance.checksumCode
    instance.checksumCode = original
    assert instance.checksumCode == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_splitLongMessage_setter(instance):
    original = instance.splitLongMessage
    instance.splitLongMessage = original
    assert instance.splitLongMessage == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_retry_setter(instance):
    original = instance.retry
    instance.retry = original
    assert instance.retry == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_bytecountcode_setter(instance):
    original = instance.bytecountcode
    instance.bytecountcode = original
    assert instance.bytecountcode == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_checksum_setter(instance):
    original = instance.checksum
    instance.checksum = original
    assert instance.checksum == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_bcc_setter(instance):
    original = instance.bcc
    instance.bcc = original
    assert instance.bcc == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_commConfig_setter(instance):
    original = instance.commConfig
    instance.commConfig = original
    assert instance.commConfig == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_useNotACK_NAK_setter(instance):
    original = instance.useNotACK_NAK
    instance.useNotACK_NAK = original
    assert instance.useNotACK_NAK == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_useNotENQ_setter(instance):
    original = instance.useNotENQ
    instance.useNotENQ = original
    assert instance.useNotENQ == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_byteCount_setter(instance):
    original = instance.byteCount
    instance.byteCount = original
    assert instance.byteCount == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_maxDataLength_setter(instance):
    original = instance.maxDataLength
    instance.maxDataLength = original
    assert instance.maxDataLength == original



@given(instance=MachineLibrary_Compac_Link_strategy)
def test_machinelibrary_compac_link_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=MachineLibrary_FileTransfer_Link_strategy)
@settings(max_examples=50)
def test_machinelibrary_filetransfer_link_instantiation(instance):
    assert isinstance(instance, MachineLibrary_FileTransfer_Link)



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_flagToWriteWaitFor_setter(instance):
    original = instance.flagToWriteWaitFor
    instance.flagToWriteWaitFor = original
    assert instance.flagToWriteWaitFor == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_flagWriteAfterReading_setter(instance):
    original = instance.flagWriteAfterReading
    instance.flagWriteAfterReading = original
    assert instance.flagWriteAfterReading == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_timeoutwrite_setter(instance):
    original = instance.timeoutwrite
    instance.timeoutwrite = original
    assert instance.timeoutwrite == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_pollTime_setter(instance):
    original = instance.pollTime
    instance.pollTime = original
    assert instance.pollTime == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_delimter_setter(instance):
    original = instance.delimter
    instance.delimter = original
    assert instance.delimter == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_flagDelAfterReading_setter(instance):
    original = instance.flagDelAfterReading
    instance.flagDelAfterReading = original
    assert instance.flagDelAfterReading == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_writeAfterReading_setter(instance):
    original = instance.writeAfterReading
    instance.writeAfterReading = original
    assert instance.writeAfterReading == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_toWriteWaitFor_setter(instance):
    original = instance.toWriteWaitFor
    instance.toWriteWaitFor = original
    assert instance.toWriteWaitFor == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_flagToWriteWaitForDeleted_setter(instance):
    original = instance.flagToWriteWaitForDeleted
    instance.flagToWriteWaitForDeleted = original
    assert instance.flagToWriteWaitForDeleted == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_writePath_setter(instance):
    original = instance.writePath
    instance.writePath = original
    assert instance.writePath == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_readPath_setter(instance):
    original = instance.readPath
    instance.readPath = original
    assert instance.readPath == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original



@given(instance=MachineLibrary_FileTransfer_Link_strategy)
def test_machinelibrary_filetransfer_link_maxDataLength_setter(instance):
    original = instance.maxDataLength
    instance.maxDataLength = original
    assert instance.maxDataLength == original

@given(instance=MachineLibrary_Serial_Link_strategy)
@settings(max_examples=50)
def test_machinelibrary_serial_link_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Serial_Link)



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_maxCharDelay_setter(instance):
    original = instance.maxCharDelay
    instance.maxCharDelay = original
    assert instance.maxCharDelay == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_commConfig_setter(instance):
    original = instance.commConfig
    instance.commConfig = original
    assert instance.commConfig == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_endChar_setter(instance):
    original = instance.endChar
    instance.endChar = original
    assert instance.endChar == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_startChar_setter(instance):
    original = instance.startChar
    instance.startChar = original
    assert instance.startChar == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_bufferLenght_setter(instance):
    original = instance.bufferLenght
    instance.bufferLenght = original
    assert instance.bufferLenght == original



@given(instance=MachineLibrary_Serial_Link_strategy)
def test_machinelibrary_serial_link_logging_setter(instance):
    original = instance.logging
    instance.logging = original
    assert instance.logging == original

@given(instance=MachineLibrary_TCPIP_Link_strategy)
@settings(max_examples=50)
def test_machinelibrary_tcpip_link_instantiation(instance):
    assert isinstance(instance, MachineLibrary_TCPIP_Link)



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_1_setter(instance):
    original = instance.address_1
    instance.address_1 = original
    assert instance.address_1 == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_msgDelay_setter(instance):
    original = instance.msgDelay
    instance.msgDelay = original
    assert instance.msgDelay == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_5_setter(instance):
    original = instance.address_5
    instance.address_5 = original
    assert instance.address_5 == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_maxDataSize_setter(instance):
    original = instance.maxDataSize
    instance.maxDataSize = original
    assert instance.maxDataSize == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_6_setter(instance):
    original = instance.address_6
    instance.address_6 = original
    assert instance.address_6 == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_3_setter(instance):
    original = instance.address_3
    instance.address_3 = original
    assert instance.address_3 == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_termChar_setter(instance):
    original = instance.termChar
    instance.termChar = original
    assert instance.termChar == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_2_setter(instance):
    original = instance.address_2
    instance.address_2 = original
    assert instance.address_2 == original



@given(instance=MachineLibrary_TCPIP_Link_strategy)
def test_machinelibrary_tcpip_link_address_4_setter(instance):
    original = instance.address_4
    instance.address_4 = original
    assert instance.address_4 == original

@given(instance=MachineLibrary_WinCCLnk_strategy)
@settings(max_examples=50)
def test_machinelibrary_wincclnk_instantiation(instance):
    assert isinstance(instance, MachineLibrary_WinCCLnk)



@given(instance=MachineLibrary_WinCCLnk_strategy)
def test_machinelibrary_wincclnk_updateCycle_setter(instance):
    original = instance.updateCycle
    instance.updateCycle = original
    assert instance.updateCycle == original



@given(instance=MachineLibrary_WinCCLnk_strategy)
def test_machinelibrary_wincclnk_canCreateTags_setter(instance):
    original = instance.canCreateTags
    instance.canCreateTags = original
    assert instance.canCreateTags == original



@given(instance=MachineLibrary_WinCCLnk_strategy)
def test_machinelibrary_wincclnk_updateCycle_Help_setter(instance):
    original = instance.updateCycle_Help
    instance.updateCycle_Help = original
    assert instance.updateCycle_Help == original



@given(instance=MachineLibrary_WinCCLnk_strategy)
def test_machinelibrary_wincclnk_canModifyTag_setter(instance):
    original = instance.canModifyTag
    instance.canModifyTag = original
    assert instance.canModifyTag == original



@given(instance=MachineLibrary_WinCCLnk_strategy)
def test_machinelibrary_wincclnk_connectionName_setter(instance):
    original = instance.connectionName
    instance.connectionName = original
    assert instance.connectionName == original

@given(instance=MachineLibrary_LinkConfig_strategy)
@settings(max_examples=50)
def test_machinelibrary_linkconfig_instantiation(instance):
    assert isinstance(instance, MachineLibrary_LinkConfig)

@given(instance=MachineLibrary_NodeConfig_strategy)
@settings(max_examples=50)
def test_machinelibrary_nodeconfig_instantiation(instance):
    assert isinstance(instance, MachineLibrary_NodeConfig)



@given(instance=MachineLibrary_NodeConfig_strategy)
def test_machinelibrary_nodeconfig_nodeName_setter(instance):
    original = instance.nodeName
    instance.nodeName = original
    assert instance.nodeName == original



@given(instance=MachineLibrary_NodeConfig_strategy)
def test_machinelibrary_nodeconfig_simFileName_setter(instance):
    original = instance.simFileName
    instance.simFileName = original
    assert instance.simFileName == original



@given(instance=MachineLibrary_NodeConfig_strategy)
def test_machinelibrary_nodeconfig_nodeNo_setter(instance):
    original = instance.nodeNo
    instance.nodeNo = original
    assert instance.nodeNo == original

@given(instance=MachineLibrary_Link2_strategy)
@settings(max_examples=50)
def test_machinelibrary_link2_instantiation(instance):
    assert isinstance(instance, MachineLibrary_Link2)



@given(instance=MachineLibrary_Link2_strategy)
def test_machinelibrary_link2_link2ParamSection_setter(instance):
    original = instance.link2ParamSection
    instance.link2ParamSection = original
    assert instance.link2ParamSection == original



@given(instance=MachineLibrary_Link2_strategy)
def test_machinelibrary_link2_link2Type_setter(instance):
    original = instance.link2Type
    instance.link2Type = original
    assert instance.link2Type == original



@given(instance=MachineLibrary_Link2_strategy)
def test_machinelibrary_link2_link2ParamFile_setter(instance):
    original = instance.link2ParamFile
    instance.link2ParamFile = original
    assert instance.link2ParamFile == original

@given(instance=MachineLibrary_DPbase_Link_strategy)
@settings(max_examples=50)
def test_machinelibrary_dpbase_link_instantiation(instance):
    assert isinstance(instance, MachineLibrary_DPbase_Link)



@given(instance=MachineLibrary_DPbase_Link_strategy)
def test_machinelibrary_dpbase_link_cp_name_setter(instance):
    original = instance.cp_name
    instance.cp_name = original
    assert instance.cp_name == original



@given(instance=MachineLibrary_DPbase_Link_strategy)
def test_machinelibrary_dpbase_link_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original



@given(instance=MachineLibrary_DPbase_Link_strategy)
def test_machinelibrary_dpbase_link_maxNodes_setter(instance):
    original = instance.maxNodes
    instance.maxNodes = original
    assert instance.maxNodes == original

@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
@settings(max_examples=50)
def test_machinelibrary_ibmwebspheremq_instantiation(instance):
    assert isinstance(instance, MachineLibrary_IBMWebsphereMQ)



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_qName_setter(instance):
    original = instance.qName
    instance.qName = original
    assert instance.qName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_sendDynamicQueName_setter(instance):
    original = instance.sendDynamicQueName
    instance.sendDynamicQueName = original
    assert instance.sendDynamicQueName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_sendQueName_setter(instance):
    original = instance.sendQueName
    instance.sendQueName = original
    assert instance.sendQueName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_maxDataSize_setter(instance):
    original = instance.maxDataSize
    instance.maxDataSize = original
    assert instance.maxDataSize == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_sendQueMgrName_setter(instance):
    original = instance.sendQueMgrName
    instance.sendQueMgrName = original
    assert instance.sendQueMgrName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_readDynamicQueName_setter(instance):
    original = instance.readDynamicQueName
    instance.readDynamicQueName = original
    assert instance.readDynamicQueName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_readQueMgrName_setter(instance):
    original = instance.readQueMgrName
    instance.readQueMgrName = original
    assert instance.readQueMgrName == original



@given(instance=MachineLibrary_IBMWebsphereMQ_strategy)
def test_machinelibrary_ibmwebspheremq_readQueName_setter(instance):
    original = instance.readQueName
    instance.readQueName = original
    assert instance.readQueName == original

@given(instance=MachineLibrary_LabMachine_strategy)
@settings(max_examples=50)
def test_machinelibrary_labmachine_instantiation(instance):
    assert isinstance(instance, MachineLibrary_LabMachine)



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_linkParamFile_setter(instance):
    original = instance.linkParamFile
    instance.linkParamFile = original
    assert instance.linkParamFile == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_versionRemark_setter(instance):
    original = instance.versionRemark
    instance.versionRemark = original
    assert instance.versionRemark == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_machineVersionNo_setter(instance):
    original = instance.machineVersionNo
    instance.machineVersionNo = original
    assert instance.machineVersionNo == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_linkParamSection_setter(instance):
    original = instance.linkParamSection
    instance.linkParamSection = original
    assert instance.linkParamSection == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_machineName_setter(instance):
    original = instance.machineName
    instance.machineName = original
    assert instance.machineName == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_createWinCCTags_setter(instance):
    original = instance.createWinCCTags
    instance.createWinCCTags = original
    assert instance.createWinCCTags == original



@given(instance=MachineLibrary_LabMachine_strategy)
def test_machinelibrary_labmachine_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=MachineLibrary_LabMachines_strategy)
@settings(max_examples=50)
def test_machinelibrary_labmachines_instantiation(instance):
    assert isinstance(instance, MachineLibrary_LabMachines)

@given(instance=MachineLibrary_PMMachineLibrary_strategy)
@settings(max_examples=50)
def test_machinelibrary_pmmachinelibrary_instantiation(instance):
    assert isinstance(instance, MachineLibrary_PMMachineLibrary)



@given(instance=MachineLibrary_PMMachineLibrary_strategy)
def test_machinelibrary_pmmachinelibrary_libraryVersion_setter(instance):
    original = instance.libraryVersion
    instance.libraryVersion = original
    assert instance.libraryVersion == original



@given(instance=MachineLibrary_PMMachineLibrary_strategy)
def test_machinelibrary_pmmachinelibrary_libraryVersionRemark_setter(instance):
    original = instance.libraryVersionRemark
    instance.libraryVersionRemark = original
    assert instance.libraryVersionRemark == original
