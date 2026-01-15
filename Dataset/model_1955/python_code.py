from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class MachineLibrary_RobotVarToErrorbit:

    def __init__(self, robotvartoerrorbitVar_X: str, robotvartoerrorbitBit_X: int, robotvartoerrorbitInv_X: int, robotvartoerrorbitType_X: str, robotvartoerrorbitSeq_X: int, MachineLibrary_RobotVarToErrorbit: "MachineLibrary_RobotVarToErrorbits" = None):
        self.robotvartoerrorbitVar_X = robotvartoerrorbitVar_X
        self.robotvartoerrorbitBit_X = robotvartoerrorbitBit_X
        self.robotvartoerrorbitInv_X = robotvartoerrorbitInv_X
        self.robotvartoerrorbitType_X = robotvartoerrorbitType_X
        self.robotvartoerrorbitSeq_X = robotvartoerrorbitSeq_X
        self.MachineLibrary_RobotVarToErrorbit = MachineLibrary_RobotVarToErrorbit
        
    @property
    def robotvartoerrorbitBit_X(self) -> int:
        return self.__robotvartoerrorbitBit_X

    @robotvartoerrorbitBit_X.setter
    def robotvartoerrorbitBit_X(self, robotvartoerrorbitBit_X: int):
        self.__robotvartoerrorbitBit_X = robotvartoerrorbitBit_X

    @property
    def robotvartoerrorbitSeq_X(self) -> int:
        return self.__robotvartoerrorbitSeq_X

    @robotvartoerrorbitSeq_X.setter
    def robotvartoerrorbitSeq_X(self, robotvartoerrorbitSeq_X: int):
        self.__robotvartoerrorbitSeq_X = robotvartoerrorbitSeq_X

    @property
    def robotvartoerrorbitVar_X(self) -> str:
        return self.__robotvartoerrorbitVar_X

    @robotvartoerrorbitVar_X.setter
    def robotvartoerrorbitVar_X(self, robotvartoerrorbitVar_X: str):
        self.__robotvartoerrorbitVar_X = robotvartoerrorbitVar_X

    @property
    def robotvartoerrorbitType_X(self) -> str:
        return self.__robotvartoerrorbitType_X

    @robotvartoerrorbitType_X.setter
    def robotvartoerrorbitType_X(self, robotvartoerrorbitType_X: str):
        self.__robotvartoerrorbitType_X = robotvartoerrorbitType_X

    @property
    def robotvartoerrorbitInv_X(self) -> int:
        return self.__robotvartoerrorbitInv_X

    @robotvartoerrorbitInv_X.setter
    def robotvartoerrorbitInv_X(self, robotvartoerrorbitInv_X: int):
        self.__robotvartoerrorbitInv_X = robotvartoerrorbitInv_X

    @property
    def MachineLibrary_RobotVarToErrorbit(self):
        return self.__MachineLibrary_RobotVarToErrorbit

    @MachineLibrary_RobotVarToErrorbit.setter
    def MachineLibrary_RobotVarToErrorbit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotVarToErrorbit__MachineLibrary_RobotVarToErrorbit", None)
        self.__MachineLibrary_RobotVarToErrorbit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotVarToErrorbits260"):
                opp_val = getattr(old_value, "MachineLibrary_RobotVarToErrorbits260", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotVarToErrorbits260"):
                opp_val = getattr(value, "MachineLibrary_RobotVarToErrorbits260", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RobotVarToErrorbits260", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_RobotToWinCC:

    def __init__(self, robotToWinccFrom_X: str, robotToWinccTo_X: str, robotToWinccType_X: str, robotToWinccSeq_X: int, MachineLibrary_RobotToWinCC: "MachineLibrary_RobotToWinccs" = None):
        self.robotToWinccFrom_X = robotToWinccFrom_X
        self.robotToWinccTo_X = robotToWinccTo_X
        self.robotToWinccType_X = robotToWinccType_X
        self.robotToWinccSeq_X = robotToWinccSeq_X
        self.MachineLibrary_RobotToWinCC = MachineLibrary_RobotToWinCC
        
    @property
    def robotToWinccSeq_X(self) -> int:
        return self.__robotToWinccSeq_X

    @robotToWinccSeq_X.setter
    def robotToWinccSeq_X(self, robotToWinccSeq_X: int):
        self.__robotToWinccSeq_X = robotToWinccSeq_X

    @property
    def robotToWinccTo_X(self) -> str:
        return self.__robotToWinccTo_X

    @robotToWinccTo_X.setter
    def robotToWinccTo_X(self, robotToWinccTo_X: str):
        self.__robotToWinccTo_X = robotToWinccTo_X

    @property
    def robotToWinccFrom_X(self) -> str:
        return self.__robotToWinccFrom_X

    @robotToWinccFrom_X.setter
    def robotToWinccFrom_X(self, robotToWinccFrom_X: str):
        self.__robotToWinccFrom_X = robotToWinccFrom_X

    @property
    def robotToWinccType_X(self) -> str:
        return self.__robotToWinccType_X

    @robotToWinccType_X.setter
    def robotToWinccType_X(self, robotToWinccType_X: str):
        self.__robotToWinccType_X = robotToWinccType_X

    @property
    def MachineLibrary_RobotToWinCC(self):
        return self.__MachineLibrary_RobotToWinCC

    @MachineLibrary_RobotToWinCC.setter
    def MachineLibrary_RobotToWinCC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotToWinCC__MachineLibrary_RobotToWinCC", None)
        self.__MachineLibrary_RobotToWinCC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotToWinccs258"):
                opp_val = getattr(old_value, "MachineLibrary_RobotToWinccs258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotToWinccs258"):
                opp_val = getattr(value, "MachineLibrary_RobotToWinccs258", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RobotToWinccs258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_RobotConfSendOrder:

    def __init__(self, robotconfsendorderVar_X: str, robotconfsendorderFrom_X: str, robotconfsendorderType_X: str, robotconfsendorderSeq_X: int, MachineLibrary_RobotConfSendOrder: "MachineLibrary_RobotConfSendOrders" = None):
        self.robotconfsendorderVar_X = robotconfsendorderVar_X
        self.robotconfsendorderFrom_X = robotconfsendorderFrom_X
        self.robotconfsendorderType_X = robotconfsendorderType_X
        self.robotconfsendorderSeq_X = robotconfsendorderSeq_X
        self.MachineLibrary_RobotConfSendOrder = MachineLibrary_RobotConfSendOrder
        
    @property
    def robotconfsendorderVar_X(self) -> str:
        return self.__robotconfsendorderVar_X

    @robotconfsendorderVar_X.setter
    def robotconfsendorderVar_X(self, robotconfsendorderVar_X: str):
        self.__robotconfsendorderVar_X = robotconfsendorderVar_X

    @property
    def robotconfsendorderFrom_X(self) -> str:
        return self.__robotconfsendorderFrom_X

    @robotconfsendorderFrom_X.setter
    def robotconfsendorderFrom_X(self, robotconfsendorderFrom_X: str):
        self.__robotconfsendorderFrom_X = robotconfsendorderFrom_X

    @property
    def robotconfsendorderSeq_X(self) -> int:
        return self.__robotconfsendorderSeq_X

    @robotconfsendorderSeq_X.setter
    def robotconfsendorderSeq_X(self, robotconfsendorderSeq_X: int):
        self.__robotconfsendorderSeq_X = robotconfsendorderSeq_X

    @property
    def robotconfsendorderType_X(self) -> str:
        return self.__robotconfsendorderType_X

    @robotconfsendorderType_X.setter
    def robotconfsendorderType_X(self, robotconfsendorderType_X: str):
        self.__robotconfsendorderType_X = robotconfsendorderType_X

    @property
    def MachineLibrary_RobotConfSendOrder(self):
        return self.__MachineLibrary_RobotConfSendOrder

    @MachineLibrary_RobotConfSendOrder.setter
    def MachineLibrary_RobotConfSendOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfSendOrder__MachineLibrary_RobotConfSendOrder", None)
        self.__MachineLibrary_RobotConfSendOrder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotConfSendOrders254"):
                opp_val = getattr(old_value, "MachineLibrary_RobotConfSendOrders254", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotConfSendOrders254"):
                opp_val = getattr(value, "MachineLibrary_RobotConfSendOrders254", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RobotConfSendOrders254", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_RobotVarToBusycode:

    def __init__(self, robotvartobusycodeVar_X: str, robotvartobusycodeUnit_X: int, robotvartobusycodeBit_X: int, robotvartobusycodeType_X: str, robotvartobusycodeSeq_X: int, MachineLibrary_RobotVarToBusycode: "MachineLibrary_RobotVarToBusyCodes" = None):
        self.robotvartobusycodeVar_X = robotvartobusycodeVar_X
        self.robotvartobusycodeUnit_X = robotvartobusycodeUnit_X
        self.robotvartobusycodeBit_X = robotvartobusycodeBit_X
        self.robotvartobusycodeType_X = robotvartobusycodeType_X
        self.robotvartobusycodeSeq_X = robotvartobusycodeSeq_X
        self.MachineLibrary_RobotVarToBusycode = MachineLibrary_RobotVarToBusycode
        
    @property
    def robotvartobusycodeBit_X(self) -> int:
        return self.__robotvartobusycodeBit_X

    @robotvartobusycodeBit_X.setter
    def robotvartobusycodeBit_X(self, robotvartobusycodeBit_X: int):
        self.__robotvartobusycodeBit_X = robotvartobusycodeBit_X

    @property
    def robotvartobusycodeSeq_X(self) -> int:
        return self.__robotvartobusycodeSeq_X

    @robotvartobusycodeSeq_X.setter
    def robotvartobusycodeSeq_X(self, robotvartobusycodeSeq_X: int):
        self.__robotvartobusycodeSeq_X = robotvartobusycodeSeq_X

    @property
    def robotvartobusycodeVar_X(self) -> str:
        return self.__robotvartobusycodeVar_X

    @robotvartobusycodeVar_X.setter
    def robotvartobusycodeVar_X(self, robotvartobusycodeVar_X: str):
        self.__robotvartobusycodeVar_X = robotvartobusycodeVar_X

    @property
    def robotvartobusycodeType_X(self) -> str:
        return self.__robotvartobusycodeType_X

    @robotvartobusycodeType_X.setter
    def robotvartobusycodeType_X(self, robotvartobusycodeType_X: str):
        self.__robotvartobusycodeType_X = robotvartobusycodeType_X

    @property
    def robotvartobusycodeUnit_X(self) -> int:
        return self.__robotvartobusycodeUnit_X

    @robotvartobusycodeUnit_X.setter
    def robotvartobusycodeUnit_X(self, robotvartobusycodeUnit_X: int):
        self.__robotvartobusycodeUnit_X = robotvartobusycodeUnit_X

    @property
    def MachineLibrary_RobotVarToBusycode(self):
        return self.__MachineLibrary_RobotVarToBusycode

    @MachineLibrary_RobotVarToBusycode.setter
    def MachineLibrary_RobotVarToBusycode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotVarToBusycode__MachineLibrary_RobotVarToBusycode", None)
        self.__MachineLibrary_RobotVarToBusycode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotVarToBusyCodes252"):
                opp_val = getattr(old_value, "MachineLibrary_RobotVarToBusyCodes252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotVarToBusyCodes252"):
                opp_val = getattr(value, "MachineLibrary_RobotVarToBusyCodes252", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RobotVarToBusyCodes252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_RobotVarToErrorbits:

    pass
class MachineLibrary_RobotWarningONDelete:

    def __init__(self, robotErrBitWhenConfirmationIsNeededFor_Robot: int, robotErrBitWhenConfirmationIsNeededFor_PM: int, robotExtraPos_1: str, robotExtraUnit_2: str, MachineLibrary_RobotWarningONDelete: "MachineLibrary_RobotConfiguration" = None):
        self.robotErrBitWhenConfirmationIsNeededFor_Robot = robotErrBitWhenConfirmationIsNeededFor_Robot
        self.robotErrBitWhenConfirmationIsNeededFor_PM = robotErrBitWhenConfirmationIsNeededFor_PM
        self.robotExtraPos_1 = robotExtraPos_1
        self.robotExtraUnit_2 = robotExtraUnit_2
        self.MachineLibrary_RobotWarningONDelete = MachineLibrary_RobotWarningONDelete
        
    @property
    def robotExtraPos_1(self) -> str:
        return self.__robotExtraPos_1

    @robotExtraPos_1.setter
    def robotExtraPos_1(self, robotExtraPos_1: str):
        self.__robotExtraPos_1 = robotExtraPos_1

    @property
    def robotErrBitWhenConfirmationIsNeededFor_PM(self) -> int:
        return self.__robotErrBitWhenConfirmationIsNeededFor_PM

    @robotErrBitWhenConfirmationIsNeededFor_PM.setter
    def robotErrBitWhenConfirmationIsNeededFor_PM(self, robotErrBitWhenConfirmationIsNeededFor_PM: int):
        self.__robotErrBitWhenConfirmationIsNeededFor_PM = robotErrBitWhenConfirmationIsNeededFor_PM

    @property
    def robotErrBitWhenConfirmationIsNeededFor_Robot(self) -> int:
        return self.__robotErrBitWhenConfirmationIsNeededFor_Robot

    @robotErrBitWhenConfirmationIsNeededFor_Robot.setter
    def robotErrBitWhenConfirmationIsNeededFor_Robot(self, robotErrBitWhenConfirmationIsNeededFor_Robot: int):
        self.__robotErrBitWhenConfirmationIsNeededFor_Robot = robotErrBitWhenConfirmationIsNeededFor_Robot

    @property
    def robotExtraUnit_2(self) -> str:
        return self.__robotExtraUnit_2

    @robotExtraUnit_2.setter
    def robotExtraUnit_2(self, robotExtraUnit_2: str):
        self.__robotExtraUnit_2 = robotExtraUnit_2

    @property
    def MachineLibrary_RobotWarningONDelete(self):
        return self.__MachineLibrary_RobotWarningONDelete

    @MachineLibrary_RobotWarningONDelete.setter
    def MachineLibrary_RobotWarningONDelete(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotWarningONDelete__MachineLibrary_RobotWarningONDelete", None)
        self.__MachineLibrary_RobotWarningONDelete = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotConfiguration248"):
                opp_val = getattr(old_value, "MachineLibrary_RobotConfiguration248", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotConfiguration248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotConfiguration248"):
                opp_val = getattr(value, "MachineLibrary_RobotConfiguration248", None)
                setattr(value, "MachineLibrary_RobotConfiguration248", self)

class MachineLibrary_RobotToWinccs:

    pass
class MachineLibrary_RobotWinCCToRobots:

    pass
class MachineLibrary_RobotConfSendOrders:

    pass
class MachineLibrary_RobotVarToBusyCodes:

    pass
class MachineLibrary_RobotWinCCToRobot:

    def __init__(self, robotwincctorobotFrom_X: str, robotwincctorobotTo_X: str, robotwincctorobootType_X: str, robotwincctorobootSeq_X: int, MachineLibrary_RobotWinCCToRobot: "MachineLibrary_RobotWinCCToRobots" = None):
        self.robotwincctorobotFrom_X = robotwincctorobotFrom_X
        self.robotwincctorobotTo_X = robotwincctorobotTo_X
        self.robotwincctorobootType_X = robotwincctorobootType_X
        self.robotwincctorobootSeq_X = robotwincctorobootSeq_X
        self.MachineLibrary_RobotWinCCToRobot = MachineLibrary_RobotWinCCToRobot
        
    @property
    def robotwincctorobotFrom_X(self) -> str:
        return self.__robotwincctorobotFrom_X

    @robotwincctorobotFrom_X.setter
    def robotwincctorobotFrom_X(self, robotwincctorobotFrom_X: str):
        self.__robotwincctorobotFrom_X = robotwincctorobotFrom_X

    @property
    def robotwincctorobotTo_X(self) -> str:
        return self.__robotwincctorobotTo_X

    @robotwincctorobotTo_X.setter
    def robotwincctorobotTo_X(self, robotwincctorobotTo_X: str):
        self.__robotwincctorobotTo_X = robotwincctorobotTo_X

    @property
    def robotwincctorobootSeq_X(self) -> int:
        return self.__robotwincctorobootSeq_X

    @robotwincctorobootSeq_X.setter
    def robotwincctorobootSeq_X(self, robotwincctorobootSeq_X: int):
        self.__robotwincctorobootSeq_X = robotwincctorobootSeq_X

    @property
    def robotwincctorobootType_X(self) -> str:
        return self.__robotwincctorobootType_X

    @robotwincctorobootType_X.setter
    def robotwincctorobootType_X(self, robotwincctorobootType_X: str):
        self.__robotwincctorobootType_X = robotwincctorobootType_X

    @property
    def MachineLibrary_RobotWinCCToRobot(self):
        return self.__MachineLibrary_RobotWinCCToRobot

    @MachineLibrary_RobotWinCCToRobot.setter
    def MachineLibrary_RobotWinCCToRobot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotWinCCToRobot__MachineLibrary_RobotWinCCToRobot", None)
        self.__MachineLibrary_RobotWinCCToRobot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotWinCCToRobots256"):
                opp_val = getattr(old_value, "MachineLibrary_RobotWinCCToRobots256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotWinCCToRobots256"):
                opp_val = getattr(value, "MachineLibrary_RobotWinCCToRobots256", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RobotWinCCToRobots256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_PlainMoveEntrySend:

    def __init__(self, plainmoveSeq: int, plainmoveEntry: str, plainmoveSend: str, MachineLibrary_PlainMoveEntrySend: "MachineLibrary_PlainMove" = None):
        self.plainmoveSeq = plainmoveSeq
        self.plainmoveEntry = plainmoveEntry
        self.plainmoveSend = plainmoveSend
        self.MachineLibrary_PlainMoveEntrySend = MachineLibrary_PlainMoveEntrySend
        
    @property
    def plainmoveEntry(self) -> str:
        return self.__plainmoveEntry

    @plainmoveEntry.setter
    def plainmoveEntry(self, plainmoveEntry: str):
        self.__plainmoveEntry = plainmoveEntry

    @property
    def plainmoveSeq(self) -> int:
        return self.__plainmoveSeq

    @plainmoveSeq.setter
    def plainmoveSeq(self, plainmoveSeq: int):
        self.__plainmoveSeq = plainmoveSeq

    @property
    def plainmoveSend(self) -> str:
        return self.__plainmoveSend

    @plainmoveSend.setter
    def plainmoveSend(self, plainmoveSend: str):
        self.__plainmoveSend = plainmoveSend

    @property
    def MachineLibrary_PlainMoveEntrySend(self):
        return self.__MachineLibrary_PlainMoveEntrySend

    @MachineLibrary_PlainMoveEntrySend.setter
    def MachineLibrary_PlainMoveEntrySend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PlainMoveEntrySend__MachineLibrary_PlainMoveEntrySend", None)
        self.__MachineLibrary_PlainMoveEntrySend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_PlainMove238"):
                opp_val = getattr(old_value, "MachineLibrary_PlainMove238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_PlainMove238"):
                opp_val = getattr(value, "MachineLibrary_PlainMove238", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_PlainMove238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_TransferFileSection:

    def __init__(self, transferFile: str, transferSection: str, transferSeq: int, MachineLibrary_TransferFileSection: "MachineLibrary_Transfer" = None):
        self.transferFile = transferFile
        self.transferSection = transferSection
        self.transferSeq = transferSeq
        self.MachineLibrary_TransferFileSection = MachineLibrary_TransferFileSection
        
    @property
    def transferSeq(self) -> int:
        return self.__transferSeq

    @transferSeq.setter
    def transferSeq(self, transferSeq: int):
        self.__transferSeq = transferSeq

    @property
    def transferSection(self) -> str:
        return self.__transferSection

    @transferSection.setter
    def transferSection(self, transferSection: str):
        self.__transferSection = transferSection

    @property
    def transferFile(self) -> str:
        return self.__transferFile

    @transferFile.setter
    def transferFile(self, transferFile: str):
        self.__transferFile = transferFile

    @property
    def MachineLibrary_TransferFileSection(self):
        return self.__MachineLibrary_TransferFileSection

    @MachineLibrary_TransferFileSection.setter
    def MachineLibrary_TransferFileSection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_TransferFileSection__MachineLibrary_TransferFileSection", None)
        self.__MachineLibrary_TransferFileSection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Transfer236"):
                opp_val = getattr(old_value, "MachineLibrary_Transfer236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Transfer236"):
                opp_val = getattr(value, "MachineLibrary_Transfer236", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Transfer236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_RobotConfiguration:

    def __init__(self, robotActivate: int, robotSystemID: str, robotID: str, robotIPAddress: str, MachineLibrary_RobotConfiguration: "MachineLibrary_NodeSpecialConfiguration" = None, MachineLibrary_RobotConfiguration240: "MachineLibrary_RobotVarToBusyCodes" = None, MachineLibrary_RobotConfiguration242: "MachineLibrary_RobotConfSendOrders" = None, MachineLibrary_RobotConfiguration244: "MachineLibrary_RobotWinCCToRobots" = None, MachineLibrary_RobotConfiguration246: "MachineLibrary_RobotToWinccs" = None, MachineLibrary_RobotConfiguration248: "MachineLibrary_RobotWarningONDelete" = None, MachineLibrary_RobotConfiguration250: "MachineLibrary_RobotVarToErrorbits" = None):
        self.robotActivate = robotActivate
        self.robotSystemID = robotSystemID
        self.robotID = robotID
        self.robotIPAddress = robotIPAddress
        self.MachineLibrary_RobotConfiguration = MachineLibrary_RobotConfiguration
        self.MachineLibrary_RobotConfiguration240 = MachineLibrary_RobotConfiguration240
        self.MachineLibrary_RobotConfiguration242 = MachineLibrary_RobotConfiguration242
        self.MachineLibrary_RobotConfiguration244 = MachineLibrary_RobotConfiguration244
        self.MachineLibrary_RobotConfiguration246 = MachineLibrary_RobotConfiguration246
        self.MachineLibrary_RobotConfiguration248 = MachineLibrary_RobotConfiguration248
        self.MachineLibrary_RobotConfiguration250 = MachineLibrary_RobotConfiguration250
        
    @property
    def robotID(self) -> str:
        return self.__robotID

    @robotID.setter
    def robotID(self, robotID: str):
        self.__robotID = robotID

    @property
    def robotActivate(self) -> int:
        return self.__robotActivate

    @robotActivate.setter
    def robotActivate(self, robotActivate: int):
        self.__robotActivate = robotActivate

    @property
    def robotSystemID(self) -> str:
        return self.__robotSystemID

    @robotSystemID.setter
    def robotSystemID(self, robotSystemID: str):
        self.__robotSystemID = robotSystemID

    @property
    def robotIPAddress(self) -> str:
        return self.__robotIPAddress

    @robotIPAddress.setter
    def robotIPAddress(self, robotIPAddress: str):
        self.__robotIPAddress = robotIPAddress

    @property
    def MachineLibrary_RobotConfiguration(self):
        return self.__MachineLibrary_RobotConfiguration

    @MachineLibrary_RobotConfiguration.setter
    def MachineLibrary_RobotConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration", None)
        self.__MachineLibrary_RobotConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeSpecialConfiguration234"):
                opp_val = getattr(old_value, "MachineLibrary_NodeSpecialConfiguration234", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeSpecialConfiguration234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeSpecialConfiguration234"):
                opp_val = getattr(value, "MachineLibrary_NodeSpecialConfiguration234", None)
                setattr(value, "MachineLibrary_NodeSpecialConfiguration234", self)

    @property
    def MachineLibrary_RobotConfiguration244(self):
        return self.__MachineLibrary_RobotConfiguration244

    @MachineLibrary_RobotConfiguration244.setter
    def MachineLibrary_RobotConfiguration244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration244", None)
        self.__MachineLibrary_RobotConfiguration244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotWinCCToRobots"):
                opp_val = getattr(old_value, "MachineLibrary_RobotWinCCToRobots", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotWinCCToRobots", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotWinCCToRobots"):
                opp_val = getattr(value, "MachineLibrary_RobotWinCCToRobots", None)
                setattr(value, "MachineLibrary_RobotWinCCToRobots", self)

    @property
    def MachineLibrary_RobotConfiguration242(self):
        return self.__MachineLibrary_RobotConfiguration242

    @MachineLibrary_RobotConfiguration242.setter
    def MachineLibrary_RobotConfiguration242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration242", None)
        self.__MachineLibrary_RobotConfiguration242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotConfSendOrders"):
                opp_val = getattr(old_value, "MachineLibrary_RobotConfSendOrders", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotConfSendOrders", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotConfSendOrders"):
                opp_val = getattr(value, "MachineLibrary_RobotConfSendOrders", None)
                setattr(value, "MachineLibrary_RobotConfSendOrders", self)

    @property
    def MachineLibrary_RobotConfiguration250(self):
        return self.__MachineLibrary_RobotConfiguration250

    @MachineLibrary_RobotConfiguration250.setter
    def MachineLibrary_RobotConfiguration250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration250", None)
        self.__MachineLibrary_RobotConfiguration250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotVarToErrorbits"):
                opp_val = getattr(old_value, "MachineLibrary_RobotVarToErrorbits", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotVarToErrorbits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotVarToErrorbits"):
                opp_val = getattr(value, "MachineLibrary_RobotVarToErrorbits", None)
                setattr(value, "MachineLibrary_RobotVarToErrorbits", self)

    @property
    def MachineLibrary_RobotConfiguration246(self):
        return self.__MachineLibrary_RobotConfiguration246

    @MachineLibrary_RobotConfiguration246.setter
    def MachineLibrary_RobotConfiguration246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration246", None)
        self.__MachineLibrary_RobotConfiguration246 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotToWinccs"):
                opp_val = getattr(old_value, "MachineLibrary_RobotToWinccs", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotToWinccs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotToWinccs"):
                opp_val = getattr(value, "MachineLibrary_RobotToWinccs", None)
                setattr(value, "MachineLibrary_RobotToWinccs", self)

    @property
    def MachineLibrary_RobotConfiguration240(self):
        return self.__MachineLibrary_RobotConfiguration240

    @MachineLibrary_RobotConfiguration240.setter
    def MachineLibrary_RobotConfiguration240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration240", None)
        self.__MachineLibrary_RobotConfiguration240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotVarToBusyCodes"):
                opp_val = getattr(old_value, "MachineLibrary_RobotVarToBusyCodes", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotVarToBusyCodes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotVarToBusyCodes"):
                opp_val = getattr(value, "MachineLibrary_RobotVarToBusyCodes", None)
                setattr(value, "MachineLibrary_RobotVarToBusyCodes", self)

    @property
    def MachineLibrary_RobotConfiguration248(self):
        return self.__MachineLibrary_RobotConfiguration248

    @MachineLibrary_RobotConfiguration248.setter
    def MachineLibrary_RobotConfiguration248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RobotConfiguration__MachineLibrary_RobotConfiguration248", None)
        self.__MachineLibrary_RobotConfiguration248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RobotWarningONDelete"):
                opp_val = getattr(old_value, "MachineLibrary_RobotWarningONDelete", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_RobotWarningONDelete", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RobotWarningONDelete"):
                opp_val = getattr(value, "MachineLibrary_RobotWarningONDelete", None)
                setattr(value, "MachineLibrary_RobotWarningONDelete", self)

class MachineLibrary_PlainMove:

    def __init__(self, plainmoveType: int, plainmoveSID_REF: str, plainmovePreDefWS: str, MachineLibrary_PlainMove: "MachineLibrary_NodeSpecialConfiguration" = None, MachineLibrary_PlainMove238: set["MachineLibrary_PlainMoveEntrySend"] = None):
        self.plainmoveType = plainmoveType
        self.plainmoveSID_REF = plainmoveSID_REF
        self.plainmovePreDefWS = plainmovePreDefWS
        self.MachineLibrary_PlainMove = MachineLibrary_PlainMove
        self.MachineLibrary_PlainMove238 = MachineLibrary_PlainMove238 if MachineLibrary_PlainMove238 is not None else set()
        
    @property
    def plainmoveSID_REF(self) -> str:
        return self.__plainmoveSID_REF

    @plainmoveSID_REF.setter
    def plainmoveSID_REF(self, plainmoveSID_REF: str):
        self.__plainmoveSID_REF = plainmoveSID_REF

    @property
    def plainmoveType(self) -> int:
        return self.__plainmoveType

    @plainmoveType.setter
    def plainmoveType(self, plainmoveType: int):
        self.__plainmoveType = plainmoveType

    @property
    def plainmovePreDefWS(self) -> str:
        return self.__plainmovePreDefWS

    @plainmovePreDefWS.setter
    def plainmovePreDefWS(self, plainmovePreDefWS: str):
        self.__plainmovePreDefWS = plainmovePreDefWS

    @property
    def MachineLibrary_PlainMove(self):
        return self.__MachineLibrary_PlainMove

    @MachineLibrary_PlainMove.setter
    def MachineLibrary_PlainMove(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PlainMove__MachineLibrary_PlainMove", None)
        self.__MachineLibrary_PlainMove = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeSpecialConfiguration232"):
                opp_val = getattr(old_value, "MachineLibrary_NodeSpecialConfiguration232", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeSpecialConfiguration232", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeSpecialConfiguration232"):
                opp_val = getattr(value, "MachineLibrary_NodeSpecialConfiguration232", None)
                setattr(value, "MachineLibrary_NodeSpecialConfiguration232", self)

    @property
    def MachineLibrary_PlainMove238(self):
        return self.__MachineLibrary_PlainMove238

    @MachineLibrary_PlainMove238.setter
    def MachineLibrary_PlainMove238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PlainMove__MachineLibrary_PlainMove238", None)
        self.__MachineLibrary_PlainMove238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_PlainMoveEntrySend"):
                    opp_val = getattr(item, "MachineLibrary_PlainMoveEntrySend", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_PlainMoveEntrySend", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_PlainMoveEntrySend"):
                    opp_val = getattr(item, "MachineLibrary_PlainMoveEntrySend", None)
                    
                    setattr(item, "MachineLibrary_PlainMoveEntrySend", self)
                    

class MachineLibrary_Transfer:

    pass
class MachineLibrary_ParamPrint:

    def __init__(self, fontHightHeader: float, fontHightData: float, vertPosHeader: float, vertPosData: float, vertLineSpace: float, horzPosLeftBorder: float, horzPosValues: float, dateStamp: str, MachineLibrary_ParamPrint: "MachineLibrary_NodeSpecialConfiguration" = None):
        self.fontHightHeader = fontHightHeader
        self.fontHightData = fontHightData
        self.vertPosHeader = vertPosHeader
        self.vertPosData = vertPosData
        self.vertLineSpace = vertLineSpace
        self.horzPosLeftBorder = horzPosLeftBorder
        self.horzPosValues = horzPosValues
        self.dateStamp = dateStamp
        self.MachineLibrary_ParamPrint = MachineLibrary_ParamPrint
        
    @property
    def horzPosValues(self) -> float:
        return self.__horzPosValues

    @horzPosValues.setter
    def horzPosValues(self, horzPosValues: float):
        self.__horzPosValues = horzPosValues

    @property
    def vertPosHeader(self) -> float:
        return self.__vertPosHeader

    @vertPosHeader.setter
    def vertPosHeader(self, vertPosHeader: float):
        self.__vertPosHeader = vertPosHeader

    @property
    def vertPosData(self) -> float:
        return self.__vertPosData

    @vertPosData.setter
    def vertPosData(self, vertPosData: float):
        self.__vertPosData = vertPosData

    @property
    def fontHightData(self) -> float:
        return self.__fontHightData

    @fontHightData.setter
    def fontHightData(self, fontHightData: float):
        self.__fontHightData = fontHightData

    @property
    def fontHightHeader(self) -> float:
        return self.__fontHightHeader

    @fontHightHeader.setter
    def fontHightHeader(self, fontHightHeader: float):
        self.__fontHightHeader = fontHightHeader

    @property
    def horzPosLeftBorder(self) -> float:
        return self.__horzPosLeftBorder

    @horzPosLeftBorder.setter
    def horzPosLeftBorder(self, horzPosLeftBorder: float):
        self.__horzPosLeftBorder = horzPosLeftBorder

    @property
    def vertLineSpace(self) -> float:
        return self.__vertLineSpace

    @vertLineSpace.setter
    def vertLineSpace(self, vertLineSpace: float):
        self.__vertLineSpace = vertLineSpace

    @property
    def dateStamp(self) -> str:
        return self.__dateStamp

    @dateStamp.setter
    def dateStamp(self, dateStamp: str):
        self.__dateStamp = dateStamp

    @property
    def MachineLibrary_ParamPrint(self):
        return self.__MachineLibrary_ParamPrint

    @MachineLibrary_ParamPrint.setter
    def MachineLibrary_ParamPrint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ParamPrint__MachineLibrary_ParamPrint", None)
        self.__MachineLibrary_ParamPrint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeSpecialConfiguration228"):
                opp_val = getattr(old_value, "MachineLibrary_NodeSpecialConfiguration228", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeSpecialConfiguration228", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeSpecialConfiguration228"):
                opp_val = getattr(value, "MachineLibrary_NodeSpecialConfiguration228", None)
                setattr(value, "MachineLibrary_NodeSpecialConfiguration228", self)

class MachineLibrary_Parameter:

    def __init__(self, parameterName: str, parameterT1: str, parameterT2: str, parameterV: str, parameterType: str, parameterV0: str, parameterV1: str, parameterMin: int, parameterMax: int, parameterParaLen: int, parameterConfig: str, MachineLibrary_Parameter: "MachineLibrary_Parameters" = None):
        self.parameterName = parameterName
        self.parameterT1 = parameterT1
        self.parameterT2 = parameterT2
        self.parameterV = parameterV
        self.parameterType = parameterType
        self.parameterV0 = parameterV0
        self.parameterV1 = parameterV1
        self.parameterMin = parameterMin
        self.parameterMax = parameterMax
        self.parameterParaLen = parameterParaLen
        self.parameterConfig = parameterConfig
        self.MachineLibrary_Parameter = MachineLibrary_Parameter
        
    @property
    def parameterMin(self) -> int:
        return self.__parameterMin

    @parameterMin.setter
    def parameterMin(self, parameterMin: int):
        self.__parameterMin = parameterMin

    @property
    def parameterT1(self) -> str:
        return self.__parameterT1

    @parameterT1.setter
    def parameterT1(self, parameterT1: str):
        self.__parameterT1 = parameterT1

    @property
    def parameterMax(self) -> int:
        return self.__parameterMax

    @parameterMax.setter
    def parameterMax(self, parameterMax: int):
        self.__parameterMax = parameterMax

    @property
    def parameterConfig(self) -> str:
        return self.__parameterConfig

    @parameterConfig.setter
    def parameterConfig(self, parameterConfig: str):
        self.__parameterConfig = parameterConfig

    @property
    def parameterT2(self) -> str:
        return self.__parameterT2

    @parameterT2.setter
    def parameterT2(self, parameterT2: str):
        self.__parameterT2 = parameterT2

    @property
    def parameterV(self) -> str:
        return self.__parameterV

    @parameterV.setter
    def parameterV(self, parameterV: str):
        self.__parameterV = parameterV

    @property
    def parameterName(self) -> str:
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName

    @property
    def parameterV1(self) -> str:
        return self.__parameterV1

    @parameterV1.setter
    def parameterV1(self, parameterV1: str):
        self.__parameterV1 = parameterV1

    @property
    def parameterType(self) -> str:
        return self.__parameterType

    @parameterType.setter
    def parameterType(self, parameterType: str):
        self.__parameterType = parameterType

    @property
    def parameterV0(self) -> str:
        return self.__parameterV0

    @parameterV0.setter
    def parameterV0(self, parameterV0: str):
        self.__parameterV0 = parameterV0

    @property
    def parameterParaLen(self) -> int:
        return self.__parameterParaLen

    @parameterParaLen.setter
    def parameterParaLen(self, parameterParaLen: int):
        self.__parameterParaLen = parameterParaLen

    @property
    def MachineLibrary_Parameter(self):
        return self.__MachineLibrary_Parameter

    @MachineLibrary_Parameter.setter
    def MachineLibrary_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Parameter__MachineLibrary_Parameter", None)
        self.__MachineLibrary_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Parameters226"):
                opp_val = getattr(old_value, "MachineLibrary_Parameters226", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Parameters226"):
                opp_val = getattr(value, "MachineLibrary_Parameters226", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Parameters226", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_UnitProgParameters:

    def __init__(self, parameter: str, parameterNo: int, MachineLibrary_UnitProgParameters: "MachineLibrary_UnitProgram" = None):
        self.parameter = parameter
        self.parameterNo = parameterNo
        self.MachineLibrary_UnitProgParameters = MachineLibrary_UnitProgParameters
        
    @property
    def parameterNo(self) -> int:
        return self.__parameterNo

    @parameterNo.setter
    def parameterNo(self, parameterNo: int):
        self.__parameterNo = parameterNo

    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def MachineLibrary_UnitProgParameters(self):
        return self.__MachineLibrary_UnitProgParameters

    @MachineLibrary_UnitProgParameters.setter
    def MachineLibrary_UnitProgParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitProgParameters__MachineLibrary_UnitProgParameters", None)
        self.__MachineLibrary_UnitProgParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitProgram224"):
                opp_val = getattr(old_value, "MachineLibrary_UnitProgram224", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitProgram224"):
                opp_val = getattr(value, "MachineLibrary_UnitProgram224", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_UnitProgram224", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_UnitProgram:

    def __init__(self, unitProgName: str, MachineLibrary_UnitProgram: "MachineLibrary_UnitPrograms" = None, MachineLibrary_UnitProgram224: set["MachineLibrary_UnitProgParameters"] = None):
        self.unitProgName = unitProgName
        self.MachineLibrary_UnitProgram = MachineLibrary_UnitProgram
        self.MachineLibrary_UnitProgram224 = MachineLibrary_UnitProgram224 if MachineLibrary_UnitProgram224 is not None else set()
        
    @property
    def unitProgName(self) -> str:
        return self.__unitProgName

    @unitProgName.setter
    def unitProgName(self, unitProgName: str):
        self.__unitProgName = unitProgName

    @property
    def MachineLibrary_UnitProgram(self):
        return self.__MachineLibrary_UnitProgram

    @MachineLibrary_UnitProgram.setter
    def MachineLibrary_UnitProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitProgram__MachineLibrary_UnitProgram", None)
        self.__MachineLibrary_UnitProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitPrograms222"):
                opp_val = getattr(old_value, "MachineLibrary_UnitPrograms222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitPrograms222"):
                opp_val = getattr(value, "MachineLibrary_UnitPrograms222", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_UnitPrograms222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_UnitProgram224(self):
        return self.__MachineLibrary_UnitProgram224

    @MachineLibrary_UnitProgram224.setter
    def MachineLibrary_UnitProgram224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitProgram__MachineLibrary_UnitProgram224", None)
        self.__MachineLibrary_UnitProgram224 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_UnitProgParameters"):
                    opp_val = getattr(item, "MachineLibrary_UnitProgParameters", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_UnitProgParameters", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_UnitProgParameters"):
                    opp_val = getattr(item, "MachineLibrary_UnitProgParameters", None)
                    
                    setattr(item, "MachineLibrary_UnitProgParameters", self)
                    

class MachineLibrary_NodeProgram:

    def __init__(self, programName: str, programAddress: str, programLenPerParam: str, programSection: str, programNo: int, MachineLibrary_NodeProgram: "MachineLibrary_NodePrograms" = None):
        self.programName = programName
        self.programAddress = programAddress
        self.programLenPerParam = programLenPerParam
        self.programSection = programSection
        self.programNo = programNo
        self.MachineLibrary_NodeProgram = MachineLibrary_NodeProgram
        
    @property
    def programName(self) -> str:
        return self.__programName

    @programName.setter
    def programName(self, programName: str):
        self.__programName = programName

    @property
    def programNo(self) -> int:
        return self.__programNo

    @programNo.setter
    def programNo(self, programNo: int):
        self.__programNo = programNo

    @property
    def programSection(self) -> str:
        return self.__programSection

    @programSection.setter
    def programSection(self, programSection: str):
        self.__programSection = programSection

    @property
    def programLenPerParam(self) -> str:
        return self.__programLenPerParam

    @programLenPerParam.setter
    def programLenPerParam(self, programLenPerParam: str):
        self.__programLenPerParam = programLenPerParam

    @property
    def programAddress(self) -> str:
        return self.__programAddress

    @programAddress.setter
    def programAddress(self, programAddress: str):
        self.__programAddress = programAddress

    @property
    def MachineLibrary_NodeProgram(self):
        return self.__MachineLibrary_NodeProgram

    @MachineLibrary_NodeProgram.setter
    def MachineLibrary_NodeProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeProgram__MachineLibrary_NodeProgram", None)
        self.__MachineLibrary_NodeProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodePrograms220"):
                opp_val = getattr(old_value, "MachineLibrary_NodePrograms220", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodePrograms220"):
                opp_val = getattr(value, "MachineLibrary_NodePrograms220", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_NodePrograms220", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_Command:

    def __init__(self, commandName: str, commandNo: str, commandProgParameter: int, MachineLibrary_Command: "MachineLibrary_Commands" = None):
        self.commandName = commandName
        self.commandNo = commandNo
        self.commandProgParameter = commandProgParameter
        self.MachineLibrary_Command = MachineLibrary_Command
        
    @property
    def commandProgParameter(self) -> int:
        return self.__commandProgParameter

    @commandProgParameter.setter
    def commandProgParameter(self, commandProgParameter: int):
        self.__commandProgParameter = commandProgParameter

    @property
    def commandNo(self) -> str:
        return self.__commandNo

    @commandNo.setter
    def commandNo(self, commandNo: str):
        self.__commandNo = commandNo

    @property
    def commandName(self) -> str:
        return self.__commandName

    @commandName.setter
    def commandName(self, commandName: str):
        self.__commandName = commandName

    @property
    def MachineLibrary_Command(self):
        return self.__MachineLibrary_Command

    @MachineLibrary_Command.setter
    def MachineLibrary_Command(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Command__MachineLibrary_Command", None)
        self.__MachineLibrary_Command = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Commands218"):
                opp_val = getattr(old_value, "MachineLibrary_Commands218", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Commands218"):
                opp_val = getattr(value, "MachineLibrary_Commands218", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Commands218", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_StatusBit:

    def __init__(self, bitName: str, bitNo: int, MachineLibrary_StatusBit: "MachineLibrary_StausBits" = None):
        self.bitName = bitName
        self.bitNo = bitNo
        self.MachineLibrary_StatusBit = MachineLibrary_StatusBit
        
    @property
    def bitName(self) -> str:
        return self.__bitName

    @bitName.setter
    def bitName(self, bitName: str):
        self.__bitName = bitName

    @property
    def bitNo(self) -> int:
        return self.__bitNo

    @bitNo.setter
    def bitNo(self, bitNo: int):
        self.__bitNo = bitNo

    @property
    def MachineLibrary_StatusBit(self):
        return self.__MachineLibrary_StatusBit

    @MachineLibrary_StatusBit.setter
    def MachineLibrary_StatusBit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_StatusBit__MachineLibrary_StatusBit", None)
        self.__MachineLibrary_StatusBit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_StausBits216"):
                opp_val = getattr(old_value, "MachineLibrary_StausBits216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_StausBits216"):
                opp_val = getattr(value, "MachineLibrary_StausBits216", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_StausBits216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_Position:

    def __init__(self, posName: str, posNo: int, posIndex: int, posWarningOnDelete: int, posExit: int, posRemark: str, MachineLibrary_Position: "MachineLibrary_Positions" = None):
        self.posName = posName
        self.posNo = posNo
        self.posIndex = posIndex
        self.posWarningOnDelete = posWarningOnDelete
        self.posExit = posExit
        self.posRemark = posRemark
        self.MachineLibrary_Position = MachineLibrary_Position
        
    @property
    def posWarningOnDelete(self) -> int:
        return self.__posWarningOnDelete

    @posWarningOnDelete.setter
    def posWarningOnDelete(self, posWarningOnDelete: int):
        self.__posWarningOnDelete = posWarningOnDelete

    @property
    def posIndex(self) -> int:
        return self.__posIndex

    @posIndex.setter
    def posIndex(self, posIndex: int):
        self.__posIndex = posIndex

    @property
    def posName(self) -> str:
        return self.__posName

    @posName.setter
    def posName(self, posName: str):
        self.__posName = posName

    @property
    def posRemark(self) -> str:
        return self.__posRemark

    @posRemark.setter
    def posRemark(self, posRemark: str):
        self.__posRemark = posRemark

    @property
    def posNo(self) -> int:
        return self.__posNo

    @posNo.setter
    def posNo(self, posNo: int):
        self.__posNo = posNo

    @property
    def posExit(self) -> int:
        return self.__posExit

    @posExit.setter
    def posExit(self, posExit: int):
        self.__posExit = posExit

    @property
    def MachineLibrary_Position(self):
        return self.__MachineLibrary_Position

    @MachineLibrary_Position.setter
    def MachineLibrary_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Position__MachineLibrary_Position", None)
        self.__MachineLibrary_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Positions214"):
                opp_val = getattr(old_value, "MachineLibrary_Positions214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Positions214"):
                opp_val = getattr(value, "MachineLibrary_Positions214", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Positions214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_CheckAddSID_Values_PM2PM:

    def __init__(self, optionNo: int, optonValue: str, MachineLibrary_CheckAddSID_Values_PM2PM: "MachineLibrary_CheckAddSID_PM2PM" = None):
        self.optionNo = optionNo
        self.optonValue = optonValue
        self.MachineLibrary_CheckAddSID_Values_PM2PM = MachineLibrary_CheckAddSID_Values_PM2PM
        
    @property
    def optionNo(self) -> int:
        return self.__optionNo

    @optionNo.setter
    def optionNo(self, optionNo: int):
        self.__optionNo = optionNo

    @property
    def optonValue(self) -> str:
        return self.__optonValue

    @optonValue.setter
    def optonValue(self, optonValue: str):
        self.__optonValue = optonValue

    @property
    def MachineLibrary_CheckAddSID_Values_PM2PM(self):
        return self.__MachineLibrary_CheckAddSID_Values_PM2PM

    @MachineLibrary_CheckAddSID_Values_PM2PM.setter
    def MachineLibrary_CheckAddSID_Values_PM2PM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckAddSID_Values_PM2PM__MachineLibrary_CheckAddSID_Values_PM2PM", None)
        self.__MachineLibrary_CheckAddSID_Values_PM2PM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckAddSID_PM2PM210"):
                opp_val = getattr(old_value, "MachineLibrary_CheckAddSID_PM2PM210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckAddSID_PM2PM210"):
                opp_val = getattr(value, "MachineLibrary_CheckAddSID_PM2PM210", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckAddSID_PM2PM210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_SepByComma_ID_Scanner:

    def __init__(self, idSeq_X: int, idValue: int, idPrevValue: str, idCharValue: str, MachineLibrary_SepByComma_ID_Scanner: "MachineLibrary_SepByComma_Scanner" = None):
        self.idSeq_X = idSeq_X
        self.idValue = idValue
        self.idPrevValue = idPrevValue
        self.idCharValue = idCharValue
        self.MachineLibrary_SepByComma_ID_Scanner = MachineLibrary_SepByComma_ID_Scanner
        
    @property
    def idPrevValue(self) -> str:
        return self.__idPrevValue

    @idPrevValue.setter
    def idPrevValue(self, idPrevValue: str):
        self.__idPrevValue = idPrevValue

    @property
    def idCharValue(self) -> str:
        return self.__idCharValue

    @idCharValue.setter
    def idCharValue(self, idCharValue: str):
        self.__idCharValue = idCharValue

    @property
    def idValue(self) -> int:
        return self.__idValue

    @idValue.setter
    def idValue(self, idValue: int):
        self.__idValue = idValue

    @property
    def idSeq_X(self) -> int:
        return self.__idSeq_X

    @idSeq_X.setter
    def idSeq_X(self, idSeq_X: int):
        self.__idSeq_X = idSeq_X

    @property
    def MachineLibrary_SepByComma_ID_Scanner(self):
        return self.__MachineLibrary_SepByComma_ID_Scanner

    @MachineLibrary_SepByComma_ID_Scanner.setter
    def MachineLibrary_SepByComma_ID_Scanner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_SepByComma_ID_Scanner__MachineLibrary_SepByComma_ID_Scanner", None)
        self.__MachineLibrary_SepByComma_ID_Scanner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_SepByComma_Scanner208"):
                opp_val = getattr(old_value, "MachineLibrary_SepByComma_Scanner208", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_SepByComma_Scanner208"):
                opp_val = getattr(value, "MachineLibrary_SepByComma_Scanner208", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_SepByComma_Scanner208", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_SepByComma_Field_Scanner:

    def __init__(self, fieldNo: int, fieldName: str, MachineLibrary_SepByComma_Field_Scanner: "MachineLibrary_SepByComma_Scanner" = None):
        self.fieldNo = fieldNo
        self.fieldName = fieldName
        self.MachineLibrary_SepByComma_Field_Scanner = MachineLibrary_SepByComma_Field_Scanner
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def fieldNo(self) -> int:
        return self.__fieldNo

    @fieldNo.setter
    def fieldNo(self, fieldNo: int):
        self.__fieldNo = fieldNo

    @property
    def MachineLibrary_SepByComma_Field_Scanner(self):
        return self.__MachineLibrary_SepByComma_Field_Scanner

    @MachineLibrary_SepByComma_Field_Scanner.setter
    def MachineLibrary_SepByComma_Field_Scanner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_SepByComma_Field_Scanner__MachineLibrary_SepByComma_Field_Scanner", None)
        self.__MachineLibrary_SepByComma_Field_Scanner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_SepByComma_Scanner206"):
                opp_val = getattr(old_value, "MachineLibrary_SepByComma_Scanner206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_SepByComma_Scanner206"):
                opp_val = getattr(value, "MachineLibrary_SepByComma_Scanner206", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_SepByComma_Scanner206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_InsertRemove_Keywords_Host:

    def __init__(self, keywordKey: str, keywordValue: str, MachineLibrary_InsertRemove_Keywords_Host: "MachineLibrary_InsertRemove_Host" = None):
        self.keywordKey = keywordKey
        self.keywordValue = keywordValue
        self.MachineLibrary_InsertRemove_Keywords_Host = MachineLibrary_InsertRemove_Keywords_Host
        
    @property
    def keywordKey(self) -> str:
        return self.__keywordKey

    @keywordKey.setter
    def keywordKey(self, keywordKey: str):
        self.__keywordKey = keywordKey

    @property
    def keywordValue(self) -> str:
        return self.__keywordValue

    @keywordValue.setter
    def keywordValue(self, keywordValue: str):
        self.__keywordValue = keywordValue

    @property
    def MachineLibrary_InsertRemove_Keywords_Host(self):
        return self.__MachineLibrary_InsertRemove_Keywords_Host

    @MachineLibrary_InsertRemove_Keywords_Host.setter
    def MachineLibrary_InsertRemove_Keywords_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Keywords_Host__MachineLibrary_InsertRemove_Keywords_Host", None)
        self.__MachineLibrary_InsertRemove_Keywords_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_InsertRemove_Host204"):
                opp_val = getattr(old_value, "MachineLibrary_InsertRemove_Host204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_InsertRemove_Host204"):
                opp_val = getattr(value, "MachineLibrary_InsertRemove_Host204", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_InsertRemove_Host204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_InsertRemove_Types_Host:

    def __init__(self, typeNo: int, typeValue: str, MachineLibrary_InsertRemove_Types_Host: "MachineLibrary_InsertRemove_Host" = None):
        self.typeNo = typeNo
        self.typeValue = typeValue
        self.MachineLibrary_InsertRemove_Types_Host = MachineLibrary_InsertRemove_Types_Host
        
    @property
    def typeNo(self) -> int:
        return self.__typeNo

    @typeNo.setter
    def typeNo(self, typeNo: int):
        self.__typeNo = typeNo

    @property
    def typeValue(self) -> str:
        return self.__typeValue

    @typeValue.setter
    def typeValue(self, typeValue: str):
        self.__typeValue = typeValue

    @property
    def MachineLibrary_InsertRemove_Types_Host(self):
        return self.__MachineLibrary_InsertRemove_Types_Host

    @MachineLibrary_InsertRemove_Types_Host.setter
    def MachineLibrary_InsertRemove_Types_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Types_Host__MachineLibrary_InsertRemove_Types_Host", None)
        self.__MachineLibrary_InsertRemove_Types_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_InsertRemove_Host202"):
                opp_val = getattr(old_value, "MachineLibrary_InsertRemove_Host202", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_InsertRemove_Host202"):
                opp_val = getattr(value, "MachineLibrary_InsertRemove_Host202", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_InsertRemove_Host202", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_InsertRemove_Entry_Host:

    def __init__(self, entryNo: int, entryName: str, MachineLibrary_InsertRemove_Entry_Host: "MachineLibrary_InsertRemove_Host" = None):
        self.entryNo = entryNo
        self.entryName = entryName
        self.MachineLibrary_InsertRemove_Entry_Host = MachineLibrary_InsertRemove_Entry_Host
        
    @property
    def entryNo(self) -> int:
        return self.__entryNo

    @entryNo.setter
    def entryNo(self, entryNo: int):
        self.__entryNo = entryNo

    @property
    def entryName(self) -> str:
        return self.__entryName

    @entryName.setter
    def entryName(self, entryName: str):
        self.__entryName = entryName

    @property
    def MachineLibrary_InsertRemove_Entry_Host(self):
        return self.__MachineLibrary_InsertRemove_Entry_Host

    @MachineLibrary_InsertRemove_Entry_Host.setter
    def MachineLibrary_InsertRemove_Entry_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Entry_Host__MachineLibrary_InsertRemove_Entry_Host", None)
        self.__MachineLibrary_InsertRemove_Entry_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_InsertRemove_Host200"):
                opp_val = getattr(old_value, "MachineLibrary_InsertRemove_Host200", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_InsertRemove_Host200"):
                opp_val = getattr(value, "MachineLibrary_InsertRemove_Host200", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_InsertRemove_Host200", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_Button:

    def __init__(self, buttonText: str, commandNo: int, buttonNo: int, MachineLibrary_Button: "MachineLibrary_Buttons" = None):
        self.buttonText = buttonText
        self.commandNo = commandNo
        self.buttonNo = buttonNo
        self.MachineLibrary_Button = MachineLibrary_Button
        
    @property
    def buttonText(self) -> str:
        return self.__buttonText

    @buttonText.setter
    def buttonText(self, buttonText: str):
        self.__buttonText = buttonText

    @property
    def buttonNo(self) -> int:
        return self.__buttonNo

    @buttonNo.setter
    def buttonNo(self, buttonNo: int):
        self.__buttonNo = buttonNo

    @property
    def commandNo(self) -> int:
        return self.__commandNo

    @commandNo.setter
    def commandNo(self, commandNo: int):
        self.__commandNo = commandNo

    @property
    def MachineLibrary_Button(self):
        return self.__MachineLibrary_Button

    @MachineLibrary_Button.setter
    def MachineLibrary_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Button__MachineLibrary_Button", None)
        self.__MachineLibrary_Button = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Buttons212"):
                opp_val = getattr(old_value, "MachineLibrary_Buttons212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Buttons212"):
                opp_val = getattr(value, "MachineLibrary_Buttons212", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Buttons212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_HistoryConfig_AccuPyc:

    def __init__(self, currentSample: str, currentSampleID: str, sampleCupWeight: float, MachineLibrary_HistoryConfig_AccuPyc: "MachineLibrary_History_AccuPycMeter" = None):
        self.currentSample = currentSample
        self.currentSampleID = currentSampleID
        self.sampleCupWeight = sampleCupWeight
        self.MachineLibrary_HistoryConfig_AccuPyc = MachineLibrary_HistoryConfig_AccuPyc
        
    @property
    def currentSample(self) -> str:
        return self.__currentSample

    @currentSample.setter
    def currentSample(self, currentSample: str):
        self.__currentSample = currentSample

    @property
    def sampleCupWeight(self) -> float:
        return self.__sampleCupWeight

    @sampleCupWeight.setter
    def sampleCupWeight(self, sampleCupWeight: float):
        self.__sampleCupWeight = sampleCupWeight

    @property
    def currentSampleID(self) -> str:
        return self.__currentSampleID

    @currentSampleID.setter
    def currentSampleID(self, currentSampleID: str):
        self.__currentSampleID = currentSampleID

    @property
    def MachineLibrary_HistoryConfig_AccuPyc(self):
        return self.__MachineLibrary_HistoryConfig_AccuPyc

    @MachineLibrary_HistoryConfig_AccuPyc.setter
    def MachineLibrary_HistoryConfig_AccuPyc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_HistoryConfig_AccuPyc__MachineLibrary_HistoryConfig_AccuPyc", None)
        self.__MachineLibrary_HistoryConfig_AccuPyc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_History_AccuPycMeter198"):
                opp_val = getattr(old_value, "MachineLibrary_History_AccuPycMeter198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_History_AccuPycMeter198"):
                opp_val = getattr(value, "MachineLibrary_History_AccuPycMeter198", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_History_AccuPycMeter198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_CheckSampleConfig_SuperQXRF:

    def __init__(self, anaProg: str, minutes: str, samples: str, program: str, sampleID: str, seq_X: int, MachineLibrary_CheckSampleConfig_SuperQXRF: "MachineLibrary_CheckSample_SuperQXRF" = None):
        self.anaProg = anaProg
        self.minutes = minutes
        self.samples = samples
        self.program = program
        self.sampleID = sampleID
        self.seq_X = seq_X
        self.MachineLibrary_CheckSampleConfig_SuperQXRF = MachineLibrary_CheckSampleConfig_SuperQXRF
        
    @property
    def samples(self) -> str:
        return self.__samples

    @samples.setter
    def samples(self, samples: str):
        self.__samples = samples

    @property
    def sampleID(self) -> str:
        return self.__sampleID

    @sampleID.setter
    def sampleID(self, sampleID: str):
        self.__sampleID = sampleID

    @property
    def minutes(self) -> str:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: str):
        self.__minutes = minutes

    @property
    def anaProg(self) -> str:
        return self.__anaProg

    @anaProg.setter
    def anaProg(self, anaProg: str):
        self.__anaProg = anaProg

    @property
    def seq_X(self) -> int:
        return self.__seq_X

    @seq_X.setter
    def seq_X(self, seq_X: int):
        self.__seq_X = seq_X

    @property
    def program(self) -> str:
        return self.__program

    @program.setter
    def program(self, program: str):
        self.__program = program

    @property
    def MachineLibrary_CheckSampleConfig_SuperQXRF(self):
        return self.__MachineLibrary_CheckSampleConfig_SuperQXRF

    @MachineLibrary_CheckSampleConfig_SuperQXRF.setter
    def MachineLibrary_CheckSampleConfig_SuperQXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckSampleConfig_SuperQXRF__MachineLibrary_CheckSampleConfig_SuperQXRF", None)
        self.__MachineLibrary_CheckSampleConfig_SuperQXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckSample_SuperQXRF196"):
                opp_val = getattr(old_value, "MachineLibrary_CheckSample_SuperQXRF196", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckSample_SuperQXRF196"):
                opp_val = getattr(value, "MachineLibrary_CheckSample_SuperQXRF196", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckSample_SuperQXRF196", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_CheckSampleRunTimeParams_SuperQXRF:

    def __init__(self, sampleType: int, value: int, MachineLibrary_CheckSampleRunTimeParams_SuperQXRF: "MachineLibrary_CheckSampleRunTime_SuperQXRF" = None):
        self.sampleType = sampleType
        self.value = value
        self.MachineLibrary_CheckSampleRunTimeParams_SuperQXRF = MachineLibrary_CheckSampleRunTimeParams_SuperQXRF
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def sampleType(self) -> int:
        return self.__sampleType

    @sampleType.setter
    def sampleType(self, sampleType: int):
        self.__sampleType = sampleType

    @property
    def MachineLibrary_CheckSampleRunTimeParams_SuperQXRF(self):
        return self.__MachineLibrary_CheckSampleRunTimeParams_SuperQXRF

    @MachineLibrary_CheckSampleRunTimeParams_SuperQXRF.setter
    def MachineLibrary_CheckSampleRunTimeParams_SuperQXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckSampleRunTimeParams_SuperQXRF__MachineLibrary_CheckSampleRunTimeParams_SuperQXRF", None)
        self.__MachineLibrary_CheckSampleRunTimeParams_SuperQXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckSampleRunTime_SuperQXRF194"):
                opp_val = getattr(old_value, "MachineLibrary_CheckSampleRunTime_SuperQXRF194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckSampleRunTime_SuperQXRF194"):
                opp_val = getattr(value, "MachineLibrary_CheckSampleRunTime_SuperQXRF194", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckSampleRunTime_SuperQXRF194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_OES_XRF_Condition:

    def __init__(self, paraName: str, para: str, comment: str, seq_X: int, MachineLibrary_OES_XRF_Condition174: "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition: "MachineLibrary_OutputRequest_OBLFOES" = None, MachineLibrary_OES_XRF_Condition162: "MachineLibrary_TestRequest_OBLFOES" = None, MachineLibrary_OES_XRF_Condition165: "MachineLibrary_RecalRequest_OBLFOES" = None, MachineLibrary_OES_XRF_Condition168: "MachineLibrary_CheckFilling_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition171: "MachineLibrary_ExecuteFiling_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition177: "MachineLibrary_ExePrepUnit_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition180: "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition183: "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition186: "MachineLibrary_DisableSCT_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition189: "MachineLibrary_Settings_ARL_XRF_OES" = None, MachineLibrary_OES_XRF_Condition192: "MachineLibrary_GeneralSetting_ARL_XRF_OES" = None):
        self.paraName = paraName
        self.para = para
        self.comment = comment
        self.seq_X = seq_X
        self.MachineLibrary_OES_XRF_Condition174 = MachineLibrary_OES_XRF_Condition174
        self.MachineLibrary_OES_XRF_Condition = MachineLibrary_OES_XRF_Condition
        self.MachineLibrary_OES_XRF_Condition162 = MachineLibrary_OES_XRF_Condition162
        self.MachineLibrary_OES_XRF_Condition165 = MachineLibrary_OES_XRF_Condition165
        self.MachineLibrary_OES_XRF_Condition168 = MachineLibrary_OES_XRF_Condition168
        self.MachineLibrary_OES_XRF_Condition171 = MachineLibrary_OES_XRF_Condition171
        self.MachineLibrary_OES_XRF_Condition177 = MachineLibrary_OES_XRF_Condition177
        self.MachineLibrary_OES_XRF_Condition180 = MachineLibrary_OES_XRF_Condition180
        self.MachineLibrary_OES_XRF_Condition183 = MachineLibrary_OES_XRF_Condition183
        self.MachineLibrary_OES_XRF_Condition186 = MachineLibrary_OES_XRF_Condition186
        self.MachineLibrary_OES_XRF_Condition189 = MachineLibrary_OES_XRF_Condition189
        self.MachineLibrary_OES_XRF_Condition192 = MachineLibrary_OES_XRF_Condition192
        
    @property
    def paraName(self) -> str:
        return self.__paraName

    @paraName.setter
    def paraName(self, paraName: str):
        self.__paraName = paraName

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def para(self) -> str:
        return self.__para

    @para.setter
    def para(self, para: str):
        self.__para = para

    @property
    def seq_X(self) -> int:
        return self.__seq_X

    @seq_X.setter
    def seq_X(self, seq_X: int):
        self.__seq_X = seq_X

    @property
    def MachineLibrary_OES_XRF_Condition(self):
        return self.__MachineLibrary_OES_XRF_Condition

    @MachineLibrary_OES_XRF_Condition.setter
    def MachineLibrary_OES_XRF_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition", None)
        self.__MachineLibrary_OES_XRF_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_OutputRequest_OBLFOES159"):
                opp_val = getattr(old_value, "MachineLibrary_OutputRequest_OBLFOES159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_OutputRequest_OBLFOES159"):
                opp_val = getattr(value, "MachineLibrary_OutputRequest_OBLFOES159", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_OutputRequest_OBLFOES159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition183(self):
        return self.__MachineLibrary_OES_XRF_Condition183

    @MachineLibrary_OES_XRF_Condition183.setter
    def MachineLibrary_OES_XRF_Condition183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition183", None)
        self.__MachineLibrary_OES_XRF_Condition183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182"):
                opp_val = getattr(old_value, "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182"):
                opp_val = getattr(value, "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition186(self):
        return self.__MachineLibrary_OES_XRF_Condition186

    @MachineLibrary_OES_XRF_Condition186.setter
    def MachineLibrary_OES_XRF_Condition186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition186", None)
        self.__MachineLibrary_OES_XRF_Condition186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_DisableSCT_ARL_XRF_OES185"):
                opp_val = getattr(old_value, "MachineLibrary_DisableSCT_ARL_XRF_OES185", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_DisableSCT_ARL_XRF_OES185"):
                opp_val = getattr(value, "MachineLibrary_DisableSCT_ARL_XRF_OES185", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_DisableSCT_ARL_XRF_OES185", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition177(self):
        return self.__MachineLibrary_OES_XRF_Condition177

    @MachineLibrary_OES_XRF_Condition177.setter
    def MachineLibrary_OES_XRF_Condition177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition177", None)
        self.__MachineLibrary_OES_XRF_Condition177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_ExePrepUnit_ARL_XRF_OES176"):
                opp_val = getattr(old_value, "MachineLibrary_ExePrepUnit_ARL_XRF_OES176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_ExePrepUnit_ARL_XRF_OES176"):
                opp_val = getattr(value, "MachineLibrary_ExePrepUnit_ARL_XRF_OES176", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_ExePrepUnit_ARL_XRF_OES176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition162(self):
        return self.__MachineLibrary_OES_XRF_Condition162

    @MachineLibrary_OES_XRF_Condition162.setter
    def MachineLibrary_OES_XRF_Condition162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition162", None)
        self.__MachineLibrary_OES_XRF_Condition162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_TestRequest_OBLFOES161"):
                opp_val = getattr(old_value, "MachineLibrary_TestRequest_OBLFOES161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_TestRequest_OBLFOES161"):
                opp_val = getattr(value, "MachineLibrary_TestRequest_OBLFOES161", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_TestRequest_OBLFOES161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition180(self):
        return self.__MachineLibrary_OES_XRF_Condition180

    @MachineLibrary_OES_XRF_Condition180.setter
    def MachineLibrary_OES_XRF_Condition180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition180", None)
        self.__MachineLibrary_OES_XRF_Condition180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179"):
                opp_val = getattr(old_value, "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179"):
                opp_val = getattr(value, "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition171(self):
        return self.__MachineLibrary_OES_XRF_Condition171

    @MachineLibrary_OES_XRF_Condition171.setter
    def MachineLibrary_OES_XRF_Condition171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition171", None)
        self.__MachineLibrary_OES_XRF_Condition171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_ExecuteFiling_ARL_XRF_OES170"):
                opp_val = getattr(old_value, "MachineLibrary_ExecuteFiling_ARL_XRF_OES170", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_ExecuteFiling_ARL_XRF_OES170"):
                opp_val = getattr(value, "MachineLibrary_ExecuteFiling_ARL_XRF_OES170", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_ExecuteFiling_ARL_XRF_OES170", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition192(self):
        return self.__MachineLibrary_OES_XRF_Condition192

    @MachineLibrary_OES_XRF_Condition192.setter
    def MachineLibrary_OES_XRF_Condition192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition192", None)
        self.__MachineLibrary_OES_XRF_Condition192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_GeneralSetting_ARL_XRF_OES191"):
                opp_val = getattr(old_value, "MachineLibrary_GeneralSetting_ARL_XRF_OES191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_GeneralSetting_ARL_XRF_OES191"):
                opp_val = getattr(value, "MachineLibrary_GeneralSetting_ARL_XRF_OES191", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_GeneralSetting_ARL_XRF_OES191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition189(self):
        return self.__MachineLibrary_OES_XRF_Condition189

    @MachineLibrary_OES_XRF_Condition189.setter
    def MachineLibrary_OES_XRF_Condition189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition189", None)
        self.__MachineLibrary_OES_XRF_Condition189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Settings_ARL_XRF_OES188"):
                opp_val = getattr(old_value, "MachineLibrary_Settings_ARL_XRF_OES188", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Settings_ARL_XRF_OES188"):
                opp_val = getattr(value, "MachineLibrary_Settings_ARL_XRF_OES188", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_Settings_ARL_XRF_OES188", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition168(self):
        return self.__MachineLibrary_OES_XRF_Condition168

    @MachineLibrary_OES_XRF_Condition168.setter
    def MachineLibrary_OES_XRF_Condition168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition168", None)
        self.__MachineLibrary_OES_XRF_Condition168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckFilling_ARL_XRF_OES167"):
                opp_val = getattr(old_value, "MachineLibrary_CheckFilling_ARL_XRF_OES167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckFilling_ARL_XRF_OES167"):
                opp_val = getattr(value, "MachineLibrary_CheckFilling_ARL_XRF_OES167", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckFilling_ARL_XRF_OES167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition165(self):
        return self.__MachineLibrary_OES_XRF_Condition165

    @MachineLibrary_OES_XRF_Condition165.setter
    def MachineLibrary_OES_XRF_Condition165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition165", None)
        self.__MachineLibrary_OES_XRF_Condition165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_RecalRequest_OBLFOES164"):
                opp_val = getattr(old_value, "MachineLibrary_RecalRequest_OBLFOES164", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_RecalRequest_OBLFOES164"):
                opp_val = getattr(value, "MachineLibrary_RecalRequest_OBLFOES164", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_RecalRequest_OBLFOES164", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_OES_XRF_Condition174(self):
        return self.__MachineLibrary_OES_XRF_Condition174

    @MachineLibrary_OES_XRF_Condition174.setter
    def MachineLibrary_OES_XRF_Condition174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OES_XRF_Condition__MachineLibrary_OES_XRF_Condition174", None)
        self.__MachineLibrary_OES_XRF_Condition174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173"):
                opp_val = getattr(old_value, "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173"):
                opp_val = getattr(value, "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_InsertRemove_Host:

    def __init__(self, report_All: int, MachineLibrary_InsertRemove_Host: "MachineLibrary_UnitConfig_Host" = None, MachineLibrary_InsertRemove_Host157: "MachineLibrary_UnitConfig_Host" = None, MachineLibrary_InsertRemove_Host200: set["MachineLibrary_InsertRemove_Entry_Host"] = None, MachineLibrary_InsertRemove_Host202: set["MachineLibrary_InsertRemove_Types_Host"] = None, MachineLibrary_InsertRemove_Host204: set["MachineLibrary_InsertRemove_Keywords_Host"] = None):
        self.report_All = report_All
        self.MachineLibrary_InsertRemove_Host = MachineLibrary_InsertRemove_Host
        self.MachineLibrary_InsertRemove_Host157 = MachineLibrary_InsertRemove_Host157
        self.MachineLibrary_InsertRemove_Host200 = MachineLibrary_InsertRemove_Host200 if MachineLibrary_InsertRemove_Host200 is not None else set()
        self.MachineLibrary_InsertRemove_Host202 = MachineLibrary_InsertRemove_Host202 if MachineLibrary_InsertRemove_Host202 is not None else set()
        self.MachineLibrary_InsertRemove_Host204 = MachineLibrary_InsertRemove_Host204 if MachineLibrary_InsertRemove_Host204 is not None else set()
        
    @property
    def report_All(self) -> int:
        return self.__report_All

    @report_All.setter
    def report_All(self, report_All: int):
        self.__report_All = report_All

    @property
    def MachineLibrary_InsertRemove_Host157(self):
        return self.__MachineLibrary_InsertRemove_Host157

    @MachineLibrary_InsertRemove_Host157.setter
    def MachineLibrary_InsertRemove_Host157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Host__MachineLibrary_InsertRemove_Host157", None)
        self.__MachineLibrary_InsertRemove_Host157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Host156"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Host156", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Host156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Host156"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Host156", None)
                setattr(value, "MachineLibrary_UnitConfig_Host156", self)

    @property
    def MachineLibrary_InsertRemove_Host(self):
        return self.__MachineLibrary_InsertRemove_Host

    @MachineLibrary_InsertRemove_Host.setter
    def MachineLibrary_InsertRemove_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Host__MachineLibrary_InsertRemove_Host", None)
        self.__MachineLibrary_InsertRemove_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Host154"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Host154", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Host154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Host154"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Host154", None)
                setattr(value, "MachineLibrary_UnitConfig_Host154", self)

    @property
    def MachineLibrary_InsertRemove_Host204(self):
        return self.__MachineLibrary_InsertRemove_Host204

    @MachineLibrary_InsertRemove_Host204.setter
    def MachineLibrary_InsertRemove_Host204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Host__MachineLibrary_InsertRemove_Host204", None)
        self.__MachineLibrary_InsertRemove_Host204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_InsertRemove_Keywords_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Keywords_Host", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_InsertRemove_Keywords_Host", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_InsertRemove_Keywords_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Keywords_Host", None)
                    
                    setattr(item, "MachineLibrary_InsertRemove_Keywords_Host", self)
                    

    @property
    def MachineLibrary_InsertRemove_Host200(self):
        return self.__MachineLibrary_InsertRemove_Host200

    @MachineLibrary_InsertRemove_Host200.setter
    def MachineLibrary_InsertRemove_Host200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Host__MachineLibrary_InsertRemove_Host200", None)
        self.__MachineLibrary_InsertRemove_Host200 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_InsertRemove_Entry_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Entry_Host", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_InsertRemove_Entry_Host", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_InsertRemove_Entry_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Entry_Host", None)
                    
                    setattr(item, "MachineLibrary_InsertRemove_Entry_Host", self)
                    

    @property
    def MachineLibrary_InsertRemove_Host202(self):
        return self.__MachineLibrary_InsertRemove_Host202

    @MachineLibrary_InsertRemove_Host202.setter
    def MachineLibrary_InsertRemove_Host202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_InsertRemove_Host__MachineLibrary_InsertRemove_Host202", None)
        self.__MachineLibrary_InsertRemove_Host202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_InsertRemove_Types_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Types_Host", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_InsertRemove_Types_Host", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_InsertRemove_Types_Host"):
                    opp_val = getattr(item, "MachineLibrary_InsertRemove_Types_Host", None)
                    
                    setattr(item, "MachineLibrary_InsertRemove_Types_Host", self)
                    

class MachineLibrary_WS_Update_Host:

    def __init__(self, checkUnit: int, AllowUnit0: int, MachineLibrary_WS_Update_Host: "MachineLibrary_UnitConfig_Host" = None):
        self.checkUnit = checkUnit
        self.AllowUnit0 = AllowUnit0
        self.MachineLibrary_WS_Update_Host = MachineLibrary_WS_Update_Host
        
    @property
    def AllowUnit0(self) -> int:
        return self.__AllowUnit0

    @AllowUnit0.setter
    def AllowUnit0(self, AllowUnit0: int):
        self.__AllowUnit0 = AllowUnit0

    @property
    def checkUnit(self) -> int:
        return self.__checkUnit

    @checkUnit.setter
    def checkUnit(self, checkUnit: int):
        self.__checkUnit = checkUnit

    @property
    def MachineLibrary_WS_Update_Host(self):
        return self.__MachineLibrary_WS_Update_Host

    @MachineLibrary_WS_Update_Host.setter
    def MachineLibrary_WS_Update_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_WS_Update_Host__MachineLibrary_WS_Update_Host", None)
        self.__MachineLibrary_WS_Update_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Host150"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Host150", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Host150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Host150"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Host150", None)
                setattr(value, "MachineLibrary_UnitConfig_Host150", self)

class MachineLibrary_Report_Host:

    def __init__(self, note1: str, note: str, sampleMoved: int, sampleRemoved: int, sampleInsert: int, stateChanged: int, fileName: str, minType: int, maxType: int, internal: int, rawData: int, sendErrorWarningsMsgOnly: int, sendLifeMessages: int, timeStamp: int, MachineLibrary_Report_Host: "MachineLibrary_UnitConfig_Host" = None):
        self.note1 = note1
        self.note = note
        self.sampleMoved = sampleMoved
        self.sampleRemoved = sampleRemoved
        self.sampleInsert = sampleInsert
        self.stateChanged = stateChanged
        self.fileName = fileName
        self.minType = minType
        self.maxType = maxType
        self.internal = internal
        self.rawData = rawData
        self.sendErrorWarningsMsgOnly = sendErrorWarningsMsgOnly
        self.sendLifeMessages = sendLifeMessages
        self.timeStamp = timeStamp
        self.MachineLibrary_Report_Host = MachineLibrary_Report_Host
        
    @property
    def sendErrorWarningsMsgOnly(self) -> int:
        return self.__sendErrorWarningsMsgOnly

    @sendErrorWarningsMsgOnly.setter
    def sendErrorWarningsMsgOnly(self, sendErrorWarningsMsgOnly: int):
        self.__sendErrorWarningsMsgOnly = sendErrorWarningsMsgOnly

    @property
    def sampleMoved(self) -> int:
        return self.__sampleMoved

    @sampleMoved.setter
    def sampleMoved(self, sampleMoved: int):
        self.__sampleMoved = sampleMoved

    @property
    def internal(self) -> int:
        return self.__internal

    @internal.setter
    def internal(self, internal: int):
        self.__internal = internal

    @property
    def maxType(self) -> int:
        return self.__maxType

    @maxType.setter
    def maxType(self, maxType: int):
        self.__maxType = maxType

    @property
    def stateChanged(self) -> int:
        return self.__stateChanged

    @stateChanged.setter
    def stateChanged(self, stateChanged: int):
        self.__stateChanged = stateChanged

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def rawData(self) -> int:
        return self.__rawData

    @rawData.setter
    def rawData(self, rawData: int):
        self.__rawData = rawData

    @property
    def sampleRemoved(self) -> int:
        return self.__sampleRemoved

    @sampleRemoved.setter
    def sampleRemoved(self, sampleRemoved: int):
        self.__sampleRemoved = sampleRemoved

    @property
    def sampleInsert(self) -> int:
        return self.__sampleInsert

    @sampleInsert.setter
    def sampleInsert(self, sampleInsert: int):
        self.__sampleInsert = sampleInsert

    @property
    def note1(self) -> str:
        return self.__note1

    @note1.setter
    def note1(self, note1: str):
        self.__note1 = note1

    @property
    def sendLifeMessages(self) -> int:
        return self.__sendLifeMessages

    @sendLifeMessages.setter
    def sendLifeMessages(self, sendLifeMessages: int):
        self.__sendLifeMessages = sendLifeMessages

    @property
    def timeStamp(self) -> int:
        return self.__timeStamp

    @timeStamp.setter
    def timeStamp(self, timeStamp: int):
        self.__timeStamp = timeStamp

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def minType(self) -> int:
        return self.__minType

    @minType.setter
    def minType(self, minType: int):
        self.__minType = minType

    @property
    def MachineLibrary_Report_Host(self):
        return self.__MachineLibrary_Report_Host

    @MachineLibrary_Report_Host.setter
    def MachineLibrary_Report_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Report_Host__MachineLibrary_Report_Host", None)
        self.__MachineLibrary_Report_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Host148"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Host148", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Host148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Host148"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Host148", None)
                setattr(value, "MachineLibrary_UnitConfig_Host148", self)

class MachineLibrary_File_Sample_ARL_XRF_OES:

    def __init__(self, noSuccess: str, MachineLibrary_File_Sample_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None):
        self.noSuccess = noSuccess
        self.MachineLibrary_File_Sample_ARL_XRF_OES = MachineLibrary_File_Sample_ARL_XRF_OES
        
    @property
    def noSuccess(self) -> str:
        return self.__noSuccess

    @noSuccess.setter
    def noSuccess(self, noSuccess: str):
        self.__noSuccess = noSuccess

    @property
    def MachineLibrary_File_Sample_ARL_XRF_OES(self):
        return self.__MachineLibrary_File_Sample_ARL_XRF_OES

    @MachineLibrary_File_Sample_ARL_XRF_OES.setter
    def MachineLibrary_File_Sample_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_File_Sample_ARL_XRF_OES__MachineLibrary_File_Sample_ARL_XRF_OES", None)
        self.__MachineLibrary_File_Sample_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES146"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES146", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES146"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES146", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES146", self)

class MachineLibrary_PS_Process_Finished_ARL_XRF_OES:

    def __init__(self, noSuccess: str, MachineLibrary_PS_Process_Finished_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None):
        self.noSuccess = noSuccess
        self.MachineLibrary_PS_Process_Finished_ARL_XRF_OES = MachineLibrary_PS_Process_Finished_ARL_XRF_OES
        
    @property
    def noSuccess(self) -> str:
        return self.__noSuccess

    @noSuccess.setter
    def noSuccess(self, noSuccess: str):
        self.__noSuccess = noSuccess

    @property
    def MachineLibrary_PS_Process_Finished_ARL_XRF_OES(self):
        return self.__MachineLibrary_PS_Process_Finished_ARL_XRF_OES

    @MachineLibrary_PS_Process_Finished_ARL_XRF_OES.setter
    def MachineLibrary_PS_Process_Finished_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PS_Process_Finished_ARL_XRF_OES__MachineLibrary_PS_Process_Finished_ARL_XRF_OES", None)
        self.__MachineLibrary_PS_Process_Finished_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES144"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES144", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES144"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES144", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES144", self)

class MachineLibrary_GeneralSetting_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_GeneralSetting_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_GeneralSetting_ARL_XRF_OES191: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_GeneralSetting_ARL_XRF_OES = MachineLibrary_GeneralSetting_ARL_XRF_OES
        self.MachineLibrary_GeneralSetting_ARL_XRF_OES191 = MachineLibrary_GeneralSetting_ARL_XRF_OES191 if MachineLibrary_GeneralSetting_ARL_XRF_OES191 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_GeneralSetting_ARL_XRF_OES(self):
        return self.__MachineLibrary_GeneralSetting_ARL_XRF_OES

    @MachineLibrary_GeneralSetting_ARL_XRF_OES.setter
    def MachineLibrary_GeneralSetting_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_GeneralSetting_ARL_XRF_OES__MachineLibrary_GeneralSetting_ARL_XRF_OES", None)
        self.__MachineLibrary_GeneralSetting_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES142"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES142", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES142"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES142", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES142", self)

    @property
    def MachineLibrary_GeneralSetting_ARL_XRF_OES191(self):
        return self.__MachineLibrary_GeneralSetting_ARL_XRF_OES191

    @MachineLibrary_GeneralSetting_ARL_XRF_OES191.setter
    def MachineLibrary_GeneralSetting_ARL_XRF_OES191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_GeneralSetting_ARL_XRF_OES__MachineLibrary_GeneralSetting_ARL_XRF_OES191", None)
        self.__MachineLibrary_GeneralSetting_ARL_XRF_OES191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition192"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition192", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition192"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition192", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition192", self)
                    

class MachineLibrary_Settings_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_Settings_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_Settings_ARL_XRF_OES188: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_Settings_ARL_XRF_OES = MachineLibrary_Settings_ARL_XRF_OES
        self.MachineLibrary_Settings_ARL_XRF_OES188 = MachineLibrary_Settings_ARL_XRF_OES188 if MachineLibrary_Settings_ARL_XRF_OES188 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_Settings_ARL_XRF_OES(self):
        return self.__MachineLibrary_Settings_ARL_XRF_OES

    @MachineLibrary_Settings_ARL_XRF_OES.setter
    def MachineLibrary_Settings_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Settings_ARL_XRF_OES__MachineLibrary_Settings_ARL_XRF_OES", None)
        self.__MachineLibrary_Settings_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES140"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES140", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES140"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES140", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES140", self)

    @property
    def MachineLibrary_Settings_ARL_XRF_OES188(self):
        return self.__MachineLibrary_Settings_ARL_XRF_OES188

    @MachineLibrary_Settings_ARL_XRF_OES188.setter
    def MachineLibrary_Settings_ARL_XRF_OES188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Settings_ARL_XRF_OES__MachineLibrary_Settings_ARL_XRF_OES188", None)
        self.__MachineLibrary_Settings_ARL_XRF_OES188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition189"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition189", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition189"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition189", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition189", self)
                    

class MachineLibrary_DisableSCT_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_DisableSCT_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_DisableSCT_ARL_XRF_OES185: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_DisableSCT_ARL_XRF_OES = MachineLibrary_DisableSCT_ARL_XRF_OES
        self.MachineLibrary_DisableSCT_ARL_XRF_OES185 = MachineLibrary_DisableSCT_ARL_XRF_OES185 if MachineLibrary_DisableSCT_ARL_XRF_OES185 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_DisableSCT_ARL_XRF_OES185(self):
        return self.__MachineLibrary_DisableSCT_ARL_XRF_OES185

    @MachineLibrary_DisableSCT_ARL_XRF_OES185.setter
    def MachineLibrary_DisableSCT_ARL_XRF_OES185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_DisableSCT_ARL_XRF_OES__MachineLibrary_DisableSCT_ARL_XRF_OES185", None)
        self.__MachineLibrary_DisableSCT_ARL_XRF_OES185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition186"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition186", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition186"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition186", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition186", self)
                    

    @property
    def MachineLibrary_DisableSCT_ARL_XRF_OES(self):
        return self.__MachineLibrary_DisableSCT_ARL_XRF_OES

    @MachineLibrary_DisableSCT_ARL_XRF_OES.setter
    def MachineLibrary_DisableSCT_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_DisableSCT_ARL_XRF_OES__MachineLibrary_DisableSCT_ARL_XRF_OES", None)
        self.__MachineLibrary_DisableSCT_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES138"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES138", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES138", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES138"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES138", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES138", self)

class MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES = MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES
        self.MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182 = MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182 if MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(self):
        return self.__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES

    @MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES.setter
    def MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES", None)
        self.__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES136"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES136", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES136"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES136", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES136", self)

    @property
    def MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182(self):
        return self.__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182

    @MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182.setter
    def MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182", None)
        self.__MachineLibrary_ExeAskPrepUnit_ARL_XRF_OES182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition183"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition183", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition183"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition183", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition183", self)
                    

class MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES = MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES
        self.MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179 = MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179 if MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179(self):
        return self.__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179

    @MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179.setter
    def MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179", None)
        self.__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition180"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition180", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition180"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition180", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition180", self)
                    

    @property
    def MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(self):
        return self.__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES

    @MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES.setter
    def MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES", None)
        self.__MachineLibrary_CheckAskPrepUnit_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES134"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES134", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES134"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES134", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES134", self)

class MachineLibrary_ExePrepUnit_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_ExePrepUnit_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_ExePrepUnit_ARL_XRF_OES176: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_ExePrepUnit_ARL_XRF_OES = MachineLibrary_ExePrepUnit_ARL_XRF_OES
        self.MachineLibrary_ExePrepUnit_ARL_XRF_OES176 = MachineLibrary_ExePrepUnit_ARL_XRF_OES176 if MachineLibrary_ExePrepUnit_ARL_XRF_OES176 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_ExePrepUnit_ARL_XRF_OES(self):
        return self.__MachineLibrary_ExePrepUnit_ARL_XRF_OES

    @MachineLibrary_ExePrepUnit_ARL_XRF_OES.setter
    def MachineLibrary_ExePrepUnit_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExePrepUnit_ARL_XRF_OES__MachineLibrary_ExePrepUnit_ARL_XRF_OES", None)
        self.__MachineLibrary_ExePrepUnit_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES132"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES132", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES132"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES132", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES132", self)

    @property
    def MachineLibrary_ExePrepUnit_ARL_XRF_OES176(self):
        return self.__MachineLibrary_ExePrepUnit_ARL_XRF_OES176

    @MachineLibrary_ExePrepUnit_ARL_XRF_OES176.setter
    def MachineLibrary_ExePrepUnit_ARL_XRF_OES176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExePrepUnit_ARL_XRF_OES__MachineLibrary_ExePrepUnit_ARL_XRF_OES176", None)
        self.__MachineLibrary_ExePrepUnit_ARL_XRF_OES176 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition177"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition177", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition177", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition177"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition177", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition177", self)
                    

class MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES = MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES
        self.MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173 = MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173 if MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173(self):
        return self.__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173

    @MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173.setter
    def MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173", None)
        self.__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition174"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition174", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition174"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition174", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition174", self)
                    

    @property
    def MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES(self):
        return self.__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES

    @MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES.setter
    def MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES", None)
        self.__MachineLibrary_CheckReqPrepUnit_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES130"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES130", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES130"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES130", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES130", self)

class MachineLibrary_ExecuteFiling_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_ExecuteFiling_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_ExecuteFiling_ARL_XRF_OES170: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_ExecuteFiling_ARL_XRF_OES = MachineLibrary_ExecuteFiling_ARL_XRF_OES
        self.MachineLibrary_ExecuteFiling_ARL_XRF_OES170 = MachineLibrary_ExecuteFiling_ARL_XRF_OES170 if MachineLibrary_ExecuteFiling_ARL_XRF_OES170 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_ExecuteFiling_ARL_XRF_OES170(self):
        return self.__MachineLibrary_ExecuteFiling_ARL_XRF_OES170

    @MachineLibrary_ExecuteFiling_ARL_XRF_OES170.setter
    def MachineLibrary_ExecuteFiling_ARL_XRF_OES170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExecuteFiling_ARL_XRF_OES__MachineLibrary_ExecuteFiling_ARL_XRF_OES170", None)
        self.__MachineLibrary_ExecuteFiling_ARL_XRF_OES170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition171"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition171", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition171"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition171", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition171", self)
                    

    @property
    def MachineLibrary_ExecuteFiling_ARL_XRF_OES(self):
        return self.__MachineLibrary_ExecuteFiling_ARL_XRF_OES

    @MachineLibrary_ExecuteFiling_ARL_XRF_OES.setter
    def MachineLibrary_ExecuteFiling_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ExecuteFiling_ARL_XRF_OES__MachineLibrary_ExecuteFiling_ARL_XRF_OES", None)
        self.__MachineLibrary_ExecuteFiling_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES128"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES128", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES128"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES128", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES128", self)

class MachineLibrary_CheckFilling_ARL_XRF_OES:

    def __init__(self, name: str, MachineLibrary_CheckFilling_ARL_XRF_OES: "MachineLibrary_UnitConfig_ARL_XRF_OES" = None, MachineLibrary_CheckFilling_ARL_XRF_OES167: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_CheckFilling_ARL_XRF_OES = MachineLibrary_CheckFilling_ARL_XRF_OES
        self.MachineLibrary_CheckFilling_ARL_XRF_OES167 = MachineLibrary_CheckFilling_ARL_XRF_OES167 if MachineLibrary_CheckFilling_ARL_XRF_OES167 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_CheckFilling_ARL_XRF_OES(self):
        return self.__MachineLibrary_CheckFilling_ARL_XRF_OES

    @MachineLibrary_CheckFilling_ARL_XRF_OES.setter
    def MachineLibrary_CheckFilling_ARL_XRF_OES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckFilling_ARL_XRF_OES__MachineLibrary_CheckFilling_ARL_XRF_OES", None)
        self.__MachineLibrary_CheckFilling_ARL_XRF_OES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES126"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES126", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_ARL_XRF_OES126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES126"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES126", None)
                setattr(value, "MachineLibrary_UnitConfig_ARL_XRF_OES126", self)

    @property
    def MachineLibrary_CheckFilling_ARL_XRF_OES167(self):
        return self.__MachineLibrary_CheckFilling_ARL_XRF_OES167

    @MachineLibrary_CheckFilling_ARL_XRF_OES167.setter
    def MachineLibrary_CheckFilling_ARL_XRF_OES167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CheckFilling_ARL_XRF_OES__MachineLibrary_CheckFilling_ARL_XRF_OES167", None)
        self.__MachineLibrary_CheckFilling_ARL_XRF_OES167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition168"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition168", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition168"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition168", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition168", self)
                    

class MachineLibrary_CheckSample_SuperQXRF:

    pass
class MachineLibrary_CheckSampleRunTime_SuperQXRF:

    pass
class MachineLibrary_Communication_SuperQXRF:

    def __init__(self, enq_ACK_Protocol: int, MachineLibrary_Communication_SuperQXRF: "MachineLibrary_UnitConfig_SuperQ_XRF" = None):
        self.enq_ACK_Protocol = enq_ACK_Protocol
        self.MachineLibrary_Communication_SuperQXRF = MachineLibrary_Communication_SuperQXRF
        
    @property
    def enq_ACK_Protocol(self) -> int:
        return self.__enq_ACK_Protocol

    @enq_ACK_Protocol.setter
    def enq_ACK_Protocol(self, enq_ACK_Protocol: int):
        self.__enq_ACK_Protocol = enq_ACK_Protocol

    @property
    def MachineLibrary_Communication_SuperQXRF(self):
        return self.__MachineLibrary_Communication_SuperQXRF

    @MachineLibrary_Communication_SuperQXRF.setter
    def MachineLibrary_Communication_SuperQXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Communication_SuperQXRF__MachineLibrary_Communication_SuperQXRF", None)
        self.__MachineLibrary_Communication_SuperQXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF120"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF120", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF120"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF120", None)
                setattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF120", self)

class MachineLibrary_ControlSamples_SuperQXRF:

    def __init__(self, outOfControl: int, MachineLibrary_ControlSamples_SuperQXRF: "MachineLibrary_UnitConfig_SuperQ_XRF" = None):
        self.outOfControl = outOfControl
        self.MachineLibrary_ControlSamples_SuperQXRF = MachineLibrary_ControlSamples_SuperQXRF
        
    @property
    def outOfControl(self) -> int:
        return self.__outOfControl

    @outOfControl.setter
    def outOfControl(self, outOfControl: int):
        self.__outOfControl = outOfControl

    @property
    def MachineLibrary_ControlSamples_SuperQXRF(self):
        return self.__MachineLibrary_ControlSamples_SuperQXRF

    @MachineLibrary_ControlSamples_SuperQXRF.setter
    def MachineLibrary_ControlSamples_SuperQXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ControlSamples_SuperQXRF__MachineLibrary_ControlSamples_SuperQXRF", None)
        self.__MachineLibrary_ControlSamples_SuperQXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF118"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF118", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF118"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF118", None)
                setattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF118", self)

class MachineLibrary_Moved_Host:

    def __init__(self, pos0: int, type0: int, writePositionNameInFile: int, report_ALL: int, MachineLibrary_Moved_Host: "MachineLibrary_UnitConfig_Host" = None):
        self.pos0 = pos0
        self.type0 = type0
        self.writePositionNameInFile = writePositionNameInFile
        self.report_ALL = report_ALL
        self.MachineLibrary_Moved_Host = MachineLibrary_Moved_Host
        
    @property
    def pos0(self) -> int:
        return self.__pos0

    @pos0.setter
    def pos0(self, pos0: int):
        self.__pos0 = pos0

    @property
    def writePositionNameInFile(self) -> int:
        return self.__writePositionNameInFile

    @writePositionNameInFile.setter
    def writePositionNameInFile(self, writePositionNameInFile: int):
        self.__writePositionNameInFile = writePositionNameInFile

    @property
    def report_ALL(self) -> int:
        return self.__report_ALL

    @report_ALL.setter
    def report_ALL(self, report_ALL: int):
        self.__report_ALL = report_ALL

    @property
    def type0(self) -> int:
        return self.__type0

    @type0.setter
    def type0(self, type0: int):
        self.__type0 = type0

    @property
    def MachineLibrary_Moved_Host(self):
        return self.__MachineLibrary_Moved_Host

    @MachineLibrary_Moved_Host.setter
    def MachineLibrary_Moved_Host(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Moved_Host__MachineLibrary_Moved_Host", None)
        self.__MachineLibrary_Moved_Host = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Host152"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Host152", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Host152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Host152"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Host152", None)
                setattr(value, "MachineLibrary_UnitConfig_Host152", self)

class MachineLibrary_RecalRequest_OBLFOES:

    def __init__(self, name: str, MachineLibrary_RecalRequest_OBLFOES: "MachineLibrary_UnitConfig_OBLF_OES" = None, MachineLibrary_RecalRequest_OBLFOES164: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_RecalRequest_OBLFOES = MachineLibrary_RecalRequest_OBLFOES
        self.MachineLibrary_RecalRequest_OBLFOES164 = MachineLibrary_RecalRequest_OBLFOES164 if MachineLibrary_RecalRequest_OBLFOES164 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_RecalRequest_OBLFOES(self):
        return self.__MachineLibrary_RecalRequest_OBLFOES

    @MachineLibrary_RecalRequest_OBLFOES.setter
    def MachineLibrary_RecalRequest_OBLFOES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RecalRequest_OBLFOES__MachineLibrary_RecalRequest_OBLFOES", None)
        self.__MachineLibrary_RecalRequest_OBLFOES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES112"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_OBLF_OES112"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_OBLF_OES112", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_UnitConfig_OBLF_OES112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_RecalRequest_OBLFOES164(self):
        return self.__MachineLibrary_RecalRequest_OBLFOES164

    @MachineLibrary_RecalRequest_OBLFOES164.setter
    def MachineLibrary_RecalRequest_OBLFOES164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_RecalRequest_OBLFOES__MachineLibrary_RecalRequest_OBLFOES164", None)
        self.__MachineLibrary_RecalRequest_OBLFOES164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition165"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition165", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition165"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition165", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition165", self)
                    

class MachineLibrary_TestRequest_OBLFOES:

    def __init__(self, name: str, MachineLibrary_TestRequest_OBLFOES: "MachineLibrary_UnitConfig_OBLF_OES" = None, MachineLibrary_TestRequest_OBLFOES161: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_TestRequest_OBLFOES = MachineLibrary_TestRequest_OBLFOES
        self.MachineLibrary_TestRequest_OBLFOES161 = MachineLibrary_TestRequest_OBLFOES161 if MachineLibrary_TestRequest_OBLFOES161 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_TestRequest_OBLFOES(self):
        return self.__MachineLibrary_TestRequest_OBLFOES

    @MachineLibrary_TestRequest_OBLFOES.setter
    def MachineLibrary_TestRequest_OBLFOES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_TestRequest_OBLFOES__MachineLibrary_TestRequest_OBLFOES", None)
        self.__MachineLibrary_TestRequest_OBLFOES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES110"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_OBLF_OES110"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_OBLF_OES110", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_UnitConfig_OBLF_OES110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_TestRequest_OBLFOES161(self):
        return self.__MachineLibrary_TestRequest_OBLFOES161

    @MachineLibrary_TestRequest_OBLFOES161.setter
    def MachineLibrary_TestRequest_OBLFOES161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_TestRequest_OBLFOES__MachineLibrary_TestRequest_OBLFOES161", None)
        self.__MachineLibrary_TestRequest_OBLFOES161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition162"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition162", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition162"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition162", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition162", self)
                    

class MachineLibrary_OutputRequest_OBLFOES:

    def __init__(self, name: str, MachineLibrary_OutputRequest_OBLFOES: "MachineLibrary_UnitConfig_OBLF_OES" = None, MachineLibrary_OutputRequest_OBLFOES159: set["MachineLibrary_OES_XRF_Condition"] = None):
        self.name = name
        self.MachineLibrary_OutputRequest_OBLFOES = MachineLibrary_OutputRequest_OBLFOES
        self.MachineLibrary_OutputRequest_OBLFOES159 = MachineLibrary_OutputRequest_OBLFOES159 if MachineLibrary_OutputRequest_OBLFOES159 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def MachineLibrary_OutputRequest_OBLFOES(self):
        return self.__MachineLibrary_OutputRequest_OBLFOES

    @MachineLibrary_OutputRequest_OBLFOES.setter
    def MachineLibrary_OutputRequest_OBLFOES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OutputRequest_OBLFOES__MachineLibrary_OutputRequest_OBLFOES", None)
        self.__MachineLibrary_OutputRequest_OBLFOES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES108"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES108", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_OBLF_OES108"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_OBLF_OES108", None)
                setattr(value, "MachineLibrary_UnitConfig_OBLF_OES108", self)

    @property
    def MachineLibrary_OutputRequest_OBLFOES159(self):
        return self.__MachineLibrary_OutputRequest_OBLFOES159

    @MachineLibrary_OutputRequest_OBLFOES159.setter
    def MachineLibrary_OutputRequest_OBLFOES159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_OutputRequest_OBLFOES__MachineLibrary_OutputRequest_OBLFOES159", None)
        self.__MachineLibrary_OutputRequest_OBLFOES159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_OES_XRF_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_OES_XRF_Condition"):
                    opp_val = getattr(item, "MachineLibrary_OES_XRF_Condition", None)
                    
                    setattr(item, "MachineLibrary_OES_XRF_Condition", self)
                    

class MachineLibrary_Translate_Terminal:

    def __init__(self, auto_Ready: str, auto_Busy: str, man_Ready: str, man_Busy: str, MachineLibrary_Translate_Terminal: "MachineLibrary_UnitConfig_Terminal" = None):
        self.auto_Ready = auto_Ready
        self.auto_Busy = auto_Busy
        self.man_Ready = man_Ready
        self.man_Busy = man_Busy
        self.MachineLibrary_Translate_Terminal = MachineLibrary_Translate_Terminal
        
    @property
    def man_Busy(self) -> str:
        return self.__man_Busy

    @man_Busy.setter
    def man_Busy(self, man_Busy: str):
        self.__man_Busy = man_Busy

    @property
    def man_Ready(self) -> str:
        return self.__man_Ready

    @man_Ready.setter
    def man_Ready(self, man_Ready: str):
        self.__man_Ready = man_Ready

    @property
    def auto_Busy(self) -> str:
        return self.__auto_Busy

    @auto_Busy.setter
    def auto_Busy(self, auto_Busy: str):
        self.__auto_Busy = auto_Busy

    @property
    def auto_Ready(self) -> str:
        return self.__auto_Ready

    @auto_Ready.setter
    def auto_Ready(self, auto_Ready: str):
        self.__auto_Ready = auto_Ready

    @property
    def MachineLibrary_Translate_Terminal(self):
        return self.__MachineLibrary_Translate_Terminal

    @MachineLibrary_Translate_Terminal.setter
    def MachineLibrary_Translate_Terminal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Translate_Terminal__MachineLibrary_Translate_Terminal", None)
        self.__MachineLibrary_Translate_Terminal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_Terminal106"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_Terminal106", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_Terminal106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_Terminal106"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_Terminal106", None)
                setattr(value, "MachineLibrary_UnitConfig_Terminal106", self)

class MachineLibrary_CheckAddSID_PM2PM:

    pass
class MachineLibrary_SepByComma_Scanner:

    def __init__(self, activ: int, preDefWS: int, MachineLibrary_SepByComma_Scanner: "MachineLibrary_UnitSpecialConfiguration" = None, MachineLibrary_SepByComma_Scanner206: set["MachineLibrary_SepByComma_Field_Scanner"] = None, MachineLibrary_SepByComma_Scanner208: set["MachineLibrary_SepByComma_ID_Scanner"] = None):
        self.activ = activ
        self.preDefWS = preDefWS
        self.MachineLibrary_SepByComma_Scanner = MachineLibrary_SepByComma_Scanner
        self.MachineLibrary_SepByComma_Scanner206 = MachineLibrary_SepByComma_Scanner206 if MachineLibrary_SepByComma_Scanner206 is not None else set()
        self.MachineLibrary_SepByComma_Scanner208 = MachineLibrary_SepByComma_Scanner208 if MachineLibrary_SepByComma_Scanner208 is not None else set()
        
    @property
    def preDefWS(self) -> int:
        return self.__preDefWS

    @preDefWS.setter
    def preDefWS(self, preDefWS: int):
        self.__preDefWS = preDefWS

    @property
    def activ(self) -> int:
        return self.__activ

    @activ.setter
    def activ(self, activ: int):
        self.__activ = activ

    @property
    def MachineLibrary_SepByComma_Scanner208(self):
        return self.__MachineLibrary_SepByComma_Scanner208

    @MachineLibrary_SepByComma_Scanner208.setter
    def MachineLibrary_SepByComma_Scanner208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_SepByComma_Scanner__MachineLibrary_SepByComma_Scanner208", None)
        self.__MachineLibrary_SepByComma_Scanner208 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_SepByComma_ID_Scanner"):
                    opp_val = getattr(item, "MachineLibrary_SepByComma_ID_Scanner", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_SepByComma_ID_Scanner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_SepByComma_ID_Scanner"):
                    opp_val = getattr(item, "MachineLibrary_SepByComma_ID_Scanner", None)
                    
                    setattr(item, "MachineLibrary_SepByComma_ID_Scanner", self)
                    

    @property
    def MachineLibrary_SepByComma_Scanner206(self):
        return self.__MachineLibrary_SepByComma_Scanner206

    @MachineLibrary_SepByComma_Scanner206.setter
    def MachineLibrary_SepByComma_Scanner206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_SepByComma_Scanner__MachineLibrary_SepByComma_Scanner206", None)
        self.__MachineLibrary_SepByComma_Scanner206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_SepByComma_Field_Scanner"):
                    opp_val = getattr(item, "MachineLibrary_SepByComma_Field_Scanner", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_SepByComma_Field_Scanner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_SepByComma_Field_Scanner"):
                    opp_val = getattr(item, "MachineLibrary_SepByComma_Field_Scanner", None)
                    
                    setattr(item, "MachineLibrary_SepByComma_Field_Scanner", self)
                    

    @property
    def MachineLibrary_SepByComma_Scanner(self):
        return self.__MachineLibrary_SepByComma_Scanner

    @MachineLibrary_SepByComma_Scanner.setter
    def MachineLibrary_SepByComma_Scanner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_SepByComma_Scanner__MachineLibrary_SepByComma_Scanner", None)
        self.__MachineLibrary_SepByComma_Scanner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitSpecialConfiguration102"):
                opp_val = getattr(old_value, "MachineLibrary_UnitSpecialConfiguration102", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitSpecialConfiguration102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitSpecialConfiguration102"):
                opp_val = getattr(value, "MachineLibrary_UnitSpecialConfiguration102", None)
                setattr(value, "MachineLibrary_UnitSpecialConfiguration102", self)

class MachineLibrary_History_AccuPycMeter:

    pass
class MachineLibrary_UnitConfig_Host:

    pass
class MachineLibrary_UnitConfig_ARL_XRF_OES:

    pass
class MachineLibrary_UnitConfig_SuperQ_XRF:

    pass
class MachineLibrary_UnitConfig_OBLF_OES:

    pass
class MachineLibrary_UnitConfig_Terminal:

    pass
class MachineLibrary_GeneralParameter_SuperQXRF:

    def __init__(self, switchRemote: str, startList: str, listName: str, MachineLibrary_GeneralParameter_SuperQXRF: "MachineLibrary_UnitConfig_SuperQ_XRF" = None):
        self.switchRemote = switchRemote
        self.startList = startList
        self.listName = listName
        self.MachineLibrary_GeneralParameter_SuperQXRF = MachineLibrary_GeneralParameter_SuperQXRF
        
    @property
    def listName(self) -> str:
        return self.__listName

    @listName.setter
    def listName(self, listName: str):
        self.__listName = listName

    @property
    def startList(self) -> str:
        return self.__startList

    @startList.setter
    def startList(self, startList: str):
        self.__startList = startList

    @property
    def switchRemote(self) -> str:
        return self.__switchRemote

    @switchRemote.setter
    def switchRemote(self, switchRemote: str):
        self.__switchRemote = switchRemote

    @property
    def MachineLibrary_GeneralParameter_SuperQXRF(self):
        return self.__MachineLibrary_GeneralParameter_SuperQXRF

    @MachineLibrary_GeneralParameter_SuperQXRF.setter
    def MachineLibrary_GeneralParameter_SuperQXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_GeneralParameter_SuperQXRF__MachineLibrary_GeneralParameter_SuperQXRF", None)
        self.__MachineLibrary_GeneralParameter_SuperQXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF116"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF116", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_SuperQ_XRF116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF116"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF116", None)
                setattr(value, "MachineLibrary_UnitConfig_SuperQ_XRF116", self)

class MachineLibrary_ErrorMessage_OBLFOES:

    def __init__(self, errorMessage: str, MachineLibrary_ErrorMessage_OBLFOES: "MachineLibrary_UnitConfig_OBLF_OES" = None):
        self.errorMessage = errorMessage
        self.MachineLibrary_ErrorMessage_OBLFOES = MachineLibrary_ErrorMessage_OBLFOES
        
    @property
    def errorMessage(self) -> str:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, errorMessage: str):
        self.__errorMessage = errorMessage

    @property
    def MachineLibrary_ErrorMessage_OBLFOES(self):
        return self.__MachineLibrary_ErrorMessage_OBLFOES

    @MachineLibrary_ErrorMessage_OBLFOES.setter
    def MachineLibrary_ErrorMessage_OBLFOES(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_ErrorMessage_OBLFOES__MachineLibrary_ErrorMessage_OBLFOES", None)
        self.__MachineLibrary_ErrorMessage_OBLFOES = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES114"):
                opp_val = getattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES114", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitConfig_OBLF_OES114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitConfig_OBLF_OES114"):
                opp_val = getattr(value, "MachineLibrary_UnitConfig_OBLF_OES114", None)
                setattr(value, "MachineLibrary_UnitConfig_OBLF_OES114", self)

class MachineLibrary_UnitGeneral_Scanner:

    def __init__(self, forcedSampleType: int, registerSample: int, start: int, length: int, fillWith: str, addString: str, preString: str, MachineLibrary_UnitGeneral_Scanner: "MachineLibrary_UnitGeneralSpecial" = None):
        self.forcedSampleType = forcedSampleType
        self.registerSample = registerSample
        self.start = start
        self.length = length
        self.fillWith = fillWith
        self.addString = addString
        self.preString = preString
        self.MachineLibrary_UnitGeneral_Scanner = MachineLibrary_UnitGeneral_Scanner
        
    @property
    def fillWith(self) -> str:
        return self.__fillWith

    @fillWith.setter
    def fillWith(self, fillWith: str):
        self.__fillWith = fillWith

    @property
    def registerSample(self) -> int:
        return self.__registerSample

    @registerSample.setter
    def registerSample(self, registerSample: int):
        self.__registerSample = registerSample

    @property
    def preString(self) -> str:
        return self.__preString

    @preString.setter
    def preString(self, preString: str):
        self.__preString = preString

    @property
    def addString(self) -> str:
        return self.__addString

    @addString.setter
    def addString(self, addString: str):
        self.__addString = addString

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def forcedSampleType(self) -> int:
        return self.__forcedSampleType

    @forcedSampleType.setter
    def forcedSampleType(self, forcedSampleType: int):
        self.__forcedSampleType = forcedSampleType

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def MachineLibrary_UnitGeneral_Scanner(self):
        return self.__MachineLibrary_UnitGeneral_Scanner

    @MachineLibrary_UnitGeneral_Scanner.setter
    def MachineLibrary_UnitGeneral_Scanner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_Scanner__MachineLibrary_UnitGeneral_Scanner", None)
        self.__MachineLibrary_UnitGeneral_Scanner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial88"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial88", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial88"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial88", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial88", self)

class MachineLibrary_UnitGeneral_RigakuXRF:

    def __init__(self, lastPoHAG_SIInstrument: int, lastPosAnalyHAG_SIg: int, lastPosInInstrument: int, separator: int, MachineLibrary_UnitGeneral_RigakuXRF: "MachineLibrary_UnitGeneralSpecial" = None):
        self.lastPoHAG_SIInstrument = lastPoHAG_SIInstrument
        self.lastPosAnalyHAG_SIg = lastPosAnalyHAG_SIg
        self.lastPosInInstrument = lastPosInInstrument
        self.separator = separator
        self.MachineLibrary_UnitGeneral_RigakuXRF = MachineLibrary_UnitGeneral_RigakuXRF
        
    @property
    def lastPosAnalyHAG_SIg(self) -> int:
        return self.__lastPosAnalyHAG_SIg

    @lastPosAnalyHAG_SIg.setter
    def lastPosAnalyHAG_SIg(self, lastPosAnalyHAG_SIg: int):
        self.__lastPosAnalyHAG_SIg = lastPosAnalyHAG_SIg

    @property
    def lastPoHAG_SIInstrument(self) -> int:
        return self.__lastPoHAG_SIInstrument

    @lastPoHAG_SIInstrument.setter
    def lastPoHAG_SIInstrument(self, lastPoHAG_SIInstrument: int):
        self.__lastPoHAG_SIInstrument = lastPoHAG_SIInstrument

    @property
    def separator(self) -> int:
        return self.__separator

    @separator.setter
    def separator(self, separator: int):
        self.__separator = separator

    @property
    def lastPosInInstrument(self) -> int:
        return self.__lastPosInInstrument

    @lastPosInInstrument.setter
    def lastPosInInstrument(self, lastPosInInstrument: int):
        self.__lastPosInInstrument = lastPosInInstrument

    @property
    def MachineLibrary_UnitGeneral_RigakuXRF(self):
        return self.__MachineLibrary_UnitGeneral_RigakuXRF

    @MachineLibrary_UnitGeneral_RigakuXRF.setter
    def MachineLibrary_UnitGeneral_RigakuXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_RigakuXRF__MachineLibrary_UnitGeneral_RigakuXRF", None)
        self.__MachineLibrary_UnitGeneral_RigakuXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial86"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial86", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial86"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial86", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial86", self)

class MachineLibrary_UnitGeneral_SuperQ:

    def __init__(self, lastPosInInstrument: int, lastPosAnalysing: int, MachineLibrary_UnitGeneral_SuperQ: "MachineLibrary_UnitGeneralSpecial" = None):
        self.lastPosInInstrument = lastPosInInstrument
        self.lastPosAnalysing = lastPosAnalysing
        self.MachineLibrary_UnitGeneral_SuperQ = MachineLibrary_UnitGeneral_SuperQ
        
    @property
    def lastPosAnalysing(self) -> int:
        return self.__lastPosAnalysing

    @lastPosAnalysing.setter
    def lastPosAnalysing(self, lastPosAnalysing: int):
        self.__lastPosAnalysing = lastPosAnalysing

    @property
    def lastPosInInstrument(self) -> int:
        return self.__lastPosInInstrument

    @lastPosInInstrument.setter
    def lastPosInInstrument(self, lastPosInInstrument: int):
        self.__lastPosInInstrument = lastPosInInstrument

    @property
    def MachineLibrary_UnitGeneral_SuperQ(self):
        return self.__MachineLibrary_UnitGeneral_SuperQ

    @MachineLibrary_UnitGeneral_SuperQ.setter
    def MachineLibrary_UnitGeneral_SuperQ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_SuperQ__MachineLibrary_UnitGeneral_SuperQ", None)
        self.__MachineLibrary_UnitGeneral_SuperQ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial84"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial84", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial84"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial84", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial84", self)

class MachineLibrary_UnitGeneral_AccPyc:

    def __init__(self, cupWeight: float, minSampleWeight: float, MachineLibrary_UnitGeneral_AccPyc: "MachineLibrary_UnitGeneralSpecial" = None):
        self.cupWeight = cupWeight
        self.minSampleWeight = minSampleWeight
        self.MachineLibrary_UnitGeneral_AccPyc = MachineLibrary_UnitGeneral_AccPyc
        
    @property
    def cupWeight(self) -> float:
        return self.__cupWeight

    @cupWeight.setter
    def cupWeight(self, cupWeight: float):
        self.__cupWeight = cupWeight

    @property
    def minSampleWeight(self) -> float:
        return self.__minSampleWeight

    @minSampleWeight.setter
    def minSampleWeight(self, minSampleWeight: float):
        self.__minSampleWeight = minSampleWeight

    @property
    def MachineLibrary_UnitGeneral_AccPyc(self):
        return self.__MachineLibrary_UnitGeneral_AccPyc

    @MachineLibrary_UnitGeneral_AccPyc.setter
    def MachineLibrary_UnitGeneral_AccPyc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_AccPyc__MachineLibrary_UnitGeneral_AccPyc", None)
        self.__MachineLibrary_UnitGeneral_AccPyc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial82"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial82", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial82"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial82", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial82", self)

class MachineLibrary_UnitGeneral_PM2PM:

    def __init__(self, sid_Mask: str, processFeedBack: str, MachineLibrary_UnitGeneral_PM2PM: "MachineLibrary_UnitGeneralSpecial" = None):
        self.sid_Mask = sid_Mask
        self.processFeedBack = processFeedBack
        self.MachineLibrary_UnitGeneral_PM2PM = MachineLibrary_UnitGeneral_PM2PM
        
    @property
    def sid_Mask(self) -> str:
        return self.__sid_Mask

    @sid_Mask.setter
    def sid_Mask(self, sid_Mask: str):
        self.__sid_Mask = sid_Mask

    @property
    def processFeedBack(self) -> str:
        return self.__processFeedBack

    @processFeedBack.setter
    def processFeedBack(self, processFeedBack: str):
        self.__processFeedBack = processFeedBack

    @property
    def MachineLibrary_UnitGeneral_PM2PM(self):
        return self.__MachineLibrary_UnitGeneral_PM2PM

    @MachineLibrary_UnitGeneral_PM2PM.setter
    def MachineLibrary_UnitGeneral_PM2PM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_PM2PM__MachineLibrary_UnitGeneral_PM2PM", None)
        self.__MachineLibrary_UnitGeneral_PM2PM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial80"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial80", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial80"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial80", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial80", self)

class MachineLibrary_UnitGeneral_Remote:

    def __init__(self, editWSDB: bool, handshakeT: int, handshakeQ: str, handshakeA: str, MachineLibrary_UnitGeneral_Remote: "MachineLibrary_UnitGeneralSpecial" = None):
        self.editWSDB = editWSDB
        self.handshakeT = handshakeT
        self.handshakeQ = handshakeQ
        self.handshakeA = handshakeA
        self.MachineLibrary_UnitGeneral_Remote = MachineLibrary_UnitGeneral_Remote
        
    @property
    def editWSDB(self) -> bool:
        return self.__editWSDB

    @editWSDB.setter
    def editWSDB(self, editWSDB: bool):
        self.__editWSDB = editWSDB

    @property
    def handshakeA(self) -> str:
        return self.__handshakeA

    @handshakeA.setter
    def handshakeA(self, handshakeA: str):
        self.__handshakeA = handshakeA

    @property
    def handshakeT(self) -> int:
        return self.__handshakeT

    @handshakeT.setter
    def handshakeT(self, handshakeT: int):
        self.__handshakeT = handshakeT

    @property
    def handshakeQ(self) -> str:
        return self.__handshakeQ

    @handshakeQ.setter
    def handshakeQ(self, handshakeQ: str):
        self.__handshakeQ = handshakeQ

    @property
    def MachineLibrary_UnitGeneral_Remote(self):
        return self.__MachineLibrary_UnitGeneral_Remote

    @MachineLibrary_UnitGeneral_Remote.setter
    def MachineLibrary_UnitGeneral_Remote(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_Remote__MachineLibrary_UnitGeneral_Remote", None)
        self.__MachineLibrary_UnitGeneral_Remote = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial78"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial78", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial78"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial78", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial78", self)

class MachineLibrary_UnitGeneral_HostPC:

    def __init__(self, maxIndex: int, index: int, replyOnLink: int, writeDumyIfNoDataExist: int, MachineLibrary_UnitGeneral_HostPC: "MachineLibrary_UnitGeneralSpecial" = None):
        self.maxIndex = maxIndex
        self.index = index
        self.replyOnLink = replyOnLink
        self.writeDumyIfNoDataExist = writeDumyIfNoDataExist
        self.MachineLibrary_UnitGeneral_HostPC = MachineLibrary_UnitGeneral_HostPC
        
    @property
    def replyOnLink(self) -> int:
        return self.__replyOnLink

    @replyOnLink.setter
    def replyOnLink(self, replyOnLink: int):
        self.__replyOnLink = replyOnLink

    @property
    def writeDumyIfNoDataExist(self) -> int:
        return self.__writeDumyIfNoDataExist

    @writeDumyIfNoDataExist.setter
    def writeDumyIfNoDataExist(self, writeDumyIfNoDataExist: int):
        self.__writeDumyIfNoDataExist = writeDumyIfNoDataExist

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, index: int):
        self.__index = index

    @property
    def maxIndex(self) -> int:
        return self.__maxIndex

    @maxIndex.setter
    def maxIndex(self, maxIndex: int):
        self.__maxIndex = maxIndex

    @property
    def MachineLibrary_UnitGeneral_HostPC(self):
        return self.__MachineLibrary_UnitGeneral_HostPC

    @MachineLibrary_UnitGeneral_HostPC.setter
    def MachineLibrary_UnitGeneral_HostPC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_HostPC__MachineLibrary_UnitGeneral_HostPC", None)
        self.__MachineLibrary_UnitGeneral_HostPC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial76"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial76", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial76"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial76", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial76", self)

class MachineLibrary_UnitGeneral_Terminal:

    def __init__(self, thisStation: str, station1: str, station2: str, station3: str, station4: str, station5: str, MachineLibrary_UnitGeneral_Terminal: "MachineLibrary_UnitGeneralSpecial" = None):
        self.thisStation = thisStation
        self.station1 = station1
        self.station2 = station2
        self.station3 = station3
        self.station4 = station4
        self.station5 = station5
        self.MachineLibrary_UnitGeneral_Terminal = MachineLibrary_UnitGeneral_Terminal
        
    @property
    def station5(self) -> str:
        return self.__station5

    @station5.setter
    def station5(self, station5: str):
        self.__station5 = station5

    @property
    def station3(self) -> str:
        return self.__station3

    @station3.setter
    def station3(self, station3: str):
        self.__station3 = station3

    @property
    def thisStation(self) -> str:
        return self.__thisStation

    @thisStation.setter
    def thisStation(self, thisStation: str):
        self.__thisStation = thisStation

    @property
    def station4(self) -> str:
        return self.__station4

    @station4.setter
    def station4(self, station4: str):
        self.__station4 = station4

    @property
    def station1(self) -> str:
        return self.__station1

    @station1.setter
    def station1(self, station1: str):
        self.__station1 = station1

    @property
    def station2(self) -> str:
        return self.__station2

    @station2.setter
    def station2(self, station2: str):
        self.__station2 = station2

    @property
    def MachineLibrary_UnitGeneral_Terminal(self):
        return self.__MachineLibrary_UnitGeneral_Terminal

    @MachineLibrary_UnitGeneral_Terminal.setter
    def MachineLibrary_UnitGeneral_Terminal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneral_Terminal__MachineLibrary_UnitGeneral_Terminal", None)
        self.__MachineLibrary_UnitGeneral_Terminal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial74"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial74", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial74"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial74", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial74", self)

class MachineLibrary_UnitGeneralParameters:

    def __init__(self, KeyWord_1: str, UseWith_1: str, seq_X: int, paraName_1: str, comment_1: str, unit_1: str, minValue_1: int, maxValue_1: int, defaultValue_1: int, visibleType_1: int, canBeChange_1: int, MachineLibrary_UnitGeneralParameters: "MachineLibrary_UnitGeneral" = None):
        self.KeyWord_1 = KeyWord_1
        self.UseWith_1 = UseWith_1
        self.seq_X = seq_X
        self.paraName_1 = paraName_1
        self.comment_1 = comment_1
        self.unit_1 = unit_1
        self.minValue_1 = minValue_1
        self.maxValue_1 = maxValue_1
        self.defaultValue_1 = defaultValue_1
        self.visibleType_1 = visibleType_1
        self.canBeChange_1 = canBeChange_1
        self.MachineLibrary_UnitGeneralParameters = MachineLibrary_UnitGeneralParameters
        
    @property
    def visibleType_1(self) -> int:
        return self.__visibleType_1

    @visibleType_1.setter
    def visibleType_1(self, visibleType_1: int):
        self.__visibleType_1 = visibleType_1

    @property
    def KeyWord_1(self) -> str:
        return self.__KeyWord_1

    @KeyWord_1.setter
    def KeyWord_1(self, KeyWord_1: str):
        self.__KeyWord_1 = KeyWord_1

    @property
    def UseWith_1(self) -> str:
        return self.__UseWith_1

    @UseWith_1.setter
    def UseWith_1(self, UseWith_1: str):
        self.__UseWith_1 = UseWith_1

    @property
    def seq_X(self) -> int:
        return self.__seq_X

    @seq_X.setter
    def seq_X(self, seq_X: int):
        self.__seq_X = seq_X

    @property
    def maxValue_1(self) -> int:
        return self.__maxValue_1

    @maxValue_1.setter
    def maxValue_1(self, maxValue_1: int):
        self.__maxValue_1 = maxValue_1

    @property
    def defaultValue_1(self) -> int:
        return self.__defaultValue_1

    @defaultValue_1.setter
    def defaultValue_1(self, defaultValue_1: int):
        self.__defaultValue_1 = defaultValue_1

    @property
    def unit_1(self) -> str:
        return self.__unit_1

    @unit_1.setter
    def unit_1(self, unit_1: str):
        self.__unit_1 = unit_1

    @property
    def minValue_1(self) -> int:
        return self.__minValue_1

    @minValue_1.setter
    def minValue_1(self, minValue_1: int):
        self.__minValue_1 = minValue_1

    @property
    def comment_1(self) -> str:
        return self.__comment_1

    @comment_1.setter
    def comment_1(self, comment_1: str):
        self.__comment_1 = comment_1

    @property
    def canBeChange_1(self) -> int:
        return self.__canBeChange_1

    @canBeChange_1.setter
    def canBeChange_1(self, canBeChange_1: int):
        self.__canBeChange_1 = canBeChange_1

    @property
    def paraName_1(self) -> str:
        return self.__paraName_1

    @paraName_1.setter
    def paraName_1(self, paraName_1: str):
        self.__paraName_1 = paraName_1

    @property
    def MachineLibrary_UnitGeneralParameters(self):
        return self.__MachineLibrary_UnitGeneralParameters

    @MachineLibrary_UnitGeneralParameters.setter
    def MachineLibrary_UnitGeneralParameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_UnitGeneralParameters__MachineLibrary_UnitGeneralParameters", None)
        self.__MachineLibrary_UnitGeneralParameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneral72"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneral72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneral72"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneral72", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_UnitGeneral72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_UnitSpecialConfiguration:

    pass
class MachineLibrary_UnitGeneralSpecial:

    pass
class MachineLibrary_UnitGeneral:

    pass
class MachineLibrary_Buttons:

    pass
class MachineLibrary_UnitPrograms:

    pass
class MachineLibrary_PLCtoPmMatrix:

    def __init__(self, plcpmmatrixBit0: int, plcpmmatrixBit1: int, plcpmmatrixBit2: int, plcpmmatrixBit3: int, plcpmmatrixBit4: int, plcpmmatrixBit5: int, plcpmmatrixBit6: int, plcpmmatrixBit7: int, plcpmmatrixBit8: int, plcpmmatrixBit9: int, plcpmmatrixBit11: int, plcpmmatrixBit10: int, plcpmmatrixBit12: int, plcpmmatrixBit13: int, plcpmmatrixBit14: int, plcpmmatrixBit15: int, MachineLibrary_PLCtoPmMatrix: "MachineLibrary_Units" = None):
        self.plcpmmatrixBit0 = plcpmmatrixBit0
        self.plcpmmatrixBit1 = plcpmmatrixBit1
        self.plcpmmatrixBit2 = plcpmmatrixBit2
        self.plcpmmatrixBit3 = plcpmmatrixBit3
        self.plcpmmatrixBit4 = plcpmmatrixBit4
        self.plcpmmatrixBit5 = plcpmmatrixBit5
        self.plcpmmatrixBit6 = plcpmmatrixBit6
        self.plcpmmatrixBit7 = plcpmmatrixBit7
        self.plcpmmatrixBit8 = plcpmmatrixBit8
        self.plcpmmatrixBit9 = plcpmmatrixBit9
        self.plcpmmatrixBit11 = plcpmmatrixBit11
        self.plcpmmatrixBit10 = plcpmmatrixBit10
        self.plcpmmatrixBit12 = plcpmmatrixBit12
        self.plcpmmatrixBit13 = plcpmmatrixBit13
        self.plcpmmatrixBit14 = plcpmmatrixBit14
        self.plcpmmatrixBit15 = plcpmmatrixBit15
        self.MachineLibrary_PLCtoPmMatrix = MachineLibrary_PLCtoPmMatrix
        
    @property
    def plcpmmatrixBit13(self) -> int:
        return self.__plcpmmatrixBit13

    @plcpmmatrixBit13.setter
    def plcpmmatrixBit13(self, plcpmmatrixBit13: int):
        self.__plcpmmatrixBit13 = plcpmmatrixBit13

    @property
    def plcpmmatrixBit8(self) -> int:
        return self.__plcpmmatrixBit8

    @plcpmmatrixBit8.setter
    def plcpmmatrixBit8(self, plcpmmatrixBit8: int):
        self.__plcpmmatrixBit8 = plcpmmatrixBit8

    @property
    def plcpmmatrixBit10(self) -> int:
        return self.__plcpmmatrixBit10

    @plcpmmatrixBit10.setter
    def plcpmmatrixBit10(self, plcpmmatrixBit10: int):
        self.__plcpmmatrixBit10 = plcpmmatrixBit10

    @property
    def plcpmmatrixBit11(self) -> int:
        return self.__plcpmmatrixBit11

    @plcpmmatrixBit11.setter
    def plcpmmatrixBit11(self, plcpmmatrixBit11: int):
        self.__plcpmmatrixBit11 = plcpmmatrixBit11

    @property
    def plcpmmatrixBit1(self) -> int:
        return self.__plcpmmatrixBit1

    @plcpmmatrixBit1.setter
    def plcpmmatrixBit1(self, plcpmmatrixBit1: int):
        self.__plcpmmatrixBit1 = plcpmmatrixBit1

    @property
    def plcpmmatrixBit9(self) -> int:
        return self.__plcpmmatrixBit9

    @plcpmmatrixBit9.setter
    def plcpmmatrixBit9(self, plcpmmatrixBit9: int):
        self.__plcpmmatrixBit9 = plcpmmatrixBit9

    @property
    def plcpmmatrixBit14(self) -> int:
        return self.__plcpmmatrixBit14

    @plcpmmatrixBit14.setter
    def plcpmmatrixBit14(self, plcpmmatrixBit14: int):
        self.__plcpmmatrixBit14 = plcpmmatrixBit14

    @property
    def plcpmmatrixBit12(self) -> int:
        return self.__plcpmmatrixBit12

    @plcpmmatrixBit12.setter
    def plcpmmatrixBit12(self, plcpmmatrixBit12: int):
        self.__plcpmmatrixBit12 = plcpmmatrixBit12

    @property
    def plcpmmatrixBit0(self) -> int:
        return self.__plcpmmatrixBit0

    @plcpmmatrixBit0.setter
    def plcpmmatrixBit0(self, plcpmmatrixBit0: int):
        self.__plcpmmatrixBit0 = plcpmmatrixBit0

    @property
    def plcpmmatrixBit5(self) -> int:
        return self.__plcpmmatrixBit5

    @plcpmmatrixBit5.setter
    def plcpmmatrixBit5(self, plcpmmatrixBit5: int):
        self.__plcpmmatrixBit5 = plcpmmatrixBit5

    @property
    def plcpmmatrixBit2(self) -> int:
        return self.__plcpmmatrixBit2

    @plcpmmatrixBit2.setter
    def plcpmmatrixBit2(self, plcpmmatrixBit2: int):
        self.__plcpmmatrixBit2 = plcpmmatrixBit2

    @property
    def plcpmmatrixBit6(self) -> int:
        return self.__plcpmmatrixBit6

    @plcpmmatrixBit6.setter
    def plcpmmatrixBit6(self, plcpmmatrixBit6: int):
        self.__plcpmmatrixBit6 = plcpmmatrixBit6

    @property
    def plcpmmatrixBit7(self) -> int:
        return self.__plcpmmatrixBit7

    @plcpmmatrixBit7.setter
    def plcpmmatrixBit7(self, plcpmmatrixBit7: int):
        self.__plcpmmatrixBit7 = plcpmmatrixBit7

    @property
    def plcpmmatrixBit4(self) -> int:
        return self.__plcpmmatrixBit4

    @plcpmmatrixBit4.setter
    def plcpmmatrixBit4(self, plcpmmatrixBit4: int):
        self.__plcpmmatrixBit4 = plcpmmatrixBit4

    @property
    def plcpmmatrixBit15(self) -> int:
        return self.__plcpmmatrixBit15

    @plcpmmatrixBit15.setter
    def plcpmmatrixBit15(self, plcpmmatrixBit15: int):
        self.__plcpmmatrixBit15 = plcpmmatrixBit15

    @property
    def plcpmmatrixBit3(self) -> int:
        return self.__plcpmmatrixBit3

    @plcpmmatrixBit3.setter
    def plcpmmatrixBit3(self, plcpmmatrixBit3: int):
        self.__plcpmmatrixBit3 = plcpmmatrixBit3

    @property
    def MachineLibrary_PLCtoPmMatrix(self):
        return self.__MachineLibrary_PLCtoPmMatrix

    @MachineLibrary_PLCtoPmMatrix.setter
    def MachineLibrary_PLCtoPmMatrix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PLCtoPmMatrix__MachineLibrary_PLCtoPmMatrix", None)
        self.__MachineLibrary_PLCtoPmMatrix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Units60"):
                opp_val = getattr(old_value, "MachineLibrary_Units60", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Units60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Units60"):
                opp_val = getattr(value, "MachineLibrary_Units60", None)
                setattr(value, "MachineLibrary_Units60", self)

class MachineLibrary_StausBits:

    pass
class MachineLibrary_Positions:

    pass
class MachineLibrary_WinCCAddTag:

    def __init__(self, winCCTag: str, MachineLibrary_WinCCAddTag: "MachineLibrary_NodeGeneral_WinCC2WinCC" = None):
        self.winCCTag = winCCTag
        self.MachineLibrary_WinCCAddTag = MachineLibrary_WinCCAddTag
        
    @property
    def winCCTag(self) -> str:
        return self.__winCCTag

    @winCCTag.setter
    def winCCTag(self, winCCTag: str):
        self.__winCCTag = winCCTag

    @property
    def MachineLibrary_WinCCAddTag(self):
        return self.__MachineLibrary_WinCCAddTag

    @MachineLibrary_WinCCAddTag.setter
    def MachineLibrary_WinCCAddTag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_WinCCAddTag__MachineLibrary_WinCCAddTag", None)
        self.__MachineLibrary_WinCCAddTag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneral_WinCC2WinCC54"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneral_WinCC2WinCC54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneral_WinCC2WinCC54"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneral_WinCC2WinCC54", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_NodeGeneral_WinCC2WinCC54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_NodeGeneral_WinCC2WinCC:

    def __init__(self, prefix: str, MachineLibrary_NodeGeneral_WinCC2WinCC: "MachineLibrary_NodeGeneralSpecial" = None, MachineLibrary_NodeGeneral_WinCC2WinCC54: set["MachineLibrary_WinCCAddTag"] = None):
        self.prefix = prefix
        self.MachineLibrary_NodeGeneral_WinCC2WinCC = MachineLibrary_NodeGeneral_WinCC2WinCC
        self.MachineLibrary_NodeGeneral_WinCC2WinCC54 = MachineLibrary_NodeGeneral_WinCC2WinCC54 if MachineLibrary_NodeGeneral_WinCC2WinCC54 is not None else set()
        
    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def MachineLibrary_NodeGeneral_WinCC2WinCC(self):
        return self.__MachineLibrary_NodeGeneral_WinCC2WinCC

    @MachineLibrary_NodeGeneral_WinCC2WinCC.setter
    def MachineLibrary_NodeGeneral_WinCC2WinCC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_WinCC2WinCC__MachineLibrary_NodeGeneral_WinCC2WinCC", None)
        self.__MachineLibrary_NodeGeneral_WinCC2WinCC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial48"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial48", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial48"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial48", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial48", self)

    @property
    def MachineLibrary_NodeGeneral_WinCC2WinCC54(self):
        return self.__MachineLibrary_NodeGeneral_WinCC2WinCC54

    @MachineLibrary_NodeGeneral_WinCC2WinCC54.setter
    def MachineLibrary_NodeGeneral_WinCC2WinCC54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_WinCC2WinCC__MachineLibrary_NodeGeneral_WinCC2WinCC54", None)
        self.__MachineLibrary_NodeGeneral_WinCC2WinCC54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_WinCCAddTag"):
                    opp_val = getattr(item, "MachineLibrary_WinCCAddTag", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_WinCCAddTag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_WinCCAddTag"):
                    opp_val = getattr(item, "MachineLibrary_WinCCAddTag", None)
                    
                    setattr(item, "MachineLibrary_WinCCAddTag", self)
                    

class MachineLibrary_NodeGeneral_RemotePM:

    def __init__(self, timeServer: int, system: str, MachineLibrary_NodeGeneral_RemotePM: "MachineLibrary_NodeGeneralSpecial" = None):
        self.timeServer = timeServer
        self.system = system
        self.MachineLibrary_NodeGeneral_RemotePM = MachineLibrary_NodeGeneral_RemotePM
        
    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def timeServer(self) -> int:
        return self.__timeServer

    @timeServer.setter
    def timeServer(self, timeServer: int):
        self.__timeServer = timeServer

    @property
    def MachineLibrary_NodeGeneral_RemotePM(self):
        return self.__MachineLibrary_NodeGeneral_RemotePM

    @MachineLibrary_NodeGeneral_RemotePM.setter
    def MachineLibrary_NodeGeneral_RemotePM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_RemotePM__MachineLibrary_NodeGeneral_RemotePM", None)
        self.__MachineLibrary_NodeGeneral_RemotePM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial46"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial46", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial46"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial46", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial46", self)

class MachineLibrary_NodeGeneral_PM2PM:

    def __init__(self, timeServer: int, type: int, MachineLibrary_NodeGeneral_PM2PM: "MachineLibrary_NodeGeneralSpecial" = None):
        self.timeServer = timeServer
        self.type = type
        self.MachineLibrary_NodeGeneral_PM2PM = MachineLibrary_NodeGeneral_PM2PM
        
    @property
    def timeServer(self) -> int:
        return self.__timeServer

    @timeServer.setter
    def timeServer(self, timeServer: int):
        self.__timeServer = timeServer

    @property
    def type(self) -> int:
        return self.__type

    @type.setter
    def type(self, type: int):
        self.__type = type

    @property
    def MachineLibrary_NodeGeneral_PM2PM(self):
        return self.__MachineLibrary_NodeGeneral_PM2PM

    @MachineLibrary_NodeGeneral_PM2PM.setter
    def MachineLibrary_NodeGeneral_PM2PM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_PM2PM__MachineLibrary_NodeGeneral_PM2PM", None)
        self.__MachineLibrary_NodeGeneral_PM2PM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial44"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial44", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial44"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial44", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial44", self)

class MachineLibrary_NodeGeneral_Terminal:

    def __init__(self, terminalType: int, maxXValue: int, maxYValue: int, maxScreens: int, displayTime: int, customTimer1: int, customTimer2: int, signalCarrierPresent: int, keyBoardSignalCarrierPresent: int, stationAuto: str, steelCarrier: str, stationReady: str, lenOfPlanID: int, stationType: int, name_1: str, name_2: str, name_3: str, name_4: str, name_5: str, name_6: str, MachineLibrary_NodeGeneral_Terminal: "MachineLibrary_NodeGeneralSpecial" = None):
        self.terminalType = terminalType
        self.maxXValue = maxXValue
        self.maxYValue = maxYValue
        self.maxScreens = maxScreens
        self.displayTime = displayTime
        self.customTimer1 = customTimer1
        self.customTimer2 = customTimer2
        self.signalCarrierPresent = signalCarrierPresent
        self.keyBoardSignalCarrierPresent = keyBoardSignalCarrierPresent
        self.stationAuto = stationAuto
        self.steelCarrier = steelCarrier
        self.stationReady = stationReady
        self.lenOfPlanID = lenOfPlanID
        self.stationType = stationType
        self.name_1 = name_1
        self.name_2 = name_2
        self.name_3 = name_3
        self.name_4 = name_4
        self.name_5 = name_5
        self.name_6 = name_6
        self.MachineLibrary_NodeGeneral_Terminal = MachineLibrary_NodeGeneral_Terminal
        
    @property
    def steelCarrier(self) -> str:
        return self.__steelCarrier

    @steelCarrier.setter
    def steelCarrier(self, steelCarrier: str):
        self.__steelCarrier = steelCarrier

    @property
    def maxScreens(self) -> int:
        return self.__maxScreens

    @maxScreens.setter
    def maxScreens(self, maxScreens: int):
        self.__maxScreens = maxScreens

    @property
    def name_4(self) -> str:
        return self.__name_4

    @name_4.setter
    def name_4(self, name_4: str):
        self.__name_4 = name_4

    @property
    def maxYValue(self) -> int:
        return self.__maxYValue

    @maxYValue.setter
    def maxYValue(self, maxYValue: int):
        self.__maxYValue = maxYValue

    @property
    def customTimer2(self) -> int:
        return self.__customTimer2

    @customTimer2.setter
    def customTimer2(self, customTimer2: int):
        self.__customTimer2 = customTimer2

    @property
    def keyBoardSignalCarrierPresent(self) -> int:
        return self.__keyBoardSignalCarrierPresent

    @keyBoardSignalCarrierPresent.setter
    def keyBoardSignalCarrierPresent(self, keyBoardSignalCarrierPresent: int):
        self.__keyBoardSignalCarrierPresent = keyBoardSignalCarrierPresent

    @property
    def name_1(self) -> str:
        return self.__name_1

    @name_1.setter
    def name_1(self, name_1: str):
        self.__name_1 = name_1

    @property
    def terminalType(self) -> int:
        return self.__terminalType

    @terminalType.setter
    def terminalType(self, terminalType: int):
        self.__terminalType = terminalType

    @property
    def name_2(self) -> str:
        return self.__name_2

    @name_2.setter
    def name_2(self, name_2: str):
        self.__name_2 = name_2

    @property
    def stationAuto(self) -> str:
        return self.__stationAuto

    @stationAuto.setter
    def stationAuto(self, stationAuto: str):
        self.__stationAuto = stationAuto

    @property
    def displayTime(self) -> int:
        return self.__displayTime

    @displayTime.setter
    def displayTime(self, displayTime: int):
        self.__displayTime = displayTime

    @property
    def maxXValue(self) -> int:
        return self.__maxXValue

    @maxXValue.setter
    def maxXValue(self, maxXValue: int):
        self.__maxXValue = maxXValue

    @property
    def name_5(self) -> str:
        return self.__name_5

    @name_5.setter
    def name_5(self, name_5: str):
        self.__name_5 = name_5

    @property
    def name_6(self) -> str:
        return self.__name_6

    @name_6.setter
    def name_6(self, name_6: str):
        self.__name_6 = name_6

    @property
    def stationType(self) -> int:
        return self.__stationType

    @stationType.setter
    def stationType(self, stationType: int):
        self.__stationType = stationType

    @property
    def customTimer1(self) -> int:
        return self.__customTimer1

    @customTimer1.setter
    def customTimer1(self, customTimer1: int):
        self.__customTimer1 = customTimer1

    @property
    def lenOfPlanID(self) -> int:
        return self.__lenOfPlanID

    @lenOfPlanID.setter
    def lenOfPlanID(self, lenOfPlanID: int):
        self.__lenOfPlanID = lenOfPlanID

    @property
    def name_3(self) -> str:
        return self.__name_3

    @name_3.setter
    def name_3(self, name_3: str):
        self.__name_3 = name_3

    @property
    def stationReady(self) -> str:
        return self.__stationReady

    @stationReady.setter
    def stationReady(self, stationReady: str):
        self.__stationReady = stationReady

    @property
    def signalCarrierPresent(self) -> int:
        return self.__signalCarrierPresent

    @signalCarrierPresent.setter
    def signalCarrierPresent(self, signalCarrierPresent: int):
        self.__signalCarrierPresent = signalCarrierPresent

    @property
    def MachineLibrary_NodeGeneral_Terminal(self):
        return self.__MachineLibrary_NodeGeneral_Terminal

    @MachineLibrary_NodeGeneral_Terminal.setter
    def MachineLibrary_NodeGeneral_Terminal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_Terminal__MachineLibrary_NodeGeneral_Terminal", None)
        self.__MachineLibrary_NodeGeneral_Terminal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial42"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial42", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial42"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial42", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial42", self)

class MachineLibrary_NodeGeneralSpecial:

    pass
class MachineLibrary_NodeGeneral:

    def __init__(self, canCreateStateTag: str, canCreateErrorTag: str, MachineLibrary_NodeGeneral: "MachineLibrary_NodeConfig" = None):
        self.canCreateStateTag = canCreateStateTag
        self.canCreateErrorTag = canCreateErrorTag
        self.MachineLibrary_NodeGeneral = MachineLibrary_NodeGeneral
        
    @property
    def canCreateStateTag(self) -> str:
        return self.__canCreateStateTag

    @canCreateStateTag.setter
    def canCreateStateTag(self, canCreateStateTag: str):
        self.__canCreateStateTag = canCreateStateTag

    @property
    def canCreateErrorTag(self) -> str:
        return self.__canCreateErrorTag

    @canCreateErrorTag.setter
    def canCreateErrorTag(self, canCreateErrorTag: str):
        self.__canCreateErrorTag = canCreateErrorTag

    @property
    def MachineLibrary_NodeGeneral(self):
        return self.__MachineLibrary_NodeGeneral

    @MachineLibrary_NodeGeneral.setter
    def MachineLibrary_NodeGeneral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral__MachineLibrary_NodeGeneral", None)
        self.__MachineLibrary_NodeGeneral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeConfig38"):
                opp_val = getattr(old_value, "MachineLibrary_NodeConfig38", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeConfig38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeConfig38"):
                opp_val = getattr(value, "MachineLibrary_NodeConfig38", None)
                setattr(value, "MachineLibrary_NodeConfig38", self)

class MachineLibrary_NodeSpecialConfiguration:

    pass
class MachineLibrary_CommunicationData:

    def __init__(self, comSendDataAddress: str, comSendDataLength: int, comRequestDataAddress: str, comRequestDataLength: int, comErrorDataAddress: str, comErrorDataLength: int, comSIDDataAddress: str, comSIDDataLength: int, comProgressIndDataAddress: str, comProgressIndDataLength: int, MachineLibrary_CommunicationData: "MachineLibrary_NodeConfig" = None):
        self.comSendDataAddress = comSendDataAddress
        self.comSendDataLength = comSendDataLength
        self.comRequestDataAddress = comRequestDataAddress
        self.comRequestDataLength = comRequestDataLength
        self.comErrorDataAddress = comErrorDataAddress
        self.comErrorDataLength = comErrorDataLength
        self.comSIDDataAddress = comSIDDataAddress
        self.comSIDDataLength = comSIDDataLength
        self.comProgressIndDataAddress = comProgressIndDataAddress
        self.comProgressIndDataLength = comProgressIndDataLength
        self.MachineLibrary_CommunicationData = MachineLibrary_CommunicationData
        
    @property
    def comSendDataLength(self) -> int:
        return self.__comSendDataLength

    @comSendDataLength.setter
    def comSendDataLength(self, comSendDataLength: int):
        self.__comSendDataLength = comSendDataLength

    @property
    def comSIDDataLength(self) -> int:
        return self.__comSIDDataLength

    @comSIDDataLength.setter
    def comSIDDataLength(self, comSIDDataLength: int):
        self.__comSIDDataLength = comSIDDataLength

    @property
    def comErrorDataAddress(self) -> str:
        return self.__comErrorDataAddress

    @comErrorDataAddress.setter
    def comErrorDataAddress(self, comErrorDataAddress: str):
        self.__comErrorDataAddress = comErrorDataAddress

    @property
    def comSendDataAddress(self) -> str:
        return self.__comSendDataAddress

    @comSendDataAddress.setter
    def comSendDataAddress(self, comSendDataAddress: str):
        self.__comSendDataAddress = comSendDataAddress

    @property
    def comErrorDataLength(self) -> int:
        return self.__comErrorDataLength

    @comErrorDataLength.setter
    def comErrorDataLength(self, comErrorDataLength: int):
        self.__comErrorDataLength = comErrorDataLength

    @property
    def comRequestDataAddress(self) -> str:
        return self.__comRequestDataAddress

    @comRequestDataAddress.setter
    def comRequestDataAddress(self, comRequestDataAddress: str):
        self.__comRequestDataAddress = comRequestDataAddress

    @property
    def comSIDDataAddress(self) -> str:
        return self.__comSIDDataAddress

    @comSIDDataAddress.setter
    def comSIDDataAddress(self, comSIDDataAddress: str):
        self.__comSIDDataAddress = comSIDDataAddress

    @property
    def comProgressIndDataAddress(self) -> str:
        return self.__comProgressIndDataAddress

    @comProgressIndDataAddress.setter
    def comProgressIndDataAddress(self, comProgressIndDataAddress: str):
        self.__comProgressIndDataAddress = comProgressIndDataAddress

    @property
    def comProgressIndDataLength(self) -> int:
        return self.__comProgressIndDataLength

    @comProgressIndDataLength.setter
    def comProgressIndDataLength(self, comProgressIndDataLength: int):
        self.__comProgressIndDataLength = comProgressIndDataLength

    @property
    def comRequestDataLength(self) -> int:
        return self.__comRequestDataLength

    @comRequestDataLength.setter
    def comRequestDataLength(self, comRequestDataLength: int):
        self.__comRequestDataLength = comRequestDataLength

    @property
    def MachineLibrary_CommunicationData(self):
        return self.__MachineLibrary_CommunicationData

    @MachineLibrary_CommunicationData.setter
    def MachineLibrary_CommunicationData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_CommunicationData__MachineLibrary_CommunicationData", None)
        self.__MachineLibrary_CommunicationData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeConfig34"):
                opp_val = getattr(old_value, "MachineLibrary_NodeConfig34", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeConfig34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeConfig34"):
                opp_val = getattr(value, "MachineLibrary_NodeConfig34", None)
                setattr(value, "MachineLibrary_NodeConfig34", self)

class MachineLibrary_Parameters:

    def __init__(self, parameterConfigYes: str, parameterConfigNo: str, MachineLibrary_Parameters: "MachineLibrary_NodeConfig" = None, MachineLibrary_Parameters226: set["MachineLibrary_Parameter"] = None):
        self.parameterConfigYes = parameterConfigYes
        self.parameterConfigNo = parameterConfigNo
        self.MachineLibrary_Parameters = MachineLibrary_Parameters
        self.MachineLibrary_Parameters226 = MachineLibrary_Parameters226 if MachineLibrary_Parameters226 is not None else set()
        
    @property
    def parameterConfigYes(self) -> str:
        return self.__parameterConfigYes

    @parameterConfigYes.setter
    def parameterConfigYes(self, parameterConfigYes: str):
        self.__parameterConfigYes = parameterConfigYes

    @property
    def parameterConfigNo(self) -> str:
        return self.__parameterConfigNo

    @parameterConfigNo.setter
    def parameterConfigNo(self, parameterConfigNo: str):
        self.__parameterConfigNo = parameterConfigNo

    @property
    def MachineLibrary_Parameters226(self):
        return self.__MachineLibrary_Parameters226

    @MachineLibrary_Parameters226.setter
    def MachineLibrary_Parameters226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Parameters__MachineLibrary_Parameters226", None)
        self.__MachineLibrary_Parameters226 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_Parameter"):
                    opp_val = getattr(item, "MachineLibrary_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_Parameter"):
                    opp_val = getattr(item, "MachineLibrary_Parameter", None)
                    
                    setattr(item, "MachineLibrary_Parameter", self)
                    

    @property
    def MachineLibrary_Parameters(self):
        return self.__MachineLibrary_Parameters

    @MachineLibrary_Parameters.setter
    def MachineLibrary_Parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Parameters__MachineLibrary_Parameters", None)
        self.__MachineLibrary_Parameters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeConfig32"):
                opp_val = getattr(old_value, "MachineLibrary_NodeConfig32", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeConfig32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeConfig32"):
                opp_val = getattr(value, "MachineLibrary_NodeConfig32", None)
                setattr(value, "MachineLibrary_NodeConfig32", self)

class MachineLibrary_NodePrograms:

    pass
class MachineLibrary_Commands:

    pass
class MachineLibrary_Units:

    def __init__(self, unitName: str, unitNo: int, internalUniNo: int, MachineLibrary_Units: "MachineLibrary_NodeConfig" = None, MachineLibrary_Units56: "MachineLibrary_Positions" = None, MachineLibrary_Units58: "MachineLibrary_StausBits" = None, MachineLibrary_Units60: "MachineLibrary_PLCtoPmMatrix" = None, MachineLibrary_Units62: "MachineLibrary_UnitPrograms" = None, MachineLibrary_Units64: "MachineLibrary_Buttons" = None, MachineLibrary_Units66: "MachineLibrary_UnitGeneral" = None, MachineLibrary_Units68: "MachineLibrary_UnitGeneralSpecial" = None, MachineLibrary_Units70: "MachineLibrary_UnitSpecialConfiguration" = None):
        self.unitName = unitName
        self.unitNo = unitNo
        self.internalUniNo = internalUniNo
        self.MachineLibrary_Units = MachineLibrary_Units
        self.MachineLibrary_Units56 = MachineLibrary_Units56
        self.MachineLibrary_Units58 = MachineLibrary_Units58
        self.MachineLibrary_Units60 = MachineLibrary_Units60
        self.MachineLibrary_Units62 = MachineLibrary_Units62
        self.MachineLibrary_Units64 = MachineLibrary_Units64
        self.MachineLibrary_Units66 = MachineLibrary_Units66
        self.MachineLibrary_Units68 = MachineLibrary_Units68
        self.MachineLibrary_Units70 = MachineLibrary_Units70
        
    @property
    def unitName(self) -> str:
        return self.__unitName

    @unitName.setter
    def unitName(self, unitName: str):
        self.__unitName = unitName

    @property
    def internalUniNo(self) -> int:
        return self.__internalUniNo

    @internalUniNo.setter
    def internalUniNo(self, internalUniNo: int):
        self.__internalUniNo = internalUniNo

    @property
    def unitNo(self) -> int:
        return self.__unitNo

    @unitNo.setter
    def unitNo(self, unitNo: int):
        self.__unitNo = unitNo

    @property
    def MachineLibrary_Units64(self):
        return self.__MachineLibrary_Units64

    @MachineLibrary_Units64.setter
    def MachineLibrary_Units64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units64", None)
        self.__MachineLibrary_Units64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Buttons"):
                opp_val = getattr(old_value, "MachineLibrary_Buttons", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Buttons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Buttons"):
                opp_val = getattr(value, "MachineLibrary_Buttons", None)
                setattr(value, "MachineLibrary_Buttons", self)

    @property
    def MachineLibrary_Units56(self):
        return self.__MachineLibrary_Units56

    @MachineLibrary_Units56.setter
    def MachineLibrary_Units56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units56", None)
        self.__MachineLibrary_Units56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Positions"):
                opp_val = getattr(old_value, "MachineLibrary_Positions", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Positions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Positions"):
                opp_val = getattr(value, "MachineLibrary_Positions", None)
                setattr(value, "MachineLibrary_Positions", self)

    @property
    def MachineLibrary_Units58(self):
        return self.__MachineLibrary_Units58

    @MachineLibrary_Units58.setter
    def MachineLibrary_Units58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units58", None)
        self.__MachineLibrary_Units58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_StausBits"):
                opp_val = getattr(old_value, "MachineLibrary_StausBits", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_StausBits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_StausBits"):
                opp_val = getattr(value, "MachineLibrary_StausBits", None)
                setattr(value, "MachineLibrary_StausBits", self)

    @property
    def MachineLibrary_Units68(self):
        return self.__MachineLibrary_Units68

    @MachineLibrary_Units68.setter
    def MachineLibrary_Units68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units68", None)
        self.__MachineLibrary_Units68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneralSpecial"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneralSpecial", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneralSpecial", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneralSpecial"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneralSpecial", None)
                setattr(value, "MachineLibrary_UnitGeneralSpecial", self)

    @property
    def MachineLibrary_Units62(self):
        return self.__MachineLibrary_Units62

    @MachineLibrary_Units62.setter
    def MachineLibrary_Units62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units62", None)
        self.__MachineLibrary_Units62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitPrograms"):
                opp_val = getattr(old_value, "MachineLibrary_UnitPrograms", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitPrograms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitPrograms"):
                opp_val = getattr(value, "MachineLibrary_UnitPrograms", None)
                setattr(value, "MachineLibrary_UnitPrograms", self)

    @property
    def MachineLibrary_Units70(self):
        return self.__MachineLibrary_Units70

    @MachineLibrary_Units70.setter
    def MachineLibrary_Units70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units70", None)
        self.__MachineLibrary_Units70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitSpecialConfiguration"):
                opp_val = getattr(old_value, "MachineLibrary_UnitSpecialConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitSpecialConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitSpecialConfiguration"):
                opp_val = getattr(value, "MachineLibrary_UnitSpecialConfiguration", None)
                setattr(value, "MachineLibrary_UnitSpecialConfiguration", self)

    @property
    def MachineLibrary_Units66(self):
        return self.__MachineLibrary_Units66

    @MachineLibrary_Units66.setter
    def MachineLibrary_Units66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units66", None)
        self.__MachineLibrary_Units66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_UnitGeneral"):
                opp_val = getattr(old_value, "MachineLibrary_UnitGeneral", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_UnitGeneral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_UnitGeneral"):
                opp_val = getattr(value, "MachineLibrary_UnitGeneral", None)
                setattr(value, "MachineLibrary_UnitGeneral", self)

    @property
    def MachineLibrary_Units(self):
        return self.__MachineLibrary_Units

    @MachineLibrary_Units.setter
    def MachineLibrary_Units(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units", None)
        self.__MachineLibrary_Units = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeConfig26"):
                opp_val = getattr(old_value, "MachineLibrary_NodeConfig26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeConfig26"):
                opp_val = getattr(value, "MachineLibrary_NodeConfig26", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_NodeConfig26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_Units60(self):
        return self.__MachineLibrary_Units60

    @MachineLibrary_Units60.setter
    def MachineLibrary_Units60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Units__MachineLibrary_Units60", None)
        self.__MachineLibrary_Units60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_PLCtoPmMatrix"):
                opp_val = getattr(old_value, "MachineLibrary_PLCtoPmMatrix", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_PLCtoPmMatrix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_PLCtoPmMatrix"):
                opp_val = getattr(value, "MachineLibrary_PLCtoPmMatrix", None)
                setattr(value, "MachineLibrary_PLCtoPmMatrix", self)

class MachineLibrary_NodeGeneral_RigakuXRF:

    def __init__(self, timeout: int, bDoNotshiftAtExit: int, timerToSendStatus: int, timeoutResponce: int, MachineLibrary_NodeGeneral_RigakuXRF: "MachineLibrary_NodeGeneralSpecial" = None):
        self.timeout = timeout
        self.bDoNotshiftAtExit = bDoNotshiftAtExit
        self.timerToSendStatus = timerToSendStatus
        self.timeoutResponce = timeoutResponce
        self.MachineLibrary_NodeGeneral_RigakuXRF = MachineLibrary_NodeGeneral_RigakuXRF
        
    @property
    def timeoutResponce(self) -> int:
        return self.__timeoutResponce

    @timeoutResponce.setter
    def timeoutResponce(self, timeoutResponce: int):
        self.__timeoutResponce = timeoutResponce

    @property
    def timerToSendStatus(self) -> int:
        return self.__timerToSendStatus

    @timerToSendStatus.setter
    def timerToSendStatus(self, timerToSendStatus: int):
        self.__timerToSendStatus = timerToSendStatus

    @property
    def bDoNotshiftAtExit(self) -> int:
        return self.__bDoNotshiftAtExit

    @bDoNotshiftAtExit.setter
    def bDoNotshiftAtExit(self, bDoNotshiftAtExit: int):
        self.__bDoNotshiftAtExit = bDoNotshiftAtExit

    @property
    def timeout(self) -> int:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: int):
        self.__timeout = timeout

    @property
    def MachineLibrary_NodeGeneral_RigakuXRF(self):
        return self.__MachineLibrary_NodeGeneral_RigakuXRF

    @MachineLibrary_NodeGeneral_RigakuXRF.setter
    def MachineLibrary_NodeGeneral_RigakuXRF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_RigakuXRF__MachineLibrary_NodeGeneral_RigakuXRF", None)
        self.__MachineLibrary_NodeGeneral_RigakuXRF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial52"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial52", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial52"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial52", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial52", self)

class MachineLibrary_NodeGeneral_AccuPycMeter:

    def __init__(self, polling: int, runTimout: int, expectSampleWeight: int, sendSampleWeight: int, MachineLibrary_NodeGeneral_AccuPycMeter: "MachineLibrary_NodeGeneralSpecial" = None):
        self.polling = polling
        self.runTimout = runTimout
        self.expectSampleWeight = expectSampleWeight
        self.sendSampleWeight = sendSampleWeight
        self.MachineLibrary_NodeGeneral_AccuPycMeter = MachineLibrary_NodeGeneral_AccuPycMeter
        
    @property
    def polling(self) -> int:
        return self.__polling

    @polling.setter
    def polling(self, polling: int):
        self.__polling = polling

    @property
    def sendSampleWeight(self) -> int:
        return self.__sendSampleWeight

    @sendSampleWeight.setter
    def sendSampleWeight(self, sendSampleWeight: int):
        self.__sendSampleWeight = sendSampleWeight

    @property
    def expectSampleWeight(self) -> int:
        return self.__expectSampleWeight

    @expectSampleWeight.setter
    def expectSampleWeight(self, expectSampleWeight: int):
        self.__expectSampleWeight = expectSampleWeight

    @property
    def runTimout(self) -> int:
        return self.__runTimout

    @runTimout.setter
    def runTimout(self, runTimout: int):
        self.__runTimout = runTimout

    @property
    def MachineLibrary_NodeGeneral_AccuPycMeter(self):
        return self.__MachineLibrary_NodeGeneral_AccuPycMeter

    @MachineLibrary_NodeGeneral_AccuPycMeter.setter
    def MachineLibrary_NodeGeneral_AccuPycMeter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeGeneral_AccuPycMeter__MachineLibrary_NodeGeneral_AccuPycMeter", None)
        self.__MachineLibrary_NodeGeneral_AccuPycMeter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial50"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial50", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial50"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial50", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial50", self)

class MachineLibrary_DPbase_Node:

    def __init__(self, nodeNo: int, isXPS: int, MachineLibrary_DPbase_Node: "MachineLibrary_DPbase_Link" = None):
        self.nodeNo = nodeNo
        self.isXPS = isXPS
        self.MachineLibrary_DPbase_Node = MachineLibrary_DPbase_Node
        
    @property
    def nodeNo(self) -> int:
        return self.__nodeNo

    @nodeNo.setter
    def nodeNo(self, nodeNo: int):
        self.__nodeNo = nodeNo

    @property
    def isXPS(self) -> int:
        return self.__isXPS

    @isXPS.setter
    def isXPS(self, isXPS: int):
        self.__isXPS = isXPS

    @property
    def MachineLibrary_DPbase_Node(self):
        return self.__MachineLibrary_DPbase_Node

    @MachineLibrary_DPbase_Node.setter
    def MachineLibrary_DPbase_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_DPbase_Node__MachineLibrary_DPbase_Node", None)
        self.__MachineLibrary_DPbase_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_DPbase_Link24"):
                opp_val = getattr(old_value, "MachineLibrary_DPbase_Link24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_DPbase_Link24"):
                opp_val = getattr(value, "MachineLibrary_DPbase_Link24", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_DPbase_Link24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MachineLibrary_DPbase_Link:

    def __init__(self, maxNodes: int, cp_name: str, speed: int, MachineLibrary_DPbase_Link: "MachineLibrary_LinkConfig" = None, MachineLibrary_DPbase_Link24: set["MachineLibrary_DPbase_Node"] = None):
        self.maxNodes = maxNodes
        self.cp_name = cp_name
        self.speed = speed
        self.MachineLibrary_DPbase_Link = MachineLibrary_DPbase_Link
        self.MachineLibrary_DPbase_Link24 = MachineLibrary_DPbase_Link24 if MachineLibrary_DPbase_Link24 is not None else set()
        
    @property
    def speed(self) -> int:
        return self.__speed

    @speed.setter
    def speed(self, speed: int):
        self.__speed = speed

    @property
    def cp_name(self) -> str:
        return self.__cp_name

    @cp_name.setter
    def cp_name(self, cp_name: str):
        self.__cp_name = cp_name

    @property
    def maxNodes(self) -> int:
        return self.__maxNodes

    @maxNodes.setter
    def maxNodes(self, maxNodes: int):
        self.__maxNodes = maxNodes

    @property
    def MachineLibrary_DPbase_Link(self):
        return self.__MachineLibrary_DPbase_Link

    @MachineLibrary_DPbase_Link.setter
    def MachineLibrary_DPbase_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_DPbase_Link__MachineLibrary_DPbase_Link", None)
        self.__MachineLibrary_DPbase_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig22"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig22", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig22"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig22", None)
                setattr(value, "MachineLibrary_LinkConfig22", self)

    @property
    def MachineLibrary_DPbase_Link24(self):
        return self.__MachineLibrary_DPbase_Link24

    @MachineLibrary_DPbase_Link24.setter
    def MachineLibrary_DPbase_Link24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_DPbase_Link__MachineLibrary_DPbase_Link24", None)
        self.__MachineLibrary_DPbase_Link24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_DPbase_Node"):
                    opp_val = getattr(item, "MachineLibrary_DPbase_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_DPbase_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_DPbase_Node"):
                    opp_val = getattr(item, "MachineLibrary_DPbase_Node", None)
                    
                    setattr(item, "MachineLibrary_DPbase_Node", self)
                    

class MachineLibrary_IBMWebsphereMQ:

    def __init__(self, qName: str, readQueName: str, readQueMgrName: str, readDynamicQueName: str, sendQueName: str, sendQueMgrName: str, sendDynamicQueName: str, sendBuffer: int, receiveBuffer: int, maxDataSize: int, MachineLibrary_IBMWebsphereMQ: "MachineLibrary_LinkConfig" = None):
        self.qName = qName
        self.readQueName = readQueName
        self.readQueMgrName = readQueMgrName
        self.readDynamicQueName = readDynamicQueName
        self.sendQueName = sendQueName
        self.sendQueMgrName = sendQueMgrName
        self.sendDynamicQueName = sendDynamicQueName
        self.sendBuffer = sendBuffer
        self.receiveBuffer = receiveBuffer
        self.maxDataSize = maxDataSize
        self.MachineLibrary_IBMWebsphereMQ = MachineLibrary_IBMWebsphereMQ
        
    @property
    def readQueName(self) -> str:
        return self.__readQueName

    @readQueName.setter
    def readQueName(self, readQueName: str):
        self.__readQueName = readQueName

    @property
    def maxDataSize(self) -> int:
        return self.__maxDataSize

    @maxDataSize.setter
    def maxDataSize(self, maxDataSize: int):
        self.__maxDataSize = maxDataSize

    @property
    def qName(self) -> str:
        return self.__qName

    @qName.setter
    def qName(self, qName: str):
        self.__qName = qName

    @property
    def sendBuffer(self) -> int:
        return self.__sendBuffer

    @sendBuffer.setter
    def sendBuffer(self, sendBuffer: int):
        self.__sendBuffer = sendBuffer

    @property
    def sendDynamicQueName(self) -> str:
        return self.__sendDynamicQueName

    @sendDynamicQueName.setter
    def sendDynamicQueName(self, sendDynamicQueName: str):
        self.__sendDynamicQueName = sendDynamicQueName

    @property
    def sendQueName(self) -> str:
        return self.__sendQueName

    @sendQueName.setter
    def sendQueName(self, sendQueName: str):
        self.__sendQueName = sendQueName

    @property
    def readQueMgrName(self) -> str:
        return self.__readQueMgrName

    @readQueMgrName.setter
    def readQueMgrName(self, readQueMgrName: str):
        self.__readQueMgrName = readQueMgrName

    @property
    def readDynamicQueName(self) -> str:
        return self.__readDynamicQueName

    @readDynamicQueName.setter
    def readDynamicQueName(self, readDynamicQueName: str):
        self.__readDynamicQueName = readDynamicQueName

    @property
    def receiveBuffer(self) -> int:
        return self.__receiveBuffer

    @receiveBuffer.setter
    def receiveBuffer(self, receiveBuffer: int):
        self.__receiveBuffer = receiveBuffer

    @property
    def sendQueMgrName(self) -> str:
        return self.__sendQueMgrName

    @sendQueMgrName.setter
    def sendQueMgrName(self, sendQueMgrName: str):
        self.__sendQueMgrName = sendQueMgrName

    @property
    def MachineLibrary_IBMWebsphereMQ(self):
        return self.__MachineLibrary_IBMWebsphereMQ

    @MachineLibrary_IBMWebsphereMQ.setter
    def MachineLibrary_IBMWebsphereMQ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_IBMWebsphereMQ__MachineLibrary_IBMWebsphereMQ", None)
        self.__MachineLibrary_IBMWebsphereMQ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig20"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig20", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig20"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig20", None)
                setattr(value, "MachineLibrary_LinkConfig20", self)

class MachineLibrary_Compac_Link:

    def __init__(self, useNotACK_NAK: int, port: str, commConfig: str, params: str, byteCount: int, bytecountcode: int, checksum: int, checksumCode: int, retry: int, timeout: int, bcc: int, maxDataLength: int, splitLongMessage: int, useNotENQ: int, MachineLibrary_Compac_Link: "MachineLibrary_LinkConfig" = None):
        self.useNotACK_NAK = useNotACK_NAK
        self.port = port
        self.commConfig = commConfig
        self.params = params
        self.byteCount = byteCount
        self.bytecountcode = bytecountcode
        self.checksum = checksum
        self.checksumCode = checksumCode
        self.retry = retry
        self.timeout = timeout
        self.bcc = bcc
        self.maxDataLength = maxDataLength
        self.splitLongMessage = splitLongMessage
        self.useNotENQ = useNotENQ
        self.MachineLibrary_Compac_Link = MachineLibrary_Compac_Link
        
    @property
    def checksum(self) -> int:
        return self.__checksum

    @checksum.setter
    def checksum(self, checksum: int):
        self.__checksum = checksum

    @property
    def useNotACK_NAK(self) -> int:
        return self.__useNotACK_NAK

    @useNotACK_NAK.setter
    def useNotACK_NAK(self, useNotACK_NAK: int):
        self.__useNotACK_NAK = useNotACK_NAK

    @property
    def useNotENQ(self) -> int:
        return self.__useNotENQ

    @useNotENQ.setter
    def useNotENQ(self, useNotENQ: int):
        self.__useNotENQ = useNotENQ

    @property
    def timeout(self) -> int:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: int):
        self.__timeout = timeout

    @property
    def commConfig(self) -> str:
        return self.__commConfig

    @commConfig.setter
    def commConfig(self, commConfig: str):
        self.__commConfig = commConfig

    @property
    def bytecountcode(self) -> int:
        return self.__bytecountcode

    @bytecountcode.setter
    def bytecountcode(self, bytecountcode: int):
        self.__bytecountcode = bytecountcode

    @property
    def byteCount(self) -> int:
        return self.__byteCount

    @byteCount.setter
    def byteCount(self, byteCount: int):
        self.__byteCount = byteCount

    @property
    def checksumCode(self) -> int:
        return self.__checksumCode

    @checksumCode.setter
    def checksumCode(self, checksumCode: int):
        self.__checksumCode = checksumCode

    @property
    def splitLongMessage(self) -> int:
        return self.__splitLongMessage

    @splitLongMessage.setter
    def splitLongMessage(self, splitLongMessage: int):
        self.__splitLongMessage = splitLongMessage

    @property
    def maxDataLength(self) -> int:
        return self.__maxDataLength

    @maxDataLength.setter
    def maxDataLength(self, maxDataLength: int):
        self.__maxDataLength = maxDataLength

    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def bcc(self) -> int:
        return self.__bcc

    @bcc.setter
    def bcc(self, bcc: int):
        self.__bcc = bcc

    @property
    def retry(self) -> int:
        return self.__retry

    @retry.setter
    def retry(self, retry: int):
        self.__retry = retry

    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def MachineLibrary_Compac_Link(self):
        return self.__MachineLibrary_Compac_Link

    @MachineLibrary_Compac_Link.setter
    def MachineLibrary_Compac_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Compac_Link__MachineLibrary_Compac_Link", None)
        self.__MachineLibrary_Compac_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig18"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig18", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig18"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig18", None)
                setattr(value, "MachineLibrary_LinkConfig18", self)

class MachineLibrary_FileTransfer_Link:

    def __init__(self, sendBuffer: int, receiveBuffer: int, maxDataLength: int, timeoutwrite: str, pollTime: int, writePath: str, readPath: str, flagDelAfterReading: int, flagWriteAfterReading: int, flagToWriteWaitForDeleted: int, flagToWriteWaitFor: int, delimter: str, writeAfterReading: int, toWriteWaitFor: str, translation: int, delimiter: str, MachineLibrary_FileTransfer_Link: "MachineLibrary_LinkConfig" = None):
        self.sendBuffer = sendBuffer
        self.receiveBuffer = receiveBuffer
        self.maxDataLength = maxDataLength
        self.timeoutwrite = timeoutwrite
        self.pollTime = pollTime
        self.writePath = writePath
        self.readPath = readPath
        self.flagDelAfterReading = flagDelAfterReading
        self.flagWriteAfterReading = flagWriteAfterReading
        self.flagToWriteWaitForDeleted = flagToWriteWaitForDeleted
        self.flagToWriteWaitFor = flagToWriteWaitFor
        self.delimter = delimter
        self.writeAfterReading = writeAfterReading
        self.toWriteWaitFor = toWriteWaitFor
        self.translation = translation
        self.delimiter = delimiter
        self.MachineLibrary_FileTransfer_Link = MachineLibrary_FileTransfer_Link
        
    @property
    def receiveBuffer(self) -> int:
        return self.__receiveBuffer

    @receiveBuffer.setter
    def receiveBuffer(self, receiveBuffer: int):
        self.__receiveBuffer = receiveBuffer

    @property
    def flagWriteAfterReading(self) -> int:
        return self.__flagWriteAfterReading

    @flagWriteAfterReading.setter
    def flagWriteAfterReading(self, flagWriteAfterReading: int):
        self.__flagWriteAfterReading = flagWriteAfterReading

    @property
    def flagDelAfterReading(self) -> int:
        return self.__flagDelAfterReading

    @flagDelAfterReading.setter
    def flagDelAfterReading(self, flagDelAfterReading: int):
        self.__flagDelAfterReading = flagDelAfterReading

    @property
    def toWriteWaitFor(self) -> str:
        return self.__toWriteWaitFor

    @toWriteWaitFor.setter
    def toWriteWaitFor(self, toWriteWaitFor: str):
        self.__toWriteWaitFor = toWriteWaitFor

    @property
    def sendBuffer(self) -> int:
        return self.__sendBuffer

    @sendBuffer.setter
    def sendBuffer(self, sendBuffer: int):
        self.__sendBuffer = sendBuffer

    @property
    def flagToWriteWaitFor(self) -> int:
        return self.__flagToWriteWaitFor

    @flagToWriteWaitFor.setter
    def flagToWriteWaitFor(self, flagToWriteWaitFor: int):
        self.__flagToWriteWaitFor = flagToWriteWaitFor

    @property
    def delimter(self) -> str:
        return self.__delimter

    @delimter.setter
    def delimter(self, delimter: str):
        self.__delimter = delimter

    @property
    def writePath(self) -> str:
        return self.__writePath

    @writePath.setter
    def writePath(self, writePath: str):
        self.__writePath = writePath

    @property
    def maxDataLength(self) -> int:
        return self.__maxDataLength

    @maxDataLength.setter
    def maxDataLength(self, maxDataLength: int):
        self.__maxDataLength = maxDataLength

    @property
    def pollTime(self) -> int:
        return self.__pollTime

    @pollTime.setter
    def pollTime(self, pollTime: int):
        self.__pollTime = pollTime

    @property
    def delimiter(self) -> str:
        return self.__delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str):
        self.__delimiter = delimiter

    @property
    def translation(self) -> int:
        return self.__translation

    @translation.setter
    def translation(self, translation: int):
        self.__translation = translation

    @property
    def timeoutwrite(self) -> str:
        return self.__timeoutwrite

    @timeoutwrite.setter
    def timeoutwrite(self, timeoutwrite: str):
        self.__timeoutwrite = timeoutwrite

    @property
    def flagToWriteWaitForDeleted(self) -> int:
        return self.__flagToWriteWaitForDeleted

    @flagToWriteWaitForDeleted.setter
    def flagToWriteWaitForDeleted(self, flagToWriteWaitForDeleted: int):
        self.__flagToWriteWaitForDeleted = flagToWriteWaitForDeleted

    @property
    def writeAfterReading(self) -> int:
        return self.__writeAfterReading

    @writeAfterReading.setter
    def writeAfterReading(self, writeAfterReading: int):
        self.__writeAfterReading = writeAfterReading

    @property
    def readPath(self) -> str:
        return self.__readPath

    @readPath.setter
    def readPath(self, readPath: str):
        self.__readPath = readPath

    @property
    def MachineLibrary_FileTransfer_Link(self):
        return self.__MachineLibrary_FileTransfer_Link

    @MachineLibrary_FileTransfer_Link.setter
    def MachineLibrary_FileTransfer_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_FileTransfer_Link__MachineLibrary_FileTransfer_Link", None)
        self.__MachineLibrary_FileTransfer_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig16"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig16", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig16"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig16", None)
                setattr(value, "MachineLibrary_LinkConfig16", self)

class MachineLibrary_Serial_Link:

    def __init__(self, port: str, commConfig: str, params: str, endChar: str, maxCharDelay: str, bufferLenght: str, startChar: str, logging: int, MachineLibrary_Serial_Link: "MachineLibrary_LinkConfig" = None):
        self.port = port
        self.commConfig = commConfig
        self.params = params
        self.endChar = endChar
        self.maxCharDelay = maxCharDelay
        self.bufferLenght = bufferLenght
        self.startChar = startChar
        self.logging = logging
        self.MachineLibrary_Serial_Link = MachineLibrary_Serial_Link
        
    @property
    def bufferLenght(self) -> str:
        return self.__bufferLenght

    @bufferLenght.setter
    def bufferLenght(self, bufferLenght: str):
        self.__bufferLenght = bufferLenght

    @property
    def port(self) -> str:
        return self.__port

    @port.setter
    def port(self, port: str):
        self.__port = port

    @property
    def maxCharDelay(self) -> str:
        return self.__maxCharDelay

    @maxCharDelay.setter
    def maxCharDelay(self, maxCharDelay: str):
        self.__maxCharDelay = maxCharDelay

    @property
    def params(self) -> str:
        return self.__params

    @params.setter
    def params(self, params: str):
        self.__params = params

    @property
    def commConfig(self) -> str:
        return self.__commConfig

    @commConfig.setter
    def commConfig(self, commConfig: str):
        self.__commConfig = commConfig

    @property
    def logging(self) -> int:
        return self.__logging

    @logging.setter
    def logging(self, logging: int):
        self.__logging = logging

    @property
    def startChar(self) -> str:
        return self.__startChar

    @startChar.setter
    def startChar(self, startChar: str):
        self.__startChar = startChar

    @property
    def endChar(self) -> str:
        return self.__endChar

    @endChar.setter
    def endChar(self, endChar: str):
        self.__endChar = endChar

    @property
    def MachineLibrary_Serial_Link(self):
        return self.__MachineLibrary_Serial_Link

    @MachineLibrary_Serial_Link.setter
    def MachineLibrary_Serial_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Serial_Link__MachineLibrary_Serial_Link", None)
        self.__MachineLibrary_Serial_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig14"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig14", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig14"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig14", None)
                setattr(value, "MachineLibrary_LinkConfig14", self)

class MachineLibrary_TCPIP_Link:

    def __init__(self, protocol: int, termChar: int, port: int, address_1: str, address_2: str, address_3: str, address_4: str, address_5: str, address_6: str, sendBuffer: int, receiveBuffer: int, maxDataSize: int, msgDelay: int, MachineLibrary_TCPIP_Link: "MachineLibrary_LinkConfig" = None):
        self.protocol = protocol
        self.termChar = termChar
        self.port = port
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.address_4 = address_4
        self.address_5 = address_5
        self.address_6 = address_6
        self.sendBuffer = sendBuffer
        self.receiveBuffer = receiveBuffer
        self.maxDataSize = maxDataSize
        self.msgDelay = msgDelay
        self.MachineLibrary_TCPIP_Link = MachineLibrary_TCPIP_Link
        
    @property
    def termChar(self) -> int:
        return self.__termChar

    @termChar.setter
    def termChar(self, termChar: int):
        self.__termChar = termChar

    @property
    def sendBuffer(self) -> int:
        return self.__sendBuffer

    @sendBuffer.setter
    def sendBuffer(self, sendBuffer: int):
        self.__sendBuffer = sendBuffer

    @property
    def address_1(self) -> str:
        return self.__address_1

    @address_1.setter
    def address_1(self, address_1: str):
        self.__address_1 = address_1

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def address_4(self) -> str:
        return self.__address_4

    @address_4.setter
    def address_4(self, address_4: str):
        self.__address_4 = address_4

    @property
    def address_5(self) -> str:
        return self.__address_5

    @address_5.setter
    def address_5(self, address_5: str):
        self.__address_5 = address_5

    @property
    def maxDataSize(self) -> int:
        return self.__maxDataSize

    @maxDataSize.setter
    def maxDataSize(self, maxDataSize: int):
        self.__maxDataSize = maxDataSize

    @property
    def msgDelay(self) -> int:
        return self.__msgDelay

    @msgDelay.setter
    def msgDelay(self, msgDelay: int):
        self.__msgDelay = msgDelay

    @property
    def address_3(self) -> str:
        return self.__address_3

    @address_3.setter
    def address_3(self, address_3: str):
        self.__address_3 = address_3

    @property
    def address_6(self) -> str:
        return self.__address_6

    @address_6.setter
    def address_6(self, address_6: str):
        self.__address_6 = address_6

    @property
    def protocol(self) -> int:
        return self.__protocol

    @protocol.setter
    def protocol(self, protocol: int):
        self.__protocol = protocol

    @property
    def address_2(self) -> str:
        return self.__address_2

    @address_2.setter
    def address_2(self, address_2: str):
        self.__address_2 = address_2

    @property
    def receiveBuffer(self) -> int:
        return self.__receiveBuffer

    @receiveBuffer.setter
    def receiveBuffer(self, receiveBuffer: int):
        self.__receiveBuffer = receiveBuffer

    @property
    def MachineLibrary_TCPIP_Link(self):
        return self.__MachineLibrary_TCPIP_Link

    @MachineLibrary_TCPIP_Link.setter
    def MachineLibrary_TCPIP_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_TCPIP_Link__MachineLibrary_TCPIP_Link", None)
        self.__MachineLibrary_TCPIP_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig12"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig12", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig12"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig12", None)
                setattr(value, "MachineLibrary_LinkConfig12", self)

class MachineLibrary_WinCCLnk:

    def __init__(self, connectionName: str, canModifyTag: int, canCreateTags: int, updateCycle: int, updateCycle_Help: str, MachineLibrary_WinCCLnk: "MachineLibrary_LinkConfig" = None):
        self.connectionName = connectionName
        self.canModifyTag = canModifyTag
        self.canCreateTags = canCreateTags
        self.updateCycle = updateCycle
        self.updateCycle_Help = updateCycle_Help
        self.MachineLibrary_WinCCLnk = MachineLibrary_WinCCLnk
        
    @property
    def connectionName(self) -> str:
        return self.__connectionName

    @connectionName.setter
    def connectionName(self, connectionName: str):
        self.__connectionName = connectionName

    @property
    def canCreateTags(self) -> int:
        return self.__canCreateTags

    @canCreateTags.setter
    def canCreateTags(self, canCreateTags: int):
        self.__canCreateTags = canCreateTags

    @property
    def updateCycle_Help(self) -> str:
        return self.__updateCycle_Help

    @updateCycle_Help.setter
    def updateCycle_Help(self, updateCycle_Help: str):
        self.__updateCycle_Help = updateCycle_Help

    @property
    def updateCycle(self) -> int:
        return self.__updateCycle

    @updateCycle.setter
    def updateCycle(self, updateCycle: int):
        self.__updateCycle = updateCycle

    @property
    def canModifyTag(self) -> int:
        return self.__canModifyTag

    @canModifyTag.setter
    def canModifyTag(self, canModifyTag: int):
        self.__canModifyTag = canModifyTag

    @property
    def MachineLibrary_WinCCLnk(self):
        return self.__MachineLibrary_WinCCLnk

    @MachineLibrary_WinCCLnk.setter
    def MachineLibrary_WinCCLnk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_WinCCLnk__MachineLibrary_WinCCLnk", None)
        self.__MachineLibrary_WinCCLnk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig10"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig10", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig10"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig10", None)
                setattr(value, "MachineLibrary_LinkConfig10", self)

class MachineLibrary_NodeConfig:

    def __init__(self, nodeName: str, nodeNo: int, simFileName: str, MachineLibrary_NodeConfig: "MachineLibrary_LabMachine" = None, MachineLibrary_NodeConfig26: set["MachineLibrary_Units"] = None, MachineLibrary_NodeConfig28: "MachineLibrary_Commands" = None, MachineLibrary_NodeConfig30: "MachineLibrary_NodePrograms" = None, MachineLibrary_NodeConfig32: "MachineLibrary_Parameters" = None, MachineLibrary_NodeConfig34: "MachineLibrary_CommunicationData" = None, MachineLibrary_NodeConfig36: "MachineLibrary_NodeSpecialConfiguration" = None, MachineLibrary_NodeConfig38: "MachineLibrary_NodeGeneral" = None, MachineLibrary_NodeConfig40: "MachineLibrary_NodeGeneralSpecial" = None):
        self.nodeName = nodeName
        self.nodeNo = nodeNo
        self.simFileName = simFileName
        self.MachineLibrary_NodeConfig = MachineLibrary_NodeConfig
        self.MachineLibrary_NodeConfig26 = MachineLibrary_NodeConfig26 if MachineLibrary_NodeConfig26 is not None else set()
        self.MachineLibrary_NodeConfig28 = MachineLibrary_NodeConfig28
        self.MachineLibrary_NodeConfig30 = MachineLibrary_NodeConfig30
        self.MachineLibrary_NodeConfig32 = MachineLibrary_NodeConfig32
        self.MachineLibrary_NodeConfig34 = MachineLibrary_NodeConfig34
        self.MachineLibrary_NodeConfig36 = MachineLibrary_NodeConfig36
        self.MachineLibrary_NodeConfig38 = MachineLibrary_NodeConfig38
        self.MachineLibrary_NodeConfig40 = MachineLibrary_NodeConfig40
        
    @property
    def simFileName(self) -> str:
        return self.__simFileName

    @simFileName.setter
    def simFileName(self, simFileName: str):
        self.__simFileName = simFileName

    @property
    def nodeNo(self) -> int:
        return self.__nodeNo

    @nodeNo.setter
    def nodeNo(self, nodeNo: int):
        self.__nodeNo = nodeNo

    @property
    def nodeName(self) -> str:
        return self.__nodeName

    @nodeName.setter
    def nodeName(self, nodeName: str):
        self.__nodeName = nodeName

    @property
    def MachineLibrary_NodeConfig(self):
        return self.__MachineLibrary_NodeConfig

    @MachineLibrary_NodeConfig.setter
    def MachineLibrary_NodeConfig(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig", None)
        self.__MachineLibrary_NodeConfig = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LabMachine6"):
                opp_val = getattr(old_value, "MachineLibrary_LabMachine6", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LabMachine6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LabMachine6"):
                opp_val = getattr(value, "MachineLibrary_LabMachine6", None)
                setattr(value, "MachineLibrary_LabMachine6", self)

    @property
    def MachineLibrary_NodeConfig34(self):
        return self.__MachineLibrary_NodeConfig34

    @MachineLibrary_NodeConfig34.setter
    def MachineLibrary_NodeConfig34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig34", None)
        self.__MachineLibrary_NodeConfig34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_CommunicationData"):
                opp_val = getattr(old_value, "MachineLibrary_CommunicationData", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_CommunicationData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_CommunicationData"):
                opp_val = getattr(value, "MachineLibrary_CommunicationData", None)
                setattr(value, "MachineLibrary_CommunicationData", self)

    @property
    def MachineLibrary_NodeConfig38(self):
        return self.__MachineLibrary_NodeConfig38

    @MachineLibrary_NodeConfig38.setter
    def MachineLibrary_NodeConfig38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig38", None)
        self.__MachineLibrary_NodeConfig38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneral"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneral", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneral", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneral"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneral", None)
                setattr(value, "MachineLibrary_NodeGeneral", self)

    @property
    def MachineLibrary_NodeConfig32(self):
        return self.__MachineLibrary_NodeConfig32

    @MachineLibrary_NodeConfig32.setter
    def MachineLibrary_NodeConfig32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig32", None)
        self.__MachineLibrary_NodeConfig32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Parameters"):
                opp_val = getattr(old_value, "MachineLibrary_Parameters", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Parameters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Parameters"):
                opp_val = getattr(value, "MachineLibrary_Parameters", None)
                setattr(value, "MachineLibrary_Parameters", self)

    @property
    def MachineLibrary_NodeConfig26(self):
        return self.__MachineLibrary_NodeConfig26

    @MachineLibrary_NodeConfig26.setter
    def MachineLibrary_NodeConfig26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig26", None)
        self.__MachineLibrary_NodeConfig26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MachineLibrary_Units"):
                    opp_val = getattr(item, "MachineLibrary_Units", None)
                    
                    if opp_val == self:
                        setattr(item, "MachineLibrary_Units", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MachineLibrary_Units"):
                    opp_val = getattr(item, "MachineLibrary_Units", None)
                    
                    setattr(item, "MachineLibrary_Units", self)
                    

    @property
    def MachineLibrary_NodeConfig40(self):
        return self.__MachineLibrary_NodeConfig40

    @MachineLibrary_NodeConfig40.setter
    def MachineLibrary_NodeConfig40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig40", None)
        self.__MachineLibrary_NodeConfig40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeGeneralSpecial"):
                opp_val = getattr(old_value, "MachineLibrary_NodeGeneralSpecial", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeGeneralSpecial", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeGeneralSpecial"):
                opp_val = getattr(value, "MachineLibrary_NodeGeneralSpecial", None)
                setattr(value, "MachineLibrary_NodeGeneralSpecial", self)

    @property
    def MachineLibrary_NodeConfig36(self):
        return self.__MachineLibrary_NodeConfig36

    @MachineLibrary_NodeConfig36.setter
    def MachineLibrary_NodeConfig36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig36", None)
        self.__MachineLibrary_NodeConfig36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeSpecialConfiguration"):
                opp_val = getattr(old_value, "MachineLibrary_NodeSpecialConfiguration", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeSpecialConfiguration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeSpecialConfiguration"):
                opp_val = getattr(value, "MachineLibrary_NodeSpecialConfiguration", None)
                setattr(value, "MachineLibrary_NodeSpecialConfiguration", self)

    @property
    def MachineLibrary_NodeConfig30(self):
        return self.__MachineLibrary_NodeConfig30

    @MachineLibrary_NodeConfig30.setter
    def MachineLibrary_NodeConfig30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig30", None)
        self.__MachineLibrary_NodeConfig30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodePrograms"):
                opp_val = getattr(old_value, "MachineLibrary_NodePrograms", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodePrograms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodePrograms"):
                opp_val = getattr(value, "MachineLibrary_NodePrograms", None)
                setattr(value, "MachineLibrary_NodePrograms", self)

    @property
    def MachineLibrary_NodeConfig28(self):
        return self.__MachineLibrary_NodeConfig28

    @MachineLibrary_NodeConfig28.setter
    def MachineLibrary_NodeConfig28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_NodeConfig__MachineLibrary_NodeConfig28", None)
        self.__MachineLibrary_NodeConfig28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Commands"):
                opp_val = getattr(old_value, "MachineLibrary_Commands", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Commands", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Commands"):
                opp_val = getattr(value, "MachineLibrary_Commands", None)
                setattr(value, "MachineLibrary_Commands", self)

class MachineLibrary_Link2:

    def __init__(self, link2Type: str, link2ParamFile: str, link2ParamSection: str, MachineLibrary_Link2: "MachineLibrary_LabMachine" = None):
        self.link2Type = link2Type
        self.link2ParamFile = link2ParamFile
        self.link2ParamSection = link2ParamSection
        self.MachineLibrary_Link2 = MachineLibrary_Link2
        
    @property
    def link2ParamFile(self) -> str:
        return self.__link2ParamFile

    @link2ParamFile.setter
    def link2ParamFile(self, link2ParamFile: str):
        self.__link2ParamFile = link2ParamFile

    @property
    def link2ParamSection(self) -> str:
        return self.__link2ParamSection

    @link2ParamSection.setter
    def link2ParamSection(self, link2ParamSection: str):
        self.__link2ParamSection = link2ParamSection

    @property
    def link2Type(self) -> str:
        return self.__link2Type

    @link2Type.setter
    def link2Type(self, link2Type: str):
        self.__link2Type = link2Type

    @property
    def MachineLibrary_Link2(self):
        return self.__MachineLibrary_Link2

    @MachineLibrary_Link2.setter
    def MachineLibrary_Link2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_Link2__MachineLibrary_Link2", None)
        self.__MachineLibrary_Link2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LabMachine4"):
                opp_val = getattr(old_value, "MachineLibrary_LabMachine4", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LabMachine4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LabMachine4"):
                opp_val = getattr(value, "MachineLibrary_LabMachine4", None)
                setattr(value, "MachineLibrary_LabMachine4", self)

class MachineLibrary_LabMachine:

    def __init__(self, machineName: str, machineVersionNo: float, versionRemark: str, driver: str, linkType: str, linkParamFile: str, linkParamSection: str, createWinCCTags: str, MachineLibrary_LabMachine6: "MachineLibrary_NodeConfig" = None, MachineLibrary_LabMachine8: "MachineLibrary_LinkConfig" = None, MachineLibrary_LabMachine: "MachineLibrary_LabMachines" = None, MachineLibrary_LabMachine4: "MachineLibrary_Link2" = None):
        self.machineName = machineName
        self.machineVersionNo = machineVersionNo
        self.versionRemark = versionRemark
        self.driver = driver
        self.linkType = linkType
        self.linkParamFile = linkParamFile
        self.linkParamSection = linkParamSection
        self.createWinCCTags = createWinCCTags
        self.MachineLibrary_LabMachine6 = MachineLibrary_LabMachine6
        self.MachineLibrary_LabMachine8 = MachineLibrary_LabMachine8
        self.MachineLibrary_LabMachine = MachineLibrary_LabMachine
        self.MachineLibrary_LabMachine4 = MachineLibrary_LabMachine4
        
    @property
    def versionRemark(self) -> str:
        return self.__versionRemark

    @versionRemark.setter
    def versionRemark(self, versionRemark: str):
        self.__versionRemark = versionRemark

    @property
    def linkParamSection(self) -> str:
        return self.__linkParamSection

    @linkParamSection.setter
    def linkParamSection(self, linkParamSection: str):
        self.__linkParamSection = linkParamSection

    @property
    def createWinCCTags(self) -> str:
        return self.__createWinCCTags

    @createWinCCTags.setter
    def createWinCCTags(self, createWinCCTags: str):
        self.__createWinCCTags = createWinCCTags

    @property
    def driver(self) -> str:
        return self.__driver

    @driver.setter
    def driver(self, driver: str):
        self.__driver = driver

    @property
    def linkType(self) -> str:
        return self.__linkType

    @linkType.setter
    def linkType(self, linkType: str):
        self.__linkType = linkType

    @property
    def machineVersionNo(self) -> float:
        return self.__machineVersionNo

    @machineVersionNo.setter
    def machineVersionNo(self, machineVersionNo: float):
        self.__machineVersionNo = machineVersionNo

    @property
    def machineName(self) -> str:
        return self.__machineName

    @machineName.setter
    def machineName(self, machineName: str):
        self.__machineName = machineName

    @property
    def linkParamFile(self) -> str:
        return self.__linkParamFile

    @linkParamFile.setter
    def linkParamFile(self, linkParamFile: str):
        self.__linkParamFile = linkParamFile

    @property
    def MachineLibrary_LabMachine8(self):
        return self.__MachineLibrary_LabMachine8

    @MachineLibrary_LabMachine8.setter
    def MachineLibrary_LabMachine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_LabMachine__MachineLibrary_LabMachine8", None)
        self.__MachineLibrary_LabMachine8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LinkConfig"):
                opp_val = getattr(old_value, "MachineLibrary_LinkConfig", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LinkConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LinkConfig"):
                opp_val = getattr(value, "MachineLibrary_LinkConfig", None)
                setattr(value, "MachineLibrary_LinkConfig", self)

    @property
    def MachineLibrary_LabMachine(self):
        return self.__MachineLibrary_LabMachine

    @MachineLibrary_LabMachine.setter
    def MachineLibrary_LabMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_LabMachine__MachineLibrary_LabMachine", None)
        self.__MachineLibrary_LabMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LabMachines2"):
                opp_val = getattr(old_value, "MachineLibrary_LabMachines2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LabMachines2"):
                opp_val = getattr(value, "MachineLibrary_LabMachines2", None)
                if opp_val is None:
                    setattr(value, "MachineLibrary_LabMachines2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MachineLibrary_LabMachine4(self):
        return self.__MachineLibrary_LabMachine4

    @MachineLibrary_LabMachine4.setter
    def MachineLibrary_LabMachine4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_LabMachine__MachineLibrary_LabMachine4", None)
        self.__MachineLibrary_LabMachine4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_Link2"):
                opp_val = getattr(old_value, "MachineLibrary_Link2", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_Link2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_Link2"):
                opp_val = getattr(value, "MachineLibrary_Link2", None)
                setattr(value, "MachineLibrary_Link2", self)

    @property
    def MachineLibrary_LabMachine6(self):
        return self.__MachineLibrary_LabMachine6

    @MachineLibrary_LabMachine6.setter
    def MachineLibrary_LabMachine6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_LabMachine__MachineLibrary_LabMachine6", None)
        self.__MachineLibrary_LabMachine6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_NodeConfig"):
                opp_val = getattr(old_value, "MachineLibrary_NodeConfig", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_NodeConfig", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_NodeConfig"):
                opp_val = getattr(value, "MachineLibrary_NodeConfig", None)
                setattr(value, "MachineLibrary_NodeConfig", self)

class MachineLibrary_LabMachines:

    pass
class MachineLibrary_PMMachineLibrary:

    def __init__(self, libraryVersion: float, libraryVersionRemark: str, MachineLibrary_PMMachineLibrary: "MachineLibrary_LabMachines" = None):
        self.libraryVersion = libraryVersion
        self.libraryVersionRemark = libraryVersionRemark
        self.MachineLibrary_PMMachineLibrary = MachineLibrary_PMMachineLibrary
        
    @property
    def libraryVersionRemark(self) -> str:
        return self.__libraryVersionRemark

    @libraryVersionRemark.setter
    def libraryVersionRemark(self, libraryVersionRemark: str):
        self.__libraryVersionRemark = libraryVersionRemark

    @property
    def libraryVersion(self) -> float:
        return self.__libraryVersion

    @libraryVersion.setter
    def libraryVersion(self, libraryVersion: float):
        self.__libraryVersion = libraryVersion

    @property
    def MachineLibrary_PMMachineLibrary(self):
        return self.__MachineLibrary_PMMachineLibrary

    @MachineLibrary_PMMachineLibrary.setter
    def MachineLibrary_PMMachineLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MachineLibrary_PMMachineLibrary__MachineLibrary_PMMachineLibrary", None)
        self.__MachineLibrary_PMMachineLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MachineLibrary_LabMachines"):
                opp_val = getattr(old_value, "MachineLibrary_LabMachines", None)
                if opp_val == self:
                    setattr(old_value, "MachineLibrary_LabMachines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MachineLibrary_LabMachines"):
                opp_val = getattr(value, "MachineLibrary_LabMachines", None)
                setattr(value, "MachineLibrary_LabMachines", self)

class MachineLibrary_LinkConfig:

    pass