





import java.util.List;
import java.util.ArrayList;

public class FeatureModel_FeatureConstraint extends Constraint {

    private String type;





    private FeatureModel_FeatureModel featuremodel_featuremodel;


    public FeatureModel_FeatureConstraint(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public FeatureModel_FeatureModel getFeaturemodel_featuremodel() {
        return featuremodel_featuremodel;
    }

    public void setFeaturemodel_featuremodel(FeatureModel_FeatureModel featuremodel_featuremodel) {
        this.featuremodel_featuremodel = featuremodel_featuremodel;
    }

}