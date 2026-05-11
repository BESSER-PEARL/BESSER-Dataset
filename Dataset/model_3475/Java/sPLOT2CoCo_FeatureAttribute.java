





import java.util.List;
import java.util.ArrayList;

public class sPLOT2CoCo_FeatureAttribute  {

    private String attributeType;
    private int minValue;
    private int defaultValue;
    private int maxValue;
    private int nullValue;





    private sPLOT2CoCo_Feature splot2coco_feature;




    private sPLOT2CoCo_FM splot2coco_fm;


    public sPLOT2CoCo_FeatureAttribute(
        String attributeType,        int minValue,        int defaultValue,        int maxValue,        int nullValue    ) {
        this.attributeType = attributeType;
        this.minValue = minValue;
        this.defaultValue = defaultValue;
        this.maxValue = maxValue;
        this.nullValue = nullValue;
    }


    public String getAttributetype() {
        return attributeType;
    }

    public void setAttributetype(String attributeType) {
        this.attributeType = attributeType;
    }
    public int getMinvalue() {
        return minValue;
    }

    public void setMinvalue(int minValue) {
        this.minValue = minValue;
    }
    public int getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(int defaultValue) {
        this.defaultValue = defaultValue;
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

    public sPLOT2CoCo_Feature getSplot2coco_feature() {
        return splot2coco_feature;
    }

    public void setSplot2coco_feature(sPLOT2CoCo_Feature splot2coco_feature) {
        this.splot2coco_feature = splot2coco_feature;
    }
    public sPLOT2CoCo_FM getSplot2coco_fm() {
        return splot2coco_fm;
    }

    public void setSplot2coco_fm(sPLOT2CoCo_FM splot2coco_fm) {
        this.splot2coco_fm = splot2coco_fm;
    }

}