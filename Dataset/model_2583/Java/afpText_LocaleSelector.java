





import java.util.List;
import java.util.ArrayList;

public class afpText_LocaleSelector extends triplet {

    private String VarCde;
    private String Reserved;
    private String LangCode;
    private String RegCde;
    private String LocFlgs;
    private String ScrptCde;



    public afpText_LocaleSelector(
        String VarCde,        String Reserved,        String LangCode,        String RegCde,        String LocFlgs,        String ScrptCde    ) {
        super(
        );
        this.VarCde = VarCde;
        this.Reserved = Reserved;
        this.LangCode = LangCode;
        this.RegCde = RegCde;
        this.LocFlgs = LocFlgs;
        this.ScrptCde = ScrptCde;
    }


    public String getVarcde() {
        return VarCde;
    }

    public void setVarcde(String VarCde) {
        this.VarCde = VarCde;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getLangcode() {
        return LangCode;
    }

    public void setLangcode(String LangCode) {
        this.LangCode = LangCode;
    }
    public String getRegcde() {
        return RegCde;
    }

    public void setRegcde(String RegCde) {
        this.RegCde = RegCde;
    }
    public String getLocflgs() {
        return LocFlgs;
    }

    public void setLocflgs(String LocFlgs) {
        this.LocFlgs = LocFlgs;
    }
    public String getScrptcde() {
        return ScrptCde;
    }

    public void setScrptcde(String ScrptCde) {
        this.ScrptCde = ScrptCde;
    }


}