





import java.util.List;
import java.util.ArrayList;

public class feature_Group extends Identifiable {

    private int minCardinality;
    private int maxCardinality;





    private feature_Feature feature_feature;




    private feature_Feature feature_feature;




    private feature_Feature feature_feature;




    private List<feature_Feature> feature_features;


    public feature_Group(
        int minCardinality,        int maxCardinality    ) {
        super(
        );
        this.minCardinality = minCardinality;
        this.maxCardinality = maxCardinality;
        this.feature_features = new ArrayList<>();
    }

    public feature_Group(
        int minCardinality,        int maxCardinality        ArrayList<feature_Feature> feature_features    ) {
        this.minCardinality = minCardinality;
        this.maxCardinality = maxCardinality;
        this.feature_features = feature_features;
    }

    public int getMincardinality() {
        return minCardinality;
    }

    public void setMincardinality(int minCardinality) {
        this.minCardinality = minCardinality;
    }
    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }

    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }
    public feature_Feature getFeature_feature() {
        return feature_feature;
    }

    public void setFeature_feature(feature_Feature feature_feature) {
        this.feature_feature = feature_feature;
    }
    public List<feature_Feature> getFeature_features() {
        return feature_features;
    }

    public void addFeature_feature(Feature_feature feature_feature) {
        this.feature_features.add(feature_feature);
    }

}