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
MachineLibrary_LinkConfig = Class(name="MachineLibrary::LinkConfig")
MachineLibrary_PMMachineLibrary = Class(name="MachineLibrary::PMMachineLibrary")
MachineLibrary_LabMachines = Class(name="MachineLibrary::LabMachines")
MachineLibrary_LabMachine = Class(name="MachineLibrary::LabMachine")
MachineLibrary_Link2 = Class(name="MachineLibrary::Link2")
MachineLibrary_NodeConfig = Class(name="MachineLibrary::NodeConfig")
MachineLibrary_WinCCLnk = Class(name="MachineLibrary::WinCCLnk")
MachineLibrary_TCPIP_Link = Class(name="MachineLibrary::TCPIP::Link")
MachineLibrary_Serial_Link = Class(name="MachineLibrary::Serial::Link")
MachineLibrary_FileTransfer_Link = Class(name="MachineLibrary::FileTransfer::Link")
MachineLibrary_Compac_Link = Class(name="MachineLibrary::Compac::Link")
MachineLibrary_IBMWebsphereMQ = Class(name="MachineLibrary::IBMWebsphereMQ")
MachineLibrary_DPbase_Link = Class(name="MachineLibrary::DPbase::Link")
MachineLibrary_DPbase_Node = Class(name="MachineLibrary::DPbase::Node")
MachineLibrary_NodeGeneral_AccuPycMeter = Class(name="MachineLibrary::NodeGeneral::AccuPycMeter")
MachineLibrary_NodeGeneral_RigakuXRF = Class(name="MachineLibrary::NodeGeneral::RigakuXRF")
MachineLibrary_Units = Class(name="MachineLibrary::Units")
MachineLibrary_Commands = Class(name="MachineLibrary::Commands")
MachineLibrary_NodePrograms = Class(name="MachineLibrary::NodePrograms")
MachineLibrary_Parameters = Class(name="MachineLibrary::Parameters")
MachineLibrary_CommunicationData = Class(name="MachineLibrary::CommunicationData")
MachineLibrary_NodeSpecialConfiguration = Class(name="MachineLibrary::NodeSpecialConfiguration")
MachineLibrary_NodeGeneral = Class(name="MachineLibrary::NodeGeneral")
MachineLibrary_NodeGeneralSpecial = Class(name="MachineLibrary::NodeGeneralSpecial")
MachineLibrary_NodeGeneral_Terminal = Class(name="MachineLibrary::NodeGeneral::Terminal")
MachineLibrary_NodeGeneral_PM2PM = Class(name="MachineLibrary::NodeGeneral::PM2PM")
MachineLibrary_NodeGeneral_RemotePM = Class(name="MachineLibrary::NodeGeneral::RemotePM")
MachineLibrary_NodeGeneral_WinCC2WinCC = Class(name="MachineLibrary::NodeGeneral::WinCC2WinCC")
MachineLibrary_WinCCAddTag = Class(name="MachineLibrary::WinCCAddTag")
MachineLibrary_Positions = Class(name="MachineLibrary::Positions")
MachineLibrary_StausBits = Class(name="MachineLibrary::StausBits")
MachineLibrary_PLCtoPmMatrix = Class(name="MachineLibrary::PLCtoPmMatrix")
MachineLibrary_UnitPrograms = Class(name="MachineLibrary::UnitPrograms")
MachineLibrary_Buttons = Class(name="MachineLibrary::Buttons")
MachineLibrary_UnitGeneral = Class(name="MachineLibrary::UnitGeneral")
MachineLibrary_UnitGeneralSpecial = Class(name="MachineLibrary::UnitGeneralSpecial")
MachineLibrary_UnitSpecialConfiguration = Class(name="MachineLibrary::UnitSpecialConfiguration")
MachineLibrary_UnitGeneralParameters = Class(name="MachineLibrary::UnitGeneralParameters")
MachineLibrary_UnitGeneral_Terminal = Class(name="MachineLibrary::UnitGeneral::Terminal")
MachineLibrary_UnitGeneral_HostPC = Class(name="MachineLibrary::UnitGeneral::HostPC")
MachineLibrary_UnitGeneral_Remote = Class(name="MachineLibrary::UnitGeneral::Remote")
MachineLibrary_UnitGeneral_PM2PM = Class(name="MachineLibrary::UnitGeneral::PM2PM")
MachineLibrary_UnitGeneral_AccPyc = Class(name="MachineLibrary::UnitGeneral::AccPyc")
MachineLibrary_UnitGeneral_SuperQ = Class(name="MachineLibrary::UnitGeneral::SuperQ")
MachineLibrary_UnitGeneral_RigakuXRF = Class(name="MachineLibrary::UnitGeneral::RigakuXRF")
MachineLibrary_UnitGeneral_Scanner = Class(name="MachineLibrary::UnitGeneral::Scanner")
MachineLibrary_ErrorMessage_OBLFOES = Class(name="MachineLibrary::ErrorMessage::OBLFOES")
MachineLibrary_GeneralParameter_SuperQXRF = Class(name="MachineLibrary::GeneralParameter::SuperQXRF")
MachineLibrary_UnitConfig_Terminal = Class(name="MachineLibrary::UnitConfig::Terminal")
MachineLibrary_UnitConfig_OBLF_OES = Class(name="MachineLibrary::UnitConfig::OBLF::OES")
MachineLibrary_UnitConfig_SuperQ_XRF = Class(name="MachineLibrary::UnitConfig::SuperQ::XRF")
MachineLibrary_UnitConfig_ARL_XRF_OES = Class(name="MachineLibrary::UnitConfig::ARL::XRF::OES")
MachineLibrary_UnitConfig_Host = Class(name="MachineLibrary::UnitConfig::Host")
MachineLibrary_History_AccuPycMeter = Class(name="MachineLibrary::History::AccuPycMeter")
MachineLibrary_SepByComma_Scanner = Class(name="MachineLibrary::SepByComma::Scanner")
MachineLibrary_CheckAddSID_PM2PM = Class(name="MachineLibrary::CheckAddSID::PM2PM")
MachineLibrary_Translate_Terminal = Class(name="MachineLibrary::Translate::Terminal")
MachineLibrary_OutputRequest_OBLFOES = Class(name="MachineLibrary::OutputRequest::OBLFOES")
MachineLibrary_TestRequest_OBLFOES = Class(name="MachineLibrary::TestRequest::OBLFOES")
MachineLibrary_RecalRequest_OBLFOES = Class(name="MachineLibrary::RecalRequest::OBLFOES")
MachineLibrary_Moved_Host = Class(name="MachineLibrary::Moved::Host")
MachineLibrary_ControlSamples_SuperQXRF = Class(name="MachineLibrary::ControlSamples::SuperQXRF")
MachineLibrary_Communication_SuperQXRF = Class(name="MachineLibrary::Communication::SuperQXRF")
MachineLibrary_CheckSampleRunTime_SuperQXRF = Class(name="MachineLibrary::CheckSampleRunTime::SuperQXRF")
MachineLibrary_CheckSample_SuperQXRF = Class(name="MachineLibrary::CheckSample::SuperQXRF")
MachineLibrary_CheckFilling_ARL_XRF_OES = Class(name="MachineLibrary::CheckFilling::ARL::XRF::OES")
MachineLibrary_ExecuteFiling_ARL_XRF_OES = Class(name="MachineLibrary::ExecuteFiling::ARL::XRF::OES")
MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES = Class(name="MachineLibrary::CheckReqPrepUnit::ARL::XRF::OES")
MachineLibrary_ExePrepUnit_ARL_XRF_OES = Class(name="MachineLibrary::ExePrepUnit::ARL::XRF::OES")
MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES = Class(name="MachineLibrary::CheckAskPrepUnit::ARL::XRF::OES")
MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES = Class(name="MachineLibrary::ExeAskPrepUnit::ARL::XRF::OES")
MachineLibrary_DisableSCT_ARL_XRF_OES = Class(name="MachineLibrary::DisableSCT::ARL::XRF::OES")
MachineLibrary_Settings_ARL_XRF_OES = Class(name="MachineLibrary::Settings::ARL::XRF::OES")
MachineLibrary_GeneralSetting_ARL_XRF_OES = Class(name="MachineLibrary::GeneralSetting::ARL::XRF::OES")
MachineLibrary_PS_Process_Finished_ARL_XRF_OES = Class(name="MachineLibrary::PS::Process::Finished::ARL::XRF::OES")
MachineLibrary_File_Sample_ARL_XRF_OES = Class(name="MachineLibrary::File::Sample::ARL::XRF::OES")
MachineLibrary_Report_Host = Class(name="MachineLibrary::Report::Host")
MachineLibrary_WS_Update_Host = Class(name="MachineLibrary::WS::Update::Host")
MachineLibrary_InsertRemove_Host = Class(name="MachineLibrary::InsertRemove::Host")
MachineLibrary_OES_XRF_Condition = Class(name="MachineLibrary::OES::XRF::Condition")
MachineLibrary_CheckSampleRunTimeParams_SuperQXRF = Class(name="MachineLibrary::CheckSampleRunTimeParams::SuperQXRF")
MachineLibrary_CheckSampleConfig_SuperQXRF = Class(name="MachineLibrary::CheckSampleConfig::SuperQXRF")
MachineLibrary_HistoryConfig_AccuPyc = Class(name="MachineLibrary::HistoryConfig::AccuPyc")
MachineLibrary_Button = Class(name="MachineLibrary::Button")
MachineLibrary_InsertRemove_Entry_Host = Class(name="MachineLibrary::InsertRemove::Entry::Host")
MachineLibrary_InsertRemove_Types_Host = Class(name="MachineLibrary::InsertRemove::Types::Host")
MachineLibrary_InsertRemove_Keywords_Host = Class(name="MachineLibrary::InsertRemove::Keywords::Host")
MachineLibrary_SepByComma_Field_Scanner = Class(name="MachineLibrary::SepByComma::Field::Scanner")
MachineLibrary_SepByComma_ID_Scanner = Class(name="MachineLibrary::SepByComma::ID::Scanner")
MachineLibrary_CheckAddSID_Values_PM2PM = Class(name="MachineLibrary::CheckAddSID::Values::PM2PM")
MachineLibrary_Position = Class(name="MachineLibrary::Position")
MachineLibrary_StatusBit = Class(name="MachineLibrary::StatusBit")
MachineLibrary_Command = Class(name="MachineLibrary::Command")
MachineLibrary_NodeProgram = Class(name="MachineLibrary::NodeProgram")
MachineLibrary_UnitProgram = Class(name="MachineLibrary::UnitProgram")
MachineLibrary_UnitProgParameters = Class(name="MachineLibrary::UnitProgParameters")
MachineLibrary_Parameter = Class(name="MachineLibrary::Parameter")
MachineLibrary_ParamPrint = Class(name="MachineLibrary::ParamPrint")
MachineLibrary_Transfer = Class(name="MachineLibrary::Transfer")
MachineLibrary_PlainMove = Class(name="MachineLibrary::PlainMove")
MachineLibrary_RobotConfiguration = Class(name="MachineLibrary::RobotConfiguration")
MachineLibrary_TransferFileSection = Class(name="MachineLibrary::TransferFileSection")
MachineLibrary_PlainMoveEntrySend = Class(name="MachineLibrary::PlainMoveEntrySend")
MachineLibrary_RobotWinCCToRobot = Class(name="MachineLibrary::RobotWinCCToRobot")
MachineLibrary_RobotVarToBusyCodes = Class(name="MachineLibrary::RobotVarToBusyCodes")
MachineLibrary_RobotConfSendOrders = Class(name="MachineLibrary::RobotConfSendOrders")
MachineLibrary_RobotWinCCToRobots = Class(name="MachineLibrary::RobotWinCCToRobots")
MachineLibrary_RobotToWinccs = Class(name="MachineLibrary::RobotToWinccs")
MachineLibrary_RobotWarningONDelete = Class(name="MachineLibrary::RobotWarningONDelete")
MachineLibrary_RobotVarToErrorbits = Class(name="MachineLibrary::RobotVarToErrorbits")
MachineLibrary_RobotVarToBusycode = Class(name="MachineLibrary::RobotVarToBusycode")
MachineLibrary_RobotConfSendOrder = Class(name="MachineLibrary::RobotConfSendOrder")
MachineLibrary_RobotToWinCC = Class(name="MachineLibrary::RobotToWinCC")
MachineLibrary_RobotVarToErrorbit = Class(name="MachineLibrary::RobotVarToErrorbit")

# MachineLibrary_LinkConfig class attributes and methods

# MachineLibrary_PMMachineLibrary class attributes and methods
MachineLibrary_PMMachineLibrary_libraryVersion: Property = Property(name="libraryVersion", type=FloatType)
MachineLibrary_PMMachineLibrary_libraryVersionRemark: Property = Property(name="libraryVersionRemark", type=StringType)
MachineLibrary_PMMachineLibrary.attributes={MachineLibrary_PMMachineLibrary_libraryVersionRemark, MachineLibrary_PMMachineLibrary_libraryVersion}

# MachineLibrary_LabMachines class attributes and methods

# MachineLibrary_LabMachine class attributes and methods
MachineLibrary_LabMachine_machineName: Property = Property(name="machineName", type=StringType)
MachineLibrary_LabMachine_machineVersionNo: Property = Property(name="machineVersionNo", type=FloatType)
MachineLibrary_LabMachine_versionRemark: Property = Property(name="versionRemark", type=StringType)
MachineLibrary_LabMachine_driver: Property = Property(name="driver", type=StringType)
MachineLibrary_LabMachine_linkType: Property = Property(name="linkType", type=StringType)
MachineLibrary_LabMachine_linkParamFile: Property = Property(name="linkParamFile", type=StringType)
MachineLibrary_LabMachine_linkParamSection: Property = Property(name="linkParamSection", type=StringType)
MachineLibrary_LabMachine_createWinCCTags: Property = Property(name="createWinCCTags", type=StringType)
MachineLibrary_LabMachine.attributes={MachineLibrary_LabMachine_versionRemark, MachineLibrary_LabMachine_linkParamSection, MachineLibrary_LabMachine_createWinCCTags, MachineLibrary_LabMachine_driver, MachineLibrary_LabMachine_linkType, MachineLibrary_LabMachine_machineVersionNo, MachineLibrary_LabMachine_machineName, MachineLibrary_LabMachine_linkParamFile}

# MachineLibrary_Link2 class attributes and methods
MachineLibrary_Link2_link2Type: Property = Property(name="link2Type", type=StringType)
MachineLibrary_Link2_link2ParamFile: Property = Property(name="link2ParamFile", type=StringType)
MachineLibrary_Link2_link2ParamSection: Property = Property(name="link2ParamSection", type=StringType)
MachineLibrary_Link2.attributes={MachineLibrary_Link2_link2ParamFile, MachineLibrary_Link2_link2ParamSection, MachineLibrary_Link2_link2Type}

# MachineLibrary_NodeConfig class attributes and methods
MachineLibrary_NodeConfig_nodeName: Property = Property(name="nodeName", type=StringType)
MachineLibrary_NodeConfig_nodeNo: Property = Property(name="nodeNo", type=IntegerType)
MachineLibrary_NodeConfig_simFileName: Property = Property(name="simFileName", type=StringType)
MachineLibrary_NodeConfig.attributes={MachineLibrary_NodeConfig_simFileName, MachineLibrary_NodeConfig_nodeNo, MachineLibrary_NodeConfig_nodeName}

