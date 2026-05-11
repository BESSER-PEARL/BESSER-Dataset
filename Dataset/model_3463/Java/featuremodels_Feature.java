





import java.util.List;
import java.util.ArrayList;

public class featuremodels_Feature  {

    private int lowerBound;
    private String name;
    private int upperBound;
    private boolean root;
    private boolean required;





    private featuremodels_Feature featuremodels_feature;




    private featuremodels_Feature featuremodels_feature;


    public featuremodels_Feature(
        int lowerBound,        String name,        int upperBound,        boolean root,        boolean required    ) {
        this.lowerBound = lowerBound;
        this.name = name;
        this.upperBound = upperBound;
        this.root = root;
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

}