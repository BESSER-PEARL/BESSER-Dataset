from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Page:

    pass
class Arc:

    pass
class Transition:

    pass
class pragmacpndefinition_OntologyMember(ABC):

    def __init__(self, pragmacpndefinition_OntologyMember: set["pragmacpndefinition_Pragma"] = None):
        self.pragmacpndefinition_OntologyMember = pragmacpndefinition_OntologyMember if pragmacpndefinition_OntologyMember is not None else set()
        
        pass
    @property
    def pragmacpndefinition_OntologyMember(self):
        return self.__pragmacpndefinition_OntologyMember

    @pragmacpndefinition_OntologyMember.setter
    def pragmacpndefinition_OntologyMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_OntologyMember__pragmacpndefinition_OntologyMember", None)
        self.__pragmacpndefinition_OntologyMember = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pragmacpndefinition_Pragma"):
                    opp_val = getattr(item, "pragmacpndefinition_Pragma", None)
                    
                    if opp_val == self:
                        setattr(item, "pragmacpndefinition_Pragma", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pragmacpndefinition_Pragma"):
                    opp_val = getattr(item, "pragmacpndefinition_Pragma", None)
                    
                    setattr(item, "pragmacpndefinition_Pragma", self)
                    

    def getOWLClass(self) :
        # TODO: Implement getOWLClass method
        pass

class PetriNet:

    pass
class pragmacpndefinition_OntologyDocument:

    def __init__(self, iri: str, path: str, documents: "pragmacpndefinition_PragmaticsOntology" = None, OntologyDocument: "pragmacpndefinition_PragmaticsOntology" = None):
        self.iri = iri
        self.path = path
        self.documents = documents
        self.OntologyDocument = OntologyDocument
        
        pass
    @property
    def iri(self):
        return self.__iri

    @iri.setter
    def iri(self, iri: str):
        self.__iri = iri


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def OntologyDocument(self):
        return self.__OntologyDocument

    @OntologyDocument.setter
    def OntologyDocument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_OntologyDocument__OntologyDocument", None)
        self.__OntologyDocument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ontology"):
                opp_val = getattr(old_value, "ontology", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ontology"):
                opp_val = getattr(value, "ontology", None)
                if opp_val is None:
                    setattr(value, "ontology", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def documents(self):
        return self.__documents

    @documents.setter
    def documents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_OntologyDocument__documents", None)
        self.__documents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PragmaticsOntology"):
                opp_val = getattr(old_value, "PragmaticsOntology", None)
                if opp_val == self:
                    setattr(old_value, "PragmaticsOntology", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PragmaticsOntology"):
                opp_val = getattr(value, "PragmaticsOntology", None)
                setattr(value, "PragmaticsOntology", self)

class Label:

    pass
class pragmacpndefinition_PragmaticsOntology(Label):

    def __init__(self, manager: str, ontology3: "pragmacpndefinition_PetriNet" = None, PragmaticsOntology: "pragmacpndefinition_OntologyDocument" = None, ontology: set["pragmacpndefinition_OntologyDocument"] = None, PragmaticsOntology5: "pragmacpndefinition_PetriNet" = None):
        self.manager = manager
        self.ontology3 = ontology3
        self.PragmaticsOntology = PragmaticsOntology
        self.ontology = ontology if ontology is not None else set()
        self.PragmaticsOntology5 = PragmaticsOntology5
        
        pass
    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager: str):
        self.__manager = manager


    @property
    def ontology(self):
        return self.__ontology

    @ontology.setter
    def ontology(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_PragmaticsOntology__ontology", None)
        self.__ontology = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OntologyDocument"):
                    opp_val = getattr(item, "OntologyDocument", None)
                    
                    if opp_val == self:
                        setattr(item, "OntologyDocument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OntologyDocument"):
                    opp_val = getattr(item, "OntologyDocument", None)
                    
                    setattr(item, "OntologyDocument", self)
                    

    @property
    def PragmaticsOntology(self):
        return self.__PragmaticsOntology

    @PragmaticsOntology.setter
    def PragmaticsOntology(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_PragmaticsOntology__PragmaticsOntology", None)
        self.__PragmaticsOntology = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "documents"):
                opp_val = getattr(old_value, "documents", None)
                if opp_val == self:
                    setattr(old_value, "documents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "documents"):
                opp_val = getattr(value, "documents", None)
                setattr(value, "documents", self)

    @property
    def ontology3(self):
        return self.__ontology3

    @ontology3.setter
    def ontology3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_PragmaticsOntology__ontology3", None)
        self.__ontology3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet"):
                opp_val = getattr(old_value, "PetriNet", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet"):
                opp_val = getattr(value, "PetriNet", None)
                setattr(value, "PetriNet", self)

    @property
    def PragmaticsOntology5(self):
        return self.__PragmaticsOntology5

    @PragmaticsOntology5.setter
    def PragmaticsOntology5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_PragmaticsOntology__PragmaticsOntology5", None)
        self.__PragmaticsOntology5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "net"):
                opp_val = getattr(old_value, "net", None)
                if opp_val == self:
                    setattr(old_value, "net", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "net"):
                opp_val = getattr(value, "net", None)
                setattr(value, "net", self)

    def getValidPragmatics(self, pragmacpndefinition_object) :
        # TODO: Implement getValidPragmatics method
        pass

    def addOntologyFromFile(self, pragmacpndefinition_file):
        # TODO: Implement addOntologyFromFile method
        pass

class pragmacpndefinition_Pragma(Label):

    def __init__(self, text: str, pragmacpndefinition_Pragma: "pragmacpndefinition_OntologyMember" = None):
        self.text = text
        self.pragmacpndefinition_Pragma = pragmacpndefinition_Pragma
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def pragmacpndefinition_Pragma(self):
        return self.__pragmacpndefinition_Pragma

    @pragmacpndefinition_Pragma.setter
    def pragmacpndefinition_Pragma(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pragmacpndefinition_Pragma__pragmacpndefinition_Pragma", None)
        self.__pragmacpndefinition_Pragma = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pragmacpndefinition_OntologyMember"):
                opp_val = getattr(old_value, "pragmacpndefinition_OntologyMember", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pragmacpndefinition_OntologyMember"):
                opp_val = getattr(value, "pragmacpndefinition_OntologyMember", None)
                if opp_val is None:
                    setattr(value, "pragmacpndefinition_OntologyMember", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class OntologyMember:

    pass
class pragmacpndefinition_Transition(Transition, OntologyMember):

    pass
class pragmacpndefinition_Arc(Arc, OntologyMember):

    pass
class pragmacpndefinition_Page(OntologyMember, Page):

    pass
class Place:

    pass
class pragmacpndefinition_Place(OntologyMember, Place):

    pass
class CPN:

    pass
class pragmacpndefinition_PragmaCPN(CPN):

    pass
class pragmacpndefinition_PetriNet(PetriNet):

    pass