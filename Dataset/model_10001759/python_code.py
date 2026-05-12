from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class voiture:

    def __init__(self, type_de_voiture: str, nombre_de_si_ges: int):
        self.type_de_voiture = type_de_voiture
        self.nombre_de_si_ges = nombre_de_si_ges
        
        pass
    @property
    def nombre_de_si_ges(self):
        return self.__nombre_de_si_ges
    @nombre_de_si_ges.setter
    def nombre_de_si_ges(self, nombre_de_si_ges: int):
        self.__nombre_de_si_ges = nombre_de_si_ges

    @property
    def type_de_voiture(self):
        return self.__type_de_voiture
    @type_de_voiture.setter
    def type_de_voiture(self, type_de_voiture: str):
        self.__type_de_voiture = type_de_voiture



class conducteur:

    def __init__(self, informations_conducteur: str, inscription16: "inscription" = None):
        self.informations_conducteur = informations_conducteur
        self.inscription16 = inscription16
        
        pass
    @property
    def informations_conducteur(self):
        return self.__informations_conducteur
    @informations_conducteur.setter
    def informations_conducteur(self, informations_conducteur: str):
        self.__informations_conducteur = informations_conducteur

    @property
    def inscription16(self):
        return self.__inscription16
    @inscription16.setter
    def inscription16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conducteur__inscription16", None)
        self.__inscription16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conducteur17"):
                opp_val = getattr(old_value, "conducteur17", None)
                if opp_val == self:
                    setattr(old_value, "conducteur17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conducteur17"):
                opp_val = getattr(value, "conducteur17", None)
                setattr(value, "conducteur17", self)



