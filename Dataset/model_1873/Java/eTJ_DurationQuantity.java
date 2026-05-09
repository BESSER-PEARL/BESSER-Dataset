





import java.util.List;
import java.util.ArrayList;

public class eTJ_DurationQuantity extends GapLength, GapDuration {

    private float value;
    private String unit;





    private eTJ_Interval3 etj_interval3;




    private eTJ_Remaining etj_remaining;


    public eTJ_DurationQuantity(
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

    public eTJ_Interval3 getEtj_interval3() {
        return etj_interval3;
    }

    public void setEtj_interval3(eTJ_Interval3 etj_interval3) {
        this.etj_interval3 = etj_interval3;
    }
    public eTJ_Remaining getEtj_remaining() {
        return etj_remaining;
    }

    public void setEtj_remaining(eTJ_Remaining etj_remaining) {
        this.etj_remaining = etj_remaining;
    }

}