





import java.util.List;
import java.util.ArrayList;

public class MARTE_SAM_SaEndtoEndFlow  {

    private String schSlack;
    private String end2EndD;
    private String isSched;
    private String end2EndT;





    private SAM_MARTE_NamedElement sam_marte_namedelement;




    private List<GQAM_GaTimedObs> gqam_gatimedobss;


    public MARTE_SAM_SaEndtoEndFlow(
        String schSlack,        String end2EndD,        String isSched,        String end2EndT    ) {
        this.schSlack = schSlack;
        this.end2EndD = end2EndD;
        this.isSched = isSched;
        this.end2EndT = end2EndT;
        this.gqam_gatimedobss = new ArrayList<>();
    }

    public MARTE_SAM_SaEndtoEndFlow(
        String schSlack,        String end2EndD,        String isSched,        String end2EndT        ArrayList<GQAM_GaTimedObs> gqam_gatimedobss    ) {
        this.schSlack = schSlack;
        this.end2EndD = end2EndD;
        this.isSched = isSched;
        this.end2EndT = end2EndT;
        this.gqam_gatimedobss = gqam_gatimedobss;
    }

    public String getSchslack() {
        return schSlack;
    }

    public void setSchslack(String schSlack) {
        this.schSlack = schSlack;
    }
    public String getEnd2endd() {
        return end2EndD;
    }

    public void setEnd2endd(String end2EndD) {
        this.end2EndD = end2EndD;
    }
    public String getIssched() {
        return isSched;
    }

    public void setIssched(String isSched) {
        this.isSched = isSched;
    }
    public String getEnd2endt() {
        return end2EndT;
    }

    public void setEnd2endt(String end2EndT) {
        this.end2EndT = end2EndT;
    }

    public SAM_MARTE_NamedElement getSam_marte_namedelement() {
        return sam_marte_namedelement;
    }

    public void setSam_marte_namedelement(SAM_MARTE_NamedElement sam_marte_namedelement) {
        this.sam_marte_namedelement = sam_marte_namedelement;
    }
    public List<GQAM_GaTimedObs> getGqam_gatimedobss() {
        return gqam_gatimedobss;
    }

    public void addGqam_gatimedobs(Gqam_gatimedobs gqam_gatimedobs) {
        this.gqam_gatimedobss.add(gqam_gatimedobs);
    }

}