from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Parallele:

    pass
class droneDSL_Parallele4(Parallele):

    pass
class droneDSL_Parallele3(Parallele):

    pass
class droneDSL_Parallele2(Parallele):

    pass
class droneDSL_AR:

    pass
class droneDSL_RGRD:

    pass
class droneDSL_GDr:

    pass
class droneDSL_MD:

    pass
class FonctionCall:

    pass
class droneDSL_FonctionCallExterne(FonctionCall):

    def __init__(self, name: str, droneDSL_FonctionCallExterne: "droneDSL_Import" = None):
        self.name = name
        self.droneDSL_FonctionCallExterne = droneDSL_FonctionCallExterne
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def droneDSL_FonctionCallExterne(self):
        return self.__droneDSL_FonctionCallExterne

    @droneDSL_FonctionCallExterne.setter
    def droneDSL_FonctionCallExterne(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_FonctionCallExterne__droneDSL_FonctionCallExterne", None)
        self.__droneDSL_FonctionCallExterne = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Import83"):
                opp_val = getattr(old_value, "droneDSL_Import83", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Import83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Import83"):
                opp_val = getattr(value, "droneDSL_Import83", None)
                setattr(value, "droneDSL_Import83", self)

class droneDSL_FonctionCallInterne(FonctionCall):

    pass
class droneDSL_FonctionCall:

    pass
class droneDSL_FinDeMain:

    def __init__(self, accolade: str, droneDSL_FinDeMain: "droneDSL_Main" = None):
        self.accolade = accolade
        self.droneDSL_FinDeMain = droneDSL_FinDeMain
        
    @property
    def accolade(self) -> str:
        return self.__accolade

    @accolade.setter
    def accolade(self, accolade: str):
        self.__accolade = accolade

    @property
    def droneDSL_FinDeMain(self):
        return self.__droneDSL_FinDeMain

    @droneDSL_FinDeMain.setter
    def droneDSL_FinDeMain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_FinDeMain__droneDSL_FinDeMain", None)
        self.__droneDSL_FinDeMain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Main92"):
                opp_val = getattr(old_value, "droneDSL_Main92", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Main92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Main92"):
                opp_val = getattr(value, "droneDSL_Main92", None)
                setattr(value, "droneDSL_Main92", self)

class droneDSL_EObject:

    pass
class droneDSL_CommandeBasique:

    pass
class droneDSL_DecollerAtterrir:

    def __init__(self, str: str):
        self.str = str
        
    @property
    def str(self) -> str:
        return self.__str

    @str.setter
    def str(self, str: str):
        self.__str = str

class droneDSL_Mouvement:

    pass
class RGRD:

    pass
class GDr:

    pass
class AR:

    pass
class MD:

    pass
class CommandeBasique:

    pass
class droneDSL_Pause(CommandeBasique):

    pass
class Mouvement:

    pass
class droneDSL_Avancer(AR, CommandeBasique, Mouvement):

    pass
class droneDSL_Descendre(MD, CommandeBasique, Mouvement):

    pass
class droneDSL_Reculer(AR, CommandeBasique, Mouvement):

    pass
class droneDSL_Parallele(Mouvement):

    pass
class droneDSL_RotationGauche(RGRD, CommandeBasique, Mouvement):

    pass
class droneDSL_Gauche(GDr, CommandeBasique, Mouvement):

    pass
class droneDSL_RotationDroite(RGRD, CommandeBasique, Mouvement):

    pass
class droneDSL_Droite(GDr, CommandeBasique, Mouvement):

    pass
class droneDSL_Monter(MD, CommandeBasique, Mouvement):

    pass
class DecollerAtterrir:

    pass
class droneDSL_Atterrir(DecollerAtterrir):

    pass
class droneDSL_Decoller(DecollerAtterrir):

    pass
class droneDSL_SecondeExp:

    pass
class droneDSL_PourcentExp:

    pass
class droneDSL_VarDecl:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class VarDecl:

    pass
class droneDSL_PourcentDecl(VarDecl):

    pass
class droneDSL_SecondeDecl(VarDecl):

    pass
class PourcentExp:

    pass
class droneDSL_RefPourcentVar(PourcentExp):

    pass
class SecondeExp:

    pass
class droneDSL_RefSecondeVar(SecondeExp):

    pass
class droneDSL_Eloignement_max:

    pass
class droneDSL_SecondeConst(SecondeExp):

    def __init__(self, val: str, droneDSL_SecondeConst: "droneDSL_Hauteur_max" = None, droneDSL_SecondeConst14: "droneDSL_Eloignement_max" = None, droneDSL_SecondeConst31: "droneDSL_SecondeDecl" = None):
        self.val = val
        self.droneDSL_SecondeConst = droneDSL_SecondeConst
        self.droneDSL_SecondeConst14 = droneDSL_SecondeConst14
        self.droneDSL_SecondeConst31 = droneDSL_SecondeConst31
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def droneDSL_SecondeConst31(self):
        return self.__droneDSL_SecondeConst31

    @droneDSL_SecondeConst31.setter
    def droneDSL_SecondeConst31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_SecondeConst__droneDSL_SecondeConst31", None)
        self.__droneDSL_SecondeConst31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_SecondeDecl"):
                opp_val = getattr(old_value, "droneDSL_SecondeDecl", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_SecondeDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_SecondeDecl"):
                opp_val = getattr(value, "droneDSL_SecondeDecl", None)
                setattr(value, "droneDSL_SecondeDecl", self)

    @property
    def droneDSL_SecondeConst14(self):
        return self.__droneDSL_SecondeConst14

    @droneDSL_SecondeConst14.setter
    def droneDSL_SecondeConst14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_SecondeConst__droneDSL_SecondeConst14", None)
        self.__droneDSL_SecondeConst14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Eloignement_max"):
                opp_val = getattr(old_value, "droneDSL_Eloignement_max", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Eloignement_max", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Eloignement_max"):
                opp_val = getattr(value, "droneDSL_Eloignement_max", None)
                setattr(value, "droneDSL_Eloignement_max", self)

    @property
    def droneDSL_SecondeConst(self):
        return self.__droneDSL_SecondeConst

    @droneDSL_SecondeConst.setter
    def droneDSL_SecondeConst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_SecondeConst__droneDSL_SecondeConst", None)
        self.__droneDSL_SecondeConst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Hauteur_max"):
                opp_val = getattr(old_value, "droneDSL_Hauteur_max", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Hauteur_max", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Hauteur_max"):
                opp_val = getattr(value, "droneDSL_Hauteur_max", None)
                setattr(value, "droneDSL_Hauteur_max", self)

class droneDSL_Hauteur_max:

    pass
class droneDSL_Pourcent_vitesse_rotation_max:

    pass
class droneDSL_Pourcent_vitesse_deplacement_max:

    pass
class droneDSL_PourcentConst(PourcentExp):

    def __init__(self, val: str, droneDSL_PourcentConst: "droneDSL_Pourcent_vitesse_hauteur_max" = None, droneDSL_PourcentConst9: "droneDSL_Pourcent_vitesse_deplacement_max" = None, droneDSL_PourcentConst11: "droneDSL_Pourcent_vitesse_rotation_max" = None, droneDSL_PourcentConst33: "droneDSL_PourcentDecl" = None):
        self.val = val
        self.droneDSL_PourcentConst = droneDSL_PourcentConst
        self.droneDSL_PourcentConst9 = droneDSL_PourcentConst9
        self.droneDSL_PourcentConst11 = droneDSL_PourcentConst11
        self.droneDSL_PourcentConst33 = droneDSL_PourcentConst33
        
    @property
    def val(self) -> str:
        return self.__val

    @val.setter
    def val(self, val: str):
        self.__val = val

    @property
    def droneDSL_PourcentConst11(self):
        return self.__droneDSL_PourcentConst11

    @droneDSL_PourcentConst11.setter
    def droneDSL_PourcentConst11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_PourcentConst__droneDSL_PourcentConst11", None)
        self.__droneDSL_PourcentConst11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Pourcent_vitesse_rotation_max"):
                opp_val = getattr(old_value, "droneDSL_Pourcent_vitesse_rotation_max", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Pourcent_vitesse_rotation_max", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Pourcent_vitesse_rotation_max"):
                opp_val = getattr(value, "droneDSL_Pourcent_vitesse_rotation_max", None)
                setattr(value, "droneDSL_Pourcent_vitesse_rotation_max", self)

    @property
    def droneDSL_PourcentConst9(self):
        return self.__droneDSL_PourcentConst9

    @droneDSL_PourcentConst9.setter
    def droneDSL_PourcentConst9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_PourcentConst__droneDSL_PourcentConst9", None)
        self.__droneDSL_PourcentConst9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Pourcent_vitesse_deplacement_max"):
                opp_val = getattr(old_value, "droneDSL_Pourcent_vitesse_deplacement_max", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Pourcent_vitesse_deplacement_max", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Pourcent_vitesse_deplacement_max"):
                opp_val = getattr(value, "droneDSL_Pourcent_vitesse_deplacement_max", None)
                setattr(value, "droneDSL_Pourcent_vitesse_deplacement_max", self)

    @property
    def droneDSL_PourcentConst(self):
        return self.__droneDSL_PourcentConst

    @droneDSL_PourcentConst.setter
    def droneDSL_PourcentConst(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_PourcentConst__droneDSL_PourcentConst", None)
        self.__droneDSL_PourcentConst = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Pourcent_vitesse_hauteur_max"):
                opp_val = getattr(old_value, "droneDSL_Pourcent_vitesse_hauteur_max", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_Pourcent_vitesse_hauteur_max", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Pourcent_vitesse_hauteur_max"):
                opp_val = getattr(value, "droneDSL_Pourcent_vitesse_hauteur_max", None)
                setattr(value, "droneDSL_Pourcent_vitesse_hauteur_max", self)

    @property
    def droneDSL_PourcentConst33(self):
        return self.__droneDSL_PourcentConst33

    @droneDSL_PourcentConst33.setter
    def droneDSL_PourcentConst33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_PourcentConst__droneDSL_PourcentConst33", None)
        self.__droneDSL_PourcentConst33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_PourcentDecl"):
                opp_val = getattr(old_value, "droneDSL_PourcentDecl", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_PourcentDecl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_PourcentDecl"):
                opp_val = getattr(value, "droneDSL_PourcentDecl", None)
                setattr(value, "droneDSL_PourcentDecl", self)

class droneDSL_Pourcent_vitesse_hauteur_max:

    pass
class droneDSL_FonctionDecl:

    def __init__(self, name: str, droneDSL_FonctionDecl: "droneDSL_Model" = None, droneDSL_FonctionDecl79: set["droneDSL_EObject"] = None, droneDSL_FonctionDecl81: "droneDSL_FonctionCallInterne" = None):
        self.name = name
        self.droneDSL_FonctionDecl = droneDSL_FonctionDecl
        self.droneDSL_FonctionDecl79 = droneDSL_FonctionDecl79 if droneDSL_FonctionDecl79 is not None else set()
        self.droneDSL_FonctionDecl81 = droneDSL_FonctionDecl81
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def droneDSL_FonctionDecl81(self):
        return self.__droneDSL_FonctionDecl81

    @droneDSL_FonctionDecl81.setter
    def droneDSL_FonctionDecl81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_FonctionDecl__droneDSL_FonctionDecl81", None)
        self.__droneDSL_FonctionDecl81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_FonctionCallInterne"):
                opp_val = getattr(old_value, "droneDSL_FonctionCallInterne", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_FonctionCallInterne", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_FonctionCallInterne"):
                opp_val = getattr(value, "droneDSL_FonctionCallInterne", None)
                setattr(value, "droneDSL_FonctionCallInterne", self)

    @property
    def droneDSL_FonctionDecl(self):
        return self.__droneDSL_FonctionDecl

    @droneDSL_FonctionDecl.setter
    def droneDSL_FonctionDecl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_FonctionDecl__droneDSL_FonctionDecl", None)
        self.__droneDSL_FonctionDecl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Model6"):
                opp_val = getattr(old_value, "droneDSL_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Model6"):
                opp_val = getattr(value, "droneDSL_Model6", None)
                if opp_val is None:
                    setattr(value, "droneDSL_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def droneDSL_FonctionDecl79(self):
        return self.__droneDSL_FonctionDecl79

    @droneDSL_FonctionDecl79.setter
    def droneDSL_FonctionDecl79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_FonctionDecl__droneDSL_FonctionDecl79", None)
        self.__droneDSL_FonctionDecl79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "droneDSL_EObject"):
                    opp_val = getattr(item, "droneDSL_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "droneDSL_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "droneDSL_EObject"):
                    opp_val = getattr(item, "droneDSL_EObject", None)
                    
                    setattr(item, "droneDSL_EObject", self)
                    

class droneDSL_Main:

    pass
class droneDSL_Prologue:

    pass
class droneDSL_Import:

    def __init__(self, name: str, droneDSL_Import: "droneDSL_Model" = None, droneDSL_Import83: "droneDSL_FonctionCallExterne" = None):
        self.name = name
        self.droneDSL_Import = droneDSL_Import
        self.droneDSL_Import83 = droneDSL_Import83
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def droneDSL_Import83(self):
        return self.__droneDSL_Import83

    @droneDSL_Import83.setter
    def droneDSL_Import83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_Import__droneDSL_Import83", None)
        self.__droneDSL_Import83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_FonctionCallExterne"):
                opp_val = getattr(old_value, "droneDSL_FonctionCallExterne", None)
                if opp_val == self:
                    setattr(old_value, "droneDSL_FonctionCallExterne", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_FonctionCallExterne"):
                opp_val = getattr(value, "droneDSL_FonctionCallExterne", None)
                setattr(value, "droneDSL_FonctionCallExterne", self)

    @property
    def droneDSL_Import(self):
        return self.__droneDSL_Import

    @droneDSL_Import.setter
    def droneDSL_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_droneDSL_Import__droneDSL_Import", None)
        self.__droneDSL_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneDSL_Model"):
                opp_val = getattr(old_value, "droneDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneDSL_Model"):
                opp_val = getattr(value, "droneDSL_Model", None)
                if opp_val is None:
                    setattr(value, "droneDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class droneDSL_Model:

    pass