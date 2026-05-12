





import java.util.List;
import java.util.ArrayList;

public class model_expression_BoolConst extends IExpressionTerm {

    private boolean value;



    public model_expression_BoolConst(
        boolean value    ) {
        super(
        );
        this.value = value;
    }


    public boolean getValue() {
        return value;
    }

    public void setValue(boolean value) {
        this.value = value;
    }


}