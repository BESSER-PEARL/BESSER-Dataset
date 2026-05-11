





import java.util.List;
import java.util.ArrayList;

public class expression_DoubleValue extends Term {

    private float value;



    public expression_DoubleValue(
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