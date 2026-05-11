





import java.util.List;
import java.util.ArrayList;

public class feature_FeatureModel  {

    private String name;





    private feature_FeatureModel feature_featuremodel;




    private List<feature_Constraint> feature_constraints;




    private feature_Feature feature_feature;




    private List<feature_FeatureModel> feature_featuremodels;




    private feature_FeatureModel feature_featuremodel;


    public feature_FeatureModel(
        String name    ) {
        this.name = name;
        this.feature_constraints = new ArrayList<>();
        this.feature_featuremodels = new ArrayList<>();
    }

    public feature_FeatureModel(
        String name        ArrayList<feature_Constraint> feature_constraints,        ArrayList<feature_FeatureModel> feature_featuremodels    ) {
        this.name = name;
        this.feature_constraints = feature_constraints;
        this.feature_featuremodels = feature_featuremodels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }
    public List<feature_Constraint> getFeature_constraints() {
        return feature_constraints;
    }

    public void addFeature_constraint(Feature_constraint feature_constraint) {
        this.feature_constraints.add(feature_constraint);
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }
    public List<feature_FeatureModel> getFeature_featuremodels() {
        return feature_featuremodels;
    }

    public void addFeature_featuremodel(Feature_featuremodel feature_featuremodel) {
        this.feature_featuremodels.add(feature_featuremodel);
    }
    public feature_FeatureModel getFeature_featuremodel() {
        return feature_featuremodel;
    }

    public void setFeature_featuremodel(feature_FeatureModel feature_featuremodel) {
        this.feature_featuremodel = feature_featuremodel;
    }

}