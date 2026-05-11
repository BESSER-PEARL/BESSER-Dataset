





import java.util.List;
import java.util.ArrayList;

public class featureModel_Model  {






    private List<featureModel_Feature> featuremodel_features;


    public featureModel_Model(
    ) {
        this.featuremodel_features = new ArrayList<>();
    }

    public featureModel_Model(
        ArrayList<featureModel_Feature> featuremodel_features    ) {
        this.featuremodel_features = featuremodel_features;
    }


    public List<featureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }

}