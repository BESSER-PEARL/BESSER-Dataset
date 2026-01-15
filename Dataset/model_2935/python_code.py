from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class FormTypes:

    pass
class extended_FormReport(FormTypes):

    def __init__(self, filter: str, order: str, pagination: str):
        self.filter = filter
        self.order = order
        self.pagination = pagination
        
    @property
    def filter(self) -> str:
        return self.__filter

    @filter.setter
    def filter(self, filter: str):
        self.__filter = filter

    @property
    def pagination(self) -> str:
        return self.__pagination

    @pagination.setter
    def pagination(self, pagination: str):
        self.__pagination = pagination

    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

class extended_FormNewEntityOnly(FormTypes):

    pass
class extended_Form(FormTypes):

    def __init__(self, get: str, post: str, put: str, delete: str):
        self.get = get
        self.post = post
        self.put = put
        self.delete = delete
        
    @property
    def delete(self) -> str:
        return self.__delete

    @delete.setter
    def delete(self, delete: str):
        self.__delete = delete

    @property
    def post(self) -> str:
        return self.__post

    @post.setter
    def post(self, post: str):
        self.__post = post

    @property
    def put(self) -> str:
        return self.__put

    @put.setter
    def put(self, put: str):
        self.__put = put

    @property
    def get(self) -> str:
        return self.__get

    @get.setter
    def get(self, get: str):
        self.__get = get

