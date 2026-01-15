from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class decobat_Service:

    def __init__(self, code: str, name: str, shortDescription: str, description: str, hourlyCostPrice: str, hourlyBilledPrice: str):
        self.code = code
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.hourlyCostPrice = hourlyCostPrice
        self.hourlyBilledPrice = hourlyBilledPrice
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def hourlyBilledPrice(self) -> str:
        return self.__hourlyBilledPrice

    @hourlyBilledPrice.setter
    def hourlyBilledPrice(self, hourlyBilledPrice: str):
        self.__hourlyBilledPrice = hourlyBilledPrice

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hourlyCostPrice(self) -> str:
        return self.__hourlyCostPrice

    @hourlyCostPrice.setter
    def hourlyCostPrice(self, hourlyCostPrice: str):
        self.__hourlyCostPrice = hourlyCostPrice

class decobat_Object:

    def __init__(self, code: str, name: str, shortDescription: str, description: str, decobat_Object: set["decobat_Library"] = None):
        self.code = code
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.decobat_Object = decobat_Object if decobat_Object is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def decobat_Object(self):
        return self.__decobat_Object

    @decobat_Object.setter
    def decobat_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Object__decobat_Object", None)
        self.__decobat_Object = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decobat_Library15"):
                    opp_val = getattr(item, "decobat_Library15", None)
                    
                    if opp_val == self:
                        setattr(item, "decobat_Library15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decobat_Library15"):
                    opp_val = getattr(item, "decobat_Library15", None)
                    
                    setattr(item, "decobat_Library15", self)
                    

