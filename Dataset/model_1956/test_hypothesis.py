import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MachineLibrary::RobotToWinCC,
    MachineLibrary::RobotWinCCToRobot,
    MachineLibrary::RobotConfSendOrder,
    MachineLibrary::RobotVarToBusycode,
    MachineLibrary::RobotVarToErrorbit,
    MachineLibrary::PlainMoveEntrySend,
    MachineLibrary::TransferFileSection,
    MachineLibrary::RobotConfiguration,
    MachineLibrary::RobotVarToErrorbits,
    MachineLibrary::RobotWarningONDelete,
    MachineLibrary::RobotToWinccs,
    MachineLibrary::RobotWinCCToRobots,
    MachineLibrary::RobotConfSendOrders,
    MachineLibrary::RobotVarToBusyCodes,
    MachineLibrary::Parameter,
    MachineLibrary::PlainMove,
    MachineLibrary::Transfer,
    MachineLibrary::ParamPrint,
    MachineLibrary::NodeProgram,
    MachineLibrary::Command,
    MachineLibrary::UnitProgParameters,
    MachineLibrary::UnitProgram,
    MachineLibrary::Position,
    MachineLibrary::Button,
    MachineLibrary::CheckAddSID::Values::PM2PM,
    MachineLibrary::SepByComma::ID::Scanner,
    MachineLibrary::SepByComma::Field::Scanner,
    MachineLibrary::StatusBit,
    MachineLibrary::HistoryConfig::AccuPyc,
    MachineLibrary::CheckSampleConfig::SuperQXRF,
    MachineLibrary::InsertRemove::Keywords::Host,
    MachineLibrary::InsertRemove::Types::Host,
    MachineLibrary::InsertRemove::Entry::Host,
    MachineLibrary::CheckSampleRunTimeParams::SuperQXRF,
    MachineLibrary::OES::XRF::Condition,
    MachineLibrary::InsertRemove::Host,
    MachineLibrary::Moved::Host,
    MachineLibrary::WS::Update::Host,
    MachineLibrary::Report::Host,
    MachineLibrary::Settings::ARL::XRF::OES,
    MachineLibrary::DisableSCT::ARL::XRF::OES,
    MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES,
    MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES,
    MachineLibrary::ExePrepUnit::ARL::XRF::OES,
    MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES,
    MachineLibrary::ExecuteFiling::ARL::XRF::OES,
    MachineLibrary::CheckFilling::ARL::XRF::OES,
    MachineLibrary::CheckSample::SuperQXRF,
    MachineLibrary::CheckSampleRunTime::SuperQXRF,
    MachineLibrary::Communication::SuperQXRF,
    MachineLibrary::ControlSamples::SuperQXRF,
    MachineLibrary::File::Sample::ARL::XRF::OES,
    MachineLibrary::PS::Process::Finished::ARL::XRF::OES,
    MachineLibrary::GeneralSetting::ARL::XRF::OES,
    MachineLibrary::CheckAddSID::PM2PM,
    MachineLibrary::SepByComma::Scanner,
    MachineLibrary::History::AccuPycMeter,
    MachineLibrary::UnitConfig::Host,
    MachineLibrary::UnitConfig::ARL::XRF::OES,
    MachineLibrary::UnitConfig::SuperQ::XRF,
    MachineLibrary::UnitConfig::OBLF::OES,
    MachineLibrary::UnitConfig::Terminal,
    MachineLibrary::GeneralParameter::SuperQXRF,
    MachineLibrary::ErrorMessage::OBLFOES,
    MachineLibrary::RecalRequest::OBLFOES,
    MachineLibrary::TestRequest::OBLFOES,
    MachineLibrary::OutputRequest::OBLFOES,
    MachineLibrary::Translate::Terminal,
    MachineLibrary::UnitGeneral::Scanner,
    MachineLibrary::UnitGeneral::RigakuXRF,
    MachineLibrary::UnitGeneral::SuperQ,
    MachineLibrary::UnitGeneral::AccPyc,
    MachineLibrary::UnitGeneral::PM2PM,
    MachineLibrary::UnitGeneral::Remote,
    MachineLibrary::UnitGeneral::HostPC,
    MachineLibrary::UnitGeneral::Terminal,
    MachineLibrary::PLCtoPmMatrix,
    MachineLibrary::StausBits,
    MachineLibrary::Positions,
    MachineLibrary::WinCCAddTag,
    MachineLibrary::UnitGeneralParameters,
    MachineLibrary::UnitSpecialConfiguration,
    MachineLibrary::UnitGeneralSpecial,
    MachineLibrary::UnitGeneral,
    MachineLibrary::Buttons,
    MachineLibrary::UnitPrograms,
    MachineLibrary::NodeGeneral::RigakuXRF,
    MachineLibrary::NodeGeneral::AccuPycMeter,
    MachineLibrary::NodeGeneral::WinCC2WinCC,
    MachineLibrary::NodeGeneral::RemotePM,
    MachineLibrary::NodeGeneral::PM2PM,
    MachineLibrary::NodeGeneral::Terminal,
    MachineLibrary::NodeGeneralSpecial,
    MachineLibrary::NodeGeneral,
    MachineLibrary::NodeSpecialConfiguration,
    MachineLibrary::CommunicationData,
    MachineLibrary::Parameters,
    MachineLibrary::NodePrograms,
    MachineLibrary::Commands,
    MachineLibrary::Units,
    MachineLibrary::DPbase::Node,
    MachineLibrary::Compac::Link,
    MachineLibrary::FileTransfer::Link,
    MachineLibrary::Serial::Link,
    MachineLibrary::TCPIP::Link,
    MachineLibrary::WinCCLnk,
    MachineLibrary::LinkConfig,
    MachineLibrary::NodeConfig,
    MachineLibrary::Link2,
    MachineLibrary::DPbase::Link,
    MachineLibrary::IBMWebsphereMQ,
    MachineLibrary::LabMachine,
    MachineLibrary::LabMachines,
    MachineLibrary::PMMachineLibrary,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_machinelibrary::robottowincc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotToWinCC)


def test_machinelibrary::robottowincc_constructor_exists():
    assert callable(MachineLibrary::RobotToWinCC.__init__)


def test_machinelibrary::robottowincc_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotToWinCC.__init__)
    params = list(sig.parameters.keys())
    assert "robotToWinccFrom_X" in params, "Missing parameter 'robotToWinccFrom_X'"
    assert "robotToWinccType_X" in params, "Missing parameter 'robotToWinccType_X'"
    assert "robotToWinccSeq_X" in params, "Missing parameter 'robotToWinccSeq_X'"
    assert "robotToWinccTo_X" in params, "Missing parameter 'robotToWinccTo_X'"

def test_machinelibrary::robottowincc_has_robotToWinccFrom_X():
    assert hasattr(MachineLibrary::RobotToWinCC, "robotToWinccFrom_X")
    descriptor = None
    for klass in MachineLibrary::RobotToWinCC.__mro__:
        if "robotToWinccFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccFrom_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robottowincc_has_robotToWinccType_X():
    assert hasattr(MachineLibrary::RobotToWinCC, "robotToWinccType_X")
    descriptor = None
    for klass in MachineLibrary::RobotToWinCC.__mro__:
        if "robotToWinccType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robottowincc_has_robotToWinccSeq_X():
    assert hasattr(MachineLibrary::RobotToWinCC, "robotToWinccSeq_X")
    descriptor = None
    for klass in MachineLibrary::RobotToWinCC.__mro__:
        if "robotToWinccSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robottowincc_has_robotToWinccTo_X():
    assert hasattr(MachineLibrary::RobotToWinCC, "robotToWinccTo_X")
    descriptor = None
    for klass in MachineLibrary::RobotToWinCC.__mro__:
        if "robotToWinccTo_X" in klass.__dict__:
            descriptor = klass.__dict__["robotToWinccTo_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotwincctorobot_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotWinCCToRobot)


def test_machinelibrary::robotwincctorobot_constructor_exists():
    assert callable(MachineLibrary::RobotWinCCToRobot.__init__)


def test_machinelibrary::robotwincctorobot_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotWinCCToRobot.__init__)
    params = list(sig.parameters.keys())
    assert "robotwincctorobootType_X" in params, "Missing parameter 'robotwincctorobootType_X'"
    assert "robotwincctorobotFrom_X" in params, "Missing parameter 'robotwincctorobotFrom_X'"
    assert "robotwincctorobootSeq_X" in params, "Missing parameter 'robotwincctorobootSeq_X'"
    assert "robotwincctorobotTo_X" in params, "Missing parameter 'robotwincctorobotTo_X'"

def test_machinelibrary::robotwincctorobot_has_robotwincctorobootType_X():
    assert hasattr(MachineLibrary::RobotWinCCToRobot, "robotwincctorobootType_X")
    descriptor = None
    for klass in MachineLibrary::RobotWinCCToRobot.__mro__:
        if "robotwincctorobootType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobootType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwincctorobot_has_robotwincctorobotFrom_X():
    assert hasattr(MachineLibrary::RobotWinCCToRobot, "robotwincctorobotFrom_X")
    descriptor = None
    for klass in MachineLibrary::RobotWinCCToRobot.__mro__:
        if "robotwincctorobotFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobotFrom_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwincctorobot_has_robotwincctorobootSeq_X():
    assert hasattr(MachineLibrary::RobotWinCCToRobot, "robotwincctorobootSeq_X")
    descriptor = None
    for klass in MachineLibrary::RobotWinCCToRobot.__mro__:
        if "robotwincctorobootSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobootSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwincctorobot_has_robotwincctorobotTo_X():
    assert hasattr(MachineLibrary::RobotWinCCToRobot, "robotwincctorobotTo_X")
    descriptor = None
    for klass in MachineLibrary::RobotWinCCToRobot.__mro__:
        if "robotwincctorobotTo_X" in klass.__dict__:
            descriptor = klass.__dict__["robotwincctorobotTo_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotconfsendorder_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotConfSendOrder)


def test_machinelibrary::robotconfsendorder_constructor_exists():
    assert callable(MachineLibrary::RobotConfSendOrder.__init__)


def test_machinelibrary::robotconfsendorder_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotConfSendOrder.__init__)
    params = list(sig.parameters.keys())
    assert "robotconfsendorderFrom_X" in params, "Missing parameter 'robotconfsendorderFrom_X'"
    assert "robotconfsendorderType_X" in params, "Missing parameter 'robotconfsendorderType_X'"
    assert "robotconfsendorderVar_X" in params, "Missing parameter 'robotconfsendorderVar_X'"
    assert "robotconfsendorderSeq_X" in params, "Missing parameter 'robotconfsendorderSeq_X'"

def test_machinelibrary::robotconfsendorder_has_robotconfsendorderFrom_X():
    assert hasattr(MachineLibrary::RobotConfSendOrder, "robotconfsendorderFrom_X")
    descriptor = None
    for klass in MachineLibrary::RobotConfSendOrder.__mro__:
        if "robotconfsendorderFrom_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderFrom_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfsendorder_has_robotconfsendorderType_X():
    assert hasattr(MachineLibrary::RobotConfSendOrder, "robotconfsendorderType_X")
    descriptor = None
    for klass in MachineLibrary::RobotConfSendOrder.__mro__:
        if "robotconfsendorderType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfsendorder_has_robotconfsendorderVar_X():
    assert hasattr(MachineLibrary::RobotConfSendOrder, "robotconfsendorderVar_X")
    descriptor = None
    for klass in MachineLibrary::RobotConfSendOrder.__mro__:
        if "robotconfsendorderVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderVar_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfsendorder_has_robotconfsendorderSeq_X():
    assert hasattr(MachineLibrary::RobotConfSendOrder, "robotconfsendorderSeq_X")
    descriptor = None
    for klass in MachineLibrary::RobotConfSendOrder.__mro__:
        if "robotconfsendorderSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotconfsendorderSeq_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotvartobusycode_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotVarToBusycode)


def test_machinelibrary::robotvartobusycode_constructor_exists():
    assert callable(MachineLibrary::RobotVarToBusycode.__init__)


def test_machinelibrary::robotvartobusycode_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotVarToBusycode.__init__)
    params = list(sig.parameters.keys())
    assert "robotvartobusycodeSeq_X" in params, "Missing parameter 'robotvartobusycodeSeq_X'"
    assert "robotvartobusycodeUnit_X" in params, "Missing parameter 'robotvartobusycodeUnit_X'"
    assert "robotvartobusycodeBit_X" in params, "Missing parameter 'robotvartobusycodeBit_X'"
    assert "robotvartobusycodeType_X" in params, "Missing parameter 'robotvartobusycodeType_X'"
    assert "robotvartobusycodeVar_X" in params, "Missing parameter 'robotvartobusycodeVar_X'"

