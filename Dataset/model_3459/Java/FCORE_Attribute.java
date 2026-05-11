





import java.util.List;
import java.util.ArrayList;

public class FCORE_Attribute  {

    private String name;
    private int max;
    private int value;
    private int min;





    private FCORE_Feature fcore_feature;




    private FCORE_FeatureModel fcore_featuremodel;


    public FCORE_Attribute(
        String name,        int max,        int value,        int min    ) {
        this.name = name;
        this.max = max;
        this.value = value;
        this.min = min;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public FCORE_Feature getFcore_feature() {
        return fcore_feature;
    }

    public void setFcore_feature(FCORE_Feature fcore_feature) {
        this.fcore_feature = fcore_feature;
    }
    public FCORE_FeatureModel getFcore_featuremodel() {
        return fcore_featuremodel;
    }

    public void setFcore_featuremodel(FCORE_FeatureModel fcore_featuremodel) {
        this.fcore_featuremodel = fcore_featuremodel;
    }

}