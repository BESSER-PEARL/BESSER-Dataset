





import java.util.List;
import java.util.ArrayList;

public class ir_FloatLiteral extends LiteralExpression {

    private float value;



    public ir_FloatLiteral(
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