# MachineLibrary_WinCCLnk class attributes and methods
MachineLibrary_WinCCLnk_connectionName: Property = Property(name="connectionName", type=StringType)
MachineLibrary_WinCCLnk_canModifyTag: Property = Property(name="canModifyTag", type=IntegerType)
MachineLibrary_WinCCLnk_canCreateTags: Property = Property(name="canCreateTags", type=IntegerType)
MachineLibrary_WinCCLnk_updateCycle: Property = Property(name="updateCycle", type=IntegerType)
MachineLibrary_WinCCLnk_updateCycle_Help: Property = Property(name="updateCycle_Help", type=StringType)
MachineLibrary_WinCCLnk.attributes={MachineLibrary_WinCCLnk_connectionName, MachineLibrary_WinCCLnk_canCreateTags, MachineLibrary_WinCCLnk_updateCycle_Help, MachineLibrary_WinCCLnk_updateCycle, MachineLibrary_WinCCLnk_canModifyTag}

# MachineLibrary_TCPIP_Link class attributes and methods
MachineLibrary_TCPIP_Link_protocol: Property = Property(name="protocol", type=IntegerType)
MachineLibrary_TCPIP_Link_termChar: Property = Property(name="termChar", type=IntegerType)
MachineLibrary_TCPIP_Link_port: Property = Property(name="port", type=IntegerType)
MachineLibrary_TCPIP_Link_address_1: Property = Property(name="address_1", type=StringType)
MachineLibrary_TCPIP_Link_address_2: Property = Property(name="address_2", type=StringType)
MachineLibrary_TCPIP_Link_address_3: Property = Property(name="address_3", type=StringType)
MachineLibrary_TCPIP_Link_address_4: Property = Property(name="address_4", type=StringType)
MachineLibrary_TCPIP_Link_address_5: Property = Property(name="address_5", type=StringType)
MachineLibrary_TCPIP_Link_address_6: Property = Property(name="address_6", type=StringType)
MachineLibrary_TCPIP_Link_sendBuffer: Property = Property(name="sendBuffer", type=IntegerType)
MachineLibrary_TCPIP_Link_receiveBuffer: Property = Property(name="receiveBuffer", type=IntegerType)
MachineLibrary_TCPIP_Link_maxDataSize: Property = Property(name="maxDataSize", type=IntegerType)
MachineLibrary_TCPIP_Link_msgDelay: Property = Property(name="msgDelay", type=IntegerType)
MachineLibrary_TCPIP_Link.attributes={MachineLibrary_TCPIP_Link_termChar, MachineLibrary_TCPIP_Link_sendBuffer, MachineLibrary_TCPIP_Link_address_1, MachineLibrary_TCPIP_Link_port, MachineLibrary_TCPIP_Link_address_4, MachineLibrary_TCPIP_Link_address_5, MachineLibrary_TCPIP_Link_maxDataSize, MachineLibrary_TCPIP_Link_msgDelay, MachineLibrary_TCPIP_Link_address_3, MachineLibrary_TCPIP_Link_address_6, MachineLibrary_TCPIP_Link_protocol, MachineLibrary_TCPIP_Link_address_2, MachineLibrary_TCPIP_Link_receiveBuffer}

# MachineLibrary_Serial_Link class attributes and methods
MachineLibrary_Serial_Link_port: Property = Property(name="port", type=StringType)
MachineLibrary_Serial_Link_commConfig: Property = Property(name="commConfig", type=StringType)
MachineLibrary_Serial_Link_params: Property = Property(name="params", type=StringType)
MachineLibrary_Serial_Link_endChar: Property = Property(name="endChar", type=StringType)
MachineLibrary_Serial_Link_maxCharDelay: Property = Property(name="maxCharDelay", type=StringType)
MachineLibrary_Serial_Link_bufferLenght: Property = Property(name="bufferLenght", type=StringType)
MachineLibrary_Serial_Link_startChar: Property = Property(name="startChar", type=StringType)
MachineLibrary_Serial_Link_logging: Property = Property(name="logging", type=IntegerType)
MachineLibrary_Serial_Link.attributes={MachineLibrary_Serial_Link_bufferLenght, MachineLibrary_Serial_Link_port, MachineLibrary_Serial_Link_maxCharDelay, MachineLibrary_Serial_Link_params, MachineLibrary_Serial_Link_commConfig, MachineLibrary_Serial_Link_logging, MachineLibrary_Serial_Link_startChar, MachineLibrary_Serial_Link_endChar}

# MachineLibrary_FileTransfer_Link class attributes and methods
MachineLibrary_FileTransfer_Link_sendBuffer: Property = Property(name="sendBuffer", type=IntegerType)
MachineLibrary_FileTransfer_Link_receiveBuffer: Property = Property(name="receiveBuffer", type=IntegerType)
MachineLibrary_FileTransfer_Link_maxDataLength: Property = Property(name="maxDataLength", type=IntegerType)
MachineLibrary_FileTransfer_Link_timeoutwrite: Property = Property(name="timeoutwrite", type=StringType)
MachineLibrary_FileTransfer_Link_pollTime: Property = Property(name="pollTime", type=IntegerType)
MachineLibrary_FileTransfer_Link_writePath: Property = Property(name="writePath", type=StringType)
MachineLibrary_FileTransfer_Link_readPath: Property = Property(name="readPath", type=StringType)
MachineLibrary_FileTransfer_Link_flagDelAfterReading: Property = Property(name="flagDelAfterReading", type=IntegerType)
MachineLibrary_FileTransfer_Link_flagWriteAfterReading: Property = Property(name="flagWriteAfterReading", type=IntegerType)
MachineLibrary_FileTransfer_Link_flagToWriteWaitForDeleted: Property = Property(name="flagToWriteWaitForDeleted", type=IntegerType)
MachineLibrary_FileTransfer_Link_flagToWriteWaitFor: Property = Property(name="flagToWriteWaitFor", type=IntegerType)
MachineLibrary_FileTransfer_Link_delimter: Property = Property(name="delimter", type=StringType)
MachineLibrary_FileTransfer_Link_writeAfterReading: Property = Property(name="writeAfterReading", type=IntegerType)
MachineLibrary_FileTransfer_Link_toWriteWaitFor: Property = Property(name="toWriteWaitFor", type=StringType)
MachineLibrary_FileTransfer_Link_translation: Property = Property(name="translation", type=IntegerType)
MachineLibrary_FileTransfer_Link_delimiter: Property = Property(name="delimiter", type=StringType)
MachineLibrary_FileTransfer_Link.attributes={MachineLibrary_FileTransfer_Link_receiveBuffer, MachineLibrary_FileTransfer_Link_flagWriteAfterReading, MachineLibrary_FileTransfer_Link_flagDelAfterReading, MachineLibrary_FileTransfer_Link_toWriteWaitFor, MachineLibrary_FileTransfer_Link_sendBuffer, MachineLibrary_FileTransfer_Link_flagToWriteWaitFor, MachineLibrary_FileTransfer_Link_delimter, MachineLibrary_FileTransfer_Link_writePath, MachineLibrary_FileTransfer_Link_maxDataLength, MachineLibrary_FileTransfer_Link_pollTime, MachineLibrary_FileTransfer_Link_delimiter, MachineLibrary_FileTransfer_Link_translation, MachineLibrary_FileTransfer_Link_timeoutwrite, MachineLibrary_FileTransfer_Link_flagToWriteWaitForDeleted, MachineLibrary_FileTransfer_Link_writeAfterReading, MachineLibrary_FileTransfer_Link_readPath}

# MachineLibrary_Compac_Link class attributes and methods
MachineLibrary_Compac_Link_useNotACK_NAK: Property = Property(name="useNotACK_NAK", type=IntegerType)
MachineLibrary_Compac_Link_port: Property = Property(name="port", type=StringType)
MachineLibrary_Compac_Link_commConfig: Property = Property(name="commConfig", type=StringType)
MachineLibrary_Compac_Link_params: Property = Property(name="params", type=StringType)
MachineLibrary_Compac_Link_byteCount: Property = Property(name="byteCount", type=IntegerType)
MachineLibrary_Compac_Link_bytecountcode: Property = Property(name="bytecountcode", type=IntegerType)
MachineLibrary_Compac_Link_checksum: Property = Property(name="checksum", type=IntegerType)
MachineLibrary_Compac_Link_checksumCode: Property = Property(name="checksumCode", type=IntegerType)
MachineLibrary_Compac_Link_retry: Property = Property(name="retry", type=IntegerType)
MachineLibrary_Compac_Link_timeout: Property = Property(name="timeout", type=IntegerType)
MachineLibrary_Compac_Link_bcc: Property = Property(name="bcc", type=IntegerType)
MachineLibrary_Compac_Link_maxDataLength: Property = Property(name="maxDataLength", type=IntegerType)
MachineLibrary_Compac_Link_splitLongMessage: Property = Property(name="splitLongMessage", type=IntegerType)
MachineLibrary_Compac_Link_useNotENQ: Property = Property(name="useNotENQ", type=IntegerType)
MachineLibrary_Compac_Link.attributes={MachineLibrary_Compac_Link_checksum, MachineLibrary_Compac_Link_useNotACK_NAK, MachineLibrary_Compac_Link_useNotENQ, MachineLibrary_Compac_Link_timeout, MachineLibrary_Compac_Link_commConfig, MachineLibrary_Compac_Link_bytecountcode, MachineLibrary_Compac_Link_byteCount, MachineLibrary_Compac_Link_checksumCode, MachineLibrary_Compac_Link_splitLongMessage, MachineLibrary_Compac_Link_maxDataLength, MachineLibrary_Compac_Link_params, MachineLibrary_Compac_Link_bcc, MachineLibrary_Compac_Link_retry, MachineLibrary_Compac_Link_port}

# MachineLibrary_IBMWebsphereMQ class attributes and methods
MachineLibrary_IBMWebsphereMQ_qName: Property = Property(name="qName", type=StringType)
MachineLibrary_IBMWebsphereMQ_readQueName: Property = Property(name="readQueName", type=StringType)
MachineLibrary_IBMWebsphereMQ_readQueMgrName: Property = Property(name="readQueMgrName", type=StringType)
MachineLibrary_IBMWebsphereMQ_readDynamicQueName: Property = Property(name="readDynamicQueName", type=StringType)
MachineLibrary_IBMWebsphereMQ_sendQueName: Property = Property(name="sendQueName", type=StringType)
MachineLibrary_IBMWebsphereMQ_sendQueMgrName: Property = Property(name="sendQueMgrName", type=StringType)
MachineLibrary_IBMWebsphereMQ_sendDynamicQueName: Property = Property(name="sendDynamicQueName", type=StringType)
MachineLibrary_IBMWebsphereMQ_sendBuffer: Property = Property(name="sendBuffer", type=IntegerType)
MachineLibrary_IBMWebsphereMQ_receiveBuffer: Property = Property(name="receiveBuffer", type=IntegerType)
MachineLibrary_IBMWebsphereMQ_maxDataSize: Property = Property(name="maxDataSize", type=IntegerType)
MachineLibrary_IBMWebsphereMQ.attributes={MachineLibrary_IBMWebsphereMQ_readQueName, MachineLibrary_IBMWebsphereMQ_maxDataSize, MachineLibrary_IBMWebsphereMQ_qName, MachineLibrary_IBMWebsphereMQ_sendBuffer, MachineLibrary_IBMWebsphereMQ_sendDynamicQueName, MachineLibrary_IBMWebsphereMQ_sendQueName, MachineLibrary_IBMWebsphereMQ_readQueMgrName, MachineLibrary_IBMWebsphereMQ_readDynamicQueName, MachineLibrary_IBMWebsphereMQ_receiveBuffer, MachineLibrary_IBMWebsphereMQ_sendQueMgrName}

# MachineLibrary_DPbase_Link class attributes and methods
MachineLibrary_DPbase_Link_maxNodes: Property = Property(name="maxNodes", type=IntegerType)
MachineLibrary_DPbase_Link_cp_name: Property = Property(name="cp_name", type=StringType)
MachineLibrary_DPbase_Link_speed: Property = Property(name="speed", type=IntegerType)
MachineLibrary_DPbase_Link.attributes={MachineLibrary_DPbase_Link_speed, MachineLibrary_DPbase_Link_cp_name, MachineLibrary_DPbase_Link_maxNodes}

# MachineLibrary_DPbase_Node class attributes and methods
MachineLibrary_DPbase_Node_nodeNo: Property = Property(name="nodeNo", type=IntegerType)
MachineLibrary_DPbase_Node_isXPS: Property = Property(name="isXPS", type=IntegerType)
MachineLibrary_DPbase_Node.attributes={MachineLibrary_DPbase_Node_nodeNo, MachineLibrary_DPbase_Node_isXPS}

# MachineLibrary_NodeGeneral_AccuPycMeter class attributes and methods
MachineLibrary_NodeGeneral_AccuPycMeter_polling: Property = Property(name="polling", type=IntegerType)
MachineLibrary_NodeGeneral_AccuPycMeter_runTimout: Property = Property(name="runTimout", type=IntegerType)
MachineLibrary_NodeGeneral_AccuPycMeter_expectSampleWeight: Property = Property(name="expectSampleWeight", type=IntegerType)
MachineLibrary_NodeGeneral_AccuPycMeter_sendSampleWeight: Property = Property(name="sendSampleWeight", type=IntegerType)
MachineLibrary_NodeGeneral_AccuPycMeter.attributes={MachineLibrary_NodeGeneral_AccuPycMeter_polling, MachineLibrary_NodeGeneral_AccuPycMeter_sendSampleWeight, MachineLibrary_NodeGeneral_AccuPycMeter_expectSampleWeight, MachineLibrary_NodeGeneral_AccuPycMeter_runTimout}

# MachineLibrary_NodeGeneral_RigakuXRF class attributes and methods
MachineLibrary_NodeGeneral_RigakuXRF_timeout: Property = Property(name="timeout", type=IntegerType)
MachineLibrary_NodeGeneral_RigakuXRF_bDoNotshiftAtExit: Property = Property(name="bDoNotshiftAtExit", type=IntegerType)
MachineLibrary_NodeGeneral_RigakuXRF_timerToSendStatus: Property = Property(name="timerToSendStatus", type=IntegerType)
MachineLibrary_NodeGeneral_RigakuXRF_timeoutResponce: Property = Property(name="timeoutResponce", type=IntegerType)
MachineLibrary_NodeGeneral_RigakuXRF.attributes={MachineLibrary_NodeGeneral_RigakuXRF_timeoutResponce, MachineLibrary_NodeGeneral_RigakuXRF_timerToSendStatus, MachineLibrary_NodeGeneral_RigakuXRF_bDoNotshiftAtExit, MachineLibrary_NodeGeneral_RigakuXRF_timeout}

# MachineLibrary_Units class attributes and methods
MachineLibrary_Units_unitName: Property = Property(name="unitName", type=StringType)
MachineLibrary_Units_unitNo: Property = Property(name="unitNo", type=IntegerType)
MachineLibrary_Units_internalUniNo: Property = Property(name="internalUniNo", type=IntegerType)
MachineLibrary_Units.attributes={MachineLibrary_Units_unitName, MachineLibrary_Units_internalUniNo, MachineLibrary_Units_unitNo}