class decobat_Level:

    def __init__(self, code: str, name: str, shortDescription: str, description: str, decobat_Level: "decobat_Plan" = None, decobat_Level12: set["decobat_Library"] = None):
        self.code = code
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.decobat_Level = decobat_Level
        self.decobat_Level12 = decobat_Level12 if decobat_Level12 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def decobat_Level(self):
        return self.__decobat_Level

    @decobat_Level.setter
    def decobat_Level(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Level__decobat_Level", None)
        self.__decobat_Level = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Plan10"):
                opp_val = getattr(old_value, "decobat_Plan10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Plan10"):
                opp_val = getattr(value, "decobat_Plan10", None)
                if opp_val is None:
                    setattr(value, "decobat_Plan10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def decobat_Level12(self):
        return self.__decobat_Level12

    @decobat_Level12.setter
    def decobat_Level12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Level__decobat_Level12", None)
        self.__decobat_Level12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decobat_Library13"):
                    opp_val = getattr(item, "decobat_Library13", None)
                    
                    if opp_val == self:
                        setattr(item, "decobat_Library13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decobat_Library13"):
                    opp_val = getattr(item, "decobat_Library13", None)
                    
                    setattr(item, "decobat_Library13", self)
                    

class decobat_Supplier:

    def __init__(self, code: str, name: str, address: str, zip: str, city: str, country: str, fax: str, phone: str, email: str, decobat_Supplier: "decobat_Product" = None):
        self.code = code
        self.name = name
        self.address = address
        self.zip = zip
        self.city = city
        self.country = country
        self.fax = fax
        self.phone = phone
        self.email = email
        self.decobat_Supplier = decobat_Supplier
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def fax(self) -> str:
        return self.__fax

    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def decobat_Supplier(self):
        return self.__decobat_Supplier

    @decobat_Supplier.setter
    def decobat_Supplier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Supplier__decobat_Supplier", None)
        self.__decobat_Supplier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Product"):
                opp_val = getattr(old_value, "decobat_Product", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Product", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Product"):
                opp_val = getattr(value, "decobat_Product", None)
                setattr(value, "decobat_Product", self)

class decobat_Product:

    def __init__(self, name: str, shortDescription: str, description: str, created: date, update: date, unitCostPrice: str, unitBilledPrice: str, unitWeight: str, height: str, width: str, depth: str, decobat_Product: "decobat_Supplier" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.created = created
        self.update = update
        self.unitCostPrice = unitCostPrice
        self.unitBilledPrice = unitBilledPrice
        self.unitWeight = unitWeight
        self.height = height
        self.width = width
        self.depth = depth
        self.decobat_Product = decobat_Product
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def unitBilledPrice(self) -> str:
        return self.__unitBilledPrice

    @unitBilledPrice.setter
    def unitBilledPrice(self, unitBilledPrice: str):
        self.__unitBilledPrice = unitBilledPrice

    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def unitCostPrice(self) -> str:
        return self.__unitCostPrice

    @unitCostPrice.setter
    def unitCostPrice(self, unitCostPrice: str):
        self.__unitCostPrice = unitCostPrice

    @property
    def unitWeight(self) -> str:
        return self.__unitWeight

    @unitWeight.setter
    def unitWeight(self, unitWeight: str):
        self.__unitWeight = unitWeight

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def update(self) -> date:
        return self.__update

    @update.setter
    def update(self, update: date):
        self.__update = update

    @property
    def decobat_Product(self):
        return self.__decobat_Product

    @decobat_Product.setter
    def decobat_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Product__decobat_Product", None)
        self.__decobat_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Supplier"):
                opp_val = getattr(old_value, "decobat_Supplier", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Supplier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Supplier"):
                opp_val = getattr(value, "decobat_Supplier", None)
                setattr(value, "decobat_Supplier", self)

class decobat_LibraryCategory:

    def __init__(self, name: str, shortDescription: str, description: str, created: date, decobat_LibraryCategory: "decobat_Library" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.created = created
        self.decobat_LibraryCategory = decobat_LibraryCategory
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def decobat_LibraryCategory(self):
        return self.__decobat_LibraryCategory

    @decobat_LibraryCategory.setter
    def decobat_LibraryCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_LibraryCategory__decobat_LibraryCategory", None)
        self.__decobat_LibraryCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Library"):
                opp_val = getattr(old_value, "decobat_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Library"):
                opp_val = getattr(value, "decobat_Library", None)
                if opp_val is None:
                    setattr(value, "decobat_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class decobat_Library:

    def __init__(self, name: str, shortDescription: str, description: str, created: date, update: date, height: str, width: str, depth: str, decobat_Library: set["decobat_LibraryCategory"] = None, decobat_Library13: "decobat_Level" = None, decobat_Library15: "decobat_Object" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.created = created
        self.update = update
        self.height = height
        self.width = width
        self.depth = depth
        self.decobat_Library = decobat_Library if decobat_Library is not None else set()
        self.decobat_Library13 = decobat_Library13
        self.decobat_Library15 = decobat_Library15
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def update(self) -> date:
        return self.__update

    @update.setter
    def update(self, update: date):
        self.__update = update

    @property
    def depth(self) -> str:
        return self.__depth

    @depth.setter
    def depth(self, depth: str):
        self.__depth = depth

    @property
    def decobat_Library(self):
        return self.__decobat_Library

    @decobat_Library.setter
    def decobat_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Library__decobat_Library", None)
        self.__decobat_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decobat_LibraryCategory"):
                    opp_val = getattr(item, "decobat_LibraryCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "decobat_LibraryCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decobat_LibraryCategory"):
                    opp_val = getattr(item, "decobat_LibraryCategory", None)
                    
                    setattr(item, "decobat_LibraryCategory", self)
                    

    @property
    def decobat_Library15(self):
        return self.__decobat_Library15

    @decobat_Library15.setter
    def decobat_Library15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Library__decobat_Library15", None)
        self.__decobat_Library15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Object"):
                opp_val = getattr(old_value, "decobat_Object", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Object"):
                opp_val = getattr(value, "decobat_Object", None)
                if opp_val is None:
                    setattr(value, "decobat_Object", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def decobat_Library13(self):
        return self.__decobat_Library13

    @decobat_Library13.setter
    def decobat_Library13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Library__decobat_Library13", None)
        self.__decobat_Library13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Level12"):
                opp_val = getattr(old_value, "decobat_Level12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Level12"):
                opp_val = getattr(value, "decobat_Level12", None)
                if opp_val is None:
                    setattr(value, "decobat_Level12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class decobat_Customer:

    def __init__(self, code: str, name: str, address: str, zip: str, city: str, country: str, fax: str, phone: str, email: str, decobat_Customer: "decobat_Project" = None):
        self.code = code
        self.name = name
        self.address = address
        self.zip = zip
        self.city = city
        self.country = country
        self.fax = fax
        self.phone = phone
        self.email = email
        self.decobat_Customer = decobat_Customer
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, zip: str):
        self.__zip = zip

    @property
    def fax(self) -> str:
        return self.__fax

    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def decobat_Customer(self):
        return self.__decobat_Customer

    @decobat_Customer.setter
    def decobat_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Customer__decobat_Customer", None)
        self.__decobat_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Project6"):
                opp_val = getattr(old_value, "decobat_Project6", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Project6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Project6"):
                opp_val = getattr(value, "decobat_Project6", None)
                setattr(value, "decobat_Project6", self)

class decobat_Plan:

    def __init__(self, code: str, name: str, shortDescription: str, description: str, decobat_Plan: "decobat_Project" = None, decobat_Plan10: set["decobat_Level"] = None):
        self.code = code
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.decobat_Plan = decobat_Plan
        self.decobat_Plan10 = decobat_Plan10 if decobat_Plan10 is not None else set()
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def decobat_Plan(self):
        return self.__decobat_Plan

    @decobat_Plan.setter
    def decobat_Plan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Plan__decobat_Plan", None)
        self.__decobat_Plan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Project4"):
                opp_val = getattr(old_value, "decobat_Project4", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Project4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Project4"):
                opp_val = getattr(value, "decobat_Project4", None)
                setattr(value, "decobat_Project4", self)

    @property
    def decobat_Plan10(self):
        return self.__decobat_Plan10

    @decobat_Plan10.setter
    def decobat_Plan10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Plan__decobat_Plan10", None)
        self.__decobat_Plan10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decobat_Level"):
                    opp_val = getattr(item, "decobat_Level", None)
                    
                    if opp_val == self:
                        setattr(item, "decobat_Level", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decobat_Level"):
                    opp_val = getattr(item, "decobat_Level", None)
                    
                    setattr(item, "decobat_Level", self)
                    

class decobat_ProjectCategory:

    def __init__(self, name: str, shortDescription: str, description: str, created: date, decobat_ProjectCategory: "decobat_Project" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.created = created
        self.decobat_ProjectCategory = decobat_ProjectCategory
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def decobat_ProjectCategory(self):
        return self.__decobat_ProjectCategory

    @decobat_ProjectCategory.setter
    def decobat_ProjectCategory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_ProjectCategory__decobat_ProjectCategory", None)
        self.__decobat_ProjectCategory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Project2"):
                opp_val = getattr(old_value, "decobat_Project2", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Project2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Project2"):
                opp_val = getattr(value, "decobat_Project2", None)
                setattr(value, "decobat_Project2", self)

class decobat_ProjectRevision:

    def __init__(self, shortDescription: str, description: str, update: date, comment: str, decobat_ProjectRevision: "decobat_Project" = None):
        self.shortDescription = shortDescription
        self.description = description
        self.update = update
        self.comment = comment
        self.decobat_ProjectRevision = decobat_ProjectRevision
        
    @property
    def update(self) -> date:
        return self.__update

    @update.setter
    def update(self, update: date):
        self.__update = update

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def decobat_ProjectRevision(self):
        return self.__decobat_ProjectRevision

    @decobat_ProjectRevision.setter
    def decobat_ProjectRevision(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_ProjectRevision__decobat_ProjectRevision", None)
        self.__decobat_ProjectRevision = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Project"):
                opp_val = getattr(old_value, "decobat_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Project"):
                opp_val = getattr(value, "decobat_Project", None)
                if opp_val is None:
                    setattr(value, "decobat_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class decobat_Project:

    def __init__(self, name: str, shortDescription: str, description: str, created: date, closed: date, decobat_Project: set["decobat_ProjectRevision"] = None, decobat_Project2: "decobat_ProjectCategory" = None, decobat_Project4: "decobat_Plan" = None, decobat_Project6: "decobat_Customer" = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.created = created
        self.closed = closed
        self.decobat_Project = decobat_Project if decobat_Project is not None else set()
        self.decobat_Project2 = decobat_Project2
        self.decobat_Project4 = decobat_Project4
        self.decobat_Project6 = decobat_Project6
        
    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def closed(self) -> date:
        return self.__closed

    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def created(self) -> date:
        return self.__created

    @created.setter
    def created(self, created: date):
        self.__created = created

    @property
    def decobat_Project2(self):
        return self.__decobat_Project2

    @decobat_Project2.setter
    def decobat_Project2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Project__decobat_Project2", None)
        self.__decobat_Project2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_ProjectCategory"):
                opp_val = getattr(old_value, "decobat_ProjectCategory", None)
                if opp_val == self:
                    setattr(old_value, "decobat_ProjectCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_ProjectCategory"):
                opp_val = getattr(value, "decobat_ProjectCategory", None)
                setattr(value, "decobat_ProjectCategory", self)

    @property
    def decobat_Project4(self):
        return self.__decobat_Project4

    @decobat_Project4.setter
    def decobat_Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Project__decobat_Project4", None)
        self.__decobat_Project4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Plan"):
                opp_val = getattr(old_value, "decobat_Plan", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Plan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Plan"):
                opp_val = getattr(value, "decobat_Plan", None)
                setattr(value, "decobat_Plan", self)

    @property
    def decobat_Project6(self):
        return self.__decobat_Project6

    @decobat_Project6.setter
    def decobat_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Project__decobat_Project6", None)
        self.__decobat_Project6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "decobat_Customer"):
                opp_val = getattr(old_value, "decobat_Customer", None)
                if opp_val == self:
                    setattr(old_value, "decobat_Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "decobat_Customer"):
                opp_val = getattr(value, "decobat_Customer", None)
                setattr(value, "decobat_Customer", self)

    @property
    def decobat_Project(self):
        return self.__decobat_Project

    @decobat_Project.setter
    def decobat_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_decobat_Project__decobat_Project", None)
        self.__decobat_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "decobat_ProjectRevision"):
                    opp_val = getattr(item, "decobat_ProjectRevision", None)
                    
                    if opp_val == self:
                        setattr(item, "decobat_ProjectRevision", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "decobat_ProjectRevision"):
                    opp_val = getattr(item, "decobat_ProjectRevision", None)
                    
                    setattr(item, "decobat_ProjectRevision", self)
                    
