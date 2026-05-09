





import java.util.List;
import java.util.ArrayList;

public class model_values_Quantity extends Value {

    private String scalingFactor;
    private String value;



    public model_values_Quantity(
        String scalingFactor,        String value    ) {
        super(
        );
        this.scalingFactor = scalingFactor;
        this.value = value;
    }


    public String getScalingfactor() {
        return scalingFactor;
    }

    public void setScalingfactor(String scalingFactor) {
        this.scalingFactor = scalingFactor;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}