





import java.util.List;
import java.util.ArrayList;

public class NumberValue extends ValueType {

    private float value;



    public NumberValue(
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