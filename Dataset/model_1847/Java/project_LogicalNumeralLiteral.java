





import java.util.List;
import java.util.ArrayList;

public class project_LogicalNumeralLiteral extends LogicalExpression {

    private float value;



    public project_LogicalNumeralLiteral(
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