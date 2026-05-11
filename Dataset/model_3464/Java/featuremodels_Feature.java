





import java.util.List;
import java.util.ArrayList;

public class featuremodels_Feature  {

    private int upperBound;
    private boolean root;
    private boolean required;
    private int lowerBound;
    private String name;





    private featuremodels_Feature featuremodels_feature;




    private List<featuremodels_Feature> featuremodels_features;


    public featuremodels_Feature(
        int upperBound,        boolean root,        boolean required,        int lowerBound,        String name    ) {
        this.upperBound = upperBound;
        this.root = root;
        this.required = required;
        this.lowerBound = lowerBound;
        this.name = name;
        this.featuremodels_features = new ArrayList<>();
    }

    public featuremodels_Feature(
        int upperBound,        boolean root,        boolean required,        int lowerBound,        String name        ArrayList<featuremodels_Feature> featuremodels_features    ) {
        this.upperBound = upperBound;
        this.root = root;
        this.required = required;
        this.lowerBound = lowerBound;
        this.name = name;
        this.featuremodels_features = featuremodels_features;
    }

    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getRoot() {
        return root;
    }

    public void setRoot(boolean root) {
        this.root = root;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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