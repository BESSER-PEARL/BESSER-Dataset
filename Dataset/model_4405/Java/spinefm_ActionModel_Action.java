





import java.util.List;
import java.util.ArrayList;

public class spinefm_ActionModel_Action  {

    private String id;





    private Feature feature;




    private FeatureModel featuremodel;


    public spinefm_ActionModel_Action(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Feature getFeature() {
        return feature;
    }

    public void setFeature(Feature feature) {
        this.feature = feature;
    }
    public FeatureModel getFeaturemodel() {
        return featuremodel;
    }

    public void setFeaturemodel(FeatureModel featuremodel) {
        this.featuremodel = featuremodel;
    }

}