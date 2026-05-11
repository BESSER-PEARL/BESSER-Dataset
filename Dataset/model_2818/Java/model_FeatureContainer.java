





import java.util.List;
import java.util.ArrayList;

public class model_FeatureContainer  {






    private List<model_Feature> model_features;


    public model_FeatureContainer(
    ) {
        this.model_features = new ArrayList<>();
    }

    public model_FeatureContainer(
        ArrayList<model_Feature> model_features    ) {
        this.model_features = model_features;
    }


    public List<model_Feature> getModel_features() {
        return model_features;
    }

    public void addModel_feature(Model_feature model_feature) {
        this.model_features.add(model_feature);
    }

}