





import java.util.List;
import java.util.ArrayList;

public class myDsl_FeatureAttribute  {

    private int maxValue;
    private int nullValue;
    private int defaultValue;
    private int minValue;
    private String attributeType;





    private myDsl_Feature mydsl_feature;


    public myDsl_FeatureAttribute(
        int maxValue,        int nullValue,        int defaultValue,        int minValue,        String attributeType    ) {
        this.maxValue = maxValue;
        this.nullValue = nullValue;
        this.defaultValue = defaultValue;
        this.minValue = minValue;
        this.attributeType = attributeType;
    }


    public int getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(int maxValue) {
        this.maxValue = maxValue;
    }
    public int getNullvalue() {
        return nullValue;
    }

    public void setNullvalue(int nullValue) {
        this.nullValue = nullValue;
    }
    public int getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(int defaultValue) {
        this.defaultValue = defaultValue;
    }
    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public String getAttributetype() {
        return attributeType;
    }

    public void setAttributetype(String attributeType) {
        this.attributeType = attributeType;
    }

    public myDsl_Feature getMydsl_feature() {
        return mydsl_feature;
    }

    public void setMydsl_feature(myDsl_Feature mydsl_feature) {
        this.mydsl_feature = mydsl_feature;
    }

}