def test_machinelibrary::robotvartobusycode_has_robotvartobusycodeSeq_X():
    assert hasattr(MachineLibrary::RobotVarToBusycode, "robotvartobusycodeSeq_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToBusycode.__mro__:
        if "robotvartobusycodeSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartobusycode_has_robotvartobusycodeUnit_X():
    assert hasattr(MachineLibrary::RobotVarToBusycode, "robotvartobusycodeUnit_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToBusycode.__mro__:
        if "robotvartobusycodeUnit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeUnit_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartobusycode_has_robotvartobusycodeBit_X():
    assert hasattr(MachineLibrary::RobotVarToBusycode, "robotvartobusycodeBit_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToBusycode.__mro__:
        if "robotvartobusycodeBit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeBit_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartobusycode_has_robotvartobusycodeType_X():
    assert hasattr(MachineLibrary::RobotVarToBusycode, "robotvartobusycodeType_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToBusycode.__mro__:
        if "robotvartobusycodeType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeType_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartobusycode_has_robotvartobusycodeVar_X():
    assert hasattr(MachineLibrary::RobotVarToBusycode, "robotvartobusycodeVar_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToBusycode.__mro__:
        if "robotvartobusycodeVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartobusycodeVar_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotvartoerrorbit_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotVarToErrorbit)


def test_machinelibrary::robotvartoerrorbit_constructor_exists():
    assert callable(MachineLibrary::RobotVarToErrorbit.__init__)


def test_machinelibrary::robotvartoerrorbit_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotVarToErrorbit.__init__)
    params = list(sig.parameters.keys())
    assert "robotvartoerrorbitBit_X" in params, "Missing parameter 'robotvartoerrorbitBit_X'"
    assert "robotvartoerrorbitSeq_X" in params, "Missing parameter 'robotvartoerrorbitSeq_X'"
    assert "robotvartoerrorbitInv_X" in params, "Missing parameter 'robotvartoerrorbitInv_X'"
    assert "robotvartoerrorbitVar_X" in params, "Missing parameter 'robotvartoerrorbitVar_X'"
    assert "robotvartoerrorbitType_X" in params, "Missing parameter 'robotvartoerrorbitType_X'"

def test_machinelibrary::robotvartoerrorbit_has_robotvartoerrorbitBit_X():
    assert hasattr(MachineLibrary::RobotVarToErrorbit, "robotvartoerrorbitBit_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitBit_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitBit_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartoerrorbit_has_robotvartoerrorbitSeq_X():
    assert hasattr(MachineLibrary::RobotVarToErrorbit, "robotvartoerrorbitSeq_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartoerrorbit_has_robotvartoerrorbitInv_X():
    assert hasattr(MachineLibrary::RobotVarToErrorbit, "robotvartoerrorbitInv_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitInv_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitInv_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartoerrorbit_has_robotvartoerrorbitVar_X():
    assert hasattr(MachineLibrary::RobotVarToErrorbit, "robotvartoerrorbitVar_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitVar_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitVar_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotvartoerrorbit_has_robotvartoerrorbitType_X():
    assert hasattr(MachineLibrary::RobotVarToErrorbit, "robotvartoerrorbitType_X")
    descriptor = None
    for klass in MachineLibrary::RobotVarToErrorbit.__mro__:
        if "robotvartoerrorbitType_X" in klass.__dict__:
            descriptor = klass.__dict__["robotvartoerrorbitType_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::plainmoveentrysend_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::PlainMoveEntrySend)


def test_machinelibrary::plainmoveentrysend_constructor_exists():
    assert callable(MachineLibrary::PlainMoveEntrySend.__init__)


def test_machinelibrary::plainmoveentrysend_constructor_args():
    sig = inspect.signature(MachineLibrary::PlainMoveEntrySend.__init__)
    params = list(sig.parameters.keys())
    assert "plainmoveSeq" in params, "Missing parameter 'plainmoveSeq'"
    assert "plainmoveEntry" in params, "Missing parameter 'plainmoveEntry'"
    assert "plainmoveSend" in params, "Missing parameter 'plainmoveSend'"

def test_machinelibrary::plainmoveentrysend_has_plainmoveSeq():
    assert hasattr(MachineLibrary::PlainMoveEntrySend, "plainmoveSeq")
    descriptor = None
    for klass in MachineLibrary::PlainMoveEntrySend.__mro__:
        if "plainmoveSeq" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSeq"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plainmoveentrysend_has_plainmoveEntry():
    assert hasattr(MachineLibrary::PlainMoveEntrySend, "plainmoveEntry")
    descriptor = None
    for klass in MachineLibrary::PlainMoveEntrySend.__mro__:
        if "plainmoveEntry" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveEntry"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plainmoveentrysend_has_plainmoveSend():
    assert hasattr(MachineLibrary::PlainMoveEntrySend, "plainmoveSend")
    descriptor = None
    for klass in MachineLibrary::PlainMoveEntrySend.__mro__:
        if "plainmoveSend" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSend"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::transferfilesection_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::TransferFileSection)


def test_machinelibrary::transferfilesection_constructor_exists():
    assert callable(MachineLibrary::TransferFileSection.__init__)


def test_machinelibrary::transferfilesection_constructor_args():
    sig = inspect.signature(MachineLibrary::TransferFileSection.__init__)
    params = list(sig.parameters.keys())
    assert "transferSection" in params, "Missing parameter 'transferSection'"
    assert "transferFile" in params, "Missing parameter 'transferFile'"
    assert "transferSeq" in params, "Missing parameter 'transferSeq'"

def test_machinelibrary::transferfilesection_has_transferSection():
    assert hasattr(MachineLibrary::TransferFileSection, "transferSection")
    descriptor = None
    for klass in MachineLibrary::TransferFileSection.__mro__:
        if "transferSection" in klass.__dict__:
            descriptor = klass.__dict__["transferSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::transferfilesection_has_transferFile():
    assert hasattr(MachineLibrary::TransferFileSection, "transferFile")
    descriptor = None
    for klass in MachineLibrary::TransferFileSection.__mro__:
        if "transferFile" in klass.__dict__:
            descriptor = klass.__dict__["transferFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::transferfilesection_has_transferSeq():
    assert hasattr(MachineLibrary::TransferFileSection, "transferSeq")
    descriptor = None
    for klass in MachineLibrary::TransferFileSection.__mro__:
        if "transferSeq" in klass.__dict__:
            descriptor = klass.__dict__["transferSeq"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotConfiguration)


def test_machinelibrary::robotconfiguration_constructor_exists():
    assert callable(MachineLibrary::RobotConfiguration.__init__)


def test_machinelibrary::robotconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotConfiguration.__init__)
    params = list(sig.parameters.keys())
    assert "robotSystemID" in params, "Missing parameter 'robotSystemID'"
    assert "robotIPAddress" in params, "Missing parameter 'robotIPAddress'"
    assert "robotID" in params, "Missing parameter 'robotID'"
    assert "robotActivate" in params, "Missing parameter 'robotActivate'"

def test_machinelibrary::robotconfiguration_has_robotSystemID():
    assert hasattr(MachineLibrary::RobotConfiguration, "robotSystemID")
    descriptor = None
    for klass in MachineLibrary::RobotConfiguration.__mro__:
        if "robotSystemID" in klass.__dict__:
            descriptor = klass.__dict__["robotSystemID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfiguration_has_robotIPAddress():
    assert hasattr(MachineLibrary::RobotConfiguration, "robotIPAddress")
    descriptor = None
    for klass in MachineLibrary::RobotConfiguration.__mro__:
        if "robotIPAddress" in klass.__dict__:
            descriptor = klass.__dict__["robotIPAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfiguration_has_robotID():
    assert hasattr(MachineLibrary::RobotConfiguration, "robotID")
    descriptor = None
    for klass in MachineLibrary::RobotConfiguration.__mro__:
        if "robotID" in klass.__dict__:
            descriptor = klass.__dict__["robotID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotconfiguration_has_robotActivate():
    assert hasattr(MachineLibrary::RobotConfiguration, "robotActivate")
    descriptor = None
    for klass in MachineLibrary::RobotConfiguration.__mro__:
        if "robotActivate" in klass.__dict__:
            descriptor = klass.__dict__["robotActivate"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robotvartoerrorbits_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotVarToErrorbits)


def test_machinelibrary::robotvartoerrorbits_constructor_exists():
    assert callable(MachineLibrary::RobotVarToErrorbits.__init__)


def test_machinelibrary::robotvartoerrorbits_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotVarToErrorbits.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::robotwarningondelete_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotWarningONDelete)


def test_machinelibrary::robotwarningondelete_constructor_exists():
    assert callable(MachineLibrary::RobotWarningONDelete.__init__)


def test_machinelibrary::robotwarningondelete_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotWarningONDelete.__init__)
    params = list(sig.parameters.keys())
    assert "robotExtraPos_1" in params, "Missing parameter 'robotExtraPos_1'"
    assert "robotExtraUnit_2" in params, "Missing parameter 'robotExtraUnit_2'"
    assert "robotErrBitWhenConfirmationIsNeededFor_PM" in params, "Missing parameter 'robotErrBitWhenConfirmationIsNeededFor_PM'"
    assert "robotErrBitWhenConfirmationIsNeededFor_Robot" in params, "Missing parameter 'robotErrBitWhenConfirmationIsNeededFor_Robot'"

def test_machinelibrary::robotwarningondelete_has_robotExtraPos_1():
    assert hasattr(MachineLibrary::RobotWarningONDelete, "robotExtraPos_1")
    descriptor = None
    for klass in MachineLibrary::RobotWarningONDelete.__mro__:
        if "robotExtraPos_1" in klass.__dict__:
            descriptor = klass.__dict__["robotExtraPos_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwarningondelete_has_robotExtraUnit_2():
    assert hasattr(MachineLibrary::RobotWarningONDelete, "robotExtraUnit_2")
    descriptor = None
    for klass in MachineLibrary::RobotWarningONDelete.__mro__:
        if "robotExtraUnit_2" in klass.__dict__:
            descriptor = klass.__dict__["robotExtraUnit_2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwarningondelete_has_robotErrBitWhenConfirmationIsNeededFor_PM():
    assert hasattr(MachineLibrary::RobotWarningONDelete, "robotErrBitWhenConfirmationIsNeededFor_PM")
    descriptor = None
    for klass in MachineLibrary::RobotWarningONDelete.__mro__:
        if "robotErrBitWhenConfirmationIsNeededFor_PM" in klass.__dict__:
            descriptor = klass.__dict__["robotErrBitWhenConfirmationIsNeededFor_PM"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::robotwarningondelete_has_robotErrBitWhenConfirmationIsNeededFor_Robot():
    assert hasattr(MachineLibrary::RobotWarningONDelete, "robotErrBitWhenConfirmationIsNeededFor_Robot")
    descriptor = None
    for klass in MachineLibrary::RobotWarningONDelete.__mro__:
        if "robotErrBitWhenConfirmationIsNeededFor_Robot" in klass.__dict__:
            descriptor = klass.__dict__["robotErrBitWhenConfirmationIsNeededFor_Robot"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::robottowinccs_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotToWinccs)


def test_machinelibrary::robottowinccs_constructor_exists():
    assert callable(MachineLibrary::RobotToWinccs.__init__)


def test_machinelibrary::robottowinccs_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotToWinccs.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::robotwincctorobots_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotWinCCToRobots)


def test_machinelibrary::robotwincctorobots_constructor_exists():
    assert callable(MachineLibrary::RobotWinCCToRobots.__init__)


def test_machinelibrary::robotwincctorobots_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotWinCCToRobots.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::robotconfsendorders_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotConfSendOrders)


def test_machinelibrary::robotconfsendorders_constructor_exists():
    assert callable(MachineLibrary::RobotConfSendOrders.__init__)


def test_machinelibrary::robotconfsendorders_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotConfSendOrders.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::robotvartobusycodes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RobotVarToBusyCodes)


def test_machinelibrary::robotvartobusycodes_constructor_exists():
    assert callable(MachineLibrary::RobotVarToBusyCodes.__init__)


def test_machinelibrary::robotvartobusycodes_constructor_args():
    sig = inspect.signature(MachineLibrary::RobotVarToBusyCodes.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::parameter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Parameter)


def test_machinelibrary::parameter_constructor_exists():
    assert callable(MachineLibrary::Parameter.__init__)


def test_machinelibrary::parameter_constructor_args():
    sig = inspect.signature(MachineLibrary::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterT2" in params, "Missing parameter 'parameterT2'"
    assert "parameterMin" in params, "Missing parameter 'parameterMin'"
    assert "parameterV" in params, "Missing parameter 'parameterV'"
    assert "parameterT1" in params, "Missing parameter 'parameterT1'"
    assert "parameterConfig" in params, "Missing parameter 'parameterConfig'"
    assert "parameterMax" in params, "Missing parameter 'parameterMax'"
    assert "parameterV1" in params, "Missing parameter 'parameterV1'"
    assert "parameterType" in params, "Missing parameter 'parameterType'"
    assert "parameterName" in params, "Missing parameter 'parameterName'"
    assert "parameterV0" in params, "Missing parameter 'parameterV0'"
    assert "parameterParaLen" in params, "Missing parameter 'parameterParaLen'"

def test_machinelibrary::parameter_has_parameterT2():
    assert hasattr(MachineLibrary::Parameter, "parameterT2")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterT2" in klass.__dict__:
            descriptor = klass.__dict__["parameterT2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterMin():
    assert hasattr(MachineLibrary::Parameter, "parameterMin")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterMin" in klass.__dict__:
            descriptor = klass.__dict__["parameterMin"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterV():
    assert hasattr(MachineLibrary::Parameter, "parameterV")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterV" in klass.__dict__:
            descriptor = klass.__dict__["parameterV"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterT1():
    assert hasattr(MachineLibrary::Parameter, "parameterT1")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterT1" in klass.__dict__:
            descriptor = klass.__dict__["parameterT1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterConfig():
    assert hasattr(MachineLibrary::Parameter, "parameterConfig")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterConfig" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterMax():
    assert hasattr(MachineLibrary::Parameter, "parameterMax")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterMax" in klass.__dict__:
            descriptor = klass.__dict__["parameterMax"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterV1():
    assert hasattr(MachineLibrary::Parameter, "parameterV1")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterV1" in klass.__dict__:
            descriptor = klass.__dict__["parameterV1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterType():
    assert hasattr(MachineLibrary::Parameter, "parameterType")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterName():
    assert hasattr(MachineLibrary::Parameter, "parameterName")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterName" in klass.__dict__:
            descriptor = klass.__dict__["parameterName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterV0():
    assert hasattr(MachineLibrary::Parameter, "parameterV0")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterV0" in klass.__dict__:
            descriptor = klass.__dict__["parameterV0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameter_has_parameterParaLen():
    assert hasattr(MachineLibrary::Parameter, "parameterParaLen")
    descriptor = None
    for klass in MachineLibrary::Parameter.__mro__:
        if "parameterParaLen" in klass.__dict__:
            descriptor = klass.__dict__["parameterParaLen"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::plainmove_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::PlainMove)


def test_machinelibrary::plainmove_constructor_exists():
    assert callable(MachineLibrary::PlainMove.__init__)


def test_machinelibrary::plainmove_constructor_args():
    sig = inspect.signature(MachineLibrary::PlainMove.__init__)
    params = list(sig.parameters.keys())
    assert "plainmovePreDefWS" in params, "Missing parameter 'plainmovePreDefWS'"
    assert "plainmoveType" in params, "Missing parameter 'plainmoveType'"
    assert "plainmoveSID_REF" in params, "Missing parameter 'plainmoveSID_REF'"

def test_machinelibrary::plainmove_has_plainmovePreDefWS():
    assert hasattr(MachineLibrary::PlainMove, "plainmovePreDefWS")
    descriptor = None
    for klass in MachineLibrary::PlainMove.__mro__:
        if "plainmovePreDefWS" in klass.__dict__:
            descriptor = klass.__dict__["plainmovePreDefWS"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plainmove_has_plainmoveType():
    assert hasattr(MachineLibrary::PlainMove, "plainmoveType")
    descriptor = None
    for klass in MachineLibrary::PlainMove.__mro__:
        if "plainmoveType" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plainmove_has_plainmoveSID_REF():
    assert hasattr(MachineLibrary::PlainMove, "plainmoveSID_REF")
    descriptor = None
    for klass in MachineLibrary::PlainMove.__mro__:
        if "plainmoveSID_REF" in klass.__dict__:
            descriptor = klass.__dict__["plainmoveSID_REF"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::transfer_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Transfer)


def test_machinelibrary::transfer_constructor_exists():
    assert callable(MachineLibrary::Transfer.__init__)


def test_machinelibrary::transfer_constructor_args():
    sig = inspect.signature(MachineLibrary::Transfer.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::paramprint_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ParamPrint)


def test_machinelibrary::paramprint_constructor_exists():
    assert callable(MachineLibrary::ParamPrint.__init__)


def test_machinelibrary::paramprint_constructor_args():
    sig = inspect.signature(MachineLibrary::ParamPrint.__init__)
    params = list(sig.parameters.keys())
    assert "fontHightData" in params, "Missing parameter 'fontHightData'"
    assert "horzPosLeftBorder" in params, "Missing parameter 'horzPosLeftBorder'"
    assert "fontHightHeader" in params, "Missing parameter 'fontHightHeader'"
    assert "dateStamp" in params, "Missing parameter 'dateStamp'"
    assert "vertPosData" in params, "Missing parameter 'vertPosData'"
    assert "horzPosValues" in params, "Missing parameter 'horzPosValues'"
    assert "vertPosHeader" in params, "Missing parameter 'vertPosHeader'"
    assert "vertLineSpace" in params, "Missing parameter 'vertLineSpace'"

def test_machinelibrary::paramprint_has_fontHightData():
    assert hasattr(MachineLibrary::ParamPrint, "fontHightData")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "fontHightData" in klass.__dict__:
            descriptor = klass.__dict__["fontHightData"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_horzPosLeftBorder():
    assert hasattr(MachineLibrary::ParamPrint, "horzPosLeftBorder")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "horzPosLeftBorder" in klass.__dict__:
            descriptor = klass.__dict__["horzPosLeftBorder"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_fontHightHeader():
    assert hasattr(MachineLibrary::ParamPrint, "fontHightHeader")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "fontHightHeader" in klass.__dict__:
            descriptor = klass.__dict__["fontHightHeader"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_dateStamp():
    assert hasattr(MachineLibrary::ParamPrint, "dateStamp")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "dateStamp" in klass.__dict__:
            descriptor = klass.__dict__["dateStamp"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_vertPosData():
    assert hasattr(MachineLibrary::ParamPrint, "vertPosData")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "vertPosData" in klass.__dict__:
            descriptor = klass.__dict__["vertPosData"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_horzPosValues():
    assert hasattr(MachineLibrary::ParamPrint, "horzPosValues")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "horzPosValues" in klass.__dict__:
            descriptor = klass.__dict__["horzPosValues"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_vertPosHeader():
    assert hasattr(MachineLibrary::ParamPrint, "vertPosHeader")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "vertPosHeader" in klass.__dict__:
            descriptor = klass.__dict__["vertPosHeader"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::paramprint_has_vertLineSpace():
    assert hasattr(MachineLibrary::ParamPrint, "vertLineSpace")
    descriptor = None
    for klass in MachineLibrary::ParamPrint.__mro__:
        if "vertLineSpace" in klass.__dict__:
            descriptor = klass.__dict__["vertLineSpace"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodeprogram_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeProgram)


def test_machinelibrary::nodeprogram_constructor_exists():
    assert callable(MachineLibrary::NodeProgram.__init__)


def test_machinelibrary::nodeprogram_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeProgram.__init__)
    params = list(sig.parameters.keys())
    assert "programLenPerParam" in params, "Missing parameter 'programLenPerParam'"
    assert "programSection" in params, "Missing parameter 'programSection'"
    assert "programNo" in params, "Missing parameter 'programNo'"
    assert "programName" in params, "Missing parameter 'programName'"
    assert "programAddress" in params, "Missing parameter 'programAddress'"

def test_machinelibrary::nodeprogram_has_programLenPerParam():
    assert hasattr(MachineLibrary::NodeProgram, "programLenPerParam")
    descriptor = None
    for klass in MachineLibrary::NodeProgram.__mro__:
        if "programLenPerParam" in klass.__dict__:
            descriptor = klass.__dict__["programLenPerParam"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeprogram_has_programSection():
    assert hasattr(MachineLibrary::NodeProgram, "programSection")
    descriptor = None
    for klass in MachineLibrary::NodeProgram.__mro__:
        if "programSection" in klass.__dict__:
            descriptor = klass.__dict__["programSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeprogram_has_programNo():
    assert hasattr(MachineLibrary::NodeProgram, "programNo")
    descriptor = None
    for klass in MachineLibrary::NodeProgram.__mro__:
        if "programNo" in klass.__dict__:
            descriptor = klass.__dict__["programNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeprogram_has_programName():
    assert hasattr(MachineLibrary::NodeProgram, "programName")
    descriptor = None
    for klass in MachineLibrary::NodeProgram.__mro__:
        if "programName" in klass.__dict__:
            descriptor = klass.__dict__["programName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeprogram_has_programAddress():
    assert hasattr(MachineLibrary::NodeProgram, "programAddress")
    descriptor = None
    for klass in MachineLibrary::NodeProgram.__mro__:
        if "programAddress" in klass.__dict__:
            descriptor = klass.__dict__["programAddress"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::command_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Command)


def test_machinelibrary::command_constructor_exists():
    assert callable(MachineLibrary::Command.__init__)


def test_machinelibrary::command_constructor_args():
    sig = inspect.signature(MachineLibrary::Command.__init__)
    params = list(sig.parameters.keys())
    assert "commandProgParameter" in params, "Missing parameter 'commandProgParameter'"
    assert "commandName" in params, "Missing parameter 'commandName'"
    assert "commandNo" in params, "Missing parameter 'commandNo'"

def test_machinelibrary::command_has_commandProgParameter():
    assert hasattr(MachineLibrary::Command, "commandProgParameter")
    descriptor = None
    for klass in MachineLibrary::Command.__mro__:
        if "commandProgParameter" in klass.__dict__:
            descriptor = klass.__dict__["commandProgParameter"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::command_has_commandName():
    assert hasattr(MachineLibrary::Command, "commandName")
    descriptor = None
    for klass in MachineLibrary::Command.__mro__:
        if "commandName" in klass.__dict__:
            descriptor = klass.__dict__["commandName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::command_has_commandNo():
    assert hasattr(MachineLibrary::Command, "commandNo")
    descriptor = None
    for klass in MachineLibrary::Command.__mro__:
        if "commandNo" in klass.__dict__:
            descriptor = klass.__dict__["commandNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitprogparameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitProgParameters)


def test_machinelibrary::unitprogparameters_constructor_exists():
    assert callable(MachineLibrary::UnitProgParameters.__init__)


def test_machinelibrary::unitprogparameters_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitProgParameters.__init__)
    params = list(sig.parameters.keys())
    assert "parameterNo" in params, "Missing parameter 'parameterNo'"
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_machinelibrary::unitprogparameters_has_parameterNo():
    assert hasattr(MachineLibrary::UnitProgParameters, "parameterNo")
    descriptor = None
    for klass in MachineLibrary::UnitProgParameters.__mro__:
        if "parameterNo" in klass.__dict__:
            descriptor = klass.__dict__["parameterNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitprogparameters_has_parameter():
    assert hasattr(MachineLibrary::UnitProgParameters, "parameter")
    descriptor = None
    for klass in MachineLibrary::UnitProgParameters.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitprogram_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitProgram)


def test_machinelibrary::unitprogram_constructor_exists():
    assert callable(MachineLibrary::UnitProgram.__init__)


def test_machinelibrary::unitprogram_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitProgram.__init__)
    params = list(sig.parameters.keys())
    assert "unitProgName" in params, "Missing parameter 'unitProgName'"

def test_machinelibrary::unitprogram_has_unitProgName():
    assert hasattr(MachineLibrary::UnitProgram, "unitProgName")
    descriptor = None
    for klass in MachineLibrary::UnitProgram.__mro__:
        if "unitProgName" in klass.__dict__:
            descriptor = klass.__dict__["unitProgName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::position_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Position)


def test_machinelibrary::position_constructor_exists():
    assert callable(MachineLibrary::Position.__init__)


def test_machinelibrary::position_constructor_args():
    sig = inspect.signature(MachineLibrary::Position.__init__)
    params = list(sig.parameters.keys())
    assert "posWarningOnDelete" in params, "Missing parameter 'posWarningOnDelete'"
    assert "posExit" in params, "Missing parameter 'posExit'"
    assert "posName" in params, "Missing parameter 'posName'"
    assert "posIndex" in params, "Missing parameter 'posIndex'"
    assert "posRemark" in params, "Missing parameter 'posRemark'"
    assert "posNo" in params, "Missing parameter 'posNo'"

def test_machinelibrary::position_has_posWarningOnDelete():
    assert hasattr(MachineLibrary::Position, "posWarningOnDelete")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posWarningOnDelete" in klass.__dict__:
            descriptor = klass.__dict__["posWarningOnDelete"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::position_has_posExit():
    assert hasattr(MachineLibrary::Position, "posExit")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posExit" in klass.__dict__:
            descriptor = klass.__dict__["posExit"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::position_has_posName():
    assert hasattr(MachineLibrary::Position, "posName")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posName" in klass.__dict__:
            descriptor = klass.__dict__["posName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::position_has_posIndex():
    assert hasattr(MachineLibrary::Position, "posIndex")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posIndex" in klass.__dict__:
            descriptor = klass.__dict__["posIndex"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::position_has_posRemark():
    assert hasattr(MachineLibrary::Position, "posRemark")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posRemark" in klass.__dict__:
            descriptor = klass.__dict__["posRemark"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::position_has_posNo():
    assert hasattr(MachineLibrary::Position, "posNo")
    descriptor = None
    for klass in MachineLibrary::Position.__mro__:
        if "posNo" in klass.__dict__:
            descriptor = klass.__dict__["posNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::button_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Button)


def test_machinelibrary::button_constructor_exists():
    assert callable(MachineLibrary::Button.__init__)


def test_machinelibrary::button_constructor_args():
    sig = inspect.signature(MachineLibrary::Button.__init__)
    params = list(sig.parameters.keys())
    assert "commandNo" in params, "Missing parameter 'commandNo'"
    assert "buttonText" in params, "Missing parameter 'buttonText'"
    assert "buttonNo" in params, "Missing parameter 'buttonNo'"

def test_machinelibrary::button_has_commandNo():
    assert hasattr(MachineLibrary::Button, "commandNo")
    descriptor = None
    for klass in MachineLibrary::Button.__mro__:
        if "commandNo" in klass.__dict__:
            descriptor = klass.__dict__["commandNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::button_has_buttonText():
    assert hasattr(MachineLibrary::Button, "buttonText")
    descriptor = None
    for klass in MachineLibrary::Button.__mro__:
        if "buttonText" in klass.__dict__:
            descriptor = klass.__dict__["buttonText"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::button_has_buttonNo():
    assert hasattr(MachineLibrary::Button, "buttonNo")
    descriptor = None
    for klass in MachineLibrary::Button.__mro__:
        if "buttonNo" in klass.__dict__:
            descriptor = klass.__dict__["buttonNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checkaddsid::values::pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckAddSID::Values::PM2PM)


def test_machinelibrary::checkaddsid::values::pm2pm_constructor_exists():
    assert callable(MachineLibrary::CheckAddSID::Values::PM2PM.__init__)


def test_machinelibrary::checkaddsid::values::pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckAddSID::Values::PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "optionNo" in params, "Missing parameter 'optionNo'"
    assert "optonValue" in params, "Missing parameter 'optonValue'"

def test_machinelibrary::checkaddsid::values::pm2pm_has_optionNo():
    assert hasattr(MachineLibrary::CheckAddSID::Values::PM2PM, "optionNo")
    descriptor = None
    for klass in MachineLibrary::CheckAddSID::Values::PM2PM.__mro__:
        if "optionNo" in klass.__dict__:
            descriptor = klass.__dict__["optionNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checkaddsid::values::pm2pm_has_optonValue():
    assert hasattr(MachineLibrary::CheckAddSID::Values::PM2PM, "optonValue")
    descriptor = None
    for klass in MachineLibrary::CheckAddSID::Values::PM2PM.__mro__:
        if "optonValue" in klass.__dict__:
            descriptor = klass.__dict__["optonValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::sepbycomma::id::scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::SepByComma::ID::Scanner)


def test_machinelibrary::sepbycomma::id::scanner_constructor_exists():
    assert callable(MachineLibrary::SepByComma::ID::Scanner.__init__)


def test_machinelibrary::sepbycomma::id::scanner_constructor_args():
    sig = inspect.signature(MachineLibrary::SepByComma::ID::Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "idPrevValue" in params, "Missing parameter 'idPrevValue'"
    assert "idCharValue" in params, "Missing parameter 'idCharValue'"
    assert "idSeq_X" in params, "Missing parameter 'idSeq_X'"
    assert "idValue" in params, "Missing parameter 'idValue'"

def test_machinelibrary::sepbycomma::id::scanner_has_idPrevValue():
    assert hasattr(MachineLibrary::SepByComma::ID::Scanner, "idPrevValue")
    descriptor = None
    for klass in MachineLibrary::SepByComma::ID::Scanner.__mro__:
        if "idPrevValue" in klass.__dict__:
            descriptor = klass.__dict__["idPrevValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::sepbycomma::id::scanner_has_idCharValue():
    assert hasattr(MachineLibrary::SepByComma::ID::Scanner, "idCharValue")
    descriptor = None
    for klass in MachineLibrary::SepByComma::ID::Scanner.__mro__:
        if "idCharValue" in klass.__dict__:
            descriptor = klass.__dict__["idCharValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::sepbycomma::id::scanner_has_idSeq_X():
    assert hasattr(MachineLibrary::SepByComma::ID::Scanner, "idSeq_X")
    descriptor = None
    for klass in MachineLibrary::SepByComma::ID::Scanner.__mro__:
        if "idSeq_X" in klass.__dict__:
            descriptor = klass.__dict__["idSeq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::sepbycomma::id::scanner_has_idValue():
    assert hasattr(MachineLibrary::SepByComma::ID::Scanner, "idValue")
    descriptor = None
    for klass in MachineLibrary::SepByComma::ID::Scanner.__mro__:
        if "idValue" in klass.__dict__:
            descriptor = klass.__dict__["idValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::sepbycomma::field::scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::SepByComma::Field::Scanner)


def test_machinelibrary::sepbycomma::field::scanner_constructor_exists():
    assert callable(MachineLibrary::SepByComma::Field::Scanner.__init__)


def test_machinelibrary::sepbycomma::field::scanner_constructor_args():
    sig = inspect.signature(MachineLibrary::SepByComma::Field::Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "fieldNo" in params, "Missing parameter 'fieldNo'"
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_machinelibrary::sepbycomma::field::scanner_has_fieldNo():
    assert hasattr(MachineLibrary::SepByComma::Field::Scanner, "fieldNo")
    descriptor = None
    for klass in MachineLibrary::SepByComma::Field::Scanner.__mro__:
        if "fieldNo" in klass.__dict__:
            descriptor = klass.__dict__["fieldNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::sepbycomma::field::scanner_has_fieldName():
    assert hasattr(MachineLibrary::SepByComma::Field::Scanner, "fieldName")
    descriptor = None
    for klass in MachineLibrary::SepByComma::Field::Scanner.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::statusbit_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::StatusBit)


def test_machinelibrary::statusbit_constructor_exists():
    assert callable(MachineLibrary::StatusBit.__init__)


def test_machinelibrary::statusbit_constructor_args():
    sig = inspect.signature(MachineLibrary::StatusBit.__init__)
    params = list(sig.parameters.keys())
    assert "bitName" in params, "Missing parameter 'bitName'"
    assert "bitNo" in params, "Missing parameter 'bitNo'"

def test_machinelibrary::statusbit_has_bitName():
    assert hasattr(MachineLibrary::StatusBit, "bitName")
    descriptor = None
    for klass in MachineLibrary::StatusBit.__mro__:
        if "bitName" in klass.__dict__:
            descriptor = klass.__dict__["bitName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::statusbit_has_bitNo():
    assert hasattr(MachineLibrary::StatusBit, "bitNo")
    descriptor = None
    for klass in MachineLibrary::StatusBit.__mro__:
        if "bitNo" in klass.__dict__:
            descriptor = klass.__dict__["bitNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::historyconfig::accupyc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::HistoryConfig::AccuPyc)


def test_machinelibrary::historyconfig::accupyc_constructor_exists():
    assert callable(MachineLibrary::HistoryConfig::AccuPyc.__init__)


def test_machinelibrary::historyconfig::accupyc_constructor_args():
    sig = inspect.signature(MachineLibrary::HistoryConfig::AccuPyc.__init__)
    params = list(sig.parameters.keys())
    assert "sampleCupWeight" in params, "Missing parameter 'sampleCupWeight'"
    assert "currentSample" in params, "Missing parameter 'currentSample'"
    assert "currentSampleID" in params, "Missing parameter 'currentSampleID'"

def test_machinelibrary::historyconfig::accupyc_has_sampleCupWeight():
    assert hasattr(MachineLibrary::HistoryConfig::AccuPyc, "sampleCupWeight")
    descriptor = None
    for klass in MachineLibrary::HistoryConfig::AccuPyc.__mro__:
        if "sampleCupWeight" in klass.__dict__:
            descriptor = klass.__dict__["sampleCupWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::historyconfig::accupyc_has_currentSample():
    assert hasattr(MachineLibrary::HistoryConfig::AccuPyc, "currentSample")
    descriptor = None
    for klass in MachineLibrary::HistoryConfig::AccuPyc.__mro__:
        if "currentSample" in klass.__dict__:
            descriptor = klass.__dict__["currentSample"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::historyconfig::accupyc_has_currentSampleID():
    assert hasattr(MachineLibrary::HistoryConfig::AccuPyc, "currentSampleID")
    descriptor = None
    for klass in MachineLibrary::HistoryConfig::AccuPyc.__mro__:
        if "currentSampleID" in klass.__dict__:
            descriptor = klass.__dict__["currentSampleID"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checksampleconfig::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckSampleConfig::SuperQXRF)


def test_machinelibrary::checksampleconfig::superqxrf_constructor_exists():
    assert callable(MachineLibrary::CheckSampleConfig::SuperQXRF.__init__)


def test_machinelibrary::checksampleconfig::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckSampleConfig::SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "samples" in params, "Missing parameter 'samples'"
    assert "sampleID" in params, "Missing parameter 'sampleID'"
    assert "program" in params, "Missing parameter 'program'"
    assert "anaProg" in params, "Missing parameter 'anaProg'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"

def test_machinelibrary::checksampleconfig::superqxrf_has_minutes():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "minutes")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleconfig::superqxrf_has_samples():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "samples")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "samples" in klass.__dict__:
            descriptor = klass.__dict__["samples"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleconfig::superqxrf_has_sampleID():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "sampleID")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "sampleID" in klass.__dict__:
            descriptor = klass.__dict__["sampleID"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleconfig::superqxrf_has_program():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "program")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "program" in klass.__dict__:
            descriptor = klass.__dict__["program"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleconfig::superqxrf_has_anaProg():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "anaProg")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "anaProg" in klass.__dict__:
            descriptor = klass.__dict__["anaProg"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleconfig::superqxrf_has_seq_X():
    assert hasattr(MachineLibrary::CheckSampleConfig::SuperQXRF, "seq_X")
    descriptor = None
    for klass in MachineLibrary::CheckSampleConfig::SuperQXRF.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::insertremove::keywords::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::InsertRemove::Keywords::Host)


def test_machinelibrary::insertremove::keywords::host_constructor_exists():
    assert callable(MachineLibrary::InsertRemove::Keywords::Host.__init__)


def test_machinelibrary::insertremove::keywords::host_constructor_args():
    sig = inspect.signature(MachineLibrary::InsertRemove::Keywords::Host.__init__)
    params = list(sig.parameters.keys())
    assert "keywordKey" in params, "Missing parameter 'keywordKey'"
    assert "keywordValue" in params, "Missing parameter 'keywordValue'"

def test_machinelibrary::insertremove::keywords::host_has_keywordKey():
    assert hasattr(MachineLibrary::InsertRemove::Keywords::Host, "keywordKey")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Keywords::Host.__mro__:
        if "keywordKey" in klass.__dict__:
            descriptor = klass.__dict__["keywordKey"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::insertremove::keywords::host_has_keywordValue():
    assert hasattr(MachineLibrary::InsertRemove::Keywords::Host, "keywordValue")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Keywords::Host.__mro__:
        if "keywordValue" in klass.__dict__:
            descriptor = klass.__dict__["keywordValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::insertremove::types::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::InsertRemove::Types::Host)


def test_machinelibrary::insertremove::types::host_constructor_exists():
    assert callable(MachineLibrary::InsertRemove::Types::Host.__init__)


def test_machinelibrary::insertremove::types::host_constructor_args():
    sig = inspect.signature(MachineLibrary::InsertRemove::Types::Host.__init__)
    params = list(sig.parameters.keys())
    assert "typeNo" in params, "Missing parameter 'typeNo'"
    assert "typeValue" in params, "Missing parameter 'typeValue'"

def test_machinelibrary::insertremove::types::host_has_typeNo():
    assert hasattr(MachineLibrary::InsertRemove::Types::Host, "typeNo")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Types::Host.__mro__:
        if "typeNo" in klass.__dict__:
            descriptor = klass.__dict__["typeNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::insertremove::types::host_has_typeValue():
    assert hasattr(MachineLibrary::InsertRemove::Types::Host, "typeValue")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Types::Host.__mro__:
        if "typeValue" in klass.__dict__:
            descriptor = klass.__dict__["typeValue"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::insertremove::entry::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::InsertRemove::Entry::Host)


def test_machinelibrary::insertremove::entry::host_constructor_exists():
    assert callable(MachineLibrary::InsertRemove::Entry::Host.__init__)


def test_machinelibrary::insertremove::entry::host_constructor_args():
    sig = inspect.signature(MachineLibrary::InsertRemove::Entry::Host.__init__)
    params = list(sig.parameters.keys())
    assert "entryName" in params, "Missing parameter 'entryName'"
    assert "entryNo" in params, "Missing parameter 'entryNo'"

def test_machinelibrary::insertremove::entry::host_has_entryName():
    assert hasattr(MachineLibrary::InsertRemove::Entry::Host, "entryName")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Entry::Host.__mro__:
        if "entryName" in klass.__dict__:
            descriptor = klass.__dict__["entryName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::insertremove::entry::host_has_entryNo():
    assert hasattr(MachineLibrary::InsertRemove::Entry::Host, "entryNo")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Entry::Host.__mro__:
        if "entryNo" in klass.__dict__:
            descriptor = klass.__dict__["entryNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checksampleruntimeparams::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckSampleRunTimeParams::SuperQXRF)


def test_machinelibrary::checksampleruntimeparams::superqxrf_constructor_exists():
    assert callable(MachineLibrary::CheckSampleRunTimeParams::SuperQXRF.__init__)


def test_machinelibrary::checksampleruntimeparams::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckSampleRunTimeParams::SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "sampleType" in params, "Missing parameter 'sampleType'"

def test_machinelibrary::checksampleruntimeparams::superqxrf_has_value():
    assert hasattr(MachineLibrary::CheckSampleRunTimeParams::SuperQXRF, "value")
    descriptor = None
    for klass in MachineLibrary::CheckSampleRunTimeParams::SuperQXRF.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::checksampleruntimeparams::superqxrf_has_sampleType():
    assert hasattr(MachineLibrary::CheckSampleRunTimeParams::SuperQXRF, "sampleType")
    descriptor = None
    for klass in MachineLibrary::CheckSampleRunTimeParams::SuperQXRF.__mro__:
        if "sampleType" in klass.__dict__:
            descriptor = klass.__dict__["sampleType"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::oes::xrf::condition_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::OES::XRF::Condition)


def test_machinelibrary::oes::xrf::condition_constructor_exists():
    assert callable(MachineLibrary::OES::XRF::Condition.__init__)


def test_machinelibrary::oes::xrf::condition_constructor_args():
    sig = inspect.signature(MachineLibrary::OES::XRF::Condition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"
    assert "paraName" in params, "Missing parameter 'paraName'"
    assert "para" in params, "Missing parameter 'para'"

def test_machinelibrary::oes::xrf::condition_has_comment():
    assert hasattr(MachineLibrary::OES::XRF::Condition, "comment")
    descriptor = None
    for klass in MachineLibrary::OES::XRF::Condition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::oes::xrf::condition_has_seq_X():
    assert hasattr(MachineLibrary::OES::XRF::Condition, "seq_X")
    descriptor = None
    for klass in MachineLibrary::OES::XRF::Condition.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::oes::xrf::condition_has_paraName():
    assert hasattr(MachineLibrary::OES::XRF::Condition, "paraName")
    descriptor = None
    for klass in MachineLibrary::OES::XRF::Condition.__mro__:
        if "paraName" in klass.__dict__:
            descriptor = klass.__dict__["paraName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::oes::xrf::condition_has_para():
    assert hasattr(MachineLibrary::OES::XRF::Condition, "para")
    descriptor = None
    for klass in MachineLibrary::OES::XRF::Condition.__mro__:
        if "para" in klass.__dict__:
            descriptor = klass.__dict__["para"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::insertremove::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::InsertRemove::Host)


def test_machinelibrary::insertremove::host_constructor_exists():
    assert callable(MachineLibrary::InsertRemove::Host.__init__)


def test_machinelibrary::insertremove::host_constructor_args():
    sig = inspect.signature(MachineLibrary::InsertRemove::Host.__init__)
    params = list(sig.parameters.keys())
    assert "report_All" in params, "Missing parameter 'report_All'"

def test_machinelibrary::insertremove::host_has_report_All():
    assert hasattr(MachineLibrary::InsertRemove::Host, "report_All")
    descriptor = None
    for klass in MachineLibrary::InsertRemove::Host.__mro__:
        if "report_All" in klass.__dict__:
            descriptor = klass.__dict__["report_All"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::moved::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Moved::Host)


def test_machinelibrary::moved::host_constructor_exists():
    assert callable(MachineLibrary::Moved::Host.__init__)


def test_machinelibrary::moved::host_constructor_args():
    sig = inspect.signature(MachineLibrary::Moved::Host.__init__)
    params = list(sig.parameters.keys())
    assert "pos0" in params, "Missing parameter 'pos0'"
    assert "report_ALL" in params, "Missing parameter 'report_ALL'"
    assert "writePositionNameInFile" in params, "Missing parameter 'writePositionNameInFile'"
    assert "type0" in params, "Missing parameter 'type0'"

def test_machinelibrary::moved::host_has_pos0():
    assert hasattr(MachineLibrary::Moved::Host, "pos0")
    descriptor = None
    for klass in MachineLibrary::Moved::Host.__mro__:
        if "pos0" in klass.__dict__:
            descriptor = klass.__dict__["pos0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::moved::host_has_report_ALL():
    assert hasattr(MachineLibrary::Moved::Host, "report_ALL")
    descriptor = None
    for klass in MachineLibrary::Moved::Host.__mro__:
        if "report_ALL" in klass.__dict__:
            descriptor = klass.__dict__["report_ALL"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::moved::host_has_writePositionNameInFile():
    assert hasattr(MachineLibrary::Moved::Host, "writePositionNameInFile")
    descriptor = None
    for klass in MachineLibrary::Moved::Host.__mro__:
        if "writePositionNameInFile" in klass.__dict__:
            descriptor = klass.__dict__["writePositionNameInFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::moved::host_has_type0():
    assert hasattr(MachineLibrary::Moved::Host, "type0")
    descriptor = None
    for klass in MachineLibrary::Moved::Host.__mro__:
        if "type0" in klass.__dict__:
            descriptor = klass.__dict__["type0"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::ws::update::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::WS::Update::Host)


def test_machinelibrary::ws::update::host_constructor_exists():
    assert callable(MachineLibrary::WS::Update::Host.__init__)


def test_machinelibrary::ws::update::host_constructor_args():
    sig = inspect.signature(MachineLibrary::WS::Update::Host.__init__)
    params = list(sig.parameters.keys())
    assert "AllowUnit0" in params, "Missing parameter 'AllowUnit0'"
    assert "checkUnit" in params, "Missing parameter 'checkUnit'"

def test_machinelibrary::ws::update::host_has_AllowUnit0():
    assert hasattr(MachineLibrary::WS::Update::Host, "AllowUnit0")
    descriptor = None
    for klass in MachineLibrary::WS::Update::Host.__mro__:
        if "AllowUnit0" in klass.__dict__:
            descriptor = klass.__dict__["AllowUnit0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ws::update::host_has_checkUnit():
    assert hasattr(MachineLibrary::WS::Update::Host, "checkUnit")
    descriptor = None
    for klass in MachineLibrary::WS::Update::Host.__mro__:
        if "checkUnit" in klass.__dict__:
            descriptor = klass.__dict__["checkUnit"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::report::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Report::Host)


def test_machinelibrary::report::host_constructor_exists():
    assert callable(MachineLibrary::Report::Host.__init__)


def test_machinelibrary::report::host_constructor_args():
    sig = inspect.signature(MachineLibrary::Report::Host.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"
    assert "stateChanged" in params, "Missing parameter 'stateChanged'"
    assert "maxType" in params, "Missing parameter 'maxType'"
    assert "timeStamp" in params, "Missing parameter 'timeStamp'"
    assert "sampleInsert" in params, "Missing parameter 'sampleInsert'"
    assert "sendErrorWarningsMsgOnly" in params, "Missing parameter 'sendErrorWarningsMsgOnly'"
    assert "sendLifeMessages" in params, "Missing parameter 'sendLifeMessages'"
    assert "note" in params, "Missing parameter 'note'"
    assert "note1" in params, "Missing parameter 'note1'"
    assert "minType" in params, "Missing parameter 'minType'"
    assert "sampleMoved" in params, "Missing parameter 'sampleMoved'"
    assert "internal" in params, "Missing parameter 'internal'"
    assert "sampleRemoved" in params, "Missing parameter 'sampleRemoved'"
    assert "rawData" in params, "Missing parameter 'rawData'"

def test_machinelibrary::report::host_has_fileName():
    assert hasattr(MachineLibrary::Report::Host, "fileName")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_stateChanged():
    assert hasattr(MachineLibrary::Report::Host, "stateChanged")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "stateChanged" in klass.__dict__:
            descriptor = klass.__dict__["stateChanged"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_maxType():
    assert hasattr(MachineLibrary::Report::Host, "maxType")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "maxType" in klass.__dict__:
            descriptor = klass.__dict__["maxType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_timeStamp():
    assert hasattr(MachineLibrary::Report::Host, "timeStamp")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "timeStamp" in klass.__dict__:
            descriptor = klass.__dict__["timeStamp"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_sampleInsert():
    assert hasattr(MachineLibrary::Report::Host, "sampleInsert")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "sampleInsert" in klass.__dict__:
            descriptor = klass.__dict__["sampleInsert"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_sendErrorWarningsMsgOnly():
    assert hasattr(MachineLibrary::Report::Host, "sendErrorWarningsMsgOnly")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "sendErrorWarningsMsgOnly" in klass.__dict__:
            descriptor = klass.__dict__["sendErrorWarningsMsgOnly"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_sendLifeMessages():
    assert hasattr(MachineLibrary::Report::Host, "sendLifeMessages")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "sendLifeMessages" in klass.__dict__:
            descriptor = klass.__dict__["sendLifeMessages"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_note():
    assert hasattr(MachineLibrary::Report::Host, "note")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_note1():
    assert hasattr(MachineLibrary::Report::Host, "note1")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "note1" in klass.__dict__:
            descriptor = klass.__dict__["note1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_minType():
    assert hasattr(MachineLibrary::Report::Host, "minType")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "minType" in klass.__dict__:
            descriptor = klass.__dict__["minType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_sampleMoved():
    assert hasattr(MachineLibrary::Report::Host, "sampleMoved")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "sampleMoved" in klass.__dict__:
            descriptor = klass.__dict__["sampleMoved"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_internal():
    assert hasattr(MachineLibrary::Report::Host, "internal")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "internal" in klass.__dict__:
            descriptor = klass.__dict__["internal"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_sampleRemoved():
    assert hasattr(MachineLibrary::Report::Host, "sampleRemoved")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "sampleRemoved" in klass.__dict__:
            descriptor = klass.__dict__["sampleRemoved"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::report::host_has_rawData():
    assert hasattr(MachineLibrary::Report::Host, "rawData")
    descriptor = None
    for klass in MachineLibrary::Report::Host.__mro__:
        if "rawData" in klass.__dict__:
            descriptor = klass.__dict__["rawData"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::settings::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Settings::ARL::XRF::OES)


def test_machinelibrary::settings::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::Settings::ARL::XRF::OES.__init__)


def test_machinelibrary::settings::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::Settings::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::settings::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::Settings::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::Settings::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::disablesct::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::DisableSCT::ARL::XRF::OES)


def test_machinelibrary::disablesct::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::DisableSCT::ARL::XRF::OES.__init__)


def test_machinelibrary::disablesct::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::DisableSCT::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::disablesct::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::DisableSCT::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::DisableSCT::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::exeaskprepunit::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES)


def test_machinelibrary::exeaskprepunit::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES.__init__)


def test_machinelibrary::exeaskprepunit::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::exeaskprepunit::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checkaskprepunit::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES)


def test_machinelibrary::checkaskprepunit::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES.__init__)


def test_machinelibrary::checkaskprepunit::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::checkaskprepunit::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::exeprepunit::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ExePrepUnit::ARL::XRF::OES)


def test_machinelibrary::exeprepunit::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::ExePrepUnit::ARL::XRF::OES.__init__)


def test_machinelibrary::exeprepunit::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::ExePrepUnit::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::exeprepunit::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::ExePrepUnit::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::ExePrepUnit::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checkreqprepunit::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES)


def test_machinelibrary::checkreqprepunit::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES.__init__)


def test_machinelibrary::checkreqprepunit::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::checkreqprepunit::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::executefiling::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ExecuteFiling::ARL::XRF::OES)


def test_machinelibrary::executefiling::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::ExecuteFiling::ARL::XRF::OES.__init__)


def test_machinelibrary::executefiling::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::ExecuteFiling::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::executefiling::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::ExecuteFiling::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::ExecuteFiling::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checkfilling::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckFilling::ARL::XRF::OES)


def test_machinelibrary::checkfilling::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::CheckFilling::ARL::XRF::OES.__init__)


def test_machinelibrary::checkfilling::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckFilling::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::checkfilling::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::CheckFilling::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::CheckFilling::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checksample::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckSample::SuperQXRF)


def test_machinelibrary::checksample::superqxrf_constructor_exists():
    assert callable(MachineLibrary::CheckSample::SuperQXRF.__init__)


def test_machinelibrary::checksample::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckSample::SuperQXRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::checksampleruntime::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckSampleRunTime::SuperQXRF)


def test_machinelibrary::checksampleruntime::superqxrf_constructor_exists():
    assert callable(MachineLibrary::CheckSampleRunTime::SuperQXRF.__init__)


def test_machinelibrary::checksampleruntime::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckSampleRunTime::SuperQXRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::communication::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Communication::SuperQXRF)


def test_machinelibrary::communication::superqxrf_constructor_exists():
    assert callable(MachineLibrary::Communication::SuperQXRF.__init__)


def test_machinelibrary::communication::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::Communication::SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "enq_ACK_Protocol" in params, "Missing parameter 'enq_ACK_Protocol'"

def test_machinelibrary::communication::superqxrf_has_enq_ACK_Protocol():
    assert hasattr(MachineLibrary::Communication::SuperQXRF, "enq_ACK_Protocol")
    descriptor = None
    for klass in MachineLibrary::Communication::SuperQXRF.__mro__:
        if "enq_ACK_Protocol" in klass.__dict__:
            descriptor = klass.__dict__["enq_ACK_Protocol"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::controlsamples::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ControlSamples::SuperQXRF)


def test_machinelibrary::controlsamples::superqxrf_constructor_exists():
    assert callable(MachineLibrary::ControlSamples::SuperQXRF.__init__)


def test_machinelibrary::controlsamples::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::ControlSamples::SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "outOfControl" in params, "Missing parameter 'outOfControl'"

def test_machinelibrary::controlsamples::superqxrf_has_outOfControl():
    assert hasattr(MachineLibrary::ControlSamples::SuperQXRF, "outOfControl")
    descriptor = None
    for klass in MachineLibrary::ControlSamples::SuperQXRF.__mro__:
        if "outOfControl" in klass.__dict__:
            descriptor = klass.__dict__["outOfControl"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::file::sample::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::File::Sample::ARL::XRF::OES)


def test_machinelibrary::file::sample::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::File::Sample::ARL::XRF::OES.__init__)


def test_machinelibrary::file::sample::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::File::Sample::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "noSuccess" in params, "Missing parameter 'noSuccess'"

def test_machinelibrary::file::sample::arl::xrf::oes_has_noSuccess():
    assert hasattr(MachineLibrary::File::Sample::ARL::XRF::OES, "noSuccess")
    descriptor = None
    for klass in MachineLibrary::File::Sample::ARL::XRF::OES.__mro__:
        if "noSuccess" in klass.__dict__:
            descriptor = klass.__dict__["noSuccess"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::ps::process::finished::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::PS::Process::Finished::ARL::XRF::OES)


def test_machinelibrary::ps::process::finished::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::PS::Process::Finished::ARL::XRF::OES.__init__)


def test_machinelibrary::ps::process::finished::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::PS::Process::Finished::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "noSuccess" in params, "Missing parameter 'noSuccess'"

def test_machinelibrary::ps::process::finished::arl::xrf::oes_has_noSuccess():
    assert hasattr(MachineLibrary::PS::Process::Finished::ARL::XRF::OES, "noSuccess")
    descriptor = None
    for klass in MachineLibrary::PS::Process::Finished::ARL::XRF::OES.__mro__:
        if "noSuccess" in klass.__dict__:
            descriptor = klass.__dict__["noSuccess"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::generalsetting::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::GeneralSetting::ARL::XRF::OES)


def test_machinelibrary::generalsetting::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::GeneralSetting::ARL::XRF::OES.__init__)


def test_machinelibrary::generalsetting::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::GeneralSetting::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::generalsetting::arl::xrf::oes_has_name():
    assert hasattr(MachineLibrary::GeneralSetting::ARL::XRF::OES, "name")
    descriptor = None
    for klass in MachineLibrary::GeneralSetting::ARL::XRF::OES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::checkaddsid::pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CheckAddSID::PM2PM)


def test_machinelibrary::checkaddsid::pm2pm_constructor_exists():
    assert callable(MachineLibrary::CheckAddSID::PM2PM.__init__)


def test_machinelibrary::checkaddsid::pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary::CheckAddSID::PM2PM.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::sepbycomma::scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::SepByComma::Scanner)


def test_machinelibrary::sepbycomma::scanner_constructor_exists():
    assert callable(MachineLibrary::SepByComma::Scanner.__init__)


def test_machinelibrary::sepbycomma::scanner_constructor_args():
    sig = inspect.signature(MachineLibrary::SepByComma::Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "activ" in params, "Missing parameter 'activ'"
    assert "preDefWS" in params, "Missing parameter 'preDefWS'"

def test_machinelibrary::sepbycomma::scanner_has_activ():
    assert hasattr(MachineLibrary::SepByComma::Scanner, "activ")
    descriptor = None
    for klass in MachineLibrary::SepByComma::Scanner.__mro__:
        if "activ" in klass.__dict__:
            descriptor = klass.__dict__["activ"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::sepbycomma::scanner_has_preDefWS():
    assert hasattr(MachineLibrary::SepByComma::Scanner, "preDefWS")
    descriptor = None
    for klass in MachineLibrary::SepByComma::Scanner.__mro__:
        if "preDefWS" in klass.__dict__:
            descriptor = klass.__dict__["preDefWS"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::history::accupycmeter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::History::AccuPycMeter)


def test_machinelibrary::history::accupycmeter_constructor_exists():
    assert callable(MachineLibrary::History::AccuPycMeter.__init__)


def test_machinelibrary::history::accupycmeter_constructor_args():
    sig = inspect.signature(MachineLibrary::History::AccuPycMeter.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitconfig::host_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitConfig::Host)


def test_machinelibrary::unitconfig::host_constructor_exists():
    assert callable(MachineLibrary::UnitConfig::Host.__init__)


def test_machinelibrary::unitconfig::host_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitConfig::Host.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitconfig::arl::xrf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitConfig::ARL::XRF::OES)


def test_machinelibrary::unitconfig::arl::xrf::oes_constructor_exists():
    assert callable(MachineLibrary::UnitConfig::ARL::XRF::OES.__init__)


def test_machinelibrary::unitconfig::arl::xrf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitConfig::ARL::XRF::OES.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitconfig::superq::xrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitConfig::SuperQ::XRF)


def test_machinelibrary::unitconfig::superq::xrf_constructor_exists():
    assert callable(MachineLibrary::UnitConfig::SuperQ::XRF.__init__)


def test_machinelibrary::unitconfig::superq::xrf_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitConfig::SuperQ::XRF.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitconfig::oblf::oes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitConfig::OBLF::OES)


def test_machinelibrary::unitconfig::oblf::oes_constructor_exists():
    assert callable(MachineLibrary::UnitConfig::OBLF::OES.__init__)


def test_machinelibrary::unitconfig::oblf::oes_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitConfig::OBLF::OES.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitconfig::terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitConfig::Terminal)


def test_machinelibrary::unitconfig::terminal_constructor_exists():
    assert callable(MachineLibrary::UnitConfig::Terminal.__init__)


def test_machinelibrary::unitconfig::terminal_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitConfig::Terminal.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::generalparameter::superqxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::GeneralParameter::SuperQXRF)


def test_machinelibrary::generalparameter::superqxrf_constructor_exists():
    assert callable(MachineLibrary::GeneralParameter::SuperQXRF.__init__)


def test_machinelibrary::generalparameter::superqxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::GeneralParameter::SuperQXRF.__init__)
    params = list(sig.parameters.keys())
    assert "listName" in params, "Missing parameter 'listName'"
    assert "switchRemote" in params, "Missing parameter 'switchRemote'"
    assert "startList" in params, "Missing parameter 'startList'"

def test_machinelibrary::generalparameter::superqxrf_has_listName():
    assert hasattr(MachineLibrary::GeneralParameter::SuperQXRF, "listName")
    descriptor = None
    for klass in MachineLibrary::GeneralParameter::SuperQXRF.__mro__:
        if "listName" in klass.__dict__:
            descriptor = klass.__dict__["listName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::generalparameter::superqxrf_has_switchRemote():
    assert hasattr(MachineLibrary::GeneralParameter::SuperQXRF, "switchRemote")
    descriptor = None
    for klass in MachineLibrary::GeneralParameter::SuperQXRF.__mro__:
        if "switchRemote" in klass.__dict__:
            descriptor = klass.__dict__["switchRemote"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::generalparameter::superqxrf_has_startList():
    assert hasattr(MachineLibrary::GeneralParameter::SuperQXRF, "startList")
    descriptor = None
    for klass in MachineLibrary::GeneralParameter::SuperQXRF.__mro__:
        if "startList" in klass.__dict__:
            descriptor = klass.__dict__["startList"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::errormessage::oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::ErrorMessage::OBLFOES)


def test_machinelibrary::errormessage::oblfoes_constructor_exists():
    assert callable(MachineLibrary::ErrorMessage::OBLFOES.__init__)


def test_machinelibrary::errormessage::oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary::ErrorMessage::OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "errorMessage" in params, "Missing parameter 'errorMessage'"

def test_machinelibrary::errormessage::oblfoes_has_errorMessage():
    assert hasattr(MachineLibrary::ErrorMessage::OBLFOES, "errorMessage")
    descriptor = None
    for klass in MachineLibrary::ErrorMessage::OBLFOES.__mro__:
        if "errorMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorMessage"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::recalrequest::oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::RecalRequest::OBLFOES)


def test_machinelibrary::recalrequest::oblfoes_constructor_exists():
    assert callable(MachineLibrary::RecalRequest::OBLFOES.__init__)


def test_machinelibrary::recalrequest::oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary::RecalRequest::OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::recalrequest::oblfoes_has_name():
    assert hasattr(MachineLibrary::RecalRequest::OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary::RecalRequest::OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::testrequest::oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::TestRequest::OBLFOES)


def test_machinelibrary::testrequest::oblfoes_constructor_exists():
    assert callable(MachineLibrary::TestRequest::OBLFOES.__init__)


def test_machinelibrary::testrequest::oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary::TestRequest::OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::testrequest::oblfoes_has_name():
    assert hasattr(MachineLibrary::TestRequest::OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary::TestRequest::OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::outputrequest::oblfoes_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::OutputRequest::OBLFOES)


def test_machinelibrary::outputrequest::oblfoes_constructor_exists():
    assert callable(MachineLibrary::OutputRequest::OBLFOES.__init__)


def test_machinelibrary::outputrequest::oblfoes_constructor_args():
    sig = inspect.signature(MachineLibrary::OutputRequest::OBLFOES.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_machinelibrary::outputrequest::oblfoes_has_name():
    assert hasattr(MachineLibrary::OutputRequest::OBLFOES, "name")
    descriptor = None
    for klass in MachineLibrary::OutputRequest::OBLFOES.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::translate::terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Translate::Terminal)


def test_machinelibrary::translate::terminal_constructor_exists():
    assert callable(MachineLibrary::Translate::Terminal.__init__)


def test_machinelibrary::translate::terminal_constructor_args():
    sig = inspect.signature(MachineLibrary::Translate::Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "auto_Ready" in params, "Missing parameter 'auto_Ready'"
    assert "man_Ready" in params, "Missing parameter 'man_Ready'"
    assert "man_Busy" in params, "Missing parameter 'man_Busy'"
    assert "auto_Busy" in params, "Missing parameter 'auto_Busy'"

def test_machinelibrary::translate::terminal_has_auto_Ready():
    assert hasattr(MachineLibrary::Translate::Terminal, "auto_Ready")
    descriptor = None
    for klass in MachineLibrary::Translate::Terminal.__mro__:
        if "auto_Ready" in klass.__dict__:
            descriptor = klass.__dict__["auto_Ready"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::translate::terminal_has_man_Ready():
    assert hasattr(MachineLibrary::Translate::Terminal, "man_Ready")
    descriptor = None
    for klass in MachineLibrary::Translate::Terminal.__mro__:
        if "man_Ready" in klass.__dict__:
            descriptor = klass.__dict__["man_Ready"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::translate::terminal_has_man_Busy():
    assert hasattr(MachineLibrary::Translate::Terminal, "man_Busy")
    descriptor = None
    for klass in MachineLibrary::Translate::Terminal.__mro__:
        if "man_Busy" in klass.__dict__:
            descriptor = klass.__dict__["man_Busy"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::translate::terminal_has_auto_Busy():
    assert hasattr(MachineLibrary::Translate::Terminal, "auto_Busy")
    descriptor = None
    for klass in MachineLibrary::Translate::Terminal.__mro__:
        if "auto_Busy" in klass.__dict__:
            descriptor = klass.__dict__["auto_Busy"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::scanner_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::Scanner)


def test_machinelibrary::unitgeneral::scanner_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::Scanner.__init__)


def test_machinelibrary::unitgeneral::scanner_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::Scanner.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "length" in params, "Missing parameter 'length'"
    assert "preString" in params, "Missing parameter 'preString'"
    assert "registerSample" in params, "Missing parameter 'registerSample'"
    assert "forcedSampleType" in params, "Missing parameter 'forcedSampleType'"
    assert "fillWith" in params, "Missing parameter 'fillWith'"
    assert "addString" in params, "Missing parameter 'addString'"

def test_machinelibrary::unitgeneral::scanner_has_start():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "start")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_length():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "length")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_preString():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "preString")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "preString" in klass.__dict__:
            descriptor = klass.__dict__["preString"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_registerSample():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "registerSample")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "registerSample" in klass.__dict__:
            descriptor = klass.__dict__["registerSample"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_forcedSampleType():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "forcedSampleType")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "forcedSampleType" in klass.__dict__:
            descriptor = klass.__dict__["forcedSampleType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_fillWith():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "fillWith")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "fillWith" in klass.__dict__:
            descriptor = klass.__dict__["fillWith"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::scanner_has_addString():
    assert hasattr(MachineLibrary::UnitGeneral::Scanner, "addString")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Scanner.__mro__:
        if "addString" in klass.__dict__:
            descriptor = klass.__dict__["addString"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::rigakuxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::RigakuXRF)


def test_machinelibrary::unitgeneral::rigakuxrf_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::RigakuXRF.__init__)


def test_machinelibrary::unitgeneral::rigakuxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::RigakuXRF.__init__)
    params = list(sig.parameters.keys())
    assert "lastPoHAG_SIInstrument" in params, "Missing parameter 'lastPoHAG_SIInstrument'"
    assert "lastPosInInstrument" in params, "Missing parameter 'lastPosInInstrument'"
    assert "separator" in params, "Missing parameter 'separator'"
    assert "lastPosAnalyHAG_SIg" in params, "Missing parameter 'lastPosAnalyHAG_SIg'"

def test_machinelibrary::unitgeneral::rigakuxrf_has_lastPoHAG_SIInstrument():
    assert hasattr(MachineLibrary::UnitGeneral::RigakuXRF, "lastPoHAG_SIInstrument")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::RigakuXRF.__mro__:
        if "lastPoHAG_SIInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPoHAG_SIInstrument"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::rigakuxrf_has_lastPosInInstrument():
    assert hasattr(MachineLibrary::UnitGeneral::RigakuXRF, "lastPosInInstrument")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::RigakuXRF.__mro__:
        if "lastPosInInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPosInInstrument"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::rigakuxrf_has_separator():
    assert hasattr(MachineLibrary::UnitGeneral::RigakuXRF, "separator")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::RigakuXRF.__mro__:
        if "separator" in klass.__dict__:
            descriptor = klass.__dict__["separator"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::rigakuxrf_has_lastPosAnalyHAG_SIg():
    assert hasattr(MachineLibrary::UnitGeneral::RigakuXRF, "lastPosAnalyHAG_SIg")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::RigakuXRF.__mro__:
        if "lastPosAnalyHAG_SIg" in klass.__dict__:
            descriptor = klass.__dict__["lastPosAnalyHAG_SIg"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::superq_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::SuperQ)


def test_machinelibrary::unitgeneral::superq_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::SuperQ.__init__)


def test_machinelibrary::unitgeneral::superq_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::SuperQ.__init__)
    params = list(sig.parameters.keys())
    assert "lastPosAnalysing" in params, "Missing parameter 'lastPosAnalysing'"
    assert "lastPosInInstrument" in params, "Missing parameter 'lastPosInInstrument'"

def test_machinelibrary::unitgeneral::superq_has_lastPosAnalysing():
    assert hasattr(MachineLibrary::UnitGeneral::SuperQ, "lastPosAnalysing")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::SuperQ.__mro__:
        if "lastPosAnalysing" in klass.__dict__:
            descriptor = klass.__dict__["lastPosAnalysing"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::superq_has_lastPosInInstrument():
    assert hasattr(MachineLibrary::UnitGeneral::SuperQ, "lastPosInInstrument")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::SuperQ.__mro__:
        if "lastPosInInstrument" in klass.__dict__:
            descriptor = klass.__dict__["lastPosInInstrument"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::accpyc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::AccPyc)


def test_machinelibrary::unitgeneral::accpyc_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::AccPyc.__init__)


def test_machinelibrary::unitgeneral::accpyc_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::AccPyc.__init__)
    params = list(sig.parameters.keys())
    assert "minSampleWeight" in params, "Missing parameter 'minSampleWeight'"
    assert "cupWeight" in params, "Missing parameter 'cupWeight'"

def test_machinelibrary::unitgeneral::accpyc_has_minSampleWeight():
    assert hasattr(MachineLibrary::UnitGeneral::AccPyc, "minSampleWeight")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::AccPyc.__mro__:
        if "minSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["minSampleWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::accpyc_has_cupWeight():
    assert hasattr(MachineLibrary::UnitGeneral::AccPyc, "cupWeight")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::AccPyc.__mro__:
        if "cupWeight" in klass.__dict__:
            descriptor = klass.__dict__["cupWeight"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::PM2PM)


def test_machinelibrary::unitgeneral::pm2pm_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::PM2PM.__init__)


def test_machinelibrary::unitgeneral::pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "processFeedBack" in params, "Missing parameter 'processFeedBack'"
    assert "sid_Mask" in params, "Missing parameter 'sid_Mask'"

def test_machinelibrary::unitgeneral::pm2pm_has_processFeedBack():
    assert hasattr(MachineLibrary::UnitGeneral::PM2PM, "processFeedBack")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::PM2PM.__mro__:
        if "processFeedBack" in klass.__dict__:
            descriptor = klass.__dict__["processFeedBack"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::pm2pm_has_sid_Mask():
    assert hasattr(MachineLibrary::UnitGeneral::PM2PM, "sid_Mask")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::PM2PM.__mro__:
        if "sid_Mask" in klass.__dict__:
            descriptor = klass.__dict__["sid_Mask"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::remote_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::Remote)


def test_machinelibrary::unitgeneral::remote_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::Remote.__init__)


def test_machinelibrary::unitgeneral::remote_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::Remote.__init__)
    params = list(sig.parameters.keys())
    assert "handshakeA" in params, "Missing parameter 'handshakeA'"
    assert "handshakeQ" in params, "Missing parameter 'handshakeQ'"
    assert "handshakeT" in params, "Missing parameter 'handshakeT'"
    assert "editWSDB" in params, "Missing parameter 'editWSDB'"

def test_machinelibrary::unitgeneral::remote_has_handshakeA():
    assert hasattr(MachineLibrary::UnitGeneral::Remote, "handshakeA")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Remote.__mro__:
        if "handshakeA" in klass.__dict__:
            descriptor = klass.__dict__["handshakeA"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::remote_has_handshakeQ():
    assert hasattr(MachineLibrary::UnitGeneral::Remote, "handshakeQ")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Remote.__mro__:
        if "handshakeQ" in klass.__dict__:
            descriptor = klass.__dict__["handshakeQ"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::remote_has_handshakeT():
    assert hasattr(MachineLibrary::UnitGeneral::Remote, "handshakeT")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Remote.__mro__:
        if "handshakeT" in klass.__dict__:
            descriptor = klass.__dict__["handshakeT"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::remote_has_editWSDB():
    assert hasattr(MachineLibrary::UnitGeneral::Remote, "editWSDB")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Remote.__mro__:
        if "editWSDB" in klass.__dict__:
            descriptor = klass.__dict__["editWSDB"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::hostpc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::HostPC)


def test_machinelibrary::unitgeneral::hostpc_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::HostPC.__init__)


def test_machinelibrary::unitgeneral::hostpc_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::HostPC.__init__)
    params = list(sig.parameters.keys())
    assert "writeDumyIfNoDataExist" in params, "Missing parameter 'writeDumyIfNoDataExist'"
    assert "replyOnLink" in params, "Missing parameter 'replyOnLink'"
    assert "index" in params, "Missing parameter 'index'"
    assert "maxIndex" in params, "Missing parameter 'maxIndex'"

def test_machinelibrary::unitgeneral::hostpc_has_writeDumyIfNoDataExist():
    assert hasattr(MachineLibrary::UnitGeneral::HostPC, "writeDumyIfNoDataExist")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::HostPC.__mro__:
        if "writeDumyIfNoDataExist" in klass.__dict__:
            descriptor = klass.__dict__["writeDumyIfNoDataExist"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::hostpc_has_replyOnLink():
    assert hasattr(MachineLibrary::UnitGeneral::HostPC, "replyOnLink")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::HostPC.__mro__:
        if "replyOnLink" in klass.__dict__:
            descriptor = klass.__dict__["replyOnLink"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::hostpc_has_index():
    assert hasattr(MachineLibrary::UnitGeneral::HostPC, "index")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::HostPC.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::hostpc_has_maxIndex():
    assert hasattr(MachineLibrary::UnitGeneral::HostPC, "maxIndex")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::HostPC.__mro__:
        if "maxIndex" in klass.__dict__:
            descriptor = klass.__dict__["maxIndex"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneral::terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral::Terminal)


def test_machinelibrary::unitgeneral::terminal_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral::Terminal.__init__)


def test_machinelibrary::unitgeneral::terminal_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral::Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "station5" in params, "Missing parameter 'station5'"
    assert "station3" in params, "Missing parameter 'station3'"
    assert "thisStation" in params, "Missing parameter 'thisStation'"
    assert "station1" in params, "Missing parameter 'station1'"
    assert "station4" in params, "Missing parameter 'station4'"
    assert "station2" in params, "Missing parameter 'station2'"

def test_machinelibrary::unitgeneral::terminal_has_station5():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "station5")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "station5" in klass.__dict__:
            descriptor = klass.__dict__["station5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::terminal_has_station3():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "station3")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "station3" in klass.__dict__:
            descriptor = klass.__dict__["station3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::terminal_has_thisStation():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "thisStation")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "thisStation" in klass.__dict__:
            descriptor = klass.__dict__["thisStation"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::terminal_has_station1():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "station1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "station1" in klass.__dict__:
            descriptor = klass.__dict__["station1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::terminal_has_station4():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "station4")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "station4" in klass.__dict__:
            descriptor = klass.__dict__["station4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneral::terminal_has_station2():
    assert hasattr(MachineLibrary::UnitGeneral::Terminal, "station2")
    descriptor = None
    for klass in MachineLibrary::UnitGeneral::Terminal.__mro__:
        if "station2" in klass.__dict__:
            descriptor = klass.__dict__["station2"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::plctopmmatrix_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::PLCtoPmMatrix)


def test_machinelibrary::plctopmmatrix_constructor_exists():
    assert callable(MachineLibrary::PLCtoPmMatrix.__init__)


def test_machinelibrary::plctopmmatrix_constructor_args():
    sig = inspect.signature(MachineLibrary::PLCtoPmMatrix.__init__)
    params = list(sig.parameters.keys())
    assert "plcpmmatrixBit0" in params, "Missing parameter 'plcpmmatrixBit0'"
    assert "plcpmmatrixBit15" in params, "Missing parameter 'plcpmmatrixBit15'"
    assert "plcpmmatrixBit2" in params, "Missing parameter 'plcpmmatrixBit2'"
    assert "plcpmmatrixBit7" in params, "Missing parameter 'plcpmmatrixBit7'"
    assert "plcpmmatrixBit9" in params, "Missing parameter 'plcpmmatrixBit9'"
    assert "plcpmmatrixBit11" in params, "Missing parameter 'plcpmmatrixBit11'"
    assert "plcpmmatrixBit13" in params, "Missing parameter 'plcpmmatrixBit13'"
    assert "plcpmmatrixBit6" in params, "Missing parameter 'plcpmmatrixBit6'"
    assert "plcpmmatrixBit12" in params, "Missing parameter 'plcpmmatrixBit12'"
    assert "plcpmmatrixBit1" in params, "Missing parameter 'plcpmmatrixBit1'"
    assert "plcpmmatrixBit14" in params, "Missing parameter 'plcpmmatrixBit14'"
    assert "plcpmmatrixBit3" in params, "Missing parameter 'plcpmmatrixBit3'"
    assert "plcpmmatrixBit8" in params, "Missing parameter 'plcpmmatrixBit8'"
    assert "plcpmmatrixBit4" in params, "Missing parameter 'plcpmmatrixBit4'"
    assert "plcpmmatrixBit5" in params, "Missing parameter 'plcpmmatrixBit5'"
    assert "plcpmmatrixBit10" in params, "Missing parameter 'plcpmmatrixBit10'"

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit0():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit0")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit0" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit0"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit15():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit15")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit15" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit15"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit2():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit2")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit2" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit7():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit7")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit7" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit7"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit9():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit9")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit9" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit9"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit11():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit11")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit11" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit11"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit13():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit13")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit13" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit13"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit6():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit6")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit6" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit12():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit12")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit12" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit12"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit1():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit1")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit1" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit14():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit14")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit14" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit14"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit3():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit3")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit3" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit8():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit8")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit8" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit8"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit4():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit4")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit4" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit5():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit5")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit5" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::plctopmmatrix_has_plcpmmatrixBit10():
    assert hasattr(MachineLibrary::PLCtoPmMatrix, "plcpmmatrixBit10")
    descriptor = None
    for klass in MachineLibrary::PLCtoPmMatrix.__mro__:
        if "plcpmmatrixBit10" in klass.__dict__:
            descriptor = klass.__dict__["plcpmmatrixBit10"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::stausbits_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::StausBits)


def test_machinelibrary::stausbits_constructor_exists():
    assert callable(MachineLibrary::StausBits.__init__)


def test_machinelibrary::stausbits_constructor_args():
    sig = inspect.signature(MachineLibrary::StausBits.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::positions_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Positions)


def test_machinelibrary::positions_constructor_exists():
    assert callable(MachineLibrary::Positions.__init__)


def test_machinelibrary::positions_constructor_args():
    sig = inspect.signature(MachineLibrary::Positions.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::winccaddtag_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::WinCCAddTag)


def test_machinelibrary::winccaddtag_constructor_exists():
    assert callable(MachineLibrary::WinCCAddTag.__init__)


def test_machinelibrary::winccaddtag_constructor_args():
    sig = inspect.signature(MachineLibrary::WinCCAddTag.__init__)
    params = list(sig.parameters.keys())
    assert "winCCTag" in params, "Missing parameter 'winCCTag'"

def test_machinelibrary::winccaddtag_has_winCCTag():
    assert hasattr(MachineLibrary::WinCCAddTag, "winCCTag")
    descriptor = None
    for klass in MachineLibrary::WinCCAddTag.__mro__:
        if "winCCTag" in klass.__dict__:
            descriptor = klass.__dict__["winCCTag"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitgeneralparameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneralParameters)


def test_machinelibrary::unitgeneralparameters_constructor_exists():
    assert callable(MachineLibrary::UnitGeneralParameters.__init__)


def test_machinelibrary::unitgeneralparameters_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneralParameters.__init__)
    params = list(sig.parameters.keys())
    assert "minValue_1" in params, "Missing parameter 'minValue_1'"
    assert "UseWith_1" in params, "Missing parameter 'UseWith_1'"
    assert "defaultValue_1" in params, "Missing parameter 'defaultValue_1'"
    assert "unit_1" in params, "Missing parameter 'unit_1'"
    assert "seq_X" in params, "Missing parameter 'seq_X'"
    assert "comment_1" in params, "Missing parameter 'comment_1'"
    assert "canBeChange_1" in params, "Missing parameter 'canBeChange_1'"
    assert "maxValue_1" in params, "Missing parameter 'maxValue_1'"
    assert "KeyWord_1" in params, "Missing parameter 'KeyWord_1'"
    assert "paraName_1" in params, "Missing parameter 'paraName_1'"
    assert "visibleType_1" in params, "Missing parameter 'visibleType_1'"

def test_machinelibrary::unitgeneralparameters_has_minValue_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "minValue_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "minValue_1" in klass.__dict__:
            descriptor = klass.__dict__["minValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_UseWith_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "UseWith_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "UseWith_1" in klass.__dict__:
            descriptor = klass.__dict__["UseWith_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_defaultValue_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "defaultValue_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "defaultValue_1" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_unit_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "unit_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "unit_1" in klass.__dict__:
            descriptor = klass.__dict__["unit_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_seq_X():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "seq_X")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "seq_X" in klass.__dict__:
            descriptor = klass.__dict__["seq_X"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_comment_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "comment_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "comment_1" in klass.__dict__:
            descriptor = klass.__dict__["comment_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_canBeChange_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "canBeChange_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "canBeChange_1" in klass.__dict__:
            descriptor = klass.__dict__["canBeChange_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_maxValue_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "maxValue_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "maxValue_1" in klass.__dict__:
            descriptor = klass.__dict__["maxValue_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_KeyWord_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "KeyWord_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "KeyWord_1" in klass.__dict__:
            descriptor = klass.__dict__["KeyWord_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_paraName_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "paraName_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "paraName_1" in klass.__dict__:
            descriptor = klass.__dict__["paraName_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::unitgeneralparameters_has_visibleType_1():
    assert hasattr(MachineLibrary::UnitGeneralParameters, "visibleType_1")
    descriptor = None
    for klass in MachineLibrary::UnitGeneralParameters.__mro__:
        if "visibleType_1" in klass.__dict__:
            descriptor = klass.__dict__["visibleType_1"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::unitspecialconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitSpecialConfiguration)


def test_machinelibrary::unitspecialconfiguration_constructor_exists():
    assert callable(MachineLibrary::UnitSpecialConfiguration.__init__)


def test_machinelibrary::unitspecialconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitSpecialConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitgeneralspecial_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneralSpecial)


def test_machinelibrary::unitgeneralspecial_constructor_exists():
    assert callable(MachineLibrary::UnitGeneralSpecial.__init__)


def test_machinelibrary::unitgeneralspecial_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneralSpecial.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitgeneral_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitGeneral)


def test_machinelibrary::unitgeneral_constructor_exists():
    assert callable(MachineLibrary::UnitGeneral.__init__)


def test_machinelibrary::unitgeneral_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitGeneral.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::buttons_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Buttons)


def test_machinelibrary::buttons_constructor_exists():
    assert callable(MachineLibrary::Buttons.__init__)


def test_machinelibrary::buttons_constructor_args():
    sig = inspect.signature(MachineLibrary::Buttons.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::unitprograms_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::UnitPrograms)


def test_machinelibrary::unitprograms_constructor_exists():
    assert callable(MachineLibrary::UnitPrograms.__init__)


def test_machinelibrary::unitprograms_constructor_args():
    sig = inspect.signature(MachineLibrary::UnitPrograms.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::nodegeneral::rigakuxrf_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::RigakuXRF)


def test_machinelibrary::nodegeneral::rigakuxrf_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::RigakuXRF.__init__)


def test_machinelibrary::nodegeneral::rigakuxrf_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::RigakuXRF.__init__)
    params = list(sig.parameters.keys())
    assert "timeoutResponce" in params, "Missing parameter 'timeoutResponce'"
    assert "timeout" in params, "Missing parameter 'timeout'"
    assert "bDoNotshiftAtExit" in params, "Missing parameter 'bDoNotshiftAtExit'"
    assert "timerToSendStatus" in params, "Missing parameter 'timerToSendStatus'"

def test_machinelibrary::nodegeneral::rigakuxrf_has_timeoutResponce():
    assert hasattr(MachineLibrary::NodeGeneral::RigakuXRF, "timeoutResponce")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RigakuXRF.__mro__:
        if "timeoutResponce" in klass.__dict__:
            descriptor = klass.__dict__["timeoutResponce"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::rigakuxrf_has_timeout():
    assert hasattr(MachineLibrary::NodeGeneral::RigakuXRF, "timeout")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RigakuXRF.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::rigakuxrf_has_bDoNotshiftAtExit():
    assert hasattr(MachineLibrary::NodeGeneral::RigakuXRF, "bDoNotshiftAtExit")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RigakuXRF.__mro__:
        if "bDoNotshiftAtExit" in klass.__dict__:
            descriptor = klass.__dict__["bDoNotshiftAtExit"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::rigakuxrf_has_timerToSendStatus():
    assert hasattr(MachineLibrary::NodeGeneral::RigakuXRF, "timerToSendStatus")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RigakuXRF.__mro__:
        if "timerToSendStatus" in klass.__dict__:
            descriptor = klass.__dict__["timerToSendStatus"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneral::accupycmeter_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::AccuPycMeter)


def test_machinelibrary::nodegeneral::accupycmeter_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::AccuPycMeter.__init__)


def test_machinelibrary::nodegeneral::accupycmeter_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::AccuPycMeter.__init__)
    params = list(sig.parameters.keys())
    assert "runTimout" in params, "Missing parameter 'runTimout'"
    assert "expectSampleWeight" in params, "Missing parameter 'expectSampleWeight'"
    assert "polling" in params, "Missing parameter 'polling'"
    assert "sendSampleWeight" in params, "Missing parameter 'sendSampleWeight'"

def test_machinelibrary::nodegeneral::accupycmeter_has_runTimout():
    assert hasattr(MachineLibrary::NodeGeneral::AccuPycMeter, "runTimout")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::AccuPycMeter.__mro__:
        if "runTimout" in klass.__dict__:
            descriptor = klass.__dict__["runTimout"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::accupycmeter_has_expectSampleWeight():
    assert hasattr(MachineLibrary::NodeGeneral::AccuPycMeter, "expectSampleWeight")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::AccuPycMeter.__mro__:
        if "expectSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["expectSampleWeight"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::accupycmeter_has_polling():
    assert hasattr(MachineLibrary::NodeGeneral::AccuPycMeter, "polling")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::AccuPycMeter.__mro__:
        if "polling" in klass.__dict__:
            descriptor = klass.__dict__["polling"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::accupycmeter_has_sendSampleWeight():
    assert hasattr(MachineLibrary::NodeGeneral::AccuPycMeter, "sendSampleWeight")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::AccuPycMeter.__mro__:
        if "sendSampleWeight" in klass.__dict__:
            descriptor = klass.__dict__["sendSampleWeight"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneral::wincc2wincc_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::WinCC2WinCC)


def test_machinelibrary::nodegeneral::wincc2wincc_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::WinCC2WinCC.__init__)


def test_machinelibrary::nodegeneral::wincc2wincc_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::WinCC2WinCC.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_machinelibrary::nodegeneral::wincc2wincc_has_prefix():
    assert hasattr(MachineLibrary::NodeGeneral::WinCC2WinCC, "prefix")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::WinCC2WinCC.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneral::remotepm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::RemotePM)


def test_machinelibrary::nodegeneral::remotepm_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::RemotePM.__init__)


def test_machinelibrary::nodegeneral::remotepm_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::RemotePM.__init__)
    params = list(sig.parameters.keys())
    assert "timeServer" in params, "Missing parameter 'timeServer'"
    assert "system" in params, "Missing parameter 'system'"

def test_machinelibrary::nodegeneral::remotepm_has_timeServer():
    assert hasattr(MachineLibrary::NodeGeneral::RemotePM, "timeServer")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RemotePM.__mro__:
        if "timeServer" in klass.__dict__:
            descriptor = klass.__dict__["timeServer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::remotepm_has_system():
    assert hasattr(MachineLibrary::NodeGeneral::RemotePM, "system")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::RemotePM.__mro__:
        if "system" in klass.__dict__:
            descriptor = klass.__dict__["system"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneral::pm2pm_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::PM2PM)


def test_machinelibrary::nodegeneral::pm2pm_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::PM2PM.__init__)


def test_machinelibrary::nodegeneral::pm2pm_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::PM2PM.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "timeServer" in params, "Missing parameter 'timeServer'"

def test_machinelibrary::nodegeneral::pm2pm_has_type():
    assert hasattr(MachineLibrary::NodeGeneral::PM2PM, "type")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::PM2PM.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::pm2pm_has_timeServer():
    assert hasattr(MachineLibrary::NodeGeneral::PM2PM, "timeServer")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::PM2PM.__mro__:
        if "timeServer" in klass.__dict__:
            descriptor = klass.__dict__["timeServer"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneral::terminal_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral::Terminal)


def test_machinelibrary::nodegeneral::terminal_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral::Terminal.__init__)


def test_machinelibrary::nodegeneral::terminal_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral::Terminal.__init__)
    params = list(sig.parameters.keys())
    assert "customTimer1" in params, "Missing parameter 'customTimer1'"
    assert "terminalType" in params, "Missing parameter 'terminalType'"
    assert "stationReady" in params, "Missing parameter 'stationReady'"
    assert "steelCarrier" in params, "Missing parameter 'steelCarrier'"
    assert "name_1" in params, "Missing parameter 'name_1'"
    assert "name_3" in params, "Missing parameter 'name_3'"
    assert "name_2" in params, "Missing parameter 'name_2'"
    assert "name_6" in params, "Missing parameter 'name_6'"
    assert "signalCarrierPresent" in params, "Missing parameter 'signalCarrierPresent'"
    assert "keyBoardSignalCarrierPresent" in params, "Missing parameter 'keyBoardSignalCarrierPresent'"
    assert "maxScreens" in params, "Missing parameter 'maxScreens'"
    assert "stationAuto" in params, "Missing parameter 'stationAuto'"
    assert "maxXValue" in params, "Missing parameter 'maxXValue'"
    assert "name_5" in params, "Missing parameter 'name_5'"
    assert "displayTime" in params, "Missing parameter 'displayTime'"
    assert "name_4" in params, "Missing parameter 'name_4'"
    assert "customTimer2" in params, "Missing parameter 'customTimer2'"
    assert "stationType" in params, "Missing parameter 'stationType'"
    assert "maxYValue" in params, "Missing parameter 'maxYValue'"
    assert "lenOfPlanID" in params, "Missing parameter 'lenOfPlanID'"

def test_machinelibrary::nodegeneral::terminal_has_customTimer1():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "customTimer1")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "customTimer1" in klass.__dict__:
            descriptor = klass.__dict__["customTimer1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_terminalType():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "terminalType")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "terminalType" in klass.__dict__:
            descriptor = klass.__dict__["terminalType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_stationReady():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "stationReady")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "stationReady" in klass.__dict__:
            descriptor = klass.__dict__["stationReady"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_steelCarrier():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "steelCarrier")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "steelCarrier" in klass.__dict__:
            descriptor = klass.__dict__["steelCarrier"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_1():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_1")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_1" in klass.__dict__:
            descriptor = klass.__dict__["name_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_3():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_3")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_3" in klass.__dict__:
            descriptor = klass.__dict__["name_3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_2():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_2")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_2" in klass.__dict__:
            descriptor = klass.__dict__["name_2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_6():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_6")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_6" in klass.__dict__:
            descriptor = klass.__dict__["name_6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_signalCarrierPresent():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "signalCarrierPresent")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "signalCarrierPresent" in klass.__dict__:
            descriptor = klass.__dict__["signalCarrierPresent"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_keyBoardSignalCarrierPresent():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "keyBoardSignalCarrierPresent")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "keyBoardSignalCarrierPresent" in klass.__dict__:
            descriptor = klass.__dict__["keyBoardSignalCarrierPresent"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_maxScreens():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "maxScreens")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "maxScreens" in klass.__dict__:
            descriptor = klass.__dict__["maxScreens"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_stationAuto():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "stationAuto")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "stationAuto" in klass.__dict__:
            descriptor = klass.__dict__["stationAuto"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_maxXValue():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "maxXValue")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "maxXValue" in klass.__dict__:
            descriptor = klass.__dict__["maxXValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_5():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_5")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_5" in klass.__dict__:
            descriptor = klass.__dict__["name_5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_displayTime():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "displayTime")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "displayTime" in klass.__dict__:
            descriptor = klass.__dict__["displayTime"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_name_4():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "name_4")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "name_4" in klass.__dict__:
            descriptor = klass.__dict__["name_4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_customTimer2():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "customTimer2")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "customTimer2" in klass.__dict__:
            descriptor = klass.__dict__["customTimer2"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_stationType():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "stationType")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "stationType" in klass.__dict__:
            descriptor = klass.__dict__["stationType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_maxYValue():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "maxYValue")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "maxYValue" in klass.__dict__:
            descriptor = klass.__dict__["maxYValue"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral::terminal_has_lenOfPlanID():
    assert hasattr(MachineLibrary::NodeGeneral::Terminal, "lenOfPlanID")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral::Terminal.__mro__:
        if "lenOfPlanID" in klass.__dict__:
            descriptor = klass.__dict__["lenOfPlanID"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodegeneralspecial_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneralSpecial)


def test_machinelibrary::nodegeneralspecial_constructor_exists():
    assert callable(MachineLibrary::NodeGeneralSpecial.__init__)


def test_machinelibrary::nodegeneralspecial_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneralSpecial.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::nodegeneral_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeGeneral)


def test_machinelibrary::nodegeneral_constructor_exists():
    assert callable(MachineLibrary::NodeGeneral.__init__)


def test_machinelibrary::nodegeneral_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeGeneral.__init__)
    params = list(sig.parameters.keys())
    assert "canCreateErrorTag" in params, "Missing parameter 'canCreateErrorTag'"
    assert "canCreateStateTag" in params, "Missing parameter 'canCreateStateTag'"

def test_machinelibrary::nodegeneral_has_canCreateErrorTag():
    assert hasattr(MachineLibrary::NodeGeneral, "canCreateErrorTag")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral.__mro__:
        if "canCreateErrorTag" in klass.__dict__:
            descriptor = klass.__dict__["canCreateErrorTag"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodegeneral_has_canCreateStateTag():
    assert hasattr(MachineLibrary::NodeGeneral, "canCreateStateTag")
    descriptor = None
    for klass in MachineLibrary::NodeGeneral.__mro__:
        if "canCreateStateTag" in klass.__dict__:
            descriptor = klass.__dict__["canCreateStateTag"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodespecialconfiguration_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeSpecialConfiguration)


def test_machinelibrary::nodespecialconfiguration_constructor_exists():
    assert callable(MachineLibrary::NodeSpecialConfiguration.__init__)


def test_machinelibrary::nodespecialconfiguration_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeSpecialConfiguration.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::communicationdata_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::CommunicationData)


def test_machinelibrary::communicationdata_constructor_exists():
    assert callable(MachineLibrary::CommunicationData.__init__)


def test_machinelibrary::communicationdata_constructor_args():
    sig = inspect.signature(MachineLibrary::CommunicationData.__init__)
    params = list(sig.parameters.keys())
    assert "comErrorDataLength" in params, "Missing parameter 'comErrorDataLength'"
    assert "comProgressIndDataAddress" in params, "Missing parameter 'comProgressIndDataAddress'"
    assert "comSendDataLength" in params, "Missing parameter 'comSendDataLength'"
    assert "comErrorDataAddress" in params, "Missing parameter 'comErrorDataAddress'"
    assert "comProgressIndDataLength" in params, "Missing parameter 'comProgressIndDataLength'"
    assert "comSIDDataLength" in params, "Missing parameter 'comSIDDataLength'"
    assert "comSendDataAddress" in params, "Missing parameter 'comSendDataAddress'"
    assert "comRequestDataLength" in params, "Missing parameter 'comRequestDataLength'"
    assert "comSIDDataAddress" in params, "Missing parameter 'comSIDDataAddress'"
    assert "comRequestDataAddress" in params, "Missing parameter 'comRequestDataAddress'"

def test_machinelibrary::communicationdata_has_comErrorDataLength():
    assert hasattr(MachineLibrary::CommunicationData, "comErrorDataLength")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comErrorDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comErrorDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comProgressIndDataAddress():
    assert hasattr(MachineLibrary::CommunicationData, "comProgressIndDataAddress")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comProgressIndDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comProgressIndDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comSendDataLength():
    assert hasattr(MachineLibrary::CommunicationData, "comSendDataLength")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comSendDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comSendDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comErrorDataAddress():
    assert hasattr(MachineLibrary::CommunicationData, "comErrorDataAddress")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comErrorDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comErrorDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comProgressIndDataLength():
    assert hasattr(MachineLibrary::CommunicationData, "comProgressIndDataLength")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comProgressIndDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comProgressIndDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comSIDDataLength():
    assert hasattr(MachineLibrary::CommunicationData, "comSIDDataLength")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comSIDDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comSIDDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comSendDataAddress():
    assert hasattr(MachineLibrary::CommunicationData, "comSendDataAddress")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comSendDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comSendDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comRequestDataLength():
    assert hasattr(MachineLibrary::CommunicationData, "comRequestDataLength")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comRequestDataLength" in klass.__dict__:
            descriptor = klass.__dict__["comRequestDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comSIDDataAddress():
    assert hasattr(MachineLibrary::CommunicationData, "comSIDDataAddress")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comSIDDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comSIDDataAddress"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::communicationdata_has_comRequestDataAddress():
    assert hasattr(MachineLibrary::CommunicationData, "comRequestDataAddress")
    descriptor = None
    for klass in MachineLibrary::CommunicationData.__mro__:
        if "comRequestDataAddress" in klass.__dict__:
            descriptor = klass.__dict__["comRequestDataAddress"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::parameters_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Parameters)


def test_machinelibrary::parameters_constructor_exists():
    assert callable(MachineLibrary::Parameters.__init__)


def test_machinelibrary::parameters_constructor_args():
    sig = inspect.signature(MachineLibrary::Parameters.__init__)
    params = list(sig.parameters.keys())
    assert "parameterConfigNo" in params, "Missing parameter 'parameterConfigNo'"
    assert "parameterConfigYes" in params, "Missing parameter 'parameterConfigYes'"

def test_machinelibrary::parameters_has_parameterConfigNo():
    assert hasattr(MachineLibrary::Parameters, "parameterConfigNo")
    descriptor = None
    for klass in MachineLibrary::Parameters.__mro__:
        if "parameterConfigNo" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfigNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::parameters_has_parameterConfigYes():
    assert hasattr(MachineLibrary::Parameters, "parameterConfigYes")
    descriptor = None
    for klass in MachineLibrary::Parameters.__mro__:
        if "parameterConfigYes" in klass.__dict__:
            descriptor = klass.__dict__["parameterConfigYes"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::nodeprograms_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodePrograms)


def test_machinelibrary::nodeprograms_constructor_exists():
    assert callable(MachineLibrary::NodePrograms.__init__)


def test_machinelibrary::nodeprograms_constructor_args():
    sig = inspect.signature(MachineLibrary::NodePrograms.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::commands_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Commands)


def test_machinelibrary::commands_constructor_exists():
    assert callable(MachineLibrary::Commands.__init__)


def test_machinelibrary::commands_constructor_args():
    sig = inspect.signature(MachineLibrary::Commands.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::units_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Units)


def test_machinelibrary::units_constructor_exists():
    assert callable(MachineLibrary::Units.__init__)


def test_machinelibrary::units_constructor_args():
    sig = inspect.signature(MachineLibrary::Units.__init__)
    params = list(sig.parameters.keys())
    assert "internalUniNo" in params, "Missing parameter 'internalUniNo'"
    assert "unitNo" in params, "Missing parameter 'unitNo'"
    assert "unitName" in params, "Missing parameter 'unitName'"

def test_machinelibrary::units_has_internalUniNo():
    assert hasattr(MachineLibrary::Units, "internalUniNo")
    descriptor = None
    for klass in MachineLibrary::Units.__mro__:
        if "internalUniNo" in klass.__dict__:
            descriptor = klass.__dict__["internalUniNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::units_has_unitNo():
    assert hasattr(MachineLibrary::Units, "unitNo")
    descriptor = None
    for klass in MachineLibrary::Units.__mro__:
        if "unitNo" in klass.__dict__:
            descriptor = klass.__dict__["unitNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::units_has_unitName():
    assert hasattr(MachineLibrary::Units, "unitName")
    descriptor = None
    for klass in MachineLibrary::Units.__mro__:
        if "unitName" in klass.__dict__:
            descriptor = klass.__dict__["unitName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::dpbase::node_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::DPbase::Node)


def test_machinelibrary::dpbase::node_constructor_exists():
    assert callable(MachineLibrary::DPbase::Node.__init__)


def test_machinelibrary::dpbase::node_constructor_args():
    sig = inspect.signature(MachineLibrary::DPbase::Node.__init__)
    params = list(sig.parameters.keys())
    assert "isXPS" in params, "Missing parameter 'isXPS'"
    assert "nodeNo" in params, "Missing parameter 'nodeNo'"

def test_machinelibrary::dpbase::node_has_isXPS():
    assert hasattr(MachineLibrary::DPbase::Node, "isXPS")
    descriptor = None
    for klass in MachineLibrary::DPbase::Node.__mro__:
        if "isXPS" in klass.__dict__:
            descriptor = klass.__dict__["isXPS"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::dpbase::node_has_nodeNo():
    assert hasattr(MachineLibrary::DPbase::Node, "nodeNo")
    descriptor = None
    for klass in MachineLibrary::DPbase::Node.__mro__:
        if "nodeNo" in klass.__dict__:
            descriptor = klass.__dict__["nodeNo"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::compac::link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Compac::Link)


def test_machinelibrary::compac::link_constructor_exists():
    assert callable(MachineLibrary::Compac::Link.__init__)


def test_machinelibrary::compac::link_constructor_args():
    sig = inspect.signature(MachineLibrary::Compac::Link.__init__)
    params = list(sig.parameters.keys())
    assert "useNotENQ" in params, "Missing parameter 'useNotENQ'"
    assert "splitLongMessage" in params, "Missing parameter 'splitLongMessage'"
    assert "maxDataLength" in params, "Missing parameter 'maxDataLength'"
    assert "retry" in params, "Missing parameter 'retry'"
    assert "bcc" in params, "Missing parameter 'bcc'"
    assert "port" in params, "Missing parameter 'port'"
    assert "checksum" in params, "Missing parameter 'checksum'"
    assert "useNotACK_NAK" in params, "Missing parameter 'useNotACK_NAK'"
    assert "commConfig" in params, "Missing parameter 'commConfig'"
    assert "checksumCode" in params, "Missing parameter 'checksumCode'"
    assert "byteCount" in params, "Missing parameter 'byteCount'"
    assert "params" in params, "Missing parameter 'params'"
    assert "bytecountcode" in params, "Missing parameter 'bytecountcode'"
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_machinelibrary::compac::link_has_useNotENQ():
    assert hasattr(MachineLibrary::Compac::Link, "useNotENQ")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "useNotENQ" in klass.__dict__:
            descriptor = klass.__dict__["useNotENQ"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_splitLongMessage():
    assert hasattr(MachineLibrary::Compac::Link, "splitLongMessage")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "splitLongMessage" in klass.__dict__:
            descriptor = klass.__dict__["splitLongMessage"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_maxDataLength():
    assert hasattr(MachineLibrary::Compac::Link, "maxDataLength")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "maxDataLength" in klass.__dict__:
            descriptor = klass.__dict__["maxDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_retry():
    assert hasattr(MachineLibrary::Compac::Link, "retry")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "retry" in klass.__dict__:
            descriptor = klass.__dict__["retry"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_bcc():
    assert hasattr(MachineLibrary::Compac::Link, "bcc")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "bcc" in klass.__dict__:
            descriptor = klass.__dict__["bcc"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_port():
    assert hasattr(MachineLibrary::Compac::Link, "port")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_checksum():
    assert hasattr(MachineLibrary::Compac::Link, "checksum")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "checksum" in klass.__dict__:
            descriptor = klass.__dict__["checksum"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_useNotACK_NAK():
    assert hasattr(MachineLibrary::Compac::Link, "useNotACK_NAK")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "useNotACK_NAK" in klass.__dict__:
            descriptor = klass.__dict__["useNotACK_NAK"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_commConfig():
    assert hasattr(MachineLibrary::Compac::Link, "commConfig")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "commConfig" in klass.__dict__:
            descriptor = klass.__dict__["commConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_checksumCode():
    assert hasattr(MachineLibrary::Compac::Link, "checksumCode")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "checksumCode" in klass.__dict__:
            descriptor = klass.__dict__["checksumCode"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_byteCount():
    assert hasattr(MachineLibrary::Compac::Link, "byteCount")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "byteCount" in klass.__dict__:
            descriptor = klass.__dict__["byteCount"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_params():
    assert hasattr(MachineLibrary::Compac::Link, "params")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_bytecountcode():
    assert hasattr(MachineLibrary::Compac::Link, "bytecountcode")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "bytecountcode" in klass.__dict__:
            descriptor = klass.__dict__["bytecountcode"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::compac::link_has_timeout():
    assert hasattr(MachineLibrary::Compac::Link, "timeout")
    descriptor = None
    for klass in MachineLibrary::Compac::Link.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::filetransfer::link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::FileTransfer::Link)


def test_machinelibrary::filetransfer::link_constructor_exists():
    assert callable(MachineLibrary::FileTransfer::Link.__init__)


def test_machinelibrary::filetransfer::link_constructor_args():
    sig = inspect.signature(MachineLibrary::FileTransfer::Link.__init__)
    params = list(sig.parameters.keys())
    assert "timeoutwrite" in params, "Missing parameter 'timeoutwrite'"
    assert "delimiter" in params, "Missing parameter 'delimiter'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "delimter" in params, "Missing parameter 'delimter'"
    assert "flagDelAfterReading" in params, "Missing parameter 'flagDelAfterReading'"
    assert "writeAfterReading" in params, "Missing parameter 'writeAfterReading'"
    assert "pollTime" in params, "Missing parameter 'pollTime'"
    assert "readPath" in params, "Missing parameter 'readPath'"
    assert "maxDataLength" in params, "Missing parameter 'maxDataLength'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "flagWriteAfterReading" in params, "Missing parameter 'flagWriteAfterReading'"
    assert "flagToWriteWaitForDeleted" in params, "Missing parameter 'flagToWriteWaitForDeleted'"
    assert "toWriteWaitFor" in params, "Missing parameter 'toWriteWaitFor'"
    assert "writePath" in params, "Missing parameter 'writePath'"
    assert "translation" in params, "Missing parameter 'translation'"
    assert "flagToWriteWaitFor" in params, "Missing parameter 'flagToWriteWaitFor'"

def test_machinelibrary::filetransfer::link_has_timeoutwrite():
    assert hasattr(MachineLibrary::FileTransfer::Link, "timeoutwrite")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "timeoutwrite" in klass.__dict__:
            descriptor = klass.__dict__["timeoutwrite"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_delimiter():
    assert hasattr(MachineLibrary::FileTransfer::Link, "delimiter")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_sendBuffer():
    assert hasattr(MachineLibrary::FileTransfer::Link, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_delimter():
    assert hasattr(MachineLibrary::FileTransfer::Link, "delimter")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "delimter" in klass.__dict__:
            descriptor = klass.__dict__["delimter"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_flagDelAfterReading():
    assert hasattr(MachineLibrary::FileTransfer::Link, "flagDelAfterReading")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "flagDelAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["flagDelAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_writeAfterReading():
    assert hasattr(MachineLibrary::FileTransfer::Link, "writeAfterReading")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "writeAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["writeAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_pollTime():
    assert hasattr(MachineLibrary::FileTransfer::Link, "pollTime")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "pollTime" in klass.__dict__:
            descriptor = klass.__dict__["pollTime"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_readPath():
    assert hasattr(MachineLibrary::FileTransfer::Link, "readPath")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "readPath" in klass.__dict__:
            descriptor = klass.__dict__["readPath"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_maxDataLength():
    assert hasattr(MachineLibrary::FileTransfer::Link, "maxDataLength")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "maxDataLength" in klass.__dict__:
            descriptor = klass.__dict__["maxDataLength"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_receiveBuffer():
    assert hasattr(MachineLibrary::FileTransfer::Link, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_flagWriteAfterReading():
    assert hasattr(MachineLibrary::FileTransfer::Link, "flagWriteAfterReading")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "flagWriteAfterReading" in klass.__dict__:
            descriptor = klass.__dict__["flagWriteAfterReading"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_flagToWriteWaitForDeleted():
    assert hasattr(MachineLibrary::FileTransfer::Link, "flagToWriteWaitForDeleted")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "flagToWriteWaitForDeleted" in klass.__dict__:
            descriptor = klass.__dict__["flagToWriteWaitForDeleted"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_toWriteWaitFor():
    assert hasattr(MachineLibrary::FileTransfer::Link, "toWriteWaitFor")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "toWriteWaitFor" in klass.__dict__:
            descriptor = klass.__dict__["toWriteWaitFor"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_writePath():
    assert hasattr(MachineLibrary::FileTransfer::Link, "writePath")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "writePath" in klass.__dict__:
            descriptor = klass.__dict__["writePath"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_translation():
    assert hasattr(MachineLibrary::FileTransfer::Link, "translation")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "translation" in klass.__dict__:
            descriptor = klass.__dict__["translation"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::filetransfer::link_has_flagToWriteWaitFor():
    assert hasattr(MachineLibrary::FileTransfer::Link, "flagToWriteWaitFor")
    descriptor = None
    for klass in MachineLibrary::FileTransfer::Link.__mro__:
        if "flagToWriteWaitFor" in klass.__dict__:
            descriptor = klass.__dict__["flagToWriteWaitFor"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::serial::link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Serial::Link)


def test_machinelibrary::serial::link_constructor_exists():
    assert callable(MachineLibrary::Serial::Link.__init__)


def test_machinelibrary::serial::link_constructor_args():
    sig = inspect.signature(MachineLibrary::Serial::Link.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"
    assert "startChar" in params, "Missing parameter 'startChar'"
    assert "logging" in params, "Missing parameter 'logging'"
    assert "port" in params, "Missing parameter 'port'"
    assert "maxCharDelay" in params, "Missing parameter 'maxCharDelay'"
    assert "bufferLenght" in params, "Missing parameter 'bufferLenght'"
    assert "commConfig" in params, "Missing parameter 'commConfig'"
    assert "endChar" in params, "Missing parameter 'endChar'"

def test_machinelibrary::serial::link_has_params():
    assert hasattr(MachineLibrary::Serial::Link, "params")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_startChar():
    assert hasattr(MachineLibrary::Serial::Link, "startChar")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "startChar" in klass.__dict__:
            descriptor = klass.__dict__["startChar"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_logging():
    assert hasattr(MachineLibrary::Serial::Link, "logging")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "logging" in klass.__dict__:
            descriptor = klass.__dict__["logging"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_port():
    assert hasattr(MachineLibrary::Serial::Link, "port")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_maxCharDelay():
    assert hasattr(MachineLibrary::Serial::Link, "maxCharDelay")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "maxCharDelay" in klass.__dict__:
            descriptor = klass.__dict__["maxCharDelay"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_bufferLenght():
    assert hasattr(MachineLibrary::Serial::Link, "bufferLenght")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "bufferLenght" in klass.__dict__:
            descriptor = klass.__dict__["bufferLenght"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_commConfig():
    assert hasattr(MachineLibrary::Serial::Link, "commConfig")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "commConfig" in klass.__dict__:
            descriptor = klass.__dict__["commConfig"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::serial::link_has_endChar():
    assert hasattr(MachineLibrary::Serial::Link, "endChar")
    descriptor = None
    for klass in MachineLibrary::Serial::Link.__mro__:
        if "endChar" in klass.__dict__:
            descriptor = klass.__dict__["endChar"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::tcpip::link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::TCPIP::Link)


def test_machinelibrary::tcpip::link_constructor_exists():
    assert callable(MachineLibrary::TCPIP::Link.__init__)


def test_machinelibrary::tcpip::link_constructor_args():
    sig = inspect.signature(MachineLibrary::TCPIP::Link.__init__)
    params = list(sig.parameters.keys())
    assert "port" in params, "Missing parameter 'port'"
    assert "address_3" in params, "Missing parameter 'address_3'"
    assert "termChar" in params, "Missing parameter 'termChar'"
    assert "msgDelay" in params, "Missing parameter 'msgDelay'"
    assert "address_1" in params, "Missing parameter 'address_1'"
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "address_6" in params, "Missing parameter 'address_6'"
    assert "address_4" in params, "Missing parameter 'address_4'"
    assert "address_5" in params, "Missing parameter 'address_5'"
    assert "maxDataSize" in params, "Missing parameter 'maxDataSize'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "address_2" in params, "Missing parameter 'address_2'"

def test_machinelibrary::tcpip::link_has_port():
    assert hasattr(MachineLibrary::TCPIP::Link, "port")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_3():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_3")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_3" in klass.__dict__:
            descriptor = klass.__dict__["address_3"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_termChar():
    assert hasattr(MachineLibrary::TCPIP::Link, "termChar")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "termChar" in klass.__dict__:
            descriptor = klass.__dict__["termChar"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_msgDelay():
    assert hasattr(MachineLibrary::TCPIP::Link, "msgDelay")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "msgDelay" in klass.__dict__:
            descriptor = klass.__dict__["msgDelay"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_1():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_1")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_1" in klass.__dict__:
            descriptor = klass.__dict__["address_1"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_protocol():
    assert hasattr(MachineLibrary::TCPIP::Link, "protocol")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_6():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_6")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_6" in klass.__dict__:
            descriptor = klass.__dict__["address_6"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_4():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_4")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_4" in klass.__dict__:
            descriptor = klass.__dict__["address_4"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_5():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_5")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_5" in klass.__dict__:
            descriptor = klass.__dict__["address_5"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_maxDataSize():
    assert hasattr(MachineLibrary::TCPIP::Link, "maxDataSize")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "maxDataSize" in klass.__dict__:
            descriptor = klass.__dict__["maxDataSize"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_receiveBuffer():
    assert hasattr(MachineLibrary::TCPIP::Link, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_sendBuffer():
    assert hasattr(MachineLibrary::TCPIP::Link, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::tcpip::link_has_address_2():
    assert hasattr(MachineLibrary::TCPIP::Link, "address_2")
    descriptor = None
    for klass in MachineLibrary::TCPIP::Link.__mro__:
        if "address_2" in klass.__dict__:
            descriptor = klass.__dict__["address_2"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::wincclnk_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::WinCCLnk)


def test_machinelibrary::wincclnk_constructor_exists():
    assert callable(MachineLibrary::WinCCLnk.__init__)


def test_machinelibrary::wincclnk_constructor_args():
    sig = inspect.signature(MachineLibrary::WinCCLnk.__init__)
    params = list(sig.parameters.keys())
    assert "updateCycle" in params, "Missing parameter 'updateCycle'"
    assert "updateCycle_Help" in params, "Missing parameter 'updateCycle_Help'"
    assert "connectionName" in params, "Missing parameter 'connectionName'"
    assert "canModifyTag" in params, "Missing parameter 'canModifyTag'"
    assert "canCreateTags" in params, "Missing parameter 'canCreateTags'"

def test_machinelibrary::wincclnk_has_updateCycle():
    assert hasattr(MachineLibrary::WinCCLnk, "updateCycle")
    descriptor = None
    for klass in MachineLibrary::WinCCLnk.__mro__:
        if "updateCycle" in klass.__dict__:
            descriptor = klass.__dict__["updateCycle"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::wincclnk_has_updateCycle_Help():
    assert hasattr(MachineLibrary::WinCCLnk, "updateCycle_Help")
    descriptor = None
    for klass in MachineLibrary::WinCCLnk.__mro__:
        if "updateCycle_Help" in klass.__dict__:
            descriptor = klass.__dict__["updateCycle_Help"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::wincclnk_has_connectionName():
    assert hasattr(MachineLibrary::WinCCLnk, "connectionName")
    descriptor = None
    for klass in MachineLibrary::WinCCLnk.__mro__:
        if "connectionName" in klass.__dict__:
            descriptor = klass.__dict__["connectionName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::wincclnk_has_canModifyTag():
    assert hasattr(MachineLibrary::WinCCLnk, "canModifyTag")
    descriptor = None
    for klass in MachineLibrary::WinCCLnk.__mro__:
        if "canModifyTag" in klass.__dict__:
            descriptor = klass.__dict__["canModifyTag"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::wincclnk_has_canCreateTags():
    assert hasattr(MachineLibrary::WinCCLnk, "canCreateTags")
    descriptor = None
    for klass in MachineLibrary::WinCCLnk.__mro__:
        if "canCreateTags" in klass.__dict__:
            descriptor = klass.__dict__["canCreateTags"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::linkconfig_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::LinkConfig)


def test_machinelibrary::linkconfig_constructor_exists():
    assert callable(MachineLibrary::LinkConfig.__init__)


def test_machinelibrary::linkconfig_constructor_args():
    sig = inspect.signature(MachineLibrary::LinkConfig.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::nodeconfig_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::NodeConfig)


def test_machinelibrary::nodeconfig_constructor_exists():
    assert callable(MachineLibrary::NodeConfig.__init__)


def test_machinelibrary::nodeconfig_constructor_args():
    sig = inspect.signature(MachineLibrary::NodeConfig.__init__)
    params = list(sig.parameters.keys())
    assert "nodeNo" in params, "Missing parameter 'nodeNo'"
    assert "simFileName" in params, "Missing parameter 'simFileName'"
    assert "nodeName" in params, "Missing parameter 'nodeName'"

def test_machinelibrary::nodeconfig_has_nodeNo():
    assert hasattr(MachineLibrary::NodeConfig, "nodeNo")
    descriptor = None
    for klass in MachineLibrary::NodeConfig.__mro__:
        if "nodeNo" in klass.__dict__:
            descriptor = klass.__dict__["nodeNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeconfig_has_simFileName():
    assert hasattr(MachineLibrary::NodeConfig, "simFileName")
    descriptor = None
    for klass in MachineLibrary::NodeConfig.__mro__:
        if "simFileName" in klass.__dict__:
            descriptor = klass.__dict__["simFileName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::nodeconfig_has_nodeName():
    assert hasattr(MachineLibrary::NodeConfig, "nodeName")
    descriptor = None
    for klass in MachineLibrary::NodeConfig.__mro__:
        if "nodeName" in klass.__dict__:
            descriptor = klass.__dict__["nodeName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::link2_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::Link2)


def test_machinelibrary::link2_constructor_exists():
    assert callable(MachineLibrary::Link2.__init__)


def test_machinelibrary::link2_constructor_args():
    sig = inspect.signature(MachineLibrary::Link2.__init__)
    params = list(sig.parameters.keys())
    assert "link2Type" in params, "Missing parameter 'link2Type'"
    assert "link2ParamFile" in params, "Missing parameter 'link2ParamFile'"
    assert "link2ParamSection" in params, "Missing parameter 'link2ParamSection'"

def test_machinelibrary::link2_has_link2Type():
    assert hasattr(MachineLibrary::Link2, "link2Type")
    descriptor = None
    for klass in MachineLibrary::Link2.__mro__:
        if "link2Type" in klass.__dict__:
            descriptor = klass.__dict__["link2Type"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::link2_has_link2ParamFile():
    assert hasattr(MachineLibrary::Link2, "link2ParamFile")
    descriptor = None
    for klass in MachineLibrary::Link2.__mro__:
        if "link2ParamFile" in klass.__dict__:
            descriptor = klass.__dict__["link2ParamFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::link2_has_link2ParamSection():
    assert hasattr(MachineLibrary::Link2, "link2ParamSection")
    descriptor = None
    for klass in MachineLibrary::Link2.__mro__:
        if "link2ParamSection" in klass.__dict__:
            descriptor = klass.__dict__["link2ParamSection"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::dpbase::link_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::DPbase::Link)


def test_machinelibrary::dpbase::link_constructor_exists():
    assert callable(MachineLibrary::DPbase::Link.__init__)


def test_machinelibrary::dpbase::link_constructor_args():
    sig = inspect.signature(MachineLibrary::DPbase::Link.__init__)
    params = list(sig.parameters.keys())
    assert "speed" in params, "Missing parameter 'speed'"
    assert "maxNodes" in params, "Missing parameter 'maxNodes'"
    assert "cp_name" in params, "Missing parameter 'cp_name'"

def test_machinelibrary::dpbase::link_has_speed():
    assert hasattr(MachineLibrary::DPbase::Link, "speed")
    descriptor = None
    for klass in MachineLibrary::DPbase::Link.__mro__:
        if "speed" in klass.__dict__:
            descriptor = klass.__dict__["speed"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::dpbase::link_has_maxNodes():
    assert hasattr(MachineLibrary::DPbase::Link, "maxNodes")
    descriptor = None
    for klass in MachineLibrary::DPbase::Link.__mro__:
        if "maxNodes" in klass.__dict__:
            descriptor = klass.__dict__["maxNodes"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::dpbase::link_has_cp_name():
    assert hasattr(MachineLibrary::DPbase::Link, "cp_name")
    descriptor = None
    for klass in MachineLibrary::DPbase::Link.__mro__:
        if "cp_name" in klass.__dict__:
            descriptor = klass.__dict__["cp_name"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::ibmwebspheremq_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::IBMWebsphereMQ)


def test_machinelibrary::ibmwebspheremq_constructor_exists():
    assert callable(MachineLibrary::IBMWebsphereMQ.__init__)


def test_machinelibrary::ibmwebspheremq_constructor_args():
    sig = inspect.signature(MachineLibrary::IBMWebsphereMQ.__init__)
    params = list(sig.parameters.keys())
    assert "readDynamicQueName" in params, "Missing parameter 'readDynamicQueName'"
    assert "maxDataSize" in params, "Missing parameter 'maxDataSize'"
    assert "readQueName" in params, "Missing parameter 'readQueName'"
    assert "qName" in params, "Missing parameter 'qName'"
    assert "sendBuffer" in params, "Missing parameter 'sendBuffer'"
    assert "sendQueName" in params, "Missing parameter 'sendQueName'"
    assert "sendDynamicQueName" in params, "Missing parameter 'sendDynamicQueName'"
    assert "receiveBuffer" in params, "Missing parameter 'receiveBuffer'"
    assert "readQueMgrName" in params, "Missing parameter 'readQueMgrName'"
    assert "sendQueMgrName" in params, "Missing parameter 'sendQueMgrName'"

def test_machinelibrary::ibmwebspheremq_has_readDynamicQueName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "readDynamicQueName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "readDynamicQueName" in klass.__dict__:
            descriptor = klass.__dict__["readDynamicQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_maxDataSize():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "maxDataSize")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "maxDataSize" in klass.__dict__:
            descriptor = klass.__dict__["maxDataSize"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_readQueName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "readQueName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "readQueName" in klass.__dict__:
            descriptor = klass.__dict__["readQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_qName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "qName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "qName" in klass.__dict__:
            descriptor = klass.__dict__["qName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_sendBuffer():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "sendBuffer")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "sendBuffer" in klass.__dict__:
            descriptor = klass.__dict__["sendBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_sendQueName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "sendQueName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "sendQueName" in klass.__dict__:
            descriptor = klass.__dict__["sendQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_sendDynamicQueName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "sendDynamicQueName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "sendDynamicQueName" in klass.__dict__:
            descriptor = klass.__dict__["sendDynamicQueName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_receiveBuffer():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "receiveBuffer")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "receiveBuffer" in klass.__dict__:
            descriptor = klass.__dict__["receiveBuffer"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_readQueMgrName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "readQueMgrName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "readQueMgrName" in klass.__dict__:
            descriptor = klass.__dict__["readQueMgrName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::ibmwebspheremq_has_sendQueMgrName():
    assert hasattr(MachineLibrary::IBMWebsphereMQ, "sendQueMgrName")
    descriptor = None
    for klass in MachineLibrary::IBMWebsphereMQ.__mro__:
        if "sendQueMgrName" in klass.__dict__:
            descriptor = klass.__dict__["sendQueMgrName"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::labmachine_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::LabMachine)


def test_machinelibrary::labmachine_constructor_exists():
    assert callable(MachineLibrary::LabMachine.__init__)


def test_machinelibrary::labmachine_constructor_args():
    sig = inspect.signature(MachineLibrary::LabMachine.__init__)
    params = list(sig.parameters.keys())
    assert "linkParamFile" in params, "Missing parameter 'linkParamFile'"
    assert "linkType" in params, "Missing parameter 'linkType'"
    assert "createWinCCTags" in params, "Missing parameter 'createWinCCTags'"
    assert "linkParamSection" in params, "Missing parameter 'linkParamSection'"
    assert "machineName" in params, "Missing parameter 'machineName'"
    assert "versionRemark" in params, "Missing parameter 'versionRemark'"
    assert "machineVersionNo" in params, "Missing parameter 'machineVersionNo'"
    assert "driver" in params, "Missing parameter 'driver'"

def test_machinelibrary::labmachine_has_linkParamFile():
    assert hasattr(MachineLibrary::LabMachine, "linkParamFile")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "linkParamFile" in klass.__dict__:
            descriptor = klass.__dict__["linkParamFile"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_linkType():
    assert hasattr(MachineLibrary::LabMachine, "linkType")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "linkType" in klass.__dict__:
            descriptor = klass.__dict__["linkType"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_createWinCCTags():
    assert hasattr(MachineLibrary::LabMachine, "createWinCCTags")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "createWinCCTags" in klass.__dict__:
            descriptor = klass.__dict__["createWinCCTags"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_linkParamSection():
    assert hasattr(MachineLibrary::LabMachine, "linkParamSection")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "linkParamSection" in klass.__dict__:
            descriptor = klass.__dict__["linkParamSection"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_machineName():
    assert hasattr(MachineLibrary::LabMachine, "machineName")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "machineName" in klass.__dict__:
            descriptor = klass.__dict__["machineName"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_versionRemark():
    assert hasattr(MachineLibrary::LabMachine, "versionRemark")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "versionRemark" in klass.__dict__:
            descriptor = klass.__dict__["versionRemark"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_machineVersionNo():
    assert hasattr(MachineLibrary::LabMachine, "machineVersionNo")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "machineVersionNo" in klass.__dict__:
            descriptor = klass.__dict__["machineVersionNo"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::labmachine_has_driver():
    assert hasattr(MachineLibrary::LabMachine, "driver")
    descriptor = None
    for klass in MachineLibrary::LabMachine.__mro__:
        if "driver" in klass.__dict__:
            descriptor = klass.__dict__["driver"]
            break
    assert isinstance(descriptor, property)



def test_machinelibrary::labmachines_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::LabMachines)


def test_machinelibrary::labmachines_constructor_exists():
    assert callable(MachineLibrary::LabMachines.__init__)


def test_machinelibrary::labmachines_constructor_args():
    sig = inspect.signature(MachineLibrary::LabMachines.__init__)
    params = list(sig.parameters.keys())



def test_machinelibrary::pmmachinelibrary_is_not_abstract():
    assert not inspect.isabstract(MachineLibrary::PMMachineLibrary)


def test_machinelibrary::pmmachinelibrary_constructor_exists():
    assert callable(MachineLibrary::PMMachineLibrary.__init__)


def test_machinelibrary::pmmachinelibrary_constructor_args():
    sig = inspect.signature(MachineLibrary::PMMachineLibrary.__init__)
    params = list(sig.parameters.keys())
    assert "libraryVersion" in params, "Missing parameter 'libraryVersion'"
    assert "libraryVersionRemark" in params, "Missing parameter 'libraryVersionRemark'"

def test_machinelibrary::pmmachinelibrary_has_libraryVersion():
    assert hasattr(MachineLibrary::PMMachineLibrary, "libraryVersion")
    descriptor = None
    for klass in MachineLibrary::PMMachineLibrary.__mro__:
        if "libraryVersion" in klass.__dict__:
            descriptor = klass.__dict__["libraryVersion"]
            break
    assert isinstance(descriptor, property)

def test_machinelibrary::pmmachinelibrary_has_libraryVersionRemark():
    assert hasattr(MachineLibrary::PMMachineLibrary, "libraryVersionRemark")
    descriptor = None
    for klass in MachineLibrary::PMMachineLibrary.__mro__:
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
MachineLibrary::RobotToWinCC_strategy = st.builds(
    MachineLibrary::RobotToWinCC,
    robotToWinccFrom_X=
        safe_text,
    robotToWinccType_X=
        safe_text,
    robotToWinccSeq_X=
        st.integers(),
    robotToWinccTo_X=
        safe_text
)
MachineLibrary::RobotWinCCToRobot_strategy = st.builds(
    MachineLibrary::RobotWinCCToRobot,
    robotwincctorobootType_X=
        safe_text,
    robotwincctorobotFrom_X=
        safe_text,
    robotwincctorobootSeq_X=
        st.integers(),
    robotwincctorobotTo_X=
        safe_text
)
MachineLibrary::RobotConfSendOrder_strategy = st.builds(
    MachineLibrary::RobotConfSendOrder,
    robotconfsendorderFrom_X=
        safe_text,
    robotconfsendorderType_X=
        safe_text,
    robotconfsendorderVar_X=
        safe_text,
    robotconfsendorderSeq_X=
        st.integers()
)
MachineLibrary::RobotVarToBusycode_strategy = st.builds(
    MachineLibrary::RobotVarToBusycode,
    robotvartobusycodeSeq_X=
        st.integers(),
    robotvartobusycodeUnit_X=
        st.integers(),
    robotvartobusycodeBit_X=
        st.integers(),
    robotvartobusycodeType_X=
        safe_text,
    robotvartobusycodeVar_X=
        safe_text
)
MachineLibrary::RobotVarToErrorbit_strategy = st.builds(
    MachineLibrary::RobotVarToErrorbit,
    robotvartoerrorbitBit_X=
        st.integers(),
    robotvartoerrorbitSeq_X=
        st.integers(),
    robotvartoerrorbitInv_X=
        st.integers(),
    robotvartoerrorbitVar_X=
        safe_text,
    robotvartoerrorbitType_X=
        safe_text
)
MachineLibrary::PlainMoveEntrySend_strategy = st.builds(
    MachineLibrary::PlainMoveEntrySend,
    plainmoveSeq=
        st.integers(),
    plainmoveEntry=
        safe_text,
    plainmoveSend=
        safe_text
)
MachineLibrary::TransferFileSection_strategy = st.builds(
    MachineLibrary::TransferFileSection,
    transferSection=
        safe_text,
    transferFile=
        safe_text,
    transferSeq=
        st.integers()
)
MachineLibrary::RobotConfiguration_strategy = st.builds(
    MachineLibrary::RobotConfiguration,
    robotSystemID=
        safe_text,
    robotIPAddress=
        safe_text,
    robotID=
        safe_text,
    robotActivate=
        st.integers()
)
MachineLibrary::RobotVarToErrorbits_strategy = st.builds(
    MachineLibrary::RobotVarToErrorbits,
)
MachineLibrary::RobotWarningONDelete_strategy = st.builds(
    MachineLibrary::RobotWarningONDelete,
    robotExtraPos_1=
        safe_text,
    robotExtraUnit_2=
        safe_text,
    robotErrBitWhenConfirmationIsNeededFor_PM=
        st.integers(),
    robotErrBitWhenConfirmationIsNeededFor_Robot=
        st.integers()
)
MachineLibrary::RobotToWinccs_strategy = st.builds(
    MachineLibrary::RobotToWinccs,
)
MachineLibrary::RobotWinCCToRobots_strategy = st.builds(
    MachineLibrary::RobotWinCCToRobots,
)
MachineLibrary::RobotConfSendOrders_strategy = st.builds(
    MachineLibrary::RobotConfSendOrders,
)
MachineLibrary::RobotVarToBusyCodes_strategy = st.builds(
    MachineLibrary::RobotVarToBusyCodes,
)
MachineLibrary::Parameter_strategy = st.builds(
    MachineLibrary::Parameter,
    parameterT2=
        safe_text,
    parameterMin=
        st.integers(),
    parameterV=
        safe_text,
    parameterT1=
        safe_text,
    parameterConfig=
        safe_text,
    parameterMax=
        st.integers(),
    parameterV1=
        safe_text,
    parameterType=
        safe_text,
    parameterName=
        safe_text,
    parameterV0=
        safe_text,
    parameterParaLen=
        st.integers()
)
MachineLibrary::PlainMove_strategy = st.builds(
    MachineLibrary::PlainMove,
    plainmovePreDefWS=
        safe_text,
    plainmoveType=
        st.integers(),
    plainmoveSID_REF=
        safe_text
)
MachineLibrary::Transfer_strategy = st.builds(
    MachineLibrary::Transfer,
)
MachineLibrary::ParamPrint_strategy = st.builds(
    MachineLibrary::ParamPrint,
    fontHightData=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    horzPosLeftBorder=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    fontHightHeader=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    dateStamp=
        safe_text,
    vertPosData=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    horzPosValues=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    vertPosHeader=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    vertLineSpace=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MachineLibrary::NodeProgram_strategy = st.builds(
    MachineLibrary::NodeProgram,
    programLenPerParam=
        safe_text,
    programSection=
        safe_text,
    programNo=
        st.integers(),
    programName=
        safe_text,
    programAddress=
        safe_text
)
MachineLibrary::Command_strategy = st.builds(
    MachineLibrary::Command,
    commandProgParameter=
        st.integers(),
    commandName=
        safe_text,
    commandNo=
        safe_text
)
MachineLibrary::UnitProgParameters_strategy = st.builds(
    MachineLibrary::UnitProgParameters,
    parameterNo=
        st.integers(),
    parameter=
        safe_text
)
MachineLibrary::UnitProgram_strategy = st.builds(
    MachineLibrary::UnitProgram,
    unitProgName=
        safe_text
)
MachineLibrary::Position_strategy = st.builds(
    MachineLibrary::Position,
    posWarningOnDelete=
        st.integers(),
    posExit=
        st.integers(),
    posName=
        safe_text,
    posIndex=
        st.integers(),
    posRemark=
        safe_text,
    posNo=
        st.integers()
)
MachineLibrary::Button_strategy = st.builds(
    MachineLibrary::Button,
    commandNo=
        st.integers(),
    buttonText=
        safe_text,
    buttonNo=
        st.integers()
)
MachineLibrary::CheckAddSID::Values::PM2PM_strategy = st.builds(
    MachineLibrary::CheckAddSID::Values::PM2PM,
    optionNo=
        st.integers(),
    optonValue=
        safe_text
)
MachineLibrary::SepByComma::ID::Scanner_strategy = st.builds(
    MachineLibrary::SepByComma::ID::Scanner,
    idPrevValue=
        safe_text,
    idCharValue=
        safe_text,
    idSeq_X=
        st.integers(),
    idValue=
        st.integers()
)
MachineLibrary::SepByComma::Field::Scanner_strategy = st.builds(
    MachineLibrary::SepByComma::Field::Scanner,
    fieldNo=
        st.integers(),
    fieldName=
        safe_text
)
MachineLibrary::StatusBit_strategy = st.builds(
    MachineLibrary::StatusBit,
    bitName=
        safe_text,
    bitNo=
        st.integers()
)
MachineLibrary::HistoryConfig::AccuPyc_strategy = st.builds(
    MachineLibrary::HistoryConfig::AccuPyc,
    sampleCupWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    currentSample=
        safe_text,
    currentSampleID=
        safe_text
)
MachineLibrary::CheckSampleConfig::SuperQXRF_strategy = st.builds(
    MachineLibrary::CheckSampleConfig::SuperQXRF,
    minutes=
        safe_text,
    samples=
        safe_text,
    sampleID=
        safe_text,
    program=
        safe_text,
    anaProg=
        safe_text,
    seq_X=
        st.integers()
)
MachineLibrary::InsertRemove::Keywords::Host_strategy = st.builds(
    MachineLibrary::InsertRemove::Keywords::Host,
    keywordKey=
        safe_text,
    keywordValue=
        safe_text
)
MachineLibrary::InsertRemove::Types::Host_strategy = st.builds(
    MachineLibrary::InsertRemove::Types::Host,
    typeNo=
        st.integers(),
    typeValue=
        safe_text
)
MachineLibrary::InsertRemove::Entry::Host_strategy = st.builds(
    MachineLibrary::InsertRemove::Entry::Host,
    entryName=
        safe_text,
    entryNo=
        st.integers()
)
MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy = st.builds(
    MachineLibrary::CheckSampleRunTimeParams::SuperQXRF,
    value=
        st.integers(),
    sampleType=
        st.integers()
)
MachineLibrary::OES::XRF::Condition_strategy = st.builds(
    MachineLibrary::OES::XRF::Condition,
    comment=
        safe_text,
    seq_X=
        st.integers(),
    paraName=
        safe_text,
    para=
        safe_text
)
MachineLibrary::InsertRemove::Host_strategy = st.builds(
    MachineLibrary::InsertRemove::Host,
    report_All=
        st.integers()
)
MachineLibrary::Moved::Host_strategy = st.builds(
    MachineLibrary::Moved::Host,
    pos0=
        st.integers(),
    report_ALL=
        st.integers(),
    writePositionNameInFile=
        st.integers(),
    type0=
        st.integers()
)
MachineLibrary::WS::Update::Host_strategy = st.builds(
    MachineLibrary::WS::Update::Host,
    AllowUnit0=
        st.integers(),
    checkUnit=
        st.integers()
)
MachineLibrary::Report::Host_strategy = st.builds(
    MachineLibrary::Report::Host,
    fileName=
        safe_text,
    stateChanged=
        st.integers(),
    maxType=
        st.integers(),
    timeStamp=
        st.integers(),
    sampleInsert=
        st.integers(),
    sendErrorWarningsMsgOnly=
        st.integers(),
    sendLifeMessages=
        st.integers(),
    note=
        safe_text,
    note1=
        safe_text,
    minType=
        st.integers(),
    sampleMoved=
        st.integers(),
    internal=
        st.integers(),
    sampleRemoved=
        st.integers(),
    rawData=
        st.integers()
)
MachineLibrary::Settings::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::Settings::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::DisableSCT::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::DisableSCT::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::ExePrepUnit::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::ExePrepUnit::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::ExecuteFiling::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::ExecuteFiling::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::CheckFilling::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::CheckFilling::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::CheckSample::SuperQXRF_strategy = st.builds(
    MachineLibrary::CheckSample::SuperQXRF,
)
MachineLibrary::CheckSampleRunTime::SuperQXRF_strategy = st.builds(
    MachineLibrary::CheckSampleRunTime::SuperQXRF,
)
MachineLibrary::Communication::SuperQXRF_strategy = st.builds(
    MachineLibrary::Communication::SuperQXRF,
    enq_ACK_Protocol=
        st.integers()
)
MachineLibrary::ControlSamples::SuperQXRF_strategy = st.builds(
    MachineLibrary::ControlSamples::SuperQXRF,
    outOfControl=
        st.integers()
)
MachineLibrary::File::Sample::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::File::Sample::ARL::XRF::OES,
    noSuccess=
        safe_text
)
MachineLibrary::PS::Process::Finished::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::PS::Process::Finished::ARL::XRF::OES,
    noSuccess=
        safe_text
)
MachineLibrary::GeneralSetting::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::GeneralSetting::ARL::XRF::OES,
    name=
        safe_text
)
MachineLibrary::CheckAddSID::PM2PM_strategy = st.builds(
    MachineLibrary::CheckAddSID::PM2PM,
)
MachineLibrary::SepByComma::Scanner_strategy = st.builds(
    MachineLibrary::SepByComma::Scanner,
    activ=
        st.integers(),
    preDefWS=
        st.integers()
)
MachineLibrary::History::AccuPycMeter_strategy = st.builds(
    MachineLibrary::History::AccuPycMeter,
)
MachineLibrary::UnitConfig::Host_strategy = st.builds(
    MachineLibrary::UnitConfig::Host,
)
MachineLibrary::UnitConfig::ARL::XRF::OES_strategy = st.builds(
    MachineLibrary::UnitConfig::ARL::XRF::OES,
)
MachineLibrary::UnitConfig::SuperQ::XRF_strategy = st.builds(
    MachineLibrary::UnitConfig::SuperQ::XRF,
)
MachineLibrary::UnitConfig::OBLF::OES_strategy = st.builds(
    MachineLibrary::UnitConfig::OBLF::OES,
)
MachineLibrary::UnitConfig::Terminal_strategy = st.builds(
    MachineLibrary::UnitConfig::Terminal,
)
MachineLibrary::GeneralParameter::SuperQXRF_strategy = st.builds(
    MachineLibrary::GeneralParameter::SuperQXRF,
    listName=
        safe_text,
    switchRemote=
        safe_text,
    startList=
        safe_text
)
MachineLibrary::ErrorMessage::OBLFOES_strategy = st.builds(
    MachineLibrary::ErrorMessage::OBLFOES,
    errorMessage=
        safe_text
)
MachineLibrary::RecalRequest::OBLFOES_strategy = st.builds(
    MachineLibrary::RecalRequest::OBLFOES,
    name=
        safe_text
)
MachineLibrary::TestRequest::OBLFOES_strategy = st.builds(
    MachineLibrary::TestRequest::OBLFOES,
    name=
        safe_text
)
MachineLibrary::OutputRequest::OBLFOES_strategy = st.builds(
    MachineLibrary::OutputRequest::OBLFOES,
    name=
        safe_text
)
MachineLibrary::Translate::Terminal_strategy = st.builds(
    MachineLibrary::Translate::Terminal,
    auto_Ready=
        safe_text,
    man_Ready=
        safe_text,
    man_Busy=
        safe_text,
    auto_Busy=
        safe_text
)
MachineLibrary::UnitGeneral::Scanner_strategy = st.builds(
    MachineLibrary::UnitGeneral::Scanner,
    start=
        st.integers(),
    length=
        st.integers(),
    preString=
        safe_text,
    registerSample=
        st.integers(),
    forcedSampleType=
        st.integers(),
    fillWith=
        safe_text,
    addString=
        safe_text
)
MachineLibrary::UnitGeneral::RigakuXRF_strategy = st.builds(
    MachineLibrary::UnitGeneral::RigakuXRF,
    lastPoHAG_SIInstrument=
        st.integers(),
    lastPosInInstrument=
        st.integers(),
    separator=
        st.integers(),
    lastPosAnalyHAG_SIg=
        st.integers()
)
MachineLibrary::UnitGeneral::SuperQ_strategy = st.builds(
    MachineLibrary::UnitGeneral::SuperQ,
    lastPosAnalysing=
        st.integers(),
    lastPosInInstrument=
        st.integers()
)
MachineLibrary::UnitGeneral::AccPyc_strategy = st.builds(
    MachineLibrary::UnitGeneral::AccPyc,
    minSampleWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    cupWeight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
MachineLibrary::UnitGeneral::PM2PM_strategy = st.builds(
    MachineLibrary::UnitGeneral::PM2PM,
    processFeedBack=
        safe_text,
    sid_Mask=
        safe_text
)
MachineLibrary::UnitGeneral::Remote_strategy = st.builds(
    MachineLibrary::UnitGeneral::Remote,
    handshakeA=
        safe_text,
    handshakeQ=
        safe_text,
    handshakeT=
        st.integers(),
    editWSDB=
        st.booleans()
)
MachineLibrary::UnitGeneral::HostPC_strategy = st.builds(
    MachineLibrary::UnitGeneral::HostPC,
    writeDumyIfNoDataExist=
        st.integers(),
    replyOnLink=
        st.integers(),
    index=
        st.integers(),
    maxIndex=
        st.integers()
)
MachineLibrary::UnitGeneral::Terminal_strategy = st.builds(
    MachineLibrary::UnitGeneral::Terminal,
    station5=
        safe_text,
    station3=
        safe_text,
    thisStation=
        safe_text,
    station1=
        safe_text,
    station4=
        safe_text,
    station2=
        safe_text
)
MachineLibrary::PLCtoPmMatrix_strategy = st.builds(
    MachineLibrary::PLCtoPmMatrix,
    plcpmmatrixBit0=
        st.integers(),
    plcpmmatrixBit15=
        st.integers(),
    plcpmmatrixBit2=
        st.integers(),
    plcpmmatrixBit7=
        st.integers(),
    plcpmmatrixBit9=
        st.integers(),
    plcpmmatrixBit11=
        st.integers(),
    plcpmmatrixBit13=
        st.integers(),
    plcpmmatrixBit6=
        st.integers(),
    plcpmmatrixBit12=
        st.integers(),
    plcpmmatrixBit1=
        st.integers(),
    plcpmmatrixBit14=
        st.integers(),
    plcpmmatrixBit3=
        st.integers(),
    plcpmmatrixBit8=
        st.integers(),
    plcpmmatrixBit4=
        st.integers(),
    plcpmmatrixBit5=
        st.integers(),
    plcpmmatrixBit10=
        st.integers()
)
MachineLibrary::StausBits_strategy = st.builds(
    MachineLibrary::StausBits,
)
MachineLibrary::Positions_strategy = st.builds(
    MachineLibrary::Positions,
)
MachineLibrary::WinCCAddTag_strategy = st.builds(
    MachineLibrary::WinCCAddTag,
    winCCTag=
        safe_text
)
MachineLibrary::UnitGeneralParameters_strategy = st.builds(
    MachineLibrary::UnitGeneralParameters,
    minValue_1=
        st.integers(),
    UseWith_1=
        safe_text,
    defaultValue_1=
        st.integers(),
    unit_1=
        safe_text,
    seq_X=
        st.integers(),
    comment_1=
        safe_text,
    canBeChange_1=
        st.integers(),
    maxValue_1=
        st.integers(),
    KeyWord_1=
        safe_text,
    paraName_1=
        safe_text,
    visibleType_1=
        st.integers()
)
MachineLibrary::UnitSpecialConfiguration_strategy = st.builds(
    MachineLibrary::UnitSpecialConfiguration,
)
MachineLibrary::UnitGeneralSpecial_strategy = st.builds(
    MachineLibrary::UnitGeneralSpecial,
)
MachineLibrary::UnitGeneral_strategy = st.builds(
    MachineLibrary::UnitGeneral,
)
MachineLibrary::Buttons_strategy = st.builds(
    MachineLibrary::Buttons,
)
MachineLibrary::UnitPrograms_strategy = st.builds(
    MachineLibrary::UnitPrograms,
)
MachineLibrary::NodeGeneral::RigakuXRF_strategy = st.builds(
    MachineLibrary::NodeGeneral::RigakuXRF,
    timeoutResponce=
        st.integers(),
    timeout=
        st.integers(),
    bDoNotshiftAtExit=
        st.integers(),
    timerToSendStatus=
        st.integers()
)
MachineLibrary::NodeGeneral::AccuPycMeter_strategy = st.builds(
    MachineLibrary::NodeGeneral::AccuPycMeter,
    runTimout=
        st.integers(),
    expectSampleWeight=
        st.integers(),
    polling=
        st.integers(),
    sendSampleWeight=
        st.integers()
)
MachineLibrary::NodeGeneral::WinCC2WinCC_strategy = st.builds(
    MachineLibrary::NodeGeneral::WinCC2WinCC,
    prefix=
        safe_text
)
MachineLibrary::NodeGeneral::RemotePM_strategy = st.builds(
    MachineLibrary::NodeGeneral::RemotePM,
    timeServer=
        st.integers(),
    system=
        safe_text
)
MachineLibrary::NodeGeneral::PM2PM_strategy = st.builds(
    MachineLibrary::NodeGeneral::PM2PM,
    type=
        st.integers(),
    timeServer=
        st.integers()
)
MachineLibrary::NodeGeneral::Terminal_strategy = st.builds(
    MachineLibrary::NodeGeneral::Terminal,
    customTimer1=
        st.integers(),
    terminalType=
        st.integers(),
    stationReady=
        safe_text,
    steelCarrier=
        safe_text,
    name_1=
        safe_text,
    name_3=
        safe_text,
    name_2=
        safe_text,
    name_6=
        safe_text,
    signalCarrierPresent=
        st.integers(),
    keyBoardSignalCarrierPresent=
        st.integers(),
    maxScreens=
        st.integers(),
    stationAuto=
        safe_text,
    maxXValue=
        st.integers(),
    name_5=
        safe_text,
    displayTime=
        st.integers(),
    name_4=
        safe_text,
    customTimer2=
        st.integers(),
    stationType=
        st.integers(),
    maxYValue=
        st.integers(),
    lenOfPlanID=
        st.integers()
)
MachineLibrary::NodeGeneralSpecial_strategy = st.builds(
    MachineLibrary::NodeGeneralSpecial,
)
MachineLibrary::NodeGeneral_strategy = st.builds(
    MachineLibrary::NodeGeneral,
    canCreateErrorTag=
        safe_text,
    canCreateStateTag=
        safe_text
)
MachineLibrary::NodeSpecialConfiguration_strategy = st.builds(
    MachineLibrary::NodeSpecialConfiguration,
)
MachineLibrary::CommunicationData_strategy = st.builds(
    MachineLibrary::CommunicationData,
    comErrorDataLength=
        st.integers(),
    comProgressIndDataAddress=
        safe_text,
    comSendDataLength=
        st.integers(),
    comErrorDataAddress=
        safe_text,
    comProgressIndDataLength=
        st.integers(),
    comSIDDataLength=
        st.integers(),
    comSendDataAddress=
        safe_text,
    comRequestDataLength=
        st.integers(),
    comSIDDataAddress=
        safe_text,
    comRequestDataAddress=
        safe_text
)
MachineLibrary::Parameters_strategy = st.builds(
    MachineLibrary::Parameters,
    parameterConfigNo=
        safe_text,
    parameterConfigYes=
        safe_text
)
MachineLibrary::NodePrograms_strategy = st.builds(
    MachineLibrary::NodePrograms,
)
MachineLibrary::Commands_strategy = st.builds(
    MachineLibrary::Commands,
)
MachineLibrary::Units_strategy = st.builds(
    MachineLibrary::Units,
    internalUniNo=
        st.integers(),
    unitNo=
        st.integers(),
    unitName=
        safe_text
)
MachineLibrary::DPbase::Node_strategy = st.builds(
    MachineLibrary::DPbase::Node,
    isXPS=
        st.integers(),
    nodeNo=
        st.integers()
)
MachineLibrary::Compac::Link_strategy = st.builds(
    MachineLibrary::Compac::Link,
    useNotENQ=
        st.integers(),
    splitLongMessage=
        st.integers(),
    maxDataLength=
        st.integers(),
    retry=
        st.integers(),
    bcc=
        st.integers(),
    port=
        safe_text,
    checksum=
        st.integers(),
    useNotACK_NAK=
        st.integers(),
    commConfig=
        safe_text,
    checksumCode=
        st.integers(),
    byteCount=
        st.integers(),
    params=
        safe_text,
    bytecountcode=
        st.integers(),
    timeout=
        st.integers()
)
MachineLibrary::FileTransfer::Link_strategy = st.builds(
    MachineLibrary::FileTransfer::Link,
    timeoutwrite=
        safe_text,
    delimiter=
        safe_text,
    sendBuffer=
        st.integers(),
    delimter=
        safe_text,
    flagDelAfterReading=
        st.integers(),
    writeAfterReading=
        st.integers(),
    pollTime=
        st.integers(),
    readPath=
        safe_text,
    maxDataLength=
        st.integers(),
    receiveBuffer=
        st.integers(),
    flagWriteAfterReading=
        st.integers(),
    flagToWriteWaitForDeleted=
        st.integers(),
    toWriteWaitFor=
        safe_text,
    writePath=
        safe_text,
    translation=
        st.integers(),
    flagToWriteWaitFor=
        st.integers()
)
MachineLibrary::Serial::Link_strategy = st.builds(
    MachineLibrary::Serial::Link,
    params=
        safe_text,
    startChar=
        safe_text,
    logging=
        st.integers(),
    port=
        safe_text,
    maxCharDelay=
        safe_text,
    bufferLenght=
        safe_text,
    commConfig=
        safe_text,
    endChar=
        safe_text
)
MachineLibrary::TCPIP::Link_strategy = st.builds(
    MachineLibrary::TCPIP::Link,
    port=
        st.integers(),
    address_3=
        safe_text,
    termChar=
        st.integers(),
    msgDelay=
        st.integers(),
    address_1=
        safe_text,
    protocol=
        st.integers(),
    address_6=
        safe_text,
    address_4=
        safe_text,
    address_5=
        safe_text,
    maxDataSize=
        st.integers(),
    receiveBuffer=
        st.integers(),
    sendBuffer=
        st.integers(),
    address_2=
        safe_text
)
MachineLibrary::WinCCLnk_strategy = st.builds(
    MachineLibrary::WinCCLnk,
    updateCycle=
        st.integers(),
    updateCycle_Help=
        safe_text,
    connectionName=
        safe_text,
    canModifyTag=
        st.integers(),
    canCreateTags=
        st.integers()
)
MachineLibrary::LinkConfig_strategy = st.builds(
    MachineLibrary::LinkConfig,
)
MachineLibrary::NodeConfig_strategy = st.builds(
    MachineLibrary::NodeConfig,
    nodeNo=
        st.integers(),
    simFileName=
        safe_text,
    nodeName=
        safe_text
)
MachineLibrary::Link2_strategy = st.builds(
    MachineLibrary::Link2,
    link2Type=
        safe_text,
    link2ParamFile=
        safe_text,
    link2ParamSection=
        safe_text
)
MachineLibrary::DPbase::Link_strategy = st.builds(
    MachineLibrary::DPbase::Link,
    speed=
        st.integers(),
    maxNodes=
        st.integers(),
    cp_name=
        safe_text
)
MachineLibrary::IBMWebsphereMQ_strategy = st.builds(
    MachineLibrary::IBMWebsphereMQ,
    readDynamicQueName=
        safe_text,
    maxDataSize=
        st.integers(),
    readQueName=
        safe_text,
    qName=
        safe_text,
    sendBuffer=
        st.integers(),
    sendQueName=
        safe_text,
    sendDynamicQueName=
        safe_text,
    receiveBuffer=
        st.integers(),
    readQueMgrName=
        safe_text,
    sendQueMgrName=
        safe_text
)
MachineLibrary::LabMachine_strategy = st.builds(
    MachineLibrary::LabMachine,
    linkParamFile=
        safe_text,
    linkType=
        safe_text,
    createWinCCTags=
        safe_text,
    linkParamSection=
        safe_text,
    machineName=
        safe_text,
    versionRemark=
        safe_text,
    machineVersionNo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    driver=
        safe_text
)
MachineLibrary::LabMachines_strategy = st.builds(
    MachineLibrary::LabMachines,
)
MachineLibrary::PMMachineLibrary_strategy = st.builds(
    MachineLibrary::PMMachineLibrary,
    libraryVersion=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    libraryVersionRemark=
        safe_text
)

@given(instance=MachineLibrary::RobotToWinCC_strategy)
@settings(max_examples=50)
def test_machinelibrary::robottowincc_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotToWinCC)

@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccFrom_X_type(instance):
    assert isinstance(instance.robotToWinccFrom_X, str)


@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccFrom_X_setter(instance):
    original = instance.robotToWinccFrom_X
    instance.robotToWinccFrom_X = original
    assert instance.robotToWinccFrom_X == original

@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccType_X_type(instance):
    assert isinstance(instance.robotToWinccType_X, str)


@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccType_X_setter(instance):
    original = instance.robotToWinccType_X
    instance.robotToWinccType_X = original
    assert instance.robotToWinccType_X == original

@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccSeq_X_type(instance):
    assert isinstance(instance.robotToWinccSeq_X, int)


@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccSeq_X_setter(instance):
    original = instance.robotToWinccSeq_X
    instance.robotToWinccSeq_X = original
    assert instance.robotToWinccSeq_X == original

@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccTo_X_type(instance):
    assert isinstance(instance.robotToWinccTo_X, str)


@given(instance=MachineLibrary::RobotToWinCC_strategy)
def test_machinelibrary::robottowincc_robotToWinccTo_X_setter(instance):
    original = instance.robotToWinccTo_X
    instance.robotToWinccTo_X = original
    assert instance.robotToWinccTo_X == original

@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotwincctorobot_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotWinCCToRobot)

@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobootType_X_type(instance):
    assert isinstance(instance.robotwincctorobootType_X, str)


@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobootType_X_setter(instance):
    original = instance.robotwincctorobootType_X
    instance.robotwincctorobootType_X = original
    assert instance.robotwincctorobootType_X == original

@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobotFrom_X_type(instance):
    assert isinstance(instance.robotwincctorobotFrom_X, str)


@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobotFrom_X_setter(instance):
    original = instance.robotwincctorobotFrom_X
    instance.robotwincctorobotFrom_X = original
    assert instance.robotwincctorobotFrom_X == original

@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobootSeq_X_type(instance):
    assert isinstance(instance.robotwincctorobootSeq_X, int)


@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobootSeq_X_setter(instance):
    original = instance.robotwincctorobootSeq_X
    instance.robotwincctorobootSeq_X = original
    assert instance.robotwincctorobootSeq_X == original

@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobotTo_X_type(instance):
    assert isinstance(instance.robotwincctorobotTo_X, str)


@given(instance=MachineLibrary::RobotWinCCToRobot_strategy)
def test_machinelibrary::robotwincctorobot_robotwincctorobotTo_X_setter(instance):
    original = instance.robotwincctorobotTo_X
    instance.robotwincctorobotTo_X = original
    assert instance.robotwincctorobotTo_X == original

@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotconfsendorder_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotConfSendOrder)

@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderFrom_X_type(instance):
    assert isinstance(instance.robotconfsendorderFrom_X, str)


@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderFrom_X_setter(instance):
    original = instance.robotconfsendorderFrom_X
    instance.robotconfsendorderFrom_X = original
    assert instance.robotconfsendorderFrom_X == original

@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderType_X_type(instance):
    assert isinstance(instance.robotconfsendorderType_X, str)


@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderType_X_setter(instance):
    original = instance.robotconfsendorderType_X
    instance.robotconfsendorderType_X = original
    assert instance.robotconfsendorderType_X == original

@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderVar_X_type(instance):
    assert isinstance(instance.robotconfsendorderVar_X, str)


@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderVar_X_setter(instance):
    original = instance.robotconfsendorderVar_X
    instance.robotconfsendorderVar_X = original
    assert instance.robotconfsendorderVar_X == original

@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderSeq_X_type(instance):
    assert isinstance(instance.robotconfsendorderSeq_X, int)


@given(instance=MachineLibrary::RobotConfSendOrder_strategy)
def test_machinelibrary::robotconfsendorder_robotconfsendorderSeq_X_setter(instance):
    original = instance.robotconfsendorderSeq_X
    instance.robotconfsendorderSeq_X = original
    assert instance.robotconfsendorderSeq_X == original

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotvartobusycode_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotVarToBusycode)

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeSeq_X_type(instance):
    assert isinstance(instance.robotvartobusycodeSeq_X, int)


@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeSeq_X_setter(instance):
    original = instance.robotvartobusycodeSeq_X
    instance.robotvartobusycodeSeq_X = original
    assert instance.robotvartobusycodeSeq_X == original

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeUnit_X_type(instance):
    assert isinstance(instance.robotvartobusycodeUnit_X, int)


@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeUnit_X_setter(instance):
    original = instance.robotvartobusycodeUnit_X
    instance.robotvartobusycodeUnit_X = original
    assert instance.robotvartobusycodeUnit_X == original

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeBit_X_type(instance):
    assert isinstance(instance.robotvartobusycodeBit_X, int)


@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeBit_X_setter(instance):
    original = instance.robotvartobusycodeBit_X
    instance.robotvartobusycodeBit_X = original
    assert instance.robotvartobusycodeBit_X == original

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeType_X_type(instance):
    assert isinstance(instance.robotvartobusycodeType_X, str)


@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeType_X_setter(instance):
    original = instance.robotvartobusycodeType_X
    instance.robotvartobusycodeType_X = original
    assert instance.robotvartobusycodeType_X == original

@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeVar_X_type(instance):
    assert isinstance(instance.robotvartobusycodeVar_X, str)


@given(instance=MachineLibrary::RobotVarToBusycode_strategy)
def test_machinelibrary::robotvartobusycode_robotvartobusycodeVar_X_setter(instance):
    original = instance.robotvartobusycodeVar_X
    instance.robotvartobusycodeVar_X = original
    assert instance.robotvartobusycodeVar_X == original

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotvartoerrorbit_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotVarToErrorbit)

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitBit_X_type(instance):
    assert isinstance(instance.robotvartoerrorbitBit_X, int)


@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitBit_X_setter(instance):
    original = instance.robotvartoerrorbitBit_X
    instance.robotvartoerrorbitBit_X = original
    assert instance.robotvartoerrorbitBit_X == original

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitSeq_X_type(instance):
    assert isinstance(instance.robotvartoerrorbitSeq_X, int)


@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitSeq_X_setter(instance):
    original = instance.robotvartoerrorbitSeq_X
    instance.robotvartoerrorbitSeq_X = original
    assert instance.robotvartoerrorbitSeq_X == original

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitInv_X_type(instance):
    assert isinstance(instance.robotvartoerrorbitInv_X, int)


@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitInv_X_setter(instance):
    original = instance.robotvartoerrorbitInv_X
    instance.robotvartoerrorbitInv_X = original
    assert instance.robotvartoerrorbitInv_X == original

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitVar_X_type(instance):
    assert isinstance(instance.robotvartoerrorbitVar_X, str)


@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitVar_X_setter(instance):
    original = instance.robotvartoerrorbitVar_X
    instance.robotvartoerrorbitVar_X = original
    assert instance.robotvartoerrorbitVar_X == original

@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitType_X_type(instance):
    assert isinstance(instance.robotvartoerrorbitType_X, str)


@given(instance=MachineLibrary::RobotVarToErrorbit_strategy)
def test_machinelibrary::robotvartoerrorbit_robotvartoerrorbitType_X_setter(instance):
    original = instance.robotvartoerrorbitType_X
    instance.robotvartoerrorbitType_X = original
    assert instance.robotvartoerrorbitType_X == original

@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
@settings(max_examples=50)
def test_machinelibrary::plainmoveentrysend_instantiation(instance):
    assert isinstance(instance, MachineLibrary::PlainMoveEntrySend)

@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveSeq_type(instance):
    assert isinstance(instance.plainmoveSeq, int)


@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveSeq_setter(instance):
    original = instance.plainmoveSeq
    instance.plainmoveSeq = original
    assert instance.plainmoveSeq == original

@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveEntry_type(instance):
    assert isinstance(instance.plainmoveEntry, str)


@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveEntry_setter(instance):
    original = instance.plainmoveEntry
    instance.plainmoveEntry = original
    assert instance.plainmoveEntry == original

@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveSend_type(instance):
    assert isinstance(instance.plainmoveSend, str)


@given(instance=MachineLibrary::PlainMoveEntrySend_strategy)
def test_machinelibrary::plainmoveentrysend_plainmoveSend_setter(instance):
    original = instance.plainmoveSend
    instance.plainmoveSend = original
    assert instance.plainmoveSend == original

@given(instance=MachineLibrary::TransferFileSection_strategy)
@settings(max_examples=50)
def test_machinelibrary::transferfilesection_instantiation(instance):
    assert isinstance(instance, MachineLibrary::TransferFileSection)

@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferSection_type(instance):
    assert isinstance(instance.transferSection, str)


@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferSection_setter(instance):
    original = instance.transferSection
    instance.transferSection = original
    assert instance.transferSection == original

@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferFile_type(instance):
    assert isinstance(instance.transferFile, str)


@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferFile_setter(instance):
    original = instance.transferFile
    instance.transferFile = original
    assert instance.transferFile == original

@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferSeq_type(instance):
    assert isinstance(instance.transferSeq, int)


@given(instance=MachineLibrary::TransferFileSection_strategy)
def test_machinelibrary::transferfilesection_transferSeq_setter(instance):
    original = instance.transferSeq
    instance.transferSeq = original
    assert instance.transferSeq == original

@given(instance=MachineLibrary::RobotConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotConfiguration)

@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotSystemID_type(instance):
    assert isinstance(instance.robotSystemID, str)


@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotSystemID_setter(instance):
    original = instance.robotSystemID
    instance.robotSystemID = original
    assert instance.robotSystemID == original

@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotIPAddress_type(instance):
    assert isinstance(instance.robotIPAddress, str)


@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotIPAddress_setter(instance):
    original = instance.robotIPAddress
    instance.robotIPAddress = original
    assert instance.robotIPAddress == original

@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotID_type(instance):
    assert isinstance(instance.robotID, str)


@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotID_setter(instance):
    original = instance.robotID
    instance.robotID = original
    assert instance.robotID == original

@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotActivate_type(instance):
    assert isinstance(instance.robotActivate, int)


@given(instance=MachineLibrary::RobotConfiguration_strategy)
def test_machinelibrary::robotconfiguration_robotActivate_setter(instance):
    original = instance.robotActivate
    instance.robotActivate = original
    assert instance.robotActivate == original

@given(instance=MachineLibrary::RobotVarToErrorbits_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotvartoerrorbits_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotVarToErrorbits)

@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotwarningondelete_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotWarningONDelete)

@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotExtraPos_1_type(instance):
    assert isinstance(instance.robotExtraPos_1, str)


@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotExtraPos_1_setter(instance):
    original = instance.robotExtraPos_1
    instance.robotExtraPos_1 = original
    assert instance.robotExtraPos_1 == original

@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotExtraUnit_2_type(instance):
    assert isinstance(instance.robotExtraUnit_2, str)


@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotExtraUnit_2_setter(instance):
    original = instance.robotExtraUnit_2
    instance.robotExtraUnit_2 = original
    assert instance.robotExtraUnit_2 == original

@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_PM_type(instance):
    assert isinstance(instance.robotErrBitWhenConfirmationIsNeededFor_PM, int)


@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_PM_setter(instance):
    original = instance.robotErrBitWhenConfirmationIsNeededFor_PM
    instance.robotErrBitWhenConfirmationIsNeededFor_PM = original
    assert instance.robotErrBitWhenConfirmationIsNeededFor_PM == original

@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_Robot_type(instance):
    assert isinstance(instance.robotErrBitWhenConfirmationIsNeededFor_Robot, int)


@given(instance=MachineLibrary::RobotWarningONDelete_strategy)
def test_machinelibrary::robotwarningondelete_robotErrBitWhenConfirmationIsNeededFor_Robot_setter(instance):
    original = instance.robotErrBitWhenConfirmationIsNeededFor_Robot
    instance.robotErrBitWhenConfirmationIsNeededFor_Robot = original
    assert instance.robotErrBitWhenConfirmationIsNeededFor_Robot == original

@given(instance=MachineLibrary::RobotToWinccs_strategy)
@settings(max_examples=50)
def test_machinelibrary::robottowinccs_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotToWinccs)

@given(instance=MachineLibrary::RobotWinCCToRobots_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotwincctorobots_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotWinCCToRobots)

@given(instance=MachineLibrary::RobotConfSendOrders_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotconfsendorders_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotConfSendOrders)

@given(instance=MachineLibrary::RobotVarToBusyCodes_strategy)
@settings(max_examples=50)
def test_machinelibrary::robotvartobusycodes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RobotVarToBusyCodes)

@given(instance=MachineLibrary::Parameter_strategy)
@settings(max_examples=50)
def test_machinelibrary::parameter_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Parameter)

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterT2_type(instance):
    assert isinstance(instance.parameterT2, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterT2_setter(instance):
    original = instance.parameterT2
    instance.parameterT2 = original
    assert instance.parameterT2 == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterMin_type(instance):
    assert isinstance(instance.parameterMin, int)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterMin_setter(instance):
    original = instance.parameterMin
    instance.parameterMin = original
    assert instance.parameterMin == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV_type(instance):
    assert isinstance(instance.parameterV, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV_setter(instance):
    original = instance.parameterV
    instance.parameterV = original
    assert instance.parameterV == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterT1_type(instance):
    assert isinstance(instance.parameterT1, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterT1_setter(instance):
    original = instance.parameterT1
    instance.parameterT1 = original
    assert instance.parameterT1 == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterConfig_type(instance):
    assert isinstance(instance.parameterConfig, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterConfig_setter(instance):
    original = instance.parameterConfig
    instance.parameterConfig = original
    assert instance.parameterConfig == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterMax_type(instance):
    assert isinstance(instance.parameterMax, int)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterMax_setter(instance):
    original = instance.parameterMax
    instance.parameterMax = original
    assert instance.parameterMax == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV1_type(instance):
    assert isinstance(instance.parameterV1, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV1_setter(instance):
    original = instance.parameterV1
    instance.parameterV1 = original
    assert instance.parameterV1 == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterType_type(instance):
    assert isinstance(instance.parameterType, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterName_type(instance):
    assert isinstance(instance.parameterName, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterName_setter(instance):
    original = instance.parameterName
    instance.parameterName = original
    assert instance.parameterName == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV0_type(instance):
    assert isinstance(instance.parameterV0, str)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterV0_setter(instance):
    original = instance.parameterV0
    instance.parameterV0 = original
    assert instance.parameterV0 == original

@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterParaLen_type(instance):
    assert isinstance(instance.parameterParaLen, int)


@given(instance=MachineLibrary::Parameter_strategy)
def test_machinelibrary::parameter_parameterParaLen_setter(instance):
    original = instance.parameterParaLen
    instance.parameterParaLen = original
    assert instance.parameterParaLen == original

@given(instance=MachineLibrary::PlainMove_strategy)
@settings(max_examples=50)
def test_machinelibrary::plainmove_instantiation(instance):
    assert isinstance(instance, MachineLibrary::PlainMove)

@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmovePreDefWS_type(instance):
    assert isinstance(instance.plainmovePreDefWS, str)


@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmovePreDefWS_setter(instance):
    original = instance.plainmovePreDefWS
    instance.plainmovePreDefWS = original
    assert instance.plainmovePreDefWS == original

@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmoveType_type(instance):
    assert isinstance(instance.plainmoveType, int)


@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmoveType_setter(instance):
    original = instance.plainmoveType
    instance.plainmoveType = original
    assert instance.plainmoveType == original

@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmoveSID_REF_type(instance):
    assert isinstance(instance.plainmoveSID_REF, str)


@given(instance=MachineLibrary::PlainMove_strategy)
def test_machinelibrary::plainmove_plainmoveSID_REF_setter(instance):
    original = instance.plainmoveSID_REF
    instance.plainmoveSID_REF = original
    assert instance.plainmoveSID_REF == original

@given(instance=MachineLibrary::Transfer_strategy)
@settings(max_examples=50)
def test_machinelibrary::transfer_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Transfer)

@given(instance=MachineLibrary::ParamPrint_strategy)
@settings(max_examples=50)
def test_machinelibrary::paramprint_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ParamPrint)

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_fontHightData_type(instance):
    assert isinstance(instance.fontHightData, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_fontHightData_setter(instance):
    original = instance.fontHightData
    instance.fontHightData = original
    assert instance.fontHightData == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_horzPosLeftBorder_type(instance):
    assert isinstance(instance.horzPosLeftBorder, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_horzPosLeftBorder_setter(instance):
    original = instance.horzPosLeftBorder
    instance.horzPosLeftBorder = original
    assert instance.horzPosLeftBorder == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_fontHightHeader_type(instance):
    assert isinstance(instance.fontHightHeader, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_fontHightHeader_setter(instance):
    original = instance.fontHightHeader
    instance.fontHightHeader = original
    assert instance.fontHightHeader == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_dateStamp_type(instance):
    assert isinstance(instance.dateStamp, str)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_dateStamp_setter(instance):
    original = instance.dateStamp
    instance.dateStamp = original
    assert instance.dateStamp == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertPosData_type(instance):
    assert isinstance(instance.vertPosData, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertPosData_setter(instance):
    original = instance.vertPosData
    instance.vertPosData = original
    assert instance.vertPosData == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_horzPosValues_type(instance):
    assert isinstance(instance.horzPosValues, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_horzPosValues_setter(instance):
    original = instance.horzPosValues
    instance.horzPosValues = original
    assert instance.horzPosValues == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertPosHeader_type(instance):
    assert isinstance(instance.vertPosHeader, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertPosHeader_setter(instance):
    original = instance.vertPosHeader
    instance.vertPosHeader = original
    assert instance.vertPosHeader == original

@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertLineSpace_type(instance):
    assert isinstance(instance.vertLineSpace, float)


@given(instance=MachineLibrary::ParamPrint_strategy)
def test_machinelibrary::paramprint_vertLineSpace_setter(instance):
    original = instance.vertLineSpace
    instance.vertLineSpace = original
    assert instance.vertLineSpace == original

@given(instance=MachineLibrary::NodeProgram_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodeprogram_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeProgram)

@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programLenPerParam_type(instance):
    assert isinstance(instance.programLenPerParam, str)


@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programLenPerParam_setter(instance):
    original = instance.programLenPerParam
    instance.programLenPerParam = original
    assert instance.programLenPerParam == original

@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programSection_type(instance):
    assert isinstance(instance.programSection, str)


@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programSection_setter(instance):
    original = instance.programSection
    instance.programSection = original
    assert instance.programSection == original

@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programNo_type(instance):
    assert isinstance(instance.programNo, int)


@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programNo_setter(instance):
    original = instance.programNo
    instance.programNo = original
    assert instance.programNo == original

@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programName_type(instance):
    assert isinstance(instance.programName, str)


@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programName_setter(instance):
    original = instance.programName
    instance.programName = original
    assert instance.programName == original

@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programAddress_type(instance):
    assert isinstance(instance.programAddress, str)


@given(instance=MachineLibrary::NodeProgram_strategy)
def test_machinelibrary::nodeprogram_programAddress_setter(instance):
    original = instance.programAddress
    instance.programAddress = original
    assert instance.programAddress == original

@given(instance=MachineLibrary::Command_strategy)
@settings(max_examples=50)
def test_machinelibrary::command_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Command)

@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandProgParameter_type(instance):
    assert isinstance(instance.commandProgParameter, int)


@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandProgParameter_setter(instance):
    original = instance.commandProgParameter
    instance.commandProgParameter = original
    assert instance.commandProgParameter == original

@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandName_type(instance):
    assert isinstance(instance.commandName, str)


@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandName_setter(instance):
    original = instance.commandName
    instance.commandName = original
    assert instance.commandName == original

@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandNo_type(instance):
    assert isinstance(instance.commandNo, str)


@given(instance=MachineLibrary::Command_strategy)
def test_machinelibrary::command_commandNo_setter(instance):
    original = instance.commandNo
    instance.commandNo = original
    assert instance.commandNo == original

@given(instance=MachineLibrary::UnitProgParameters_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitprogparameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitProgParameters)

@given(instance=MachineLibrary::UnitProgParameters_strategy)
def test_machinelibrary::unitprogparameters_parameterNo_type(instance):
    assert isinstance(instance.parameterNo, int)


@given(instance=MachineLibrary::UnitProgParameters_strategy)
def test_machinelibrary::unitprogparameters_parameterNo_setter(instance):
    original = instance.parameterNo
    instance.parameterNo = original
    assert instance.parameterNo == original

@given(instance=MachineLibrary::UnitProgParameters_strategy)
def test_machinelibrary::unitprogparameters_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=MachineLibrary::UnitProgParameters_strategy)
def test_machinelibrary::unitprogparameters_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=MachineLibrary::UnitProgram_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitprogram_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitProgram)

@given(instance=MachineLibrary::UnitProgram_strategy)
def test_machinelibrary::unitprogram_unitProgName_type(instance):
    assert isinstance(instance.unitProgName, str)


@given(instance=MachineLibrary::UnitProgram_strategy)
def test_machinelibrary::unitprogram_unitProgName_setter(instance):
    original = instance.unitProgName
    instance.unitProgName = original
    assert instance.unitProgName == original

@given(instance=MachineLibrary::Position_strategy)
@settings(max_examples=50)
def test_machinelibrary::position_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Position)

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posWarningOnDelete_type(instance):
    assert isinstance(instance.posWarningOnDelete, int)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posWarningOnDelete_setter(instance):
    original = instance.posWarningOnDelete
    instance.posWarningOnDelete = original
    assert instance.posWarningOnDelete == original

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posExit_type(instance):
    assert isinstance(instance.posExit, int)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posExit_setter(instance):
    original = instance.posExit
    instance.posExit = original
    assert instance.posExit == original

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posName_type(instance):
    assert isinstance(instance.posName, str)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posName_setter(instance):
    original = instance.posName
    instance.posName = original
    assert instance.posName == original

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posIndex_type(instance):
    assert isinstance(instance.posIndex, int)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posIndex_setter(instance):
    original = instance.posIndex
    instance.posIndex = original
    assert instance.posIndex == original

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posRemark_type(instance):
    assert isinstance(instance.posRemark, str)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posRemark_setter(instance):
    original = instance.posRemark
    instance.posRemark = original
    assert instance.posRemark == original

@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posNo_type(instance):
    assert isinstance(instance.posNo, int)


@given(instance=MachineLibrary::Position_strategy)
def test_machinelibrary::position_posNo_setter(instance):
    original = instance.posNo
    instance.posNo = original
    assert instance.posNo == original

@given(instance=MachineLibrary::Button_strategy)
@settings(max_examples=50)
def test_machinelibrary::button_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Button)

@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_commandNo_type(instance):
    assert isinstance(instance.commandNo, int)


@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_commandNo_setter(instance):
    original = instance.commandNo
    instance.commandNo = original
    assert instance.commandNo == original

@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_buttonText_type(instance):
    assert isinstance(instance.buttonText, str)


@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_buttonText_setter(instance):
    original = instance.buttonText
    instance.buttonText = original
    assert instance.buttonText == original

@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_buttonNo_type(instance):
    assert isinstance(instance.buttonNo, int)


@given(instance=MachineLibrary::Button_strategy)
def test_machinelibrary::button_buttonNo_setter(instance):
    original = instance.buttonNo
    instance.buttonNo = original
    assert instance.buttonNo == original

@given(instance=MachineLibrary::CheckAddSID::Values::PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary::checkaddsid::values::pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckAddSID::Values::PM2PM)

@given(instance=MachineLibrary::CheckAddSID::Values::PM2PM_strategy)
def test_machinelibrary::checkaddsid::values::pm2pm_optionNo_type(instance):
    assert isinstance(instance.optionNo, int)


@given(instance=MachineLibrary::CheckAddSID::Values::PM2PM_strategy)
def test_machinelibrary::checkaddsid::values::pm2pm_optionNo_setter(instance):
    original = instance.optionNo
    instance.optionNo = original
    assert instance.optionNo == original

@given(instance=MachineLibrary::CheckAddSID::Values::PM2PM_strategy)
def test_machinelibrary::checkaddsid::values::pm2pm_optonValue_type(instance):
    assert isinstance(instance.optonValue, str)


@given(instance=MachineLibrary::CheckAddSID::Values::PM2PM_strategy)
def test_machinelibrary::checkaddsid::values::pm2pm_optonValue_setter(instance):
    original = instance.optonValue
    instance.optonValue = original
    assert instance.optonValue == original

@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary::sepbycomma::id::scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary::SepByComma::ID::Scanner)

@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idPrevValue_type(instance):
    assert isinstance(instance.idPrevValue, str)


@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idPrevValue_setter(instance):
    original = instance.idPrevValue
    instance.idPrevValue = original
    assert instance.idPrevValue == original

@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idCharValue_type(instance):
    assert isinstance(instance.idCharValue, str)


@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idCharValue_setter(instance):
    original = instance.idCharValue
    instance.idCharValue = original
    assert instance.idCharValue == original

@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idSeq_X_type(instance):
    assert isinstance(instance.idSeq_X, int)


@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idSeq_X_setter(instance):
    original = instance.idSeq_X
    instance.idSeq_X = original
    assert instance.idSeq_X == original

@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idValue_type(instance):
    assert isinstance(instance.idValue, int)


@given(instance=MachineLibrary::SepByComma::ID::Scanner_strategy)
def test_machinelibrary::sepbycomma::id::scanner_idValue_setter(instance):
    original = instance.idValue
    instance.idValue = original
    assert instance.idValue == original

@given(instance=MachineLibrary::SepByComma::Field::Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary::sepbycomma::field::scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary::SepByComma::Field::Scanner)

@given(instance=MachineLibrary::SepByComma::Field::Scanner_strategy)
def test_machinelibrary::sepbycomma::field::scanner_fieldNo_type(instance):
    assert isinstance(instance.fieldNo, int)


@given(instance=MachineLibrary::SepByComma::Field::Scanner_strategy)
def test_machinelibrary::sepbycomma::field::scanner_fieldNo_setter(instance):
    original = instance.fieldNo
    instance.fieldNo = original
    assert instance.fieldNo == original

@given(instance=MachineLibrary::SepByComma::Field::Scanner_strategy)
def test_machinelibrary::sepbycomma::field::scanner_fieldName_type(instance):
    assert isinstance(instance.fieldName, str)


@given(instance=MachineLibrary::SepByComma::Field::Scanner_strategy)
def test_machinelibrary::sepbycomma::field::scanner_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=MachineLibrary::StatusBit_strategy)
@settings(max_examples=50)
def test_machinelibrary::statusbit_instantiation(instance):
    assert isinstance(instance, MachineLibrary::StatusBit)

@given(instance=MachineLibrary::StatusBit_strategy)
def test_machinelibrary::statusbit_bitName_type(instance):
    assert isinstance(instance.bitName, str)


@given(instance=MachineLibrary::StatusBit_strategy)
def test_machinelibrary::statusbit_bitName_setter(instance):
    original = instance.bitName
    instance.bitName = original
    assert instance.bitName == original

@given(instance=MachineLibrary::StatusBit_strategy)
def test_machinelibrary::statusbit_bitNo_type(instance):
    assert isinstance(instance.bitNo, int)


@given(instance=MachineLibrary::StatusBit_strategy)
def test_machinelibrary::statusbit_bitNo_setter(instance):
    original = instance.bitNo
    instance.bitNo = original
    assert instance.bitNo == original

@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
@settings(max_examples=50)
def test_machinelibrary::historyconfig::accupyc_instantiation(instance):
    assert isinstance(instance, MachineLibrary::HistoryConfig::AccuPyc)

@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_sampleCupWeight_type(instance):
    assert isinstance(instance.sampleCupWeight, float)


@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_sampleCupWeight_setter(instance):
    original = instance.sampleCupWeight
    instance.sampleCupWeight = original
    assert instance.sampleCupWeight == original

@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_currentSample_type(instance):
    assert isinstance(instance.currentSample, str)


@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_currentSample_setter(instance):
    original = instance.currentSample
    instance.currentSample = original
    assert instance.currentSample == original

@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_currentSampleID_type(instance):
    assert isinstance(instance.currentSampleID, str)


@given(instance=MachineLibrary::HistoryConfig::AccuPyc_strategy)
def test_machinelibrary::historyconfig::accupyc_currentSampleID_setter(instance):
    original = instance.currentSampleID
    instance.currentSampleID = original
    assert instance.currentSampleID == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::checksampleconfig::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckSampleConfig::SuperQXRF)

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_minutes_type(instance):
    assert isinstance(instance.minutes, str)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_samples_type(instance):
    assert isinstance(instance.samples, str)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_samples_setter(instance):
    original = instance.samples
    instance.samples = original
    assert instance.samples == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_sampleID_type(instance):
    assert isinstance(instance.sampleID, str)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_sampleID_setter(instance):
    original = instance.sampleID
    instance.sampleID = original
    assert instance.sampleID == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_program_type(instance):
    assert isinstance(instance.program, str)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_program_setter(instance):
    original = instance.program
    instance.program = original
    assert instance.program == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_anaProg_type(instance):
    assert isinstance(instance.anaProg, str)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_anaProg_setter(instance):
    original = instance.anaProg
    instance.anaProg = original
    assert instance.anaProg == original

@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_seq_X_type(instance):
    assert isinstance(instance.seq_X, int)


@given(instance=MachineLibrary::CheckSampleConfig::SuperQXRF_strategy)
def test_machinelibrary::checksampleconfig::superqxrf_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original

@given(instance=MachineLibrary::InsertRemove::Keywords::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::insertremove::keywords::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::InsertRemove::Keywords::Host)

@given(instance=MachineLibrary::InsertRemove::Keywords::Host_strategy)
def test_machinelibrary::insertremove::keywords::host_keywordKey_type(instance):
    assert isinstance(instance.keywordKey, str)


@given(instance=MachineLibrary::InsertRemove::Keywords::Host_strategy)
def test_machinelibrary::insertremove::keywords::host_keywordKey_setter(instance):
    original = instance.keywordKey
    instance.keywordKey = original
    assert instance.keywordKey == original

@given(instance=MachineLibrary::InsertRemove::Keywords::Host_strategy)
def test_machinelibrary::insertremove::keywords::host_keywordValue_type(instance):
    assert isinstance(instance.keywordValue, str)


@given(instance=MachineLibrary::InsertRemove::Keywords::Host_strategy)
def test_machinelibrary::insertremove::keywords::host_keywordValue_setter(instance):
    original = instance.keywordValue
    instance.keywordValue = original
    assert instance.keywordValue == original

@given(instance=MachineLibrary::InsertRemove::Types::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::insertremove::types::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::InsertRemove::Types::Host)

@given(instance=MachineLibrary::InsertRemove::Types::Host_strategy)
def test_machinelibrary::insertremove::types::host_typeNo_type(instance):
    assert isinstance(instance.typeNo, int)


@given(instance=MachineLibrary::InsertRemove::Types::Host_strategy)
def test_machinelibrary::insertremove::types::host_typeNo_setter(instance):
    original = instance.typeNo
    instance.typeNo = original
    assert instance.typeNo == original

@given(instance=MachineLibrary::InsertRemove::Types::Host_strategy)
def test_machinelibrary::insertremove::types::host_typeValue_type(instance):
    assert isinstance(instance.typeValue, str)


@given(instance=MachineLibrary::InsertRemove::Types::Host_strategy)
def test_machinelibrary::insertremove::types::host_typeValue_setter(instance):
    original = instance.typeValue
    instance.typeValue = original
    assert instance.typeValue == original

@given(instance=MachineLibrary::InsertRemove::Entry::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::insertremove::entry::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::InsertRemove::Entry::Host)

@given(instance=MachineLibrary::InsertRemove::Entry::Host_strategy)
def test_machinelibrary::insertremove::entry::host_entryName_type(instance):
    assert isinstance(instance.entryName, str)


@given(instance=MachineLibrary::InsertRemove::Entry::Host_strategy)
def test_machinelibrary::insertremove::entry::host_entryName_setter(instance):
    original = instance.entryName
    instance.entryName = original
    assert instance.entryName == original

@given(instance=MachineLibrary::InsertRemove::Entry::Host_strategy)
def test_machinelibrary::insertremove::entry::host_entryNo_type(instance):
    assert isinstance(instance.entryNo, int)


@given(instance=MachineLibrary::InsertRemove::Entry::Host_strategy)
def test_machinelibrary::insertremove::entry::host_entryNo_setter(instance):
    original = instance.entryNo
    instance.entryNo = original
    assert instance.entryNo == original

@given(instance=MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::checksampleruntimeparams::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckSampleRunTimeParams::SuperQXRF)

@given(instance=MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy)
def test_machinelibrary::checksampleruntimeparams::superqxrf_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy)
def test_machinelibrary::checksampleruntimeparams::superqxrf_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy)
def test_machinelibrary::checksampleruntimeparams::superqxrf_sampleType_type(instance):
    assert isinstance(instance.sampleType, int)


@given(instance=MachineLibrary::CheckSampleRunTimeParams::SuperQXRF_strategy)
def test_machinelibrary::checksampleruntimeparams::superqxrf_sampleType_setter(instance):
    original = instance.sampleType
    instance.sampleType = original
    assert instance.sampleType == original

@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
@settings(max_examples=50)
def test_machinelibrary::oes::xrf::condition_instantiation(instance):
    assert isinstance(instance, MachineLibrary::OES::XRF::Condition)

@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_seq_X_type(instance):
    assert isinstance(instance.seq_X, int)


@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original

@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_paraName_type(instance):
    assert isinstance(instance.paraName, str)


@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_paraName_setter(instance):
    original = instance.paraName
    instance.paraName = original
    assert instance.paraName == original

@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_para_type(instance):
    assert isinstance(instance.para, str)


@given(instance=MachineLibrary::OES::XRF::Condition_strategy)
def test_machinelibrary::oes::xrf::condition_para_setter(instance):
    original = instance.para
    instance.para = original
    assert instance.para == original

@given(instance=MachineLibrary::InsertRemove::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::insertremove::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::InsertRemove::Host)

@given(instance=MachineLibrary::InsertRemove::Host_strategy)
def test_machinelibrary::insertremove::host_report_All_type(instance):
    assert isinstance(instance.report_All, int)


@given(instance=MachineLibrary::InsertRemove::Host_strategy)
def test_machinelibrary::insertremove::host_report_All_setter(instance):
    original = instance.report_All
    instance.report_All = original
    assert instance.report_All == original

@given(instance=MachineLibrary::Moved::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::moved::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Moved::Host)

@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_pos0_type(instance):
    assert isinstance(instance.pos0, int)


@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_pos0_setter(instance):
    original = instance.pos0
    instance.pos0 = original
    assert instance.pos0 == original

@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_report_ALL_type(instance):
    assert isinstance(instance.report_ALL, int)


@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_report_ALL_setter(instance):
    original = instance.report_ALL
    instance.report_ALL = original
    assert instance.report_ALL == original

@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_writePositionNameInFile_type(instance):
    assert isinstance(instance.writePositionNameInFile, int)


@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_writePositionNameInFile_setter(instance):
    original = instance.writePositionNameInFile
    instance.writePositionNameInFile = original
    assert instance.writePositionNameInFile == original

@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_type0_type(instance):
    assert isinstance(instance.type0, int)


@given(instance=MachineLibrary::Moved::Host_strategy)
def test_machinelibrary::moved::host_type0_setter(instance):
    original = instance.type0
    instance.type0 = original
    assert instance.type0 == original

@given(instance=MachineLibrary::WS::Update::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::ws::update::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::WS::Update::Host)

@given(instance=MachineLibrary::WS::Update::Host_strategy)
def test_machinelibrary::ws::update::host_AllowUnit0_type(instance):
    assert isinstance(instance.AllowUnit0, int)


@given(instance=MachineLibrary::WS::Update::Host_strategy)
def test_machinelibrary::ws::update::host_AllowUnit0_setter(instance):
    original = instance.AllowUnit0
    instance.AllowUnit0 = original
    assert instance.AllowUnit0 == original

@given(instance=MachineLibrary::WS::Update::Host_strategy)
def test_machinelibrary::ws::update::host_checkUnit_type(instance):
    assert isinstance(instance.checkUnit, int)


@given(instance=MachineLibrary::WS::Update::Host_strategy)
def test_machinelibrary::ws::update::host_checkUnit_setter(instance):
    original = instance.checkUnit
    instance.checkUnit = original
    assert instance.checkUnit == original

@given(instance=MachineLibrary::Report::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::report::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Report::Host)

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_fileName_type(instance):
    assert isinstance(instance.fileName, str)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_stateChanged_type(instance):
    assert isinstance(instance.stateChanged, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_stateChanged_setter(instance):
    original = instance.stateChanged
    instance.stateChanged = original
    assert instance.stateChanged == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_maxType_type(instance):
    assert isinstance(instance.maxType, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_maxType_setter(instance):
    original = instance.maxType
    instance.maxType = original
    assert instance.maxType == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_timeStamp_type(instance):
    assert isinstance(instance.timeStamp, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_timeStamp_setter(instance):
    original = instance.timeStamp
    instance.timeStamp = original
    assert instance.timeStamp == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleInsert_type(instance):
    assert isinstance(instance.sampleInsert, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleInsert_setter(instance):
    original = instance.sampleInsert
    instance.sampleInsert = original
    assert instance.sampleInsert == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sendErrorWarningsMsgOnly_type(instance):
    assert isinstance(instance.sendErrorWarningsMsgOnly, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sendErrorWarningsMsgOnly_setter(instance):
    original = instance.sendErrorWarningsMsgOnly
    instance.sendErrorWarningsMsgOnly = original
    assert instance.sendErrorWarningsMsgOnly == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sendLifeMessages_type(instance):
    assert isinstance(instance.sendLifeMessages, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sendLifeMessages_setter(instance):
    original = instance.sendLifeMessages
    instance.sendLifeMessages = original
    assert instance.sendLifeMessages == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_note1_type(instance):
    assert isinstance(instance.note1, str)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_note1_setter(instance):
    original = instance.note1
    instance.note1 = original
    assert instance.note1 == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_minType_type(instance):
    assert isinstance(instance.minType, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_minType_setter(instance):
    original = instance.minType
    instance.minType = original
    assert instance.minType == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleMoved_type(instance):
    assert isinstance(instance.sampleMoved, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleMoved_setter(instance):
    original = instance.sampleMoved
    instance.sampleMoved = original
    assert instance.sampleMoved == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_internal_type(instance):
    assert isinstance(instance.internal, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_internal_setter(instance):
    original = instance.internal
    instance.internal = original
    assert instance.internal == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleRemoved_type(instance):
    assert isinstance(instance.sampleRemoved, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_sampleRemoved_setter(instance):
    original = instance.sampleRemoved
    instance.sampleRemoved = original
    assert instance.sampleRemoved == original

@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_rawData_type(instance):
    assert isinstance(instance.rawData, int)


@given(instance=MachineLibrary::Report::Host_strategy)
def test_machinelibrary::report::host_rawData_setter(instance):
    original = instance.rawData
    instance.rawData = original
    assert instance.rawData == original

@given(instance=MachineLibrary::Settings::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::settings::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Settings::ARL::XRF::OES)

@given(instance=MachineLibrary::Settings::ARL::XRF::OES_strategy)
def test_machinelibrary::settings::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::Settings::ARL::XRF::OES_strategy)
def test_machinelibrary::settings::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::DisableSCT::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::disablesct::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::DisableSCT::ARL::XRF::OES)

@given(instance=MachineLibrary::DisableSCT::ARL::XRF::OES_strategy)
def test_machinelibrary::disablesct::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::DisableSCT::ARL::XRF::OES_strategy)
def test_machinelibrary::disablesct::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::exeaskprepunit::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES)

@given(instance=MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::exeaskprepunit::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::exeaskprepunit::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::checkaskprepunit::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES)

@given(instance=MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::checkaskprepunit::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::checkaskprepunit::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::ExePrepUnit::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::exeprepunit::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ExePrepUnit::ARL::XRF::OES)

@given(instance=MachineLibrary::ExePrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::exeprepunit::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::ExePrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::exeprepunit::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::checkreqprepunit::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES)

@given(instance=MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::checkreqprepunit::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES_strategy)
def test_machinelibrary::checkreqprepunit::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::ExecuteFiling::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::executefiling::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ExecuteFiling::ARL::XRF::OES)

@given(instance=MachineLibrary::ExecuteFiling::ARL::XRF::OES_strategy)
def test_machinelibrary::executefiling::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::ExecuteFiling::ARL::XRF::OES_strategy)
def test_machinelibrary::executefiling::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::CheckFilling::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::checkfilling::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckFilling::ARL::XRF::OES)

@given(instance=MachineLibrary::CheckFilling::ARL::XRF::OES_strategy)
def test_machinelibrary::checkfilling::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::CheckFilling::ARL::XRF::OES_strategy)
def test_machinelibrary::checkfilling::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::CheckSample::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::checksample::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckSample::SuperQXRF)

@given(instance=MachineLibrary::CheckSampleRunTime::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::checksampleruntime::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckSampleRunTime::SuperQXRF)

@given(instance=MachineLibrary::Communication::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::communication::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Communication::SuperQXRF)

@given(instance=MachineLibrary::Communication::SuperQXRF_strategy)
def test_machinelibrary::communication::superqxrf_enq_ACK_Protocol_type(instance):
    assert isinstance(instance.enq_ACK_Protocol, int)


@given(instance=MachineLibrary::Communication::SuperQXRF_strategy)
def test_machinelibrary::communication::superqxrf_enq_ACK_Protocol_setter(instance):
    original = instance.enq_ACK_Protocol
    instance.enq_ACK_Protocol = original
    assert instance.enq_ACK_Protocol == original

@given(instance=MachineLibrary::ControlSamples::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::controlsamples::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ControlSamples::SuperQXRF)

@given(instance=MachineLibrary::ControlSamples::SuperQXRF_strategy)
def test_machinelibrary::controlsamples::superqxrf_outOfControl_type(instance):
    assert isinstance(instance.outOfControl, int)


@given(instance=MachineLibrary::ControlSamples::SuperQXRF_strategy)
def test_machinelibrary::controlsamples::superqxrf_outOfControl_setter(instance):
    original = instance.outOfControl
    instance.outOfControl = original
    assert instance.outOfControl == original

@given(instance=MachineLibrary::File::Sample::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::file::sample::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::File::Sample::ARL::XRF::OES)

@given(instance=MachineLibrary::File::Sample::ARL::XRF::OES_strategy)
def test_machinelibrary::file::sample::arl::xrf::oes_noSuccess_type(instance):
    assert isinstance(instance.noSuccess, str)


@given(instance=MachineLibrary::File::Sample::ARL::XRF::OES_strategy)
def test_machinelibrary::file::sample::arl::xrf::oes_noSuccess_setter(instance):
    original = instance.noSuccess
    instance.noSuccess = original
    assert instance.noSuccess == original

@given(instance=MachineLibrary::PS::Process::Finished::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::ps::process::finished::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::PS::Process::Finished::ARL::XRF::OES)

@given(instance=MachineLibrary::PS::Process::Finished::ARL::XRF::OES_strategy)
def test_machinelibrary::ps::process::finished::arl::xrf::oes_noSuccess_type(instance):
    assert isinstance(instance.noSuccess, str)


@given(instance=MachineLibrary::PS::Process::Finished::ARL::XRF::OES_strategy)
def test_machinelibrary::ps::process::finished::arl::xrf::oes_noSuccess_setter(instance):
    original = instance.noSuccess
    instance.noSuccess = original
    assert instance.noSuccess == original

@given(instance=MachineLibrary::GeneralSetting::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::generalsetting::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::GeneralSetting::ARL::XRF::OES)

@given(instance=MachineLibrary::GeneralSetting::ARL::XRF::OES_strategy)
def test_machinelibrary::generalsetting::arl::xrf::oes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::GeneralSetting::ARL::XRF::OES_strategy)
def test_machinelibrary::generalsetting::arl::xrf::oes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::CheckAddSID::PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary::checkaddsid::pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CheckAddSID::PM2PM)

@given(instance=MachineLibrary::SepByComma::Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary::sepbycomma::scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary::SepByComma::Scanner)

@given(instance=MachineLibrary::SepByComma::Scanner_strategy)
def test_machinelibrary::sepbycomma::scanner_activ_type(instance):
    assert isinstance(instance.activ, int)


@given(instance=MachineLibrary::SepByComma::Scanner_strategy)
def test_machinelibrary::sepbycomma::scanner_activ_setter(instance):
    original = instance.activ
    instance.activ = original
    assert instance.activ == original

@given(instance=MachineLibrary::SepByComma::Scanner_strategy)
def test_machinelibrary::sepbycomma::scanner_preDefWS_type(instance):
    assert isinstance(instance.preDefWS, int)


@given(instance=MachineLibrary::SepByComma::Scanner_strategy)
def test_machinelibrary::sepbycomma::scanner_preDefWS_setter(instance):
    original = instance.preDefWS
    instance.preDefWS = original
    assert instance.preDefWS == original

@given(instance=MachineLibrary::History::AccuPycMeter_strategy)
@settings(max_examples=50)
def test_machinelibrary::history::accupycmeter_instantiation(instance):
    assert isinstance(instance, MachineLibrary::History::AccuPycMeter)

@given(instance=MachineLibrary::UnitConfig::Host_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitconfig::host_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitConfig::Host)

@given(instance=MachineLibrary::UnitConfig::ARL::XRF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitconfig::arl::xrf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitConfig::ARL::XRF::OES)

@given(instance=MachineLibrary::UnitConfig::SuperQ::XRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitconfig::superq::xrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitConfig::SuperQ::XRF)

@given(instance=MachineLibrary::UnitConfig::OBLF::OES_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitconfig::oblf::oes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitConfig::OBLF::OES)

@given(instance=MachineLibrary::UnitConfig::Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitconfig::terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitConfig::Terminal)

@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::generalparameter::superqxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::GeneralParameter::SuperQXRF)

@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_listName_type(instance):
    assert isinstance(instance.listName, str)


@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_listName_setter(instance):
    original = instance.listName
    instance.listName = original
    assert instance.listName == original

@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_switchRemote_type(instance):
    assert isinstance(instance.switchRemote, str)


@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_switchRemote_setter(instance):
    original = instance.switchRemote
    instance.switchRemote = original
    assert instance.switchRemote == original

@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_startList_type(instance):
    assert isinstance(instance.startList, str)


@given(instance=MachineLibrary::GeneralParameter::SuperQXRF_strategy)
def test_machinelibrary::generalparameter::superqxrf_startList_setter(instance):
    original = instance.startList
    instance.startList = original
    assert instance.startList == original

@given(instance=MachineLibrary::ErrorMessage::OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary::errormessage::oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::ErrorMessage::OBLFOES)

@given(instance=MachineLibrary::ErrorMessage::OBLFOES_strategy)
def test_machinelibrary::errormessage::oblfoes_errorMessage_type(instance):
    assert isinstance(instance.errorMessage, str)


@given(instance=MachineLibrary::ErrorMessage::OBLFOES_strategy)
def test_machinelibrary::errormessage::oblfoes_errorMessage_setter(instance):
    original = instance.errorMessage
    instance.errorMessage = original
    assert instance.errorMessage == original

@given(instance=MachineLibrary::RecalRequest::OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary::recalrequest::oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::RecalRequest::OBLFOES)

@given(instance=MachineLibrary::RecalRequest::OBLFOES_strategy)
def test_machinelibrary::recalrequest::oblfoes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::RecalRequest::OBLFOES_strategy)
def test_machinelibrary::recalrequest::oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::TestRequest::OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary::testrequest::oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::TestRequest::OBLFOES)

@given(instance=MachineLibrary::TestRequest::OBLFOES_strategy)
def test_machinelibrary::testrequest::oblfoes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::TestRequest::OBLFOES_strategy)
def test_machinelibrary::testrequest::oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::OutputRequest::OBLFOES_strategy)
@settings(max_examples=50)
def test_machinelibrary::outputrequest::oblfoes_instantiation(instance):
    assert isinstance(instance, MachineLibrary::OutputRequest::OBLFOES)

@given(instance=MachineLibrary::OutputRequest::OBLFOES_strategy)
def test_machinelibrary::outputrequest::oblfoes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MachineLibrary::OutputRequest::OBLFOES_strategy)
def test_machinelibrary::outputrequest::oblfoes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MachineLibrary::Translate::Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary::translate::terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Translate::Terminal)

@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_auto_Ready_type(instance):
    assert isinstance(instance.auto_Ready, str)


@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_auto_Ready_setter(instance):
    original = instance.auto_Ready
    instance.auto_Ready = original
    assert instance.auto_Ready == original

@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_man_Ready_type(instance):
    assert isinstance(instance.man_Ready, str)


@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_man_Ready_setter(instance):
    original = instance.man_Ready
    instance.man_Ready = original
    assert instance.man_Ready == original

@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_man_Busy_type(instance):
    assert isinstance(instance.man_Busy, str)


@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_man_Busy_setter(instance):
    original = instance.man_Busy
    instance.man_Busy = original
    assert instance.man_Busy == original

@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_auto_Busy_type(instance):
    assert isinstance(instance.auto_Busy, str)


@given(instance=MachineLibrary::Translate::Terminal_strategy)
def test_machinelibrary::translate::terminal_auto_Busy_setter(instance):
    original = instance.auto_Busy
    instance.auto_Busy = original
    assert instance.auto_Busy == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::scanner_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::Scanner)

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_start_type(instance):
    assert isinstance(instance.start, int)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_length_type(instance):
    assert isinstance(instance.length, int)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_preString_type(instance):
    assert isinstance(instance.preString, str)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_preString_setter(instance):
    original = instance.preString
    instance.preString = original
    assert instance.preString == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_registerSample_type(instance):
    assert isinstance(instance.registerSample, int)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_registerSample_setter(instance):
    original = instance.registerSample
    instance.registerSample = original
    assert instance.registerSample == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_forcedSampleType_type(instance):
    assert isinstance(instance.forcedSampleType, int)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_forcedSampleType_setter(instance):
    original = instance.forcedSampleType
    instance.forcedSampleType = original
    assert instance.forcedSampleType == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_fillWith_type(instance):
    assert isinstance(instance.fillWith, str)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_fillWith_setter(instance):
    original = instance.fillWith
    instance.fillWith = original
    assert instance.fillWith == original

@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_addString_type(instance):
    assert isinstance(instance.addString, str)


@given(instance=MachineLibrary::UnitGeneral::Scanner_strategy)
def test_machinelibrary::unitgeneral::scanner_addString_setter(instance):
    original = instance.addString
    instance.addString = original
    assert instance.addString == original

@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::rigakuxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::RigakuXRF)

@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPoHAG_SIInstrument_type(instance):
    assert isinstance(instance.lastPoHAG_SIInstrument, int)


@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPoHAG_SIInstrument_setter(instance):
    original = instance.lastPoHAG_SIInstrument
    instance.lastPoHAG_SIInstrument = original
    assert instance.lastPoHAG_SIInstrument == original

@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPosInInstrument_type(instance):
    assert isinstance(instance.lastPosInInstrument, int)


@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPosInInstrument_setter(instance):
    original = instance.lastPosInInstrument
    instance.lastPosInInstrument = original
    assert instance.lastPosInInstrument == original

@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_separator_type(instance):
    assert isinstance(instance.separator, int)


@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_separator_setter(instance):
    original = instance.separator
    instance.separator = original
    assert instance.separator == original

@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPosAnalyHAG_SIg_type(instance):
    assert isinstance(instance.lastPosAnalyHAG_SIg, int)


@given(instance=MachineLibrary::UnitGeneral::RigakuXRF_strategy)
def test_machinelibrary::unitgeneral::rigakuxrf_lastPosAnalyHAG_SIg_setter(instance):
    original = instance.lastPosAnalyHAG_SIg
    instance.lastPosAnalyHAG_SIg = original
    assert instance.lastPosAnalyHAG_SIg == original

@given(instance=MachineLibrary::UnitGeneral::SuperQ_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::superq_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::SuperQ)

@given(instance=MachineLibrary::UnitGeneral::SuperQ_strategy)
def test_machinelibrary::unitgeneral::superq_lastPosAnalysing_type(instance):
    assert isinstance(instance.lastPosAnalysing, int)


@given(instance=MachineLibrary::UnitGeneral::SuperQ_strategy)
def test_machinelibrary::unitgeneral::superq_lastPosAnalysing_setter(instance):
    original = instance.lastPosAnalysing
    instance.lastPosAnalysing = original
    assert instance.lastPosAnalysing == original

@given(instance=MachineLibrary::UnitGeneral::SuperQ_strategy)
def test_machinelibrary::unitgeneral::superq_lastPosInInstrument_type(instance):
    assert isinstance(instance.lastPosInInstrument, int)


@given(instance=MachineLibrary::UnitGeneral::SuperQ_strategy)
def test_machinelibrary::unitgeneral::superq_lastPosInInstrument_setter(instance):
    original = instance.lastPosInInstrument
    instance.lastPosInInstrument = original
    assert instance.lastPosInInstrument == original

@given(instance=MachineLibrary::UnitGeneral::AccPyc_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::accpyc_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::AccPyc)

@given(instance=MachineLibrary::UnitGeneral::AccPyc_strategy)
def test_machinelibrary::unitgeneral::accpyc_minSampleWeight_type(instance):
    assert isinstance(instance.minSampleWeight, float)


@given(instance=MachineLibrary::UnitGeneral::AccPyc_strategy)
def test_machinelibrary::unitgeneral::accpyc_minSampleWeight_setter(instance):
    original = instance.minSampleWeight
    instance.minSampleWeight = original
    assert instance.minSampleWeight == original

@given(instance=MachineLibrary::UnitGeneral::AccPyc_strategy)
def test_machinelibrary::unitgeneral::accpyc_cupWeight_type(instance):
    assert isinstance(instance.cupWeight, float)


@given(instance=MachineLibrary::UnitGeneral::AccPyc_strategy)
def test_machinelibrary::unitgeneral::accpyc_cupWeight_setter(instance):
    original = instance.cupWeight
    instance.cupWeight = original
    assert instance.cupWeight == original

@given(instance=MachineLibrary::UnitGeneral::PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::PM2PM)

@given(instance=MachineLibrary::UnitGeneral::PM2PM_strategy)
def test_machinelibrary::unitgeneral::pm2pm_processFeedBack_type(instance):
    assert isinstance(instance.processFeedBack, str)


@given(instance=MachineLibrary::UnitGeneral::PM2PM_strategy)
def test_machinelibrary::unitgeneral::pm2pm_processFeedBack_setter(instance):
    original = instance.processFeedBack
    instance.processFeedBack = original
    assert instance.processFeedBack == original

@given(instance=MachineLibrary::UnitGeneral::PM2PM_strategy)
def test_machinelibrary::unitgeneral::pm2pm_sid_Mask_type(instance):
    assert isinstance(instance.sid_Mask, str)


@given(instance=MachineLibrary::UnitGeneral::PM2PM_strategy)
def test_machinelibrary::unitgeneral::pm2pm_sid_Mask_setter(instance):
    original = instance.sid_Mask
    instance.sid_Mask = original
    assert instance.sid_Mask == original

@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::remote_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::Remote)

@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeA_type(instance):
    assert isinstance(instance.handshakeA, str)


@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeA_setter(instance):
    original = instance.handshakeA
    instance.handshakeA = original
    assert instance.handshakeA == original

@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeQ_type(instance):
    assert isinstance(instance.handshakeQ, str)


@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeQ_setter(instance):
    original = instance.handshakeQ
    instance.handshakeQ = original
    assert instance.handshakeQ == original

@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeT_type(instance):
    assert isinstance(instance.handshakeT, int)


@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_handshakeT_setter(instance):
    original = instance.handshakeT
    instance.handshakeT = original
    assert instance.handshakeT == original

@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_editWSDB_type(instance):
    assert isinstance(instance.editWSDB, bool)


@given(instance=MachineLibrary::UnitGeneral::Remote_strategy)
def test_machinelibrary::unitgeneral::remote_editWSDB_setter(instance):
    original = instance.editWSDB
    instance.editWSDB = original
    assert instance.editWSDB == original

@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::hostpc_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::HostPC)

@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_writeDumyIfNoDataExist_type(instance):
    assert isinstance(instance.writeDumyIfNoDataExist, int)


@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_writeDumyIfNoDataExist_setter(instance):
    original = instance.writeDumyIfNoDataExist
    instance.writeDumyIfNoDataExist = original
    assert instance.writeDumyIfNoDataExist == original

@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_replyOnLink_type(instance):
    assert isinstance(instance.replyOnLink, int)


@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_replyOnLink_setter(instance):
    original = instance.replyOnLink
    instance.replyOnLink = original
    assert instance.replyOnLink == original

@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_index_type(instance):
    assert isinstance(instance.index, int)


@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_maxIndex_type(instance):
    assert isinstance(instance.maxIndex, int)


@given(instance=MachineLibrary::UnitGeneral::HostPC_strategy)
def test_machinelibrary::unitgeneral::hostpc_maxIndex_setter(instance):
    original = instance.maxIndex
    instance.maxIndex = original
    assert instance.maxIndex == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral::terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral::Terminal)

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station5_type(instance):
    assert isinstance(instance.station5, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station5_setter(instance):
    original = instance.station5
    instance.station5 = original
    assert instance.station5 == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station3_type(instance):
    assert isinstance(instance.station3, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station3_setter(instance):
    original = instance.station3
    instance.station3 = original
    assert instance.station3 == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_thisStation_type(instance):
    assert isinstance(instance.thisStation, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_thisStation_setter(instance):
    original = instance.thisStation
    instance.thisStation = original
    assert instance.thisStation == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station1_type(instance):
    assert isinstance(instance.station1, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station1_setter(instance):
    original = instance.station1
    instance.station1 = original
    assert instance.station1 == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station4_type(instance):
    assert isinstance(instance.station4, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station4_setter(instance):
    original = instance.station4
    instance.station4 = original
    assert instance.station4 == original

@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station2_type(instance):
    assert isinstance(instance.station2, str)


@given(instance=MachineLibrary::UnitGeneral::Terminal_strategy)
def test_machinelibrary::unitgeneral::terminal_station2_setter(instance):
    original = instance.station2
    instance.station2 = original
    assert instance.station2 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
@settings(max_examples=50)
def test_machinelibrary::plctopmmatrix_instantiation(instance):
    assert isinstance(instance, MachineLibrary::PLCtoPmMatrix)

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit0_type(instance):
    assert isinstance(instance.plcpmmatrixBit0, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit0_setter(instance):
    original = instance.plcpmmatrixBit0
    instance.plcpmmatrixBit0 = original
    assert instance.plcpmmatrixBit0 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit15_type(instance):
    assert isinstance(instance.plcpmmatrixBit15, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit15_setter(instance):
    original = instance.plcpmmatrixBit15
    instance.plcpmmatrixBit15 = original
    assert instance.plcpmmatrixBit15 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit2_type(instance):
    assert isinstance(instance.plcpmmatrixBit2, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit2_setter(instance):
    original = instance.plcpmmatrixBit2
    instance.plcpmmatrixBit2 = original
    assert instance.plcpmmatrixBit2 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit7_type(instance):
    assert isinstance(instance.plcpmmatrixBit7, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit7_setter(instance):
    original = instance.plcpmmatrixBit7
    instance.plcpmmatrixBit7 = original
    assert instance.plcpmmatrixBit7 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit9_type(instance):
    assert isinstance(instance.plcpmmatrixBit9, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit9_setter(instance):
    original = instance.plcpmmatrixBit9
    instance.plcpmmatrixBit9 = original
    assert instance.plcpmmatrixBit9 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit11_type(instance):
    assert isinstance(instance.plcpmmatrixBit11, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit11_setter(instance):
    original = instance.plcpmmatrixBit11
    instance.plcpmmatrixBit11 = original
    assert instance.plcpmmatrixBit11 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit13_type(instance):
    assert isinstance(instance.plcpmmatrixBit13, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit13_setter(instance):
    original = instance.plcpmmatrixBit13
    instance.plcpmmatrixBit13 = original
    assert instance.plcpmmatrixBit13 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit6_type(instance):
    assert isinstance(instance.plcpmmatrixBit6, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit6_setter(instance):
    original = instance.plcpmmatrixBit6
    instance.plcpmmatrixBit6 = original
    assert instance.plcpmmatrixBit6 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit12_type(instance):
    assert isinstance(instance.plcpmmatrixBit12, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit12_setter(instance):
    original = instance.plcpmmatrixBit12
    instance.plcpmmatrixBit12 = original
    assert instance.plcpmmatrixBit12 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit1_type(instance):
    assert isinstance(instance.plcpmmatrixBit1, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit1_setter(instance):
    original = instance.plcpmmatrixBit1
    instance.plcpmmatrixBit1 = original
    assert instance.plcpmmatrixBit1 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit14_type(instance):
    assert isinstance(instance.plcpmmatrixBit14, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit14_setter(instance):
    original = instance.plcpmmatrixBit14
    instance.plcpmmatrixBit14 = original
    assert instance.plcpmmatrixBit14 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit3_type(instance):
    assert isinstance(instance.plcpmmatrixBit3, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit3_setter(instance):
    original = instance.plcpmmatrixBit3
    instance.plcpmmatrixBit3 = original
    assert instance.plcpmmatrixBit3 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit8_type(instance):
    assert isinstance(instance.plcpmmatrixBit8, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit8_setter(instance):
    original = instance.plcpmmatrixBit8
    instance.plcpmmatrixBit8 = original
    assert instance.plcpmmatrixBit8 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit4_type(instance):
    assert isinstance(instance.plcpmmatrixBit4, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit4_setter(instance):
    original = instance.plcpmmatrixBit4
    instance.plcpmmatrixBit4 = original
    assert instance.plcpmmatrixBit4 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit5_type(instance):
    assert isinstance(instance.plcpmmatrixBit5, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit5_setter(instance):
    original = instance.plcpmmatrixBit5
    instance.plcpmmatrixBit5 = original
    assert instance.plcpmmatrixBit5 == original

@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit10_type(instance):
    assert isinstance(instance.plcpmmatrixBit10, int)


@given(instance=MachineLibrary::PLCtoPmMatrix_strategy)
def test_machinelibrary::plctopmmatrix_plcpmmatrixBit10_setter(instance):
    original = instance.plcpmmatrixBit10
    instance.plcpmmatrixBit10 = original
    assert instance.plcpmmatrixBit10 == original

@given(instance=MachineLibrary::StausBits_strategy)
@settings(max_examples=50)
def test_machinelibrary::stausbits_instantiation(instance):
    assert isinstance(instance, MachineLibrary::StausBits)

@given(instance=MachineLibrary::Positions_strategy)
@settings(max_examples=50)
def test_machinelibrary::positions_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Positions)

@given(instance=MachineLibrary::WinCCAddTag_strategy)
@settings(max_examples=50)
def test_machinelibrary::winccaddtag_instantiation(instance):
    assert isinstance(instance, MachineLibrary::WinCCAddTag)

@given(instance=MachineLibrary::WinCCAddTag_strategy)
def test_machinelibrary::winccaddtag_winCCTag_type(instance):
    assert isinstance(instance.winCCTag, str)


@given(instance=MachineLibrary::WinCCAddTag_strategy)
def test_machinelibrary::winccaddtag_winCCTag_setter(instance):
    original = instance.winCCTag
    instance.winCCTag = original
    assert instance.winCCTag == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneralparameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneralParameters)

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_minValue_1_type(instance):
    assert isinstance(instance.minValue_1, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_minValue_1_setter(instance):
    original = instance.minValue_1
    instance.minValue_1 = original
    assert instance.minValue_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_UseWith_1_type(instance):
    assert isinstance(instance.UseWith_1, str)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_UseWith_1_setter(instance):
    original = instance.UseWith_1
    instance.UseWith_1 = original
    assert instance.UseWith_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_defaultValue_1_type(instance):
    assert isinstance(instance.defaultValue_1, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_defaultValue_1_setter(instance):
    original = instance.defaultValue_1
    instance.defaultValue_1 = original
    assert instance.defaultValue_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_unit_1_type(instance):
    assert isinstance(instance.unit_1, str)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_unit_1_setter(instance):
    original = instance.unit_1
    instance.unit_1 = original
    assert instance.unit_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_seq_X_type(instance):
    assert isinstance(instance.seq_X, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_seq_X_setter(instance):
    original = instance.seq_X
    instance.seq_X = original
    assert instance.seq_X == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_comment_1_type(instance):
    assert isinstance(instance.comment_1, str)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_comment_1_setter(instance):
    original = instance.comment_1
    instance.comment_1 = original
    assert instance.comment_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_canBeChange_1_type(instance):
    assert isinstance(instance.canBeChange_1, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_canBeChange_1_setter(instance):
    original = instance.canBeChange_1
    instance.canBeChange_1 = original
    assert instance.canBeChange_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_maxValue_1_type(instance):
    assert isinstance(instance.maxValue_1, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_maxValue_1_setter(instance):
    original = instance.maxValue_1
    instance.maxValue_1 = original
    assert instance.maxValue_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_KeyWord_1_type(instance):
    assert isinstance(instance.KeyWord_1, str)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_KeyWord_1_setter(instance):
    original = instance.KeyWord_1
    instance.KeyWord_1 = original
    assert instance.KeyWord_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_paraName_1_type(instance):
    assert isinstance(instance.paraName_1, str)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_paraName_1_setter(instance):
    original = instance.paraName_1
    instance.paraName_1 = original
    assert instance.paraName_1 == original

@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_visibleType_1_type(instance):
    assert isinstance(instance.visibleType_1, int)


@given(instance=MachineLibrary::UnitGeneralParameters_strategy)
def test_machinelibrary::unitgeneralparameters_visibleType_1_setter(instance):
    original = instance.visibleType_1
    instance.visibleType_1 = original
    assert instance.visibleType_1 == original

@given(instance=MachineLibrary::UnitSpecialConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitspecialconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitSpecialConfiguration)

@given(instance=MachineLibrary::UnitGeneralSpecial_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneralspecial_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneralSpecial)

@given(instance=MachineLibrary::UnitGeneral_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitgeneral_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitGeneral)

@given(instance=MachineLibrary::Buttons_strategy)
@settings(max_examples=50)
def test_machinelibrary::buttons_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Buttons)

@given(instance=MachineLibrary::UnitPrograms_strategy)
@settings(max_examples=50)
def test_machinelibrary::unitprograms_instantiation(instance):
    assert isinstance(instance, MachineLibrary::UnitPrograms)

@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::rigakuxrf_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::RigakuXRF)

@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timeoutResponce_type(instance):
    assert isinstance(instance.timeoutResponce, int)


@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timeoutResponce_setter(instance):
    original = instance.timeoutResponce
    instance.timeoutResponce = original
    assert instance.timeoutResponce == original

@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timeout_type(instance):
    assert isinstance(instance.timeout, int)


@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_bDoNotshiftAtExit_type(instance):
    assert isinstance(instance.bDoNotshiftAtExit, int)


@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_bDoNotshiftAtExit_setter(instance):
    original = instance.bDoNotshiftAtExit
    instance.bDoNotshiftAtExit = original
    assert instance.bDoNotshiftAtExit == original

@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timerToSendStatus_type(instance):
    assert isinstance(instance.timerToSendStatus, int)


@given(instance=MachineLibrary::NodeGeneral::RigakuXRF_strategy)
def test_machinelibrary::nodegeneral::rigakuxrf_timerToSendStatus_setter(instance):
    original = instance.timerToSendStatus
    instance.timerToSendStatus = original
    assert instance.timerToSendStatus == original

@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::accupycmeter_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::AccuPycMeter)

@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_runTimout_type(instance):
    assert isinstance(instance.runTimout, int)


@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_runTimout_setter(instance):
    original = instance.runTimout
    instance.runTimout = original
    assert instance.runTimout == original

@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_expectSampleWeight_type(instance):
    assert isinstance(instance.expectSampleWeight, int)


@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_expectSampleWeight_setter(instance):
    original = instance.expectSampleWeight
    instance.expectSampleWeight = original
    assert instance.expectSampleWeight == original

@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_polling_type(instance):
    assert isinstance(instance.polling, int)


@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_polling_setter(instance):
    original = instance.polling
    instance.polling = original
    assert instance.polling == original

@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_sendSampleWeight_type(instance):
    assert isinstance(instance.sendSampleWeight, int)


@given(instance=MachineLibrary::NodeGeneral::AccuPycMeter_strategy)
def test_machinelibrary::nodegeneral::accupycmeter_sendSampleWeight_setter(instance):
    original = instance.sendSampleWeight
    instance.sendSampleWeight = original
    assert instance.sendSampleWeight == original

@given(instance=MachineLibrary::NodeGeneral::WinCC2WinCC_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::wincc2wincc_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::WinCC2WinCC)

@given(instance=MachineLibrary::NodeGeneral::WinCC2WinCC_strategy)
def test_machinelibrary::nodegeneral::wincc2wincc_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=MachineLibrary::NodeGeneral::WinCC2WinCC_strategy)
def test_machinelibrary::nodegeneral::wincc2wincc_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=MachineLibrary::NodeGeneral::RemotePM_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::remotepm_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::RemotePM)

@given(instance=MachineLibrary::NodeGeneral::RemotePM_strategy)
def test_machinelibrary::nodegeneral::remotepm_timeServer_type(instance):
    assert isinstance(instance.timeServer, int)


@given(instance=MachineLibrary::NodeGeneral::RemotePM_strategy)
def test_machinelibrary::nodegeneral::remotepm_timeServer_setter(instance):
    original = instance.timeServer
    instance.timeServer = original
    assert instance.timeServer == original

@given(instance=MachineLibrary::NodeGeneral::RemotePM_strategy)
def test_machinelibrary::nodegeneral::remotepm_system_type(instance):
    assert isinstance(instance.system, str)


@given(instance=MachineLibrary::NodeGeneral::RemotePM_strategy)
def test_machinelibrary::nodegeneral::remotepm_system_setter(instance):
    original = instance.system
    instance.system = original
    assert instance.system == original

@given(instance=MachineLibrary::NodeGeneral::PM2PM_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::pm2pm_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::PM2PM)

@given(instance=MachineLibrary::NodeGeneral::PM2PM_strategy)
def test_machinelibrary::nodegeneral::pm2pm_type_type(instance):
    assert isinstance(instance.type, int)


@given(instance=MachineLibrary::NodeGeneral::PM2PM_strategy)
def test_machinelibrary::nodegeneral::pm2pm_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MachineLibrary::NodeGeneral::PM2PM_strategy)
def test_machinelibrary::nodegeneral::pm2pm_timeServer_type(instance):
    assert isinstance(instance.timeServer, int)


@given(instance=MachineLibrary::NodeGeneral::PM2PM_strategy)
def test_machinelibrary::nodegeneral::pm2pm_timeServer_setter(instance):
    original = instance.timeServer
    instance.timeServer = original
    assert instance.timeServer == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral::terminal_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral::Terminal)

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_customTimer1_type(instance):
    assert isinstance(instance.customTimer1, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_customTimer1_setter(instance):
    original = instance.customTimer1
    instance.customTimer1 = original
    assert instance.customTimer1 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_terminalType_type(instance):
    assert isinstance(instance.terminalType, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_terminalType_setter(instance):
    original = instance.terminalType
    instance.terminalType = original
    assert instance.terminalType == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationReady_type(instance):
    assert isinstance(instance.stationReady, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationReady_setter(instance):
    original = instance.stationReady
    instance.stationReady = original
    assert instance.stationReady == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_steelCarrier_type(instance):
    assert isinstance(instance.steelCarrier, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_steelCarrier_setter(instance):
    original = instance.steelCarrier
    instance.steelCarrier = original
    assert instance.steelCarrier == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_1_type(instance):
    assert isinstance(instance.name_1, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_1_setter(instance):
    original = instance.name_1
    instance.name_1 = original
    assert instance.name_1 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_3_type(instance):
    assert isinstance(instance.name_3, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_3_setter(instance):
    original = instance.name_3
    instance.name_3 = original
    assert instance.name_3 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_2_type(instance):
    assert isinstance(instance.name_2, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_2_setter(instance):
    original = instance.name_2
    instance.name_2 = original
    assert instance.name_2 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_6_type(instance):
    assert isinstance(instance.name_6, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_6_setter(instance):
    original = instance.name_6
    instance.name_6 = original
    assert instance.name_6 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_signalCarrierPresent_type(instance):
    assert isinstance(instance.signalCarrierPresent, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_signalCarrierPresent_setter(instance):
    original = instance.signalCarrierPresent
    instance.signalCarrierPresent = original
    assert instance.signalCarrierPresent == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_keyBoardSignalCarrierPresent_type(instance):
    assert isinstance(instance.keyBoardSignalCarrierPresent, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_keyBoardSignalCarrierPresent_setter(instance):
    original = instance.keyBoardSignalCarrierPresent
    instance.keyBoardSignalCarrierPresent = original
    assert instance.keyBoardSignalCarrierPresent == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxScreens_type(instance):
    assert isinstance(instance.maxScreens, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxScreens_setter(instance):
    original = instance.maxScreens
    instance.maxScreens = original
    assert instance.maxScreens == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationAuto_type(instance):
    assert isinstance(instance.stationAuto, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationAuto_setter(instance):
    original = instance.stationAuto
    instance.stationAuto = original
    assert instance.stationAuto == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxXValue_type(instance):
    assert isinstance(instance.maxXValue, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxXValue_setter(instance):
    original = instance.maxXValue
    instance.maxXValue = original
    assert instance.maxXValue == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_5_type(instance):
    assert isinstance(instance.name_5, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_5_setter(instance):
    original = instance.name_5
    instance.name_5 = original
    assert instance.name_5 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_displayTime_type(instance):
    assert isinstance(instance.displayTime, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_displayTime_setter(instance):
    original = instance.displayTime
    instance.displayTime = original
    assert instance.displayTime == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_4_type(instance):
    assert isinstance(instance.name_4, str)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_name_4_setter(instance):
    original = instance.name_4
    instance.name_4 = original
    assert instance.name_4 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_customTimer2_type(instance):
    assert isinstance(instance.customTimer2, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_customTimer2_setter(instance):
    original = instance.customTimer2
    instance.customTimer2 = original
    assert instance.customTimer2 == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationType_type(instance):
    assert isinstance(instance.stationType, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_stationType_setter(instance):
    original = instance.stationType
    instance.stationType = original
    assert instance.stationType == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxYValue_type(instance):
    assert isinstance(instance.maxYValue, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_maxYValue_setter(instance):
    original = instance.maxYValue
    instance.maxYValue = original
    assert instance.maxYValue == original

@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_lenOfPlanID_type(instance):
    assert isinstance(instance.lenOfPlanID, int)


@given(instance=MachineLibrary::NodeGeneral::Terminal_strategy)
def test_machinelibrary::nodegeneral::terminal_lenOfPlanID_setter(instance):
    original = instance.lenOfPlanID
    instance.lenOfPlanID = original
    assert instance.lenOfPlanID == original

@given(instance=MachineLibrary::NodeGeneralSpecial_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneralspecial_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneralSpecial)

@given(instance=MachineLibrary::NodeGeneral_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodegeneral_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeGeneral)

@given(instance=MachineLibrary::NodeGeneral_strategy)
def test_machinelibrary::nodegeneral_canCreateErrorTag_type(instance):
    assert isinstance(instance.canCreateErrorTag, str)


@given(instance=MachineLibrary::NodeGeneral_strategy)
def test_machinelibrary::nodegeneral_canCreateErrorTag_setter(instance):
    original = instance.canCreateErrorTag
    instance.canCreateErrorTag = original
    assert instance.canCreateErrorTag == original

@given(instance=MachineLibrary::NodeGeneral_strategy)
def test_machinelibrary::nodegeneral_canCreateStateTag_type(instance):
    assert isinstance(instance.canCreateStateTag, str)


@given(instance=MachineLibrary::NodeGeneral_strategy)
def test_machinelibrary::nodegeneral_canCreateStateTag_setter(instance):
    original = instance.canCreateStateTag
    instance.canCreateStateTag = original
    assert instance.canCreateStateTag == original

@given(instance=MachineLibrary::NodeSpecialConfiguration_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodespecialconfiguration_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeSpecialConfiguration)

@given(instance=MachineLibrary::CommunicationData_strategy)
@settings(max_examples=50)
def test_machinelibrary::communicationdata_instantiation(instance):
    assert isinstance(instance, MachineLibrary::CommunicationData)

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comErrorDataLength_type(instance):
    assert isinstance(instance.comErrorDataLength, int)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comErrorDataLength_setter(instance):
    original = instance.comErrorDataLength
    instance.comErrorDataLength = original
    assert instance.comErrorDataLength == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comProgressIndDataAddress_type(instance):
    assert isinstance(instance.comProgressIndDataAddress, str)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comProgressIndDataAddress_setter(instance):
    original = instance.comProgressIndDataAddress
    instance.comProgressIndDataAddress = original
    assert instance.comProgressIndDataAddress == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSendDataLength_type(instance):
    assert isinstance(instance.comSendDataLength, int)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSendDataLength_setter(instance):
    original = instance.comSendDataLength
    instance.comSendDataLength = original
    assert instance.comSendDataLength == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comErrorDataAddress_type(instance):
    assert isinstance(instance.comErrorDataAddress, str)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comErrorDataAddress_setter(instance):
    original = instance.comErrorDataAddress
    instance.comErrorDataAddress = original
    assert instance.comErrorDataAddress == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comProgressIndDataLength_type(instance):
    assert isinstance(instance.comProgressIndDataLength, int)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comProgressIndDataLength_setter(instance):
    original = instance.comProgressIndDataLength
    instance.comProgressIndDataLength = original
    assert instance.comProgressIndDataLength == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSIDDataLength_type(instance):
    assert isinstance(instance.comSIDDataLength, int)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSIDDataLength_setter(instance):
    original = instance.comSIDDataLength
    instance.comSIDDataLength = original
    assert instance.comSIDDataLength == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSendDataAddress_type(instance):
    assert isinstance(instance.comSendDataAddress, str)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSendDataAddress_setter(instance):
    original = instance.comSendDataAddress
    instance.comSendDataAddress = original
    assert instance.comSendDataAddress == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comRequestDataLength_type(instance):
    assert isinstance(instance.comRequestDataLength, int)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comRequestDataLength_setter(instance):
    original = instance.comRequestDataLength
    instance.comRequestDataLength = original
    assert instance.comRequestDataLength == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSIDDataAddress_type(instance):
    assert isinstance(instance.comSIDDataAddress, str)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comSIDDataAddress_setter(instance):
    original = instance.comSIDDataAddress
    instance.comSIDDataAddress = original
    assert instance.comSIDDataAddress == original

@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comRequestDataAddress_type(instance):
    assert isinstance(instance.comRequestDataAddress, str)


@given(instance=MachineLibrary::CommunicationData_strategy)
def test_machinelibrary::communicationdata_comRequestDataAddress_setter(instance):
    original = instance.comRequestDataAddress
    instance.comRequestDataAddress = original
    assert instance.comRequestDataAddress == original

@given(instance=MachineLibrary::Parameters_strategy)
@settings(max_examples=50)
def test_machinelibrary::parameters_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Parameters)

@given(instance=MachineLibrary::Parameters_strategy)
def test_machinelibrary::parameters_parameterConfigNo_type(instance):
    assert isinstance(instance.parameterConfigNo, str)


@given(instance=MachineLibrary::Parameters_strategy)
def test_machinelibrary::parameters_parameterConfigNo_setter(instance):
    original = instance.parameterConfigNo
    instance.parameterConfigNo = original
    assert instance.parameterConfigNo == original

@given(instance=MachineLibrary::Parameters_strategy)
def test_machinelibrary::parameters_parameterConfigYes_type(instance):
    assert isinstance(instance.parameterConfigYes, str)


@given(instance=MachineLibrary::Parameters_strategy)
def test_machinelibrary::parameters_parameterConfigYes_setter(instance):
    original = instance.parameterConfigYes
    instance.parameterConfigYes = original
    assert instance.parameterConfigYes == original

@given(instance=MachineLibrary::NodePrograms_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodeprograms_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodePrograms)

@given(instance=MachineLibrary::Commands_strategy)
@settings(max_examples=50)
def test_machinelibrary::commands_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Commands)

@given(instance=MachineLibrary::Units_strategy)
@settings(max_examples=50)
def test_machinelibrary::units_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Units)

@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_internalUniNo_type(instance):
    assert isinstance(instance.internalUniNo, int)


@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_internalUniNo_setter(instance):
    original = instance.internalUniNo
    instance.internalUniNo = original
    assert instance.internalUniNo == original

@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_unitNo_type(instance):
    assert isinstance(instance.unitNo, int)


@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_unitNo_setter(instance):
    original = instance.unitNo
    instance.unitNo = original
    assert instance.unitNo == original

@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_unitName_type(instance):
    assert isinstance(instance.unitName, str)


@given(instance=MachineLibrary::Units_strategy)
def test_machinelibrary::units_unitName_setter(instance):
    original = instance.unitName
    instance.unitName = original
    assert instance.unitName == original

@given(instance=MachineLibrary::DPbase::Node_strategy)
@settings(max_examples=50)
def test_machinelibrary::dpbase::node_instantiation(instance):
    assert isinstance(instance, MachineLibrary::DPbase::Node)

@given(instance=MachineLibrary::DPbase::Node_strategy)
def test_machinelibrary::dpbase::node_isXPS_type(instance):
    assert isinstance(instance.isXPS, int)


@given(instance=MachineLibrary::DPbase::Node_strategy)
def test_machinelibrary::dpbase::node_isXPS_setter(instance):
    original = instance.isXPS
    instance.isXPS = original
    assert instance.isXPS == original

@given(instance=MachineLibrary::DPbase::Node_strategy)
def test_machinelibrary::dpbase::node_nodeNo_type(instance):
    assert isinstance(instance.nodeNo, int)


@given(instance=MachineLibrary::DPbase::Node_strategy)
def test_machinelibrary::dpbase::node_nodeNo_setter(instance):
    original = instance.nodeNo
    instance.nodeNo = original
    assert instance.nodeNo == original

@given(instance=MachineLibrary::Compac::Link_strategy)
@settings(max_examples=50)
def test_machinelibrary::compac::link_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Compac::Link)

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_useNotENQ_type(instance):
    assert isinstance(instance.useNotENQ, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_useNotENQ_setter(instance):
    original = instance.useNotENQ
    instance.useNotENQ = original
    assert instance.useNotENQ == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_splitLongMessage_type(instance):
    assert isinstance(instance.splitLongMessage, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_splitLongMessage_setter(instance):
    original = instance.splitLongMessage
    instance.splitLongMessage = original
    assert instance.splitLongMessage == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_maxDataLength_type(instance):
    assert isinstance(instance.maxDataLength, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_maxDataLength_setter(instance):
    original = instance.maxDataLength
    instance.maxDataLength = original
    assert instance.maxDataLength == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_retry_type(instance):
    assert isinstance(instance.retry, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_retry_setter(instance):
    original = instance.retry
    instance.retry = original
    assert instance.retry == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_bcc_type(instance):
    assert isinstance(instance.bcc, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_bcc_setter(instance):
    original = instance.bcc
    instance.bcc = original
    assert instance.bcc == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_checksum_type(instance):
    assert isinstance(instance.checksum, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_checksum_setter(instance):
    original = instance.checksum
    instance.checksum = original
    assert instance.checksum == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_useNotACK_NAK_type(instance):
    assert isinstance(instance.useNotACK_NAK, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_useNotACK_NAK_setter(instance):
    original = instance.useNotACK_NAK
    instance.useNotACK_NAK = original
    assert instance.useNotACK_NAK == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_commConfig_type(instance):
    assert isinstance(instance.commConfig, str)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_commConfig_setter(instance):
    original = instance.commConfig
    instance.commConfig = original
    assert instance.commConfig == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_checksumCode_type(instance):
    assert isinstance(instance.checksumCode, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_checksumCode_setter(instance):
    original = instance.checksumCode
    instance.checksumCode = original
    assert instance.checksumCode == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_byteCount_type(instance):
    assert isinstance(instance.byteCount, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_byteCount_setter(instance):
    original = instance.byteCount
    instance.byteCount = original
    assert instance.byteCount == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_bytecountcode_type(instance):
    assert isinstance(instance.bytecountcode, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_bytecountcode_setter(instance):
    original = instance.bytecountcode
    instance.bytecountcode = original
    assert instance.bytecountcode == original

@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_timeout_type(instance):
    assert isinstance(instance.timeout, int)


@given(instance=MachineLibrary::Compac::Link_strategy)
def test_machinelibrary::compac::link_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
@settings(max_examples=50)
def test_machinelibrary::filetransfer::link_instantiation(instance):
    assert isinstance(instance, MachineLibrary::FileTransfer::Link)

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_timeoutwrite_type(instance):
    assert isinstance(instance.timeoutwrite, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_timeoutwrite_setter(instance):
    original = instance.timeoutwrite
    instance.timeoutwrite = original
    assert instance.timeoutwrite == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_delimiter_type(instance):
    assert isinstance(instance.delimiter, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_sendBuffer_type(instance):
    assert isinstance(instance.sendBuffer, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_delimter_type(instance):
    assert isinstance(instance.delimter, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_delimter_setter(instance):
    original = instance.delimter
    instance.delimter = original
    assert instance.delimter == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagDelAfterReading_type(instance):
    assert isinstance(instance.flagDelAfterReading, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagDelAfterReading_setter(instance):
    original = instance.flagDelAfterReading
    instance.flagDelAfterReading = original
    assert instance.flagDelAfterReading == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_writeAfterReading_type(instance):
    assert isinstance(instance.writeAfterReading, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_writeAfterReading_setter(instance):
    original = instance.writeAfterReading
    instance.writeAfterReading = original
    assert instance.writeAfterReading == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_pollTime_type(instance):
    assert isinstance(instance.pollTime, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_pollTime_setter(instance):
    original = instance.pollTime
    instance.pollTime = original
    assert instance.pollTime == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_readPath_type(instance):
    assert isinstance(instance.readPath, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_readPath_setter(instance):
    original = instance.readPath
    instance.readPath = original
    assert instance.readPath == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_maxDataLength_type(instance):
    assert isinstance(instance.maxDataLength, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_maxDataLength_setter(instance):
    original = instance.maxDataLength
    instance.maxDataLength = original
    assert instance.maxDataLength == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_receiveBuffer_type(instance):
    assert isinstance(instance.receiveBuffer, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagWriteAfterReading_type(instance):
    assert isinstance(instance.flagWriteAfterReading, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagWriteAfterReading_setter(instance):
    original = instance.flagWriteAfterReading
    instance.flagWriteAfterReading = original
    assert instance.flagWriteAfterReading == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagToWriteWaitForDeleted_type(instance):
    assert isinstance(instance.flagToWriteWaitForDeleted, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagToWriteWaitForDeleted_setter(instance):
    original = instance.flagToWriteWaitForDeleted
    instance.flagToWriteWaitForDeleted = original
    assert instance.flagToWriteWaitForDeleted == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_toWriteWaitFor_type(instance):
    assert isinstance(instance.toWriteWaitFor, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_toWriteWaitFor_setter(instance):
    original = instance.toWriteWaitFor
    instance.toWriteWaitFor = original
    assert instance.toWriteWaitFor == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_writePath_type(instance):
    assert isinstance(instance.writePath, str)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_writePath_setter(instance):
    original = instance.writePath
    instance.writePath = original
    assert instance.writePath == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_translation_type(instance):
    assert isinstance(instance.translation, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_translation_setter(instance):
    original = instance.translation
    instance.translation = original
    assert instance.translation == original

@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagToWriteWaitFor_type(instance):
    assert isinstance(instance.flagToWriteWaitFor, int)


@given(instance=MachineLibrary::FileTransfer::Link_strategy)
def test_machinelibrary::filetransfer::link_flagToWriteWaitFor_setter(instance):
    original = instance.flagToWriteWaitFor
    instance.flagToWriteWaitFor = original
    assert instance.flagToWriteWaitFor == original

@given(instance=MachineLibrary::Serial::Link_strategy)
@settings(max_examples=50)
def test_machinelibrary::serial::link_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Serial::Link)

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_startChar_type(instance):
    assert isinstance(instance.startChar, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_startChar_setter(instance):
    original = instance.startChar
    instance.startChar = original
    assert instance.startChar == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_logging_type(instance):
    assert isinstance(instance.logging, int)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_logging_setter(instance):
    original = instance.logging
    instance.logging = original
    assert instance.logging == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_port_type(instance):
    assert isinstance(instance.port, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_maxCharDelay_type(instance):
    assert isinstance(instance.maxCharDelay, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_maxCharDelay_setter(instance):
    original = instance.maxCharDelay
    instance.maxCharDelay = original
    assert instance.maxCharDelay == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_bufferLenght_type(instance):
    assert isinstance(instance.bufferLenght, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_bufferLenght_setter(instance):
    original = instance.bufferLenght
    instance.bufferLenght = original
    assert instance.bufferLenght == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_commConfig_type(instance):
    assert isinstance(instance.commConfig, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_commConfig_setter(instance):
    original = instance.commConfig
    instance.commConfig = original
    assert instance.commConfig == original

@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_endChar_type(instance):
    assert isinstance(instance.endChar, str)


@given(instance=MachineLibrary::Serial::Link_strategy)
def test_machinelibrary::serial::link_endChar_setter(instance):
    original = instance.endChar
    instance.endChar = original
    assert instance.endChar == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
@settings(max_examples=50)
def test_machinelibrary::tcpip::link_instantiation(instance):
    assert isinstance(instance, MachineLibrary::TCPIP::Link)

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_port_type(instance):
    assert isinstance(instance.port, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_3_type(instance):
    assert isinstance(instance.address_3, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_3_setter(instance):
    original = instance.address_3
    instance.address_3 = original
    assert instance.address_3 == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_termChar_type(instance):
    assert isinstance(instance.termChar, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_termChar_setter(instance):
    original = instance.termChar
    instance.termChar = original
    assert instance.termChar == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_msgDelay_type(instance):
    assert isinstance(instance.msgDelay, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_msgDelay_setter(instance):
    original = instance.msgDelay
    instance.msgDelay = original
    assert instance.msgDelay == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_1_type(instance):
    assert isinstance(instance.address_1, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_1_setter(instance):
    original = instance.address_1
    instance.address_1 = original
    assert instance.address_1 == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_protocol_type(instance):
    assert isinstance(instance.protocol, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_6_type(instance):
    assert isinstance(instance.address_6, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_6_setter(instance):
    original = instance.address_6
    instance.address_6 = original
    assert instance.address_6 == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_4_type(instance):
    assert isinstance(instance.address_4, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_4_setter(instance):
    original = instance.address_4
    instance.address_4 = original
    assert instance.address_4 == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_5_type(instance):
    assert isinstance(instance.address_5, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_5_setter(instance):
    original = instance.address_5
    instance.address_5 = original
    assert instance.address_5 == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_maxDataSize_type(instance):
    assert isinstance(instance.maxDataSize, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_maxDataSize_setter(instance):
    original = instance.maxDataSize
    instance.maxDataSize = original
    assert instance.maxDataSize == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_receiveBuffer_type(instance):
    assert isinstance(instance.receiveBuffer, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_sendBuffer_type(instance):
    assert isinstance(instance.sendBuffer, int)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original

@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_2_type(instance):
    assert isinstance(instance.address_2, str)


@given(instance=MachineLibrary::TCPIP::Link_strategy)
def test_machinelibrary::tcpip::link_address_2_setter(instance):
    original = instance.address_2
    instance.address_2 = original
    assert instance.address_2 == original

@given(instance=MachineLibrary::WinCCLnk_strategy)
@settings(max_examples=50)
def test_machinelibrary::wincclnk_instantiation(instance):
    assert isinstance(instance, MachineLibrary::WinCCLnk)

@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_updateCycle_type(instance):
    assert isinstance(instance.updateCycle, int)


@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_updateCycle_setter(instance):
    original = instance.updateCycle
    instance.updateCycle = original
    assert instance.updateCycle == original

@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_updateCycle_Help_type(instance):
    assert isinstance(instance.updateCycle_Help, str)


@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_updateCycle_Help_setter(instance):
    original = instance.updateCycle_Help
    instance.updateCycle_Help = original
    assert instance.updateCycle_Help == original

@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_connectionName_type(instance):
    assert isinstance(instance.connectionName, str)


@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_connectionName_setter(instance):
    original = instance.connectionName
    instance.connectionName = original
    assert instance.connectionName == original

@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_canModifyTag_type(instance):
    assert isinstance(instance.canModifyTag, int)


@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_canModifyTag_setter(instance):
    original = instance.canModifyTag
    instance.canModifyTag = original
    assert instance.canModifyTag == original

@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_canCreateTags_type(instance):
    assert isinstance(instance.canCreateTags, int)


@given(instance=MachineLibrary::WinCCLnk_strategy)
def test_machinelibrary::wincclnk_canCreateTags_setter(instance):
    original = instance.canCreateTags
    instance.canCreateTags = original
    assert instance.canCreateTags == original

@given(instance=MachineLibrary::LinkConfig_strategy)
@settings(max_examples=50)
def test_machinelibrary::linkconfig_instantiation(instance):
    assert isinstance(instance, MachineLibrary::LinkConfig)

@given(instance=MachineLibrary::NodeConfig_strategy)
@settings(max_examples=50)
def test_machinelibrary::nodeconfig_instantiation(instance):
    assert isinstance(instance, MachineLibrary::NodeConfig)

@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_nodeNo_type(instance):
    assert isinstance(instance.nodeNo, int)


@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_nodeNo_setter(instance):
    original = instance.nodeNo
    instance.nodeNo = original
    assert instance.nodeNo == original

@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_simFileName_type(instance):
    assert isinstance(instance.simFileName, str)


@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_simFileName_setter(instance):
    original = instance.simFileName
    instance.simFileName = original
    assert instance.simFileName == original

@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_nodeName_type(instance):
    assert isinstance(instance.nodeName, str)


@given(instance=MachineLibrary::NodeConfig_strategy)
def test_machinelibrary::nodeconfig_nodeName_setter(instance):
    original = instance.nodeName
    instance.nodeName = original
    assert instance.nodeName == original

@given(instance=MachineLibrary::Link2_strategy)
@settings(max_examples=50)
def test_machinelibrary::link2_instantiation(instance):
    assert isinstance(instance, MachineLibrary::Link2)

@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2Type_type(instance):
    assert isinstance(instance.link2Type, str)


@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2Type_setter(instance):
    original = instance.link2Type
    instance.link2Type = original
    assert instance.link2Type == original

@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2ParamFile_type(instance):
    assert isinstance(instance.link2ParamFile, str)


@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2ParamFile_setter(instance):
    original = instance.link2ParamFile
    instance.link2ParamFile = original
    assert instance.link2ParamFile == original

@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2ParamSection_type(instance):
    assert isinstance(instance.link2ParamSection, str)


@given(instance=MachineLibrary::Link2_strategy)
def test_machinelibrary::link2_link2ParamSection_setter(instance):
    original = instance.link2ParamSection
    instance.link2ParamSection = original
    assert instance.link2ParamSection == original

@given(instance=MachineLibrary::DPbase::Link_strategy)
@settings(max_examples=50)
def test_machinelibrary::dpbase::link_instantiation(instance):
    assert isinstance(instance, MachineLibrary::DPbase::Link)

@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_speed_type(instance):
    assert isinstance(instance.speed, int)


@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_speed_setter(instance):
    original = instance.speed
    instance.speed = original
    assert instance.speed == original

@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_maxNodes_type(instance):
    assert isinstance(instance.maxNodes, int)


@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_maxNodes_setter(instance):
    original = instance.maxNodes
    instance.maxNodes = original
    assert instance.maxNodes == original

@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_cp_name_type(instance):
    assert isinstance(instance.cp_name, str)


@given(instance=MachineLibrary::DPbase::Link_strategy)
def test_machinelibrary::dpbase::link_cp_name_setter(instance):
    original = instance.cp_name
    instance.cp_name = original
    assert instance.cp_name == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
@settings(max_examples=50)
def test_machinelibrary::ibmwebspheremq_instantiation(instance):
    assert isinstance(instance, MachineLibrary::IBMWebsphereMQ)

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readDynamicQueName_type(instance):
    assert isinstance(instance.readDynamicQueName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readDynamicQueName_setter(instance):
    original = instance.readDynamicQueName
    instance.readDynamicQueName = original
    assert instance.readDynamicQueName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_maxDataSize_type(instance):
    assert isinstance(instance.maxDataSize, int)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_maxDataSize_setter(instance):
    original = instance.maxDataSize
    instance.maxDataSize = original
    assert instance.maxDataSize == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readQueName_type(instance):
    assert isinstance(instance.readQueName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readQueName_setter(instance):
    original = instance.readQueName
    instance.readQueName = original
    assert instance.readQueName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_qName_type(instance):
    assert isinstance(instance.qName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_qName_setter(instance):
    original = instance.qName
    instance.qName = original
    assert instance.qName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendBuffer_type(instance):
    assert isinstance(instance.sendBuffer, int)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendBuffer_setter(instance):
    original = instance.sendBuffer
    instance.sendBuffer = original
    assert instance.sendBuffer == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendQueName_type(instance):
    assert isinstance(instance.sendQueName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendQueName_setter(instance):
    original = instance.sendQueName
    instance.sendQueName = original
    assert instance.sendQueName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendDynamicQueName_type(instance):
    assert isinstance(instance.sendDynamicQueName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendDynamicQueName_setter(instance):
    original = instance.sendDynamicQueName
    instance.sendDynamicQueName = original
    assert instance.sendDynamicQueName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_receiveBuffer_type(instance):
    assert isinstance(instance.receiveBuffer, int)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_receiveBuffer_setter(instance):
    original = instance.receiveBuffer
    instance.receiveBuffer = original
    assert instance.receiveBuffer == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readQueMgrName_type(instance):
    assert isinstance(instance.readQueMgrName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_readQueMgrName_setter(instance):
    original = instance.readQueMgrName
    instance.readQueMgrName = original
    assert instance.readQueMgrName == original

@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendQueMgrName_type(instance):
    assert isinstance(instance.sendQueMgrName, str)


@given(instance=MachineLibrary::IBMWebsphereMQ_strategy)
def test_machinelibrary::ibmwebspheremq_sendQueMgrName_setter(instance):
    original = instance.sendQueMgrName
    instance.sendQueMgrName = original
    assert instance.sendQueMgrName == original

@given(instance=MachineLibrary::LabMachine_strategy)
@settings(max_examples=50)
def test_machinelibrary::labmachine_instantiation(instance):
    assert isinstance(instance, MachineLibrary::LabMachine)

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkParamFile_type(instance):
    assert isinstance(instance.linkParamFile, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkParamFile_setter(instance):
    original = instance.linkParamFile
    instance.linkParamFile = original
    assert instance.linkParamFile == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkType_type(instance):
    assert isinstance(instance.linkType, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkType_setter(instance):
    original = instance.linkType
    instance.linkType = original
    assert instance.linkType == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_createWinCCTags_type(instance):
    assert isinstance(instance.createWinCCTags, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_createWinCCTags_setter(instance):
    original = instance.createWinCCTags
    instance.createWinCCTags = original
    assert instance.createWinCCTags == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkParamSection_type(instance):
    assert isinstance(instance.linkParamSection, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_linkParamSection_setter(instance):
    original = instance.linkParamSection
    instance.linkParamSection = original
    assert instance.linkParamSection == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_machineName_type(instance):
    assert isinstance(instance.machineName, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_machineName_setter(instance):
    original = instance.machineName
    instance.machineName = original
    assert instance.machineName == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_versionRemark_type(instance):
    assert isinstance(instance.versionRemark, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_versionRemark_setter(instance):
    original = instance.versionRemark
    instance.versionRemark = original
    assert instance.versionRemark == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_machineVersionNo_type(instance):
    assert isinstance(instance.machineVersionNo, float)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_machineVersionNo_setter(instance):
    original = instance.machineVersionNo
    instance.machineVersionNo = original
    assert instance.machineVersionNo == original

@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_driver_type(instance):
    assert isinstance(instance.driver, str)


@given(instance=MachineLibrary::LabMachine_strategy)
def test_machinelibrary::labmachine_driver_setter(instance):
    original = instance.driver
    instance.driver = original
    assert instance.driver == original

@given(instance=MachineLibrary::LabMachines_strategy)
@settings(max_examples=50)
def test_machinelibrary::labmachines_instantiation(instance):
    assert isinstance(instance, MachineLibrary::LabMachines)

@given(instance=MachineLibrary::PMMachineLibrary_strategy)
@settings(max_examples=50)
def test_machinelibrary::pmmachinelibrary_instantiation(instance):
    assert isinstance(instance, MachineLibrary::PMMachineLibrary)

@given(instance=MachineLibrary::PMMachineLibrary_strategy)
def test_machinelibrary::pmmachinelibrary_libraryVersion_type(instance):
    assert isinstance(instance.libraryVersion, float)


@given(instance=MachineLibrary::PMMachineLibrary_strategy)
def test_machinelibrary::pmmachinelibrary_libraryVersion_setter(instance):
    original = instance.libraryVersion
    instance.libraryVersion = original
    assert instance.libraryVersion == original

@given(instance=MachineLibrary::PMMachineLibrary_strategy)
def test_machinelibrary::pmmachinelibrary_libraryVersionRemark_type(instance):
    assert isinstance(instance.libraryVersionRemark, str)


@given(instance=MachineLibrary::PMMachineLibrary_strategy)
def test_machinelibrary::pmmachinelibrary_libraryVersionRemark_setter(instance):
    original = instance.libraryVersionRemark
    instance.libraryVersionRemark = original
    assert instance.libraryVersionRemark == original
