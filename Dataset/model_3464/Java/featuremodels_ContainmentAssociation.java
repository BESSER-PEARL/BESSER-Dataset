





import java.util.List;
import java.util.ArrayList;

public class featuremodels_ContainmentAssociation  {

    private int lowerBound;
    private int upperBound;





    private featuremodels_Feature featuremodels_feature;




    private featuremodels_Feature featuremodels_feature;




    private featuremodels_Feature featuremodels_feature;




    private List<featuremodels_Feature> featuremodels_features;


    public featuremodels_ContainmentAssociation(
        int lowerBound,        int upperBound    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.featuremodels_features = new ArrayList<>();
    }

    public featuremodels_ContainmentAssociation(
        int lowerBound,        int upperBound        ArrayList<featuremodels_Feature> featuremodels_features    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.featuremodels_features = featuremodels_features;
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

    public featuremodels_Feature getFeaturemodels_feature() {
        return featuremodels_feature;
    }

    public void setFeaturemodels_feature(featuremodels_Feature featuremodels_feature) {
        this.featuremodels_feature = featuremodels_feature;
    }
    public featuremodels_Feature getFeaturemodels_feature() {
        return featuremodels_feature;
    }

    public void setFeaturemodels_feature(featuremodels_Feature featuremodels_feature) {
        this.featuremodels_feature = featuremodels_feature;
    }
    public featuremodels_Feature getFeaturemodels_feature() {
        return featuremodels_feature;
    }

    public void setFeaturemodels_feature(featuremodels_Feature featuremodels_feature) {
        this.featuremodels_feature = featuremodels_feature;
    }
    public List<featuremodels_Feature> getFeaturemodels_features() {
        return featuremodels_features;
    }

    public void addFeaturemodels_feature(Featuremodels_feature featuremodels_feature) {
        this.featuremodels_features.add(featuremodels_feature);
    }

}