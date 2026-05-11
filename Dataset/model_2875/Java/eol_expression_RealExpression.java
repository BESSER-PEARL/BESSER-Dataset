





import java.util.List;
import java.util.ArrayList;

public class eol_expression_RealExpression extends ComparableExpression, SummableExpression {

    private float value;



    public eol_expression_RealExpression(
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