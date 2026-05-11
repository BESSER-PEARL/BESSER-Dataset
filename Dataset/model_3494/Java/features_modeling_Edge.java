





import java.util.List;
import java.util.ArrayList;

public class features_modeling_Edge  {






    private List<features_modeling_Feature> features_modeling_features;


    public features_modeling_Edge(
    ) {
        this.features_modeling_features = new ArrayList<>();
    }

    public features_modeling_Edge(
        ArrayList<features_modeling_Feature> features_modeling_features    ) {
        this.features_modeling_features = features_modeling_features;
    }


    public List<features_modeling_Feature> getFeatures_modeling_features() {
        return features_modeling_features;
    }

    public void addFeatures_modeling_feature(Features_modeling_feature features_modeling_feature) {
        this.features_modeling_features.add(features_modeling_feature);
    }

}