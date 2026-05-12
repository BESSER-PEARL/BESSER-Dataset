from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class latex_Subsection:

    def __init__(self, subsectionprefix: str, subsectionname: str, subsectiontext: str, latex_Subsection: "latex_Section" = None, latex_Subsection44: "latex_Subsection" = None, latex_Subsection42: set["latex_Subsection"] = None, latex_Subsection46: set["latex_General"] = None):
        self.subsectionprefix = subsectionprefix
        self.subsectionname = subsectionname
        self.subsectiontext = subsectiontext
        self.latex_Subsection = latex_Subsection
        self.latex_Subsection44 = latex_Subsection44
        self.latex_Subsection42 = latex_Subsection42 if latex_Subsection42 is not None else set()
        self.latex_Subsection46 = latex_Subsection46 if latex_Subsection46 is not None else set()
        
        pass
    @property
    def subsectiontext(self):
        return self.__subsectiontext

    @subsectiontext.setter
    def subsectiontext(self, subsectiontext: str):
        self.__subsectiontext = subsectiontext


    @property
    def subsectionname(self):
        return self.__subsectionname

    @subsectionname.setter
    def subsectionname(self, subsectionname: str):
        self.__subsectionname = subsectionname


    @property
    def subsectionprefix(self):
        return self.__subsectionprefix

    @subsectionprefix.setter
    def subsectionprefix(self, subsectionprefix: str):
        self.__subsectionprefix = subsectionprefix


    @property
    def latex_Subsection44(self):
        return self.__latex_Subsection44

    @latex_Subsection44.setter
    def latex_Subsection44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Subsection__latex_Subsection44", None)
        self.__latex_Subsection44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Subsection42"):
                opp_val = getattr(old_value, "latex_Subsection42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Subsection42"):
                opp_val = getattr(value, "latex_Subsection42", None)
                if opp_val is None:
                    setattr(value, "latex_Subsection42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_Subsection46(self):
        return self.__latex_Subsection46

    @latex_Subsection46.setter
    def latex_Subsection46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Subsection__latex_Subsection46", None)
        self.__latex_Subsection46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General47"):
                    opp_val = getattr(item, "latex_General47", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General47"):
                    opp_val = getattr(item, "latex_General47", None)
                    
                    setattr(item, "latex_General47", self)
                    

    @property
    def latex_Subsection42(self):
        return self.__latex_Subsection42

    @latex_Subsection42.setter
    def latex_Subsection42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Subsection__latex_Subsection42", None)
        self.__latex_Subsection42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_Subsection44"):
                    opp_val = getattr(item, "latex_Subsection44", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_Subsection44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_Subsection44"):
                    opp_val = getattr(item, "latex_Subsection44", None)
                    
                    setattr(item, "latex_Subsection44", self)
                    

    @property
    def latex_Subsection(self):
        return self.__latex_Subsection

    @latex_Subsection.setter
    def latex_Subsection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Subsection__latex_Subsection", None)
        self.__latex_Subsection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Section41"):
                opp_val = getattr(old_value, "latex_Section41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Section41"):
                opp_val = getattr(value, "latex_Section41", None)
                if opp_val is None:
                    setattr(value, "latex_Section41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Endbib:

    def __init__(self, Endbibprefix: str, latex_Endbib: "latex_Bibliography" = None):
        self.Endbibprefix = Endbibprefix
        self.latex_Endbib = latex_Endbib
        
        pass
    @property
    def Endbibprefix(self):
        return self.__Endbibprefix

    @Endbibprefix.setter
    def Endbibprefix(self, Endbibprefix: str):
        self.__Endbibprefix = Endbibprefix


    @property
    def latex_Endbib(self):
        return self.__latex_Endbib

    @latex_Endbib.setter
    def latex_Endbib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Endbib__latex_Endbib", None)
        self.__latex_Endbib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Bibliography36"):
                opp_val = getattr(old_value, "latex_Bibliography36", None)
                if opp_val == self:
                    setattr(old_value, "latex_Bibliography36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Bibliography36"):
                opp_val = getattr(value, "latex_Bibliography36", None)
                setattr(value, "latex_Bibliography36", self)

class latex_Beginbib:

    def __init__(self, Beginbibprefix: str, latex_Beginbib: "latex_Bibliography" = None):
        self.Beginbibprefix = Beginbibprefix
        self.latex_Beginbib = latex_Beginbib
        
        pass
    @property
    def Beginbibprefix(self):
        return self.__Beginbibprefix

    @Beginbibprefix.setter
    def Beginbibprefix(self, Beginbibprefix: str):
        self.__Beginbibprefix = Beginbibprefix


    @property
    def latex_Beginbib(self):
        return self.__latex_Beginbib

    @latex_Beginbib.setter
    def latex_Beginbib(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Beginbib__latex_Beginbib", None)
        self.__latex_Beginbib = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Bibliography34"):
                opp_val = getattr(old_value, "latex_Bibliography34", None)
                if opp_val == self:
                    setattr(old_value, "latex_Bibliography34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Bibliography34"):
                opp_val = getattr(value, "latex_Bibliography34", None)
                setattr(value, "latex_Bibliography34", self)

class latex_bibitem:

    def __init__(self, bibprefix: str, bibtext: str, latex_bibitem: "latex_Bibliography" = None):
        self.bibprefix = bibprefix
        self.bibtext = bibtext
        self.latex_bibitem = latex_bibitem
        
        pass
    @property
    def bibprefix(self):
        return self.__bibprefix

    @bibprefix.setter
    def bibprefix(self, bibprefix: str):
        self.__bibprefix = bibprefix


    @property
    def bibtext(self):
        return self.__bibtext

    @bibtext.setter
    def bibtext(self, bibtext: str):
        self.__bibtext = bibtext


    @property
    def latex_bibitem(self):
        return self.__latex_bibitem

    @latex_bibitem.setter
    def latex_bibitem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_bibitem__latex_bibitem", None)
        self.__latex_bibitem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Bibliography32"):
                opp_val = getattr(old_value, "latex_Bibliography32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Bibliography32"):
                opp_val = getattr(value, "latex_Bibliography32", None)
                if opp_val is None:
                    setattr(value, "latex_Bibliography32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Enumerate:

    def __init__(self, enumprefix: str, enumtext: str, latex_Enumerate: "latex_Body" = None, latex_Enumerate52: set["latex_General"] = None):
        self.enumprefix = enumprefix
        self.enumtext = enumtext
        self.latex_Enumerate = latex_Enumerate
        self.latex_Enumerate52 = latex_Enumerate52 if latex_Enumerate52 is not None else set()
        
        pass
    @property
    def enumprefix(self):
        return self.__enumprefix

    @enumprefix.setter
    def enumprefix(self, enumprefix: str):
        self.__enumprefix = enumprefix


    @property
    def enumtext(self):
        return self.__enumtext

    @enumtext.setter
    def enumtext(self, enumtext: str):
        self.__enumtext = enumtext


    @property
    def latex_Enumerate(self):
        return self.__latex_Enumerate

    @latex_Enumerate.setter
    def latex_Enumerate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Enumerate__latex_Enumerate", None)
        self.__latex_Enumerate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Body27"):
                opp_val = getattr(old_value, "latex_Body27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Body27"):
                opp_val = getattr(value, "latex_Body27", None)
                if opp_val is None:
                    setattr(value, "latex_Body27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_Enumerate52(self):
        return self.__latex_Enumerate52

    @latex_Enumerate52.setter
    def latex_Enumerate52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Enumerate__latex_Enumerate52", None)
        self.__latex_Enumerate52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General53"):
                    opp_val = getattr(item, "latex_General53", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General53"):
                    opp_val = getattr(item, "latex_General53", None)
                    
                    setattr(item, "latex_General53", self)
                    

class latex_Figures:

    def __init__(self, figprefix: str, figcaption: str, figname: str, latex_Figures: "latex_Body" = None, latex_Figures49: set["latex_General"] = None):
        self.figprefix = figprefix
        self.figcaption = figcaption
        self.figname = figname
        self.latex_Figures = latex_Figures
        self.latex_Figures49 = latex_Figures49 if latex_Figures49 is not None else set()
        
        pass
    @property
    def figname(self):
        return self.__figname

    @figname.setter
    def figname(self, figname: str):
        self.__figname = figname


    @property
    def figprefix(self):
        return self.__figprefix

    @figprefix.setter
    def figprefix(self, figprefix: str):
        self.__figprefix = figprefix


    @property
    def figcaption(self):
        return self.__figcaption

    @figcaption.setter
    def figcaption(self, figcaption: str):
        self.__figcaption = figcaption


    @property
    def latex_Figures49(self):
        return self.__latex_Figures49

    @latex_Figures49.setter
    def latex_Figures49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Figures__latex_Figures49", None)
        self.__latex_Figures49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General50"):
                    opp_val = getattr(item, "latex_General50", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General50"):
                    opp_val = getattr(item, "latex_General50", None)
                    
                    setattr(item, "latex_General50", self)
                    

    @property
    def latex_Figures(self):
        return self.__latex_Figures

    @latex_Figures.setter
    def latex_Figures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Figures__latex_Figures", None)
        self.__latex_Figures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Body25"):
                opp_val = getattr(old_value, "latex_Body25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Body25"):
                opp_val = getattr(value, "latex_Body25", None)
                if opp_val is None:
                    setattr(value, "latex_Body25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Section:

    def __init__(self, sectionprefix: str, sectionname: str, sectiontext: str, latex_Section: "latex_Body" = None, latex_Section38: set["latex_General"] = None, latex_Section41: set["latex_Subsection"] = None):
        self.sectionprefix = sectionprefix
        self.sectionname = sectionname
        self.sectiontext = sectiontext
        self.latex_Section = latex_Section
        self.latex_Section38 = latex_Section38 if latex_Section38 is not None else set()
        self.latex_Section41 = latex_Section41 if latex_Section41 is not None else set()
        
        pass
    @property
    def sectiontext(self):
        return self.__sectiontext

    @sectiontext.setter
    def sectiontext(self, sectiontext: str):
        self.__sectiontext = sectiontext


    @property
    def sectionname(self):
        return self.__sectionname

    @sectionname.setter
    def sectionname(self, sectionname: str):
        self.__sectionname = sectionname


    @property
    def sectionprefix(self):
        return self.__sectionprefix

    @sectionprefix.setter
    def sectionprefix(self, sectionprefix: str):
        self.__sectionprefix = sectionprefix


    @property
    def latex_Section38(self):
        return self.__latex_Section38

    @latex_Section38.setter
    def latex_Section38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Section__latex_Section38", None)
        self.__latex_Section38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General39"):
                    opp_val = getattr(item, "latex_General39", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General39"):
                    opp_val = getattr(item, "latex_General39", None)
                    
                    setattr(item, "latex_General39", self)
                    

    @property
    def latex_Section41(self):
        return self.__latex_Section41

    @latex_Section41.setter
    def latex_Section41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Section__latex_Section41", None)
        self.__latex_Section41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_Subsection"):
                    opp_val = getattr(item, "latex_Subsection", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_Subsection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_Subsection"):
                    opp_val = getattr(item, "latex_Subsection", None)
                    
                    setattr(item, "latex_Subsection", self)
                    

    @property
    def latex_Section(self):
        return self.__latex_Section

    @latex_Section.setter
    def latex_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Section__latex_Section", None)
        self.__latex_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Body23"):
                opp_val = getattr(old_value, "latex_Body23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Body23"):
                opp_val = getattr(value, "latex_Body23", None)
                if opp_val is None:
                    setattr(value, "latex_Body23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_End:

    def __init__(self, endprefix: str, latex_End: "latex_Document" = None):
        self.endprefix = endprefix
        self.latex_End = latex_End
        
        pass
    @property
    def endprefix(self):
        return self.__endprefix

    @endprefix.setter
    def endprefix(self, endprefix: str):
        self.__endprefix = endprefix


    @property
    def latex_End(self):
        return self.__latex_End

    @latex_End.setter
    def latex_End(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_End__latex_End", None)
        self.__latex_End = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document16"):
                opp_val = getattr(old_value, "latex_Document16", None)
                if opp_val == self:
                    setattr(old_value, "latex_Document16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document16"):
                opp_val = getattr(value, "latex_Document16", None)
                setattr(value, "latex_Document16", self)

class latex_Begin:

    def __init__(self, beginprefix: str, latex_Begin: "latex_Document" = None):
        self.beginprefix = beginprefix
        self.latex_Begin = latex_Begin
        
        pass
    @property
    def beginprefix(self):
        return self.__beginprefix

    @beginprefix.setter
    def beginprefix(self, beginprefix: str):
        self.__beginprefix = beginprefix


    @property
    def latex_Begin(self):
        return self.__latex_Begin

    @latex_Begin.setter
    def latex_Begin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Begin__latex_Begin", None)
        self.__latex_Begin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document14"):
                opp_val = getattr(old_value, "latex_Document14", None)
                if opp_val == self:
                    setattr(old_value, "latex_Document14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document14"):
                opp_val = getattr(value, "latex_Document14", None)
                setattr(value, "latex_Document14", self)

class latex_General:

    def __init__(self, genprefix: str, genname: str, gentext: str, latex_General: "latex_Title" = None, latex_General21: "latex_Abstracte" = None, latex_General30: "latex_Bibliography" = None, latex_General39: "latex_Section" = None, latex_General47: "latex_Subsection" = None, latex_General50: "latex_Figures" = None, latex_General53: "latex_Enumerate" = None):
        self.genprefix = genprefix
        self.genname = genname
        self.gentext = gentext
        self.latex_General = latex_General
        self.latex_General21 = latex_General21
        self.latex_General30 = latex_General30
        self.latex_General39 = latex_General39
        self.latex_General47 = latex_General47
        self.latex_General50 = latex_General50
        self.latex_General53 = latex_General53
        
        pass
    @property
    def genprefix(self):
        return self.__genprefix

    @genprefix.setter
    def genprefix(self, genprefix: str):
        self.__genprefix = genprefix


    @property
    def gentext(self):
        return self.__gentext

    @gentext.setter
    def gentext(self, gentext: str):
        self.__gentext = gentext


    @property
    def genname(self):
        return self.__genname

    @genname.setter
    def genname(self, genname: str):
        self.__genname = genname


    @property
    def latex_General50(self):
        return self.__latex_General50

    @latex_General50.setter
    def latex_General50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General50", None)
        self.__latex_General50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Figures49"):
                opp_val = getattr(old_value, "latex_Figures49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Figures49"):
                opp_val = getattr(value, "latex_Figures49", None)
                if opp_val is None:
                    setattr(value, "latex_Figures49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General47(self):
        return self.__latex_General47

    @latex_General47.setter
    def latex_General47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General47", None)
        self.__latex_General47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Subsection46"):
                opp_val = getattr(old_value, "latex_Subsection46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Subsection46"):
                opp_val = getattr(value, "latex_Subsection46", None)
                if opp_val is None:
                    setattr(value, "latex_Subsection46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General39(self):
        return self.__latex_General39

    @latex_General39.setter
    def latex_General39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General39", None)
        self.__latex_General39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Section38"):
                opp_val = getattr(old_value, "latex_Section38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Section38"):
                opp_val = getattr(value, "latex_Section38", None)
                if opp_val is None:
                    setattr(value, "latex_Section38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General(self):
        return self.__latex_General

    @latex_General.setter
    def latex_General(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General", None)
        self.__latex_General = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Title18"):
                opp_val = getattr(old_value, "latex_Title18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Title18"):
                opp_val = getattr(value, "latex_Title18", None)
                if opp_val is None:
                    setattr(value, "latex_Title18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General30(self):
        return self.__latex_General30

    @latex_General30.setter
    def latex_General30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General30", None)
        self.__latex_General30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Bibliography29"):
                opp_val = getattr(old_value, "latex_Bibliography29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Bibliography29"):
                opp_val = getattr(value, "latex_Bibliography29", None)
                if opp_val is None:
                    setattr(value, "latex_Bibliography29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General53(self):
        return self.__latex_General53

    @latex_General53.setter
    def latex_General53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General53", None)
        self.__latex_General53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Enumerate52"):
                opp_val = getattr(old_value, "latex_Enumerate52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Enumerate52"):
                opp_val = getattr(value, "latex_Enumerate52", None)
                if opp_val is None:
                    setattr(value, "latex_Enumerate52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def latex_General21(self):
        return self.__latex_General21

    @latex_General21.setter
    def latex_General21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_General__latex_General21", None)
        self.__latex_General21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Abstracte20"):
                opp_val = getattr(old_value, "latex_Abstracte20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Abstracte20"):
                opp_val = getattr(value, "latex_Abstracte20", None)
                if opp_val is None:
                    setattr(value, "latex_Abstracte20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Title:

    def __init__(self, titleprefix: str, titletext: str, authortext: str, latex_Title: "latex_Document" = None, latex_Title18: set["latex_General"] = None):
        self.titleprefix = titleprefix
        self.titletext = titletext
        self.authortext = authortext
        self.latex_Title = latex_Title
        self.latex_Title18 = latex_Title18 if latex_Title18 is not None else set()
        
        pass
    @property
    def authortext(self):
        return self.__authortext

    @authortext.setter
    def authortext(self, authortext: str):
        self.__authortext = authortext


    @property
    def titletext(self):
        return self.__titletext

    @titletext.setter
    def titletext(self, titletext: str):
        self.__titletext = titletext


    @property
    def titleprefix(self):
        return self.__titleprefix

    @titleprefix.setter
    def titleprefix(self, titleprefix: str):
        self.__titleprefix = titleprefix


    @property
    def latex_Title(self):
        return self.__latex_Title

    @latex_Title.setter
    def latex_Title(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Title__latex_Title", None)
        self.__latex_Title = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document4"):
                opp_val = getattr(old_value, "latex_Document4", None)
                if opp_val == self:
                    setattr(old_value, "latex_Document4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document4"):
                opp_val = getattr(value, "latex_Document4", None)
                setattr(value, "latex_Document4", self)

    @property
    def latex_Title18(self):
        return self.__latex_Title18

    @latex_Title18.setter
    def latex_Title18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Title__latex_Title18", None)
        self.__latex_Title18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General"):
                    opp_val = getattr(item, "latex_General", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General"):
                    opp_val = getattr(item, "latex_General", None)
                    
                    setattr(item, "latex_General", self)
                    

class latex_Commands:

    def __init__(self, number: float, comprefix: str, comname: str, comtext: str, latex_Commands: "latex_Document" = None):
        self.number = number
        self.comprefix = comprefix
        self.comname = comname
        self.comtext = comtext
        self.latex_Commands = latex_Commands
        
        pass
    @property
    def comtext(self):
        return self.__comtext

    @comtext.setter
    def comtext(self, comtext: str):
        self.__comtext = comtext


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: float):
        self.__number = number


    @property
    def comname(self):
        return self.__comname

    @comname.setter
    def comname(self, comname: str):
        self.__comname = comname


    @property
    def comprefix(self):
        return self.__comprefix

    @comprefix.setter
    def comprefix(self, comprefix: str):
        self.__comprefix = comprefix


    @property
    def latex_Commands(self):
        return self.__latex_Commands

    @latex_Commands.setter
    def latex_Commands(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Commands__latex_Commands", None)
        self.__latex_Commands = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document2"):
                opp_val = getattr(old_value, "latex_Document2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document2"):
                opp_val = getattr(value, "latex_Document2", None)
                if opp_val is None:
                    setattr(value, "latex_Document2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Packages:

    def __init__(self, packageprefix: str, packagetype: str, latex_Packages: "latex_Document" = None):
        self.packageprefix = packageprefix
        self.packagetype = packagetype
        self.latex_Packages = latex_Packages
        
        pass
    @property
    def packageprefix(self):
        return self.__packageprefix

    @packageprefix.setter
    def packageprefix(self, packageprefix: str):
        self.__packageprefix = packageprefix


    @property
    def packagetype(self):
        return self.__packagetype

    @packagetype.setter
    def packagetype(self, packagetype: str):
        self.__packagetype = packagetype


    @property
    def latex_Packages(self):
        return self.__latex_Packages

    @latex_Packages.setter
    def latex_Packages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Packages__latex_Packages", None)
        self.__latex_Packages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document"):
                opp_val = getattr(old_value, "latex_Document", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document"):
                opp_val = getattr(value, "latex_Document", None)
                if opp_val is None:
                    setattr(value, "latex_Document", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class latex_Bibliography:

    def __init__(self, bibstyle: str, latex_Bibliography: "latex_Document" = None, latex_Bibliography29: set["latex_General"] = None, latex_Bibliography32: set["latex_bibitem"] = None, latex_Bibliography34: "latex_Beginbib" = None, latex_Bibliography36: "latex_Endbib" = None):
        self.bibstyle = bibstyle
        self.latex_Bibliography = latex_Bibliography
        self.latex_Bibliography29 = latex_Bibliography29 if latex_Bibliography29 is not None else set()
        self.latex_Bibliography32 = latex_Bibliography32 if latex_Bibliography32 is not None else set()
        self.latex_Bibliography34 = latex_Bibliography34
        self.latex_Bibliography36 = latex_Bibliography36
        
        pass
    @property
    def bibstyle(self):
        return self.__bibstyle

    @bibstyle.setter
    def bibstyle(self, bibstyle: str):
        self.__bibstyle = bibstyle


    @property
    def latex_Bibliography36(self):
        return self.__latex_Bibliography36

    @latex_Bibliography36.setter
    def latex_Bibliography36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Bibliography__latex_Bibliography36", None)
        self.__latex_Bibliography36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Endbib"):
                opp_val = getattr(old_value, "latex_Endbib", None)
                if opp_val == self:
                    setattr(old_value, "latex_Endbib", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Endbib"):
                opp_val = getattr(value, "latex_Endbib", None)
                setattr(value, "latex_Endbib", self)

    @property
    def latex_Bibliography32(self):
        return self.__latex_Bibliography32

    @latex_Bibliography32.setter
    def latex_Bibliography32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Bibliography__latex_Bibliography32", None)
        self.__latex_Bibliography32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_bibitem"):
                    opp_val = getattr(item, "latex_bibitem", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_bibitem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_bibitem"):
                    opp_val = getattr(item, "latex_bibitem", None)
                    
                    setattr(item, "latex_bibitem", self)
                    

    @property
    def latex_Bibliography(self):
        return self.__latex_Bibliography

    @latex_Bibliography.setter
    def latex_Bibliography(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Bibliography__latex_Bibliography", None)
        self.__latex_Bibliography = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document12"):
                opp_val = getattr(old_value, "latex_Document12", None)
                if opp_val == self:
                    setattr(old_value, "latex_Document12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document12"):
                opp_val = getattr(value, "latex_Document12", None)
                setattr(value, "latex_Document12", self)

    @property
    def latex_Bibliography29(self):
        return self.__latex_Bibliography29

    @latex_Bibliography29.setter
    def latex_Bibliography29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Bibliography__latex_Bibliography29", None)
        self.__latex_Bibliography29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General30"):
                    opp_val = getattr(item, "latex_General30", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General30"):
                    opp_val = getattr(item, "latex_General30", None)
                    
                    setattr(item, "latex_General30", self)
                    

    @property
    def latex_Bibliography34(self):
        return self.__latex_Bibliography34

    @latex_Bibliography34.setter
    def latex_Bibliography34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Bibliography__latex_Bibliography34", None)
        self.__latex_Bibliography34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Beginbib"):
                opp_val = getattr(old_value, "latex_Beginbib", None)
                if opp_val == self:
                    setattr(old_value, "latex_Beginbib", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Beginbib"):
                opp_val = getattr(value, "latex_Beginbib", None)
                setattr(value, "latex_Beginbib", self)

class latex_Body:

    pass
class latex_Document:

    def __init__(self, documenttype: str, prefix: str, fontsize: str, papertype: str, latex_Document6: set["latex_Styles"] = None, latex_Document8: "latex_Abstracte" = None, latex_Document10: "latex_Body" = None, latex_Document: set["latex_Packages"] = None, latex_Document2: set["latex_Commands"] = None, latex_Document4: "latex_Title" = None, latex_Document12: "latex_Bibliography" = None, latex_Document14: "latex_Begin" = None, latex_Document16: "latex_End" = None):
        self.documenttype = documenttype
        self.prefix = prefix
        self.fontsize = fontsize
        self.papertype = papertype
        self.latex_Document6 = latex_Document6 if latex_Document6 is not None else set()
        self.latex_Document8 = latex_Document8
        self.latex_Document10 = latex_Document10
        self.latex_Document = latex_Document if latex_Document is not None else set()
        self.latex_Document2 = latex_Document2 if latex_Document2 is not None else set()
        self.latex_Document4 = latex_Document4
        self.latex_Document12 = latex_Document12
        self.latex_Document14 = latex_Document14
        self.latex_Document16 = latex_Document16
        
        pass
    @property
    def documenttype(self):
        return self.__documenttype

    @documenttype.setter
    def documenttype(self, documenttype: str):
        self.__documenttype = documenttype


    @property
    def fontsize(self):
        return self.__fontsize

    @fontsize.setter
    def fontsize(self, fontsize: str):
        self.__fontsize = fontsize


    @property
    def papertype(self):
        return self.__papertype

    @papertype.setter
    def papertype(self, papertype: str):
        self.__papertype = papertype


    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix


    @property
    def latex_Document8(self):
        return self.__latex_Document8

    @latex_Document8.setter
    def latex_Document8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document8", None)
        self.__latex_Document8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Abstracte"):
                opp_val = getattr(old_value, "latex_Abstracte", None)
                if opp_val == self:
                    setattr(old_value, "latex_Abstracte", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Abstracte"):
                opp_val = getattr(value, "latex_Abstracte", None)
                setattr(value, "latex_Abstracte", self)

    @property
    def latex_Document16(self):
        return self.__latex_Document16

    @latex_Document16.setter
    def latex_Document16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document16", None)
        self.__latex_Document16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_End"):
                opp_val = getattr(old_value, "latex_End", None)
                if opp_val == self:
                    setattr(old_value, "latex_End", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_End"):
                opp_val = getattr(value, "latex_End", None)
                setattr(value, "latex_End", self)

    @property
    def latex_Document2(self):
        return self.__latex_Document2

    @latex_Document2.setter
    def latex_Document2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document2", None)
        self.__latex_Document2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_Commands"):
                    opp_val = getattr(item, "latex_Commands", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_Commands", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_Commands"):
                    opp_val = getattr(item, "latex_Commands", None)
                    
                    setattr(item, "latex_Commands", self)
                    

    @property
    def latex_Document10(self):
        return self.__latex_Document10

    @latex_Document10.setter
    def latex_Document10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document10", None)
        self.__latex_Document10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Body"):
                opp_val = getattr(old_value, "latex_Body", None)
                if opp_val == self:
                    setattr(old_value, "latex_Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Body"):
                opp_val = getattr(value, "latex_Body", None)
                setattr(value, "latex_Body", self)

    @property
    def latex_Document12(self):
        return self.__latex_Document12

    @latex_Document12.setter
    def latex_Document12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document12", None)
        self.__latex_Document12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Bibliography"):
                opp_val = getattr(old_value, "latex_Bibliography", None)
                if opp_val == self:
                    setattr(old_value, "latex_Bibliography", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Bibliography"):
                opp_val = getattr(value, "latex_Bibliography", None)
                setattr(value, "latex_Bibliography", self)

    @property
    def latex_Document6(self):
        return self.__latex_Document6

    @latex_Document6.setter
    def latex_Document6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document6", None)
        self.__latex_Document6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_Styles"):
                    opp_val = getattr(item, "latex_Styles", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_Styles", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_Styles"):
                    opp_val = getattr(item, "latex_Styles", None)
                    
                    setattr(item, "latex_Styles", self)
                    

    @property
    def latex_Document4(self):
        return self.__latex_Document4

    @latex_Document4.setter
    def latex_Document4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document4", None)
        self.__latex_Document4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Title"):
                opp_val = getattr(old_value, "latex_Title", None)
                if opp_val == self:
                    setattr(old_value, "latex_Title", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Title"):
                opp_val = getattr(value, "latex_Title", None)
                setattr(value, "latex_Title", self)

    @property
    def latex_Document(self):
        return self.__latex_Document

    @latex_Document.setter
    def latex_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document", None)
        self.__latex_Document = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_Packages"):
                    opp_val = getattr(item, "latex_Packages", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_Packages", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_Packages"):
                    opp_val = getattr(item, "latex_Packages", None)
                    
                    setattr(item, "latex_Packages", self)
                    

    @property
    def latex_Document14(self):
        return self.__latex_Document14

    @latex_Document14.setter
    def latex_Document14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Document__latex_Document14", None)
        self.__latex_Document14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Begin"):
                opp_val = getattr(old_value, "latex_Begin", None)
                if opp_val == self:
                    setattr(old_value, "latex_Begin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Begin"):
                opp_val = getattr(value, "latex_Begin", None)
                setattr(value, "latex_Begin", self)

class latex_Abstracte:

    def __init__(self, abstracttext: str, abstractprefix: str, latex_Abstracte: "latex_Document" = None, latex_Abstracte20: set["latex_General"] = None):
        self.abstracttext = abstracttext
        self.abstractprefix = abstractprefix
        self.latex_Abstracte = latex_Abstracte
        self.latex_Abstracte20 = latex_Abstracte20 if latex_Abstracte20 is not None else set()
        
        pass
    @property
    def abstracttext(self):
        return self.__abstracttext

    @abstracttext.setter
    def abstracttext(self, abstracttext: str):
        self.__abstracttext = abstracttext


    @property
    def abstractprefix(self):
        return self.__abstractprefix

    @abstractprefix.setter
    def abstractprefix(self, abstractprefix: str):
        self.__abstractprefix = abstractprefix


    @property
    def latex_Abstracte20(self):
        return self.__latex_Abstracte20

    @latex_Abstracte20.setter
    def latex_Abstracte20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Abstracte__latex_Abstracte20", None)
        self.__latex_Abstracte20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "latex_General21"):
                    opp_val = getattr(item, "latex_General21", None)
                    
                    if opp_val == self:
                        setattr(item, "latex_General21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "latex_General21"):
                    opp_val = getattr(item, "latex_General21", None)
                    
                    setattr(item, "latex_General21", self)
                    

    @property
    def latex_Abstracte(self):
        return self.__latex_Abstracte

    @latex_Abstracte.setter
    def latex_Abstracte(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Abstracte__latex_Abstracte", None)
        self.__latex_Abstracte = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document8"):
                opp_val = getattr(old_value, "latex_Document8", None)
                if opp_val == self:
                    setattr(old_value, "latex_Document8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document8"):
                opp_val = getattr(value, "latex_Document8", None)
                setattr(value, "latex_Document8", self)

class latex_Styles:

    def __init__(self, styleprefix: str, stylesnames: str, stylenames: str, latex_Styles: "latex_Document" = None):
        self.styleprefix = styleprefix
        self.stylesnames = stylesnames
        self.stylenames = stylenames
        self.latex_Styles = latex_Styles
        
        pass
    @property
    def stylesnames(self):
        return self.__stylesnames

    @stylesnames.setter
    def stylesnames(self, stylesnames: str):
        self.__stylesnames = stylesnames


    @property
    def stylenames(self):
        return self.__stylenames

    @stylenames.setter
    def stylenames(self, stylenames: str):
        self.__stylenames = stylenames


    @property
    def styleprefix(self):
        return self.__styleprefix

    @styleprefix.setter
    def styleprefix(self, styleprefix: str):
        self.__styleprefix = styleprefix


    @property
    def latex_Styles(self):
        return self.__latex_Styles

    @latex_Styles.setter
    def latex_Styles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_latex_Styles__latex_Styles", None)
        self.__latex_Styles = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "latex_Document6"):
                opp_val = getattr(old_value, "latex_Document6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "latex_Document6"):
                opp_val = getattr(value, "latex_Document6", None)
                if opp_val is None:
                    setattr(value, "latex_Document6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
