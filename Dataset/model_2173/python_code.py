from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class graphDsl_ImportsVariable:

    def __init__(self, isExternal: bool, componentName: str, componentProperty: str, isOptional: bool, graphDsl_ImportsVariable: "graphDsl_ImportsProperty" = None):
        self.isExternal = isExternal
        self.componentName = componentName
        self.componentProperty = componentProperty
        self.isOptional = isOptional
        self.graphDsl_ImportsVariable = graphDsl_ImportsVariable
        
    @property
    def isExternal(self) -> bool:
        return self.__isExternal

    @isExternal.setter
    def isExternal(self, isExternal: bool):
        self.__isExternal = isExternal

    @property
    def componentName(self) -> str:
        return self.__componentName

    @componentName.setter
    def componentName(self, componentName: str):
        self.__componentName = componentName

    @property
    def isOptional(self) -> bool:
        return self.__isOptional

    @isOptional.setter
    def isOptional(self, isOptional: bool):
        self.__isOptional = isOptional

    @property
    def componentProperty(self) -> str:
        return self.__componentProperty

    @componentProperty.setter
    def componentProperty(self, componentProperty: str):
        self.__componentProperty = componentProperty

    @property
    def graphDsl_ImportsVariable(self):
        return self.__graphDsl_ImportsVariable

    @graphDsl_ImportsVariable.setter
    def graphDsl_ImportsVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_ImportsVariable__graphDsl_ImportsVariable", None)
        self.__graphDsl_ImportsVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ImportsProperty34"):
                opp_val = getattr(old_value, "graphDsl_ImportsProperty34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ImportsProperty34"):
                opp_val = getattr(value, "graphDsl_ImportsProperty34", None)
                if opp_val is None:
                    setattr(value, "graphDsl_ImportsProperty34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphDsl_ExportsVariable:

    def __init__(self, name: str, intValue: int, strValue: str, graphDsl_ExportsVariable: "graphDsl_ExportsProperty" = None):
        self.name = name
        self.intValue = intValue
        self.strValue = strValue
        self.graphDsl_ExportsVariable = graphDsl_ExportsVariable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def strValue(self) -> str:
        return self.__strValue

    @strValue.setter
    def strValue(self, strValue: str):
        self.__strValue = strValue

    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

    @property
    def graphDsl_ExportsVariable(self):
        return self.__graphDsl_ExportsVariable

    @graphDsl_ExportsVariable.setter
    def graphDsl_ExportsVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_ExportsVariable__graphDsl_ExportsVariable", None)
        self.__graphDsl_ExportsVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ExportsProperty32"):
                opp_val = getattr(old_value, "graphDsl_ExportsProperty32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ExportsProperty32"):
                opp_val = getattr(value, "graphDsl_ExportsProperty32", None)
                if opp_val is None:
                    setattr(value, "graphDsl_ExportsProperty32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class graphDsl_ExtendsProperty:

    def __init__(self, extendsNames: str, graphDsl_ExtendsProperty: "graphDsl_OptionalProperty" = None):
        self.extendsNames = extendsNames
        self.graphDsl_ExtendsProperty = graphDsl_ExtendsProperty
        
    @property
    def extendsNames(self) -> str:
        return self.__extendsNames

    @extendsNames.setter
    def extendsNames(self, extendsNames: str):
        self.__extendsNames = extendsNames

    @property
    def graphDsl_ExtendsProperty(self):
        return self.__graphDsl_ExtendsProperty

    @graphDsl_ExtendsProperty.setter
    def graphDsl_ExtendsProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_ExtendsProperty__graphDsl_ExtendsProperty", None)
        self.__graphDsl_ExtendsProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_OptionalProperty30"):
                opp_val = getattr(old_value, "graphDsl_OptionalProperty30", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_OptionalProperty30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_OptionalProperty30"):
                opp_val = getattr(value, "graphDsl_OptionalProperty30", None)
                setattr(value, "graphDsl_OptionalProperty30", self)

class graphDsl_FacetsProperty:

    def __init__(self, facetsNames: str, graphDsl_FacetsProperty: "graphDsl_OptionalProperty" = None):
        self.facetsNames = facetsNames
        self.graphDsl_FacetsProperty = graphDsl_FacetsProperty
        
    @property
    def facetsNames(self) -> str:
        return self.__facetsNames

    @facetsNames.setter
    def facetsNames(self, facetsNames: str):
        self.__facetsNames = facetsNames

    @property
    def graphDsl_FacetsProperty(self):
        return self.__graphDsl_FacetsProperty

    @graphDsl_FacetsProperty.setter
    def graphDsl_FacetsProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_FacetsProperty__graphDsl_FacetsProperty", None)
        self.__graphDsl_FacetsProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_OptionalProperty28"):
                opp_val = getattr(old_value, "graphDsl_OptionalProperty28", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_OptionalProperty28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_OptionalProperty28"):
                opp_val = getattr(value, "graphDsl_OptionalProperty28", None)
                setattr(value, "graphDsl_OptionalProperty28", self)

class graphDsl_ImportsProperty:

    pass
class graphDsl_ExportsProperty:

    pass
class graphDsl_ChildrenProperty:

    def __init__(self, name: str, graphDsl_ChildrenProperty: "graphDsl_FacetProperty" = None, graphDsl_ChildrenProperty21: "graphDsl_OptionalProperty" = None):
        self.name = name
        self.graphDsl_ChildrenProperty = graphDsl_ChildrenProperty
        self.graphDsl_ChildrenProperty21 = graphDsl_ChildrenProperty21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphDsl_ChildrenProperty21(self):
        return self.__graphDsl_ChildrenProperty21

    @graphDsl_ChildrenProperty21.setter
    def graphDsl_ChildrenProperty21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_ChildrenProperty__graphDsl_ChildrenProperty21", None)
        self.__graphDsl_ChildrenProperty21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_OptionalProperty20"):
                opp_val = getattr(old_value, "graphDsl_OptionalProperty20", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_OptionalProperty20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_OptionalProperty20"):
                opp_val = getattr(value, "graphDsl_OptionalProperty20", None)
                setattr(value, "graphDsl_OptionalProperty20", self)

    @property
    def graphDsl_ChildrenProperty(self):
        return self.__graphDsl_ChildrenProperty

    @graphDsl_ChildrenProperty.setter
    def graphDsl_ChildrenProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_ChildrenProperty__graphDsl_ChildrenProperty", None)
        self.__graphDsl_ChildrenProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_FacetProperty16"):
                opp_val = getattr(old_value, "graphDsl_FacetProperty16", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_FacetProperty16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_FacetProperty16"):
                opp_val = getattr(value, "graphDsl_FacetProperty16", None)
                setattr(value, "graphDsl_FacetProperty16", self)

class graphDsl_FacetProperty:

    pass
class graphDsl_InstallerProperty:

    def __init__(self, name: str, graphDsl_InstallerProperty: "graphDsl_ComponentProperties" = None):
        self.name = name
        self.graphDsl_InstallerProperty = graphDsl_InstallerProperty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphDsl_InstallerProperty(self):
        return self.__graphDsl_InstallerProperty

    @graphDsl_InstallerProperty.setter
    def graphDsl_InstallerProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_InstallerProperty__graphDsl_InstallerProperty", None)
        self.__graphDsl_InstallerProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ComponentProperties12"):
                opp_val = getattr(old_value, "graphDsl_ComponentProperties12", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_ComponentProperties12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ComponentProperties12"):
                opp_val = getattr(value, "graphDsl_ComponentProperties12", None)
                setattr(value, "graphDsl_ComponentProperties12", self)

class graphDsl_OptionalProperty:

    pass
class graphDsl_FacetProperties:

    pass
class graphDsl_ComponentProperties:

    pass
class graphDsl_Facet:

    def __init__(self, name: str, graphDsl_Facet8: "graphDsl_FacetProperties" = None, graphDsl_Facet: "graphDsl_ComponentOrFacet" = None):
        self.name = name
        self.graphDsl_Facet8 = graphDsl_Facet8
        self.graphDsl_Facet = graphDsl_Facet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphDsl_Facet8(self):
        return self.__graphDsl_Facet8

    @graphDsl_Facet8.setter
    def graphDsl_Facet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_Facet__graphDsl_Facet8", None)
        self.__graphDsl_Facet8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_FacetProperties"):
                opp_val = getattr(old_value, "graphDsl_FacetProperties", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_FacetProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_FacetProperties"):
                opp_val = getattr(value, "graphDsl_FacetProperties", None)
                setattr(value, "graphDsl_FacetProperties", self)

    @property
    def graphDsl_Facet(self):
        return self.__graphDsl_Facet

    @graphDsl_Facet.setter
    def graphDsl_Facet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_Facet__graphDsl_Facet", None)
        self.__graphDsl_Facet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ComponentOrFacet4"):
                opp_val = getattr(old_value, "graphDsl_ComponentOrFacet4", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_ComponentOrFacet4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ComponentOrFacet4"):
                opp_val = getattr(value, "graphDsl_ComponentOrFacet4", None)
                setattr(value, "graphDsl_ComponentOrFacet4", self)

class graphDsl_Component:

    def __init__(self, name: str, graphDsl_Component: "graphDsl_ComponentOrFacet" = None, graphDsl_Component6: "graphDsl_ComponentProperties" = None):
        self.name = name
        self.graphDsl_Component = graphDsl_Component
        self.graphDsl_Component6 = graphDsl_Component6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def graphDsl_Component(self):
        return self.__graphDsl_Component

    @graphDsl_Component.setter
    def graphDsl_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_Component__graphDsl_Component", None)
        self.__graphDsl_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ComponentOrFacet2"):
                opp_val = getattr(old_value, "graphDsl_ComponentOrFacet2", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_ComponentOrFacet2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ComponentOrFacet2"):
                opp_val = getattr(value, "graphDsl_ComponentOrFacet2", None)
                setattr(value, "graphDsl_ComponentOrFacet2", self)

    @property
    def graphDsl_Component6(self):
        return self.__graphDsl_Component6

    @graphDsl_Component6.setter
    def graphDsl_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_Component__graphDsl_Component6", None)
        self.__graphDsl_Component6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graphDsl_ComponentProperties"):
                opp_val = getattr(old_value, "graphDsl_ComponentProperties", None)
                if opp_val == self:
                    setattr(old_value, "graphDsl_ComponentProperties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graphDsl_ComponentProperties"):
                opp_val = getattr(value, "graphDsl_ComponentProperties", None)
                setattr(value, "graphDsl_ComponentProperties", self)

class graphDsl_ComponentOrFacet:

    pass
class graphDsl_Graph:

    def __init__(self, comments: str, graphDsl_Graph: set["graphDsl_ComponentOrFacet"] = None):
        self.comments = comments
        self.graphDsl_Graph = graphDsl_Graph if graphDsl_Graph is not None else set()
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

    @property
    def graphDsl_Graph(self):
        return self.__graphDsl_Graph

    @graphDsl_Graph.setter
    def graphDsl_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graphDsl_Graph__graphDsl_Graph", None)
        self.__graphDsl_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graphDsl_ComponentOrFacet"):
                    opp_val = getattr(item, "graphDsl_ComponentOrFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "graphDsl_ComponentOrFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graphDsl_ComponentOrFacet"):
                    opp_val = getattr(item, "graphDsl_ComponentOrFacet", None)
                    
                    setattr(item, "graphDsl_ComponentOrFacet", self)
                    
