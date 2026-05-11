





import java.util.List;
import java.util.ArrayList;

public class feature_Feature  {

    private int maxCardinality;
    private int minCardinality;
    private String name;





    private feature_FeatureModel feature_featuremodel;


    public feature_Feature(
        int maxCardinality,        int minCardinality,        String name    ) {
        this.maxCardinality = maxCardinality;
        this.minCardinality = minCardinality;
        this.name = name;
    }


    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }
    public int getMincardinality() {
        return minCardinality;
    }

    public void setMincardinality(int minCardinality) {
        this.minCardinality = minCardinality;
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

}