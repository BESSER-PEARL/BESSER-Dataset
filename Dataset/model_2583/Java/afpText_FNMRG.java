





import java.util.List;
import java.util.ArrayList;

public class afpText_FNMRG  {

    private String PatDOset;
    private String CharBoxHt;
    private String CharBoxWd;





    private afpText_FNM afptext_fnm;


    public afpText_FNMRG(
        String PatDOset,        String CharBoxHt,        String CharBoxWd    ) {
        this.PatDOset = PatDOset;
        this.CharBoxHt = CharBoxHt;
        this.CharBoxWd = CharBoxWd;
    }


    public String getPatdoset() {
        return PatDOset;
    }

    public void setPatdoset(String PatDOset) {
        this.PatDOset = PatDOset;
    }
    public String getCharboxht() {
        return CharBoxHt;
    }

    public void setCharboxht(String CharBoxHt) {
        this.CharBoxHt = CharBoxHt;
    }
    public String getCharboxwd() {
        return CharBoxWd;
    }

    public void setCharboxwd(String CharBoxWd) {
        this.CharBoxWd = CharBoxWd;
    }

    public afpText_FNM getAfptext_fnm() {
        return afptext_fnm;
    }

    public void setAfptext_fnm(afpText_FNM afptext_fnm) {
        this.afptext_fnm = afptext_fnm;
    }

}