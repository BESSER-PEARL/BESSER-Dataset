





import java.util.List;
import java.util.ArrayList;

public class robo_expression_Literal extends Expr {

    private float value;



    public robo_expression_Literal(
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