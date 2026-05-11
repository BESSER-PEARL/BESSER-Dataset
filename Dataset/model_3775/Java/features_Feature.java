





import java.util.List;
import java.util.ArrayList;

public class features_Feature  {

    private boolean abstract;
    private String short;
    private String name;





    private List<features_Feature> features_features;




    private features_Feature features_feature;




    private features_Feature features_feature;




    private features_Feature features_feature;




    private features_Model features_model;


    public features_Feature(
        boolean abstract,        String short,        String name    ) {
        this.abstract = abstract;
        this.short = short;
        this.name = name;
        this.features_features = new ArrayList<>();
    }

    public features_Feature(
        boolean abstract,        String short,        String name        ArrayList<features_Feature> features_features    ) {
        this.abstract = abstract;
        this.short = short;
        this.name = name;
        this.features_features = features_features;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getShort() {
        return short;
    }

    public void setShort(String short) {
        this.short = short;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<features_Feature> getFeatures_features() {
        return features_features;
    }

    public void addFeatures_feature(Features_feature features_feature) {
        this.features_features.add(features_feature);
    }
    public features_Feature getFeatures_feature() {
        return features_feature;
    }

    public void setFeatures_feature(features_Feature features_feature) {
        this.features_feature = features_feature;
    }
    public features_Feature getFeatures_feature() {
        return features_feature;
    }

    public void setFeatures_feature(features_Feature features_feature) {
        this.features_feature = features_feature;
    }
    public features_Feature getFeatures_feature() {
        return features_feature;
    }

    public void setFeatures_feature(features_Feature features_feature) {
        this.features_feature = features_feature;
    }
    public features_Model getFeatures_model() {
        return features_model;
    }

    public void setFeatures_model(features_Model features_model) {
        this.features_model = features_model;
    }

}