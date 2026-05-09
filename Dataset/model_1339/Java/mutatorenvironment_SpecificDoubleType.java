





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_SpecificDoubleType extends DoubleType {

    private float value;



    public mutatorenvironment_SpecificDoubleType(
        float value    ) {
        super(
        );
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }


}