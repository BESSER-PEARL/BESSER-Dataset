





import java.util.List;
import java.util.ArrayList;

public class cal_ExpressionFloat extends ExpressionLiteral {

    private float value;



    public cal_ExpressionFloat(
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