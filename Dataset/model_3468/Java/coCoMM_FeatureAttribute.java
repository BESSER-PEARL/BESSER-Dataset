





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureAttribute  {

    private String minValue;
    private String defaultValue;
    private String maxValue;





    private coCoMM_Feature cocomm_feature;


    public coCoMM_FeatureAttribute(
        String minValue,        String defaultValue,        String maxValue    ) {
        this.minValue = minValue;
        this.defaultValue = defaultValue;
        this.maxValue = maxValue;
    }


    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }

    public coCoMM_Feature getCocomm_feature() {
        return cocomm_feature;
    }

    public void setCocomm_feature(coCoMM_Feature cocomm_feature) {
        this.cocomm_feature = cocomm_feature;
    }

}