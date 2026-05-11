





import java.util.List;
import java.util.ArrayList;

public class ast_StepLiteral extends PrimitiveStepExpression {

    private int value;



    public ast_StepLiteral(
        int value    ) {
        super(
        );
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }


}