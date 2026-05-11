





import java.util.List;
import java.util.ArrayList;

public class afmmm_Relation  {






    private List<afmmm_Feature> afmmm_features;




    private afmmm_Feature afmmm_feature;




    private afmmm_AttributedFeatureDiagram afmmm_attributedfeaturediagram;


    public afmmm_Relation(
    ) {
        this.afmmm_features = new ArrayList<>();
    }

    public afmmm_Relation(
        ArrayList<afmmm_Feature> afmmm_features    ) {
        this.afmmm_features = afmmm_features;
    }


    public List<afmmm_Feature> getAfmmm_features() {
        return afmmm_features;
    }

    public void addAfmmm_feature(Afmmm_feature afmmm_feature) {
        this.afmmm_features.add(afmmm_feature);
    }
    public afmmm_Feature getAfmmm_feature() {
        return afmmm_feature;
    }

    public void setAfmmm_feature(afmmm_Feature afmmm_feature) {
        this.afmmm_feature = afmmm_feature;
    }
    public afmmm_AttributedFeatureDiagram getAfmmm_attributedfeaturediagram() {
        return afmmm_attributedfeaturediagram;
    }

    public void setAfmmm_attributedfeaturediagram(afmmm_AttributedFeatureDiagram afmmm_attributedfeaturediagram) {
        this.afmmm_attributedfeaturediagram = afmmm_attributedfeaturediagram;
    }

}