





import java.util.List;
import java.util.ArrayList;

public class featuremodel_Constraint extends Rule {

    private String id;





    private featuremodel_FeatureModel featuremodel_featuremodel;




    private featuremodel_Description featuremodel_description;


    public featuremodel_Constraint(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public featuremodel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(featuremodel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }
    public featuremodel_Description getFeaturemodel_description() {
        return featuremodel_description;
    }

    public void setFeaturemodel_description(featuremodel_Description featuremodel_description) {
        this.featuremodel_description = featuremodel_description;
    }

}