class extended_Feature:

    def __init__(self, required: str, min: int, max: int, name: str, extended_Feature: "extended_Entity" = None, extended_Feature10: "extended_AbstractType" = None):
        self.required = required
        self.min = min
        self.max = max
        self.name = name
        self.extended_Feature = extended_Feature
        self.extended_Feature10 = extended_Feature10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def required(self) -> str:
        return self.__required

    @required.setter
    def required(self, required: str):
        self.__required = required

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def extended_Feature10(self):
        return self.__extended_Feature10

    @extended_Feature10.setter
    def extended_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Feature__extended_Feature10", None)
        self.__extended_Feature10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_AbstractType"):
                opp_val = getattr(old_value, "extended_AbstractType", None)
                if opp_val == self:
                    setattr(old_value, "extended_AbstractType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_AbstractType"):
                opp_val = getattr(value, "extended_AbstractType", None)
                setattr(value, "extended_AbstractType", self)

    @property
    def extended_Feature(self):
        return self.__extended_Feature

    @extended_Feature.setter
    def extended_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Feature__extended_Feature", None)
        self.__extended_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_Entity8"):
                opp_val = getattr(old_value, "extended_Entity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_Entity8"):
                opp_val = getattr(value, "extended_Entity8", None)
                if opp_val is None:
                    setattr(value, "extended_Entity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractType:

    pass
class extended_EntityType(AbstractType):

    pass
class extended_DataType(AbstractType):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class extended_AbstractType:

    pass
class AbstractElement:

    pass
class extended_FormTypes(AbstractElement):

    def __init__(self, name: str, extended_FormTypes: "extended_Page" = None, extended_FormTypes13: "extended_Entity" = None):
        self.name = name
        self.extended_FormTypes = extended_FormTypes
        self.extended_FormTypes13 = extended_FormTypes13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extended_FormTypes13(self):
        return self.__extended_FormTypes13

    @extended_FormTypes13.setter
    def extended_FormTypes13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_FormTypes__extended_FormTypes13", None)
        self.__extended_FormTypes13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_Entity14"):
                opp_val = getattr(old_value, "extended_Entity14", None)
                if opp_val == self:
                    setattr(old_value, "extended_Entity14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_Entity14"):
                opp_val = getattr(value, "extended_Entity14", None)
                setattr(value, "extended_Entity14", self)

    @property
    def extended_FormTypes(self):
        return self.__extended_FormTypes

    @extended_FormTypes.setter
    def extended_FormTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_FormTypes__extended_FormTypes", None)
        self.__extended_FormTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_Page"):
                opp_val = getattr(old_value, "extended_Page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_Page"):
                opp_val = getattr(value, "extended_Page", None)
                if opp_val is None:
                    setattr(value, "extended_Page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extended_Page(AbstractElement):

    def __init__(self, name: str, title: str, header: str, footer: str, extended_Page: set["extended_FormTypes"] = None):
        self.name = name
        self.title = title
        self.header = header
        self.footer = footer
        self.extended_Page = extended_Page if extended_Page is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

    @property
    def footer(self) -> str:
        return self.__footer

    @footer.setter
    def footer(self, footer: str):
        self.__footer = footer

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extended_Page(self):
        return self.__extended_Page

    @extended_Page.setter
    def extended_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Page__extended_Page", None)
        self.__extended_Page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extended_FormTypes"):
                    opp_val = getattr(item, "extended_FormTypes", None)
                    
                    if opp_val == self:
                        setattr(item, "extended_FormTypes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extended_FormTypes"):
                    opp_val = getattr(item, "extended_FormTypes", None)
                    
                    setattr(item, "extended_FormTypes", self)
                    

class extended_Entity(AbstractElement):

    def __init__(self, name: str, extended_Entity: "extended_EntityType" = None, extended_Entity6: "extended_Entity" = None, extended_Entity4: "extended_Entity" = None, extended_Entity8: set["extended_Feature"] = None, extended_Entity14: "extended_FormTypes" = None):
        self.name = name
        self.extended_Entity = extended_Entity
        self.extended_Entity6 = extended_Entity6
        self.extended_Entity4 = extended_Entity4
        self.extended_Entity8 = extended_Entity8 if extended_Entity8 is not None else set()
        self.extended_Entity14 = extended_Entity14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extended_Entity(self):
        return self.__extended_Entity

    @extended_Entity.setter
    def extended_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Entity__extended_Entity", None)
        self.__extended_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_EntityType"):
                opp_val = getattr(old_value, "extended_EntityType", None)
                if opp_val == self:
                    setattr(old_value, "extended_EntityType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_EntityType"):
                opp_val = getattr(value, "extended_EntityType", None)
                setattr(value, "extended_EntityType", self)

    @property
    def extended_Entity8(self):
        return self.__extended_Entity8

    @extended_Entity8.setter
    def extended_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Entity__extended_Entity8", None)
        self.__extended_Entity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extended_Feature"):
                    opp_val = getattr(item, "extended_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "extended_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extended_Feature"):
                    opp_val = getattr(item, "extended_Feature", None)
                    
                    setattr(item, "extended_Feature", self)
                    

    @property
    def extended_Entity4(self):
        return self.__extended_Entity4

    @extended_Entity4.setter
    def extended_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Entity__extended_Entity4", None)
        self.__extended_Entity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_Entity6"):
                opp_val = getattr(old_value, "extended_Entity6", None)
                if opp_val == self:
                    setattr(old_value, "extended_Entity6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_Entity6"):
                opp_val = getattr(value, "extended_Entity6", None)
                setattr(value, "extended_Entity6", self)

    @property
    def extended_Entity6(self):
        return self.__extended_Entity6

    @extended_Entity6.setter
    def extended_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Entity__extended_Entity6", None)
        self.__extended_Entity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_Entity4"):
                opp_val = getattr(old_value, "extended_Entity4", None)
                if opp_val == self:
                    setattr(old_value, "extended_Entity4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_Entity4"):
                opp_val = getattr(value, "extended_Entity4", None)
                setattr(value, "extended_Entity4", self)

    @property
    def extended_Entity14(self):
        return self.__extended_Entity14

    @extended_Entity14.setter
    def extended_Entity14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Entity__extended_Entity14", None)
        self.__extended_Entity14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extended_FormTypes13"):
                opp_val = getattr(old_value, "extended_FormTypes13", None)
                if opp_val == self:
                    setattr(old_value, "extended_FormTypes13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extended_FormTypes13"):
                opp_val = getattr(value, "extended_FormTypes13", None)
                setattr(value, "extended_FormTypes13", self)

class extended_PackageDeclaration(AbstractElement):

    def __init__(self, name: str, extended_PackageDeclaration: set["extended_AbstractElement"] = None):
        self.name = name
        self.extended_PackageDeclaration = extended_PackageDeclaration if extended_PackageDeclaration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extended_PackageDeclaration(self):
        return self.__extended_PackageDeclaration

    @extended_PackageDeclaration.setter
    def extended_PackageDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_PackageDeclaration__extended_PackageDeclaration", None)
        self.__extended_PackageDeclaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extended_AbstractElement2"):
                    opp_val = getattr(item, "extended_AbstractElement2", None)
                    
                    if opp_val == self:
                        setattr(item, "extended_AbstractElement2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extended_AbstractElement2"):
                    opp_val = getattr(item, "extended_AbstractElement2", None)
                    
                    setattr(item, "extended_AbstractElement2", self)
                    

class extended_AbstractElement:

    pass
class extended_Domainmodel:

    def __init__(self, nomeProj: str, extended_Domainmodel: set["extended_AbstractElement"] = None):
        self.nomeProj = nomeProj
        self.extended_Domainmodel = extended_Domainmodel if extended_Domainmodel is not None else set()
        
    @property
    def nomeProj(self) -> str:
        return self.__nomeProj

    @nomeProj.setter
    def nomeProj(self, nomeProj: str):
        self.__nomeProj = nomeProj

    @property
    def extended_Domainmodel(self):
        return self.__extended_Domainmodel

    @extended_Domainmodel.setter
    def extended_Domainmodel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extended_Domainmodel__extended_Domainmodel", None)
        self.__extended_Domainmodel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extended_AbstractElement"):
                    opp_val = getattr(item, "extended_AbstractElement", None)
                    
                    if opp_val == self:
                        setattr(item, "extended_AbstractElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extended_AbstractElement"):
                    opp_val = getattr(item, "extended_AbstractElement", None)
                    
                    setattr(item, "extended_AbstractElement", self)
                    

class extended_Import(AbstractElement):

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace
