





import java.util.List;
import java.util.ArrayList;

public class model_expression_IntConst extends IExpressionTerm {

    private int value;



    public model_expression_IntConst(
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