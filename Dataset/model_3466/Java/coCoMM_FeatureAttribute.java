





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureAttribute  {

    private String name;





    private coCoMM_Feature cocomm_feature;


    public coCoMM_FeatureAttribute(
        String name    ) {
        this.name = name;
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

}