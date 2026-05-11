





import java.util.List;
import java.util.ArrayList;

public class eol_expression_BooleanExpression extends PrimitiveExpression {

    private boolean value;



    public eol_expression_BooleanExpression(
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