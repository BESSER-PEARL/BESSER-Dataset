





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureAttribute  {

    private String name;





    private coCoMM_Feature cocomm_feature;




    private List<coCoMM_FeatureAttributeElement> cocomm_featureattributeelements;


    public coCoMM_FeatureAttribute(
        String name    ) {
        this.name = name;
        this.cocomm_featureattributeelements = new ArrayList<>();
    }

    public coCoMM_FeatureAttribute(
        String name        ArrayList<coCoMM_FeatureAttributeElement> cocomm_featureattributeelements    ) {
        this.name = name;
        this.cocomm_featureattributeelements = cocomm_featureattributeelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public coCoMM_Feature getCocomm_feature() {
        return cocomm_feature;
    }

    public void setCocomm_feature(coCoMM_Feature cocomm_feature) {
        this.cocomm_feature = cocomm_feature;
    }
    public List<coCoMM_FeatureAttributeElement> getCocomm_featureattributeelements() {
        return cocomm_featureattributeelements;
    }

    public void addCocomm_featureattributeelement(Cocomm_featureattributeelement cocomm_featureattributeelement) {
        this.cocomm_featureattributeelements.add(cocomm_featureattributeelement);
    }

}