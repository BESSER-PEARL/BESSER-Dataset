





import java.util.List;
import java.util.ArrayList;

public class behaviour_FloatConstantExpression extends ConstantExpression {

    private float value;



    public behaviour_FloatConstantExpression(
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