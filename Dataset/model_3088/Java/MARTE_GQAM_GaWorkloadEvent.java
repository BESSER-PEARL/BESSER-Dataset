





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaWorkloadEvent  {

    private String pattern;





    private GQAM_MARTE_NamedElement gqam_marte_namedelement;


    public MARTE_GQAM_GaWorkloadEvent(
        String pattern    ) {
        this.pattern = pattern;
    }


    public String getPattern() {
        return pattern;
    }

    public void setPattern(String pattern) {
        this.pattern = pattern;
    }

    public GQAM_MARTE_NamedElement getGqam_marte_namedelement() {
        return gqam_marte_namedelement;
    }

    public void setGqam_marte_namedelement(GQAM_MARTE_NamedElement gqam_marte_namedelement) {
        this.gqam_marte_namedelement = gqam_marte_namedelement;
    }

}