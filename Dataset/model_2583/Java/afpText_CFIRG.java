





import java.util.List;
import java.util.ArrayList;

public class afpText_CFIRG  {

    private String Reserved;
    private String SVSize;
    private String CPName;
    private String SHScale;
    private String FCSName;
    private String Section;





    private afpText_CFI afptext_cfi;


    public afpText_CFIRG(
        String Reserved,        String SVSize,        String CPName,        String SHScale,        String FCSName,        String Section    ) {
        this.Reserved = Reserved;
        this.SVSize = SVSize;
        this.CPName = CPName;
        this.SHScale = SHScale;
        this.FCSName = FCSName;
        this.Section = Section;
    }


    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getSvsize() {
        return SVSize;
    }

    public void setSvsize(String SVSize) {
        this.SVSize = SVSize;
    }
    public String getCpname() {
        return CPName;
    }

    public void setCpname(String CPName) {
        this.CPName = CPName;
    }
    public String getShscale() {
        return SHScale;
    }

    public void setShscale(String SHScale) {
        this.SHScale = SHScale;
    }
    public String getFcsname() {
        return FCSName;
    }

    public void setFcsname(String FCSName) {
        this.FCSName = FCSName;
    }
    public String getSection() {
        return Section;
    }

    public void setSection(String Section) {
        this.Section = Section;
    }

    public afpText_CFI getAfptext_cfi() {
        return afptext_cfi;
    }

    public void setAfptext_cfi(afpText_CFI afptext_cfi) {
        this.afptext_cfi = afptext_cfi;
    }

}