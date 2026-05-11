





import java.util.List;
import java.util.ArrayList;

public class majordomo_ConstantValue extends ValueExpression {

    private float value;



    public majordomo_ConstantValue(
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