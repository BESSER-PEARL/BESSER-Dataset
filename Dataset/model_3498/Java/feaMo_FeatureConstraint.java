





import java.util.List;
import java.util.ArrayList;

public class feaMo_FeatureConstraint  {

    private String rel;





    private feaMo_FeatureModel feamo_featuremodel;


    public feaMo_FeatureConstraint(
        String rel    ) {
        this.rel = rel;
    }


    public String getRel() {
        return rel;
    }

    public void setRel(String rel) {
        this.rel = rel;
    }

    public feaMo_FeatureModel getFeamo_featuremodel() {
        return feamo_featuremodel;
    }

    public void setFeamo_featuremodel(feaMo_FeatureModel feamo_featuremodel) {
        this.feamo_featuremodel = feamo_featuremodel;
    }

}