





import java.util.List;
import java.util.ArrayList;

public class query_DoubleExpression extends Expression {

    private float value;



    public query_DoubleExpression(
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