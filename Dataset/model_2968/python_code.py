from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class owl_RDFSClass:

    pass
class owl_RDFSResource:

    pass
class OWLRestriction:

    pass
class owl_SomeValuesFromRestriction(OWLRestriction):

    pass
class owl_MinCardinalityRestriction(OWLRestriction):

    pass
class owl_CardinalityRestriction(OWLRestriction):

    pass
class owl_MaxCardinalityRestriction(OWLRestriction):

    pass
class owl_AllValuesFromRestriction(OWLRestriction):

    pass
class owl_HasValueRestriction(OWLRestriction):

    pass
class owl_ObjectSlot:

    pass
class owl_DatatypeSlot:

    pass
class RDFSResource:

    pass
class owl_OWLAllDifferent(RDFSResource):

    pass
class owl_Individual(RDFSResource):

    pass
class Property:

    pass
class owl_OWLDatatypeProperty(Property):

    pass
class owl_OWLObjectProperty(Property):

    def __init__(self, transitive: str, inverseFunctional: str, symmetric: str, OWLObjectProperty: "owl_OWLObjectProperty" = None, invOWLInverseOf: "owl_OWLObjectProperty" = None, OWLObjectProperty32: "owl_OWLObjectProperty" = None, OWLInverseOf: set["owl_OWLObjectProperty"] = None, owl_OWLObjectProperty: "owl_ObjectSlot" = None):
        self.transitive = transitive
        self.inverseFunctional = inverseFunctional
        self.symmetric = symmetric
        self.OWLObjectProperty = OWLObjectProperty
        self.invOWLInverseOf = invOWLInverseOf
        self.OWLObjectProperty32 = OWLObjectProperty32
        self.OWLInverseOf = OWLInverseOf if OWLInverseOf is not None else set()
        self.owl_OWLObjectProperty = owl_OWLObjectProperty
        
    @property
    def inverseFunctional(self) -> str:
        return self.__inverseFunctional

    @inverseFunctional.setter
    def inverseFunctional(self, inverseFunctional: str):
        self.__inverseFunctional = inverseFunctional

    @property
    def symmetric(self) -> str:
        return self.__symmetric

    @symmetric.setter
    def symmetric(self, symmetric: str):
        self.__symmetric = symmetric

    @property
    def transitive(self) -> str:
        return self.__transitive

    @transitive.setter
    def transitive(self, transitive: str):
        self.__transitive = transitive

    @property
    def OWLObjectProperty32(self):
        return self.__OWLObjectProperty32

    @OWLObjectProperty32.setter
    def OWLObjectProperty32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLObjectProperty__OWLObjectProperty32", None)
        self.__OWLObjectProperty32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OWLInverseOf"):
                opp_val = getattr(old_value, "OWLInverseOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OWLInverseOf"):
                opp_val = getattr(value, "OWLInverseOf", None)
                if opp_val is None:
                    setattr(value, "OWLInverseOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLObjectProperty(self):
        return self.__OWLObjectProperty

    @OWLObjectProperty.setter
    def OWLObjectProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLObjectProperty__OWLObjectProperty", None)
        self.__OWLObjectProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invOWLInverseOf"):
                opp_val = getattr(old_value, "invOWLInverseOf", None)
                if opp_val == self:
                    setattr(old_value, "invOWLInverseOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invOWLInverseOf"):
                opp_val = getattr(value, "invOWLInverseOf", None)
                setattr(value, "invOWLInverseOf", self)

    @property
    def OWLInverseOf(self):
        return self.__OWLInverseOf

    @OWLInverseOf.setter
    def OWLInverseOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLObjectProperty__OWLInverseOf", None)
        self.__OWLInverseOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OWLObjectProperty32"):
                    opp_val = getattr(item, "OWLObjectProperty32", None)
                    
                    if opp_val == self:
                        setattr(item, "OWLObjectProperty32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OWLObjectProperty32"):
                    opp_val = getattr(item, "OWLObjectProperty32", None)
                    
                    setattr(item, "OWLObjectProperty32", self)
                    

    @property
    def invOWLInverseOf(self):
        return self.__invOWLInverseOf

    @invOWLInverseOf.setter
    def invOWLInverseOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLObjectProperty__invOWLInverseOf", None)
        self.__invOWLInverseOf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OWLObjectProperty"):
                opp_val = getattr(old_value, "OWLObjectProperty", None)
                if opp_val == self:
                    setattr(old_value, "OWLObjectProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OWLObjectProperty"):
                opp_val = getattr(value, "OWLObjectProperty", None)
                setattr(value, "OWLObjectProperty", self)

    @property
    def owl_OWLObjectProperty(self):
        return self.__owl_OWLObjectProperty

    @owl_OWLObjectProperty.setter
    def owl_OWLObjectProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLObjectProperty__owl_OWLObjectProperty", None)
        self.__owl_OWLObjectProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owl_ObjectSlot67"):
                opp_val = getattr(old_value, "owl_ObjectSlot67", None)
                if opp_val == self:
                    setattr(old_value, "owl_ObjectSlot67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owl_ObjectSlot67"):
                opp_val = getattr(value, "owl_ObjectSlot67", None)
                setattr(value, "owl_ObjectSlot67", self)

class owl_RDFProperty:

    pass
class OWLClass:

    pass
class owl_EnumeratedClass(OWLClass):

    pass
class owl_IntersectionClass(OWLClass):

    pass
class owl_OWLRestriction(OWLClass):

    pass
class owl_ComplementClass(OWLClass):

    pass
class owl_UnionClass(OWLClass):

    pass
class RDFSClass:

    pass
class owl_OWLDataRange(RDFSClass):

    pass
class owl_OWLClass(RDFSClass):

    def __init__(self, deprecated: str, OWLClass: "owl_OWLClass" = None, OWLEquivalentClass: set["owl_OWLClass"] = None, OWLClass17: "owl_OWLClass" = None, invOWLEquivalentClass: set["owl_OWLClass"] = None, OWLClass20: "owl_OWLClass" = None, invOWLDisjointWith: set["owl_OWLClass"] = None, OWLClass23: "owl_OWLClass" = None, OWLDisjointWith: set["owl_OWLClass"] = None, OWLUnionOf: set["owl_UnionClass"] = None, OWLComplementOf: set["owl_ComplementClass"] = None, OWLIntersectionOf: set["owl_IntersectionClass"] = None, OWLClass71: "owl_IntersectionClass" = None, OWLClass73: "owl_UnionClass" = None, OWLClass85: "owl_ComplementClass" = None):
        self.deprecated = deprecated
        self.OWLClass = OWLClass
        self.OWLEquivalentClass = OWLEquivalentClass if OWLEquivalentClass is not None else set()
        self.OWLClass17 = OWLClass17
        self.invOWLEquivalentClass = invOWLEquivalentClass if invOWLEquivalentClass is not None else set()
        self.OWLClass20 = OWLClass20
        self.invOWLDisjointWith = invOWLDisjointWith if invOWLDisjointWith is not None else set()
        self.OWLClass23 = OWLClass23
        self.OWLDisjointWith = OWLDisjointWith if OWLDisjointWith is not None else set()
        self.OWLUnionOf = OWLUnionOf if OWLUnionOf is not None else set()
        self.OWLComplementOf = OWLComplementOf if OWLComplementOf is not None else set()
        self.OWLIntersectionOf = OWLIntersectionOf if OWLIntersectionOf is not None else set()
        self.OWLClass71 = OWLClass71
        self.OWLClass73 = OWLClass73
        self.OWLClass85 = OWLClass85
        
    @property
    def deprecated(self) -> str:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: str):
        self.__deprecated = deprecated

    @property
    def invOWLDisjointWith(self):
        return self.__invOWLDisjointWith

    @invOWLDisjointWith.setter
    def invOWLDisjointWith(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__invOWLDisjointWith", None)
        self.__invOWLDisjointWith = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OWLClass20"):
                    opp_val = getattr(item, "OWLClass20", None)
                    
                    if opp_val == self:
                        setattr(item, "OWLClass20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OWLClass20"):
                    opp_val = getattr(item, "OWLClass20", None)
                    
                    setattr(item, "OWLClass20", self)
                    

    @property
    def OWLClass23(self):
        return self.__OWLClass23

    @OWLClass23.setter
    def OWLClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass23", None)
        self.__OWLClass23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OWLDisjointWith"):
                opp_val = getattr(old_value, "OWLDisjointWith", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OWLDisjointWith"):
                opp_val = getattr(value, "OWLDisjointWith", None)
                if opp_val is None:
                    setattr(value, "OWLDisjointWith", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLClass71(self):
        return self.__OWLClass71

    @OWLClass71.setter
    def OWLClass71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass71", None)
        self.__OWLClass71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refByIntersectionClass"):
                opp_val = getattr(old_value, "refByIntersectionClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refByIntersectionClass"):
                opp_val = getattr(value, "refByIntersectionClass", None)
                if opp_val is None:
                    setattr(value, "refByIntersectionClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLEquivalentClass(self):
        return self.__OWLEquivalentClass

    @OWLEquivalentClass.setter
    def OWLEquivalentClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLEquivalentClass", None)
        self.__OWLEquivalentClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OWLClass"):
                    opp_val = getattr(item, "OWLClass", None)
                    
                    if opp_val == self:
                        setattr(item, "OWLClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OWLClass"):
                    opp_val = getattr(item, "OWLClass", None)
                    
                    setattr(item, "OWLClass", self)
                    

    @property
    def OWLComplementOf(self):
        return self.__OWLComplementOf

    @OWLComplementOf.setter
    def OWLComplementOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLComplementOf", None)
        self.__OWLComplementOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ComplementClass"):
                    opp_val = getattr(item, "ComplementClass", None)
                    
                    if opp_val == self:
                        setattr(item, "ComplementClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ComplementClass"):
                    opp_val = getattr(item, "ComplementClass", None)
                    
                    setattr(item, "ComplementClass", self)
                    

    @property
    def OWLClass17(self):
        return self.__OWLClass17

    @OWLClass17.setter
    def OWLClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass17", None)
        self.__OWLClass17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invOWLEquivalentClass"):
                opp_val = getattr(old_value, "invOWLEquivalentClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invOWLEquivalentClass"):
                opp_val = getattr(value, "invOWLEquivalentClass", None)
                if opp_val is None:
                    setattr(value, "invOWLEquivalentClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLClass85(self):
        return self.__OWLClass85

    @OWLClass85.setter
    def OWLClass85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass85", None)
        self.__OWLClass85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invOWLComplementOf"):
                opp_val = getattr(old_value, "invOWLComplementOf", None)
                if opp_val == self:
                    setattr(old_value, "invOWLComplementOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invOWLComplementOf"):
                opp_val = getattr(value, "invOWLComplementOf", None)
                setattr(value, "invOWLComplementOf", self)

    @property
    def OWLDisjointWith(self):
        return self.__OWLDisjointWith

    @OWLDisjointWith.setter
    def OWLDisjointWith(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLDisjointWith", None)
        self.__OWLDisjointWith = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OWLClass23"):
                    opp_val = getattr(item, "OWLClass23", None)
                    
                    if opp_val == self:
                        setattr(item, "OWLClass23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OWLClass23"):
                    opp_val = getattr(item, "OWLClass23", None)
                    
                    setattr(item, "OWLClass23", self)
                    

    @property
    def OWLClass(self):
        return self.__OWLClass

    @OWLClass.setter
    def OWLClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass", None)
        self.__OWLClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OWLEquivalentClass"):
                opp_val = getattr(old_value, "OWLEquivalentClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OWLEquivalentClass"):
                opp_val = getattr(value, "OWLEquivalentClass", None)
                if opp_val is None:
                    setattr(value, "OWLEquivalentClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invOWLEquivalentClass(self):
        return self.__invOWLEquivalentClass

    @invOWLEquivalentClass.setter
    def invOWLEquivalentClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__invOWLEquivalentClass", None)
        self.__invOWLEquivalentClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OWLClass17"):
                    opp_val = getattr(item, "OWLClass17", None)
                    
                    if opp_val == self:
                        setattr(item, "OWLClass17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OWLClass17"):
                    opp_val = getattr(item, "OWLClass17", None)
                    
                    setattr(item, "OWLClass17", self)
                    

    @property
    def OWLIntersectionOf(self):
        return self.__OWLIntersectionOf

    @OWLIntersectionOf.setter
    def OWLIntersectionOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLIntersectionOf", None)
        self.__OWLIntersectionOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "IntersectionClass"):
                    opp_val = getattr(item, "IntersectionClass", None)
                    
                    if opp_val == self:
                        setattr(item, "IntersectionClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "IntersectionClass"):
                    opp_val = getattr(item, "IntersectionClass", None)
                    
                    setattr(item, "IntersectionClass", self)
                    

    @property
    def OWLClass73(self):
        return self.__OWLClass73

    @OWLClass73.setter
    def OWLClass73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass73", None)
        self.__OWLClass73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refByUnionClass"):
                opp_val = getattr(old_value, "refByUnionClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refByUnionClass"):
                opp_val = getattr(value, "refByUnionClass", None)
                if opp_val is None:
                    setattr(value, "refByUnionClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLClass20(self):
        return self.__OWLClass20

    @OWLClass20.setter
    def OWLClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLClass20", None)
        self.__OWLClass20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invOWLDisjointWith"):
                opp_val = getattr(old_value, "invOWLDisjointWith", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invOWLDisjointWith"):
                opp_val = getattr(value, "invOWLDisjointWith", None)
                if opp_val is None:
                    setattr(value, "invOWLDisjointWith", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLUnionOf(self):
        return self.__OWLUnionOf

    @OWLUnionOf.setter
    def OWLUnionOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_OWLClass__OWLUnionOf", None)
        self.__OWLUnionOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UnionClass"):
                    opp_val = getattr(item, "UnionClass", None)
                    
                    if opp_val == self:
                        setattr(item, "UnionClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UnionClass"):
                    opp_val = getattr(item, "UnionClass", None)
                    
                    setattr(item, "UnionClass", self)
                    

class RDFProperty:

    pass
class owl_OWLAnnotationProperty(RDFProperty):

    pass
class owl_Property(RDFProperty):

    def __init__(self, deprecated: str, functional: str, Property37: "owl_Property" = None, OWLEquivalentProperty: set["owl_Property"] = None, Property: "owl_Property" = None, invOWLEquivalentProperty: set["owl_Property"] = None):
        self.deprecated = deprecated
        self.functional = functional
        self.Property37 = Property37
        self.OWLEquivalentProperty = OWLEquivalentProperty if OWLEquivalentProperty is not None else set()
        self.Property = Property
        self.invOWLEquivalentProperty = invOWLEquivalentProperty if invOWLEquivalentProperty is not None else set()
        
    @property
    def deprecated(self) -> str:
        return self.__deprecated

    @deprecated.setter
    def deprecated(self, deprecated: str):
        self.__deprecated = deprecated

    @property
    def functional(self) -> str:
        return self.__functional

    @functional.setter
    def functional(self, functional: str):
        self.__functional = functional

    @property
    def Property37(self):
        return self.__Property37

    @Property37.setter
    def Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_Property__Property37", None)
        self.__Property37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OWLEquivalentProperty"):
                opp_val = getattr(old_value, "OWLEquivalentProperty", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OWLEquivalentProperty"):
                opp_val = getattr(value, "OWLEquivalentProperty", None)
                if opp_val is None:
                    setattr(value, "OWLEquivalentProperty", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invOWLEquivalentProperty(self):
        return self.__invOWLEquivalentProperty

    @invOWLEquivalentProperty.setter
    def invOWLEquivalentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_Property__invOWLEquivalentProperty", None)
        self.__invOWLEquivalentProperty = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invOWLEquivalentProperty"):
                opp_val = getattr(old_value, "invOWLEquivalentProperty", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invOWLEquivalentProperty"):
                opp_val = getattr(value, "invOWLEquivalentProperty", None)
                if opp_val is None:
                    setattr(value, "invOWLEquivalentProperty", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OWLEquivalentProperty(self):
        return self.__OWLEquivalentProperty

    @OWLEquivalentProperty.setter
    def OWLEquivalentProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_owl_Property__OWLEquivalentProperty", None)
        self.__OWLEquivalentProperty = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property37"):
                    opp_val = getattr(item, "Property37", None)
                    
                    if opp_val == self:
                        setattr(item, "Property37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property37"):
                    opp_val = getattr(item, "Property37", None)
                    
                    setattr(item, "Property37", self)
                    

class owl_OWLOntologyProperty(RDFProperty):

    pass
class Ontology:

    pass
class owl_OWLOntology(Ontology):

    pass
class owl_RDFSLiteral:

    pass