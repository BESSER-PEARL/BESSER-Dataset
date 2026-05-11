





import java.util.List;
import java.util.ArrayList;

public class modelDsl_DoubleValue extends Value {

    private float value;



    public modelDsl_DoubleValue(
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