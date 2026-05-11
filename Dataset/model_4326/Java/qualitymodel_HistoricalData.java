





import java.util.List;
import java.util.ArrayList;

public class qualitymodel_HistoricalData  {

    private String instant;
    private float value;





    private qualitymodel_Attribute qualitymodel_attribute;


    public qualitymodel_HistoricalData(
        String instant,        float value    ) {
        this.instant = instant;
        this.value = value;
    }


    public String getInstant() {
        return instant;
    }

    public void setInstant(String instant) {
        this.instant = instant;
    }
    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public qualitymodel_Attribute getQualitymodel_attribute() {
        return qualitymodel_attribute;
    }

    public void setQualitymodel_attribute(qualitymodel_Attribute qualitymodel_attribute) {
        this.qualitymodel_attribute = qualitymodel_attribute;
    }

}