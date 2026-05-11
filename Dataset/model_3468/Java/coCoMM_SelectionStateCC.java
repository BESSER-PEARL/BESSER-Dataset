





import java.util.List;
import java.util.ArrayList;

public class coCoMM_SelectionStateCC extends ConfigurationConstraint {

    private String state;





    private coCoMM_Feature cocomm_feature;




    private coCoMM_FeatureModel cocomm_featuremodel;


    public coCoMM_SelectionStateCC(
        String state    ) {
        super(
        );
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public coCoMM_Feature getCocomm_feature() {
        return cocomm_feature;
    }

    public void setCocomm_feature(coCoMM_Feature cocomm_feature) {
        this.cocomm_feature = cocomm_feature;
    }
    public coCoMM_FeatureModel getCocomm_featuremodel() {
        return cocomm_featuremodel;
    }

    public void setCocomm_featuremodel(coCoMM_FeatureModel cocomm_featuremodel) {
        this.cocomm_featuremodel = cocomm_featuremodel;
    }

}