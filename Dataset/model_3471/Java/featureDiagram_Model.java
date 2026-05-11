





import java.util.List;
import java.util.ArrayList;

public class featureDiagram_Model  {

    private String name;





    private featureDiagram_Feature featurediagram_feature;


    public featureDiagram_Model(
        String name    ) {
        this.name = name;
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

}