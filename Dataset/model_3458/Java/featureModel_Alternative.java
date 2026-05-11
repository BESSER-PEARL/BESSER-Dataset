





import java.util.List;
import java.util.ArrayList;

public class featureModel_Alternative extends Feature {






    private List<featureModel_Feature> featuremodel_features;


    public featureModel_Alternative(
    ) {
        super(
        );
        this.featuremodel_features = new ArrayList<>();
    }

    public featureModel_Alternative(
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