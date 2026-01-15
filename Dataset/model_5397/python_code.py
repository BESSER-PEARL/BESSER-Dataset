from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class droneDSLLib_CommandeBasique:

    pass
class droneDSLLib_DecollerAtterrir:

    def __init__(self, str: str):
        self.str = str
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

class droneDSLLib_Mouvement:

    pass
class Parallele:

    pass
class droneDSLLib_Parallele4(Parallele):

    pass
class droneDSLLib_Parallele3(Parallele):

    pass
class droneDSLLib_Parallele2(Parallele):

    pass
class droneDSLLib_AR:

    pass
class droneDSLLib_RGRD:

    pass
class droneDSLLib_GDr:

    pass
class droneDSLLib_MD:

    pass
class FonctionCall:

    pass
class droneDSLLib_FonctionCallInterne(FonctionCall):

    pass
class droneDSLLib_FonctionCall:

    pass
class droneDSLLib_EObject:

    pass
class RGRD:

    pass
class GDr:

    pass
class VarDecl:

    pass
class droneDSLLib_PourcentDecl(VarDecl):

    pass
class droneDSLLib_SecondeDecl(VarDecl):

    pass
class AR:

    pass
class MD:

    pass
class CommandeBasique:

    pass
class droneDSLLib_Pause(CommandeBasique):

    pass
class Mouvement:

    pass
class droneDSLLib_Avancer(CommandeBasique, AR, Mouvement):

    pass
class droneDSLLib_Descendre(CommandeBasique, MD, Mouvement):

    pass
class droneDSLLib_Droite(CommandeBasique, GDr, Mouvement):

    pass
class droneDSLLib_Gauche(CommandeBasique, GDr, Mouvement):

    pass
class droneDSLLib_RotationDroite(CommandeBasique, Mouvement, RGRD):

    pass
class droneDSLLib_Parallele(Mouvement):

    pass
class droneDSLLib_RotationGauche(CommandeBasique, Mouvement, RGRD):

    pass
class droneDSLLib_Reculer(CommandeBasique, Mouvement, AR):

    pass
class droneDSLLib_Monter(CommandeBasique, MD, Mouvement):

    pass
class DecollerAtterrir:

    pass
class droneDSLLib_Atterrir(DecollerAtterrir):

    pass
class droneDSLLib_Decoller(DecollerAtterrir):

    pass
class droneDSLLib_SecondeExp:

    pass
class droneDSLLib_PourcentExp:

    pass
class droneDSLLib_VarDecl:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class PourcentExp:

    pass
class droneDSLLib_RefPourcentVar(PourcentExp):

    pass
class droneDSLLib_PourcentConst(PourcentExp):

    def __init__(self, val: str, droneDSLLib_PourcentConst: "droneDSLLib_PourcentDecl" = None):
        self.val = val
        self.droneDSLLib_PourcentConst = droneDSLLib_PourcentConst
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def droneDSLLib_PourcentConst(self):
        return self.__droneDSLLib_PourcentConst

    @droneDSLLib_PourcentConst.setter
    def droneDSLLib_PourcentConst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSLLib_PourcentConst__droneDSLLib_PourcentConst", None)
        self.__droneDSLLib_PourcentConst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSLLib_PourcentDecl"):
                opp_val = getattr(old_value, "droneDSLLib_PourcentDecl", None)
                if opp_val == self:
                    setattr(old_value, "droneDSLLib_PourcentDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSLLib_PourcentDecl"):
                opp_val = getattr(value, "droneDSLLib_PourcentDecl", None)
                setattr(value, "droneDSLLib_PourcentDecl", self)

class SecondeExp:

    pass
class droneDSLLib_RefSecondeVar(SecondeExp):

    pass
class droneDSLLib_SecondeConst(SecondeExp):

    def __init__(self, val: str, droneDSLLib_SecondeConst: "droneDSLLib_SecondeDecl" = None):
        self.val = val
        self.droneDSLLib_SecondeConst = droneDSLLib_SecondeConst
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def droneDSLLib_SecondeConst(self):
        return self.__droneDSLLib_SecondeConst

    @droneDSLLib_SecondeConst.setter
    def droneDSLLib_SecondeConst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSLLib_SecondeConst__droneDSLLib_SecondeConst", None)
        self.__droneDSLLib_SecondeConst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSLLib_SecondeDecl"):
                opp_val = getattr(old_value, "droneDSLLib_SecondeDecl", None)
                if opp_val == self:
                    setattr(old_value, "droneDSLLib_SecondeDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSLLib_SecondeDecl"):
                opp_val = getattr(value, "droneDSLLib_SecondeDecl", None)
                setattr(value, "droneDSLLib_SecondeDecl", self)

class droneDSLLib_FonctionDecl:

    def __init__(self, name: str, droneDSLLib_FonctionDecl: "droneDSLLib_Model" = None, droneDSLLib_FonctionDecl48: set["droneDSLLib_EObject"] = None, droneDSLLib_FonctionDecl50: "droneDSLLib_FonctionCallInterne" = None):
        self.name = name
        self.droneDSLLib_FonctionDecl = droneDSLLib_FonctionDecl
        self.droneDSLLib_FonctionDecl48 = droneDSLLib_FonctionDecl48 if droneDSLLib_FonctionDecl48 is not None else set()
        self.droneDSLLib_FonctionDecl50 = droneDSLLib_FonctionDecl50
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def droneDSLLib_FonctionDecl50(self):
        return self.__droneDSLLib_FonctionDecl50

    @droneDSLLib_FonctionDecl50.setter
    def droneDSLLib_FonctionDecl50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSLLib_FonctionDecl__droneDSLLib_FonctionDecl50", None)
        self.__droneDSLLib_FonctionDecl50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSLLib_FonctionCallInterne"):
                opp_val = getattr(old_value, "droneDSLLib_FonctionCallInterne", None)
                if opp_val == self:
                    setattr(old_value, "droneDSLLib_FonctionCallInterne", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSLLib_FonctionCallInterne"):
                opp_val = getattr(value, "droneDSLLib_FonctionCallInterne", None)
                setattr(value, "droneDSLLib_FonctionCallInterne", self)

    @property
    def droneDSLLib_FonctionDecl(self):
        return self.__droneDSLLib_FonctionDecl

    @droneDSLLib_FonctionDecl.setter
    def droneDSLLib_FonctionDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSLLib_FonctionDecl__droneDSLLib_FonctionDecl", None)
        self.__droneDSLLib_FonctionDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSLLib_Model"):
                opp_val = getattr(old_value, "droneDSLLib_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSLLib_Model"):
                opp_val = getattr(value, "droneDSLLib_Model", None)
                if opp_val is None:
                    setattr(value, "droneDSLLib_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def droneDSLLib_FonctionDecl48(self):
        return self.__droneDSLLib_FonctionDecl48

    @droneDSLLib_FonctionDecl48.setter
    def droneDSLLib_FonctionDecl48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSLLib_FonctionDecl__droneDSLLib_FonctionDecl48", None)
        self.__droneDSLLib_FonctionDecl48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "droneDSLLib_EObject"):
                    opp_val = getattr(item, "droneDSLLib_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "droneDSLLib_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "droneDSLLib_EObject"):
                    opp_val = getattr(item, "droneDSLLib_EObject", None)
                    
                    setattr(item, "droneDSLLib_EObject", self)
                    

class droneDSLLib_Model:

    pass