# MachineLibrary_Commands class attributes and methods

# MachineLibrary_NodePrograms class attributes and methods

# MachineLibrary_Parameters class attributes and methods
MachineLibrary_Parameters_parameterConfigYes: Property = Property(name="parameterConfigYes", type=StringType)
MachineLibrary_Parameters_parameterConfigNo: Property = Property(name="parameterConfigNo", type=StringType)
MachineLibrary_Parameters.attributes={MachineLibrary_Parameters_parameterConfigYes, MachineLibrary_Parameters_parameterConfigNo}

# MachineLibrary_CommunicationData class attributes and methods
MachineLibrary_CommunicationData_comSendDataAddress: Property = Property(name="comSendDataAddress", type=StringType)
MachineLibrary_CommunicationData_comSendDataLength: Property = Property(name="comSendDataLength", type=IntegerType)
MachineLibrary_CommunicationData_comRequestDataAddress: Property = Property(name="comRequestDataAddress", type=StringType)
MachineLibrary_CommunicationData_comRequestDataLength: Property = Property(name="comRequestDataLength", type=IntegerType)
MachineLibrary_CommunicationData_comErrorDataAddress: Property = Property(name="comErrorDataAddress", type=StringType)
MachineLibrary_CommunicationData_comErrorDataLength: Property = Property(name="comErrorDataLength", type=IntegerType)
MachineLibrary_CommunicationData_comSIDDataAddress: Property = Property(name="comSIDDataAddress", type=StringType)
MachineLibrary_CommunicationData_comSIDDataLength: Property = Property(name="comSIDDataLength", type=IntegerType)
MachineLibrary_CommunicationData_comProgressIndDataAddress: Property = Property(name="comProgressIndDataAddress", type=StringType)
MachineLibrary_CommunicationData_comProgressIndDataLength: Property = Property(name="comProgressIndDataLength", type=IntegerType)
MachineLibrary_CommunicationData.attributes={MachineLibrary_CommunicationData_comSendDataLength, MachineLibrary_CommunicationData_comSIDDataLength, MachineLibrary_CommunicationData_comErrorDataAddress, MachineLibrary_CommunicationData_comSendDataAddress, MachineLibrary_CommunicationData_comErrorDataLength, MachineLibrary_CommunicationData_comRequestDataAddress, MachineLibrary_CommunicationData_comSIDDataAddress, MachineLibrary_CommunicationData_comProgressIndDataAddress, MachineLibrary_CommunicationData_comProgressIndDataLength, MachineLibrary_CommunicationData_comRequestDataLength}

# MachineLibrary_NodeSpecialConfiguration class attributes and methods

# MachineLibrary_NodeGeneral class attributes and methods
MachineLibrary_NodeGeneral_canCreateStateTag: Property = Property(name="canCreateStateTag", type=StringType)
MachineLibrary_NodeGeneral_canCreateErrorTag: Property = Property(name="canCreateErrorTag", type=StringType)
MachineLibrary_NodeGeneral.attributes={MachineLibrary_NodeGeneral_canCreateStateTag, MachineLibrary_NodeGeneral_canCreateErrorTag}

# MachineLibrary_NodeGeneralSpecial class attributes and methods

