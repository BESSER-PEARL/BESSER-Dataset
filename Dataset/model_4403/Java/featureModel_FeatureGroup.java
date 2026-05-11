





import java.util.List;
import java.util.ArrayList;

public class featureModel_FeatureGroup extends Node {

    private String type;
    private int lowerBound;
    private int upperBound;





    private List<featureModel_Feature> featuremodel_features;


    public featureModel_FeatureGroup(
        String type,        int lowerBound,        int upperBound    ) {
        super(
        );
        this.type = type;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.featuremodel_features = new ArrayList<>();
    }

    public featureModel_FeatureGroup(
        String type,        int lowerBound,        int upperBound        ArrayList<featureModel_Feature> featuremodel_features    ) {
        this.type = type;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.featuremodel_features = featuremodel_features;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public List<featureModel_Feature> getFeaturemodel_features() {
        return featuremodel_features;
    }

    public void addFeaturemodel_feature(Featuremodel_feature featuremodel_feature) {
        this.featuremodel_features.add(featuremodel_feature);
    }

}