from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Phase(Enum):
    build = "build"
    run = "run"
    both = "both"
class OperatorType(Enum):
    include = "include"
    exclude = "exclude"
class StatCommand(Enum):
    createFolder = "createFolder"
    removeFolder = "removeFolder"
    listDrives = "listDrives"
    listFiles = "listFiles"
    getScreenCapture = "getScreenCapture"
    delete = "delete"
    run = "run"
    startLogging = "startLogging"
    stopLogging = "stopLogging"


############################################
# Definition of Classes
############################################

class driver_TestCasesList:

    def __init__(self, operator: str, driver_TestCasesList: set["driver_TestCase"] = None, driver_TestCasesList49: "driver_TestExecuteScript" = None):
        self.operator = operator
        self.driver_TestCasesList = driver_TestCasesList if driver_TestCasesList is not None else set()
        self.driver_TestCasesList49 = driver_TestCasesList49
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def driver_TestCasesList(self):
        return self.__driver_TestCasesList

    @driver_TestCasesList.setter
    def driver_TestCasesList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TestCasesList__driver_TestCasesList", None)
        self.__driver_TestCasesList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_TestCase"):
                    opp_val = getattr(item, "driver_TestCase", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_TestCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_TestCase"):
                    opp_val = getattr(item, "driver_TestCase", None)
                    
                    setattr(item, "driver_TestCase", self)
                    

    @property
    def driver_TestCasesList49(self):
        return self.__driver_TestCasesList49

    @driver_TestCasesList49.setter
    def driver_TestCasesList49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TestCasesList__driver_TestCasesList49", None)
        self.__driver_TestCasesList49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_TestExecuteScript48"):
                opp_val = getattr(old_value, "driver_TestExecuteScript48", None)
                if opp_val == self:
                    setattr(old_value, "driver_TestExecuteScript48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_TestExecuteScript48"):
                opp_val = getattr(value, "driver_TestExecuteScript48", None)
                setattr(value, "driver_TestExecuteScript48", self)

class driver_TestCase:

    def __init__(self, target: str, driver_TestCase: "driver_TestCasesList" = None):
        self.target = target
        self.driver_TestCase = driver_TestCase
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def driver_TestCase(self):
        return self.__driver_TestCase

    @driver_TestCase.setter
    def driver_TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TestCase__driver_TestCase", None)
        self.__driver_TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_TestCasesList"):
                opp_val = getattr(old_value, "driver_TestCasesList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_TestCasesList"):
                opp_val = getattr(value, "driver_TestCasesList", None)
                if opp_val is None:
                    setattr(value, "driver_TestCasesList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_StopTrace:

    pass
class driver_StartTrace:

    def __init__(self, enablePrimaryFilters: str, enableSecondaryFilters: str, disablePrimaryFilters: str, disableSecondaryFilters: str, configFilePath: str, driver_StartTrace: "driver_Task" = None):
        self.enablePrimaryFilters = enablePrimaryFilters
        self.enableSecondaryFilters = enableSecondaryFilters
        self.disablePrimaryFilters = disablePrimaryFilters
        self.disableSecondaryFilters = disableSecondaryFilters
        self.configFilePath = configFilePath
        self.driver_StartTrace = driver_StartTrace
        
        pass
    @property
    def disableSecondaryFilters(self):
        return self.__disableSecondaryFilters

    @disableSecondaryFilters.setter
    def disableSecondaryFilters(self, disableSecondaryFilters: str):
        self.__disableSecondaryFilters = disableSecondaryFilters


    @property
    def disablePrimaryFilters(self):
        return self.__disablePrimaryFilters

    @disablePrimaryFilters.setter
    def disablePrimaryFilters(self, disablePrimaryFilters: str):
        self.__disablePrimaryFilters = disablePrimaryFilters


    @property
    def enablePrimaryFilters(self):
        return self.__enablePrimaryFilters

    @enablePrimaryFilters.setter
    def enablePrimaryFilters(self, enablePrimaryFilters: str):
        self.__enablePrimaryFilters = enablePrimaryFilters


    @property
    def configFilePath(self):
        return self.__configFilePath

    @configFilePath.setter
    def configFilePath(self, configFilePath: str):
        self.__configFilePath = configFilePath


    @property
    def enableSecondaryFilters(self):
        return self.__enableSecondaryFilters

    @enableSecondaryFilters.setter
    def enableSecondaryFilters(self, enableSecondaryFilters: str):
        self.__enableSecondaryFilters = enableSecondaryFilters


    @property
    def driver_StartTrace(self):
        return self.__driver_StartTrace

    @driver_StartTrace.setter
    def driver_StartTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_StartTrace__driver_StartTrace", None)
        self.__driver_StartTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task43"):
                opp_val = getattr(old_value, "driver_Task43", None)
                if opp_val == self:
                    setattr(old_value, "driver_Task43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task43"):
                opp_val = getattr(value, "driver_Task43", None)
                setattr(value, "driver_Task43", self)

class driver_TransferToSymbian:

    def __init__(self, group: str, driver_TransferToSymbian: "driver_Task" = None, driver_TransferToSymbian51: set["driver_Transfer"] = None):
        self.group = group
        self.driver_TransferToSymbian = driver_TransferToSymbian
        self.driver_TransferToSymbian51 = driver_TransferToSymbian51 if driver_TransferToSymbian51 is not None else set()
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def driver_TransferToSymbian51(self):
        return self.__driver_TransferToSymbian51

    @driver_TransferToSymbian51.setter
    def driver_TransferToSymbian51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TransferToSymbian__driver_TransferToSymbian51", None)
        self.__driver_TransferToSymbian51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Transfer52"):
                    opp_val = getattr(item, "driver_Transfer52", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Transfer52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Transfer52"):
                    opp_val = getattr(item, "driver_Transfer52", None)
                    
                    setattr(item, "driver_Transfer52", self)
                    

    @property
    def driver_TransferToSymbian(self):
        return self.__driver_TransferToSymbian

    @driver_TransferToSymbian.setter
    def driver_TransferToSymbian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TransferToSymbian__driver_TransferToSymbian", None)
        self.__driver_TransferToSymbian = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task27"):
                opp_val = getattr(old_value, "driver_Task27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task27"):
                opp_val = getattr(value, "driver_Task27", None)
                if opp_val is None:
                    setattr(value, "driver_Task27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_Transfer:

    def __init__(self, move: str, pCPath: str, symbianPath: str, driver_Transfer: "driver_RetrieveFromSymbian" = None, driver_Transfer52: "driver_TransferToSymbian" = None):
        self.move = move
        self.pCPath = pCPath
        self.symbianPath = symbianPath
        self.driver_Transfer = driver_Transfer
        self.driver_Transfer52 = driver_Transfer52
        
        pass
    @property
    def pCPath(self):
        return self.__pCPath

    @pCPath.setter
    def pCPath(self, pCPath: str):
        self.__pCPath = pCPath


    @property
    def symbianPath(self):
        return self.__symbianPath

    @symbianPath.setter
    def symbianPath(self, symbianPath: str):
        self.__symbianPath = symbianPath


    @property
    def move(self):
        return self.__move

    @move.setter
    def move(self, move: str):
        self.__move = move


    @property
    def driver_Transfer(self):
        return self.__driver_Transfer

    @driver_Transfer.setter
    def driver_Transfer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Transfer__driver_Transfer", None)
        self.__driver_Transfer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_RetrieveFromSymbian"):
                opp_val = getattr(old_value, "driver_RetrieveFromSymbian", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_RetrieveFromSymbian"):
                opp_val = getattr(value, "driver_RetrieveFromSymbian", None)
                if opp_val is None:
                    setattr(value, "driver_RetrieveFromSymbian", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def driver_Transfer52(self):
        return self.__driver_Transfer52

    @driver_Transfer52.setter
    def driver_Transfer52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Transfer__driver_Transfer52", None)
        self.__driver_Transfer52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_TransferToSymbian51"):
                opp_val = getattr(old_value, "driver_TransferToSymbian51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_TransferToSymbian51"):
                opp_val = getattr(value, "driver_TransferToSymbian51", None)
                if opp_val is None:
                    setattr(value, "driver_TransferToSymbian51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_Reference:

    pass
class driver_FlashROM:

    def __init__(self, pCPath: str, driver_FlashROM: "driver_Task" = None):
        self.pCPath = pCPath
        self.driver_FlashROM = driver_FlashROM
        
        pass
    @property
    def pCPath(self):
        return self.__pCPath

    @pCPath.setter
    def pCPath(self, pCPath: str):
        self.__pCPath = pCPath


    @property
    def driver_FlashROM(self):
        return self.__driver_FlashROM

    @driver_FlashROM.setter
    def driver_FlashROM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_FlashROM__driver_FlashROM", None)
        self.__driver_FlashROM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task41"):
                opp_val = getattr(old_value, "driver_Task41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task41"):
                opp_val = getattr(value, "driver_Task41", None)
                if opp_val is None:
                    setattr(value, "driver_Task41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_RetrieveFromSymbian:

    def __init__(self, group: str, driver_RetrieveFromSymbian: set["driver_Transfer"] = None, driver_RetrieveFromSymbian33: "driver_Task" = None):
        self.group = group
        self.driver_RetrieveFromSymbian = driver_RetrieveFromSymbian if driver_RetrieveFromSymbian is not None else set()
        self.driver_RetrieveFromSymbian33 = driver_RetrieveFromSymbian33
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def driver_RetrieveFromSymbian(self):
        return self.__driver_RetrieveFromSymbian

    @driver_RetrieveFromSymbian.setter
    def driver_RetrieveFromSymbian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_RetrieveFromSymbian__driver_RetrieveFromSymbian", None)
        self.__driver_RetrieveFromSymbian = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Transfer"):
                    opp_val = getattr(item, "driver_Transfer", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Transfer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Transfer"):
                    opp_val = getattr(item, "driver_Transfer", None)
                    
                    setattr(item, "driver_Transfer", self)
                    

    @property
    def driver_RetrieveFromSymbian33(self):
        return self.__driver_RetrieveFromSymbian33

    @driver_RetrieveFromSymbian33.setter
    def driver_RetrieveFromSymbian33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_RetrieveFromSymbian__driver_RetrieveFromSymbian33", None)
        self.__driver_RetrieveFromSymbian33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task32"):
                opp_val = getattr(old_value, "driver_Task32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task32"):
                opp_val = getattr(value, "driver_Task32", None)
                if opp_val is None:
                    setattr(value, "driver_Task32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_TestExecuteScript:

    def __init__(self, pCPath: str, symbianPath: str, driver_TestExecuteScript: "driver_ExecuteOnSymbian" = None, driver_TestExecuteScript48: "driver_TestCasesList" = None):
        self.pCPath = pCPath
        self.symbianPath = symbianPath
        self.driver_TestExecuteScript = driver_TestExecuteScript
        self.driver_TestExecuteScript48 = driver_TestExecuteScript48
        
        pass
    @property
    def symbianPath(self):
        return self.__symbianPath

    @symbianPath.setter
    def symbianPath(self, symbianPath: str):
        self.__symbianPath = symbianPath


    @property
    def pCPath(self):
        return self.__pCPath

    @pCPath.setter
    def pCPath(self, pCPath: str):
        self.__pCPath = pCPath


    @property
    def driver_TestExecuteScript48(self):
        return self.__driver_TestExecuteScript48

    @driver_TestExecuteScript48.setter
    def driver_TestExecuteScript48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TestExecuteScript__driver_TestExecuteScript48", None)
        self.__driver_TestExecuteScript48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_TestCasesList49"):
                opp_val = getattr(old_value, "driver_TestCasesList49", None)
                if opp_val == self:
                    setattr(old_value, "driver_TestCasesList49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_TestCasesList49"):
                opp_val = getattr(value, "driver_TestCasesList49", None)
                setattr(value, "driver_TestCasesList49", self)

    @property
    def driver_TestExecuteScript(self):
        return self.__driver_TestExecuteScript

    @driver_TestExecuteScript.setter
    def driver_TestExecuteScript(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_TestExecuteScript__driver_TestExecuteScript", None)
        self.__driver_TestExecuteScript = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_ExecuteOnSymbian17"):
                opp_val = getattr(old_value, "driver_ExecuteOnSymbian17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_ExecuteOnSymbian17"):
                opp_val = getattr(value, "driver_ExecuteOnSymbian17", None)
                if opp_val is None:
                    setattr(value, "driver_ExecuteOnSymbian17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_ExecuteOnSymbian:

    def __init__(self, group: str, driver_ExecuteOnSymbian19: set["driver_Rtest"] = None, driver_ExecuteOnSymbian: set["driver_CmdSymbian"] = None, driver_ExecuteOnSymbian17: set["driver_TestExecuteScript"] = None, driver_ExecuteOnSymbian30: "driver_Task" = None):
        self.group = group
        self.driver_ExecuteOnSymbian19 = driver_ExecuteOnSymbian19 if driver_ExecuteOnSymbian19 is not None else set()
        self.driver_ExecuteOnSymbian = driver_ExecuteOnSymbian if driver_ExecuteOnSymbian is not None else set()
        self.driver_ExecuteOnSymbian17 = driver_ExecuteOnSymbian17 if driver_ExecuteOnSymbian17 is not None else set()
        self.driver_ExecuteOnSymbian30 = driver_ExecuteOnSymbian30
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def driver_ExecuteOnSymbian19(self):
        return self.__driver_ExecuteOnSymbian19

    @driver_ExecuteOnSymbian19.setter
    def driver_ExecuteOnSymbian19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnSymbian__driver_ExecuteOnSymbian19", None)
        self.__driver_ExecuteOnSymbian19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Rtest"):
                    opp_val = getattr(item, "driver_Rtest", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Rtest", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Rtest"):
                    opp_val = getattr(item, "driver_Rtest", None)
                    
                    setattr(item, "driver_Rtest", self)
                    

    @property
    def driver_ExecuteOnSymbian17(self):
        return self.__driver_ExecuteOnSymbian17

    @driver_ExecuteOnSymbian17.setter
    def driver_ExecuteOnSymbian17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnSymbian__driver_ExecuteOnSymbian17", None)
        self.__driver_ExecuteOnSymbian17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_TestExecuteScript"):
                    opp_val = getattr(item, "driver_TestExecuteScript", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_TestExecuteScript", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_TestExecuteScript"):
                    opp_val = getattr(item, "driver_TestExecuteScript", None)
                    
                    setattr(item, "driver_TestExecuteScript", self)
                    

    @property
    def driver_ExecuteOnSymbian(self):
        return self.__driver_ExecuteOnSymbian

    @driver_ExecuteOnSymbian.setter
    def driver_ExecuteOnSymbian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnSymbian__driver_ExecuteOnSymbian", None)
        self.__driver_ExecuteOnSymbian = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_CmdSymbian"):
                    opp_val = getattr(item, "driver_CmdSymbian", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_CmdSymbian", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_CmdSymbian"):
                    opp_val = getattr(item, "driver_CmdSymbian", None)
                    
                    setattr(item, "driver_CmdSymbian", self)
                    

    @property
    def driver_ExecuteOnSymbian30(self):
        return self.__driver_ExecuteOnSymbian30

    @driver_ExecuteOnSymbian30.setter
    def driver_ExecuteOnSymbian30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnSymbian__driver_ExecuteOnSymbian30", None)
        self.__driver_ExecuteOnSymbian30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task29"):
                opp_val = getattr(old_value, "driver_Task29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task29"):
                opp_val = getattr(value, "driver_Task29", None)
                if opp_val is None:
                    setattr(value, "driver_Task29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_ExecuteOnPC:

    def __init__(self, group: str, driver_ExecuteOnPC: set["driver_CmdPC"] = None, driver_ExecuteOnPC14: set["driver_Build"] = None, driver_ExecuteOnPC25: "driver_Task" = None):
        self.group = group
        self.driver_ExecuteOnPC = driver_ExecuteOnPC if driver_ExecuteOnPC is not None else set()
        self.driver_ExecuteOnPC14 = driver_ExecuteOnPC14 if driver_ExecuteOnPC14 is not None else set()
        self.driver_ExecuteOnPC25 = driver_ExecuteOnPC25
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def driver_ExecuteOnPC(self):
        return self.__driver_ExecuteOnPC

    @driver_ExecuteOnPC.setter
    def driver_ExecuteOnPC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnPC__driver_ExecuteOnPC", None)
        self.__driver_ExecuteOnPC = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_CmdPC"):
                    opp_val = getattr(item, "driver_CmdPC", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_CmdPC", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_CmdPC"):
                    opp_val = getattr(item, "driver_CmdPC", None)
                    
                    setattr(item, "driver_CmdPC", self)
                    

    @property
    def driver_ExecuteOnPC14(self):
        return self.__driver_ExecuteOnPC14

    @driver_ExecuteOnPC14.setter
    def driver_ExecuteOnPC14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnPC__driver_ExecuteOnPC14", None)
        self.__driver_ExecuteOnPC14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Build"):
                    opp_val = getattr(item, "driver_Build", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Build", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Build"):
                    opp_val = getattr(item, "driver_Build", None)
                    
                    setattr(item, "driver_Build", self)
                    

    @property
    def driver_ExecuteOnPC25(self):
        return self.__driver_ExecuteOnPC25

    @driver_ExecuteOnPC25.setter
    def driver_ExecuteOnPC25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_ExecuteOnPC__driver_ExecuteOnPC25", None)
        self.__driver_ExecuteOnPC25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task24"):
                opp_val = getattr(old_value, "driver_Task24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task24"):
                opp_val = getattr(value, "driver_Task24", None)
                if opp_val is None:
                    setattr(value, "driver_Task24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_Rtest:

    def __init__(self, resultFile: str, symbianPath: str, driver_Rtest: "driver_ExecuteOnSymbian" = None):
        self.resultFile = resultFile
        self.symbianPath = symbianPath
        self.driver_Rtest = driver_Rtest
        
        pass
    @property
    def symbianPath(self):
        return self.__symbianPath

    @symbianPath.setter
    def symbianPath(self, symbianPath: str):
        self.__symbianPath = symbianPath


    @property
    def resultFile(self):
        return self.__resultFile

    @resultFile.setter
    def resultFile(self, resultFile: str):
        self.__resultFile = resultFile


    @property
    def driver_Rtest(self):
        return self.__driver_Rtest

    @driver_Rtest.setter
    def driver_Rtest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Rtest__driver_Rtest", None)
        self.__driver_Rtest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_ExecuteOnSymbian19"):
                opp_val = getattr(old_value, "driver_ExecuteOnSymbian19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_ExecuteOnSymbian19"):
                opp_val = getattr(value, "driver_ExecuteOnSymbian19", None)
                if opp_val is None:
                    setattr(value, "driver_ExecuteOnSymbian19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_Task:

    def __init__(self, group: str, name: str, preRebootDevice: str, timeout: str, driver_Task: "driver_Driver" = None, driver_Task21: "driver_Reference" = None, driver_Task41: set["driver_FlashROM"] = None, driver_Task24: set["driver_ExecuteOnPC"] = None, driver_Task27: set["driver_TransferToSymbian"] = None, driver_Task29: set["driver_ExecuteOnSymbian"] = None, driver_Task32: set["driver_RetrieveFromSymbian"] = None, driver_Task35: set["driver_Reference"] = None, driver_Task39: "driver_Task" = None, driver_Task37: set["driver_Task"] = None, driver_Task43: "driver_StartTrace" = None, driver_Task45: "driver_StopTrace" = None):
        self.group = group
        self.name = name
        self.preRebootDevice = preRebootDevice
        self.timeout = timeout
        self.driver_Task = driver_Task
        self.driver_Task21 = driver_Task21
        self.driver_Task41 = driver_Task41 if driver_Task41 is not None else set()
        self.driver_Task24 = driver_Task24 if driver_Task24 is not None else set()
        self.driver_Task27 = driver_Task27 if driver_Task27 is not None else set()
        self.driver_Task29 = driver_Task29 if driver_Task29 is not None else set()
        self.driver_Task32 = driver_Task32 if driver_Task32 is not None else set()
        self.driver_Task35 = driver_Task35 if driver_Task35 is not None else set()
        self.driver_Task39 = driver_Task39
        self.driver_Task37 = driver_Task37 if driver_Task37 is not None else set()
        self.driver_Task43 = driver_Task43
        self.driver_Task45 = driver_Task45
        
        pass
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def preRebootDevice(self):
        return self.__preRebootDevice

    @preRebootDevice.setter
    def preRebootDevice(self, preRebootDevice: str):
        self.__preRebootDevice = preRebootDevice


    @property
    def timeout(self):
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: str):
        self.__timeout = timeout


    @property
    def driver_Task35(self):
        return self.__driver_Task35

    @driver_Task35.setter
    def driver_Task35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task35", None)
        self.__driver_Task35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Reference36"):
                    opp_val = getattr(item, "driver_Reference36", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Reference36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Reference36"):
                    opp_val = getattr(item, "driver_Reference36", None)
                    
                    setattr(item, "driver_Reference36", self)
                    

    @property
    def driver_Task45(self):
        return self.__driver_Task45

    @driver_Task45.setter
    def driver_Task45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task45", None)
        self.__driver_Task45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_StopTrace"):
                opp_val = getattr(old_value, "driver_StopTrace", None)
                if opp_val == self:
                    setattr(old_value, "driver_StopTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_StopTrace"):
                opp_val = getattr(value, "driver_StopTrace", None)
                setattr(value, "driver_StopTrace", self)

    @property
    def driver_Task21(self):
        return self.__driver_Task21

    @driver_Task21.setter
    def driver_Task21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task21", None)
        self.__driver_Task21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Reference"):
                opp_val = getattr(old_value, "driver_Reference", None)
                if opp_val == self:
                    setattr(old_value, "driver_Reference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Reference"):
                opp_val = getattr(value, "driver_Reference", None)
                setattr(value, "driver_Reference", self)

    @property
    def driver_Task(self):
        return self.__driver_Task

    @driver_Task.setter
    def driver_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task", None)
        self.__driver_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Driver9"):
                opp_val = getattr(old_value, "driver_Driver9", None)
                if opp_val == self:
                    setattr(old_value, "driver_Driver9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Driver9"):
                opp_val = getattr(value, "driver_Driver9", None)
                setattr(value, "driver_Driver9", self)

    @property
    def driver_Task29(self):
        return self.__driver_Task29

    @driver_Task29.setter
    def driver_Task29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task29", None)
        self.__driver_Task29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_ExecuteOnSymbian30"):
                    opp_val = getattr(item, "driver_ExecuteOnSymbian30", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_ExecuteOnSymbian30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_ExecuteOnSymbian30"):
                    opp_val = getattr(item, "driver_ExecuteOnSymbian30", None)
                    
                    setattr(item, "driver_ExecuteOnSymbian30", self)
                    

    @property
    def driver_Task43(self):
        return self.__driver_Task43

    @driver_Task43.setter
    def driver_Task43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task43", None)
        self.__driver_Task43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_StartTrace"):
                opp_val = getattr(old_value, "driver_StartTrace", None)
                if opp_val == self:
                    setattr(old_value, "driver_StartTrace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_StartTrace"):
                opp_val = getattr(value, "driver_StartTrace", None)
                setattr(value, "driver_StartTrace", self)

    @property
    def driver_Task24(self):
        return self.__driver_Task24

    @driver_Task24.setter
    def driver_Task24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task24", None)
        self.__driver_Task24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_ExecuteOnPC25"):
                    opp_val = getattr(item, "driver_ExecuteOnPC25", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_ExecuteOnPC25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_ExecuteOnPC25"):
                    opp_val = getattr(item, "driver_ExecuteOnPC25", None)
                    
                    setattr(item, "driver_ExecuteOnPC25", self)
                    

    @property
    def driver_Task37(self):
        return self.__driver_Task37

    @driver_Task37.setter
    def driver_Task37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task37", None)
        self.__driver_Task37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Task39"):
                    opp_val = getattr(item, "driver_Task39", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Task39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Task39"):
                    opp_val = getattr(item, "driver_Task39", None)
                    
                    setattr(item, "driver_Task39", self)
                    

    @property
    def driver_Task41(self):
        return self.__driver_Task41

    @driver_Task41.setter
    def driver_Task41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task41", None)
        self.__driver_Task41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_FlashROM"):
                    opp_val = getattr(item, "driver_FlashROM", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_FlashROM", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_FlashROM"):
                    opp_val = getattr(item, "driver_FlashROM", None)
                    
                    setattr(item, "driver_FlashROM", self)
                    

    @property
    def driver_Task27(self):
        return self.__driver_Task27

    @driver_Task27.setter
    def driver_Task27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task27", None)
        self.__driver_Task27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_TransferToSymbian"):
                    opp_val = getattr(item, "driver_TransferToSymbian", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_TransferToSymbian", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_TransferToSymbian"):
                    opp_val = getattr(item, "driver_TransferToSymbian", None)
                    
                    setattr(item, "driver_TransferToSymbian", self)
                    

    @property
    def driver_Task32(self):
        return self.__driver_Task32

    @driver_Task32.setter
    def driver_Task32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task32", None)
        self.__driver_Task32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_RetrieveFromSymbian33"):
                    opp_val = getattr(item, "driver_RetrieveFromSymbian33", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_RetrieveFromSymbian33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_RetrieveFromSymbian33"):
                    opp_val = getattr(item, "driver_RetrieveFromSymbian33", None)
                    
                    setattr(item, "driver_RetrieveFromSymbian33", self)
                    

    @property
    def driver_Task39(self):
        return self.__driver_Task39

    @driver_Task39.setter
    def driver_Task39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Task__driver_Task39", None)
        self.__driver_Task39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_Task37"):
                opp_val = getattr(old_value, "driver_Task37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_Task37"):
                opp_val = getattr(value, "driver_Task37", None)
                if opp_val is None:
                    setattr(value, "driver_Task37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_DriverInfo:

    pass
class driver_Driver:

    pass
class driver_EStringToStringMapEntry:

    pass
class driver_Info:

    def __init__(self, value: str, key: str, driver_Info: "driver_DriverInfo" = None):
        self.value = value
        self.key = key
        self.driver_Info = driver_Info
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def driver_Info(self):
        return self.__driver_Info

    @driver_Info.setter
    def driver_Info(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Info__driver_Info", None)
        self.__driver_Info = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_DriverInfo11"):
                opp_val = getattr(old_value, "driver_DriverInfo11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_DriverInfo11"):
                opp_val = getattr(value, "driver_DriverInfo11", None)
                if opp_val is None:
                    setattr(value, "driver_DriverInfo11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_DocumentRoot:

    def __init__(self, mixed: str, driver_DocumentRoot: set["driver_EStringToStringMapEntry"] = None, driver_DocumentRoot2: set["driver_EStringToStringMapEntry"] = None, driver_DocumentRoot5: set["driver_Driver"] = None):
        self.mixed = mixed
        self.driver_DocumentRoot = driver_DocumentRoot if driver_DocumentRoot is not None else set()
        self.driver_DocumentRoot2 = driver_DocumentRoot2 if driver_DocumentRoot2 is not None else set()
        self.driver_DocumentRoot5 = driver_DocumentRoot5 if driver_DocumentRoot5 is not None else set()
        
        pass
    @property
    def mixed(self):
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed


    @property
    def driver_DocumentRoot5(self):
        return self.__driver_DocumentRoot5

    @driver_DocumentRoot5.setter
    def driver_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_DocumentRoot__driver_DocumentRoot5", None)
        self.__driver_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_Driver"):
                    opp_val = getattr(item, "driver_Driver", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_Driver", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_Driver"):
                    opp_val = getattr(item, "driver_Driver", None)
                    
                    setattr(item, "driver_Driver", self)
                    

    @property
    def driver_DocumentRoot2(self):
        return self.__driver_DocumentRoot2

    @driver_DocumentRoot2.setter
    def driver_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_DocumentRoot__driver_DocumentRoot2", None)
        self.__driver_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "driver_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "driver_EStringToStringMapEntry3", None)
                    
                    setattr(item, "driver_EStringToStringMapEntry3", self)
                    

    @property
    def driver_DocumentRoot(self):
        return self.__driver_DocumentRoot

    @driver_DocumentRoot.setter
    def driver_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_DocumentRoot__driver_DocumentRoot", None)
        self.__driver_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "driver_EStringToStringMapEntry"):
                    opp_val = getattr(item, "driver_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "driver_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "driver_EStringToStringMapEntry"):
                    opp_val = getattr(item, "driver_EStringToStringMapEntry", None)
                    
                    setattr(item, "driver_EStringToStringMapEntry", self)
                    

class driver_CmdSymbian:

    def __init__(self, argument: str, output: str, statCommand: str, sync: str, driver_CmdSymbian: "driver_ExecuteOnSymbian" = None):
        self.argument = argument
        self.output = output
        self.statCommand = statCommand
        self.sync = sync
        self.driver_CmdSymbian = driver_CmdSymbian
        
        pass
    @property
    def output(self):
        return self.__output

    @output.setter
    def output(self, output: str):
        self.__output = output


    @property
    def sync(self):
        return self.__sync

    @sync.setter
    def sync(self, sync: str):
        self.__sync = sync


    @property
    def argument(self):
        return self.__argument

    @argument.setter
    def argument(self, argument: str):
        self.__argument = argument


    @property
    def statCommand(self):
        return self.__statCommand

    @statCommand.setter
    def statCommand(self, statCommand: str):
        self.__statCommand = statCommand


    @property
    def driver_CmdSymbian(self):
        return self.__driver_CmdSymbian

    @driver_CmdSymbian.setter
    def driver_CmdSymbian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_CmdSymbian__driver_CmdSymbian", None)
        self.__driver_CmdSymbian = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_ExecuteOnSymbian"):
                opp_val = getattr(old_value, "driver_ExecuteOnSymbian", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_ExecuteOnSymbian"):
                opp_val = getattr(value, "driver_ExecuteOnSymbian", None)
                if opp_val is None:
                    setattr(value, "driver_ExecuteOnSymbian", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_CmdPC:

    def __init__(self, value: str, phase: str, sync: str, uRI: str, driver_CmdPC: "driver_ExecuteOnPC" = None):
        self.value = value
        self.phase = phase
        self.sync = sync
        self.uRI = uRI
        self.driver_CmdPC = driver_CmdPC
        
        pass
    @property
    def sync(self):
        return self.__sync

    @sync.setter
    def sync(self, sync: str):
        self.__sync = sync


    @property
    def uRI(self):
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def phase(self):
        return self.__phase

    @phase.setter
    def phase(self, phase: str):
        self.__phase = phase


    @property
    def driver_CmdPC(self):
        return self.__driver_CmdPC

    @driver_CmdPC.setter
    def driver_CmdPC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_CmdPC__driver_CmdPC", None)
        self.__driver_CmdPC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_ExecuteOnPC"):
                opp_val = getattr(old_value, "driver_ExecuteOnPC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_ExecuteOnPC"):
                opp_val = getattr(value, "driver_ExecuteOnPC", None)
                if opp_val is None:
                    setattr(value, "driver_ExecuteOnPC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class driver_Build:

    def __init__(self, componentName: str, testBuild: str, uRI: str, driver_Build: "driver_ExecuteOnPC" = None):
        self.componentName = componentName
        self.testBuild = testBuild
        self.uRI = uRI
        self.driver_Build = driver_Build
        
        pass
    @property
    def componentName(self):
        return self.__componentName

    @componentName.setter
    def componentName(self, componentName: str):
        self.__componentName = componentName


    @property
    def testBuild(self):
        return self.__testBuild

    @testBuild.setter
    def testBuild(self, testBuild: str):
        self.__testBuild = testBuild


    @property
    def uRI(self):
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI


    @property
    def driver_Build(self):
        return self.__driver_Build

    @driver_Build.setter
    def driver_Build(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_driver_Build__driver_Build", None)
        self.__driver_Build = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "driver_ExecuteOnPC14"):
                opp_val = getattr(old_value, "driver_ExecuteOnPC14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "driver_ExecuteOnPC14"):
                opp_val = getattr(value, "driver_ExecuteOnPC14", None)
                if opp_val is None:
                    setattr(value, "driver_ExecuteOnPC14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
