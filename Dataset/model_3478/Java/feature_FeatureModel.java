





import java.util.List;
import java.util.ArrayList;

public class feature_FeatureModel  {

    private String name;





    private List<feature_FeatureModel> feature_featuremodels;




    private feature_FeatureModel feature_featuremodel;


    public feature_FeatureModel(
        String name    ) {
        this.name = name;
        this.feature_featuremodels = new ArrayList<>();
    }

    public feature_FeatureModel(
        String name        ArrayList<feature_FeatureModel> feature_featuremodels    ) {
        this.name = name;
        this.feature_featuremodels = feature_featuremodels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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