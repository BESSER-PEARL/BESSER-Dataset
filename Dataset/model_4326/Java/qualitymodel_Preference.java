





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_Preference  {

    private float weight;
    private float threshold;





    private qualitymodel_Attribute qualitymodel_attribute;


    public qualitymodel_Preference(
        float weight,        float threshold    ) {
        this.weight = weight;
        this.threshold = threshold;
    }


    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public float getThreshold() {
        return threshold;
    }

    public void setThreshold(float threshold) {
        this.threshold = threshold;
    }

    public qualitymodel_Attribute getQualitymodel_attribute() {
        return qualitymodel_attribute;
    }

    public void setQualitymodel_attribute(qualitymodel_Attribute qualitymodel_attribute) {
        this.qualitymodel_attribute = qualitymodel_attribute;
    }

}