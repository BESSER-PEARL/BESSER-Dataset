





import java.util.List;
import java.util.ArrayList;

public class afpText_MCF1RG  {

    private String CharRot;
    private String CFLid;
    private String CFName;
    private String CPName;
    private String Sectid;
    private String FCSName;





    private afpText_MCF1 afptext_mcf1;


    public afpText_MCF1RG(
        String CharRot,        String CFLid,        String CFName,        String CPName,        String Sectid,        String FCSName    ) {
        this.CharRot = CharRot;
        this.CFLid = CFLid;
        this.CFName = CFName;
        this.CPName = CPName;
        this.Sectid = Sectid;
        this.FCSName = FCSName;
    }


    public String getCharrot() {
        return CharRot;
    }

    public void setCharrot(String CharRot) {
        this.CharRot = CharRot;
    }
    public String getCflid() {
        return CFLid;
    }

    public void setCflid(String CFLid) {
        this.CFLid = CFLid;
    }
    public String getCfname() {
        return CFName;
    }

    public void setCfname(String CFName) {
        this.CFName = CFName;
    }
    public String getCpname() {
        return CPName;
    }

    public void setCpname(String CPName) {
        this.CPName = CPName;
    }
    public String getSectid() {
        return Sectid;
    }

    public void setSectid(String Sectid) {
        this.Sectid = Sectid;
    }
    public String getFcsname() {
        return FCSName;
    }

    public void setFcsname(String FCSName) {
        this.FCSName = FCSName;
    }

    public afpText_MCF1 getAfptext_mcf1() {
        return afptext_mcf1;
    }

    public void setAfptext_mcf1(afpText_MCF1 afptext_mcf1) {
        this.afptext_mcf1 = afptext_mcf1;
    }

}