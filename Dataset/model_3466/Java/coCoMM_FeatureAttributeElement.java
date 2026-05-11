





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureAttributeElement  {

    private String value;





    private coCoMM_FeatureAttribute cocomm_featureattribute;


    public coCoMM_FeatureAttributeElement(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public coCoMM_FeatureAttribute getCocomm_featureattribute() {
        return cocomm_featureattribute;
    }

    public void setCocomm_featureattribute(coCoMM_FeatureAttribute cocomm_featureattribute) {
        this.cocomm_featureattribute = cocomm_featureattribute;
    }

}