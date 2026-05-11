





import java.util.List;
import java.util.ArrayList;

public class sipme_Capacity extends EnterpriseObject {

    private float value;
    private String unit;





    private sipme_Capability sipme_capability;


    public sipme_Capacity(
        float value,        String unit    ) {
        super(
        );
        this.value = value;
        this.unit = unit;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public sipme_Capability getSipme_capability() {
        return sipme_capability;
    }

    public void setSipme_capability(sipme_Capability sipme_capability) {
        this.sipme_capability = sipme_capability;
    }

}