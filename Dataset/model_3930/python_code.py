from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class configDsl_Generator:

    def __init__(self, name: str, bundle: str, genClass: str, configDsl_Generator: "configDsl_Config" = None, configDsl_Generator3: "configDsl_Config" = None):
        self.name = name
        self.bundle = bundle
        self.genClass = genClass
        self.configDsl_Generator = configDsl_Generator
        self.configDsl_Generator3 = configDsl_Generator3
        
    @property
    def bundle(self) -> str:
        return self.__bundle

    @bundle.setter
    def bundle(self, bundle: str):
        self.__bundle = bundle

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def genClass(self) -> str:
        return self.__genClass

    @genClass.setter
    def genClass(self, genClass: str):
        self.__genClass = genClass

    @property
    def configDsl_Generator3(self):
        return self.__configDsl_Generator3

    @configDsl_Generator3.setter
    def configDsl_Generator3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_configDsl_Generator__configDsl_Generator3", None)
        self.__configDsl_Generator3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configDsl_Config2"):
                opp_val = getattr(old_value, "configDsl_Config2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configDsl_Config2"):
                opp_val = getattr(value, "configDsl_Config2", None)
                if opp_val is None:
                    setattr(value, "configDsl_Config2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def configDsl_Generator(self):
        return self.__configDsl_Generator

    @configDsl_Generator.setter
    def configDsl_Generator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_configDsl_Generator__configDsl_Generator", None)
        self.__configDsl_Generator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configDsl_Config"):
                opp_val = getattr(old_value, "configDsl_Config", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configDsl_Config"):
                opp_val = getattr(value, "configDsl_Config", None)
                if opp_val is None:
                    setattr(value, "configDsl_Config", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class configDsl_Config:

    def __init__(self, appName: str, mainClass: str, srcFolder: str, outFolder: str, configDsl_Config: set["configDsl_Generator"] = None, configDsl_Config2: set["configDsl_Generator"] = None):
        self.appName = appName
        self.mainClass = mainClass
        self.srcFolder = srcFolder
        self.outFolder = outFolder
        self.configDsl_Config = configDsl_Config if configDsl_Config is not None else set()
        self.configDsl_Config2 = configDsl_Config2 if configDsl_Config2 is not None else set()
        
    @property
    def outFolder(self) -> str:
        return self.__outFolder

    @outFolder.setter
    def outFolder(self, outFolder: str):
        self.__outFolder = outFolder

    @property
    def srcFolder(self) -> str:
        return self.__srcFolder

    @srcFolder.setter
    def srcFolder(self, srcFolder: str):
        self.__srcFolder = srcFolder

    @property
    def mainClass(self) -> str:
        return self.__mainClass

    @mainClass.setter
    def mainClass(self, mainClass: str):
        self.__mainClass = mainClass

    @property
    def appName(self) -> str:
        return self.__appName

    @appName.setter
    def appName(self, appName: str):
        self.__appName = appName

    @property
    def configDsl_Config(self):
        return self.__configDsl_Config

    @configDsl_Config.setter
    def configDsl_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_configDsl_Config__configDsl_Config", None)
        self.__configDsl_Config = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "configDsl_Generator"):
                    opp_val = getattr(item, "configDsl_Generator", None)
                    
                    if opp_val == self:
                        setattr(item, "configDsl_Generator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "configDsl_Generator"):
                    opp_val = getattr(item, "configDsl_Generator", None)
                    
                    setattr(item, "configDsl_Generator", self)
                    

    @property
    def configDsl_Config2(self):
        return self.__configDsl_Config2

    @configDsl_Config2.setter
    def configDsl_Config2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_configDsl_Config__configDsl_Config2", None)
        self.__configDsl_Config2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "configDsl_Generator3"):
                    opp_val = getattr(item, "configDsl_Generator3", None)
                    
                    if opp_val == self:
                        setattr(item, "configDsl_Generator3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "configDsl_Generator3"):
                    opp_val = getattr(item, "configDsl_Generator3", None)
                    
                    setattr(item, "configDsl_Generator3", self)
                    
