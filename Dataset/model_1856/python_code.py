from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class application_Mappers:

    pass
class application_MappingLayer:

    pass
class application_ApplicationMapper:

    def __init__(self, uid: str, name: str, application_ApplicationMapper: "application_ApplicationMappers" = None, application_ApplicationMapper48: "application_Mappers" = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationMapper = application_ApplicationMapper
        self.application_ApplicationMapper48 = application_ApplicationMapper48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def application_ApplicationMapper(self):
        return self.__application_ApplicationMapper

    @application_ApplicationMapper.setter
    def application_ApplicationMapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMapper__application_ApplicationMapper", None)
        self.__application_ApplicationMapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMappers44"):
                opp_val = getattr(old_value, "application_ApplicationMappers44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMappers44"):
                opp_val = getattr(value, "application_ApplicationMappers44", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationMappers44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_ApplicationMapper48(self):
        return self.__application_ApplicationMapper48

    @application_ApplicationMapper48.setter
    def application_ApplicationMapper48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMapper__application_ApplicationMapper48", None)
        self.__application_ApplicationMapper48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Mappers"):
                opp_val = getattr(old_value, "application_Mappers", None)
                if opp_val == self:
                    setattr(old_value, "application_Mappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Mappers"):
                opp_val = getattr(value, "application_Mappers", None)
                setattr(value, "application_Mappers", self)

class application_Recipes:

    pass
class application_ApplicationRecipe:

    def __init__(self, uid: str, name: str, application_ApplicationRecipe: "application_ApplicationRecipes" = None, application_ApplicationRecipe42: set["application_Recipes"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationRecipe = application_ApplicationRecipe
        self.application_ApplicationRecipe42 = application_ApplicationRecipe42 if application_ApplicationRecipe42 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationRecipe42(self):
        return self.__application_ApplicationRecipe42

    @application_ApplicationRecipe42.setter
    def application_ApplicationRecipe42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRecipe__application_ApplicationRecipe42", None)
        self.__application_ApplicationRecipe42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Recipes"):
                    opp_val = getattr(item, "application_Recipes", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Recipes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Recipes"):
                    opp_val = getattr(item, "application_Recipes", None)
                    
                    setattr(item, "application_Recipes", self)
                    

    @property
    def application_ApplicationRecipe(self):
        return self.__application_ApplicationRecipe

    @application_ApplicationRecipe.setter
    def application_ApplicationRecipe(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRecipe__application_ApplicationRecipe", None)
        self.__application_ApplicationRecipe = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationRecipes40"):
                opp_val = getattr(old_value, "application_ApplicationRecipes40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationRecipes40"):
                opp_val = getattr(value, "application_ApplicationRecipes40", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationRecipes40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class application_Form:

    pass
class application_ApplicationUIPackage:

    def __init__(self, uid: str, name: str, application_ApplicationUIPackage: "application_ApplicationUILayer" = None, application_ApplicationUIPackage38: set["application_Form"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationUIPackage = application_ApplicationUIPackage
        self.application_ApplicationUIPackage38 = application_ApplicationUIPackage38 if application_ApplicationUIPackage38 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def application_ApplicationUIPackage(self):
        return self.__application_ApplicationUIPackage

    @application_ApplicationUIPackage.setter
    def application_ApplicationUIPackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationUIPackage__application_ApplicationUIPackage", None)
        self.__application_ApplicationUIPackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationUILayer36"):
                opp_val = getattr(old_value, "application_ApplicationUILayer36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationUILayer36"):
                opp_val = getattr(value, "application_ApplicationUILayer36", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationUILayer36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_ApplicationUIPackage38(self):
        return self.__application_ApplicationUIPackage38

    @application_ApplicationUIPackage38.setter
    def application_ApplicationUIPackage38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationUIPackage__application_ApplicationUIPackage38", None)
        self.__application_ApplicationUIPackage38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Form"):
                    opp_val = getattr(item, "application_Form", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Form", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Form"):
                    opp_val = getattr(item, "application_Form", None)
                    
                    setattr(item, "application_Form", self)
                    

class application_StyleLibrary:

    pass
class application_Roles:

    pass
class application_ApplicationRealm:

    def __init__(self, uid: str, name: str, application_ApplicationRealm: "application_ApplicationRealms" = None, application_ApplicationRealm30: "application_Roles" = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationRealm = application_ApplicationRealm
        self.application_ApplicationRealm30 = application_ApplicationRealm30
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationRealm(self):
        return self.__application_ApplicationRealm

    @application_ApplicationRealm.setter
    def application_ApplicationRealm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRealm__application_ApplicationRealm", None)
        self.__application_ApplicationRealm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationRealms28"):
                opp_val = getattr(old_value, "application_ApplicationRealms28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationRealms28"):
                opp_val = getattr(value, "application_ApplicationRealms28", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationRealms28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_ApplicationRealm30(self):
        return self.__application_ApplicationRealm30

    @application_ApplicationRealm30.setter
    def application_ApplicationRealm30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRealm__application_ApplicationRealm30", None)
        self.__application_ApplicationRealm30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Roles"):
                opp_val = getattr(old_value, "application_Roles", None)
                if opp_val == self:
                    setattr(old_value, "application_Roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Roles"):
                opp_val = getattr(value, "application_Roles", None)
                setattr(value, "application_Roles", self)

class application_MessageLibrary:

    pass
class application_ApplicationStyle:

    def __init__(self, uid: str, name: str, application_ApplicationStyle: "application_ApplicationStyleLibraries" = None, application_ApplicationStyle34: set["application_StyleLibrary"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationStyle = application_ApplicationStyle
        self.application_ApplicationStyle34 = application_ApplicationStyle34 if application_ApplicationStyle34 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def application_ApplicationStyle34(self):
        return self.__application_ApplicationStyle34

    @application_ApplicationStyle34.setter
    def application_ApplicationStyle34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationStyle__application_ApplicationStyle34", None)
        self.__application_ApplicationStyle34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_StyleLibrary"):
                    opp_val = getattr(item, "application_StyleLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "application_StyleLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_StyleLibrary"):
                    opp_val = getattr(item, "application_StyleLibrary", None)
                    
                    setattr(item, "application_StyleLibrary", self)
                    

    @property
    def application_ApplicationStyle(self):
        return self.__application_ApplicationStyle

    @application_ApplicationStyle.setter
    def application_ApplicationStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationStyle__application_ApplicationStyle", None)
        self.__application_ApplicationStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationStyleLibraries32"):
                opp_val = getattr(old_value, "application_ApplicationStyleLibraries32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationStyleLibraries32"):
                opp_val = getattr(value, "application_ApplicationStyleLibraries32", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationStyleLibraries32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class application_ApplicationLanguages:

    def __init__(self, uid: str, name: str, application_ApplicationLanguages: "application_ApplicationMessageLibraries" = None, application_ApplicationLanguages24: set["application_Language"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationLanguages = application_ApplicationLanguages
        self.application_ApplicationLanguages24 = application_ApplicationLanguages24 if application_ApplicationLanguages24 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationLanguages24(self):
        return self.__application_ApplicationLanguages24

    @application_ApplicationLanguages24.setter
    def application_ApplicationLanguages24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationLanguages__application_ApplicationLanguages24", None)
        self.__application_ApplicationLanguages24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Language"):
                    opp_val = getattr(item, "application_Language", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Language", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Language"):
                    opp_val = getattr(item, "application_Language", None)
                    
                    setattr(item, "application_Language", self)
                    

    @property
    def application_ApplicationLanguages(self):
        return self.__application_ApplicationLanguages

    @application_ApplicationLanguages.setter
    def application_ApplicationLanguages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationLanguages__application_ApplicationLanguages", None)
        self.__application_ApplicationLanguages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMessageLibraries22"):
                opp_val = getattr(old_value, "application_ApplicationMessageLibraries22", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationMessageLibraries22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMessageLibraries22"):
                opp_val = getattr(value, "application_ApplicationMessageLibraries22", None)
                setattr(value, "application_ApplicationMessageLibraries22", self)

class application_ApplicationMessageLibrary:

    def __init__(self, uid: str, name: str, application_ApplicationMessageLibrary: "application_ApplicationMessageLibraries" = None, application_ApplicationMessageLibrary26: set["application_MessageLibrary"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationMessageLibrary = application_ApplicationMessageLibrary
        self.application_ApplicationMessageLibrary26 = application_ApplicationMessageLibrary26 if application_ApplicationMessageLibrary26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def application_ApplicationMessageLibrary26(self):
        return self.__application_ApplicationMessageLibrary26

    @application_ApplicationMessageLibrary26.setter
    def application_ApplicationMessageLibrary26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMessageLibrary__application_ApplicationMessageLibrary26", None)
        self.__application_ApplicationMessageLibrary26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_MessageLibrary"):
                    opp_val = getattr(item, "application_MessageLibrary", None)
                    
                    if opp_val == self:
                        setattr(item, "application_MessageLibrary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_MessageLibrary"):
                    opp_val = getattr(item, "application_MessageLibrary", None)
                    
                    setattr(item, "application_MessageLibrary", self)
                    

    @property
    def application_ApplicationMessageLibrary(self):
        return self.__application_ApplicationMessageLibrary

    @application_ApplicationMessageLibrary.setter
    def application_ApplicationMessageLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMessageLibrary__application_ApplicationMessageLibrary", None)
        self.__application_ApplicationMessageLibrary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMessageLibraries20"):
                opp_val = getattr(old_value, "application_ApplicationMessageLibraries20", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationMessageLibraries20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMessageLibraries20"):
                opp_val = getattr(value, "application_ApplicationMessageLibraries20", None)
                setattr(value, "application_ApplicationMessageLibraries20", self)

class application_EnterpriseInfrastructure:

    pass
class application_ApplicationInfrastructureLayer:

    def __init__(self, uid: str, name: str, application_ApplicationInfrastructureLayer: "application_ApplicationInfrastructureLayers" = None, application_ApplicationInfrastructureLayer18: set["application_EnterpriseInfrastructure"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationInfrastructureLayer = application_ApplicationInfrastructureLayer
        self.application_ApplicationInfrastructureLayer18 = application_ApplicationInfrastructureLayer18 if application_ApplicationInfrastructureLayer18 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationInfrastructureLayer18(self):
        return self.__application_ApplicationInfrastructureLayer18

    @application_ApplicationInfrastructureLayer18.setter
    def application_ApplicationInfrastructureLayer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationInfrastructureLayer__application_ApplicationInfrastructureLayer18", None)
        self.__application_ApplicationInfrastructureLayer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_EnterpriseInfrastructure"):
                    opp_val = getattr(item, "application_EnterpriseInfrastructure", None)
                    
                    if opp_val == self:
                        setattr(item, "application_EnterpriseInfrastructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_EnterpriseInfrastructure"):
                    opp_val = getattr(item, "application_EnterpriseInfrastructure", None)
                    
                    setattr(item, "application_EnterpriseInfrastructure", self)
                    

    @property
    def application_ApplicationInfrastructureLayer(self):
        return self.__application_ApplicationInfrastructureLayer

    @application_ApplicationInfrastructureLayer.setter
    def application_ApplicationInfrastructureLayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationInfrastructureLayer__application_ApplicationInfrastructureLayer", None)
        self.__application_ApplicationInfrastructureLayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationInfrastructureLayers16"):
                opp_val = getattr(old_value, "application_ApplicationInfrastructureLayers16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationInfrastructureLayers16"):
                opp_val = getattr(value, "application_ApplicationInfrastructureLayers16", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationInfrastructureLayers16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class application_Language:

    pass
class application_ApplicationMessageLibraries:

    def __init__(self, uid: str, name: str, application_ApplicationMessageLibraries: "application_Application" = None, application_ApplicationMessageLibraries20: "application_ApplicationMessageLibrary" = None, application_ApplicationMessageLibraries22: "application_ApplicationLanguages" = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationMessageLibraries = application_ApplicationMessageLibraries
        self.application_ApplicationMessageLibraries20 = application_ApplicationMessageLibraries20
        self.application_ApplicationMessageLibraries22 = application_ApplicationMessageLibraries22
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationMessageLibraries20(self):
        return self.__application_ApplicationMessageLibraries20

    @application_ApplicationMessageLibraries20.setter
    def application_ApplicationMessageLibraries20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMessageLibraries__application_ApplicationMessageLibraries20", None)
        self.__application_ApplicationMessageLibraries20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMessageLibrary"):
                opp_val = getattr(old_value, "application_ApplicationMessageLibrary", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationMessageLibrary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMessageLibrary"):
                opp_val = getattr(value, "application_ApplicationMessageLibrary", None)
                setattr(value, "application_ApplicationMessageLibrary", self)

    @property
    def application_ApplicationMessageLibraries22(self):
        return self.__application_ApplicationMessageLibraries22

    @application_ApplicationMessageLibraries22.setter
    def application_ApplicationMessageLibraries22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMessageLibraries__application_ApplicationMessageLibraries22", None)
        self.__application_ApplicationMessageLibraries22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationLanguages"):
                opp_val = getattr(old_value, "application_ApplicationLanguages", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationLanguages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationLanguages"):
                opp_val = getattr(value, "application_ApplicationLanguages", None)
                setattr(value, "application_ApplicationLanguages", self)

    @property
    def application_ApplicationMessageLibraries(self):
        return self.__application_ApplicationMessageLibraries

    @application_ApplicationMessageLibraries.setter
    def application_ApplicationMessageLibraries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMessageLibraries__application_ApplicationMessageLibraries", None)
        self.__application_ApplicationMessageLibraries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application14"):
                opp_val = getattr(old_value, "application_Application14", None)
                if opp_val == self:
                    setattr(old_value, "application_Application14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application14"):
                opp_val = getattr(value, "application_Application14", None)
                setattr(value, "application_Application14", self)

class application_ApplicationRealms:

    def __init__(self, uid: str, name: str, application_ApplicationRealms: "application_Application" = None, application_ApplicationRealms28: set["application_ApplicationRealm"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationRealms = application_ApplicationRealms
        self.application_ApplicationRealms28 = application_ApplicationRealms28 if application_ApplicationRealms28 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationRealms28(self):
        return self.__application_ApplicationRealms28

    @application_ApplicationRealms28.setter
    def application_ApplicationRealms28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRealms__application_ApplicationRealms28", None)
        self.__application_ApplicationRealms28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationRealm"):
                    opp_val = getattr(item, "application_ApplicationRealm", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationRealm", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationRealm"):
                    opp_val = getattr(item, "application_ApplicationRealm", None)
                    
                    setattr(item, "application_ApplicationRealm", self)
                    

    @property
    def application_ApplicationRealms(self):
        return self.__application_ApplicationRealms

    @application_ApplicationRealms.setter
    def application_ApplicationRealms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRealms__application_ApplicationRealms", None)
        self.__application_ApplicationRealms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application12"):
                opp_val = getattr(old_value, "application_Application12", None)
                if opp_val == self:
                    setattr(old_value, "application_Application12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application12"):
                opp_val = getattr(value, "application_Application12", None)
                setattr(value, "application_Application12", self)

class application_ApplicationStyleLibraries:

    def __init__(self, uid: str, name: str, application_ApplicationStyleLibraries: "application_Application" = None, application_ApplicationStyleLibraries32: set["application_ApplicationStyle"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationStyleLibraries = application_ApplicationStyleLibraries
        self.application_ApplicationStyleLibraries32 = application_ApplicationStyleLibraries32 if application_ApplicationStyleLibraries32 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationStyleLibraries32(self):
        return self.__application_ApplicationStyleLibraries32

    @application_ApplicationStyleLibraries32.setter
    def application_ApplicationStyleLibraries32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationStyleLibraries__application_ApplicationStyleLibraries32", None)
        self.__application_ApplicationStyleLibraries32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationStyle"):
                    opp_val = getattr(item, "application_ApplicationStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationStyle"):
                    opp_val = getattr(item, "application_ApplicationStyle", None)
                    
                    setattr(item, "application_ApplicationStyle", self)
                    

    @property
    def application_ApplicationStyleLibraries(self):
        return self.__application_ApplicationStyleLibraries

    @application_ApplicationStyleLibraries.setter
    def application_ApplicationStyleLibraries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationStyleLibraries__application_ApplicationStyleLibraries", None)
        self.__application_ApplicationStyleLibraries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application10"):
                opp_val = getattr(old_value, "application_Application10", None)
                if opp_val == self:
                    setattr(old_value, "application_Application10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application10"):
                opp_val = getattr(value, "application_Application10", None)
                setattr(value, "application_Application10", self)

class application_ApplicationInfrastructureLayers:

    def __init__(self, uid: str, name: str, application_ApplicationInfrastructureLayers: "application_Application" = None, application_ApplicationInfrastructureLayers16: set["application_ApplicationInfrastructureLayer"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationInfrastructureLayers = application_ApplicationInfrastructureLayers
        self.application_ApplicationInfrastructureLayers16 = application_ApplicationInfrastructureLayers16 if application_ApplicationInfrastructureLayers16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def application_ApplicationInfrastructureLayers16(self):
        return self.__application_ApplicationInfrastructureLayers16

    @application_ApplicationInfrastructureLayers16.setter
    def application_ApplicationInfrastructureLayers16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationInfrastructureLayers__application_ApplicationInfrastructureLayers16", None)
        self.__application_ApplicationInfrastructureLayers16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationInfrastructureLayer"):
                    opp_val = getattr(item, "application_ApplicationInfrastructureLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationInfrastructureLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationInfrastructureLayer"):
                    opp_val = getattr(item, "application_ApplicationInfrastructureLayer", None)
                    
                    setattr(item, "application_ApplicationInfrastructureLayer", self)
                    

    @property
    def application_ApplicationInfrastructureLayers(self):
        return self.__application_ApplicationInfrastructureLayers

    @application_ApplicationInfrastructureLayers.setter
    def application_ApplicationInfrastructureLayers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationInfrastructureLayers__application_ApplicationInfrastructureLayers", None)
        self.__application_ApplicationInfrastructureLayers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application8"):
                opp_val = getattr(old_value, "application_Application8", None)
                if opp_val == self:
                    setattr(old_value, "application_Application8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application8"):
                opp_val = getattr(value, "application_Application8", None)
                setattr(value, "application_Application8", self)

class application_ApplicationUILayer:

    def __init__(self, uid: str, name: str, application_ApplicationUILayer: "application_Application" = None, application_ApplicationUILayer36: set["application_ApplicationUIPackage"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationUILayer = application_ApplicationUILayer
        self.application_ApplicationUILayer36 = application_ApplicationUILayer36 if application_ApplicationUILayer36 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationUILayer36(self):
        return self.__application_ApplicationUILayer36

    @application_ApplicationUILayer36.setter
    def application_ApplicationUILayer36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationUILayer__application_ApplicationUILayer36", None)
        self.__application_ApplicationUILayer36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationUIPackage"):
                    opp_val = getattr(item, "application_ApplicationUIPackage", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationUIPackage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationUIPackage"):
                    opp_val = getattr(item, "application_ApplicationUIPackage", None)
                    
                    setattr(item, "application_ApplicationUIPackage", self)
                    

    @property
    def application_ApplicationUILayer(self):
        return self.__application_ApplicationUILayer

    @application_ApplicationUILayer.setter
    def application_ApplicationUILayer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationUILayer__application_ApplicationUILayer", None)
        self.__application_ApplicationUILayer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application6"):
                opp_val = getattr(old_value, "application_Application6", None)
                if opp_val == self:
                    setattr(old_value, "application_Application6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application6"):
                opp_val = getattr(value, "application_Application6", None)
                setattr(value, "application_Application6", self)

class application_ApplicationMappers:

    def __init__(self, uid: str, name: str, application_ApplicationMappers: "application_Application" = None, application_ApplicationMappers44: set["application_ApplicationMapper"] = None, application_ApplicationMappers46: set["application_MappingLayer"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationMappers = application_ApplicationMappers
        self.application_ApplicationMappers44 = application_ApplicationMappers44 if application_ApplicationMappers44 is not None else set()
        self.application_ApplicationMappers46 = application_ApplicationMappers46 if application_ApplicationMappers46 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationMappers46(self):
        return self.__application_ApplicationMappers46

    @application_ApplicationMappers46.setter
    def application_ApplicationMappers46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMappers__application_ApplicationMappers46", None)
        self.__application_ApplicationMappers46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_MappingLayer"):
                    opp_val = getattr(item, "application_MappingLayer", None)
                    
                    if opp_val == self:
                        setattr(item, "application_MappingLayer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_MappingLayer"):
                    opp_val = getattr(item, "application_MappingLayer", None)
                    
                    setattr(item, "application_MappingLayer", self)
                    

    @property
    def application_ApplicationMappers44(self):
        return self.__application_ApplicationMappers44

    @application_ApplicationMappers44.setter
    def application_ApplicationMappers44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMappers__application_ApplicationMappers44", None)
        self.__application_ApplicationMappers44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationMapper"):
                    opp_val = getattr(item, "application_ApplicationMapper", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationMapper", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationMapper"):
                    opp_val = getattr(item, "application_ApplicationMapper", None)
                    
                    setattr(item, "application_ApplicationMapper", self)
                    

    @property
    def application_ApplicationMappers(self):
        return self.__application_ApplicationMappers

    @application_ApplicationMappers.setter
    def application_ApplicationMappers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationMappers__application_ApplicationMappers", None)
        self.__application_ApplicationMappers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application4"):
                opp_val = getattr(old_value, "application_Application4", None)
                if opp_val == self:
                    setattr(old_value, "application_Application4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application4"):
                opp_val = getattr(value, "application_Application4", None)
                setattr(value, "application_Application4", self)

class application_ApplicationRecipes:

    def __init__(self, name: str, uid: str, application_ApplicationRecipes: "application_Application" = None, application_ApplicationRecipes40: set["application_ApplicationRecipe"] = None):
        self.name = name
        self.uid = uid
        self.application_ApplicationRecipes = application_ApplicationRecipes
        self.application_ApplicationRecipes40 = application_ApplicationRecipes40 if application_ApplicationRecipes40 is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationRecipes40(self):
        return self.__application_ApplicationRecipes40

    @application_ApplicationRecipes40.setter
    def application_ApplicationRecipes40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRecipes__application_ApplicationRecipes40", None)
        self.__application_ApplicationRecipes40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_ApplicationRecipe"):
                    opp_val = getattr(item, "application_ApplicationRecipe", None)
                    
                    if opp_val == self:
                        setattr(item, "application_ApplicationRecipe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_ApplicationRecipe"):
                    opp_val = getattr(item, "application_ApplicationRecipe", None)
                    
                    setattr(item, "application_ApplicationRecipe", self)
                    

    @property
    def application_ApplicationRecipes(self):
        return self.__application_ApplicationRecipes

    @application_ApplicationRecipes.setter
    def application_ApplicationRecipes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationRecipes__application_ApplicationRecipes", None)
        self.__application_ApplicationRecipes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_Application2"):
                opp_val = getattr(old_value, "application_Application2", None)
                if opp_val == self:
                    setattr(old_value, "application_Application2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_Application2"):
                opp_val = getattr(value, "application_Application2", None)
                setattr(value, "application_Application2", self)

class application_Application:

    def __init__(self, uid: str, name: str, application_Application: "application_ApplicationGroup" = None, application_Application2: "application_ApplicationRecipes" = None, application_Application4: "application_ApplicationMappers" = None, application_Application6: "application_ApplicationUILayer" = None, application_Application8: "application_ApplicationInfrastructureLayers" = None, application_Application10: "application_ApplicationStyleLibraries" = None, application_Application12: "application_ApplicationRealms" = None, application_Application14: "application_ApplicationMessageLibraries" = None):
        self.uid = uid
        self.name = name
        self.application_Application = application_Application
        self.application_Application2 = application_Application2
        self.application_Application4 = application_Application4
        self.application_Application6 = application_Application6
        self.application_Application8 = application_Application8
        self.application_Application10 = application_Application10
        self.application_Application12 = application_Application12
        self.application_Application14 = application_Application14
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_Application10(self):
        return self.__application_Application10

    @application_Application10.setter
    def application_Application10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application10", None)
        self.__application_Application10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationStyleLibraries"):
                opp_val = getattr(old_value, "application_ApplicationStyleLibraries", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationStyleLibraries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationStyleLibraries"):
                opp_val = getattr(value, "application_ApplicationStyleLibraries", None)
                setattr(value, "application_ApplicationStyleLibraries", self)

    @property
    def application_Application(self):
        return self.__application_Application

    @application_Application.setter
    def application_Application(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application", None)
        self.__application_Application = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationGroup"):
                opp_val = getattr(old_value, "application_ApplicationGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationGroup"):
                opp_val = getattr(value, "application_ApplicationGroup", None)
                if opp_val is None:
                    setattr(value, "application_ApplicationGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def application_Application12(self):
        return self.__application_Application12

    @application_Application12.setter
    def application_Application12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application12", None)
        self.__application_Application12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationRealms"):
                opp_val = getattr(old_value, "application_ApplicationRealms", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationRealms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationRealms"):
                opp_val = getattr(value, "application_ApplicationRealms", None)
                setattr(value, "application_ApplicationRealms", self)

    @property
    def application_Application4(self):
        return self.__application_Application4

    @application_Application4.setter
    def application_Application4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application4", None)
        self.__application_Application4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMappers"):
                opp_val = getattr(old_value, "application_ApplicationMappers", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationMappers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMappers"):
                opp_val = getattr(value, "application_ApplicationMappers", None)
                setattr(value, "application_ApplicationMappers", self)

    @property
    def application_Application14(self):
        return self.__application_Application14

    @application_Application14.setter
    def application_Application14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application14", None)
        self.__application_Application14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationMessageLibraries"):
                opp_val = getattr(old_value, "application_ApplicationMessageLibraries", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationMessageLibraries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationMessageLibraries"):
                opp_val = getattr(value, "application_ApplicationMessageLibraries", None)
                setattr(value, "application_ApplicationMessageLibraries", self)

    @property
    def application_Application6(self):
        return self.__application_Application6

    @application_Application6.setter
    def application_Application6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application6", None)
        self.__application_Application6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationUILayer"):
                opp_val = getattr(old_value, "application_ApplicationUILayer", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationUILayer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationUILayer"):
                opp_val = getattr(value, "application_ApplicationUILayer", None)
                setattr(value, "application_ApplicationUILayer", self)

    @property
    def application_Application2(self):
        return self.__application_Application2

    @application_Application2.setter
    def application_Application2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application2", None)
        self.__application_Application2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationRecipes"):
                opp_val = getattr(old_value, "application_ApplicationRecipes", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationRecipes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationRecipes"):
                opp_val = getattr(value, "application_ApplicationRecipes", None)
                setattr(value, "application_ApplicationRecipes", self)

    @property
    def application_Application8(self):
        return self.__application_Application8

    @application_Application8.setter
    def application_Application8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_Application__application_Application8", None)
        self.__application_Application8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "application_ApplicationInfrastructureLayers"):
                opp_val = getattr(old_value, "application_ApplicationInfrastructureLayers", None)
                if opp_val == self:
                    setattr(old_value, "application_ApplicationInfrastructureLayers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "application_ApplicationInfrastructureLayers"):
                opp_val = getattr(value, "application_ApplicationInfrastructureLayers", None)
                setattr(value, "application_ApplicationInfrastructureLayers", self)

class application_ApplicationGroup:

    def __init__(self, uid: str, name: str, application_ApplicationGroup: set["application_Application"] = None):
        self.uid = uid
        self.name = name
        self.application_ApplicationGroup = application_ApplicationGroup if application_ApplicationGroup is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def application_ApplicationGroup(self):
        return self.__application_ApplicationGroup

    @application_ApplicationGroup.setter
    def application_ApplicationGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_application_ApplicationGroup__application_ApplicationGroup", None)
        self.__application_ApplicationGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "application_Application"):
                    opp_val = getattr(item, "application_Application", None)
                    
                    if opp_val == self:
                        setattr(item, "application_Application", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "application_Application"):
                    opp_val = getattr(item, "application_Application", None)
                    
                    setattr(item, "application_Application", self)
                    
