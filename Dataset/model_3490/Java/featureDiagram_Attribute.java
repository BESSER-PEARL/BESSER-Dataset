





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Attribute extends FeatureElement {

    private String type;
    private String name;
    private String value;





    private featureDiagram_Feature featurediagram_feature;




    private featureDiagram_Feature featurediagram_feature;


    public featureDiagram_Attribute(
        String type,        String name,        String value    ) {
        super(
        );
        this.type = type;
        this.name = name;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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

}