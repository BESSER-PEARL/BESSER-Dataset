





import java.util.List;
import java.util.ArrayList;

public class spinefm_ActionModel_Action  {

    private String type;
    private String id;





    private FeatureModel featuremodel;




    private Feature feature;


    public spinefm_ActionModel_Action(
        String type,        String id    ) {
        this.type = type;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public FeatureModel getFeaturemodel() {
        return featuremodel;
    }

    public void setFeaturemodel(FeatureModel featuremodel) {
        this.featuremodel = featuremodel;
    }
    public Feature getFeature() {
        return feature;
    }

    public void setFeature(Feature feature) {
        this.feature = feature;
    }

}