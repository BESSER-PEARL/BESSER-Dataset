





import java.util.List;
import java.util.ArrayList;

public class features_FeatureSet extends FeatureSetDescriptor {

    private String name;
    private String description;
    private String identifier;





    private features_Feature features_feature;




    private List<features_Feature> features_features;


    public features_FeatureSet(
        String name,        String description,        String identifier    ) {
        super(
        );
        this.name = name;
        this.description = description;
        this.identifier = identifier;
        this.features_features = new ArrayList<>();
    }

    public features_FeatureSet(
        String name,        String description,        String identifier        ArrayList<features_Feature> features_features    ) {
        this.name = name;
        this.description = description;
        this.identifier = identifier;
        this.features_features = features_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public features_Feature getFeatures_feature() {
        return features_feature;
    }

    public void setFeatures_feature(features_Feature features_feature) {
        this.features_feature = features_feature;
    }
    public List<features_Feature> getFeatures_features() {
        return features_features;
    }

    public void addFeatures_feature(Features_feature features_feature) {
        this.features_features.add(features_feature);
    }

}