# MachineLibrary_NodeGeneral_Terminal class attributes and methods
MachineLibrary_NodeGeneral_Terminal_terminalType: Property = Property(name="terminalType", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_maxXValue: Property = Property(name="maxXValue", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_maxYValue: Property = Property(name="maxYValue", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_maxScreens: Property = Property(name="maxScreens", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_displayTime: Property = Property(name="displayTime", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_customTimer1: Property = Property(name="customTimer1", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_customTimer2: Property = Property(name="customTimer2", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_signalCarrierPresent: Property = Property(name="signalCarrierPresent", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_keyBoardSignalCarrierPresent: Property = Property(name="keyBoardSignalCarrierPresent", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_stationAuto: Property = Property(name="stationAuto", type=StringType)
MachineLibrary_NodeGeneral_Terminal_steelCarrier: Property = Property(name="steelCarrier", type=StringType)
MachineLibrary_NodeGeneral_Terminal_stationReady: Property = Property(name="stationReady", type=StringType)
MachineLibrary_NodeGeneral_Terminal_lenOfPlanID: Property = Property(name="lenOfPlanID", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_stationType: Property = Property(name="stationType", type=IntegerType)
MachineLibrary_NodeGeneral_Terminal_name_1: Property = Property(name="name_1", type=StringType)
MachineLibrary_NodeGeneral_Terminal_name_2: Property = Property(name="name_2", type=StringType)
MachineLibrary_NodeGeneral_Terminal_name_3: Property = Property(name="name_3", type=StringType)
MachineLibrary_NodeGeneral_Terminal_name_4: Property = Property(name="name_4", type=StringType)
MachineLibrary_NodeGeneral_Terminal_name_5: Property = Property(name="name_5", type=StringType)
MachineLibrary_NodeGeneral_Terminal_name_6: Property = Property(name="name_6", type=StringType)
MachineLibrary_NodeGeneral_Terminal.attributes={MachineLibrary_NodeGeneral_Terminal_steelCarrier, MachineLibrary_NodeGeneral_Terminal_maxScreens, MachineLibrary_NodeGeneral_Terminal_name_4, MachineLibrary_NodeGeneral_Terminal_maxYValue, MachineLibrary_NodeGeneral_Terminal_customTimer2, MachineLibrary_NodeGeneral_Terminal_keyBoardSignalCarrierPresent, MachineLibrary_NodeGeneral_Terminal_name_1, MachineLibrary_NodeGeneral_Terminal_terminalType, MachineLibrary_NodeGeneral_Terminal_name_2, MachineLibrary_NodeGeneral_Terminal_stationAuto, MachineLibrary_NodeGeneral_Terminal_displayTime, MachineLibrary_NodeGeneral_Terminal_maxXValue, MachineLibrary_NodeGeneral_Terminal_name_5, MachineLibrary_NodeGeneral_Terminal_name_6, MachineLibrary_NodeGeneral_Terminal_stationType, MachineLibrary_NodeGeneral_Terminal_customTimer1, MachineLibrary_NodeGeneral_Terminal_lenOfPlanID, MachineLibrary_NodeGeneral_Terminal_name_3, MachineLibrary_NodeGeneral_Terminal_stationReady, MachineLibrary_NodeGeneral_Terminal_signalCarrierPresent}

# MachineLibrary_NodeGeneral_PM2PM class attributes and methods
MachineLibrary_NodeGeneral_PM2PM_timeServer: Property = Property(name="timeServer", type=IntegerType)
MachineLibrary_NodeGeneral_PM2PM_type: Property = Property(name="type", type=IntegerType)
MachineLibrary_NodeGeneral_PM2PM.attributes={MachineLibrary_NodeGeneral_PM2PM_timeServer, MachineLibrary_NodeGeneral_PM2PM_type}

# MachineLibrary_NodeGeneral_RemotePM class attributes and methods
MachineLibrary_NodeGeneral_RemotePM_timeServer: Property = Property(name="timeServer", type=IntegerType)
MachineLibrary_NodeGeneral_RemotePM_system: Property = Property(name="system", type=StringType)
MachineLibrary_NodeGeneral_RemotePM.attributes={MachineLibrary_NodeGeneral_RemotePM_system, MachineLibrary_NodeGeneral_RemotePM_timeServer}

# MachineLibrary_NodeGeneral_WinCC2WinCC class attributes and methods
MachineLibrary_NodeGeneral_WinCC2WinCC_prefix: Property = Property(name="prefix", type=StringType)
MachineLibrary_NodeGeneral_WinCC2WinCC.attributes={MachineLibrary_NodeGeneral_WinCC2WinCC_prefix}

# MachineLibrary_WinCCAddTag class attributes and methods
MachineLibrary_WinCCAddTag_winCCTag: Property = Property(name="winCCTag", type=StringType)
MachineLibrary_WinCCAddTag.attributes={MachineLibrary_WinCCAddTag_winCCTag}

# MachineLibrary_Positions class attributes and methods

# MachineLibrary_StausBits class attributes and methods

# MachineLibrary_PLCtoPmMatrix class attributes and methods
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit0: Property = Property(name="plcpmmatrixBit0", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit1: Property = Property(name="plcpmmatrixBit1", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit2: Property = Property(name="plcpmmatrixBit2", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit3: Property = Property(name="plcpmmatrixBit3", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit4: Property = Property(name="plcpmmatrixBit4", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit5: Property = Property(name="plcpmmatrixBit5", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit6: Property = Property(name="plcpmmatrixBit6", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit7: Property = Property(name="plcpmmatrixBit7", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit8: Property = Property(name="plcpmmatrixBit8", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit9: Property = Property(name="plcpmmatrixBit9", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit11: Property = Property(name="plcpmmatrixBit11", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit10: Property = Property(name="plcpmmatrixBit10", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit12: Property = Property(name="plcpmmatrixBit12", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit13: Property = Property(name="plcpmmatrixBit13", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit14: Property = Property(name="plcpmmatrixBit14", type=IntegerType)
MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit15: Property = Property(name="plcpmmatrixBit15", type=IntegerType)
MachineLibrary_PLCtoPmMatrix.attributes={MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit13, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit8, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit10, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit11, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit1, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit9, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit14, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit12, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit0, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit5, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit2, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit6, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit7, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit4, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit15, MachineLibrary_PLCtoPmMatrix_plcpmmatrixBit3}

# MachineLibrary_UnitPrograms class attributes and methods

# MachineLibrary_Buttons class attributes and methods

# MachineLibrary_UnitGeneral class attributes and methods

# MachineLibrary_UnitGeneralSpecial class attributes and methods

# MachineLibrary_UnitSpecialConfiguration class attributes and methods

# MachineLibrary_UnitGeneralParameters class attributes and methods
MachineLibrary_UnitGeneralParameters_KeyWord_1: Property = Property(name="KeyWord_1", type=StringType)
MachineLibrary_UnitGeneralParameters_UseWith_1: Property = Property(name="UseWith_1", type=StringType)
MachineLibrary_UnitGeneralParameters_seq_X: Property = Property(name="seq_X", type=IntegerType)
MachineLibrary_UnitGeneralParameters_paraName_1: Property = Property(name="paraName_1", type=StringType)
MachineLibrary_UnitGeneralParameters_comment_1: Property = Property(name="comment_1", type=StringType)
MachineLibrary_UnitGeneralParameters_unit_1: Property = Property(name="unit_1", type=StringType)
MachineLibrary_UnitGeneralParameters_minValue_1: Property = Property(name="minValue_1", type=IntegerType)
MachineLibrary_UnitGeneralParameters_maxValue_1: Property = Property(name="maxValue_1", type=IntegerType)
MachineLibrary_UnitGeneralParameters_defaultValue_1: Property = Property(name="defaultValue_1", type=IntegerType)
MachineLibrary_UnitGeneralParameters_visibleType_1: Property = Property(name="visibleType_1", type=IntegerType)
MachineLibrary_UnitGeneralParameters_canBeChange_1: Property = Property(name="canBeChange_1", type=IntegerType)
MachineLibrary_UnitGeneralParameters.attributes={MachineLibrary_UnitGeneralParameters_visibleType_1, MachineLibrary_UnitGeneralParameters_KeyWord_1, MachineLibrary_UnitGeneralParameters_UseWith_1, MachineLibrary_UnitGeneralParameters_seq_X, MachineLibrary_UnitGeneralParameters_maxValue_1, MachineLibrary_UnitGeneralParameters_defaultValue_1, MachineLibrary_UnitGeneralParameters_unit_1, MachineLibrary_UnitGeneralParameters_minValue_1, MachineLibrary_UnitGeneralParameters_comment_1, MachineLibrary_UnitGeneralParameters_canBeChange_1, MachineLibrary_UnitGeneralParameters_paraName_1}

# MachineLibrary_UnitGeneral_Terminal class attributes and methods
MachineLibrary_UnitGeneral_Terminal_thisStation: Property = Property(name="thisStation", type=StringType)
MachineLibrary_UnitGeneral_Terminal_station1: Property = Property(name="station1", type=StringType)
MachineLibrary_UnitGeneral_Terminal_station2: Property = Property(name="station2", type=StringType)
MachineLibrary_UnitGeneral_Terminal_station3: Property = Property(name="station3", type=StringType)
MachineLibrary_UnitGeneral_Terminal_station4: Property = Property(name="station4", type=StringType)
MachineLibrary_UnitGeneral_Terminal_station5: Property = Property(name="station5", type=StringType)
MachineLibrary_UnitGeneral_Terminal.attributes={MachineLibrary_UnitGeneral_Terminal_station5, MachineLibrary_UnitGeneral_Terminal_station3, MachineLibrary_UnitGeneral_Terminal_thisStation, MachineLibrary_UnitGeneral_Terminal_station4, MachineLibrary_UnitGeneral_Terminal_station1, MachineLibrary_UnitGeneral_Terminal_station2}

# MachineLibrary_UnitGeneral_HostPC class attributes and methods
MachineLibrary_UnitGeneral_HostPC_maxIndex: Property = Property(name="maxIndex", type=IntegerType)
MachineLibrary_UnitGeneral_HostPC_index: Property = Property(name="index", type=IntegerType)
MachineLibrary_UnitGeneral_HostPC_replyOnLink: Property = Property(name="replyOnLink", type=IntegerType)
MachineLibrary_UnitGeneral_HostPC_writeDumyIfNoDataExist: Property = Property(name="writeDumyIfNoDataExist", type=IntegerType)
MachineLibrary_UnitGeneral_HostPC.attributes={MachineLibrary_UnitGeneral_HostPC_replyOnLink, MachineLibrary_UnitGeneral_HostPC_writeDumyIfNoDataExist, MachineLibrary_UnitGeneral_HostPC_index, MachineLibrary_UnitGeneral_HostPC_maxIndex}

# MachineLibrary_UnitGeneral_Remote class attributes and methods
MachineLibrary_UnitGeneral_Remote_editWSDB: Property = Property(name="editWSDB", type=BooleanType)
MachineLibrary_UnitGeneral_Remote_handshakeT: Property = Property(name="handshakeT", type=IntegerType)
MachineLibrary_UnitGeneral_Remote_handshakeQ: Property = Property(name="handshakeQ", type=StringType)
MachineLibrary_UnitGeneral_Remote_handshakeA: Property = Property(name="handshakeA", type=StringType)
MachineLibrary_UnitGeneral_Remote.attributes={MachineLibrary_UnitGeneral_Remote_editWSDB, MachineLibrary_UnitGeneral_Remote_handshakeA, MachineLibrary_UnitGeneral_Remote_handshakeT, MachineLibrary_UnitGeneral_Remote_handshakeQ}

# MachineLibrary_UnitGeneral_PM2PM class attributes and methods
MachineLibrary_UnitGeneral_PM2PM_sid_Mask: Property = Property(name="sid_Mask", type=StringType)
MachineLibrary_UnitGeneral_PM2PM_processFeedBack: Property = Property(name="processFeedBack", type=StringType)
MachineLibrary_UnitGeneral_PM2PM.attributes={MachineLibrary_UnitGeneral_PM2PM_sid_Mask, MachineLibrary_UnitGeneral_PM2PM_processFeedBack}

# MachineLibrary_UnitGeneral_AccPyc class attributes and methods
MachineLibrary_UnitGeneral_AccPyc_cupWeight: Property = Property(name="cupWeight", type=FloatType)
MachineLibrary_UnitGeneral_AccPyc_minSampleWeight: Property = Property(name="minSampleWeight", type=FloatType)
MachineLibrary_UnitGeneral_AccPyc.attributes={MachineLibrary_UnitGeneral_AccPyc_cupWeight, MachineLibrary_UnitGeneral_AccPyc_minSampleWeight}

# MachineLibrary_UnitGeneral_SuperQ class attributes and methods
MachineLibrary_UnitGeneral_SuperQ_lastPosInInstrument: Property = Property(name="lastPosInInstrument", type=IntegerType)
MachineLibrary_UnitGeneral_SuperQ_lastPosAnalysing: Property = Property(name="lastPosAnalysing", type=IntegerType)
MachineLibrary_UnitGeneral_SuperQ.attributes={MachineLibrary_UnitGeneral_SuperQ_lastPosAnalysing, MachineLibrary_UnitGeneral_SuperQ_lastPosInInstrument}

# MachineLibrary_UnitGeneral_RigakuXRF class attributes and methods
MachineLibrary_UnitGeneral_RigakuXRF_lastPoHAG_SIInstrument: Property = Property(name="lastPoHAG_SIInstrument", type=IntegerType)
MachineLibrary_UnitGeneral_RigakuXRF_lastPosAnalyHAG_SIg: Property = Property(name="lastPosAnalyHAG_SIg", type=IntegerType)
MachineLibrary_UnitGeneral_RigakuXRF_lastPosInInstrument: Property = Property(name="lastPosInInstrument", type=IntegerType)
MachineLibrary_UnitGeneral_RigakuXRF_separator: Property = Property(name="separator", type=IntegerType)
MachineLibrary_UnitGeneral_RigakuXRF.attributes={MachineLibrary_UnitGeneral_RigakuXRF_lastPosAnalyHAG_SIg, MachineLibrary_UnitGeneral_RigakuXRF_lastPoHAG_SIInstrument, MachineLibrary_UnitGeneral_RigakuXRF_separator, MachineLibrary_UnitGeneral_RigakuXRF_lastPosInInstrument}

# MachineLibrary_UnitGeneral_Scanner class attributes and methods
MachineLibrary_UnitGeneral_Scanner_forcedSampleType: Property = Property(name="forcedSampleType", type=IntegerType)
MachineLibrary_UnitGeneral_Scanner_registerSample: Property = Property(name="registerSample", type=IntegerType)
MachineLibrary_UnitGeneral_Scanner_start: Property = Property(name="start", type=IntegerType)
MachineLibrary_UnitGeneral_Scanner_length: Property = Property(name="length", type=IntegerType)
MachineLibrary_UnitGeneral_Scanner_fillWith: Property = Property(name="fillWith", type=StringType)
MachineLibrary_UnitGeneral_Scanner_addString: Property = Property(name="addString", type=StringType)
MachineLibrary_UnitGeneral_Scanner_preString: Property = Property(name="preString", type=StringType)
MachineLibrary_UnitGeneral_Scanner.attributes={MachineLibrary_UnitGeneral_Scanner_fillWith, MachineLibrary_UnitGeneral_Scanner_registerSample, MachineLibrary_UnitGeneral_Scanner_preString, MachineLibrary_UnitGeneral_Scanner_addString, MachineLibrary_UnitGeneral_Scanner_start, MachineLibrary_UnitGeneral_Scanner_forcedSampleType, MachineLibrary_UnitGeneral_Scanner_length}

# MachineLibrary_ErrorMessage_OBLFOES class attributes and methods
MachineLibrary_ErrorMessage_OBLFOES_errorMessage: Property = Property(name="errorMessage", type=StringType)
MachineLibrary_ErrorMessage_OBLFOES.attributes={MachineLibrary_ErrorMessage_OBLFOES_errorMessage}

# MachineLibrary_GeneralParameter_SuperQXRF class attributes and methods
MachineLibrary_GeneralParameter_SuperQXRF_switchRemote: Property = Property(name="switchRemote", type=StringType)
MachineLibrary_GeneralParameter_SuperQXRF_startList: Property = Property(name="startList", type=StringType)
MachineLibrary_GeneralParameter_SuperQXRF_listName: Property = Property(name="listName", type=StringType)
MachineLibrary_GeneralParameter_SuperQXRF.attributes={MachineLibrary_GeneralParameter_SuperQXRF_listName, MachineLibrary_GeneralParameter_SuperQXRF_startList, MachineLibrary_GeneralParameter_SuperQXRF_switchRemote}

# MachineLibrary_UnitConfig_Terminal class attributes and methods

# MachineLibrary_UnitConfig_OBLF_OES class attributes and methods

# MachineLibrary_UnitConfig_SuperQ_XRF class attributes and methods

# MachineLibrary_UnitConfig_ARL_XRF_OES class attributes and methods

# MachineLibrary_UnitConfig_Host class attributes and methods

# MachineLibrary_History_AccuPycMeter class attributes and methods

# MachineLibrary_SepByComma_Scanner class attributes and methods
MachineLibrary_SepByComma_Scanner_activ: Property = Property(name="activ", type=IntegerType)
MachineLibrary_SepByComma_Scanner_preDefWS: Property = Property(name="preDefWS", type=IntegerType)
MachineLibrary_SepByComma_Scanner.attributes={MachineLibrary_SepByComma_Scanner_preDefWS, MachineLibrary_SepByComma_Scanner_activ}

# MachineLibrary_CheckAddSID_PM2PM class attributes and methods

# MachineLibrary_Translate_Terminal class attributes and methods
MachineLibrary_Translate_Terminal_auto_Ready: Property = Property(name="auto_Ready", type=StringType)
MachineLibrary_Translate_Terminal_auto_Busy: Property = Property(name="auto_Busy", type=StringType)
MachineLibrary_Translate_Terminal_man_Ready: Property = Property(name="man_Ready", type=StringType)
MachineLibrary_Translate_Terminal_man_Busy: Property = Property(name="man_Busy", type=StringType)
MachineLibrary_Translate_Terminal.attributes={MachineLibrary_Translate_Terminal_man_Busy, MachineLibrary_Translate_Terminal_man_Ready, MachineLibrary_Translate_Terminal_auto_Busy, MachineLibrary_Translate_Terminal_auto_Ready}

# MachineLibrary_OutputRequest_OBLFOES class attributes and methods
MachineLibrary_OutputRequest_OBLFOES_name: Property = Property(name="name", type=StringType)
MachineLibrary_OutputRequest_OBLFOES.attributes={MachineLibrary_OutputRequest_OBLFOES_name}

# MachineLibrary_TestRequest_OBLFOES class attributes and methods
MachineLibrary_TestRequest_OBLFOES_name: Property = Property(name="name", type=StringType)
MachineLibrary_TestRequest_OBLFOES.attributes={MachineLibrary_TestRequest_OBLFOES_name}

# MachineLibrary_RecalRequest_OBLFOES class attributes and methods
MachineLibrary_RecalRequest_OBLFOES_name: Property = Property(name="name", type=StringType)
MachineLibrary_RecalRequest_OBLFOES.attributes={MachineLibrary_RecalRequest_OBLFOES_name}

# MachineLibrary_Moved_Host class attributes and methods
MachineLibrary_Moved_Host_pos0: Property = Property(name="pos0", type=IntegerType)
MachineLibrary_Moved_Host_type0: Property = Property(name="type0", type=IntegerType)
MachineLibrary_Moved_Host_writePositionNameInFile: Property = Property(name="writePositionNameInFile", type=IntegerType)
MachineLibrary_Moved_Host_report_ALL: Property = Property(name="report_ALL", type=IntegerType)
MachineLibrary_Moved_Host.attributes={MachineLibrary_Moved_Host_pos0, MachineLibrary_Moved_Host_writePositionNameInFile, MachineLibrary_Moved_Host_report_ALL, MachineLibrary_Moved_Host_type0}

# MachineLibrary_ControlSamples_SuperQXRF class attributes and methods
MachineLibrary_ControlSamples_SuperQXRF_outOfControl: Property = Property(name="outOfControl", type=IntegerType)
MachineLibrary_ControlSamples_SuperQXRF.attributes={MachineLibrary_ControlSamples_SuperQXRF_outOfControl}

# MachineLibrary_Communication_SuperQXRF class attributes and methods
MachineLibrary_Communication_SuperQXRF_enq_ACK_Protocol: Property = Property(name="enq_ACK_Protocol", type=IntegerType)
MachineLibrary_Communication_SuperQXRF.attributes={MachineLibrary_Communication_SuperQXRF_enq_ACK_Protocol}

# MachineLibrary_CheckSampleRunTime_SuperQXRF class attributes and methods

# MachineLibrary_CheckSample_SuperQXRF class attributes and methods

# MachineLibrary_CheckFilling_ARL_XRF_OES class attributes and methods
MachineLibrary_CheckFilling_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_CheckFilling_ARL_XRF_OES.attributes={MachineLibrary_CheckFilling_ARL_XRF_OES_name}

# MachineLibrary_ExecuteFiling_ARL_XRF_OES class attributes and methods
MachineLibrary_ExecuteFiling_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_ExecuteFiling_ARL_XRF_OES.attributes={MachineLibrary_ExecuteFiling_ARL_XRF_OES_name}

# MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES class attributes and methods
MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES.attributes={MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES_name}

# MachineLibrary_ExePrepUnit_ARL_XRF_OES class attributes and methods
MachineLibrary_ExePrepUnit_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_ExePrepUnit_ARL_XRF_OES.attributes={MachineLibrary_ExePrepUnit_ARL_XRF_OES_name}

# MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES class attributes and methods
MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES.attributes={MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES_name}

# MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES class attributes and methods
MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES.attributes={MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES_name}

# MachineLibrary_DisableSCT_ARL_XRF_OES class attributes and methods
MachineLibrary_DisableSCT_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_DisableSCT_ARL_XRF_OES.attributes={MachineLibrary_DisableSCT_ARL_XRF_OES_name}

# MachineLibrary_Settings_ARL_XRF_OES class attributes and methods
MachineLibrary_Settings_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_Settings_ARL_XRF_OES.attributes={MachineLibrary_Settings_ARL_XRF_OES_name}

# MachineLibrary_GeneralSetting_ARL_XRF_OES class attributes and methods
MachineLibrary_GeneralSetting_ARL_XRF_OES_name: Property = Property(name="name", type=StringType)
MachineLibrary_GeneralSetting_ARL_XRF_OES.attributes={MachineLibrary_GeneralSetting_ARL_XRF_OES_name}

# MachineLibrary_PS_Process_Finished_ARL_XRF_OES class attributes and methods
MachineLibrary_PS_Process_Finished_ARL_XRF_OES_noSuccess: Property = Property(name="noSuccess", type=StringType)
MachineLibrary_PS_Process_Finished_ARL_XRF_OES.attributes={MachineLibrary_PS_Process_Finished_ARL_XRF_OES_noSuccess}

# MachineLibrary_File_Sample_ARL_XRF_OES class attributes and methods
MachineLibrary_File_Sample_ARL_XRF_OES_noSuccess: Property = Property(name="noSuccess", type=StringType)
MachineLibrary_File_Sample_ARL_XRF_OES.attributes={MachineLibrary_File_Sample_ARL_XRF_OES_noSuccess}

# MachineLibrary_Report_Host class attributes and methods
MachineLibrary_Report_Host_note1: Property = Property(name="note1", type=StringType)
MachineLibrary_Report_Host_note: Property = Property(name="note", type=StringType)
MachineLibrary_Report_Host_sampleMoved: Property = Property(name="sampleMoved", type=IntegerType)
MachineLibrary_Report_Host_sampleRemoved: Property = Property(name="sampleRemoved", type=IntegerType)
MachineLibrary_Report_Host_sampleInsert: Property = Property(name="sampleInsert", type=IntegerType)
MachineLibrary_Report_Host_stateChanged: Property = Property(name="stateChanged", type=IntegerType)
MachineLibrary_Report_Host_fileName: Property = Property(name="fileName", type=StringType)
MachineLibrary_Report_Host_minType: Property = Property(name="minType", type=IntegerType)
MachineLibrary_Report_Host_maxType: Property = Property(name="maxType", type=IntegerType)
MachineLibrary_Report_Host_internal: Property = Property(name="internal", type=IntegerType)
MachineLibrary_Report_Host_rawData: Property = Property(name="rawData", type=IntegerType)
MachineLibrary_Report_Host_sendErrorWarningsMsgOnly: Property = Property(name="sendErrorWarningsMsgOnly", type=IntegerType)
MachineLibrary_Report_Host_sendLifeMessages: Property = Property(name="sendLifeMessages", type=IntegerType)
MachineLibrary_Report_Host_timeStamp: Property = Property(name="timeStamp", type=IntegerType)
MachineLibrary_Report_Host.attributes={MachineLibrary_Report_Host_sendErrorWarningsMsgOnly, MachineLibrary_Report_Host_sampleMoved, MachineLibrary_Report_Host_internal, MachineLibrary_Report_Host_maxType, MachineLibrary_Report_Host_stateChanged, MachineLibrary_Report_Host_note, MachineLibrary_Report_Host_rawData, MachineLibrary_Report_Host_sampleRemoved, MachineLibrary_Report_Host_sampleInsert, MachineLibrary_Report_Host_note1, MachineLibrary_Report_Host_sendLifeMessages, MachineLibrary_Report_Host_timeStamp, MachineLibrary_Report_Host_fileName, MachineLibrary_Report_Host_minType}

# MachineLibrary_WS_Update_Host class attributes and methods
MachineLibrary_WS_Update_Host_checkUnit: Property = Property(name="checkUnit", type=IntegerType)
MachineLibrary_WS_Update_Host_AllowUnit0: Property = Property(name="AllowUnit0", type=IntegerType)
MachineLibrary_WS_Update_Host.attributes={MachineLibrary_WS_Update_Host_AllowUnit0, MachineLibrary_WS_Update_Host_checkUnit}

# MachineLibrary_InsertRemove_Host class attributes and methods
MachineLibrary_InsertRemove_Host_report_All: Property = Property(name="report_All", type=IntegerType)
MachineLibrary_InsertRemove_Host.attributes={MachineLibrary_InsertRemove_Host_report_All}

# MachineLibrary_OES_XRF_Condition class attributes and methods
MachineLibrary_OES_XRF_Condition_paraName: Property = Property(name="paraName", type=StringType)
MachineLibrary_OES_XRF_Condition_para: Property = Property(name="para", type=StringType)
MachineLibrary_OES_XRF_Condition_comment: Property = Property(name="comment", type=StringType)
MachineLibrary_OES_XRF_Condition_seq_X: Property = Property(name="seq_X", type=IntegerType)
MachineLibrary_OES_XRF_Condition.attributes={MachineLibrary_OES_XRF_Condition_paraName, MachineLibrary_OES_XRF_Condition_comment, MachineLibrary_OES_XRF_Condition_para, MachineLibrary_OES_XRF_Condition_seq_X}

# MachineLibrary_CheckSampleRunTimeParams_SuperQXRF class attributes and methods
MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_sampleType: Property = Property(name="sampleType", type=IntegerType)
MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_value: Property = Property(name="value", type=IntegerType)
MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.attributes={MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_value, MachineLibrary_CheckSampleRunTimeParams_SuperQXRF_sampleType}

# MachineLibrary_CheckSampleConfig_SuperQXRF class attributes and methods
MachineLibrary_CheckSampleConfig_SuperQXRF_anaProg: Property = Property(name="anaProg", type=StringType)
MachineLibrary_CheckSampleConfig_SuperQXRF_minutes: Property = Property(name="minutes", type=StringType)
MachineLibrary_CheckSampleConfig_SuperQXRF_samples: Property = Property(name="samples", type=StringType)
MachineLibrary_CheckSampleConfig_SuperQXRF_program: Property = Property(name="program", type=StringType)
MachineLibrary_CheckSampleConfig_SuperQXRF_sampleID: Property = Property(name="sampleID", type=StringType)
MachineLibrary_CheckSampleConfig_SuperQXRF_seq_X: Property = Property(name="seq_X", type=IntegerType)
MachineLibrary_CheckSampleConfig_SuperQXRF.attributes={MachineLibrary_CheckSampleConfig_SuperQXRF_samples, MachineLibrary_CheckSampleConfig_SuperQXRF_sampleID, MachineLibrary_CheckSampleConfig_SuperQXRF_minutes, MachineLibrary_CheckSampleConfig_SuperQXRF_anaProg, MachineLibrary_CheckSampleConfig_SuperQXRF_seq_X, MachineLibrary_CheckSampleConfig_SuperQXRF_program}

# MachineLibrary_HistoryConfig_AccuPyc class attributes and methods
MachineLibrary_HistoryConfig_AccuPyc_currentSample: Property = Property(name="currentSample", type=StringType)
MachineLibrary_HistoryConfig_AccuPyc_currentSampleID: Property = Property(name="currentSampleID", type=StringType)
MachineLibrary_HistoryConfig_AccuPyc_sampleCupWeight: Property = Property(name="sampleCupWeight", type=FloatType)
MachineLibrary_HistoryConfig_AccuPyc.attributes={MachineLibrary_HistoryConfig_AccuPyc_currentSample, MachineLibrary_HistoryConfig_AccuPyc_sampleCupWeight, MachineLibrary_HistoryConfig_AccuPyc_currentSampleID}

# MachineLibrary_Button class attributes and methods
MachineLibrary_Button_buttonText: Property = Property(name="buttonText", type=StringType)
MachineLibrary_Button_commandNo: Property = Property(name="commandNo", type=IntegerType)
MachineLibrary_Button_buttonNo: Property = Property(name="buttonNo", type=IntegerType)
MachineLibrary_Button.attributes={MachineLibrary_Button_buttonText, MachineLibrary_Button_buttonNo, MachineLibrary_Button_commandNo}

# MachineLibrary_InsertRemove_Entry_Host class attributes and methods
MachineLibrary_InsertRemove_Entry_Host_entryNo: Property = Property(name="entryNo", type=IntegerType)
MachineLibrary_InsertRemove_Entry_Host_entryName: Property = Property(name="entryName", type=StringType)
MachineLibrary_InsertRemove_Entry_Host.attributes={MachineLibrary_InsertRemove_Entry_Host_entryNo, MachineLibrary_InsertRemove_Entry_Host_entryName}

# MachineLibrary_InsertRemove_Types_Host class attributes and methods
MachineLibrary_InsertRemove_Types_Host_typeNo: Property = Property(name="typeNo", type=IntegerType)
MachineLibrary_InsertRemove_Types_Host_typeValue: Property = Property(name="typeValue", type=StringType)
MachineLibrary_InsertRemove_Types_Host.attributes={MachineLibrary_InsertRemove_Types_Host_typeNo, MachineLibrary_InsertRemove_Types_Host_typeValue}

# MachineLibrary_InsertRemove_Keywords_Host class attributes and methods
MachineLibrary_InsertRemove_Keywords_Host_keywordKey: Property = Property(name="keywordKey", type=StringType)
MachineLibrary_InsertRemove_Keywords_Host_keywordValue: Property = Property(name="keywordValue", type=StringType)
MachineLibrary_InsertRemove_Keywords_Host.attributes={MachineLibrary_InsertRemove_Keywords_Host_keywordKey, MachineLibrary_InsertRemove_Keywords_Host_keywordValue}

# MachineLibrary_SepByComma_Field_Scanner class attributes and methods
MachineLibrary_SepByComma_Field_Scanner_fieldNo: Property = Property(name="fieldNo", type=IntegerType)
MachineLibrary_SepByComma_Field_Scanner_fieldName: Property = Property(name="fieldName", type=StringType)
MachineLibrary_SepByComma_Field_Scanner.attributes={MachineLibrary_SepByComma_Field_Scanner_fieldName, MachineLibrary_SepByComma_Field_Scanner_fieldNo}

# MachineLibrary_SepByComma_ID_Scanner class attributes and methods
MachineLibrary_SepByComma_ID_Scanner_idSeq_X: Property = Property(name="idSeq_X", type=IntegerType)
MachineLibrary_SepByComma_ID_Scanner_idValue: Property = Property(name="idValue", type=IntegerType)
MachineLibrary_SepByComma_ID_Scanner_idPrevValue: Property = Property(name="idPrevValue", type=StringType)
MachineLibrary_SepByComma_ID_Scanner_idCharValue: Property = Property(name="idCharValue", type=StringType)
MachineLibrary_SepByComma_ID_Scanner.attributes={MachineLibrary_SepByComma_ID_Scanner_idPrevValue, MachineLibrary_SepByComma_ID_Scanner_idCharValue, MachineLibrary_SepByComma_ID_Scanner_idValue, MachineLibrary_SepByComma_ID_Scanner_idSeq_X}

# MachineLibrary_CheckAddSID_Values_PM2PM class attributes and methods
MachineLibrary_CheckAddSID_Values_PM2PM_optionNo: Property = Property(name="optionNo", type=IntegerType)
MachineLibrary_CheckAddSID_Values_PM2PM_optonValue: Property = Property(name="optonValue", type=StringType)
MachineLibrary_CheckAddSID_Values_PM2PM.attributes={MachineLibrary_CheckAddSID_Values_PM2PM_optionNo, MachineLibrary_CheckAddSID_Values_PM2PM_optonValue}

# MachineLibrary_Position class attributes and methods
MachineLibrary_Position_posName: Property = Property(name="posName", type=StringType)
MachineLibrary_Position_posNo: Property = Property(name="posNo", type=IntegerType)
MachineLibrary_Position_posIndex: Property = Property(name="posIndex", type=IntegerType)
MachineLibrary_Position_posWarningOnDelete: Property = Property(name="posWarningOnDelete", type=IntegerType)
MachineLibrary_Position_posExit: Property = Property(name="posExit", type=IntegerType)
MachineLibrary_Position_posRemark: Property = Property(name="posRemark", type=StringType)
MachineLibrary_Position.attributes={MachineLibrary_Position_posWarningOnDelete, MachineLibrary_Position_posIndex, MachineLibrary_Position_posName, MachineLibrary_Position_posRemark, MachineLibrary_Position_posNo, MachineLibrary_Position_posExit}

# MachineLibrary_StatusBit class attributes and methods
MachineLibrary_StatusBit_bitName: Property = Property(name="bitName", type=StringType)
MachineLibrary_StatusBit_bitNo: Property = Property(name="bitNo", type=IntegerType)
MachineLibrary_StatusBit.attributes={MachineLibrary_StatusBit_bitName, MachineLibrary_StatusBit_bitNo}

# MachineLibrary_Command class attributes and methods
MachineLibrary_Command_commandName: Property = Property(name="commandName", type=StringType)
MachineLibrary_Command_commandNo: Property = Property(name="commandNo", type=StringType)
MachineLibrary_Command_commandProgParameter: Property = Property(name="commandProgParameter", type=IntegerType)
MachineLibrary_Command.attributes={MachineLibrary_Command_commandProgParameter, MachineLibrary_Command_commandNo, MachineLibrary_Command_commandName}

# MachineLibrary_NodeProgram class attributes and methods
MachineLibrary_NodeProgram_programName: Property = Property(name="programName", type=StringType)
MachineLibrary_NodeProgram_programAddress: Property = Property(name="programAddress", type=StringType)
MachineLibrary_NodeProgram_programLenPerParam: Property = Property(name="programLenPerParam", type=StringType)
MachineLibrary_NodeProgram_programSection: Property = Property(name="programSection", type=StringType)
MachineLibrary_NodeProgram_programNo: Property = Property(name="programNo", type=IntegerType)
MachineLibrary_NodeProgram.attributes={MachineLibrary_NodeProgram_programName, MachineLibrary_NodeProgram_programNo, MachineLibrary_NodeProgram_programSection, MachineLibrary_NodeProgram_programLenPerParam, MachineLibrary_NodeProgram_programAddress}

# MachineLibrary_UnitProgram class attributes and methods
MachineLibrary_UnitProgram_unitProgName: Property = Property(name="unitProgName", type=StringType)
MachineLibrary_UnitProgram.attributes={MachineLibrary_UnitProgram_unitProgName}

# MachineLibrary_UnitProgParameters class attributes and methods
MachineLibrary_UnitProgParameters_parameter: Property = Property(name="parameter", type=StringType)
MachineLibrary_UnitProgParameters_parameterNo: Property = Property(name="parameterNo", type=IntegerType)
MachineLibrary_UnitProgParameters.attributes={MachineLibrary_UnitProgParameters_parameterNo, MachineLibrary_UnitProgParameters_parameter}

# MachineLibrary_Parameter class attributes and methods
MachineLibrary_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
MachineLibrary_Parameter_parameterT1: Property = Property(name="parameterT1", type=StringType)
MachineLibrary_Parameter_parameterT2: Property = Property(name="parameterT2", type=StringType)
MachineLibrary_Parameter_parameterV: Property = Property(name="parameterV", type=StringType)
MachineLibrary_Parameter_parameterType: Property = Property(name="parameterType", type=StringType)
MachineLibrary_Parameter_parameterV0: Property = Property(name="parameterV0", type=StringType)
MachineLibrary_Parameter_parameterV1: Property = Property(name="parameterV1", type=StringType)
MachineLibrary_Parameter_parameterMin: Property = Property(name="parameterMin", type=IntegerType)
MachineLibrary_Parameter_parameterMax: Property = Property(name="parameterMax", type=IntegerType)
MachineLibrary_Parameter_parameterParaLen: Property = Property(name="parameterParaLen", type=IntegerType)
MachineLibrary_Parameter_parameterConfig: Property = Property(name="parameterConfig", type=StringType)
MachineLibrary_Parameter.attributes={MachineLibrary_Parameter_parameterMin, MachineLibrary_Parameter_parameterT1, MachineLibrary_Parameter_parameterMax, MachineLibrary_Parameter_parameterConfig, MachineLibrary_Parameter_parameterT2, MachineLibrary_Parameter_parameterV, MachineLibrary_Parameter_parameterName, MachineLibrary_Parameter_parameterV1, MachineLibrary_Parameter_parameterType, MachineLibrary_Parameter_parameterV0, MachineLibrary_Parameter_parameterParaLen}

# MachineLibrary_ParamPrint class attributes and methods
MachineLibrary_ParamPrint_fontHightHeader: Property = Property(name="fontHightHeader", type=FloatType)
MachineLibrary_ParamPrint_fontHightData: Property = Property(name="fontHightData", type=FloatType)
MachineLibrary_ParamPrint_vertPosHeader: Property = Property(name="vertPosHeader", type=FloatType)
MachineLibrary_ParamPrint_vertPosData: Property = Property(name="vertPosData", type=FloatType)
MachineLibrary_ParamPrint_vertLineSpace: Property = Property(name="vertLineSpace", type=FloatType)
MachineLibrary_ParamPrint_horzPosLeftBorder: Property = Property(name="horzPosLeftBorder", type=FloatType)
MachineLibrary_ParamPrint_horzPosValues: Property = Property(name="horzPosValues", type=FloatType)
MachineLibrary_ParamPrint_dateStamp: Property = Property(name="dateStamp", type=StringType)
MachineLibrary_ParamPrint.attributes={MachineLibrary_ParamPrint_horzPosValues, MachineLibrary_ParamPrint_vertPosHeader, MachineLibrary_ParamPrint_vertPosData, MachineLibrary_ParamPrint_fontHightData, MachineLibrary_ParamPrint_fontHightHeader, MachineLibrary_ParamPrint_horzPosLeftBorder, MachineLibrary_ParamPrint_vertLineSpace, MachineLibrary_ParamPrint_dateStamp}

# MachineLibrary_Transfer class attributes and methods

# MachineLibrary_PlainMove class attributes and methods
MachineLibrary_PlainMove_plainmoveType: Property = Property(name="plainmoveType", type=IntegerType)
MachineLibrary_PlainMove_plainmoveSID_REF: Property = Property(name="plainmoveSID_REF", type=StringType)
MachineLibrary_PlainMove_plainmovePreDefWS: Property = Property(name="plainmovePreDefWS", type=StringType)
MachineLibrary_PlainMove.attributes={MachineLibrary_PlainMove_plainmoveSID_REF, MachineLibrary_PlainMove_plainmoveType, MachineLibrary_PlainMove_plainmovePreDefWS}

# MachineLibrary_RobotConfiguration class attributes and methods
MachineLibrary_RobotConfiguration_robotActivate: Property = Property(name="robotActivate", type=IntegerType)
MachineLibrary_RobotConfiguration_robotSystemID: Property = Property(name="robotSystemID", type=StringType)
MachineLibrary_RobotConfiguration_robotID: Property = Property(name="robotID", type=StringType)
MachineLibrary_RobotConfiguration_robotIPAddress: Property = Property(name="robotIPAddress", type=StringType)
MachineLibrary_RobotConfiguration.attributes={MachineLibrary_RobotConfiguration_robotID, MachineLibrary_RobotConfiguration_robotActivate, MachineLibrary_RobotConfiguration_robotSystemID, MachineLibrary_RobotConfiguration_robotIPAddress}

# MachineLibrary_TransferFileSection class attributes and methods
MachineLibrary_TransferFileSection_transferFile: Property = Property(name="transferFile", type=StringType)
MachineLibrary_TransferFileSection_transferSection: Property = Property(name="transferSection", type=StringType)
MachineLibrary_TransferFileSection_transferSeq: Property = Property(name="transferSeq", type=IntegerType)
MachineLibrary_TransferFileSection.attributes={MachineLibrary_TransferFileSection_transferSeq, MachineLibrary_TransferFileSection_transferSection, MachineLibrary_TransferFileSection_transferFile}

# MachineLibrary_PlainMoveEntrySend class attributes and methods
MachineLibrary_PlainMoveEntrySend_plainmoveSeq: Property = Property(name="plainmoveSeq", type=IntegerType)
MachineLibrary_PlainMoveEntrySend_plainmoveEntry: Property = Property(name="plainmoveEntry", type=StringType)
MachineLibrary_PlainMoveEntrySend_plainmoveSend: Property = Property(name="plainmoveSend", type=StringType)
MachineLibrary_PlainMoveEntrySend.attributes={MachineLibrary_PlainMoveEntrySend_plainmoveEntry, MachineLibrary_PlainMoveEntrySend_plainmoveSeq, MachineLibrary_PlainMoveEntrySend_plainmoveSend}

# MachineLibrary_RobotWinCCToRobot class attributes and methods
MachineLibrary_RobotWinCCToRobot_robotwincctorobotFrom_X: Property = Property(name="robotwincctorobotFrom_X", type=StringType)
MachineLibrary_RobotWinCCToRobot_robotwincctorobotTo_X: Property = Property(name="robotwincctorobotTo_X", type=StringType)
MachineLibrary_RobotWinCCToRobot_robotwincctorobootType_X: Property = Property(name="robotwincctorobootType_X", type=StringType)
MachineLibrary_RobotWinCCToRobot_robotwincctorobootSeq_X: Property = Property(name="robotwincctorobootSeq_X", type=IntegerType)
MachineLibrary_RobotWinCCToRobot.attributes={MachineLibrary_RobotWinCCToRobot_robotwincctorobotFrom_X, MachineLibrary_RobotWinCCToRobot_robotwincctorobotTo_X, MachineLibrary_RobotWinCCToRobot_robotwincctorobootSeq_X, MachineLibrary_RobotWinCCToRobot_robotwincctorobootType_X}

# MachineLibrary_RobotVarToBusyCodes class attributes and methods

# MachineLibrary_RobotConfSendOrders class attributes and methods

# MachineLibrary_RobotWinCCToRobots class attributes and methods

# MachineLibrary_RobotToWinccs class attributes and methods

# MachineLibrary_RobotWarningONDelete class attributes and methods
MachineLibrary_RobotWarningONDelete_robotErrBitWhenConfirmationIsNeededFor_Robot: Property = Property(name="robotErrBitWhenConfirmationIsNeededFor_Robot", type=IntegerType)
MachineLibrary_RobotWarningONDelete_robotErrBitWhenConfirmationIsNeededFor_PM: Property = Property(name="robotErrBitWhenConfirmationIsNeededFor_PM", type=IntegerType)
MachineLibrary_RobotWarningONDelete_robotExtraPos_1: Property = Property(name="robotExtraPos_1", type=StringType)
MachineLibrary_RobotWarningONDelete_robotExtraUnit_2: Property = Property(name="robotExtraUnit_2", type=StringType)
MachineLibrary_RobotWarningONDelete.attributes={MachineLibrary_RobotWarningONDelete_robotExtraPos_1, MachineLibrary_RobotWarningONDelete_robotErrBitWhenConfirmationIsNeededFor_PM, MachineLibrary_RobotWarningONDelete_robotErrBitWhenConfirmationIsNeededFor_Robot, MachineLibrary_RobotWarningONDelete_robotExtraUnit_2}

# MachineLibrary_RobotVarToErrorbits class attributes and methods

# MachineLibrary_RobotVarToBusycode class attributes and methods
MachineLibrary_RobotVarToBusycode_robotvartobusycodeVar_X: Property = Property(name="robotvartobusycodeVar_X", type=StringType)
MachineLibrary_RobotVarToBusycode_robotvartobusycodeUnit_X: Property = Property(name="robotvartobusycodeUnit_X", type=IntegerType)
MachineLibrary_RobotVarToBusycode_robotvartobusycodeBit_X: Property = Property(name="robotvartobusycodeBit_X", type=IntegerType)
MachineLibrary_RobotVarToBusycode_robotvartobusycodeType_X: Property = Property(name="robotvartobusycodeType_X", type=StringType)
MachineLibrary_RobotVarToBusycode_robotvartobusycodeSeq_X: Property = Property(name="robotvartobusycodeSeq_X", type=IntegerType)
MachineLibrary_RobotVarToBusycode.attributes={MachineLibrary_RobotVarToBusycode_robotvartobusycodeBit_X, MachineLibrary_RobotVarToBusycode_robotvartobusycodeSeq_X, MachineLibrary_RobotVarToBusycode_robotvartobusycodeVar_X, MachineLibrary_RobotVarToBusycode_robotvartobusycodeType_X, MachineLibrary_RobotVarToBusycode_robotvartobusycodeUnit_X}

# MachineLibrary_RobotConfSendOrder class attributes and methods
MachineLibrary_RobotConfSendOrder_robotconfsendorderVar_X: Property = Property(name="robotconfsendorderVar_X", type=StringType)
MachineLibrary_RobotConfSendOrder_robotconfsendorderFrom_X: Property = Property(name="robotconfsendorderFrom_X", type=StringType)
MachineLibrary_RobotConfSendOrder_robotconfsendorderType_X: Property = Property(name="robotconfsendorderType_X", type=StringType)
MachineLibrary_RobotConfSendOrder_robotconfsendorderSeq_X: Property = Property(name="robotconfsendorderSeq_X", type=IntegerType)
MachineLibrary_RobotConfSendOrder.attributes={MachineLibrary_RobotConfSendOrder_robotconfsendorderVar_X, MachineLibrary_RobotConfSendOrder_robotconfsendorderFrom_X, MachineLibrary_RobotConfSendOrder_robotconfsendorderSeq_X, MachineLibrary_RobotConfSendOrder_robotconfsendorderType_X}

# MachineLibrary_RobotToWinCC class attributes and methods
MachineLibrary_RobotToWinCC_robotToWinccFrom_X: Property = Property(name="robotToWinccFrom_X", type=StringType)
MachineLibrary_RobotToWinCC_robotToWinccTo_X: Property = Property(name="robotToWinccTo_X", type=StringType)
MachineLibrary_RobotToWinCC_robotToWinccType_X: Property = Property(name="robotToWinccType_X", type=StringType)
MachineLibrary_RobotToWinCC_robotToWinccSeq_X: Property = Property(name="robotToWinccSeq_X", type=IntegerType)
MachineLibrary_RobotToWinCC.attributes={MachineLibrary_RobotToWinCC_robotToWinccSeq_X, MachineLibrary_RobotToWinCC_robotToWinccTo_X, MachineLibrary_RobotToWinCC_robotToWinccFrom_X, MachineLibrary_RobotToWinCC_robotToWinccType_X}

# MachineLibrary_RobotVarToErrorbit class attributes and methods
MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitVar_X: Property = Property(name="robotvartoerrorbitVar_X", type=StringType)
MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitBit_X: Property = Property(name="robotvartoerrorbitBit_X", type=IntegerType)
MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitInv_X: Property = Property(name="robotvartoerrorbitInv_X", type=IntegerType)
MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitType_X: Property = Property(name="robotvartoerrorbitType_X", type=StringType)
MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitSeq_X: Property = Property(name="robotvartoerrorbitSeq_X", type=IntegerType)
MachineLibrary_RobotVarToErrorbit.attributes={MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitBit_X, MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitSeq_X, MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitVar_X, MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitType_X, MachineLibrary_RobotVarToErrorbit_robotvartoerrorbitInv_X}

# Relationships
nodeConfig5: BinaryAssociation = BinaryAssociation(
    name="nodeConfig5",
    ends={
        Property(name="MachineLibrary_NodeConfig", type=MachineLibrary_LabMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LabMachine6", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
linkConfig7: BinaryAssociation = BinaryAssociation(
    name="linkConfig7",
    ends={
        Property(name="MachineLibrary_LinkConfig", type=MachineLibrary_LabMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LabMachine8", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labMachines0: BinaryAssociation = BinaryAssociation(
    name="labMachines0",
    ends={
        Property(name="MachineLibrary_LabMachines", type=MachineLibrary_PMMachineLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_PMMachineLibrary", type=MachineLibrary_LabMachines, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
labMachine1: BinaryAssociation = BinaryAssociation(
    name="labMachine1",
    ends={
        Property(name="MachineLibrary_LabMachine", type=MachineLibrary_LabMachines, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LabMachines2", type=MachineLibrary_LabMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links3: BinaryAssociation = BinaryAssociation(
    name="links3",
    ends={
        Property(name="MachineLibrary_Link2", type=MachineLibrary_LabMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LabMachine4", type=MachineLibrary_Link2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
winCCLnk9: BinaryAssociation = BinaryAssociation(
    name="winCCLnk9",
    ends={
        Property(name="MachineLibrary_WinCCLnk", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig10", type=MachineLibrary_WinCCLnk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tcpIP11: BinaryAssociation = BinaryAssociation(
    name="tcpIP11",
    ends={
        Property(name="MachineLibrary_TCPIP_Link", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig12", type=MachineLibrary_TCPIP_Link, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serial13: BinaryAssociation = BinaryAssociation(
    name="serial13",
    ends={
        Property(name="MachineLibrary_Serial_Link", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig14", type=MachineLibrary_Serial_Link, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileTransfer15: BinaryAssociation = BinaryAssociation(
    name="fileTransfer15",
    ends={
        Property(name="MachineLibrary_FileTransfer_Link", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig16", type=MachineLibrary_FileTransfer_Link, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
compac17: BinaryAssociation = BinaryAssociation(
    name="compac17",
    ends={
        Property(name="MachineLibrary_Compac_Link", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig18", type=MachineLibrary_Compac_Link, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ibmWebSphereMQ19: BinaryAssociation = BinaryAssociation(
    name="ibmWebSphereMQ19",
    ends={
        Property(name="MachineLibrary_IBMWebsphereMQ", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig20", type=MachineLibrary_IBMWebsphereMQ, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dpBase21: BinaryAssociation = BinaryAssociation(
    name="dpBase21",
    ends={
        Property(name="MachineLibrary_DPbase_Link", type=MachineLibrary_LinkConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_LinkConfig22", type=MachineLibrary_DPbase_Link, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dpBaseNode23: BinaryAssociation = BinaryAssociation(
    name="dpBaseNode23",
    ends={
        Property(name="MachineLibrary_DPbase_Node", type=MachineLibrary_DPbase_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_DPbase_Link24", type=MachineLibrary_DPbase_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wincc2WinCC47: BinaryAssociation = BinaryAssociation(
    name="wincc2WinCC47",
    ends={
        Property(name="MachineLibrary_NodeGeneralSpecial48", type=MachineLibrary_NodeGeneral_WinCC2WinCC, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="MachineLibrary_NodeGeneral_WinCC2WinCC", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1))
    }
)
accuPycDensityMeter49: BinaryAssociation = BinaryAssociation(
    name="accuPycDensityMeter49",
    ends={
        Property(name="MachineLibrary_NodeGeneral_AccuPycMeter", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneralSpecial50", type=MachineLibrary_NodeGeneral_AccuPycMeter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
units25: BinaryAssociation = BinaryAssociation(
    name="units25",
    ends={
        Property(name="MachineLibrary_Units", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig26", type=MachineLibrary_Units, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands27: BinaryAssociation = BinaryAssociation(
    name="commands27",
    ends={
        Property(name="MachineLibrary_Commands", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig28", type=MachineLibrary_Commands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
programs29: BinaryAssociation = BinaryAssociation(
    name="programs29",
    ends={
        Property(name="MachineLibrary_NodePrograms", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig30", type=MachineLibrary_NodePrograms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters31: BinaryAssociation = BinaryAssociation(
    name="parameters31",
    ends={
        Property(name="MachineLibrary_Parameters", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig32", type=MachineLibrary_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
communcationdata33: BinaryAssociation = BinaryAssociation(
    name="communcationdata33",
    ends={
        Property(name="MachineLibrary_CommunicationData", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig34", type=MachineLibrary_CommunicationData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specialConfiguration35: BinaryAssociation = BinaryAssociation(
    name="specialConfiguration35",
    ends={
        Property(name="MachineLibrary_NodeSpecialConfiguration", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig36", type=MachineLibrary_NodeSpecialConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeGeneral37: BinaryAssociation = BinaryAssociation(
    name="nodeGeneral37",
    ends={
        Property(name="MachineLibrary_NodeGeneral", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig38", type=MachineLibrary_NodeGeneral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodeGeneralSpecial39: BinaryAssociation = BinaryAssociation(
    name="nodeGeneralSpecial39",
    ends={
        Property(name="MachineLibrary_NodeGeneralSpecial", type=MachineLibrary_NodeConfig, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeConfig40", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terminal41: BinaryAssociation = BinaryAssociation(
    name="terminal41",
    ends={
        Property(name="MachineLibrary_NodeGeneral_Terminal", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneralSpecial42", type=MachineLibrary_NodeGeneral_Terminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pm2PM43: BinaryAssociation = BinaryAssociation(
    name="pm2PM43",
    ends={
        Property(name="MachineLibrary_NodeGeneral_PM2PM", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneralSpecial44", type=MachineLibrary_NodeGeneral_PM2PM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remotePM45: BinaryAssociation = BinaryAssociation(
    name="remotePM45",
    ends={
        Property(name="MachineLibrary_NodeGeneral_RemotePM", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneralSpecial46", type=MachineLibrary_NodeGeneral_RemotePM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rigakuXRF51: BinaryAssociation = BinaryAssociation(
    name="rigakuXRF51",
    ends={
        Property(name="MachineLibrary_NodeGeneral_RigakuXRF", type=MachineLibrary_NodeGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneralSpecial52", type=MachineLibrary_NodeGeneral_RigakuXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
addTag53: BinaryAssociation = BinaryAssociation(
    name="addTag53",
    ends={
        Property(name="MachineLibrary_WinCCAddTag", type=MachineLibrary_NodeGeneral_WinCC2WinCC, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeGeneral_WinCC2WinCC54", type=MachineLibrary_WinCCAddTag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions55: BinaryAssociation = BinaryAssociation(
    name="positions55",
    ends={
        Property(name="MachineLibrary_Positions", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units56", type=MachineLibrary_Positions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statusBits57: BinaryAssociation = BinaryAssociation(
    name="statusBits57",
    ends={
        Property(name="MachineLibrary_StausBits", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units58", type=MachineLibrary_StausBits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plctopmmatrix59: BinaryAssociation = BinaryAssociation(
    name="plctopmmatrix59",
    ends={
        Property(name="MachineLibrary_PLCtoPmMatrix", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units60", type=MachineLibrary_PLCtoPmMatrix, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
programs61: BinaryAssociation = BinaryAssociation(
    name="programs61",
    ends={
        Property(name="MachineLibrary_UnitPrograms", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units62", type=MachineLibrary_UnitPrograms, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
buttons63: BinaryAssociation = BinaryAssociation(
    name="buttons63",
    ends={
        Property(name="MachineLibrary_Buttons", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units64", type=MachineLibrary_Buttons, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitGeneral65: BinaryAssociation = BinaryAssociation(
    name="unitGeneral65",
    ends={
        Property(name="MachineLibrary_UnitGeneral", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units66", type=MachineLibrary_UnitGeneral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitGeneralSpecial67: BinaryAssociation = BinaryAssociation(
    name="unitGeneralSpecial67",
    ends={
        Property(name="MachineLibrary_UnitGeneralSpecial", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units68", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitSpecialConfiguration69: BinaryAssociation = BinaryAssociation(
    name="unitSpecialConfiguration69",
    ends={
        Property(name="MachineLibrary_UnitSpecialConfiguration", type=MachineLibrary_Units, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Units70", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unitGeneralParameter71: BinaryAssociation = BinaryAssociation(
    name="unitGeneralParameter71",
    ends={
        Property(name="MachineLibrary_UnitGeneralParameters", type=MachineLibrary_UnitGeneral, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneral72", type=MachineLibrary_UnitGeneralParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminal73: BinaryAssociation = BinaryAssociation(
    name="terminal73",
    ends={
        Property(name="MachineLibrary_UnitGeneral_Terminal", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial74", type=MachineLibrary_UnitGeneral_Terminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hostPC75: BinaryAssociation = BinaryAssociation(
    name="hostPC75",
    ends={
        Property(name="MachineLibrary_UnitGeneral_HostPC", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial76", type=MachineLibrary_UnitGeneral_HostPC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remote77: BinaryAssociation = BinaryAssociation(
    name="remote77",
    ends={
        Property(name="MachineLibrary_UnitGeneral_Remote", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial78", type=MachineLibrary_UnitGeneral_Remote, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pm2pm79: BinaryAssociation = BinaryAssociation(
    name="pm2pm79",
    ends={
        Property(name="MachineLibrary_UnitGeneral_PM2PM", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial80", type=MachineLibrary_UnitGeneral_PM2PM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accPycMeter81: BinaryAssociation = BinaryAssociation(
    name="accPycMeter81",
    ends={
        Property(name="MachineLibrary_UnitGeneral_AccPyc", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial82", type=MachineLibrary_UnitGeneral_AccPyc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superQ83: BinaryAssociation = BinaryAssociation(
    name="superQ83",
    ends={
        Property(name="MachineLibrary_UnitGeneral_SuperQ", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial84", type=MachineLibrary_UnitGeneral_SuperQ, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rigakuXRF85: BinaryAssociation = BinaryAssociation(
    name="rigakuXRF85",
    ends={
        Property(name="MachineLibrary_UnitGeneral_RigakuXRF", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial86", type=MachineLibrary_UnitGeneral_RigakuXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scanner87: BinaryAssociation = BinaryAssociation(
    name="scanner87",
    ends={
        Property(name="MachineLibrary_UnitGeneral_Scanner", type=MachineLibrary_UnitGeneralSpecial, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitGeneralSpecial88", type=MachineLibrary_UnitGeneral_Scanner, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
errorMessage_OBLFOES113: BinaryAssociation = BinaryAssociation(
    name="errorMessage_OBLFOES113",
    ends={
        Property(name="MachineLibrary_ErrorMessage_OBLFOES", type=MachineLibrary_UnitConfig_OBLF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_OBLF_OES114", type=MachineLibrary_ErrorMessage_OBLFOES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terminal_Config89: BinaryAssociation = BinaryAssociation(
    name="terminal_Config89",
    ends={
        Property(name="MachineLibrary_UnitConfig_Terminal", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration90", type=MachineLibrary_UnitConfig_Terminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
oblfOES_Config91: BinaryAssociation = BinaryAssociation(
    name="oblfOES_Config91",
    ends={
        Property(name="MachineLibrary_UnitConfig_OBLF_OES", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration92", type=MachineLibrary_UnitConfig_OBLF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superQXRF_Config93: BinaryAssociation = BinaryAssociation(
    name="superQXRF_Config93",
    ends={
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration94", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arlXRF_OES_Config95: BinaryAssociation = BinaryAssociation(
    name="arlXRF_OES_Config95",
    ends={
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration96", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
host_Config97: BinaryAssociation = BinaryAssociation(
    name="host_Config97",
    ends={
        Property(name="MachineLibrary_UnitConfig_Host", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration98", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accuPycMeter_History99: BinaryAssociation = BinaryAssociation(
    name="accuPycMeter_History99",
    ends={
        Property(name="MachineLibrary_History_AccuPycMeter", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration100", type=MachineLibrary_History_AccuPycMeter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scanner_SepByComma101: BinaryAssociation = BinaryAssociation(
    name="scanner_SepByComma101",
    ends={
        Property(name="MachineLibrary_SepByComma_Scanner", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration102", type=MachineLibrary_SepByComma_Scanner, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pm2PM_checkAddSID103: BinaryAssociation = BinaryAssociation(
    name="pm2PM_checkAddSID103",
    ends={
        Property(name="MachineLibrary_CheckAddSID_PM2PM", type=MachineLibrary_UnitSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitSpecialConfiguration104", type=MachineLibrary_CheckAddSID_PM2PM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
translate_terminal105: BinaryAssociation = BinaryAssociation(
    name="translate_terminal105",
    ends={
        Property(name="MachineLibrary_Translate_Terminal", type=MachineLibrary_UnitConfig_Terminal, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Terminal106", type=MachineLibrary_Translate_Terminal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputRequest_OBLFOES107: BinaryAssociation = BinaryAssociation(
    name="outputRequest_OBLFOES107",
    ends={
        Property(name="MachineLibrary_OutputRequest_OBLFOES", type=MachineLibrary_UnitConfig_OBLF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_OBLF_OES108", type=MachineLibrary_OutputRequest_OBLFOES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testRequest_OBLFOES109: BinaryAssociation = BinaryAssociation(
    name="testRequest_OBLFOES109",
    ends={
        Property(name="MachineLibrary_TestRequest_OBLFOES", type=MachineLibrary_UnitConfig_OBLF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_OBLF_OES110", type=MachineLibrary_TestRequest_OBLFOES, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
recalRequest_OBLFOES111: BinaryAssociation = BinaryAssociation(
    name="recalRequest_OBLFOES111",
    ends={
        Property(name="MachineLibrary_RecalRequest_OBLFOES", type=MachineLibrary_UnitConfig_OBLF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_OBLF_OES112", type=MachineLibrary_RecalRequest_OBLFOES, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ws_Update_Host149: BinaryAssociation = BinaryAssociation(
    name="ws_Update_Host149",
    ends={
        Property(name="MachineLibrary_WS_Update_Host", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Host150", type=MachineLibrary_WS_Update_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moved_Host151: BinaryAssociation = BinaryAssociation(
    name="moved_Host151",
    ends={
        Property(name="MachineLibrary_Moved_Host", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Host152", type=MachineLibrary_Moved_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generalParameter_SuperQXRF115: BinaryAssociation = BinaryAssociation(
    name="generalParameter_SuperQXRF115",
    ends={
        Property(name="MachineLibrary_GeneralParameter_SuperQXRF", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF116", type=MachineLibrary_GeneralParameter_SuperQXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
controlSamples_SuperQXRF117: BinaryAssociation = BinaryAssociation(
    name="controlSamples_SuperQXRF117",
    ends={
        Property(name="MachineLibrary_ControlSamples_SuperQXRF", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF118", type=MachineLibrary_ControlSamples_SuperQXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
communication_SuperQXRF119: BinaryAssociation = BinaryAssociation(
    name="communication_SuperQXRF119",
    ends={
        Property(name="MachineLibrary_Communication_SuperQXRF", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF120", type=MachineLibrary_Communication_SuperQXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checkSampleRunTime_SuperQXRF121: BinaryAssociation = BinaryAssociation(
    name="checkSampleRunTime_SuperQXRF121",
    ends={
        Property(name="MachineLibrary_CheckSampleRunTime_SuperQXRF", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF122", type=MachineLibrary_CheckSampleRunTime_SuperQXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checkSample_OLFXRF123: BinaryAssociation = BinaryAssociation(
    name="checkSample_OLFXRF123",
    ends={
        Property(name="MachineLibrary_CheckSample_SuperQXRF", type=MachineLibrary_UnitConfig_SuperQ_XRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_SuperQ_XRF124", type=MachineLibrary_CheckSample_SuperQXRF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checkFilling_ARL_XRF_OES125: BinaryAssociation = BinaryAssociation(
    name="checkFilling_ARL_XRF_OES125",
    ends={
        Property(name="MachineLibrary_CheckFilling_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES126", type=MachineLibrary_CheckFilling_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
executeFiling_ARL_XRF_OES127: BinaryAssociation = BinaryAssociation(
    name="executeFiling_ARL_XRF_OES127",
    ends={
        Property(name="MachineLibrary_ExecuteFiling_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES128", type=MachineLibrary_ExecuteFiling_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checkReqPrepUnit_ARL_XRF_OES129: BinaryAssociation = BinaryAssociation(
    name="checkReqPrepUnit_ARL_XRF_OES129",
    ends={
        Property(name="MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES130", type=MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exePrepUnit_ARL_XRF_OES131: BinaryAssociation = BinaryAssociation(
    name="exePrepUnit_ARL_XRF_OES131",
    ends={
        Property(name="MachineLibrary_ExePrepUnit_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES132", type=MachineLibrary_ExePrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checkAskPrepUnit_ARL_XRF_OES133: BinaryAssociation = BinaryAssociation(
    name="checkAskPrepUnit_ARL_XRF_OES133",
    ends={
        Property(name="MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES134", type=MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exeAskPrepUnit_ARL_XRF_OES135: BinaryAssociation = BinaryAssociation(
    name="exeAskPrepUnit_ARL_XRF_OES135",
    ends={
        Property(name="MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES136", type=MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
disableSCT_ARL_XRF_OES137: BinaryAssociation = BinaryAssociation(
    name="disableSCT_ARL_XRF_OES137",
    ends={
        Property(name="MachineLibrary_DisableSCT_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES138", type=MachineLibrary_DisableSCT_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
settings_ARL_XRF_OES139: BinaryAssociation = BinaryAssociation(
    name="settings_ARL_XRF_OES139",
    ends={
        Property(name="MachineLibrary_Settings_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES140", type=MachineLibrary_Settings_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generalSetting_ARL_XRF_OES141: BinaryAssociation = BinaryAssociation(
    name="generalSetting_ARL_XRF_OES141",
    ends={
        Property(name="MachineLibrary_GeneralSetting_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES142", type=MachineLibrary_GeneralSetting_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps_Process_Finished_ARL_XRF_OES143: BinaryAssociation = BinaryAssociation(
    name="ps_Process_Finished_ARL_XRF_OES143",
    ends={
        Property(name="MachineLibrary_PS_Process_Finished_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES144", type=MachineLibrary_PS_Process_Finished_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
file_Sample_ARL_XRF_OES145: BinaryAssociation = BinaryAssociation(
    name="file_Sample_ARL_XRF_OES145",
    ends={
        Property(name="MachineLibrary_File_Sample_ARL_XRF_OES", type=MachineLibrary_UnitConfig_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_ARL_XRF_OES146", type=MachineLibrary_File_Sample_ARL_XRF_OES, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
report_Host147: BinaryAssociation = BinaryAssociation(
    name="report_Host147",
    ends={
        Property(name="MachineLibrary_Report_Host", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Host148", type=MachineLibrary_Report_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition172: BinaryAssociation = BinaryAssociation(
    name="condition172",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition174", type=MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
insert_Host153: BinaryAssociation = BinaryAssociation(
    name="insert_Host153",
    ends={
        Property(name="MachineLibrary_InsertRemove_Host", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Host154", type=MachineLibrary_InsertRemove_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
remove_Host155: BinaryAssociation = BinaryAssociation(
    name="remove_Host155",
    ends={
        Property(name="MachineLibrary_InsertRemove_Host157", type=MachineLibrary_UnitConfig_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitConfig_Host156", type=MachineLibrary_InsertRemove_Host, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition158: BinaryAssociation = BinaryAssociation(
    name="condition158",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition", type=MachineLibrary_OutputRequest_OBLFOES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_OutputRequest_OBLFOES159", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition160: BinaryAssociation = BinaryAssociation(
    name="condition160",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition162", type=MachineLibrary_TestRequest_OBLFOES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_TestRequest_OBLFOES161", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition163: BinaryAssociation = BinaryAssociation(
    name="condition163",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition165", type=MachineLibrary_RecalRequest_OBLFOES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RecalRequest_OBLFOES164", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition166: BinaryAssociation = BinaryAssociation(
    name="condition166",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition168", type=MachineLibrary_CheckFilling_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckFilling_ARL_XRF_OES167", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition169: BinaryAssociation = BinaryAssociation(
    name="condition169",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition171", type=MachineLibrary_ExecuteFiling_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_ExecuteFiling_ARL_XRF_OES170", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sampleTpyeParameters193: BinaryAssociation = BinaryAssociation(
    name="sampleTpyeParameters193",
    ends={
        Property(name="MachineLibrary_CheckSampleRunTimeParams_SuperQXRF", type=MachineLibrary_CheckSampleRunTime_SuperQXRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckSampleRunTime_SuperQXRF194", type=MachineLibrary_CheckSampleRunTimeParams_SuperQXRF, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition175: BinaryAssociation = BinaryAssociation(
    name="condition175",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition177", type=MachineLibrary_ExePrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_ExePrepUnit_ARL_XRF_OES176", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition178: BinaryAssociation = BinaryAssociation(
    name="condition178",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition180", type=MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition181: BinaryAssociation = BinaryAssociation(
    name="condition181",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition183", type=MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition184: BinaryAssociation = BinaryAssociation(
    name="condition184",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition186", type=MachineLibrary_DisableSCT_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_DisableSCT_ARL_XRF_OES185", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition187: BinaryAssociation = BinaryAssociation(
    name="condition187",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition189", type=MachineLibrary_Settings_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Settings_ARL_XRF_OES188", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition190: BinaryAssociation = BinaryAssociation(
    name="condition190",
    ends={
        Property(name="MachineLibrary_OES_XRF_Condition192", type=MachineLibrary_GeneralSetting_ARL_XRF_OES, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_GeneralSetting_ARL_XRF_OES191", type=MachineLibrary_OES_XRF_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkSampleConfig_SuperQXRF195: BinaryAssociation = BinaryAssociation(
    name="checkSampleConfig_SuperQXRF195",
    ends={
        Property(name="MachineLibrary_CheckSampleConfig_SuperQXRF", type=MachineLibrary_CheckSample_SuperQXRF, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckSample_SuperQXRF196", type=MachineLibrary_CheckSampleConfig_SuperQXRF, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
historyConfig_AccPyc197: BinaryAssociation = BinaryAssociation(
    name="historyConfig_AccPyc197",
    ends={
        Property(name="MachineLibrary_HistoryConfig_AccuPyc", type=MachineLibrary_History_AccuPycMeter, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_History_AccuPycMeter198", type=MachineLibrary_HistoryConfig_AccuPyc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry199: BinaryAssociation = BinaryAssociation(
    name="entry199",
    ends={
        Property(name="MachineLibrary_InsertRemove_Entry_Host", type=MachineLibrary_InsertRemove_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_InsertRemove_Host200", type=MachineLibrary_InsertRemove_Entry_Host, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type201: BinaryAssociation = BinaryAssociation(
    name="type201",
    ends={
        Property(name="MachineLibrary_InsertRemove_Types_Host", type=MachineLibrary_InsertRemove_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_InsertRemove_Host202", type=MachineLibrary_InsertRemove_Types_Host, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyword203: BinaryAssociation = BinaryAssociation(
    name="keyword203",
    ends={
        Property(name="MachineLibrary_InsertRemove_Keywords_Host", type=MachineLibrary_InsertRemove_Host, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_InsertRemove_Host204", type=MachineLibrary_InsertRemove_Keywords_Host, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field205: BinaryAssociation = BinaryAssociation(
    name="field205",
    ends={
        Property(name="MachineLibrary_SepByComma_Field_Scanner", type=MachineLibrary_SepByComma_Scanner, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_SepByComma_Scanner206", type=MachineLibrary_SepByComma_Field_Scanner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id207: BinaryAssociation = BinaryAssociation(
    name="id207",
    ends={
        Property(name="MachineLibrary_SepByComma_ID_Scanner", type=MachineLibrary_SepByComma_Scanner, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_SepByComma_Scanner208", type=MachineLibrary_SepByComma_ID_Scanner, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options209: BinaryAssociation = BinaryAssociation(
    name="options209",
    ends={
        Property(name="MachineLibrary_CheckAddSID_Values_PM2PM", type=MachineLibrary_CheckAddSID_PM2PM, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_CheckAddSID_PM2PM210", type=MachineLibrary_CheckAddSID_Values_PM2PM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
button211: BinaryAssociation = BinaryAssociation(
    name="button211",
    ends={
        Property(name="MachineLibrary_Button", type=MachineLibrary_Buttons, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Buttons212", type=MachineLibrary_Button, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
position213: BinaryAssociation = BinaryAssociation(
    name="position213",
    ends={
        Property(name="MachineLibrary_Position", type=MachineLibrary_Positions, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Positions214", type=MachineLibrary_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statusBit215: BinaryAssociation = BinaryAssociation(
    name="statusBit215",
    ends={
        Property(name="MachineLibrary_StatusBit", type=MachineLibrary_StausBits, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_StausBits216", type=MachineLibrary_StatusBit, multiplicity=Multiplicity(0, 16), is_composite=True)
    }
)
command217: BinaryAssociation = BinaryAssociation(
    name="command217",
    ends={
        Property(name="MachineLibrary_Command", type=MachineLibrary_Commands, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Commands218", type=MachineLibrary_Command, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program219: BinaryAssociation = BinaryAssociation(
    name="program219",
    ends={
        Property(name="MachineLibrary_NodeProgram", type=MachineLibrary_NodePrograms, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodePrograms220", type=MachineLibrary_NodeProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unitProgram221: BinaryAssociation = BinaryAssociation(
    name="unitProgram221",
    ends={
        Property(name="MachineLibrary_UnitProgram", type=MachineLibrary_UnitPrograms, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitPrograms222", type=MachineLibrary_UnitProgram, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters223: BinaryAssociation = BinaryAssociation(
    name="parameters223",
    ends={
        Property(name="MachineLibrary_UnitProgParameters", type=MachineLibrary_UnitProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_UnitProgram224", type=MachineLibrary_UnitProgParameters, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter225: BinaryAssociation = BinaryAssociation(
    name="parameter225",
    ends={
        Property(name="MachineLibrary_Parameter", type=MachineLibrary_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Parameters226", type=MachineLibrary_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paramPrint227: BinaryAssociation = BinaryAssociation(
    name="paramPrint227",
    ends={
        Property(name="MachineLibrary_ParamPrint", type=MachineLibrary_NodeSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeSpecialConfiguration228", type=MachineLibrary_ParamPrint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transfer229: BinaryAssociation = BinaryAssociation(
    name="transfer229",
    ends={
        Property(name="MachineLibrary_Transfer", type=MachineLibrary_NodeSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeSpecialConfiguration230", type=MachineLibrary_Transfer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
plainMove231: BinaryAssociation = BinaryAssociation(
    name="plainMove231",
    ends={
        Property(name="MachineLibrary_PlainMove", type=MachineLibrary_NodeSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeSpecialConfiguration232", type=MachineLibrary_PlainMove, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotConfiguration233: BinaryAssociation = BinaryAssociation(
    name="robotConfiguration233",
    ends={
        Property(name="MachineLibrary_RobotConfiguration", type=MachineLibrary_NodeSpecialConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_NodeSpecialConfiguration234", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transferFileSection235: BinaryAssociation = BinaryAssociation(
    name="transferFileSection235",
    ends={
        Property(name="MachineLibrary_TransferFileSection", type=MachineLibrary_Transfer, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_Transfer236", type=MachineLibrary_TransferFileSection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plainmoveEntrySend237: BinaryAssociation = BinaryAssociation(
    name="plainmoveEntrySend237",
    ends={
        Property(name="MachineLibrary_PlainMoveEntrySend", type=MachineLibrary_PlainMove, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_PlainMove238", type=MachineLibrary_PlainMoveEntrySend, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robotWinCCToRobot255: BinaryAssociation = BinaryAssociation(
    name="robotWinCCToRobot255",
    ends={
        Property(name="MachineLibrary_RobotWinCCToRobot", type=MachineLibrary_RobotWinCCToRobots, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotWinCCToRobots256", type=MachineLibrary_RobotWinCCToRobot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robotVarToBusyCodes239: BinaryAssociation = BinaryAssociation(
    name="robotVarToBusyCodes239",
    ends={
        Property(name="MachineLibrary_RobotVarToBusyCodes", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration240", type=MachineLibrary_RobotVarToBusyCodes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotConfSendOrders241: BinaryAssociation = BinaryAssociation(
    name="robotConfSendOrders241",
    ends={
        Property(name="MachineLibrary_RobotConfSendOrders", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration242", type=MachineLibrary_RobotConfSendOrders, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotWinCCToRobots243: BinaryAssociation = BinaryAssociation(
    name="robotWinCCToRobots243",
    ends={
        Property(name="MachineLibrary_RobotWinCCToRobots", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration244", type=MachineLibrary_RobotWinCCToRobots, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotToWinCCs245: BinaryAssociation = BinaryAssociation(
    name="robotToWinCCs245",
    ends={
        Property(name="MachineLibrary_RobotToWinccs", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration246", type=MachineLibrary_RobotToWinccs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotWarningONDelete247: BinaryAssociation = BinaryAssociation(
    name="robotWarningONDelete247",
    ends={
        Property(name="MachineLibrary_RobotWarningONDelete", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration248", type=MachineLibrary_RobotWarningONDelete, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotVarToErrorBits249: BinaryAssociation = BinaryAssociation(
    name="robotVarToErrorBits249",
    ends={
        Property(name="MachineLibrary_RobotVarToErrorbits", type=MachineLibrary_RobotConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfiguration250", type=MachineLibrary_RobotVarToErrorbits, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
robotVarToBusycode251: BinaryAssociation = BinaryAssociation(
    name="robotVarToBusycode251",
    ends={
        Property(name="MachineLibrary_RobotVarToBusycode", type=MachineLibrary_RobotVarToBusyCodes, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotVarToBusyCodes252", type=MachineLibrary_RobotVarToBusycode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robotConfSendOrder253: BinaryAssociation = BinaryAssociation(
    name="robotConfSendOrder253",
    ends={
        Property(name="MachineLibrary_RobotConfSendOrder", type=MachineLibrary_RobotConfSendOrders, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotConfSendOrders254", type=MachineLibrary_RobotConfSendOrder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robotToWinCC257: BinaryAssociation = BinaryAssociation(
    name="robotToWinCC257",
    ends={
        Property(name="MachineLibrary_RobotToWinCC", type=MachineLibrary_RobotToWinccs, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotToWinccs258", type=MachineLibrary_RobotToWinCC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robotVarToErrorbit259: BinaryAssociation = BinaryAssociation(
    name="robotVarToErrorbit259",
    ends={
        Property(name="MachineLibrary_RobotVarToErrorbit", type=MachineLibrary_RobotVarToErrorbits, multiplicity=Multiplicity(1, 1)),
        Property(name="MachineLibrary_RobotVarToErrorbits260", type=MachineLibrary_RobotVarToErrorbit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="MachineLibrary",
    types={MachineLibrary_LinkConfig, MachineLibrary_PMMachineLibrary, MachineLibrary_LabMachines, MachineLibrary_LabMachine, MachineLibrary_Link2, MachineLibrary_NodeConfig, MachineLibrary_WinCCLnk, MachineLibrary_TCPIP_Link, MachineLibrary_Serial_Link, MachineLibrary_FileTransfer_Link, MachineLibrary_Compac_Link, MachineLibrary_IBMWebsphereMQ, MachineLibrary_DPbase_Link, MachineLibrary_DPbase_Node, MachineLibrary_NodeGeneral_AccuPycMeter, MachineLibrary_NodeGeneral_RigakuXRF, MachineLibrary_Units, MachineLibrary_Commands, MachineLibrary_NodePrograms, MachineLibrary_Parameters, MachineLibrary_CommunicationData, MachineLibrary_NodeSpecialConfiguration, MachineLibrary_NodeGeneral, MachineLibrary_NodeGeneralSpecial, MachineLibrary_NodeGeneral_Terminal, MachineLibrary_NodeGeneral_PM2PM, MachineLibrary_NodeGeneral_RemotePM, MachineLibrary_NodeGeneral_WinCC2WinCC, MachineLibrary_WinCCAddTag, MachineLibrary_Positions, MachineLibrary_StausBits, MachineLibrary_PLCtoPmMatrix, MachineLibrary_UnitPrograms, MachineLibrary_Buttons, MachineLibrary_UnitGeneral, MachineLibrary_UnitGeneralSpecial, MachineLibrary_UnitSpecialConfiguration, MachineLibrary_UnitGeneralParameters, MachineLibrary_UnitGeneral_Terminal, MachineLibrary_UnitGeneral_HostPC, MachineLibrary_UnitGeneral_Remote, MachineLibrary_UnitGeneral_PM2PM, MachineLibrary_UnitGeneral_AccPyc, MachineLibrary_UnitGeneral_SuperQ, MachineLibrary_UnitGeneral_RigakuXRF, MachineLibrary_UnitGeneral_Scanner, MachineLibrary_ErrorMessage_OBLFOES, MachineLibrary_GeneralParameter_SuperQXRF, MachineLibrary_UnitConfig_Terminal, MachineLibrary_UnitConfig_OBLF_OES, MachineLibrary_UnitConfig_SuperQ_XRF, MachineLibrary_UnitConfig_ARL_XRF_OES, MachineLibrary_UnitConfig_Host, MachineLibrary_History_AccuPycMeter, MachineLibrary_SepByComma_Scanner, MachineLibrary_CheckAddSID_PM2PM, MachineLibrary_Translate_Terminal, MachineLibrary_OutputRequest_OBLFOES, MachineLibrary_TestRequest_OBLFOES, MachineLibrary_RecalRequest_OBLFOES, MachineLibrary_Moved_Host, MachineLibrary_ControlSamples_SuperQXRF, MachineLibrary_Communication_SuperQXRF, MachineLibrary_CheckSampleRunTime_SuperQXRF, MachineLibrary_CheckSample_SuperQXRF, MachineLibrary_CheckFilling_ARL_XRF_OES, MachineLibrary_ExecuteFiling_ARL_XRF_OES, MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES, MachineLibrary_ExePrepUnit_ARL_XRF_OES, MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES, MachineLibrary_DisableSCT_ARL_XRF_OES, MachineLibrary_Settings_ARL_XRF_OES, MachineLibrary_GeneralSetting_ARL_XRF_OES, MachineLibrary_PS_Process_Finished_ARL_XRF_OES, MachineLibrary_File_Sample_ARL_XRF_OES, MachineLibrary_Report_Host, MachineLibrary_WS_Update_Host, MachineLibrary_InsertRemove_Host, MachineLibrary_OES_XRF_Condition, MachineLibrary_CheckSampleRunTimeParams_SuperQXRF, MachineLibrary_CheckSampleConfig_SuperQXRF, MachineLibrary_HistoryConfig_AccuPyc, MachineLibrary_Button, MachineLibrary_InsertRemove_Entry_Host, MachineLibrary_InsertRemove_Types_Host, MachineLibrary_InsertRemove_Keywords_Host, MachineLibrary_SepByComma_Field_Scanner, MachineLibrary_SepByComma_ID_Scanner, MachineLibrary_CheckAddSID_Values_PM2PM, MachineLibrary_Position, MachineLibrary_StatusBit, MachineLibrary_Command, MachineLibrary_NodeProgram, MachineLibrary_UnitProgram, MachineLibrary_UnitProgParameters, MachineLibrary_Parameter, MachineLibrary_ParamPrint, MachineLibrary_Transfer, MachineLibrary_PlainMove, MachineLibrary_RobotConfiguration, MachineLibrary_TransferFileSection, MachineLibrary_PlainMoveEntrySend, MachineLibrary_RobotWinCCToRobot, MachineLibrary_RobotVarToBusyCodes, MachineLibrary_RobotConfSendOrders, MachineLibrary_RobotWinCCToRobots, MachineLibrary_RobotToWinccs, MachineLibrary_RobotWarningONDelete, MachineLibrary_RobotVarToErrorbits, MachineLibrary_RobotVarToBusycode, MachineLibrary_RobotConfSendOrder, MachineLibrary_RobotToWinCC, MachineLibrary_RobotVarToErrorbit},
    associations={nodeConfig5, linkConfig7, labMachines0, labMachine1, links3, winCCLnk9, tcpIP11, serial13, fileTransfer15, compac17, ibmWebSphereMQ19, dpBase21, dpBaseNode23, wincc2WinCC47, accuPycDensityMeter49, units25, commands27, programs29, parameters31, communcationdata33, specialConfiguration35, nodeGeneral37, nodeGeneralSpecial39, terminal41, pm2PM43, remotePM45, rigakuXRF51, addTag53, positions55, statusBits57, plctopmmatrix59, programs61, buttons63, unitGeneral65, unitGeneralSpecial67, unitSpecialConfiguration69, unitGeneralParameter71, terminal73, hostPC75, remote77, pm2pm79, accPycMeter81, superQ83, rigakuXRF85, scanner87, errorMessage_OBLFOES113, terminal_Config89, oblfOES_Config91, superQXRF_Config93, arlXRF_OES_Config95, host_Config97, accuPycMeter_History99, scanner_SepByComma101, pm2PM_checkAddSID103, translate_terminal105, outputRequest_OBLFOES107, testRequest_OBLFOES109, recalRequest_OBLFOES111, ws_Update_Host149, moved_Host151, generalParameter_SuperQXRF115, controlSamples_SuperQXRF117, communication_SuperQXRF119, checkSampleRunTime_SuperQXRF121, checkSample_OLFXRF123, checkFilling_ARL_XRF_OES125, executeFiling_ARL_XRF_OES127, checkReqPrepUnit_ARL_XRF_OES129, exePrepUnit_ARL_XRF_OES131, checkAskPrepUnit_ARL_XRF_OES133, exeAskPrepUnit_ARL_XRF_OES135, disableSCT_ARL_XRF_OES137, settings_ARL_XRF_OES139, generalSetting_ARL_XRF_OES141, ps_Process_Finished_ARL_XRF_OES143, file_Sample_ARL_XRF_OES145, report_Host147, condition172, insert_Host153, remove_Host155, condition158, condition160, condition163, condition166, condition169, sampleTpyeParameters193, condition175, condition178, condition181, condition184, condition187, condition190, checkSampleConfig_SuperQXRF195, historyConfig_AccPyc197, entry199, type201, keyword203, field205, id207, options209, button211, position213, statusBit215, command217, program219, unitProgram221, parameters223, parameter225, paramPrint227, transfer229, plainMove231, robotConfiguration233, transferFileSection235, plainmoveEntrySend237, robotWinCCToRobot255, robotVarToBusyCodes239, robotConfSendOrders241, robotWinCCToRobots243, robotToWinCCs245, robotWarningONDelete247, robotVarToErrorBits249, robotVarToBusycode251, robotConfSendOrder253, robotToWinCC257, robotVarToErrorbit259},
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