





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Operator extends FeatureElement {

    private String name;





    private featureDiagram_Feature featurediagram_feature;




    private featureDiagram_Feature featurediagram_feature;




    private List<featureDiagram_Feature> featurediagram_features;




    private featureDiagram_Feature featurediagram_feature;


    public featureDiagram_Operator(
        String name    ) {
        super(
        );
        this.name = name;
        this.featurediagram_features = new ArrayList<>();
    }

    public featureDiagram_Operator(
        String name        ArrayList<featureDiagram_Feature> featurediagram_features    ) {
        this.name = name;
        this.featurediagram_features = featurediagram_features;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public featureDiagram_Feature getFeaturediagram_feature() {
        return featurediagram_feature;
    }

    public void setFeaturediagram_feature(featureDiagram_Feature featurediagram_feature) {
        this.featurediagram_feature = featurediagram_feature;
    }
    public featureDiagram_Feature getFeaturediagram_feature() {
        return featurediagram_feature;
    }

    public void setFeaturediagram_feature(featureDiagram_Feature featurediagram_feature) {
        this.featurediagram_feature = featurediagram_feature;
    }
    public List<featureDiagram_Feature> getFeaturediagram_features() {
        return featurediagram_features;
    }

    public void addFeaturediagram_feature(Featurediagram_feature featurediagram_feature) {
        this.featurediagram_features.add(featurediagram_feature);
    }
    public featureDiagram_Feature getFeaturediagram_feature() {
        return featurediagram_feature;
    }

    public void setFeaturediagram_feature(featureDiagram_Feature featurediagram_feature) {
        this.featurediagram_feature = featurediagram_feature;
    }

}