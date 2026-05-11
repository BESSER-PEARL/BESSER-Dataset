





import java.util.List;
import java.util.ArrayList;

public class sxfm_FeatureChoice  {

    private int decisionStep;
    private String decisionType;
    private boolean selected;





    private sxfm_Feature sxfm_feature;




    private sxfm_FeatureModelConfiguaration sxfm_featuremodelconfiguaration;


    public sxfm_FeatureChoice(
        int decisionStep,        String decisionType,        boolean selected    ) {
        this.decisionStep = decisionStep;
        this.decisionType = decisionType;
        this.selected = selected;
    }


    public int getDecisionstep() {
        return decisionStep;
    }

    public void setDecisionstep(int decisionStep) {
        this.decisionStep = decisionStep;
    }
    public String getDecisiontype() {
        return decisionType;
    }

    public void setDecisiontype(String decisionType) {
        this.decisionType = decisionType;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public sxfm_Feature getSxfm_feature() {
        return sxfm_feature;
    }

    public void setSxfm_feature(sxfm_Feature sxfm_feature) {
        this.sxfm_feature = sxfm_feature;
    }
    public sxfm_FeatureModelConfiguaration getSxfm_featuremodelconfiguaration() {
        return sxfm_featuremodelconfiguaration;
    }

    public void setSxfm_featuremodelconfiguaration(sxfm_FeatureModelConfiguaration sxfm_featuremodelconfiguaration) {
        this.sxfm_featuremodelconfiguaration = sxfm_featuremodelconfiguaration;
    }

}