





import java.util.List;
import java.util.ArrayList;

public class model_values_Quantity extends Value {

    private String value;
    private String scalingFactor;



    public model_values_Quantity(
        String value,        String scalingFactor    ) {
        super(
        );
        this.value = value;
        this.scalingFactor = scalingFactor;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getScalingfactor() {
        return scalingFactor;
    }

    public void setScalingfactor(String scalingFactor) {
        this.scalingFactor = scalingFactor;
    }


}