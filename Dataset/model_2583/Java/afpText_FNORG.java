





import java.util.List;
import java.util.ArrayList;

public class afpText_FNORG  {

    private String Reserved3;
    private String MaxCharInc;
    private String EmSpInc;
    private String Reserved2;
    private String DefBInc;
    private String OrntFlgs;
    private String MaxBExt;
    private String FigSpInc;
    private String NomCharInc;
    private String CharRot;
    private String MinASp;
    private String MaxBOset;
    private String Reserved;
    private String SpCharInc;





    private afpText_FNO afptext_fno;


    public afpText_FNORG(
        String Reserved3,        String MaxCharInc,        String EmSpInc,        String Reserved2,        String DefBInc,        String OrntFlgs,        String MaxBExt,        String FigSpInc,        String NomCharInc,        String CharRot,        String MinASp,        String MaxBOset,        String Reserved,        String SpCharInc    ) {
        this.Reserved3 = Reserved3;
        this.MaxCharInc = MaxCharInc;
        this.EmSpInc = EmSpInc;
        this.Reserved2 = Reserved2;
        this.DefBInc = DefBInc;
        this.OrntFlgs = OrntFlgs;
        this.MaxBExt = MaxBExt;
        this.FigSpInc = FigSpInc;
        this.NomCharInc = NomCharInc;
        this.CharRot = CharRot;
        this.MinASp = MinASp;
        this.MaxBOset = MaxBOset;
        this.Reserved = Reserved;
        this.SpCharInc = SpCharInc;
    }


    public String getReserved3() {
        return Reserved3;
    }

    public void setReserved3(String Reserved3) {
        this.Reserved3 = Reserved3;
    }
    public String getMaxcharinc() {
        return MaxCharInc;
    }

    public void setMaxcharinc(String MaxCharInc) {
        this.MaxCharInc = MaxCharInc;
    }
    public String getEmspinc() {
        return EmSpInc;
    }

    public void setEmspinc(String EmSpInc) {
        this.EmSpInc = EmSpInc;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }
    public String getDefbinc() {
        return DefBInc;
    }

    public void setDefbinc(String DefBInc) {
        this.DefBInc = DefBInc;
    }
    public String getOrntflgs() {
        return OrntFlgs;
    }

    public void setOrntflgs(String OrntFlgs) {
        this.OrntFlgs = OrntFlgs;
    }
    public String getMaxbext() {
        return MaxBExt;
    }

    public void setMaxbext(String MaxBExt) {
        this.MaxBExt = MaxBExt;
    }
    public String getFigspinc() {
        return FigSpInc;
    }

    public void setFigspinc(String FigSpInc) {
        this.FigSpInc = FigSpInc;
    }
    public String getNomcharinc() {
        return NomCharInc;
    }

    public void setNomcharinc(String NomCharInc) {
        this.NomCharInc = NomCharInc;
    }
    public String getCharrot() {
        return CharRot;
    }

    public void setCharrot(String CharRot) {
        this.CharRot = CharRot;
    }
    public String getMinasp() {
        return MinASp;
    }

    public void setMinasp(String MinASp) {
        this.MinASp = MinASp;
    }
    public String getMaxboset() {
        return MaxBOset;
    }

    public void setMaxboset(String MaxBOset) {
        this.MaxBOset = MaxBOset;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getSpcharinc() {
        return SpCharInc;
    }

    public void setSpcharinc(String SpCharInc) {
        this.SpCharInc = SpCharInc;
    }

    public afpText_FNO getAfptext_fno() {
        return afptext_fno;
    }

    public void setAfptext_fno(afpText_FNO afptext_fno) {
        this.afptext_fno = afptext_fno;
    }

}