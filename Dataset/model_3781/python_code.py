from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class product_ProductDomainModel:

    def __init__(self, name: str, elements: str, product_ProductDomainModel: "product_ProductDomainModels" = None):
        self.name = name
        self.elements = elements
        self.product_ProductDomainModel = product_ProductDomainModel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def elements(self) -> str:
        return self.__elements

    @elements.setter
    def elements(self, elements: str):
        self.__elements = elements

    @property
    def product_ProductDomainModel(self):
        return self.__product_ProductDomainModel

    @product_ProductDomainModel.setter
    def product_ProductDomainModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductDomainModel__product_ProductDomainModel", None)
        self.__product_ProductDomainModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductDomainModels49"):
                opp_val = getattr(old_value, "product_ProductDomainModels49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductDomainModels49"):
                opp_val = getattr(value, "product_ProductDomainModels49", None)
                if opp_val is None:
                    setattr(value, "product_ProductDomainModels49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class product_ProductFeatureConfiguration:

    def __init__(self, name: str, attribute: str, max: int, min: int, isSelected: bool, product_ProductFeatureConfiguration: "product_ProductFeaturesConfiguration" = None, product_ProductFeatureConfiguration47: "product_ProductFeatureConfiguration" = None, product_ProductFeatureConfiguration45: set["product_ProductFeatureConfiguration"] = None):
        self.name = name
        self.attribute = attribute
        self.max = max
        self.min = min
        self.isSelected = isSelected
        self.product_ProductFeatureConfiguration = product_ProductFeatureConfiguration
        self.product_ProductFeatureConfiguration47 = product_ProductFeatureConfiguration47
        self.product_ProductFeatureConfiguration45 = product_ProductFeatureConfiguration45 if product_ProductFeatureConfiguration45 is not None else set()
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def isSelected(self) -> bool:
        return self.__isSelected

    @isSelected.setter
    def isSelected(self, isSelected: bool):
        self.__isSelected = isSelected

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def product_ProductFeatureConfiguration(self):
        return self.__product_ProductFeatureConfiguration

    @product_ProductFeatureConfiguration.setter
    def product_ProductFeatureConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFeatureConfiguration__product_ProductFeatureConfiguration", None)
        self.__product_ProductFeatureConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductFeaturesConfiguration44"):
                opp_val = getattr(old_value, "product_ProductFeaturesConfiguration44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductFeaturesConfiguration44"):
                opp_val = getattr(value, "product_ProductFeaturesConfiguration44", None)
                if opp_val is None:
                    setattr(value, "product_ProductFeaturesConfiguration44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductFeatureConfiguration45(self):
        return self.__product_ProductFeatureConfiguration45

    @product_ProductFeatureConfiguration45.setter
    def product_ProductFeatureConfiguration45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFeatureConfiguration__product_ProductFeatureConfiguration45", None)
        self.__product_ProductFeatureConfiguration45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductFeatureConfiguration47"):
                    opp_val = getattr(item, "product_ProductFeatureConfiguration47", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductFeatureConfiguration47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductFeatureConfiguration47"):
                    opp_val = getattr(item, "product_ProductFeatureConfiguration47", None)
                    
                    setattr(item, "product_ProductFeatureConfiguration47", self)
                    

    @property
    def product_ProductFeatureConfiguration47(self):
        return self.__product_ProductFeatureConfiguration47

    @product_ProductFeatureConfiguration47.setter
    def product_ProductFeatureConfiguration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFeatureConfiguration__product_ProductFeatureConfiguration47", None)
        self.__product_ProductFeatureConfiguration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductFeatureConfiguration45"):
                opp_val = getattr(old_value, "product_ProductFeatureConfiguration45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductFeatureConfiguration45"):
                opp_val = getattr(value, "product_ProductFeatureConfiguration45", None)
                if opp_val is None:
                    setattr(value, "product_ProductFeatureConfiguration45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ProductEntity:

    pass
class product_ProductClass(ProductEntity):

    pass
class product_ProductAspect(ProductEntity):

    pass
class product_ProductFragment(ProductEntity):

    def __init__(self, content: str, product_ProductFragment: "product_ProductFragmentContainer" = None):
        self.content = content
        self.product_ProductFragment = product_ProductFragment
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def product_ProductFragment(self):
        return self.__product_ProductFragment

    @product_ProductFragment.setter
    def product_ProductFragment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFragment__product_ProductFragment", None)
        self.__product_ProductFragment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductFragmentContainer42"):
                opp_val = getattr(old_value, "product_ProductFragmentContainer42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductFragmentContainer42"):
                opp_val = getattr(value, "product_ProductFragmentContainer42", None)
                if opp_val is None:
                    setattr(value, "product_ProductFragmentContainer42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class product_ProductEntity:

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class product_ProductTemplate(ProductEntity):

    def __init__(self, generateToPath: str, product_ProductTemplate: "product_ProductResourcesContainer" = None, product_ProductTemplate28: "product_ProductComponent" = None, product_ProductTemplate40: "product_ProductFolder" = None):
        self.generateToPath = generateToPath
        self.product_ProductTemplate = product_ProductTemplate
        self.product_ProductTemplate28 = product_ProductTemplate28
        self.product_ProductTemplate40 = product_ProductTemplate40
        
    @property
    def generateToPath(self) -> str:
        return self.__generateToPath

    @generateToPath.setter
    def generateToPath(self, generateToPath: str):
        self.__generateToPath = generateToPath

    @property
    def product_ProductTemplate(self):
        return self.__product_ProductTemplate

    @product_ProductTemplate.setter
    def product_ProductTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductTemplate__product_ProductTemplate", None)
        self.__product_ProductTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductResourcesContainer18"):
                opp_val = getattr(old_value, "product_ProductResourcesContainer18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductResourcesContainer18"):
                opp_val = getattr(value, "product_ProductResourcesContainer18", None)
                if opp_val is None:
                    setattr(value, "product_ProductResourcesContainer18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductTemplate40(self):
        return self.__product_ProductTemplate40

    @product_ProductTemplate40.setter
    def product_ProductTemplate40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductTemplate__product_ProductTemplate40", None)
        self.__product_ProductTemplate40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductFolder39"):
                opp_val = getattr(old_value, "product_ProductFolder39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductFolder39"):
                opp_val = getattr(value, "product_ProductFolder39", None)
                if opp_val is None:
                    setattr(value, "product_ProductFolder39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductTemplate28(self):
        return self.__product_ProductTemplate28

    @product_ProductTemplate28.setter
    def product_ProductTemplate28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductTemplate__product_ProductTemplate28", None)
        self.__product_ProductTemplate28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductComponent27"):
                opp_val = getattr(old_value, "product_ProductComponent27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductComponent27"):
                opp_val = getattr(value, "product_ProductComponent27", None)
                if opp_val is None:
                    setattr(value, "product_ProductComponent27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class product_ProductFile(ProductEntity):

    pass
class product_ProductFolder(ProductEntity):

    pass
class product_ProductComponent(ProductEntity):

    pass
class product_ProductResourcesContainer:

    def __init__(self, name: str, product_ProductResourcesContainer: "product_ProductImplementationElements" = None, product_ProductResourcesContainer14: set["product_ProductFolder"] = None, product_ProductResourcesContainer16: set["product_ProductFile"] = None, product_ProductResourcesContainer18: set["product_ProductTemplate"] = None):
        self.name = name
        self.product_ProductResourcesContainer = product_ProductResourcesContainer
        self.product_ProductResourcesContainer14 = product_ProductResourcesContainer14 if product_ProductResourcesContainer14 is not None else set()
        self.product_ProductResourcesContainer16 = product_ProductResourcesContainer16 if product_ProductResourcesContainer16 is not None else set()
        self.product_ProductResourcesContainer18 = product_ProductResourcesContainer18 if product_ProductResourcesContainer18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product_ProductResourcesContainer14(self):
        return self.__product_ProductResourcesContainer14

    @product_ProductResourcesContainer14.setter
    def product_ProductResourcesContainer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductResourcesContainer__product_ProductResourcesContainer14", None)
        self.__product_ProductResourcesContainer14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductFolder"):
                    opp_val = getattr(item, "product_ProductFolder", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductFolder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductFolder"):
                    opp_val = getattr(item, "product_ProductFolder", None)
                    
                    setattr(item, "product_ProductFolder", self)
                    

    @property
    def product_ProductResourcesContainer16(self):
        return self.__product_ProductResourcesContainer16

    @product_ProductResourcesContainer16.setter
    def product_ProductResourcesContainer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductResourcesContainer__product_ProductResourcesContainer16", None)
        self.__product_ProductResourcesContainer16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductFile"):
                    opp_val = getattr(item, "product_ProductFile", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductFile"):
                    opp_val = getattr(item, "product_ProductFile", None)
                    
                    setattr(item, "product_ProductFile", self)
                    

    @property
    def product_ProductResourcesContainer(self):
        return self.__product_ProductResourcesContainer

    @product_ProductResourcesContainer.setter
    def product_ProductResourcesContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductResourcesContainer__product_ProductResourcesContainer", None)
        self.__product_ProductResourcesContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductImplementationElements10"):
                opp_val = getattr(old_value, "product_ProductImplementationElements10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductImplementationElements10"):
                opp_val = getattr(value, "product_ProductImplementationElements10", None)
                if opp_val is None:
                    setattr(value, "product_ProductImplementationElements10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductResourcesContainer18(self):
        return self.__product_ProductResourcesContainer18

    @product_ProductResourcesContainer18.setter
    def product_ProductResourcesContainer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductResourcesContainer__product_ProductResourcesContainer18", None)
        self.__product_ProductResourcesContainer18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductTemplate"):
                    opp_val = getattr(item, "product_ProductTemplate", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductTemplate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductTemplate"):
                    opp_val = getattr(item, "product_ProductTemplate", None)
                    
                    setattr(item, "product_ProductTemplate", self)
                    

class product_ProductFragmentContainer:

    def __init__(self, name: str, product_ProductFragmentContainer: "product_ProductImplementationElements" = None, product_ProductFragmentContainer42: set["product_ProductFragment"] = None):
        self.name = name
        self.product_ProductFragmentContainer = product_ProductFragmentContainer
        self.product_ProductFragmentContainer42 = product_ProductFragmentContainer42 if product_ProductFragmentContainer42 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product_ProductFragmentContainer(self):
        return self.__product_ProductFragmentContainer

    @product_ProductFragmentContainer.setter
    def product_ProductFragmentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFragmentContainer__product_ProductFragmentContainer", None)
        self.__product_ProductFragmentContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductImplementationElements8"):
                opp_val = getattr(old_value, "product_ProductImplementationElements8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductImplementationElements8"):
                opp_val = getattr(value, "product_ProductImplementationElements8", None)
                if opp_val is None:
                    setattr(value, "product_ProductImplementationElements8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductFragmentContainer42(self):
        return self.__product_ProductFragmentContainer42

    @product_ProductFragmentContainer42.setter
    def product_ProductFragmentContainer42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFragmentContainer__product_ProductFragmentContainer42", None)
        self.__product_ProductFragmentContainer42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductFragment"):
                    opp_val = getattr(item, "product_ProductFragment", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductFragment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductFragment"):
                    opp_val = getattr(item, "product_ProductFragment", None)
                    
                    setattr(item, "product_ProductFragment", self)
                    

class product_ProductContainer:

    def __init__(self, name: str, product_ProductContainer: "product_ProductImplementationElements" = None, product_ProductContainer12: set["product_ProductComponent"] = None):
        self.name = name
        self.product_ProductContainer = product_ProductContainer
        self.product_ProductContainer12 = product_ProductContainer12 if product_ProductContainer12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def product_ProductContainer(self):
        return self.__product_ProductContainer

    @product_ProductContainer.setter
    def product_ProductContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductContainer__product_ProductContainer", None)
        self.__product_ProductContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_ProductImplementationElements6"):
                opp_val = getattr(old_value, "product_ProductImplementationElements6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_ProductImplementationElements6"):
                opp_val = getattr(value, "product_ProductImplementationElements6", None)
                if opp_val is None:
                    setattr(value, "product_ProductImplementationElements6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def product_ProductContainer12(self):
        return self.__product_ProductContainer12

    @product_ProductContainer12.setter
    def product_ProductContainer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductContainer__product_ProductContainer12", None)
        self.__product_ProductContainer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductComponent"):
                    opp_val = getattr(item, "product_ProductComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductComponent"):
                    opp_val = getattr(item, "product_ProductComponent", None)
                    
                    setattr(item, "product_ProductComponent", self)
                    

class product_ProductDomainModels:

    pass
class product_ProductFeaturesConfiguration:

    def __init__(self, name: str, attribute: str, product_ProductFeaturesConfiguration: "product_Product" = None, product_ProductFeaturesConfiguration44: set["product_ProductFeatureConfiguration"] = None):
        self.name = name
        self.attribute = attribute
        self.product_ProductFeaturesConfiguration = product_ProductFeaturesConfiguration
        self.product_ProductFeaturesConfiguration44 = product_ProductFeaturesConfiguration44 if product_ProductFeaturesConfiguration44 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def product_ProductFeaturesConfiguration44(self):
        return self.__product_ProductFeaturesConfiguration44

    @product_ProductFeaturesConfiguration44.setter
    def product_ProductFeaturesConfiguration44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFeaturesConfiguration__product_ProductFeaturesConfiguration44", None)
        self.__product_ProductFeaturesConfiguration44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "product_ProductFeatureConfiguration"):
                    opp_val = getattr(item, "product_ProductFeatureConfiguration", None)
                    
                    if opp_val == self:
                        setattr(item, "product_ProductFeatureConfiguration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "product_ProductFeatureConfiguration"):
                    opp_val = getattr(item, "product_ProductFeatureConfiguration", None)
                    
                    setattr(item, "product_ProductFeatureConfiguration", self)
                    

    @property
    def product_ProductFeaturesConfiguration(self):
        return self.__product_ProductFeaturesConfiguration

    @product_ProductFeaturesConfiguration.setter
    def product_ProductFeaturesConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_product_ProductFeaturesConfiguration__product_ProductFeaturesConfiguration", None)
        self.__product_ProductFeaturesConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "product_Product2"):
                opp_val = getattr(old_value, "product_Product2", None)
                if opp_val == self:
                    setattr(old_value, "product_Product2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "product_Product2"):
                opp_val = getattr(value, "product_Product2", None)
                setattr(value, "product_Product2", self)

class product_ProductImplementationElements:

    pass
class product_Product:

    pass