class passager:

    def __init__(self, informations_passager: str, inscription0: "inscription" = None, compte2: "compte" = None, paiement5: "paiement" = None, administrateur10: "administrateur" = None, trajet14: "trajet" = None):
        self.informations_passager = informations_passager
        self.inscription0 = inscription0
        self.compte2 = compte2
        self.paiement5 = paiement5
        self.administrateur10 = administrateur10
        self.trajet14 = trajet14
        
        pass
    @property
    def informations_passager(self):
        return self.__informations_passager
    @informations_passager.setter
    def informations_passager(self, informations_passager: str):
        self.__informations_passager = informations_passager

    @property
    def paiement5(self):
        return self.__paiement5
    @paiement5.setter
    def paiement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_passager__paiement5", None)
        self.__paiement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passager4"):
                opp_val = getattr(old_value, "passager4", None)
                if opp_val == self:
                    setattr(old_value, "passager4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passager4"):
                opp_val = getattr(value, "passager4", None)
                setattr(value, "passager4", self)

    @property
    def administrateur10(self):
        return self.__administrateur10
    @administrateur10.setter
    def administrateur10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_passager__administrateur10", None)
        self.__administrateur10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passager11"):
                opp_val = getattr(old_value, "passager11", None)
                if opp_val == self:
                    setattr(old_value, "passager11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passager11"):
                opp_val = getattr(value, "passager11", None)
                setattr(value, "passager11", self)

    @property
    def inscription0(self):
        return self.__inscription0
    @inscription0.setter
    def inscription0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_passager__inscription0", None)
        self.__inscription0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passager1"):
                opp_val = getattr(old_value, "passager1", None)
                if opp_val == self:
                    setattr(old_value, "passager1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passager1"):
                opp_val = getattr(value, "passager1", None)
                setattr(value, "passager1", self)

    @property
    def trajet14(self):
        return self.__trajet14
    @trajet14.setter
    def trajet14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_passager__trajet14", None)
        self.__trajet14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passager15"):
                opp_val = getattr(old_value, "passager15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passager15"):
                opp_val = getattr(value, "passager15", None)
                if opp_val is None:
                    setattr(value, "passager15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compte2(self):
        return self.__compte2
    @compte2.setter
    def compte2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_passager__compte2", None)
        self.__compte2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passager3"):
                opp_val = getattr(old_value, "passager3", None)
                if opp_val == self:
                    setattr(old_value, "passager3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passager3"):
                opp_val = getattr(value, "passager3", None)
                setattr(value, "passager3", self)



class inscription:

    def __init__(self, informations_passager: str, informations_conducteur: str, passager1: "passager" = None, administrateur12: "administrateur" = None, conducteur17: "conducteur" = None):
        self.informations_passager = informations_passager
        self.informations_conducteur = informations_conducteur
        self.passager1 = passager1
        self.administrateur12 = administrateur12
        self.conducteur17 = conducteur17
        
        pass
    @property
    def informations_conducteur(self):
        return self.__informations_conducteur
    @informations_conducteur.setter
    def informations_conducteur(self, informations_conducteur: str):
        self.__informations_conducteur = informations_conducteur

    @property
    def informations_passager(self):
        return self.__informations_passager
    @informations_passager.setter
    def informations_passager(self, informations_passager: str):
        self.__informations_passager = informations_passager

    @property
    def administrateur12(self):
        return self.__administrateur12
    @administrateur12.setter
    def administrateur12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_inscription__administrateur12", None)
        self.__administrateur12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inscription13"):
                opp_val = getattr(old_value, "inscription13", None)
                if opp_val == self:
                    setattr(old_value, "inscription13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inscription13"):
                opp_val = getattr(value, "inscription13", None)
                setattr(value, "inscription13", self)

    @property
    def conducteur17(self):
        return self.__conducteur17
    @conducteur17.setter
    def conducteur17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_inscription__conducteur17", None)
        self.__conducteur17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inscription16"):
                opp_val = getattr(old_value, "inscription16", None)
                if opp_val == self:
                    setattr(old_value, "inscription16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inscription16"):
                opp_val = getattr(value, "inscription16", None)
                setattr(value, "inscription16", self)

    @property
    def passager1(self):
        return self.__passager1
    @passager1.setter
    def passager1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_inscription__passager1", None)
        self.__passager1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inscription0"):
                opp_val = getattr(old_value, "inscription0", None)
                if opp_val == self:
                    setattr(old_value, "inscription0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inscription0"):
                opp_val = getattr(value, "inscription0", None)
                setattr(value, "inscription0", self)



class administrateur:

    pass


class trajet:

    def __init__(self, prix_du_trajet: float, l_heure_de_d_part: float, la_date: str, lieu_de_d_part: str, passager15: set["passager"] = None, administrateur18: "administrateur" = None):
        self.prix_du_trajet = prix_du_trajet
        self.l_heure_de_d_part = l_heure_de_d_part
        self.la_date = la_date
        self.lieu_de_d_part = lieu_de_d_part
        self.passager15 = passager15 if passager15 is not None else set()
        self.administrateur18 = administrateur18
        
        pass
    @property
    def prix_du_trajet(self):
        return self.__prix_du_trajet
    @prix_du_trajet.setter
    def prix_du_trajet(self, prix_du_trajet: float):
        self.__prix_du_trajet = prix_du_trajet

    @property
    def l_heure_de_d_part(self):
        return self.__l_heure_de_d_part
    @l_heure_de_d_part.setter
    def l_heure_de_d_part(self, l_heure_de_d_part: float):
        self.__l_heure_de_d_part = l_heure_de_d_part

    @property
    def la_date(self):
        return self.__la_date
    @la_date.setter
    def la_date(self, la_date: str):
        self.__la_date = la_date

    @property
    def lieu_de_d_part(self):
        return self.__lieu_de_d_part
    @lieu_de_d_part.setter
    def lieu_de_d_part(self, lieu_de_d_part: str):
        self.__lieu_de_d_part = lieu_de_d_part

    @property
    def passager15(self):
        return self.__passager15
    @passager15.setter
    def passager15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trajet__passager15", None)
        self.__passager15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trajet14"):
                    opp_val = getattr(item, "trajet14", None)
                    
                    if opp_val == self:
                        setattr(item, "trajet14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trajet14"):
                    opp_val = getattr(item, "trajet14", None)
                    
                    setattr(item, "trajet14", self)
                    

    @property
    def administrateur18(self):
        return self.__administrateur18
    @administrateur18.setter
    def administrateur18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trajet__administrateur18", None)
        self.__administrateur18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trajet19"):
                opp_val = getattr(old_value, "trajet19", None)
                if opp_val == self:
                    setattr(old_value, "trajet19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trajet19"):
                opp_val = getattr(value, "trajet19", None)
                setattr(value, "trajet19", self)



class paiement:

    def __init__(self, m_thode_de_paiement: str, passager4: "passager" = None, administrateur8: "administrateur" = None):
        self.m_thode_de_paiement = m_thode_de_paiement
        self.passager4 = passager4
        self.administrateur8 = administrateur8
        
        pass
    @property
    def m_thode_de_paiement(self):
        return self.__m_thode_de_paiement
    @m_thode_de_paiement.setter
    def m_thode_de_paiement(self, m_thode_de_paiement: str):
        self.__m_thode_de_paiement = m_thode_de_paiement

    @property
    def passager4(self):
        return self.__passager4
    @passager4.setter
    def passager4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paiement__passager4", None)
        self.__passager4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paiement5"):
                opp_val = getattr(old_value, "paiement5", None)
                if opp_val == self:
                    setattr(old_value, "paiement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paiement5"):
                opp_val = getattr(value, "paiement5", None)
                setattr(value, "paiement5", self)

    @property
    def administrateur8(self):
        return self.__administrateur8
    @administrateur8.setter
    def administrateur8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_paiement__administrateur8", None)
        self.__administrateur8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paiement9"):
                opp_val = getattr(old_value, "paiement9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paiement9"):
                opp_val = getattr(value, "paiement9", None)
                if opp_val is None:
                    setattr(value, "paiement9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class reservation:

    def __init__(self, nombre_de_passager: int, administrateur6: "administrateur" = None):
        self.nombre_de_passager = nombre_de_passager
        self.administrateur6 = administrateur6
        
        pass
    @property
    def nombre_de_passager(self):
        return self.__nombre_de_passager
    @nombre_de_passager.setter
    def nombre_de_passager(self, nombre_de_passager: int):
        self.__nombre_de_passager = nombre_de_passager

    @property
    def administrateur6(self):
        return self.__administrateur6
    @administrateur6.setter
    def administrateur6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_reservation__administrateur6", None)
        self.__administrateur6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservation7"):
                opp_val = getattr(old_value, "reservation7", None)
                if opp_val == self:
                    setattr(old_value, "reservation7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservation7"):
                opp_val = getattr(value, "reservation7", None)
                setattr(value, "reservation7", self)



class compte:

    def __init__(self, informations_conducteur: str, informations_passager: str, passager3: "passager" = None):
        self.informations_conducteur = informations_conducteur
        self.informations_passager = informations_passager
        self.passager3 = passager3
        
        pass
    @property
    def informations_passager(self):
        return self.__informations_passager
    @informations_passager.setter
    def informations_passager(self, informations_passager: str):
        self.__informations_passager = informations_passager

    @property
    def informations_conducteur(self):
        return self.__informations_conducteur
    @informations_conducteur.setter
    def informations_conducteur(self, informations_conducteur: str):
        self.__informations_conducteur = informations_conducteur

    @property
    def passager3(self):
        return self.__passager3
    @passager3.setter
    def passager3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_compte__passager3", None)
        self.__passager3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "compte2"):
                opp_val = getattr(old_value, "compte2", None)
                if opp_val == self:
                    setattr(old_value, "compte2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "compte2"):
                opp_val = getattr(value, "compte2", None)
                setattr(value, "compte2", self)

