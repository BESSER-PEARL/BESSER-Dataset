





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_Resource  {

    private String isProtected;





    private GRM_MARTE_Lifeline grm_marte_lifeline;




    private GRM_MARTE_Classifier grm_marte_classifier;




    private GRM_MARTE_ConnectableElement grm_marte_connectableelement;


    public MARTE_GRM_Resource(
        String isProtected    ) {
        this.isProtected = isProtected;
    }


    public String getIsprotected() {
        return isProtected;
    }

    public void setIsprotected(String isProtected) {
        this.isProtected = isProtected;
    }

    public GRM_MARTE_Lifeline getGrm_marte_lifeline() {
        return grm_marte_lifeline;
    }

    public void setGrm_marte_lifeline(GRM_MARTE_Lifeline grm_marte_lifeline) {
        this.grm_marte_lifeline = grm_marte_lifeline;
    }
    public GRM_MARTE_Classifier getGrm_marte_classifier() {
        return grm_marte_classifier;
    }

    public void setGrm_marte_classifier(GRM_MARTE_Classifier grm_marte_classifier) {
        this.grm_marte_classifier = grm_marte_classifier;
    }
    public GRM_MARTE_ConnectableElement getGrm_marte_connectableelement() {
        return grm_marte_connectableelement;
    }

    public void setGrm_marte_connectableelement(GRM_MARTE_ConnectableElement grm_marte_connectableelement) {
        this.grm_marte_connectableelement = grm_marte_connectableelement;
    }

}