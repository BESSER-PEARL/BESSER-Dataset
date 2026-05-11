





import java.util.List;
import java.util.ArrayList;

public class afpText_FNPRG  {

    private String UscoreWd;
    private String CapMHt;
    private String MaxAscHt;
    private String UscoreWdf;
    private String Reserved2;
    private String Reserved;
    private String UscorePos;
    private String Retired;
    private String Reserved3;
    private String LcHeight;
    private String MaxDesDp;





    private afpText_FNP afptext_fnp;


    public afpText_FNPRG(
        String UscoreWd,        String CapMHt,        String MaxAscHt,        String UscoreWdf,        String Reserved2,        String Reserved,        String UscorePos,        String Retired,        String Reserved3,        String LcHeight,        String MaxDesDp    ) {
        this.UscoreWd = UscoreWd;
        this.CapMHt = CapMHt;
        this.MaxAscHt = MaxAscHt;
        this.UscoreWdf = UscoreWdf;
        this.Reserved2 = Reserved2;
        this.Reserved = Reserved;
        this.UscorePos = UscorePos;
        this.Retired = Retired;
        this.Reserved3 = Reserved3;
        this.LcHeight = LcHeight;
        this.MaxDesDp = MaxDesDp;
    }


    public String getUscorewd() {
        return UscoreWd;
    }

    public void setUscorewd(String UscoreWd) {
        this.UscoreWd = UscoreWd;
    }
    public String getCapmht() {
        return CapMHt;
    }

    public void setCapmht(String CapMHt) {
        this.CapMHt = CapMHt;
    }
    public String getMaxascht() {
        return MaxAscHt;
    }

    public void setMaxascht(String MaxAscHt) {
        this.MaxAscHt = MaxAscHt;
    }
    public String getUscorewdf() {
        return UscoreWdf;
    }

    public void setUscorewdf(String UscoreWdf) {
        this.UscoreWdf = UscoreWdf;
    }
    public String getReserved2() {
        return Reserved2;
    }

    public void setReserved2(String Reserved2) {
        this.Reserved2 = Reserved2;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getUscorepos() {
        return UscorePos;
    }

    public void setUscorepos(String UscorePos) {
        this.UscorePos = UscorePos;
    }
    public String getRetired() {
        return Retired;
    }

    public void setRetired(String Retired) {
        this.Retired = Retired;
    }
    public String getReserved3() {
        return Reserved3;
    }

    public void setReserved3(String Reserved3) {
        this.Reserved3 = Reserved3;
    }
    public String getLcheight() {
        return LcHeight;
    }

    public void setLcheight(String LcHeight) {
        this.LcHeight = LcHeight;
    }
    public String getMaxdesdp() {
        return MaxDesDp;
    }

    public void setMaxdesdp(String MaxDesDp) {
        this.MaxDesDp = MaxDesDp;
    }

    public afpText_FNP getAfptext_fnp() {
        return afptext_fnp;
    }

    public void setAfptext_fnp(afpText_FNP afptext_fnp) {
        this.afptext_fnp = afptext_fnp;
    }

}